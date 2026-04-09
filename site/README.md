# Network Automation Handbook — Site

Astro + Starlight documentation site.

## Development

```bash
npm install
npx playwright install chromium   # one-time: download headless browser for diagram rendering
npx astro dev                     # local dev server (runs sync automatically)
npx astro build                   # production build → ./dist
```

## Static diagram images (Gantt charts)

Mermaid's Gantt renderer reads `parentElement.offsetWidth` at render time and
draws the chart at that pixel width. In a narrow content column all the tasks
and axis labels collapse on top of each other. Setting `gantt.useWidth` /
`useMaxWidth: false` fixes the width but then the whole page layout overflows
unpleasantly. Pre-rendering to SVG and embedding with `overflow-x: auto` on
the figure wrapper is the cleanest workaround.

### How it works (automated)

`scripts/sync-content.mjs` handles this automatically as part of every sync:

1. Any ` ```mermaid ` block whose content starts with `gantt` is detected
   during the chapter sync pass.
2. The block is replaced in the synced docs with a `<figure
   class="roadmap-figure">` containing light/dark `<img>` tags.
3. After all chapters are copied, Playwright (headless Chromium) renders each
   gantt to an SVG — once with `theme: "default"` (light) and once with
   `theme: "dark"` — using the local `mermaid` package so no network access
   is needed.
4. The SVGs are written to `public/diagrams/<slug>-gantt-<n>-{light,dark}.svg`
   where `<slug>` is the chapter directory name (minus leading `XX-`).

Gantt SVGs in `public/diagrams/` are **generated artefacts** — do not edit
them by hand. Edit the `gantt` code block in the source `chapter.md` and
re-run `npm run sync` (or `npm run dev`/`npm run build`).

If Playwright is not installed the script warns and falls back to client-side
Mermaid rendering for gantt charts (legible but may look squished).

### GitHub Actions

The deploy workflow already installs Playwright Chromium before building, so
diagram rendering works in CI without any extra steps.
