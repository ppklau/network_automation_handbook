import mermaid from 'mermaid';

function getTheme(): 'dark' | 'default' {
  return document.documentElement.dataset.theme === 'dark' ? 'dark' : 'default';
}

// ── Modal ─────────────────────────────────────────────────────────────────────

function getOrCreateModal(): HTMLElement {
  let modal = document.getElementById('mermaid-modal');
  if (modal) return modal;

  modal = document.createElement('div');
  modal.id = 'mermaid-modal';
  modal.setAttribute('hidden', '');
  modal.innerHTML = `
    <div class="mermaid-modal-backdrop"></div>
    <div class="mermaid-modal-inner">
      <button class="mermaid-modal-close" aria-label="Close diagram">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"
             fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
          <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
      <div class="mermaid-modal-diagram"></div>
    </div>
  `;
  document.body.appendChild(modal);
  modal.querySelector('.mermaid-modal-backdrop')!.addEventListener('click', closeModal);
  modal.querySelector('.mermaid-modal-close')!.addEventListener('click', closeModal);
  return modal;
}

function openModal(svg: SVGElement) {
  const modal = getOrCreateModal();
  const diagramEl = modal.querySelector('.mermaid-modal-diagram')!;
  diagramEl.innerHTML = '';
  diagramEl.appendChild(svg.cloneNode(true));
  modal.removeAttribute('hidden');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('mermaid-modal');
  if (modal) modal.setAttribute('hidden', '');
  document.body.style.overflow = '';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

// ── Expand button — event delegation ─────────────────────────────────────────

document.addEventListener('click', (e: MouseEvent) => {
  const btn = (e.target as Element).closest('.mermaid-expand-btn');
  if (!btn) return;
  const svg = btn.closest('.mermaid-wrapper')?.querySelector('svg');
  if (svg) openModal(svg as SVGElement);
});

// ── Render ────────────────────────────────────────────────────────────────────

async function renderMermaid() {
  // Reset any previously rendered diagrams so they re-render with the current theme
  document.querySelectorAll('.mermaid[data-processed]').forEach((el) => {
    el.removeAttribute('data-processed');
    const source = el.getAttribute('data-source');
    if (source) el.textContent = source;
  });

  // Save original source before mermaid replaces the element content
  document.querySelectorAll('.mermaid:not([data-source])').forEach((el) => {
    el.setAttribute('data-source', el.textContent ?? '');
  });

  mermaid.initialize({
    startOnLoad: false,
    theme: getTheme(),
    securityLevel: 'loose',
    fontFamily: 'inherit',
  });

  await mermaid.run({ querySelector: '.mermaid' });
}

document.addEventListener('astro:page-load', renderMermaid);

// Re-render when the user switches light/dark theme
const observer = new MutationObserver((mutations) => {
  for (const m of mutations) {
    if (m.attributeName === 'data-theme') {
      renderMermaid();
      break;
    }
  }
});
observer.observe(document.documentElement, { attributes: true });
