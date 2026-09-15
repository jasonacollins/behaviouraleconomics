// Match Cloudflare Pages' public URLs after Quarto generates canonical tags
// and the sitemap. Run via project.post-render, with the site URL as argument.
// Uses Quarto's bundled Deno runtime; no packages or network access required.
const site = new URL(Deno.args[0]);
const output = Deno.env.get("QUARTO_PROJECT_OUTPUT_DIR");
if (!output) throw new Error("Run this script as a Quarto post-render hook.");

function normalize(value: string): string {
  const url = new URL(value);
  // Preserve explicit cross-domain canonicals (for syndicated articles).
  if (url.origin !== site.origin) return value;
  const path = url.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
  if (path === url.pathname) return value;
  url.pathname = path;
  return url.href;
}

async function processDirectory(directory: string): Promise<void> {
  for await (const entry of Deno.readDir(directory)) {
    const path = `${directory}/${entry.name}`;
    if (entry.isDirectory) {
      await processDirectory(path);
    } else if (entry.isFile && (entry.name.endsWith(".html") || entry.name === "sitemap.xml")) {
      const original = await Deno.readTextFile(path);
      const updated = entry.name === "sitemap.xml"
        ? original.replace(/(<loc>)([^<]+)(<\/loc>)/g,
          (_, start, url, end) => start + normalize(url) + end)
        : original.replace(/<link\b[^>]*>/gi, (tag) => {
          if (!/\brel\s*=\s*(["'])canonical\1/i.test(tag)) return tag;
          return tag.replace(/(\bhref\s*=\s*)(["'])(.*?)\2/i,
            (_, prefix, quote, url) => prefix + quote + normalize(url) + quote);
        });
      if (updated !== original) await Deno.writeTextFile(path, updated);
    }
  }
}

await processDirectory(output);
