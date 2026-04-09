#!/usr/bin/env node
/**
 * sync-content.mjs
 *
 * Copies chapter.md files from the repo root into src/content/docs/,
 * preserving the directory structure.
 *
 * Only chapter.md files are copied — README.md, templates, examples,
 * assets, and the site/ directory itself are excluded. The docs directory
 * is cleared before each sync so deleted chapters do not persist.
 *
 * Mermaid gantt code blocks are detected during sync and replaced with
 * <figure> elements referencing pre-rendered SVGs. The SVGs are rendered
 * via Playwright (headless Chromium) using the local mermaid package so
 * that no network access or separate mermaid-cli install is needed.
 * Playwright must be installed (`playwright` devDependency) and its
 * Chromium binary must be available (`npx playwright install chromium`).
 * If Playwright is unavailable the script falls back to leaving the gantt
 * blocks as-is for client-side rendering.
 *
 * Run automatically via the prebuild/dev scripts in package.json.
 */

import { copyFileSync, mkdirSync, rmSync, readdirSync, readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname, relative, sep } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
// site/scripts/ → site/ → repo root
const HANDBOOK_DIR = join(__dirname, '..', '..');
const DOCS_DIR = join(__dirname, '..', 'src', 'content', 'docs');
const DIAGRAMS_DIR = join(__dirname, '..', 'public', 'diagrams');
const MERMAID_JS_PATH = join(__dirname, '..', 'node_modules', 'mermaid', 'dist', 'mermaid.min.js');
const BASE_PATH = '/network_automation_handbook';

// Directories at the repo root that should not become doc pages
const EXCLUDED_DIRS = new Set(['assets', 'templates', 'examples', 'site', '.github']);

// Gantt diagrams collected during sync for deferred rendering
const pendingDiagrams = []; // { name, source }
const ganttCounters = {};   // dirSlug → count (for stable per-file naming)

let copied = 0;

// ── Gantt block replacement ──────────────────────────────────────────────────

/**
 * Replace ```mermaid gantt … ``` blocks with <figure> HTML referencing
 * pre-rendered SVGs. Records each block in pendingDiagrams for later rendering.
 */
function replaceGanttBlocks(content, dirSlug) {
  return content.replace(
    /```mermaid\r?\n(gantt[\s\S]*?)```/g,
    (_match, mermaidSrc) => {
      ganttCounters[dirSlug] = (ganttCounters[dirSlug] || 0) + 1;
      const name = `${dirSlug}-gantt-${ganttCounters[dirSlug]}`;
      pendingDiagrams.push({ name, source: mermaidSrc.trim() });
      const base = `${BASE_PATH}/diagrams/${name}`;
      return [
        '<figure class="roadmap-figure not-content">',
        `<img class="theme-light-only" src="${base}-light.svg" alt="Gantt chart" />`,
        `<img class="theme-dark-only" src="${base}-dark.svg" alt="Gantt chart" />`,
        '</figure>',
      ].join('\n');
    }
  );
}

// ── Chapter sync ─────────────────────────────────────────────────────────────

