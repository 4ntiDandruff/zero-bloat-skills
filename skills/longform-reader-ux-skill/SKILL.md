---
name: longform-reader-ux-skill
description: "Longform technical article reading UX and CSS typography patterns: two-layer responsive table wrapper with gradient scroll cue, dynamic reading progress bar, hover-to-copy code blocks, accessible color-coded callouts, and zero-CLS image shimmer placeholders."
---

# Longform Reader UX Skill

Engineered typography, readability ergonomics, and micro-interactions for technical blogs, hardware documentation, post-mortems, and engineering wikis. Eliminates horizontal viewport breakage, layout shift (CLS), and mobile reading fatigue without heavy JavaScript runtimes.

Battle-tested in the **Megapass Intra Solusindo** SSR knowledge engine (`megapass.web.id/blog/`).

---

## 1. Two-Layer Responsive Table with Dynamic Gradient Scroll Cue

### The Physical Problem
Standard HTML tables in markdown often exceed mobile screen width. Default `overflow-x: auto` provides no visual indication that columns exist off-screen, leading to hidden data and accidental page scrolling.

### The Circuit Solution
A two-layer wrapper: outer container manages layout and pinned gradient shadow cue; inner container handles touch scrolling. The shadow cue automatically fades away when the user reaches the end of the table:

```html
<!-- HTML Structure -->
<div class="table-outer" id="tableWrapper">
  <div class="table-inner">
    <table>
      <thead>
        <tr>
          <th>Power Rail</th>
          <th>Nominal Voltage</th>
          <th>Standby Current</th>
          <th>Symptom on Short</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>VIN / BATT+</td>
          <td>19.0V - 19.5V</td>
          <td>10mA - 25mA</td>
          <td>Adapter shutoff / pulsing</td>
        </tr>
        <tr>
          <td>+3VALW / +5VALW</td>
          <td>3.3V / 5.0V</td>
          <td>30mA - 70mA</td>
          <td>No power button response</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

```css
/* Zero-Bloat Pure CSS */
.table-outer {
  position: relative;
  overflow: hidden;
  margin-bottom: 1.25rem;
}

/* Gradient shadow indicator pinned to right edge */
.table-outer::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 2.5rem;
  pointer-events: none;
  background: linear-gradient(to right, transparent, rgba(11, 18, 32, 0.85));
  z-index: 2;
  transition: opacity 0.2s ease;
}

/* Hide cue when scrolled to maximum right */
.table-outer.scrolled-end::after {
  opacity: 0;
}

.table-inner {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
}

th {
  text-align: left;
  padding: 0.625rem 1rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.15);
  color: #E2E8F0;
  font-weight: 600;
  white-space: nowrap;
}

td {
  padding: 0.625rem 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  color: #CBD5E1;
}

tr:nth-child(even) td {
  background: rgba(255, 255, 255, 0.02);
}
```

```javascript
// Lightweight scroll observer (10 LOC, 0% CPU idle)
document.querySelectorAll('.table-outer').forEach(function(outer) {
  var inner = outer.querySelector('.table-inner');
  if (!inner) return;
  function checkEnd() {
    var isEnd = inner.scrollLeft + inner.clientWidth >= inner.scrollWidth - 4;
    outer.classList.toggle('scrolled-end', isEnd);
  }
  inner.addEventListener('scroll', checkEnd, { passive: true });
  checkEnd();
});
```

---

## 2. Dynamic Reading Progress Bar

A hairline progress indicator fixed to the top viewport edge. Computes exact scroll percentage along the article body, giving visual reading context:

```html
<div id="readProgress" aria-hidden="true"></div>
```

```css
#readProgress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, #22D3EE, #06B6D4);
  z-index: 9999;
  transition: width 0.1s linear;
  pointer-events: none;
}
```

```javascript
window.addEventListener('scroll', function() {
  var bar = document.getElementById('readProgress');
  if (!bar) return;
  var doc = document.documentElement;
  var top = doc.scrollTop || document.body.scrollTop;
  var total = (doc.scrollHeight || document.body.scrollHeight) - doc.clientHeight;
  var pct = total > 0 ? (top / total) * 100 : 0;
  bar.style.width = Math.min(100, Math.max(0, pct)) + '%';
}, { passive: true });
```

---

## 3. Hover-to-Copy Code Block

Eliminates tedious manual text selection on code snippets and terminal commands. The button remains completely transparent until cursor enters the code container:

```html
<div class="pre-wrap">
  <button type="button" class="copy-code" aria-label="Salin kode">Salin</button>
  <pre><code># Test power rails via flashrom
flashrom -p ch341a_spi -r bios_dump.bin</code></pre>
</div>
```

```css
.pre-wrap {
  position: relative;
  margin-bottom: 1.25rem;
}

.pre-wrap pre {
  background: #0B1220;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  padding: 1rem;
  overflow-x: auto;
  font-size: 0.85rem;
  color: #E2E8F0;
}

