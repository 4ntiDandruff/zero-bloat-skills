---
name: mobile-thumb-ergonomics-skill
description: "Styling-agnostic mobile viewport physics, handheld thumb-zone geometry, and layout architecture for single-handed smartphone web and PWA applications: bottom-anchored actions, bottom sheet drawers, 44px touch targets, 100dvh safe-area clearance, virtual keypad drawers, and horizontal swipe carousels decoupled from visual design themes."
---

# Universal Mobile Thumb Ergonomics Skill (Handheld Viewport Architecture)

Architecture, physical layout formulas, and layout engineering patterns for building thumb-friendly mobile web applications and PWAs across any domain.

> **Separation of Concerns (Pemisahan Peran Arsitektur)**:
> - **Skill Ini (`mobile-thumb-ergonomics-skill`)**: Bertindak sebagai **Rangka & Geometri (Skeleton & Muscle)**: Mengatur fisika viewport ponsel (`100dvh`), zona jangkauan jempol, clearance dock (`pb-32`), safe-area hardware, target sentuh 44px, drawer bottom sheet, dan pencegahan bug browser mobile.
> - **Skill Desain Visual (`taste-skill`, `liquid-apple-ui-skill`, `minimalist-ui`, `brutalist-skill`)**: Bertindak sebagai **Kulit & Estetika (Visual Skin & Theme)**: Mengatur palet warna, tipografi, efek frosted glass, neumorphism, bayangan, dan micro-interaction.
> 
> Skill ini **TIDAK MENDIKTE** gaya visual, warna brand, atau font tertentu. Seluruh pola disajikan dalam bentuk **Wireframe Struktural Netral (Styling-Agnostic)** yang dapat dipadukan dengan tema desain apa pun (Apple Glass, Dark Tech, Neumorphic, Minimalist, atau Brutalist).

---

## 1. Handheld Physics & The Natural Thumb Zone

Modern smartphones feature elongated displays with aspect ratios of **19.5:9 and 20:9** (heights ranging between 780px and 932px on standard hardware). When a user holds a smartphone in one hand, their thumb pivots from the carpometacarpal joint at the bottom corner.

Based on empirical mobile ergonomics research:

```
┌──────────────────────────────────────────┐
│ [TOP 20%]: HARD-TO-REACH ZONE           │ -> Pass-through telemetry, passive title,
│ (Requires awkward grip adjustment)       │   status indicator. ZERO vital buttons!
├──────────────────────────────────────────┤
│ [MIDDLE 45%]: STRETCH & READING ZONE     │ -> Bento cards, summary statistics, feed,
│ (Comfortable for reading & scrolling)    │   collapsible accordions, charts.
├──────────────────────────────────────────┤
│ [BOTTOM 35%]: NATURAL THUMB ZONE         │ -> Bottom Dock, Primary Action FAB,
│ (One-tap immediate single-handed reach)  │   Bottom Sheets, Segmented Controls, Keypad.
└──────────────────────────────────────────┘
```

### The 4 Universal Laws of Handheld Layouts:
1. **Rule of Bottom Elevation**: All primary calls-to-action (Submit, Create, Filter, Search, Checkout, Record) MUST reside in the bottom 35% of the viewport.
2. **Rule of Passive Top**: The top app bar is strictly for spatial orientation (brand title, back button, passive status badge). Never place primary form submit or high-frequency interaction buttons in the top-right corner.
3. **Rule of Max Bounds (`max-w-md`)**: Mobile web interfaces must never stretch infinitely on foldables, tablets, or widescreen monitors. Always constrain the main canvas to `max-w-md` (~448px) centered with `mx-auto`.
4. **Rule of Thumb Safety Zone**: Avoid placing destructive buttons (e.g. Delete, Reset All) in the immediate direct resting spot of the thumb without a confirmation step.

---

## 2. Dynamic Viewport Geometry & Safe Area Clearance

### A. The Classic 100vh Trap vs `100dvh`

Mobile browsers (Chrome on Android, Safari on iOS) feature dynamic address bars that expand and collapse during scrolling. Using legacy `height: 100vh` causes the bottom 60px of your layout to be hidden beneath the browser navigation bar.

Always declare dynamic viewport units and safe area meta tags:

```html
<!-- <head> Viewport Tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
```

```css
/* Dynamic Viewport Reset & Anti-Wobble Shield */
html, body {
  min-height: 100vh;
  min-height: 100dvh;
  overflow-x: hidden;
  max-width: 100vw;
  overscroll-behavior-y: contain;
  -webkit-tap-highlight-color: transparent;
}
```

### B. The Dock Clearance Mandate (`pb-32`)

When using a fixed bottom navigation dock or floating bottom action bar, the scrollable document container MUST have ample bottom clearance:

```html
<main id="main" class="w-full min-h-screen pb-32"
      style="padding-top: calc(4rem + env(safe-area-inset-top));">
  <div class="w-full max-w-md mx-auto px-4 pt-1">
    <!-- Page Content -->
  </div>
</main>
```

