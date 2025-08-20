# CLAUDE.md

This file provides guidance to agents when working with code in this repository.

## Build Commands

This is a Quarto book project for behavioural economics course notes. Common commands:

- `quarto render` - Render the entire book to HTML/PDF output in `_book` directory
- `quarto preview` - Start development server with live reload at http://localhost:3000
- `quarto publish` - Publish to configured hosting platform

## Project Structure

This is a Quarto book project with the following architecture:

- **Content Organization**: Book is structured in themed parts (economic-foundations, decision-making-under-risk, prospect-theory, etc.) with each part containing multiple chapters
- **Source Files**: All content is in `.qmd` (Quarto Markdown) files that combine markdown text with embedded R code for generating figures and calculations
- **Configuration**: `_quarto.yml` contains the book structure, chapter ordering, and rendering settings
- **Assets**: Images are stored in `img/` subdirectories within each topic folder
- **Output**: Rendered content goes to `_book/` directory (HTML) and can also generate PDF
- **Caching**: `_freeze/` directory contains cached computation results to speed up rendering

## Key Files

- `_quarto.yml` - Main configuration file defining book structure and rendering options
- `index.qmd` - Book homepage/introduction
- `references.bib` - Bibliography for academic citations
- `styles.css` - Custom CSS styling
- `apa-no-ampersand.csl` - Citation style file

## Content Development

When working with content:
- Each chapter is a separate `.qmd` file with front matter and markdown content
- R code chunks are used for generating mathematical figures and calculations
- Cross-references use Quarto's native referencing system
- Academic citations reference the central `references.bib` file
- Mathematical notation uses LaTeX syntax rendered via KaTeX

## Rendering Notes

- The project uses freeze mode (`execute: freeze: auto`) to cache computational results
- Figures are generated programmatically using R code chunks
- Both HTML and PDF output formats are configured
- The HTML version includes interactive features like code folding and search