---
name: mobile-thumb-ergonomics-skill
description: "Handheld mobile UI ergonomics, viewport physics, and thumb-zone layout architecture for single-handed smartphone access: floating glass dock with elevated FAB, bottom sheet drawers, 44px minimum touch targets, 100dvh safe-area clearance, virtual keypad bottom sheets, and horizontal swipe carousels extracted from Kas Megapass production."
---

# Mobile Thumb Ergonomics Skill (Handheld Viewport Architecture)

Architecture, physical layout formulas, and frontend engineering patterns for building proportional, thumb-friendly mobile web applications and PWAs.

Directly reverse-engineered and extracted from the production-proven workbench application **Kas Megapass** (`https://kas.megapass.web.id/`), engineered specifically for single-handed smartphone operation while working on hardware benches.

---

## 1. Handheld Physics & The Natural Thumb Zone

Smartphone screens have elongated to aspect ratios of **19.5:9 and 20:9** (height 780px to 932px on standard devices). When a user holds a smartphone in one hand, their thumb pivots from the carpometacarpal joint at the bottom-right (for right-handed users) or bottom-left (for left-handed users).

Based on Steven Hoober's empirical mobile ergonomics research (1,333+ observed participants):

```
┌──────────────────────────────────────────┐
│ [TOP 20%]: HARD-TO-REACH ZONE           │ ➔ Pass-through telemetry, passive title,
│ (Requires awkward grip adjustment)       │   battery/clock. ZERO vital buttons here!
├──────────────────────────────────────────┤
│ [MIDDLE 45%]: STRETCH ZONE              │ ➔ Bento cards, summary statistics, feed,
│ (Comfortable for reading & scrolling)    │   collapsible accordions, charts.
├──────────────────────────────────────────┤
│ [BOTTOM 35%]: NATURAL THUMB ZONE         │ ➔ Floating Dock, Primary Action FAB,
│ (One-tap immediate single-handed reach)  │   Bottom Sheets, Segmented Controls, Keypad.
└──────────────────────────────────────────┘
```

### The 3 Golden Rules of Handheld Ergonomics:
1. **Rule of Bottom Elevation**: All primary calls-to-action (Submit, Record, Create, Filter, Search) MUST reside in the bottom 35% of the viewport.
2. **Rule of Neutral Top**: The top app bar is strictly for orientation (brand title, back chevron, passive notifications). Never place primary form submit or key interaction buttons in the top-right corner.
3. **Rule of Max Bounds (`max-w-md`)**: Mobile web apps must never stretch horizontally on phablets or foldables. Always constrain the main canvas to `max-w-md` (~448px) centered with `mx-auto`.

---

## 2. Viewport Geometry & Safe Area Clearance

### A. The Classic 100vh Trap vs `100dvh`

Mobile browsers (Chrome on Android, Safari on iOS) feature dynamic address bars that expand and collapse upon scrolling. Using `height: 100vh` causes the bottom 60px of your layout to be hidden behind the browser navigation bar.

Always declare dynamic viewport units and safe area meta tags:

```html
<!-- <head> Viewport Tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
```

```css
/* Dynamic Viewport Reset */
html, body {
  min-height: 100vh;
  min-height: 100dvh;
  overscroll-behavior-y: contain;
  -webkit-tap-highlight-color: transparent;
}
```

### B. The Dock Clearance Mandate (`pb-32`)

When using a fixed bottom navigation dock or floating bottom action bar, the scrollable document container MUST have ample bottom clearance:

```html
<main id="main" class="w-full min-h-screen pt-14 pb-32">
  <div class="w-full max-w-md mx-auto px-3.5 pt-3">
    <!-- Page Content -->
  </div>
</main>
```

> [!CAUTION]
> **DILARANG menggunakan `pb-16` atau `pb-20` pada halaman yang memiliki Floating Dock!**
> Floating Dock memiliki tinggi ~64px ditambah margin bawah 12px dan FAB notch ~28px (total ~104px). Jika padding bawah kurang dari `pb-32` (128px), kartu atau tombol paling bawah akan terkunci di balik dock dan tidak bisa ditekan oleh pengguna.

### C. iPhone Home Bar Inset (`env(safe-area-inset-bottom)`)

