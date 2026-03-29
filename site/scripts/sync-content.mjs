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

import { copyFileSync, mkdirSync, rmSync, readdirSync, existsSync } from 'fs';
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
      copyFileSync(srcPath, destPath);
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

console.log(`sync-content: copied ${copied} chapter files → src/content/docs/`);