.pre-wrap .copy-code {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  padding: 0.25rem 0.6rem;
  border-radius: 0.375rem;
  background: rgba(255, 255, 255, 0.08);
  color: #94A3B8;
  font-size: 0.75rem;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.1);
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s, background 0.2s, color 0.2s, transform 0.1s;
}

.pre-wrap:hover .copy-code,
.pre-wrap:focus-within .copy-code {
  opacity: 1;
}

.pre-wrap .copy-code:hover {
  background: rgba(34, 211, 238, 0.2);
  color: #22D3EE;
}

.pre-wrap .copy-code:active {
  transform: scale(0.96);
}

.pre-wrap .copy-code.copied {
  background: rgba(5, 150, 105, 0.35);
  color: #34D399;
  border-color: rgba(52, 211, 153, 0.4);
}
```

```javascript
document.querySelectorAll('.pre-wrap').forEach(function(wrap) {
  var btn = wrap.querySelector('.copy-code');
  var code = wrap.querySelector('code') || wrap.querySelector('pre');
  if (!btn || !code) return;
  btn.addEventListener('click', function() {
    navigator.clipboard.writeText(code.innerText.trim()).then(function() {
      btn.textContent = 'Tersalin!';
      btn.classList.add('copied');
      setTimeout(function() {
        btn.textContent = 'Salin';
        btn.classList.remove('copied');
      }, 2000);
    });
  });
});
```

---

## 4. Technical Callout System

Color-coded contextual alerts designed with high contrast for dark reading palettes. Never use generic low-contrast gray boxes:

```html
<!-- Info Callout -->
<div class="callout callout-info">
  <strong>Informasi Skematik</strong>
  Pastikan tegangan pada pin 8 IC BIOS bernilai stabil 3.3V sebelum menghubungkan probe programmer.
</div>

<!-- Warning Callout -->
<div class="callout callout-warn">
  <strong>Peringatan Tegangan</strong>
  Dilarang menyuntik tegangan melebihi batas toleransi chip VCC (maksimal 1.0V pada jalur CPU core).
</div>

<!-- Tip Callout -->
<div class="callout callout-tip">
  <strong>Rekomendasi Teknisi</strong>
  Gunakan flux jenis NC (No-Clean) bermutu tinggi untuk mempermudah pembersihan residu pasca-solder.
</div>

<!-- Danger Callout -->
<div class="callout callout-danger">
  <strong>Bahaya Arus Balik</strong>
  Lepaskan konektor baterai internal sebelum menyentuh konektor fleksibel layar LCD!
</div>
```

```css
.callout {
  padding: 0.85rem 1.15rem;
  border-radius: 0.75rem;
  margin: 1.25rem 0;
  font-size: 0.9375rem;
  line-height: 1.7;
  border-left: 3px solid;
}

.callout strong {
  display: block;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.callout-info {
  background: rgba(34, 211, 238, 0.08);
  border-color: #22D3EE;
  color: #E2E8F0;
}

.callout-warn {
  background: rgba(234, 179, 8, 0.08);
  border-color: #EAB308;
  color: #E2E8F0;
}

.callout-tip {
  background: rgba(34, 197, 94, 0.08);
  border-color: #22C55E;
  color: #E2E8F0;
}

.callout-danger {
  background: rgba(239, 68, 68, 0.08);
  border-color: #EF4444;
  color: #E2E8F0;
}
```

---

## 5. Shimmer Skeleton Loading (Zero-CLS)

Prevents jarring layout shift (Cumulative Layout Shift = 0) when high-resolution boardview diagrams or workshop images are loading over mobile networks:

```html
<div class="img-skeleton">
  <div class="shimmer"></div>
  <img src="/assets/schematic-rail.jpg" alt="Skema Jalur Tegangan" loading="lazy" onload="this.classList.add('loaded')">
</div>
```

```css
.img-skeleton {
  position: relative;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 0.75rem;
  min-height: 180px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  margin: 1.5rem 0;
}

.img-skeleton .shimmer {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 25%, rgba(255, 255, 255, 0.04) 50%, transparent 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.img-skeleton img {
  display: block;
  width: 100%;
  height: auto;
  opacity: 0;
  transition: opacity 0.4s ease;
  position: relative;
  z-index: 1;
}

.img-skeleton img.loaded {
  opacity: 1;
}

.img-skeleton img.loaded + .shimmer {
  display: none;
}
```

---

## 6. Layout Rules & Mobile Clearance

* **Fixed Navbar Clearance**: All anchor heading targets (`h2`, `h3`) must have `scroll-margin-top: 5rem` to prevent sticky headers from obscuring the title on in-page navigation clicks.
* **Word-Break Safeguard**: Always apply `.article-body { overflow-wrap: break-word; word-break: break-word; }` to protect against long URLs or raw memory addresses (`0x7fff5fbff8a0`) from pushing container bounds.
* **Readability Measure**: Restrict text container width to `max-w-3xl` (approx. 65-75 characters per line) and maintain `line-height: 1.8` for dense technical copy.