Every bottom-docked element must incorporate iOS Home Indicator clearance:

```html
<nav class="fixed bottom-0 inset-x-0 z-40" style="padding-bottom: env(safe-area-inset-bottom)">
  <!-- Floating Dock -->
</nav>
```

---

## 3. The Floating Glass Dock & Center Notch FAB

Extracted directly from the mobile architecture of `kas.megapass.web.id`. It features a 5-slot symmetrical grid with a center-floating action button (FAB) that sits right under the thumb.

```html
<!-- Floating Glass Dock Navigation -->
<nav id="nav-bar" class="fixed bottom-0 inset-x-0 z-40"
     style="padding-bottom: env(safe-area-inset-bottom)" aria-label="Navigasi Bawah">
  <div class="mx-3 mb-3 backdrop-blur-xl bg-white/80 border border-white/60 shadow-2xl shadow-slate-900/15 rounded-3xl relative">
    
    <!-- Central Elevated Action Button (FAB with Frosted Ring) -->
    <div class="absolute left-1/2 -translate-x-1/2 -top-7 z-[60]">
      <div class="p-1.5 backdrop-blur-xl bg-white/60 rounded-full shadow-md border border-white/50">
        <button id="fab-action" type="button"
                class="w-13 h-13 rounded-full bg-[#0071E3] text-white shadow-lg grid place-items-center active:scale-90 transition-all duration-150 ease-out cursor-pointer"
                style="width: 3.25rem; height: 3.25rem;"
                aria-label="Aksi Cepat" title="Aksi Cepat">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </button>
      </div>
    </div>

    <!-- 5-Slot Symmetrical Navigation Grid -->
    <div class="relative flex flex-row items-center h-16 pointer-events-auto">
      <!-- Slot 1: Beranda -->
      <a href="/" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none text-slate-900 active:scale-95 transition-all duration-150">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
        </svg>
        <span class="text-[10px] font-bold">Beranda</span>
      </a>

      <!-- Slot 2: Transaksi -->
      <a href="/tx" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none text-slate-400 hover:text-slate-700 active:scale-95 transition-all duration-150">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/>
        </svg>
        <span class="text-[10px] font-medium">Transaksi</span>
      </a>

      <!-- Slot 3: Spacer for Center FAB -->
      <div class="w-1/5 flex-none h-full pointer-events-none"></div>

      <!-- Slot 4: Laporan -->
      <a href="/reports" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none text-slate-400 hover:text-slate-700 active:scale-95 transition-all duration-150">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21.21 15.89A10 10 0 1 1 8 2.83M22 12A10 10 0 0 0 12 2v10z"></path>
        </svg>
        <span class="text-[10px] font-medium">Laporan</span>
      </a>

      <!-- Slot 5: Pengaturan -->
      <a href="/settings" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none text-slate-400 hover:text-slate-700 active:scale-95 transition-all duration-150">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="3"></circle>
          <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
        </svg>
        <span class="text-[10px] font-medium">Setting</span>
      </a>
    </div>
  </div>
</nav>
```

---

## 4. Bottom Sheet Architecture vs Centered Modals

> [!IMPORTANT]
> **Modals centered on mobile screens are ergonomically broken.**
> When a dialog is centered on a 6.7-inch phone, the user's thumb cannot reach the top "X" close button or form fields without shifting their grip.
> **All mobile dialogs MUST open from the bottom as a Bottom Sheet Drawer.**

```html
<!-- Bottom Sheet Container (Alpine.js Powered) -->
<div x-show="sheetOpen" x-cloak
     class="fixed inset-0 z-50 flex items-end justify-center p-0"
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

  <!-- Bottom Sheet Card (Slides Up) -->
  <div class="relative w-full max-w-md bg-white rounded-t-3xl border-t border-black/[0.08] shadow-2xl overflow-hidden p-5 space-y-4"
       x-transition:enter="transition ease-out duration-250 transform"
       x-transition:enter-start="translate-y-full"
       x-transition:enter-end="translate-y-0"
       x-transition:leave="transition ease-in duration-150 transform"
       x-transition:leave-start="translate-y-0"
       x-transition:leave-end="translate-y-full">
    
    <!-- Top Grab Handle Pill -->
    <div class="w-12 h-1.5 rounded-full bg-slate-200 mx-auto -mt-1 mb-2 cursor-grab"></div>

    <!-- Sheet Header -->
    <div class="flex items-center justify-between">
      <h3 class="text-base font-black text-slate-900 tracking-tight">Pilih Rekening Dompet</h3>
      <button @click="sheetOpen = false" type="button"
              class="w-8 h-8 rounded-full bg-black/[0.04] text-slate-500 hover:text-slate-900 flex items-center justify-center">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Sheet Body Content -->
    <div class="space-y-2 max-h-[60vh] overflow-y-auto">
      <!-- Options / Content Items -->
    </div>
  </div>
</div>
```

