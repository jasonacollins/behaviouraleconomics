#!/usr/bin/env python3
"""Add missing image dimensions to rendered Quarto HTML.

Quarto's Markdown image syntax often renders responsive images without
HTML width/height attributes. Adding dimensions lets the browser reserve
the image's aspect ratio before the file is loaded, reducing CLS.
"""

from __future__ import annotations

import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = PROJECT_ROOT / "_book"

IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)


class ImgParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.attrs: dict[str, str | None] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "img":
            self.attrs = {name.lower(): value for name, value in attrs}

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)


def image_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as image:
        header = image.read(32)

        if header.startswith(b"\x89PNG\r\n\x1a\n") and len(header) >= 24:
            width, height = struct.unpack(">II", header[16:24])
            return width, height

        if header[:6] in (b"GIF87a", b"GIF89a") and len(header) >= 10:
            width, height = struct.unpack("<HH", header[6:10])
            return width, height

        if header.startswith(b"\xff\xd8"):
            return jpeg_size(path)

        if header.startswith(b"RIFF") and header[8:12] == b"WEBP":
            return webp_size(path)

    return None


def jpeg_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as image:
        image.read(2)
        while True:
            marker_start = image.read(1)
            if not marker_start:
                return None
            if marker_start != b"\xff":
                continue

            marker = image.read(1)
            while marker == b"\xff":
                marker = image.read(1)
            if not marker:
                return None

            marker_value = marker[0]
            if marker_value in {0xD8, 0xD9}:
                continue
            if marker_value == 0xDA:
                return None

            length_bytes = image.read(2)
            if len(length_bytes) != 2:
                return None
            length = struct.unpack(">H", length_bytes)[0]
            if length < 2:
                return None

            if marker_value in {
                0xC0,
                0xC1,
                0xC2,
                0xC3,
                0xC5,
                0xC6,
                0xC7,
                0xC9,
                0xCA,
                0xCB,
                0xCD,
                0xCE,
                0xCF,
            }:
                segment = image.read(length - 2)
                if len(segment) >= 5:
                    height, width = struct.unpack(">HH", segment[1:5])
                    return width, height
                return None

            image.seek(length - 2, 1)


def webp_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as image:
        data = image.read(64)

    if len(data) < 30:
        return None

    chunk = data[12:16]

    if chunk == b"VP8X" and len(data) >= 30:
        width = int.from_bytes(data[24:27], "little") + 1
        height = int.from_bytes(data[27:30], "little") + 1
        return width, height

    if chunk == b"VP8 " and len(data) >= 30:
        width, height = struct.unpack("<HH", data[26:30])
        return width & 0x3FFF, height & 0x3FFF

    if chunk == b"VP8L" and len(data) >= 25:
        bits = int.from_bytes(data[21:25], "little")
        width = (bits & 0x3FFF) + 1
        height = ((bits >> 14) & 0x3FFF) + 1
        return width, height

    return None


def parse_img_attrs(tag: str) -> dict[str, str | None]:
    parser = ImgParser()
    parser.feed(tag)
    return parser.attrs


def resolve_local_src(html_file: Path, src: str | None) -> Path | None:
    if not src:
        return None

    parsed = urlsplit(src)
    if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
        return None

    candidate = (html_file.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(BOOK_DIR.resolve())
    except ValueError:
        return None

    if candidate.is_file():
        return candidate
    return None


def numeric_attr(value: str | None) -> int | None:
    if value is None:
        return None
    match = re.fullmatch(r"\s*(\d+)(?:\.0+)?\s*", value)
    if match:
        return int(match.group(1))
    return None


def attrs_to_add(attrs: dict[str, str | None], natural_width: int, natural_height: int) -> dict[str, int]:
    existing_width = numeric_attr(attrs.get("width"))
    existing_height = numeric_attr(attrs.get("height"))

    if existing_width and existing_height:
        return {}

    if existing_width and not existing_height:
        return {"height": round(existing_width * natural_height / natural_width)}

    if existing_height and not existing_width:
        return {"width": round(existing_height * natural_width / natural_height)}

    return {"width": natural_width, "height": natural_height}


def add_attrs(tag: str, attrs: dict[str, int]) -> str:
    if not attrs:
        return tag

    addition = "".join(f' {name}="{value}"' for name, value in attrs.items())
    self_closing = re.search(r"/\s*>$", tag) is not None
    base = re.sub(r"\s*/?>$", "", tag)
    closing = " />" if self_closing else ">"
    return f"{base}{addition}{closing}"


def process_html(html_file: Path) -> tuple[int, int]:
    html = html_file.read_text(encoding="utf-8")
    changed = 0
    checked = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed, checked

        tag = match.group(0)
        attrs = parse_img_attrs(tag)
        image = resolve_local_src(html_file, attrs.get("src"))
        if image is None:
            return tag

        checked += 1
        size = image_size(image)
        if size is None:
            return tag

        dimensions = attrs_to_add(attrs, *size)
        if not dimensions:
            return tag

        changed += 1
        return add_attrs(tag, dimensions)

    updated = IMG_RE.sub(replace, html)
    if updated != html:
        html_file.write_text(updated, encoding="utf-8")

    return checked, changed


def main() -> int:
    if not BOOK_DIR.is_dir():
        print(f"Image dimensions skipped: {BOOK_DIR} does not exist", file=sys.stderr)
        return 0

    checked_total = 0
    changed_total = 0
    for html_file in BOOK_DIR.rglob("*.html"):
        checked, changed = process_html(html_file)
        checked_total += checked
        changed_total += changed

    print(f"Image dimensions: checked {checked_total} local images, updated {changed_total} tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