> [!CAUTION]
> **DILARANG menggunakan `pb-16` atau `pb-20` pada halaman yang memiliki Floating Dock!**
> Floating Dock memiliki tinggi ~64px ditambah margin bawah 12px dan tombol aksi tengah ~28px (total ~104px). Jika padding bawah kurang dari `pb-32` (128px), kartu atau tombol paling bawah akan terkunci di balik dock dan tidak bisa ditekan oleh pengguna.

### C. iPhone Home Bar Inset (`env(safe-area-inset-bottom)`)

Every bottom-docked element must incorporate iOS Home Indicator clearance:

```html
<nav class="fixed bottom-0 inset-x-0 z-40" style="padding-bottom: env(safe-area-inset-bottom)">
  <!-- Bottom Dock Content -->
</nav>
```

### D. Top Notch & Dynamic Island Clearance (`env(safe-area-inset-top)`)

On devices with camera cutouts or Apple's Dynamic Island, a standard `top: 0` header collides with hardware bezels.

```html
<!-- Fixed Top Header with Hardware Notch Inset -->
<header class="fixed top-0 inset-x-0 z-30 flex items-center justify-between px-4"
        style="padding-top: env(safe-area-inset-top); height: calc(3.5rem + env(safe-area-inset-top));">
  <!-- Brand & Orientation Content -->
</header>
```

### E. Sideways Screen Wobble Elimination

A frequent bug on mobile web is accidental horizontal page scrolling ("sideways drift") triggered when a child element exceeds viewport bounds by 1px.

Protect the layout by declaring:
- `overflow-x: hidden; max-width: 100vw;` on `html` and `body`.
- `max-w-md mx-auto` on every direct child container.
- Horizontal carousels must manage their own isolated overflow (`overflow-x: auto`) with zero parent overflow bleeding.

---

## 3. Structural Bottom Navigation Dock & Center Action Slot

A flexible, layout-first bottom navigation bar wireframe supporting 3, 4, or 5 slots with an elevated center primary action button (FAB) positioned right under the thumb.

```html
<!-- Structural Bottom Navigation Dock (Styling-Agnostic) -->
<nav id="nav-bar" class="fixed bottom-0 inset-x-0 z-40 select-none"
     style="padding-bottom: env(safe-area-inset-bottom)" aria-label="Navigasi Utama">
  
  <!-- Outer Floating Shell: Apply your visual skin here (Glass / Neumorphic / Flat / Brutalist) -->
  <div class="mx-3 mb-3 rounded-3xl relative shadow-lg">
    
    <!-- Central Elevated Action Slot (Thumb Pivot Point) -->
    <div class="absolute left-1/2 -translate-x-1/2 -top-7 z-[60]">
      <div class="p-1.5 rounded-full shadow-md">
        <!-- The visual skin of this button is injected by your design skill -->
        <button id="fab-action" type="button"
                class="rounded-full grid place-items-center active:scale-90 transition-transform duration-150 cursor-pointer"
                style="width: 3.25rem; height: 3.25rem;"
                aria-label="Aksi Utama">
          <!-- Action Icon SVG (Lucide / Heroicons) -->
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </button>
      </div>
    </div>

    <!-- Symmetrical Navigation Slots (5-Column Wireframe) -->
    <div class="relative flex flex-row items-center h-16 pointer-events-auto">
      <!-- Slot 1 -->
      <a href="#slot1" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none active:scale-95 transition-transform">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
        <span class="text-[10px] font-bold">Slot 1</span>
      </a>

      <!-- Slot 2 -->
      <a href="#slot2" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none active:scale-95 transition-transform">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <span class="text-[10px] font-medium">Slot 2</span>
      </a>

      <!-- Slot 3: Spacer Reserved for Elevated Center Action -->
      <div class="w-1/5 flex-none h-full pointer-events-none" aria-hidden="true"></div>

      <!-- Slot 4 -->
      <a href="#slot3" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none active:scale-95 transition-transform">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
        <span class="text-[10px] font-medium">Slot 3</span>
      </a>

      <!-- Slot 5 -->
      <a href="#slot4" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none active:scale-95 transition-transform">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        <span class="text-[10px] font-medium">Slot 4</span>
      </a>
    </div>
  </div>
</nav>
```

---

## 4. Bottom Sheet Drawer Architecture (The Universal Mobile Dialog)

> [!IMPORTANT]
> **Modals centered on mobile screens are ergonomically broken.**
> When a popup dialog is centered on a 6.7-inch phone, the user's thumb cannot reach the top "X" close button or form fields without shifting their grip.
> **All mobile dialogs MUST open from the bottom edge as a Bottom Sheet Drawer.**