---

## 5. Dedicated Virtual Keypad Bottom Sheet

Browser native numerical keyboards on mobile vary wildly between Android OEM keyboards (GBoard, Samsung Keyboard, Xiaomi) and iOS Safari. They frequently overlap form buttons and trigger unexpected viewport shifts.

In `kas.megapass.web.id`, high-frequency numerical entry (cashflow, transactions, meter counts, part quantities) uses a dedicated 3-column physical keypad anchored at the bottom:

```html
<!-- Mobile Keypad Bottom Sheet Drawer -->
<div id="keypad-sheet" x-show="keypadOpen" x-cloak
     class="fixed inset-x-0 bottom-0 z-50 bg-white border-t border-black/[0.08] rounded-t-3xl shadow-2xl p-3 grid grid-cols-3 gap-2 max-w-md mx-auto"
     style="padding-bottom: max(16px, env(safe-area-inset-bottom))"
     x-transition:enter="transition ease-out duration-200 transform"
     x-transition:enter-start="translate-y-full"
     x-transition:enter-end="translate-y-0"
     x-transition:leave="transition ease-in duration-150 transform"
     x-transition:leave-start="translate-y-0"
     x-transition:leave-end="translate-y-full">
  
  <!-- Visual Grab Handle -->
  <div class="col-span-3 flex justify-center pb-1">
    <div class="w-10 h-1 rounded-full bg-slate-300"></div>
  </div>

  <!-- Keypad Keys (1 to 9, 000, 0, Backspace) -->
  <button type="button" @click="appendKey('1')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">1</button>
  <button type="button" @click="appendKey('2')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">2</button>
  <button type="button" @click="appendKey('3')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">3</button>
  
  <button type="button" @click="appendKey('4')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">4</button>
  <button type="button" @click="appendKey('5')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">5</button>
  <button type="button" @click="appendKey('6')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">6</button>
  
  <button type="button" @click="appendKey('7')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">7</button>
  <button type="button" @click="appendKey('8')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">8</button>
  <button type="button" @click="appendKey('9')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">9</button>
  
  <!-- Thousands Shortcut, Zero, and Backspace -->
  <button type="button" @click="appendKey('000')" class="rounded-2xl bg-slate-200/80 active:bg-slate-300 text-base font-extrabold py-3.5 min-h-[48px] font-mono-apple">000</button>
  <button type="button" @click="appendKey('0')" class="rounded-2xl bg-slate-100 active:bg-slate-200 text-2xl font-bold py-3.5 min-h-[48px] font-mono-apple">0</button>
  <button type="button" @click="backspaceKey()" class="rounded-2xl bg-slate-200/80 active:bg-slate-300 flex items-center justify-center min-h-[48px]">
    <svg class="w-6 h-6 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M21 4H8l-7 8 7 8h13a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2z"></path>
      <line x1="18" y1="9" x2="12" y2="15"></line>
      <line x1="12" y1="9" x2="18" y2="15"></line>
    </svg>
  </button>

  <!-- Full-Width Done / Submit Button -->
  <button type="button" @click="keypadOpen = false"
          class="col-span-3 h-12 rounded-2xl bg-[#0071E3] active:bg-[#0066CC] text-white font-bold text-sm shadow-md active:scale-[0.98] transition-transform">
    Selesai
  </button>
</div>
```

---

## 6. Horizontal Scroll Carousels vs Vertical Wrapping

On mobile screens (360px – 412px wide), when category chips, date presets, or tab filters wrap into 3 or 4 vertical lines, they consume 25% of the visible viewport before the user even sees the first card.