function sync(srcDir, destDir) {
  const entries = readdirSync(srcDir, { withFileTypes: true });

  for (const entry of entries) {
    if (entry.name.startsWith('.')) continue;

    const srcPath = join(srcDir, entry.name);
    const destPath = join(destDir, entry.name);

    if (entry.isDirectory()) {
      // Skip excluded top-level directories
      if (srcDir === HANDBOOK_DIR && (EXCLUDED_DIRS.has(entry.name) || entry.name.startsWith('.'))) continue;
      mkdirSync(destPath, { recursive: true });
      sync(srcPath, destPath);
    } else if (entry.name === 'chapter.md') {
      mkdirSync(destDir, { recursive: true });
      let content = readFileSync(srcPath, 'utf8');

      // Derive the top-level chapter directory slug for diagram naming
      const relToHandbook = relative(HANDBOOK_DIR, srcDir);
      const topDirName = relToHandbook.split(sep)[0] || 'general';
      const dirSlug = topDirName.replace(/^\d+-/, '');

      // Replace gantt blocks with static figure HTML before other rewrites
      content = replaceGanttBlocks(content, dirSlug);

      // Rewrite relative examples/ links to absolute GitHub URLs
      content = content.replace(
        /\]\((?:\.\.\/)*examples(\/[^)"]*)?\)/g,
        '](https://github.com/ppklau/network_automation_handbook/tree/main/examples$1)'
      );
      // Strip .md extension from remaining relative links so Starlight clean URLs resolve correctly
      content = content.replace(/(\]\([^)#]+)\.md((?:#[^)]*)?\))/g, '$1$2');
      // Rewrite ../templates/slug → absolute path with base prefix.
      // Relative links break because the trailing-slash behaviour differs
      // between local dev and GitHub Pages, changing how the browser resolves
      // the relative path. Absolute paths avoid this entirely.
      content = content.replace(
        /\]\(\.\.\/templates\/([^)]+)\)/g,
        `](${BASE_PATH}/templates/$1/)`
      );
      writeFileSync(destPath, content);
      copied++;
    }
  }
}

// Clear the docs directory before syncing to avoid stale files
if (existsSync(DOCS_DIR)) {
  rmSync(DOCS_DIR, { recursive: true, force: true });
}
mkdirSync(DOCS_DIR, { recursive: true });

sync(HANDBOOK_DIR, DOCS_DIR);

// ── Copy templates ─────────────────────────────────────────────────────────────
const TEMPLATES_SRC = join(HANDBOOK_DIR, 'templates');
const TEMPLATES_DEST = join(DOCS_DIR, 'templates');

let templatesCopied = 0;

// Groups templates by filename prefix for the index page
const TEMPLATE_GROUPS = [
  { prefix: 'business',      label: 'Business Alignment' },
  { prefix: 'maturity',      label: 'Maturity Assessment' },
  { prefix: 'roadmap',       label: 'Transformation Roadmap' },
  { prefix: 'tool',          label: 'Tooling Strategy' },
  { prefix: 'sot',           label: 'Architecture & Design' },
  { prefix: 'repository',    label: 'Architecture & Design' },
  { prefix: 'architecture',  label: 'Architecture & Design' },
  { prefix: 'incident',      label: 'Operations Automation' },
  { prefix: 'auto-remediation', label: 'Operations Automation' },
  { prefix: 'dashboard',     label: 'Dashboards & Metrics' },
  { prefix: 'a-team',        label: 'People & Skills' },
  { prefix: 'value-pillar',  label: 'People & Skills' },
];

function groupFor(filename) {
  const name = filename.replace('.md', '');
  for (const g of TEMPLATE_GROUPS) {
    if (name.startsWith(g.prefix)) return g.label;
  }
  return 'Other';
}

// Collected during copyTemplates for index generation
const collectedTemplates = [];

function copyTemplates(srcDir, destDir, relDir = '') {
  const entries = readdirSync(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name === 'README.md') continue;
    const srcPath = join(srcDir, entry.name);
    const destPath = join(destDir, entry.name);
    if (entry.isDirectory()) {
      mkdirSync(destPath, { recursive: true });
      copyTemplates(srcPath, destPath, relDir ? `${relDir}/${entry.name}` : entry.name);
    } else if (entry.name.endsWith('.md')) {
      const content = readFileSync(srcPath, 'utf8');
      // Extract title from first H1 heading
      const h1 = content.match(/^#\s+(.+)$/m);
      const title = h1 ? h1[1].trim() : entry.name.replace('.md', '').replace(/-/g, ' ');
      // Strip .md extension from relative links so Starlight clean URLs resolve correctly
      const rewritten = content.replace(/(\]\([^)#]+)\.md((?:#[^)]*)?\))/g, '$1$2');
      // Only prepend frontmatter if not already present
      const out = rewritten.startsWith('---')
        ? rewritten
        : `---\ntitle: "${title.replace(/"/g, '\\"')}"\n---\n\n${rewritten}`;
      mkdirSync(destDir, { recursive: true });
      writeFileSync(destPath, out);
      templatesCopied++;
      // Record for index generation (top-level templates only)
      if (!relDir) {
        collectedTemplates.push({ filename: entry.name, title, group: groupFor(entry.name) });
      }
    }
  }
}

function buildTemplateIndex() {
  // Sort templates alphabetically within each group
  collectedTemplates.sort((a, b) => a.title.localeCompare(b.title));

  // Collect unique groups in defined order
  const groupOrder = [...new Set(TEMPLATE_GROUPS.map(g => g.label)), 'Other'];
  const byGroup = {};
  for (const t of collectedTemplates) {
    (byGroup[t.group] ??= []).push(t);
  }

  let body = '';
  for (const groupLabel of groupOrder) {
    if (!byGroup[groupLabel]) continue;
    body += `## ${groupLabel}\n\n`;
    for (const t of byGroup[groupLabel]) {
      const slug = t.filename.replace('.md', '');
      body += `- [${t.title}](${BASE_PATH}/templates/${slug}/)\n`;
    }
    body += '\n';
  }

  const index = `---
title: Templates
description: Ready-to-use templates for every stage of your network automation programme.
---

These templates are ready-to-use starting points for the assessments, plans, and artefacts described throughout the handbook. Each template is in Markdown format — copy it into your own repository and adapt it to your organisation.

${body}`;

  writeFileSync(join(TEMPLATES_DEST, 'index.md'), index);
}

if (existsSync(TEMPLATES_SRC)) {
  mkdirSync(TEMPLATES_DEST, { recursive: true });
  copyTemplates(TEMPLATES_SRC, TEMPLATES_DEST);
  buildTemplateIndex();
}

console.log(`sync-content: copied ${copied} chapter files + ${templatesCopied} templates → src/content/docs/`);

// ── Gantt SVG rendering ──────────────────────────────────────────────────────

/**
 * Render a mermaid diagram to SVG using a Playwright page.
 * mermaid is loaded from the local node_modules bundle so no network is needed.
 */
async function renderMermaid(page, source, theme) {
  await page.setContent('<!DOCTYPE html><html><body></body></html>');
  await page.addScriptTag({ path: MERMAID_JS_PATH });
  return page.evaluate(async ({ source, theme }) => {
    window.mermaid.initialize({
      startOnLoad: false,
      theme,
      gantt: { useWidth: 1100, useMaxWidth: false },
    });
    const { svg } = await window.mermaid.render('g1', source);
    return svg;
  }, { source, theme });
}

async function renderDiagrams() {
  if (pendingDiagrams.length === 0) return;

  let chromium;
  try {
    ({ chromium } = await import('playwright'));
  } catch {
    console.warn(
      'sync-content: playwright not available — gantt charts will use client-side rendering.\n' +
      '  Run: npx playwright install chromium'
    );
    return;
  }

  mkdirSync(DIAGRAMS_DIR, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage();
  let rendered = 0;

  for (const { name, source } of pendingDiagrams) {
    for (const [theme, suffix] of [['default', 'light'], ['dark', 'dark']]) {
      const outPath = join(DIAGRAMS_DIR, `${name}-${suffix}.svg`);
      try {
        const svg = await renderMermaid(page, source, theme);
        writeFileSync(outPath, svg);
        rendered++;
      } catch (err) {
        console.error(`sync-content: failed to render ${name}-${suffix}.svg — ${err.message}`);
      }
    }
  }

  await browser.close();
  console.log(`sync-content: rendered ${rendered} gantt SVG(s) → public/diagrams/`);
}

await renderDiagrams();