```html
<!-- Universal Bottom Sheet Container (Alpine.js Powered) -->
<div x-show="sheetOpen" x-cloak
     x-init="$watch('sheetOpen', value => document.body.classList.toggle('overflow-hidden', value))"
     class="fixed inset-0 z-50 flex items-end justify-center p-0 select-none"
     style="padding-bottom: env(safe-area-inset-bottom)">
  
  <!-- Backdrop Blur Overlay -->
  <div @click="sheetOpen = false"
       x-transition:enter="transition ease-out duration-200"
       x-transition:enter-start="opacity-0"
       x-transition:enter-end="opacity-100"
       x-transition:leave="transition ease-in duration-150"
       x-transition:leave-start="opacity-100"
       x-transition:leave-end="opacity-0"
       class="absolute inset-0 bg-black/40 backdrop-blur-sm cursor-pointer"></div>

  <!-- Bottom Sheet Card (Slides Up from bottom edge) -->
  <div class="relative w-full max-w-md rounded-t-3xl shadow-2xl p-5 space-y-4 overscroll-contain"
       x-transition:enter="transition ease-out duration-250 transform"
       x-transition:enter-start="translate-y-full"
       x-transition:enter-end="translate-y-0"
       x-transition:leave="transition ease-in duration-150 transform"
       x-transition:leave-start="translate-y-0"
       x-transition:leave-end="translate-y-full">
    
    <!-- Top Grab Handle Pill (Visual affordance for vertical swipe) -->
    <div class="w-12 h-1.5 rounded-full mx-auto -mt-1 mb-2 cursor-grab opacity-60"></div>

    <!-- Sheet Header -->
    <div class="flex items-center justify-between">
      <h3 class="text-base font-bold tracking-tight">Judul Drawer</h3>
      <button @click="sheetOpen = false" type="button"
              class="w-8 h-8 rounded-full flex items-center justify-center cursor-pointer active:scale-95"
              aria-label="Tutup">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Sheet Scrollable Body: Put options, forms, or actions here -->
    <div class="space-y-2 max-h-[60vh] overflow-y-auto">
      <!-- Option Items (Enforce min-h-[44px] touch target) -->
      <button type="button" @click="sheetOpen = false"
              class="w-full p-3.5 rounded-2xl flex items-center justify-between gap-3 text-left active:scale-[0.98] transition-transform min-h-[48px]">
        <div class="flex items-center gap-3 min-w-0">
          <div class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 font-bold text-xs">
            01
          </div>
          <div class="min-w-0">
            <div class="text-sm font-bold truncate">Pilihan Pertama</div>
            <div class="text-xs opacity-70">Deskripsi sub-keterangan opsi</div>
          </div>
        </div>
      </button>
    </div>
  </div>
</div>
```

---

## 5. Structural Virtual Numerical / Input Keypad Drawer

When high-frequency numerical entry (counters, quantities, values, PIN codes) is required on mobile web, native OS keyboards cause jarring viewport jumps, overlap action buttons, and vary across manufacturers.

A dedicated 3-column physical keypad drawer provides a rock-solid, zero-jump touch surface:

```html
<!-- Structural Keypad Drawer (Styling-Agnostic) -->
<div id="keypad-sheet" x-show="keypadOpen" x-cloak
     class="fixed inset-x-0 bottom-0 z-50 rounded-t-3xl shadow-2xl p-4 space-y-3 max-w-md mx-auto select-none"
     style="padding-bottom: max(16px, env(safe-area-inset-bottom))"
     x-transition:enter="transition ease-out duration-200 transform"
     x-transition:enter-start="translate-y-full"
     x-transition:enter-end="translate-y-0"
     x-transition:leave="transition ease-in duration-150 transform"
     x-transition:leave-start="translate-y-0"
     x-transition:leave-end="translate-y-full">
  
  <!-- Visual Grab Handle -->
  <div class="w-10 h-1 rounded-full mx-auto opacity-50"></div>

  <!-- Numerical Display Preview Screen -->
  <div class="text-center py-2 rounded-2xl">
    <p class="text-[11px] font-bold uppercase tracking-wider opacity-70">Preview Input</p>
    <p class="text-3xl font-black font-mono tabular-nums" x-text="keypadBuffer || '0'">0</p>
  </div>

  <!-- Quick Preset / Increment Chips -->
  <div class="flex items-center justify-center gap-1.5">
    <button type="button" @click="quickAdd(1)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold active:scale-95 min-h-[36px]">+1</button>
    <button type="button" @click="quickAdd(5)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold active:scale-95 min-h-[36px]">+5</button>
    <button type="button" @click="quickAdd(10)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold active:scale-95 min-h-[36px]">+10</button>
    <button type="button" @click="quickAdd(50)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold active:scale-95 min-h-[36px]">+50</button>
  </div>

  <!-- 3-Column Touch Keypad Grid -->
  <div class="grid grid-cols-3 gap-2">
    <button type="button" @click="appendKey('1')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">1</button>
    <button type="button" @click="appendKey('2')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">2</button>
    <button type="button" @click="appendKey('3')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">3</button>
    
    <button type="button" @click="appendKey('4')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">4</button>
    <button type="button" @click="appendKey('5')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">5</button>
    <button type="button" @click="appendKey('6')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">6</button>
    
    <button type="button" @click="appendKey('7')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">7</button>
    <button type="button" @click="appendKey('8')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">8</button>
    <button type="button" @click="appendKey('9')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">9</button>
    
    <button type="button" @click="appendKey('00')" class="rounded-2xl text-base font-extrabold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">00</button>
    <button type="button" @click="appendKey('0')" class="rounded-2xl text-2xl font-bold py-3.5 min-h-[48px] font-mono active:scale-95 transition-transform">0</button>
    <button type="button" @click="backspaceKey()" class="rounded-2xl flex items-center justify-center min-h-[48px] active:scale-95 transition-transform" aria-label="Hapus">
      <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 4H8l-7 8 7 8h13a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2z"></path>
        <line x1="18" y1="9" x2="12" y2="15"></line>
        <line x1="12" y1="9" x2="18" y2="15"></line>
      </svg>
    </button>

    <!-- Full-Width Confirm Action -->
    <button type="button" @click="keypadOpen = false"
            class="col-span-3 h-12 rounded-2xl font-bold text-sm shadow-md active:scale-[0.98] transition-transform">
      Konfirmasi
    </button>
  </div>
</div>
```