**The Golden Pattern**: Keep filter pills on a single line that smoothly scrolls horizontally with native momentum, hiding scrollbars:

```html
<!-- CSS Utility -->
<style>
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>

<!-- Horizontal Chip Bar (Zero Vertical Wrap) -->
<div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1.5 -mx-3.5 px-3.5">
  <!-- Active Chip -->
  <button type="button"
          class="px-3.5 py-2 rounded-full text-xs font-bold bg-[#0071E3] text-white shadow-sm shrink-0 active:scale-95 transition-transform min-h-[38px]">
    Semua Kategori
  </button>
  <!-- Inactive Chips -->
  <button type="button"
          class="px-3.5 py-2 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 hover:text-slate-900 shrink-0 active:scale-95 transition-transform min-h-[38px]">
    Operasional Ruko
  </button>
  <button type="button"
          class="px-3.5 py-2 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 hover:text-slate-900 shrink-0 active:scale-95 transition-transform min-h-[38px]">
    Servis Laptop
  </button>
  <button type="button"
          class="px-3.5 py-2 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 hover:text-slate-900 shrink-0 active:scale-95 transition-transform min-h-[38px]">
    Sparepart
  </button>
</div>
```

---

## 7. Tactile Mobile Button Hierarchies & Hit Areas

### A. The 2-Row Thumb-Action Bar
At the conclusion of a mobile form or transaction workflow, avoid stacking 3 tiny buttons in one row. Use a **2-row hierarchical stack**:
- **Row 1**: Primary Action (Full-width, `h-12` / 48px, bold color, high elevation).
- **Row 2**: Secondary / Destructive Actions (Side-by-side, `h-11` / 44px, subtle border).

```html
<div class="space-y-2.5 pt-4">
  <!-- Row 1: Primary Action -->
  <button type="submit"
          class="w-full h-12 rounded-2xl bg-[#30D158] hover:bg-[#28B84C] text-white font-bold text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-500/20 active:scale-[0.97] transition-transform">
    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
    <span>Simpan Transaksi</span>
  </button>

  <!-- Row 2: Secondary Side-by-Side -->
  <div class="flex items-center gap-2">
    <button type="button"
            class="flex-1 h-11 rounded-2xl bg-white border border-black/[0.08] text-slate-600 font-bold text-xs active:scale-[0.97] transition-transform">
      Batal
    </button>
    <button type="button"
            class="flex-1 h-11 rounded-2xl bg-rose-50 border border-rose-200 text-rose-600 font-bold text-xs active:scale-[0.97] transition-transform flex items-center justify-center gap-1.5">
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
      </svg>
      <span>Hapus</span>
    </button>
  </div>
</div>
```

### B. Micro-Increment Quick Chips (`+1rb`, `+10rb`, `+50rb`)
Placed immediately below large numeric inputs so users can tap common increments with one thumb without opening the keypad:

```html
<div class="flex items-center justify-center gap-2 pt-2">
  <button type="button" @click="amount += 1000"
          class="px-3 py-1.5 rounded-full text-xs font-mono-apple font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 active:scale-95 transition-transform min-h-[36px]">
    +1rb
  </button>
  <button type="button" @click="amount += 10000"
          class="px-3 py-1.5 rounded-full text-xs font-mono-apple font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 active:scale-95 transition-transform min-h-[36px]">
    +10rb
  </button>
  <button type="button" @click="amount += 50000"
          class="px-3 py-1.5 rounded-full text-xs font-mono-apple font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 active:scale-95 transition-transform min-h-[36px]">
    +50rb
  </button>
  <button type="button" @click="amount += 100000"
          class="px-3 py-1.5 rounded-full text-xs font-mono-apple font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 active:scale-95 transition-transform min-h-[36px]">
    +100rb
  </button>
</div>
```

---

## 8. Mobile Typography & Density Discipline

### A. The Safari 16px Auto-Zoom Prevention Rule

> [!WARNING]
> In iOS Safari, any `<input>`, `<select>`, or `<textarea>` with a font size smaller than `16px` (`1rem`) triggers an automatic zoom-in when focused. This breaks responsive layout geometry and requires the user to pinch-to-zoom out.
> **All mobile input fields MUST declare `font-size: 16px` at minimum.**

