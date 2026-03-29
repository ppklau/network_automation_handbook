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
 * Run automatically via the prebuild/dev scripts in package.json.
 */

import { copyFileSync, mkdirSync, rmSync, readdirSync, readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
// site/scripts/ → site/ → repo root
const HANDBOOK_DIR = join(__dirname, '..', '..');
const DOCS_DIR = join(__dirname, '..', 'src', 'content', 'docs');

// Directories at the repo root that should not become doc pages
const EXCLUDED_DIRS = new Set(['assets', 'templates', 'examples', 'site', '.github']);

let copied = 0;

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
      // Rewrite relative examples/ links to absolute GitHub URLs
      content = content.replace(
        /\]\((?:\.\.\/)*examples(\/[^)"]*)?\)/g,
        '](https://github.com/ppklau/network_automation_handbook/tree/main/examples$1)'
      );
      // Strip .md extension from remaining relative links so Starlight clean URLs resolve correctly
      content = content.replace(/(\]\([^)#]+)\.md((?:#[^)]*)?\))/g, '$1$2');
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

// ── Copy templates ─────────────────────────────────────────────────────────
const TEMPLATES_SRC = join(HANDBOOK_DIR, 'templates');
const TEMPLATES_DEST = join(DOCS_DIR, 'templates');

let templatesCopied = 0;

function copyTemplates(srcDir, destDir) {
  const entries = readdirSync(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name === 'README.md') continue;
    const srcPath = join(srcDir, entry.name);
    const destPath = join(destDir, entry.name);
    if (entry.isDirectory()) {
      mkdirSync(destPath, { recursive: true });
      copyTemplates(srcPath, destPath);
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
    }
  }
}

if (existsSync(TEMPLATES_SRC)) {
  copyTemplates(TEMPLATES_SRC, TEMPLATES_DEST);
}

console.log(`sync-content: copied ${copied} chapter files + ${templatesCopied} templates → src/content/docs/`);