---

## 6. Single-Row Horizontal Carousels vs Vertical Wrapping

On mobile screens (360px – 412px wide), when filter chips or categories wrap into 3 or 4 vertical lines, they consume 25% of the visible viewport before the user even sees the content.

**The Golden Pattern**: Keep filter chips on a single horizontal row that smoothly scrolls with momentum, hiding scrollbars:

```html
<!-- CSS Utility -->
<style>
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>

<!-- Horizontal Filter Row (Zero Vertical Wrap) -->
<div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1.5 -mx-4 px-4 select-none">
  <!-- Active Filter Chip -->
  <button type="button"
          class="px-4 py-2 rounded-full text-xs font-bold shrink-0 active:scale-95 transition-transform min-h-[40px]">
    Semua Item
  </button>
  <!-- Inactive Filter Chips -->
  <button type="button"
          class="px-4 py-2 rounded-full text-xs font-semibold shrink-0 active:scale-95 transition-transform min-h-[40px]">
    Kategori A
  </button>
  <button type="button"
          class="px-4 py-2 rounded-full text-xs font-semibold shrink-0 active:scale-95 transition-transform min-h-[40px]">
    Kategori B
  </button>
  <button type="button"
          class="px-4 py-2 rounded-full text-xs font-semibold shrink-0 active:scale-95 transition-transform min-h-[40px]">
    Kategori C
  </button>
</div>
```

---

## 7. Thumb-Optimized Action Bars & Button Hierarchies

### A. The 2-Row Bottom Action Bar
At the conclusion of a mobile form or transaction workflow, avoid cramming multiple buttons into a single cramped row. Use a **2-row hierarchical layout**:
- **Row 1**: Primary Action (Full-width, `h-12` / 48px, high visual prominence).
- **Row 2**: Secondary / Dismiss / Back Actions (Side-by-side, `h-11` / 44px, split 50/50).

```html
<!-- 2-Row Thumb Action Bar -->
<div class="space-y-2.5 pt-4">
  <!-- Row 1: Primary Action (Full-Width, Elevated) -->
  <button type="submit"
          class="w-full h-12 rounded-2xl font-bold text-sm flex items-center justify-center gap-2 shadow-md active:scale-[0.97] transition-transform">
    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
    <span>Simpan & Eksekusi</span>
  </button>

  <!-- Row 2: Secondary Side-by-Side (50% / 50%) -->
  <div class="flex items-center gap-2">
    <button type="button"
            class="flex-1 h-11 rounded-2xl font-bold text-xs active:scale-[0.97] transition-transform">
      Batal
    </button>
    <button type="button"
            class="flex-1 h-11 rounded-2xl font-bold text-xs active:scale-[0.97] transition-transform flex items-center justify-center gap-1.5">
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
      </svg>
      <span>Hapus</span>
    </button>
  </div>
</div>
```

### B. Target Size Standards & The 8px Fat-Finger Barrier

1. **Apple Human Interface Guidelines (HIG)**:
   - Minimum interactive hit target: **44 x 44 pt** (`min-h-[44px] min-w-[44px]`).
2. **Google Material Design & Android**:
   - Minimum touch target: **48 x 48 dp** (`min-h-[48px] min-w-[48px]`).
3. **W3C WCAG 2.2 Criterion 2.5.8 (Target Spacing)**:
   - Any two interactive elements with hit targets smaller than 48px MUST maintain at least **8px of physical spacing separation** (`gap-2` / `space-x-2`).
   - If two 44px buttons touch with 0px margin, adult thumb false-taps surge by up to 18% during single-handed operation.

---

## 8. Mobile Typography & Safari iOS Auto-Zoom Mitigation

### A. The Safari 16px Auto-Zoom Rule

> [!WARNING]
> In iOS Safari, any `<input>`, `<select>`, or `<textarea>` with a font size smaller than `16px` (`1rem`) triggers an automatic zoom-in when focused. This breaks responsive layout geometry and forces the user to pinch-to-zoom out.
> **All mobile input fields MUST declare `font-size: 16px` at minimum.**

```css
/* Universal Mobile Input Fix */
input, select, textarea {
  font-size: 16px !important;
}
```

### B. Mobile Typographic Density
- **Mobile Heading (H1)**: `text-xl` (20px) or maximum `text-2xl` (24px).
- **Metric Big Numbers**: `text-3xl` (28px) or `text-4xl` (32px) with tabular numbers (`tabular-nums font-mono`).
- **Body & Description**: `text-sm` (14px) for comfortable readability.
- **Labels & Micro-Copy**: `text-xs` (12px) with `font-semibold`.

---

## 9. Tactile Bento Cards & Mobile Feed Architecture

Avoid wide multi-column tables for standard mobile list items. Wrap records into **Tactile Bento Cards**:

