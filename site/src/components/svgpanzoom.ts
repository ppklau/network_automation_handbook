import "@beoe/pan-zoom/css/PanZoomUi.css";
import { PanZoomUi } from "@beoe/pan-zoom";

// for mermaid diagrams rendered by @beoe/rehype-mermaid
// output structure: <figure class="beoe mermaid"><svg>...</svg></figure>
document.querySelectorAll(".beoe").forEach((container) => {
  const element = container.firstElementChild;
  if (!element) return;
  // @ts-expect-error
  new PanZoomUi({ element, container }).on();
});