```css
/* Universal Mobile Input Fix */
input, select, textarea {
  font-size: 16px !important;
}
```

### B. Mobile Heading Scale
- **H1 Mobile Title**: `text-xl` (20px) or max `text-2xl` (24px).
- **Metric Big Numbers**: `text-3xl` (28px) or `text-4xl` (32px) with `.font-mono-apple` and `tabular-nums`.
- **Labels & Micro-Copy**: `text-xs` (12px) or `text-[11px]` with `font-semibold`.

---

## 9. Mobile Data Cards & Accordion Lists

On mobile screens, long transaction records or audit lists must avoid horizontally stretched tables. Wrap records into **Tactile Bento List Items (`.card-press`)**:

```html
<!-- Mobile Transaction Item -->
<div class="p-3.5 rounded-2xl bg-white border border-black/[0.06] shadow-xs flex items-center justify-between gap-3 active:scale-[0.98] transition-transform cursor-pointer">
  <!-- Left: Category Icon + Title -->
  <div class="flex items-center gap-3 min-w-0">
    <div class="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-600 flex items-center justify-center shrink-0">
      <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
      </svg>
    </div>
    <div class="min-w-0">
      <h4 class="text-sm font-bold text-slate-900 truncate">Servis Motherboard Asus</h4>
      <p class="text-[11px] text-slate-400">14:32 • Kas Utama</p>
    </div>
  </div>

  <!-- Right: Amount + Flow Indicator -->
  <div class="text-right shrink-0">
    <div class="text-sm font-black text-emerald-600 font-mono-apple tabular-nums">+Rp 350.000</div>
    <span class="inline-block px-1.5 py-0.5 rounded text-[9px] font-bold uppercase bg-emerald-50 text-emerald-600">
      Lunas
    </span>
  </div>
</div>
```

---

## 10. Complete Standalone Turnkey Mobile Shell

Below is the complete, single-file ready-to-run template embodying all handheld ergonomic laws:

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Kas Megapass - Handheld Mobile Shell</title>

  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>

  <style>
    [x-cloak] { display: none !important; }
    html, body {
      min-height: 100vh;
      min-height: 100dvh;
      overscroll-behavior-y: contain;
      -webkit-tap-highlight-color: transparent;
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      background-color: #F8FAFC;
    }
    input, select, textarea { font-size: 16px !important; }
    .font-mono-apple { font-family: 'JetBrains Mono', monospace; font-variant-numeric: tabular-nums; }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
  </style>
