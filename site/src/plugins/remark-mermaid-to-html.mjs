/**
 * Remark plugin: transform ```mermaid code blocks into a .mermaid-wrapper div
 * with a raw <pre class="mermaid"> element and a "View full size" expand button.
 *
 * Running as a remark plugin ensures mermaid blocks are converted before
 * expressive-code gets a chance to syntax-highlight them.
 */

const EXPAND_SVG = `<svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>`;

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function walk(node, parent, index) {
  if (node.type === 'code' && node.lang === 'mermaid') {
    parent.children[index] = {
      type: 'html',
      value: `<div class="mermaid-wrapper not-content">\n<pre class="mermaid">${escapeHtml(node.value)}</pre>\n<button class="mermaid-expand-btn" aria-label="View diagram full size">${EXPAND_SVG} View full size</button>\n</div>`,
    };
    return;
  }
  if (node.children) {
    for (let i = 0; i < node.children.length; i++) {
      walk(node.children[i], node, i);
    }
  }
}

export default function remarkMermaidToHtml() {
  return function (tree) {
    if (tree.children) {
      for (let i = 0; i < tree.children.length; i++) {
        walk(tree.children[i], tree, i);
      }
    }
  };
}
