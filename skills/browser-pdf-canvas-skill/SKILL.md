---
name: browser-pdf-canvas-skill
description: "Custom PDF.js HTML5 Canvas viewer architecture: lazy virtualized rendering via IntersectionObserver, elimination of ghost-scroll feedback loops, and isolated in-document text search."
---

# Browser PDF Canvas Engine Skill

Web architectural pattern for embedding large technical documents (50-150 page boardview schematics) without relying on browser native iframes that restrict DOM interaction and event handling.

---

## 1. Native Iframe Limitations

- Native `<iframe>` PDF viewers execute within isolated browser sandboxes. Mouse events (dragging, panning, precise selection, wheel zoom) are captured internally and hidden from parent JavaScript.
- Native `Ctrl+F` searches the entire browser DOM (including navigation menus, sidebars, and AI chat panels) rather than restricting queries to technical schematic text.

---

## 2. Virtualized Lazy Rendering via HTML5 Canvas

Rendering all pages of a 100+ page schematic concurrently crashes browser tabs. Use virtualized viewport observers:

```javascript
// 1. Create lightweight empty placeholder div preserving document scroll geometry
const placeholder = document.createElement('div');
placeholder.className = 'pdf-page-container relative';
placeholder.dataset.pageNum = pageNum;
placeholder.style.minHeight = `${estimatedHeight}px`;

// 2. Attach IntersectionObserver for viewport-driven rendering
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    const pageNumber = parseInt(entry.target.dataset.pageNum, 10);
    if (entry.isIntersecting) {
      renderPageCanvas(pageNumber, entry.target);
    } else {
      // Purge non-visible canvas to conserve system memory
      cleanupPageCanvas(entry.target);
    }
  });
}, {
  rootMargin: '400px 0px' // Buffer pre-fetching 1 page ahead
});
```

---

## 3. Eliminating Ghost-Scroll Loops (`jumpTargetRef` Lock)

### Root Cause:
Observer identifies a new page -> invokes `onPageChange(p)` -> parent state updates -> triggers `scrollIntoView({ behavior: 'smooth' })` -> animated scroll travels past adjacent pages -> observer triggers repeatedly, creating an uncontrollable jumping loop.

### Dual-Fuse Circuit Breaker (`lastPageRef` + `jumpTargetRef`):
```javascript
let isProgrammaticScroll = false;
let targetPage = null;

function navigateToPage(pageNum) {
  isProgrammaticScroll = true;
  targetPage = pageNum;
  
  const el = document.querySelector(`[data-page-num="${pageNum}"]`);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}

// Inside IntersectionObserver handler:
if (isProgrammaticScroll) {
  if (detectedPage === targetPage) {
    isProgrammaticScroll = false; // Release lock upon reaching destination
  }
  return; // Suppress observer events during programmatic transition
}
```

---

## 4. Isolated In-Document Text Search

Instead of relying on browser global search:
1. Call `page.getTextContent()` per page to index exact string matches and coordinates.
2. Build an in-memory page hit table (`[{ page: 14, matches: 3 }]`).
3. Provide dedicated Previous/Next controls on the canvas toolbar to jump directly to matching schematic nodes.