```html
<!-- Structural Mobile Card Item -->
<div class="p-3.5 rounded-2xl border shadow-xs flex items-center justify-between gap-3 active:scale-[0.98] transition-transform cursor-pointer">
  <!-- Left: Category / Status Icon + Title -->
  <div class="flex items-center gap-3 min-w-0">
    <div class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0">
      <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
        <polyline points="14 2 14 8 20 8"></polyline>
      </svg>
    </div>
    <div class="min-w-0">
      <h4 class="text-sm font-bold truncate">Judul Item Record</h4>
      <p class="text-[11px] opacity-70 truncate">Keterangan parameter data</p>
    </div>
  </div>

  <!-- Right: Value Metric / Badge -->
  <div class="text-right shrink-0">
    <div class="text-sm font-bold font-mono tabular-nums">Metrik</div>
    <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold uppercase">
      Status
    </span>
  </div>
</div>
```

---

## 10. Soft-Keyboard Auto-Avoidance Architecture

When a user taps an ordinary text input, the native virtual keyboard opens, consuming **40% to 50% of the visible viewport**.

If a fixed bottom navigation dock remains visible, it collides with the native keyboard, causing visual clutter and covering form action buttons.

### The Auto-Hide Floating Dock Pattern

Declare a reactive boolean state in your root Alpine component (`isInputFocused`):

```html
<!-- Root Alpine Scope -->
<div x-data="{ isInputFocused: false }">

  <!-- Ordinary Text Inputs: Hide dock on focus -->
  <input type="text"
         placeholder="Ketik teks input..."
         @focus="isInputFocused = true"
         @blur="isInputFocused = false"
         class="w-full h-12 px-4 rounded-2xl border text-base transition-all outline-none">

  <!-- Floating Navigation Dock: Retracts downward when keyboard is open -->
  <nav class="fixed bottom-0 inset-x-0 z-40 transition-transform duration-200 ease-in-out select-none"
       :class="isInputFocused ? 'translate-y-32 pointer-events-none' : 'translate-y-0 pointer-events-auto'"
       style="padding-bottom: env(safe-area-inset-bottom)">
    <!-- Dock Content -->
  </nav>
</div>
```

---

## 11. Mobile Data Tables with Two-Layer Horizontal Scroll & Gradient Cue

When wide multi-column data tables (5+ columns) must be presented on mobile:

A two-layer scrollable table container with a subtle **visual right-gradient fade** signals to the user's thumb that more tabular data lies just beyond the right edge:

```html
<!-- Responsive Table Container with Visual Swipe Cue -->
<div class="relative overflow-hidden rounded-2xl border shadow-xs">
  
  <!-- Scrollable Layer with Hidden Scrollbars -->
  <div class="overflow-x-auto no-scrollbar">
    <table class="w-full text-left text-xs min-w-[500px]">
      <thead class="border-b font-semibold opacity-80">
        <tr>
          <th class="py-3 px-3.5">ID</th>
          <th class="py-3 px-3">Nama Kolom A</th>
          <th class="py-3 px-3">Nama Kolom B</th>
          <th class="py-3 px-3 text-right">Metrik</th>
          <th class="py-3 px-3.5 text-center">Status</th>
        </tr>
      </thead>
      <tbody class="divide-y font-medium">
        <tr class="active:opacity-80 transition-opacity">
          <td class="py-3 px-3.5 whitespace-nowrap font-mono">#001</td>
          <td class="py-3 px-3 whitespace-nowrap font-bold">Item Baris Satu</td>
          <td class="py-3 px-3 truncate max-w-[140px]">Parameter rincian</td>
          <td class="py-3 px-3 text-right whitespace-nowrap font-mono font-bold">100%</td>
          <td class="py-3 px-3.5 text-center whitespace-nowrap">
            <span class="inline-block px-2 py-0.5 rounded-full text-[10px] font-bold">Aktif</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Right Visual Gradient Cue (Signals thumb-swipe capability) -->
  <div class="pointer-events-none absolute inset-y-0 right-0 w-8 bg-gradient-to-l from-black/10 to-transparent"></div>
</div>
```

---

## 12. Universal Turnkey Mobile Application Blueprint