</head>
<body class="w-full text-slate-900 relative"
      x-data="{ activeTab: 'home', sheetOpen: false }">

  <!-- TOP APP BAR: Orientation Only -->
  <header class="fixed top-0 inset-x-0 h-14 bg-white/80 backdrop-blur-md border-b border-black/[0.06] z-30 flex items-center justify-between px-4">
    <div class="flex items-center space-x-2">
      <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
      <span class="font-extrabold text-sm tracking-tight">KAS MEGAPASS</span>
    </div>
    <span class="text-[11px] font-bold text-slate-400">Sidoarjo Ruko</span>
  </header>

  <!-- MAIN SCROLL CONTAINER: Bound to max-w-md with pb-32 clearance -->
  <main class="w-full min-h-screen pt-16 pb-32">
    <div class="w-full max-w-md mx-auto px-4 space-y-4">
      
      <!-- HERO SUMMARY CARD -->
      <section class="rounded-3xl bg-slate-900 text-white p-5 space-y-3 shadow-xl relative overflow-hidden">
        <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Saldo Kas Saat Ini</p>
        <p class="text-3xl font-black tracking-tight font-mono-apple">Rp 14.850.000</p>
        <div class="flex items-center gap-2 pt-1">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-400">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Surplus Bulan Ini +Rp 3.200.000
          </span>
        </div>
      </section>

      <!-- HORIZONTAL FILTER CAROUSEL -->
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1">
        <button class="px-3.5 py-1.5 rounded-full text-xs font-bold bg-[#0071E3] text-white shrink-0 min-h-[36px]">Semua</button>
        <button class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 shrink-0 min-h-[36px]">Pemasukan</button>
        <button class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 shrink-0 min-h-[36px]">Pengeluaran</button>
        <button class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white border border-black/[0.08] text-slate-600 shrink-0 min-h-[36px]">Piutang Servis</button>
      </div>

      <!-- TRANSACTION FEED -->
      <div class="space-y-2.5">
        <div class="p-3.5 rounded-2xl bg-white border border-black/[0.06] shadow-xs flex items-center justify-between gap-3 active:scale-[0.98] transition-transform">
          <div class="min-w-0">
            <h4 class="text-sm font-bold text-slate-900 truncate">Servis VGA GTX 1060</h4>
            <p class="text-[11px] text-slate-400">10:15 • Tunai</p>
          </div>
          <div class="text-sm font-black text-emerald-600 font-mono-apple">+Rp 250.000</div>
        </div>
      </div>

    </div>
  </main>

  <!-- FLOATING GLASS DOCK WITH CENTER FAB -->
  <nav class="fixed bottom-0 inset-x-0 z-40" style="padding-bottom: env(safe-area-inset-bottom)">
    <div class="mx-3 mb-3 backdrop-blur-xl bg-white/80 border border-white/60 shadow-2xl rounded-3xl relative">
      <div class="absolute left-1/2 -translate-x-1/2 -top-7 z-[60]">
        <div class="p-1.5 backdrop-blur-xl bg-white/60 rounded-full shadow-md border border-white/50">
          <button @click="sheetOpen = true" type="button"
                  class="w-13 h-13 rounded-full bg-[#0071E3] text-white shadow-lg grid place-items-center active:scale-90 transition-all cursor-pointer"
                  style="width: 3.25rem; height: 3.25rem;">
            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>
      </div>
      <div class="relative flex flex-row items-center h-16 pointer-events-auto">
        <button @click="activeTab = 'home'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'home' ? 'text-[#0071E3]' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          <span class="text-[10px] font-bold">Beranda</span>
        </button>
        <button @click="activeTab = 'tx'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'tx' ? 'text-[#0071E3]' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>
          <span class="text-[10px] font-medium">Transaksi</span>
        </button>
        <div class="w-1/5 flex-none h-full pointer-events-none"></div>
        <button @click="activeTab = 'reports'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'reports' ? 'text-[#0071E3]' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.21 15.89A10 10 0 1 1 8 2.83M22 12A10 10 0 0 0 12 2v10z"/></svg>
          <span class="text-[10px] font-medium">Laporan</span>
        </button>
        <button @click="activeTab = 'settings'" class="flex flex-col items-center justify-center gap-1 h-full w-1/5 flex-none" :class="activeTab === 'settings' ? 'text-[#0071E3]' : 'text-slate-400'">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span class="text-[10px] font-medium">Setting</span>
        </button>
      </div>
    </div>
  </nav>

</body>
</html>
```

---

## 11. Mobile Handheld Ergonomics Pre-Flight Checklist

Before claiming any mobile layout or PWA is complete, verify these 8 mechanical criteria:

1. **Clearance Verification**:
   - The `<main>` scroll container has `pb-32` (128px) or higher padding to prevent bottom dock overlap.
2. **Safe-Area Verification**:
   - `padding-bottom: env(safe-area-inset-bottom)` is applied to all fixed bottom bars.
3. **Touch Target Verification**:
   - Every single interactive button, tab, and chip has `min-height: 40px` (ideally `min-h-[44px]` or `min-h-[48px]`).
4. **iOS Auto-Zoom Prevention**:
   - Every `<input>`, `<select>`, and `<textarea>` has `font-size: 16px` at minimum.
5. **No Vertical Chip Wrapping**:
   - Filter chips and categories use horizontal scroll carousels (`flex overflow-x-auto no-scrollbar`), never multiline wrapping.
6. **Bottom Sheet Dialogs**:
   - Modals on mobile anchor to the bottom edge (`flex items-end rounded-t-3xl`), with a visual grab handle pill.
7. **Constraint Bounds**:
   - Mobile body/main container is constrained to `max-w-md mx-auto` to prevent stretched layouts on tablets and foldables.
8. **Tactile Haptic Feedback**:
   - Buttons have `active:scale-95` or `active:scale-[0.97]` with 100ms - 150ms transitions.