Below is the complete, single-file ready-to-run template embodying all handheld ergonomic laws, complete with interactive Alpine.js state for the Floating Dock, Universal Bottom Sheet Picker, and Virtual Numerical Keypad:

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Universal Mobile Shell Blueprint</title>

  <!-- Core Frameworks (Zero Build-Step) -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>

  <style>
    [x-cloak] { display: none !important; }
    html, body {
      min-height: 100vh;
      min-height: 100dvh;
      overflow-x: hidden;
      max-width: 100vw;
      overscroll-behavior-y: contain;
      -webkit-tap-highlight-color: transparent;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    input, select, textarea { font-size: 16px !important; }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
  </style>
</head>
<body class="w-full relative bg-slate-50 text-slate-900"
      x-data="universalMobileApp()">

  <!-- TOP APP BAR: Orientation Only (with Hardware Notch & Dynamic Island Inset) -->
  <header class="fixed top-0 inset-x-0 bg-white/90 backdrop-blur-md border-b border-slate-200 z-30 flex items-center justify-between px-4 select-none"
          style="padding-top: env(safe-area-inset-top); height: calc(3.5rem + env(safe-area-inset-top));">
    <div class="flex items-center space-x-2">
      <span class="w-2.5 h-2.5 rounded-full bg-blue-600 animate-pulse"></span>
      <span class="font-extrabold text-sm tracking-tight">APP PORTAL</span>
    </div>
    <span class="text-[11px] font-bold text-slate-400">Mobile Hub</span>
  </header>

  <!-- MAIN SCROLL CONTAINER: Bound to max-w-md with pb-32 clearance -->
  <main class="w-full min-h-screen pb-32"
        style="padding-top: calc(4.25rem + env(safe-area-inset-top));">
    <div class="w-full max-w-md mx-auto px-4 space-y-4">
      
      <!-- HERO SUMMARY CARD: Tap to trigger Selector Drawer -->
      <section @click="pickerSheetOpen = true"
               class="rounded-3xl bg-slate-900 text-white p-5 space-y-3 shadow-xl relative overflow-hidden cursor-pointer active:scale-[0.99] transition-transform">
        <div class="flex items-center justify-between">
          <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Metrik Ringkasan</p>
          <span class="text-xs font-bold text-blue-400 flex items-center gap-1">
            <span x-text="activeOptionTitle">Pilihan Aktif</span>
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
          </span>
        </div>
        <p class="text-3xl font-black tracking-tight font-mono tabular-nums" x-text="summaryMetric">1,240 Unit</p>
        <div class="flex items-center gap-2 pt-1">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-400">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Status Berjalan Normal
          </span>
        </div>
      </section>

      <!-- HORIZONTAL FILTER CAROUSEL (Zero vertical wrapping) -->
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1 -mx-4 px-4 select-none">
        <button @click="filter = 'all'"
                class="px-4 py-2 rounded-full text-xs font-bold shrink-0 min-h-[40px] transition-all"
                :class="filter === 'all' ? 'bg-blue-600 text-white shadow-sm' : 'bg-white border border-slate-200 text-slate-600'">
          Semua Data
        </button>
        <button @click="filter = 'cat1'"
                class="px-4 py-2 rounded-full text-xs font-semibold shrink-0 min-h-[40px] transition-all"
                :class="filter === 'cat1' ? 'bg-blue-600 text-white shadow-sm' : 'bg-white border border-slate-200 text-slate-600'">
          Kategori Utama
        </button>
        <button @click="filter = 'cat2'"
                class="px-4 py-2 rounded-full text-xs font-semibold shrink-0 min-h-[40px] transition-all"
                :class="filter === 'cat2' ? 'bg-blue-600 text-white shadow-sm' : 'bg-white border border-slate-200 text-slate-600'">
          Modul Tambahan
        </button>
      </div>

      <!-- TRANSACTION / ITEM FEED -->
      <div class="space-y-2.5">
        <div class="p-3.5 rounded-2xl bg-white border border-slate-200 shadow-xs flex items-center justify-between gap-3 active:scale-[0.98] transition-transform">
          <div class="min-w-0">
            <h4 class="text-sm font-bold text-slate-900 truncate">Item Aktivitas #01</h4>
            <p class="text-[11px] text-slate-400">Keterangan item • Parameter A</p>
          </div>
          <div class="text-sm font-black text-emerald-600 font-mono">Selesai</div>
        </div>
        <div class="p-3.5 rounded-2xl bg-white border border-slate-200 shadow-xs flex items-center justify-between gap-3 active:scale-[0.98] transition-transform">
          <div class="min-w-0">
            <h4 class="text-sm font-bold text-slate-900 truncate">Item Aktivitas #02</h4>
            <p class="text-[11px] text-slate-400">Keterangan item • Parameter B</p>
          </div>
          <div class="text-sm font-black text-slate-500 font-mono">Proses</div>
        </div>
      </div>

    </div>
  </main>

  <!-- FLOATING BOTTOM DOCK WITH CENTER ELEVATED ACTION -->
  <nav class="fixed bottom-0 inset-x-0 z-40 transition-transform duration-200 select-none"
       :class="isInputFocused ? 'translate-y-32 pointer-events-none' : 'translate-y-0 pointer-events-auto'"
       style="padding-bottom: env(safe-area-inset-bottom)">
    <div class="mx-3 mb-3 bg-white/90 backdrop-blur-xl border border-slate-200 shadow-2xl rounded-3xl relative">
      
      <!-- Central Elevated Action Button -->
      <div class="absolute left-1/2 -translate-x-1/2 -top-7 z-[60]">
        <div class="p-1.5 bg-white/80 backdrop-blur-md rounded-full shadow-md border border-slate-200">
          <button @click="keypadOpen = true" type="button"
                  class="w-13 h-13 rounded-full bg-blue-600 hover:bg-blue-700 text-white shadow-lg grid place-items-center active:scale-90 transition-all cursor-pointer"
                  style="width: 3.25rem; height: 3.25rem;"
                  aria-label="Aksi Utama">
            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>
      </div>

      <!-- 5-Slot Bottom Grid -->
      <div class="relative flex flex-row items-center h-16 pointer-events-auto">
        <button @click="activeTab = 'home'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'home' ? 'text-blue-600' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          <span class="text-[10px] font-bold">Beranda</span>
        </button>
        <button @click="activeTab = 'items'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'items' ? 'text-blue-600' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <span class="text-[10px] font-medium">Katalog</span>
        </button>
        <div class="w-1/5 flex-none h-full pointer-events-none"></div>
        <button @click="activeTab = 'feed'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'feed' ? 'text-blue-600' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          <span class="text-[10px] font-medium">Aktivitas</span>
        </button>
        <button @click="activeTab = 'settings'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'settings' ? 'text-blue-600' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span class="text-[10px] font-medium">Pengaturan</span>
        </button>
      </div>
    </div>
  </nav>

  <!-- BOTTOM SHEET: Universal Option Selector -->
  <div x-show="pickerSheetOpen" x-cloak
       class="fixed inset-0 z-50 flex items-end justify-center p-0 select-none"
       style="padding-bottom: env(safe-area-inset-bottom)">
    <div @click="pickerSheetOpen = false"
         class="absolute inset-0 bg-black/40 backdrop-blur-sm cursor-pointer"
         x-transition:enter="transition ease-out duration-200"
         x-transition:enter-start="opacity-0"
         x-transition:enter-end="opacity-100"
         x-transition:leave="transition ease-in duration-150"
         x-transition:leave-start="opacity-100"
         x-transition:leave-end="opacity-0"></div>

    <div class="relative w-full max-w-md bg-white rounded-t-3xl border-t border-slate-200 shadow-2xl p-5 space-y-4 overscroll-contain"
         x-transition:enter="transition ease-out duration-250 transform"
         x-transition:enter-start="translate-y-full"
         x-transition:enter-end="translate-y-0"
         x-transition:leave="transition ease-in duration-150 transform"
         x-transition:leave-start="translate-y-0"
         x-transition:leave-end="translate-y-full">
      <div class="w-12 h-1.5 rounded-full bg-slate-200 mx-auto -mt-1 mb-2"></div>
      <div class="flex items-center justify-between">
        <h3 class="text-base font-bold text-slate-900">Pilih Mode Pengoperasian</h3>
        <button @click="pickerSheetOpen = false" class="w-8 h-8 rounded-full bg-slate-100 text-slate-500 flex items-center justify-center">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="space-y-2">
        <button type="button" @click="selectOption('Opsi Prioritas Utama', '1,240 Unit')"
                class="w-full p-3.5 rounded-2xl flex items-center justify-between border bg-slate-50 border-slate-200 active:scale-[0.98] transition-all min-h-[48px]">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 font-bold text-xs flex items-center justify-center">PRI</div>
            <div class="text-left"><div class="text-sm font-bold text-slate-900">Opsi Prioritas Utama</div><div class="text-xs text-slate-400 font-mono">1,240 Unit</div></div>
          </div>
        </button>
        <button type="button" @click="selectOption('Opsi Cadangan', '850 Unit')"
                class="w-full p-3.5 rounded-2xl flex items-center justify-between border bg-slate-50 border-slate-200 active:scale-[0.98] transition-all min-h-[48px]">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-slate-100 text-slate-600 font-bold text-xs flex items-center justify-center">SEC</div>
            <div class="text-left"><div class="text-sm font-bold text-slate-900">Opsi Cadangan</div><div class="text-xs text-slate-400 font-mono">850 Unit</div></div>
          </div>
        </button>
      </div>
    </div>
  </div>

  <!-- BOTTOM SHEET: Universal Numerical Keypad Drawer -->
  <div x-show="keypadOpen" x-cloak
       class="fixed inset-x-0 bottom-0 z-50 bg-white border-t border-slate-200 rounded-t-3xl shadow-2xl p-4 space-y-3 max-w-md mx-auto select-none overscroll-contain"
       style="padding-bottom: max(16px, env(safe-area-inset-bottom))"
       x-transition:enter="transition ease-out duration-250 transform"
       x-transition:enter-start="translate-y-full"
       x-transition:enter-end="translate-y-0"
       x-transition:leave="transition ease-in duration-150 transform"
       x-transition:leave-start="translate-y-0"
       x-transition:leave-end="translate-y-full">
    
    <div class="w-10 h-1 rounded-full bg-slate-300 mx-auto"></div>
    
    <!-- Input Preview Screen -->
    <div class="text-center py-2 bg-slate-50 rounded-2xl border border-slate-200">
      <p class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Nilai Input</p>
      <p class="text-3xl font-black text-slate-900 font-mono tabular-nums" x-text="rawKeypad || '0'">0</p>
    </div>

    <!-- Quick Modifier Chips -->
    <div class="flex items-center justify-center gap-1.5">
      <button @click="quickAdd(10)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold bg-slate-100 text-slate-700 active:scale-95 min-h-[36px]">+10</button>
      <button @click="quickAdd(50)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold bg-slate-100 text-slate-700 active:scale-95 min-h-[36px]">+50</button>
      <button @click="quickAdd(100)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold bg-slate-100 text-slate-700 active:scale-95 min-h-[36px]">+100</button>
      <button @click="quickAdd(500)" class="px-3 py-1.5 rounded-full text-xs font-mono font-bold bg-slate-100 text-slate-700 active:scale-95 min-h-[36px]">+500</button>
    </div>

    <!-- 3-Column Keypad Matrix -->
    <div class="grid grid-cols-3 gap-2">
      <button type="button" @click="appendKey('1')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">1</button>
      <button type="button" @click="appendKey('2')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">2</button>
      <button type="button" @click="appendKey('3')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">3</button>
      <button type="button" @click="appendKey('4')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">4</button>
      <button type="button" @click="appendKey('5')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">5</button>
      <button type="button" @click="appendKey('6')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">6</button>
      <button type="button" @click="appendKey('7')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">7</button>
      <button type="button" @click="appendKey('8')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">8</button>
      <button type="button" @click="appendKey('9')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">9</button>
      <button type="button" @click="appendKey('00')" class="rounded-2xl bg-slate-200 active:bg-slate-300 text-base font-extrabold py-3 font-mono min-h-[48px]">00</button>
      <button type="button" @click="appendKey('0')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3 font-mono min-h-[48px]">0</button>
      <button type="button" @click="backspaceKey()" class="rounded-2xl bg-slate-200 active:bg-slate-300 flex items-center justify-center py-3 min-h-[48px]" aria-label="Hapus">
        <svg class="w-6 h-6 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 4H8l-7 8 7 8h13a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2z"/><line x1="18" y1="9" x2="12" y2="15"/><line x1="12" y1="9" x2="18" y2="15"/></svg>
      </button>
      <button type="button" @click="keypadOpen = false" class="col-span-3 h-12 rounded-2xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm shadow-md active:scale-[0.98] min-h-[48px]">
        Simpan Data
      </button>
    </div>
  </div>

  <script>
    function universalMobileApp() {
      return {
        activeTab: 'home',
        filter: 'all',
        pickerSheetOpen: false,
        keypadOpen: false,
        isInputFocused: false,
        activeOptionTitle: 'Opsi Prioritas Utama',
        summaryMetric: '1,240 Unit',
        rawKeypad: '',

        init() {
          this.$watch('pickerSheetOpen', v => document.body.classList.toggle('overflow-hidden', v));
          this.$watch('keypadOpen', v => document.body.classList.toggle('overflow-hidden', v));
        },

        selectOption(title, metric) {
          this.activeOptionTitle = title;
          this.summaryMetric = metric;
          this.pickerSheetOpen = false;
        },

        appendKey(k) {
          if (this.rawKeypad.length >= 9) return;
          if (this.rawKeypad === '' && (k === '0' || k === '00')) return;
          this.rawKeypad += k;
          this.vibe();
        },

        backspaceKey() {
          this.rawKeypad = this.rawKeypad.slice(0, -1);
          this.vibe();
        },

        quickAdd(v) {
          const cur = parseInt(this.rawKeypad || '0', 10);
          this.rawKeypad = String(cur + v);
          this.vibe();
        },

        vibe() {
          if ('vibrate' in navigator) try { navigator.vibrate(10); } catch(e) {}
        }
      };
    }
  </script>
</body>
</html>
```

---

## 13. Mobile Handheld Ergonomics Pre-Flight Checklist

Before declaring any smartphone web interface or PWA production-ready, verify these 10 physical layout criteria:

1. **Clearance Discipline (`pb-32`)**:
   - The `<main>` document container declares `pb-32` (128px) minimum clearance so that fixed bottom navigation bars never conceal the final form elements or cards.
2. **Safe-Area Inset Handling**:
   - All fixed bottom docks, action bars, and bottom sheets declare `style="padding-bottom: env(safe-area-inset-bottom)"` to avoid colliding with the iOS Home Bar.
3. **Hardware Notch Clearance**:
   - Fixed headers declare `style="padding-top: env(safe-area-inset-top); height: calc(3.5rem + env(safe-area-inset-top));"` and `<main>` padding top matches the clearance.
4. **Dynamic Viewport Physics (`100dvh`)**:
   - Containers use `min-h-[100dvh]` instead of legacy `100vh` to prevent jumping when browser address bars collapse.
5. **Target Touch Standards (44px Rule)**:
   - Every clickable button, chip, tab, and row has a minimum hit area of 44x44px (`min-h-[44px]` or `min-h-[48px]`).
6. **Fat-Finger Spacing Barrier (8px Rule)**:
   - Adjacent touch targets smaller than 48px maintain a minimum 8px separation barrier (`gap-2` / `space-x-2`).
7. **Safari iOS Auto-Zoom Mitigation**:
   - Every `<input>`, `<select>`, and `<textarea>` explicitly enforces `font-size: 16px !important;` to block iOS auto-zoom disruptions.
8. **No Multiline Filter Wrapping**:
   - Filter chips and categories scroll horizontally in a single row (`flex overflow-x-auto no-scrollbar`), preserving vertical viewing height.
9. **Bottom Sheets Over Centered Modals**:
   - Dialogs, pickers, and menus slide up from the bottom edge (`flex items-end rounded-t-3xl`) with a visible grab handle, never opening as centered popups.
10. **Device Width Bounds (`max-w-md`)**:
    - The layout canvas is restricted to `max-w-md mx-auto` (approx. 448px) so it presents an ergonomic mobile aspect ratio even when opened on foldables, tablets, or desktop viewports.
