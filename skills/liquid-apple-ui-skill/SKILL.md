---
name: liquid-apple-ui-skill
description: "Apple-inspired Cupertino liquid crystal UI v2.0 design system: iridescent ambient mesh canvas (#F5F5F7), frosted translucent glass cards (backdrop-blur 32px), soft dual-shadow neumorphism (.neo-groove, .neo-tab-active), radial dial gauges, multi-segment waterfall timeline, radar scanning HUD, scoped transitions, concentric radii, and zero-bloat standalone Tailwind implementation without node_modules."
---

# Liquid Apple UI Skill (v2.0)

Design system and frontend engineering patterns for crafting authentic Apple Cupertino-caliber light liquid crystal interfaces without heavyweight framework dependencies (React, Next.js, or runtime `node_modules`).

Directly reverse-engineered and extracted from the production-tested **AGY Router** mission-control console and **CekWeb Megapass** workbench applications.

---

## 1. Cupertino Canvas & Color Palette Tokens

Strictly avoid generic dark hacker themes or flat muddy grays. The authentic Apple aesthetic uses an ultra-clean platinum foundation (`#F5F5F7`), dynamic ambient iridescent mesh gradients, and translucent frosted glass cards.

### Core Tokens & Variables

```css
:root {
  --apple-blue: #0071E3;
  --apple-blue-hover: #0077ED;
  --apple-indigo: #5E5CE6;
  --apple-mint: #30D158;
  --apple-orange: #FF9F0A;
  --apple-pink: #FF375F;
  --apple-purple: #BF5AF2;
  --apple-teal: #64D2FF;
  --text-primary: #1D1D1F;
  --text-secondary: #86868B;
}
```

### Surface & Depth Hierarchy Table

| Component Level | Visual Specification | Styling Class / CSS | Semantic Purpose |
|---|---|---|---|
| **Ambient Canvas** | `#F5F5F7` + Iridescent Mesh Radial Gradients | `.apple-ambient-canvas` | Deepest foundation layer; dynamic color hints at 5 coordinate points |
| **Frosted Glass Cards** | `rgba(255,255,255,0.88)` + `blur(32px) saturate(190%)` | `.crystal-card` | Main content panels, data containers, and fixed sidebar navigation |
| **Hero Crystal Island** | 135deg gradient `rgba(255,255,255,0.96)` ➔ `rgba(244,248,255,0.92)` | `.hero-crystal` | Top-level active status banner, widget islands, elevated cards |
| **Neomorphic Inset Groove** | Sunken ambient inset shadow + 1px white bottom highlight | `.neo-groove` | Recessed segmented track, tab wells, gauge slots |
| **Neomorphic Active Pill** | Crisp elevated drop shadow + 1px white top highlight | `.neo-tab-active` | Selected tab state, active toggle switch, convex buttons |
| **Neomorphic Crystal Box** | Dual specular highlight + frosted backdrop blur 24px | `.neo-crystal-box` | GTmetrix grade boxes, telemetry plaques, metric plaques |
| **Primary Tactile Button** | `#0077ED` ➔ `#0066CC` gradient + 1px white top inset | `.btn-apple-blue` | Main call-to-action with Cupertino spring click haptics |
| **Tactile Pill Button** | `rgba(255,255,255,0.94)` + border `rgba(0,0,0,0.08)` | `.btn-apple-pill` | Secondary controls, modal triggers, segmented buttons |
| **Tactile Action Chip** | Micro-scaling `scale(0.95)` with cubic-bezier dampening | `.btn-tactile` | Interactive chips, copy buttons, dropdown items, switches |
| **Sidebar Navigation** | Dynamic active gradient `#0077ED` ➔ `#0066CC` | `.nav-item` / `.nav-item.active` | Left rail navigation with subtle horizontal sliding |
| **Form Inputs & Search** | `bg-white/95` + Neomorphic recessed well + blue glow ring | `.apple-input` | Clean form controls with keyboard shortcut badges |
| **Progress Meters** | Silk flow ease with inset track shadow | `.fuel-progress-fill` + `.apple-meter-track` | Quota visualizers, usage histograms, fuel gauges |
| **Fluid Scrollbar** | Native slim 5px translucent track | `::-webkit-scrollbar` | Discrete, unobtrusive scrolling for cards and timelines |

---

## 2. Background Architecture: Ambient Iridescent Mesh

The hallmark of the AGY Router canvas is the 5-point fixed iridescent mesh. It mimics light refraction through liquid crystal without burning GPU cycles:

```css
/* Ambient Dynamic Iridescent Mesh Canvas */
.apple-ambient-canvas {
  background-color: #F5F5F7;
  background-image: 
    radial-gradient(at 0% 0%, rgba(94, 92, 230, 0.14) 0px, transparent 45%),    /* Top-Left: Indigo */
    radial-gradient(at 100% 0%, rgba(0, 113, 227, 0.15) 0px, transparent 45%),  /* Top-Right: Apple Blue */
    radial-gradient(at 50% 30%, rgba(255, 159, 10, 0.10) 0px, transparent 50%), /* Center: Warm Amber */
    radial-gradient(at 100% 100%, rgba(48, 209, 88, 0.12) 0px, transparent 50%),/* Bottom-Right: Mint */
    radial-gradient(at 0% 100%, rgba(255, 55, 95, 0.11) 0px, transparent 45%);   /* Bottom-Left: Soft Pink */
  background-attachment: fixed;
}
```

Implementation in layout:
```html
<body class="min-h-screen flex apple-ambient-canvas selection:bg-[#0071E3] selection:text-white relative">
  <!-- Content -->
</body>
```

### Critical Anti-Pattern: The Opaque Container Trap (Sekring Wadah Solid)

> [!CAUTION]
> **DILARANG memberikan class background solid pada wrapper anak** (seperti `<div class="min-h-screen bg-[#F5F5F7]">`, `<main class="bg-gray-100">`, atau `<div class="bg-white">`).
> Menaruh background solid di container pembungkus konten akan **menutup total gradien iridescent mesh pada `<body>`**, membuat tampilan layu dan berubah menjadi abu-abu semen datar.
>
> **SOP Baku Wadah**:
> - Wrapper utama, `<main>`, dan kontainer halaman WAJIB transparan: `bg-transparent` atau tanpa deklarasi `bg-`.
> - Warna putih dan translusen HANYA boleh dipasang pada level kartu (`.crystal-card`, `bg-white/80`, `bg-white/88`, `bg-white/94`).

### Critical Anti-Pattern: The Conflicting Stylesheet Trap (`app.css` Shorthand Reset)

> [!WARNING]
> **DILARANG menghubungkan stylesheet eksternal generic/legacy** yang berisi reset shorthand seperti:
> ```css
> body { background: var(--bg); } /* SINTAKS RUSAK: Mereset background-image dan background-attachment! */
> ```
> Shorthand CSS `background:` otomatis menghapus nilai `background-image` dan `background-attachment: fixed` yang sudah diset oleh `.apple-ambient-canvas`.
>
> **SOP Baku CSS**:
> - Jangan load stylesheet eksternal yang memanipulasi tag `body` atau `html`.
> - Seluruh konfigurasi canvas, custom class, dan font WAJIB diletakkan di dalam blok `<style>` di `<head>` setelah pemanggilan Tailwind CDN.

---

## 3. Cupertino Physics & Animation Engine

Apple interfaces feel physical because interactive elements utilize damped spring physics (`cubic-bezier(0.16, 1, 0.3, 1)`):

### A. Spring Timing Functions

```css
/* The Cupertino Spring Formula */
transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
```
Never use browser-default `ease` or linear curves for clicks and hover states.

### B. Micro-Click Tactile Haptics

```css
/* Primary Blue Button with Inset Highlight */
.btn-apple-blue {
  background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
  color: #FFFFFF;
  font-weight: 700;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 4px 14px rgba(0, 113, 227, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.4);
  transition-property: transform, box-shadow, background;
  transition-duration: 150ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
  min-height: 36px;
}
.btn-apple-blue:hover {
  background: linear-gradient(180deg, #0A84FF 0%, #0071E3 100%);
  box-shadow: 0 6px 20px rgba(0, 113, 227, 0.38);
  transform: translateY(-0.5px);
}
.btn-apple-blue:active {
  transform: scale(0.96) translateY(0.5px);
}

/* Secondary Translucent Pill Button */
.btn-apple-pill {
  background: rgba(255, 255, 255, 0.94);
  color: #1D1D1F;
  font-weight: 600;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 9999px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 1);
  transition-property: transform, background-color, border-color, box-shadow;
  transition-duration: 150ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
  min-height: 32px;
}
.btn-apple-pill:hover {
  background: #FFFFFF;
  border-color: rgba(0, 0, 0, 0.16);
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05), inset 0 1px 0 rgba(255, 255, 255, 1);
  transform: translateY(-0.5px);
}
.btn-apple-pill:active {
  transform: scale(0.96) translateY(0.5px);
}

/* Universal Tactile Micro-Interactions (Chips, Badges, Icons) */
.btn-tactile {
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
  transition-property: transform, opacity, background-color, border-color, box-shadow;
  transition-duration: 140ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-tactile:hover {
  transform: translateY(-0.5px);
}
.btn-tactile:active {
  transform: scale(0.95);
}
```

### C. Sidebar Navigation Motion

```css
.nav-item {
  transition-property: background-color, color, transform, box-shadow;
  transition-duration: 150ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
}
.nav-item:hover {
  background-color: rgba(255, 255, 255, 0.85);
  transform: translateX(2px);
}
.nav-item:active {
  transform: scale(0.98) translateX(1px);
}
.nav-item.active {
  background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
  color: #FFFFFF !important;
  box-shadow: 0 4px 16px rgba(0, 113, 227, 0.32), inset 0 1px 0 rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.25);
}
.nav-item.active:hover {
  background: linear-gradient(180deg, #0A84FF 0%, #0071E3 100%);
  color: #FFFFFF !important;
  transform: translateX(0);
}
```

### D. Silk Flow Progress Meters

Smooth fuel gauge animations for quota counters and token capacity:

```css
.fuel-progress-fill {
  transition: width 650ms cubic-bezier(0.16, 1, 0.3, 1), background-color 300ms ease;
  background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.22) 0%, rgba(0, 0, 0, 0.04) 100%);
}
.apple-meter-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 9999px;
  padding: 2px;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.06);
}
```

---

## 4. Soft Cupertino Neomorphism & Inset Grooves

Apple neumorphism is radically different from the failed 2020 Dribbble trend (muddy dark gray clay with excessive diagonal drop shadows that destroyed contrast and readability).

Authentic Apple Cupertino Neomorphism operates on clean platinum (`#F5F5F7` / `rgba(0,0,0,0.035)`) and follows the physical optics of a **12 o'clock overhead light source** (top-down lighting):
1. **Top Ambient Occlusion**: Soft micro-inset shadow at the top rim representing depth and shadow cast by the bezel edge.
2. **Bottom Specular Reflection**: Crisp 1px pure white (`rgba(255,255,255,0.95)`) highlight at the bottom edge, simulating a CNC-milled chamfer or polished aluminum lip catching overhead room light.

### A. Core Neomorphic Classes & Shadow Physics

```css
/* Neomorphic Inset Groove & Recessed Wells (Segmented Track & Inset Bases) */
.neo-groove {
  background: rgba(0, 0, 0, 0.035);
  border: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow: 
    inset 0 2px 4px rgba(0, 0, 0, 0.04), 
    inset 0 1px 2px rgba(0, 0, 0, 0.02), 
    0 1px 0 rgba(255, 255, 255, 0.95);
}

/* Neomorphic Active Pill (Convex Elevated Tab State) */
.neo-tab-active {
  background: #FFFFFF !important;
  color: #0F172A !important;
  border: 1px solid rgba(0, 0, 0, 0.06) !important;
  box-shadow: 
    0 2px 8px rgba(0, 0, 0, 0.06), 
    0 1px 2px rgba(0, 0, 0, 0.03), 
    inset 0 1px 0 #FFFFFF !important;
}

/* Neomorphic Frosted Crystal Box (Grade Plaques & Dial Pedestals) */
.neo-crystal-box {
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  box-shadow: 
    0 4px 14px rgba(0, 0, 0, 0.03), 
    inset 0 1px 0 rgba(255, 255, 255, 0.9), 
    inset 0 -1px 0 rgba(0, 0, 0, 0.03);
  transition-property: background-color, border-color, box-shadow;
  transition-duration: 180ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

/* Tactile Form Inputs (Neomorphic Recessed Well) */
.apple-input {
  background: rgba(255, 255, 255, 0.94);
  border: 1px solid rgba(0, 0, 0, 0.09);
  box-shadow: 
    inset 0 2px 4px rgba(0, 0, 0, 0.03), 
    inset 0 1px 2px rgba(0, 0, 0, 0.02), 
    0 1px 0 rgba(255, 255, 255, 0.9);
  transition-property: border-color, box-shadow, background-color;
  transition-duration: 140ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.apple-input:focus {
  background: #FFFFFF;
  border-color: #0071E3;
  box-shadow: 
    0 0 0 3.5px rgba(0, 113, 227, 0.16), 
    inset 0 1px 2px rgba(0, 0, 0, 0.02), 
    0 1px 0 rgba(255, 255, 255, 1);
}

/* Primary Tactile Brand Button with Extruded Neomorphic Bevel */
.btn-apple-brand {
  background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.35);
  box-shadow: 
    0 4px 14px rgba(0, 113, 227, 0.30), 
    0 1px 2px rgba(0, 0, 0, 0.08), 
    inset 0 1px 0 rgba(255, 255, 255, 0.45), 
    inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  transition-property: transform, box-shadow, filter, background;
  transition-duration: 140ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: manipulation;
  cursor: pointer;
  user-select: none;
}
.btn-apple-brand:hover {
  filter: brightness(1.03);
  box-shadow: 
    0 6px 20px rgba(0, 113, 227, 0.38), 
    inset 0 1px 0 rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
}
.btn-apple-brand:active {
  transform: scale(0.975) translateY(0.5px);
  filter: brightness(0.95);
  box-shadow: 
    0 1px 4px rgba(0, 113, 227, 0.20), 
    inset 0 2px 4px rgba(0, 0, 0, 0.20);
}
```

### B. Segmented Neomorphic Tab Switcher (HTML Pattern)

Concentric radii formula applied: Outer groove (`rounded-2xl` / 16px) with `p-1.5` (6px) wraps inner tabs (`rounded-xl` / 10-12px):

```html
<div class="neo-groove p-1.5 rounded-2xl inline-flex items-center gap-1">
  <!-- Active Tab: Elevated Convex Pill -->
  <button type="button"
          class="neo-tab-active px-4 py-2 rounded-xl text-xs font-bold transition-[color,background-color,border-color,box-shadow,transform] duration-140 ease-out btn-tactile min-h-[40px]">
    Mode Audit Tunggal
  </button>
  <!-- Inactive Tab: Flat Unselected -->
  <button type="button"
          class="px-4 py-2 rounded-xl text-xs font-bold text-slate-500 hover:text-slate-900 transition-[color,background-color,border-color,box-shadow,transform] duration-140 ease-out btn-tactile min-h-[40px]">
    Mode Komparasi
  </button>
</div>
```

### C. Neomorphic Grade Plaque / Telemetry Box

High-density visual card blending crystal backdrop blur with subtle top and bottom chamfer lines:

```html
<div class="neo-crystal-box p-4 rounded-2xl bg-white/60 border border-black/[0.05] flex items-center justify-between">
  <div>
    <div class="text-[10px] font-black uppercase tracking-wider text-slate-400">GTmetrix Speed Grade</div>
    <div class="text-xl font-black text-slate-900">Grade A (98%)</div>
  </div>
  <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-600 flex items-center justify-center font-black text-sm">
    A
  </div>
</div>
```

---

## 5. Status Indicators & Dynamic Island Elements

### A. The "Liquid Pool" Brand Pill Badge
Signature capsule badge from AGY Router navigation bar:
```html
<span class="inline-flex items-center font-mono-apple text-[9.5px] font-bold tracking-wider uppercase px-2 py-0.5 rounded-full bg-[#0071E3]/[0.08] text-[#0071E3] border border-[#0071E3]/20">
  LIQUID POOL
</span>
```

### B. The "Primary Active" Radar Beacon Pill
Pulsing beacon chip indicating active real-time slot rotation:
```html
<span class="inline-flex items-center space-x-1.5 px-2 py-0.5 rounded-full text-[11px] sm:text-[13px] font-bold bg-[#30D158] text-white shadow-sm shadow-emerald-500/25">
  <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
  <span>PRIMARY ACTIVE</span>
</span>
```

### C. Apple Dynamic Island Toast Notification
Capsule notification dropping down from top-center with realistic optical spring:
```html
<div x-show="toast.visible" x-cloak
     x-transition:enter="transition ease-out duration-300 transform"
     x-transition:enter-start="opacity-0 -translate-y-6 scale-90"
     x-transition:enter-end="opacity-100 translate-y-0 scale-100"
     x-transition:leave="transition ease-in duration-200 transform"
     x-transition:leave-start="opacity-100 scale-100"
     x-transition:leave-end="opacity-0 -translate-y-6 scale-90"
     class="fixed top-6 left-1/2 -translate-x-1/2 z-[9999] flex items-center space-x-3 px-6 py-3 rounded-full bg-[#1A1A1E] text-white shadow-2xl border border-white/20 backdrop-blur-2xl text-xs font-semibold tracking-wide pointer-events-none">
  <div class="w-4 h-4 rounded-full bg-[#30D158] flex items-center justify-center flex-shrink-0">
    <svg class="w-2.5 h-2.5 text-black" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>
    </svg>
  </div>
  <span class="text-white text-xs font-medium" x-text="toast.message"></span>
</div>
```

---

## 6. Modal & Dialog Windows (Frosted Glass Sheet)

AGY Router Changelog and About dialogs use multi-stage layered frosted glass with deep drop shadows:

```html
<!-- Modal Backdrop -->
<div x-show="showModal" x-cloak
     class="fixed inset-0 z-[110] flex items-center justify-center p-3 sm:p-4 bg-black/60 backdrop-blur-md"
     x-transition:enter="transition ease-out duration-200"
     x-transition:enter-start="opacity-0"
     x-transition:enter-end="opacity-100"
     x-transition:leave="transition ease-in duration-150"
     x-transition:leave-start="opacity-100"
     x-transition:leave-end="opacity-0">

  <!-- Crystal Modal Dialog Card -->
  <div class="crystal-card p-0 max-w-2xl w-full max-h-[88vh] flex flex-col shadow-2xl border-white/95 overflow-hidden"
       @click.away="showModal = false"
       x-transition:enter="transition ease-out duration-250 transform"
       x-transition:enter-start="opacity-0 scale-95 translate-y-3"
       x-transition:enter-end="opacity-100 scale-100 translate-y-0"
       x-transition:leave="transition ease-in duration-150 transform"
       x-transition:leave-start="opacity-100 scale-100 translate-y-0"
       x-transition:leave-end="opacity-0 scale-95 translate-y-3">

    <!-- Modal Header -->
    <div class="px-5 py-4 sm:px-6 sm:py-5 border-b border-black/[0.06] bg-white/80 backdrop-blur-xl flex items-center justify-between gap-3 flex-shrink-0">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-2xl bg-blue-50/80 border border-blue-200/80 text-[#0071E3] flex items-center justify-center shadow-xs flex-shrink-0">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <div>
          <h3 class="font-bold text-base text-[#1D1D1F] tracking-tight">Dialog Title</h3>
          <p class="text-xs text-[#86868B]">Subtext description with crisp readability</p>
        </div>
      </div>

      <button @click="showModal = false" type="button"
              class="w-8 h-8 rounded-full bg-black/[0.04] hover:bg-black/[0.08] active:scale-95 text-[#86868B] hover:text-[#1D1D1F] flex items-center justify-center transition-colors cursor-pointer">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Modal Body (Scrollable with Fluid Scrollbar) -->
    <div class="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4 bg-[#F5F5F7]/40 text-xs">
      <p class="text-[#1D1D1F] leading-relaxed">Translucent frosted glass body content.</p>
    </div>

    <!-- Modal Footer -->
    <div class="px-5 py-3.5 sm:px-6 sm:py-4 border-t border-black/[0.06] bg-white/90 backdrop-blur-xl flex items-center justify-between flex-shrink-0">
      <span class="text-[11px] text-[#86868B] font-mono-apple">Status message</span>
      <button @click="showModal = false" type="button" class="btn-apple-pill px-5 py-2 text-xs font-bold cursor-pointer">
        Tutup
      </button>
    </div>
  </div>
</div>
```

---

## 7. Cupertino Form Controls & Segmented Switches

Authentic Apple controls prioritize optical softness, crystal transparency, and clear focus state geometry:

### A. Apple Search Bar with Keyboard Shortcut Badge

A clean search bar with high contrast placeholder and physical slash (`/`) hotkey tag:

```html
<div class="relative w-full max-w-md">
  <svg class="w-4 h-4 text-[#86868B] absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="11" cy="11" r="8"></circle>
    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
  </svg>
  <input type="text"
         placeholder="Filter records, domains, or logs..."
         class="w-full bg-white/95 border border-black/[0.08] focus:border-[#0071E3] focus:ring-4 focus:ring-[#0071E3]/10 rounded-xl pl-10 pr-9 py-2 text-xs font-mono-apple text-[#1D1D1F] placeholder:text-[#86868B] transition-[border-color,box-shadow] duration-140 ease-out outline-none min-h-[38px]">
  <kbd class="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] font-mono font-medium text-[#86868B] bg-black/[0.04] px-1.5 py-0.5 rounded border border-black/[0.06] pointer-events-none">/</kbd>
</div>
```

### B. Standard Form Input & Select with Apple Glow Ring

Never use harsh dark blue rings or square borders. Apple focus rings are subtle 4px halos with 10% opacity:

```html
<!-- Text Input -->
<div class="space-y-1.5">
  <label class="text-xs font-semibold text-[#1D1D1F]">Target Hostname</label>
  <input type="text"
         class="w-full bg-white/95 border border-black/[0.08] rounded-xl px-3.5 py-2.5 text-xs text-[#1D1D1F] placeholder:text-[#86868B] focus:outline-none focus:border-[#0071E3] focus:ring-4 focus:ring-[#0071E3]/10 transition-[border-color,box-shadow] duration-140 ease-out min-h-[40px]">
</div>

<!-- Select Dropdown -->
<div class="space-y-1.5">
  <label class="text-xs font-semibold text-[#1D1D1F]">Record Type</label>
  <select class="w-full bg-white/95 border border-black/[0.08] rounded-xl px-3.5 py-2.5 text-xs text-[#1D1D1F] focus:outline-none focus:border-[#0071E3] focus:ring-4 focus:ring-[#0071E3]/10 transition-[border-color,box-shadow] duration-140 ease-out cursor-pointer min-h-[40px]">
    <option value="A">A Record (IPv4)</option>
    <option value="CNAME">CNAME Alias</option>
  </select>
</div>
```

### C. Apple Segmented Control (Pill Switch Tab)

Cupertino-style radio/tab switcher inside a sunken track with concentric radii ($R_{outer} = R_{inner} + P$):

```html
<div class="inline-flex p-1.5 rounded-[22px] bg-black/[0.03] border border-black/[0.05] gap-1">
  <!-- Active Tab -->
  <button type="button"
          class="px-4 py-2 rounded-[16px] text-xs font-bold bg-white text-[#1D1D1F] shadow-xs border border-black/[0.04] transition-[color,background-color,border-color,box-shadow,transform] duration-140 ease-out btn-tactile min-h-[40px]">
    Active View
  </button>
  <!-- Inactive Tab -->
  <button type="button"
          class="px-4 py-2 rounded-[16px] text-xs font-medium text-[#86868B] hover:text-[#1D1D1F] hover:bg-black/[0.02] border border-transparent transition-[color,background-color,border-color,box-shadow,transform] duration-140 ease-out btn-tactile min-h-[40px]">
    Archived
  </button>
</div>
```

---

## 8. The Pure Light Crystal Discipline (Strict Anti-Dark Mode Mandate)

> [!IMPORTANT]
> **AGY Router DNA adalah 100% Light Crystal (Daylight Cupertino).**
> Estetika Liquid Apple dirancang khusus untuk refraksi cahaya kristal di atas latar platinum `#F5F5F7` dengan saturasi 190%. Mencampur dark mode merusak kalibrasi kontras dan membebani template dengan bloat utility classes.

### Aturan Disiplin Anti-Dark Mode:
1. **Dilarang Menambahkan `darkMode: 'class'`**:
   Dalam inisialisasi script Tailwind Play:
   ```javascript
   tailwind.config = {
     // DILARANG: darkMode: 'class',
     theme: { ... }
   }
   ```
2. **Dilarang Menulis Class Prefiks `dark:`**:
   Semua class `dark:bg-...`, `dark:text-...`, `dark:border-...` adalah **banned**. Jangan menyisakan residu dark mode pada template HTML.
3. **Dilarang Menyematkan Tombol Toggle Dark Theme**:
   Kecuali Cak secara eksplisit meminta switch mode gelap, jangan buat saklar tema matahari/bulan atau script `localStorage.getItem('theme')`.

---

## 9. Concentric Nested Radii & Optical Geometry Formula

To avoid awkward optical clashes, corner radii MUST be mathematically aligned based on nesting depth using Apple's concentric radius formula:

$$R_{outer} = R_{inner} + Padding$$

If an outer track container has `padding: 6px` (`p-1.5`) and an inner button has `border-radius: 16px` (`rounded-[16px]`), the outer container MUST have:
$$16\text{px} + 6\text{px} = 22\text{px} \rightarrow \text{rounded-[22px]}$$

### Concentric Pairing Cheatsheet:
- **Track `p-1.5` (6px gap)**: Outer `rounded-[22px]` wraps Inner `rounded-[16px]`.
- **Track `p-1` (4px gap)**: Outer `rounded-[20px]` wraps Inner `rounded-[16px]`, or Outer `rounded-[16px]` wraps Inner `rounded-[12px]`.
- **Card Wrapper**: Outer `rounded-3xl` (24px) wraps child Bento boxes `rounded-2xl` (16px to 20px).
- **Pills & Badges**: Fully circular `rounded-full` (9999px) for capsule chips and beacons.

### Typography Stack
- **Prose & Headings**: `-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', 'Nunito', 'SF Pro Text', system-ui, sans-serif` with `-0.015em` letter-spacing on titles.
- **Data & Numbers**: `'JetBrains Mono', -apple-system-monospaced, monospace` with `font-variant-numeric: tabular-nums` (`.font-mono-apple`).

---

## 10. Radial Circular Dial Gauge & Rolling Number Engine

For audit platforms, benchmarks, sensor HUDs, or telemetry monitors, use this high-precision SVG radial dial gauge with rolling number interpolation:

### A. SVG Dial Gauge Component (Centered Layout)

```html
<div class="relative flex flex-col items-center justify-center p-6 crystal-card rounded-3xl"
     x-data="{ animatedScore: 0, targetScore: 92 }"
     x-init="
       let start = null;
       const duration = 1200;
       function step(timestamp) {
         if (!start) start = timestamp;
         const progress = Math.min((timestamp - start) / duration, 1);
         const easeOut = 1 - Math.pow(1 - progress, 3);
         animatedScore = Math.round(easeOut * targetScore);
         if (progress < 1) {
           window.requestAnimationFrame(step);
         }
       }
       window.requestAnimationFrame(step);
     ">
  
  <div class="relative w-36 h-36 flex items-center justify-center">
    <!-- SVG Circular Arc Track & Meter -->
    <svg class="w-full h-full -rotate-90 transform" viewBox="0 0 100 100">
      <!-- Background Track Circle -->
      <circle cx="50" cy="50" r="45" stroke="rgba(0,0,0,0.06)" stroke-width="8" fill="transparent"/>
      <!-- Dynamic Progress Arc (Circumference = 2 * PI * 45 = 282.74) -->
      <circle cx="50" cy="50" r="45"
              stroke="url(#dial-gradient)"
              stroke-width="8"
              stroke-linecap="round"
              fill="transparent"
              stroke-dasharray="282.74"
              :stroke-dashoffset="282.74 - (282.74 * (animatedScore / 100))"
              class="transition-[stroke-dashoffset] duration-500 ease-out"/>
      <defs>
        <linearGradient id="dial-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#10B981"/>
          <stop offset="100%" stop-color="#059669"/>
        </linearGradient>
      </defs>
    </svg>

    <!-- Centered Score Display & Rolling Number -->
    <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
      <span class="text-4xl font-black font-nunito tracking-tight text-slate-900 tabular-nums"
            x-text="animatedScore">0</span>
      <span class="text-[10.5px] font-extrabold uppercase tracking-wider text-slate-400 -mt-1">/ 100</span>
    </div>
  </div>

  <!-- Anchored Grade Badge -->
  <div class="mt-3">
    <span class="px-3 py-1 rounded-xl text-xs font-black bg-emerald-100/90 text-emerald-800 border border-emerald-200 shadow-2xs">
      Grade A+
    </span>
  </div>
</div>
```

---

## 11. Multi-Segmented Waterfall Timeline & Metric Bento Cards

For visual breakdown of multi-phase operations (e.g. TTFB, DNS, TCP handshake, data transfer):

### A. Animated Multi-Color Waterfall Bar

```html
<div class="space-y-3 p-5 rounded-3xl crystal-card">
  <div class="flex items-center justify-between">
    <span class="text-xs font-extrabold uppercase tracking-wider text-slate-700">Waterfall Alur Waktu Respon</span>
    <span class="text-xs font-bold text-slate-500 tabular-nums">Total: 342 ms</span>
  </div>

  <!-- Segmented Multi-Color Bar -->
  <div class="h-3 w-full rounded-full bg-black/[0.05] p-0.5 flex gap-0.5 overflow-hidden shadow-inner">
    <!-- TTFB / Server Processing (Blue) -->
    <div class="h-full rounded-l-full bg-blue-500 transition-[flex,width] duration-700 ease-out"
         style="flex: 40;" title="TTFB Server: 136ms"></div>
    <!-- DNS Lookup (Purple) -->
    <div class="h-full bg-indigo-500 transition-[flex,width] duration-700 ease-out"
         style="flex: 15;" title="DNS Lookup: 51ms"></div>
    <!-- TCP Connect (Amber) -->
    <div class="h-full bg-amber-500 transition-[flex,width] duration-700 ease-out"
         style="flex: 20;" title="TCP Handshake: 68ms"></div>
    <!-- Content Download (Emerald) -->
    <div class="h-full rounded-r-full bg-emerald-500 transition-[flex,width] duration-700 ease-out"
         style="flex: 25;" title="Data Transfer: 87ms"></div>
  </div>

  <!-- 4-Column Micro-Detail Cards with Micro-Hover Lift -->
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
    <div class="p-2.5 rounded-2xl bg-black/[0.02] border border-black/[0.06] hover:border-black/[0.12] transition-[border-color,box-shadow,transform] duration-140 ease-out hover:-translate-y-0.5">
      <div class="text-[10px] font-extrabold uppercase text-blue-600">TTFB Server</div>
      <div class="text-xs font-black text-slate-900 tabular-nums">136 ms</div>
    </div>
    <div class="p-2.5 rounded-2xl bg-black/[0.02] border border-black/[0.06] hover:border-black/[0.12] transition-[border-color,box-shadow,transform] duration-140 ease-out hover:-translate-y-0.5">
      <div class="text-[10px] font-extrabold uppercase text-indigo-600">DNS Lookup</div>
      <div class="text-xs font-black text-slate-900 tabular-nums">51 ms</div>
    </div>
    <div class="p-2.5 rounded-2xl bg-black/[0.02] border border-black/[0.06] hover:border-black/[0.12] transition-[border-color,box-shadow,transform] duration-140 ease-out hover:-translate-y-0.5">
      <div class="text-[10px] font-extrabold uppercase text-amber-600">TCP Connect</div>
      <div class="text-xs font-black text-slate-900 tabular-nums">68 ms</div>
    </div>
    <div class="p-2.5 rounded-2xl bg-black/[0.02] border border-black/[0.06] hover:border-black/[0.12] transition-[border-color,box-shadow,transform] duration-140 ease-out hover:-translate-y-0.5">
      <div class="text-[10px] font-extrabold uppercase text-emerald-600">Transfer Data</div>
      <div class="text-xs font-black text-slate-900 tabular-nums">87 ms</div>
    </div>
  </div>
</div>
```

---

## 12. Radar Pulse Scanning HUD & Status Step Ticker

For long-running asynchronous tasks (auditing, server testing, deployment), use this Apple-styled radar scanning HUD instead of a generic spinning circle:

```html
<div class="p-8 rounded-3xl crystal-card-elevated flex flex-col items-center justify-center text-center space-y-4">
  <!-- Concentric Radar Sweeper -->
  <div class="relative w-24 h-24 flex items-center justify-center">
    <!-- Pinging Outer Rings -->
    <div class="absolute inset-0 rounded-full border-2 border-brand-500/20 animate-ping"></div>
    <div class="absolute inset-2 rounded-full border border-brand-500/30"></div>
    <div class="absolute inset-5 rounded-full border border-brand-500/40"></div>
    
    <!-- Rotating Sweep Beam -->
    <div class="absolute inset-0 rounded-full border-2 border-t-brand-600 border-r-transparent border-b-transparent border-l-transparent animate-spin duration-1000"></div>

    <!-- Center Sensor Node -->
    <div class="w-3.5 h-3.5 rounded-full bg-brand-600 shadow-md shadow-brand-500/50"></div>
  </div>

  <div class="space-y-1">
    <h4 class="text-sm font-black text-slate-900 font-nunito">Memindai Target Jaringan...</h4>
    <p class="text-xs text-slate-500 font-medium" x-text="currentStepLog">Mengukur latensi socket & TTFB byte pertama...</p>
  </div>
</div>
```

---

## 13. Scoped Transitions Anti-Jank & Zero-Shift State Swaps

> [!CAUTION]
> **DILARANG MENGGUNAKAN `transition-all` BLANKET DI MANAPUN DALAM TEMPLATE!**
> Blanket `transition-all` memaksa engine layout browser menghitung ulang geometri halaman saat pengguna menggerakkan kursor, memicu lag dan stutter pada CPU i3/STB/ponsel entry-level.

### A. Scoped Transition Property Matrix

Selalu definisikan properti yang ditransisikan secara eksplisit:

| Komponen | Styling Transisi Scoped Baku | Timing & Durasi |
|---|---|---|
| **Buttons & Chips** | `transition-[color,background-color,border-color,box-shadow,transform]` | `duration-140 ease-out` |
| **Bento & Crystal Cards** | `transition-[border-color,box-shadow,transform]` | `duration-160 ease-out` |
| **Progress / Waterfall** | `transition-[flex,width]` | `duration-700 ease-out` |
| **Radial Dial Gauge** | `transition-[stroke-dashoffset,stroke]` | `duration-500 ease-out` |
| **Input Focus Rings** | `transition-[border-color,box-shadow]` | `duration-140 ease-out` |
| **Opacity & Popovers** | `transition-opacity` | `duration-150 ease-out` |

### B. Zero-Shift Cross-Fade Icon Wrapper

Saat tombol beralih status (misal dari "Salin" ke "Tersalin!"), jangan biarkan tombol melompat atau berubah lebar (Cumulative Layout Shift / CLS = 0). Bungkus ikon dalam kontainer simetris `w-4 h-4 relative`:

```html
<button @click="copyCode" class="btn-apple-pill px-4 py-2 text-xs font-bold flex items-center gap-2 btn-tactile min-h-[40px]">
  <!-- Fixed Symmetrical Icon Container -->
  <span class="relative w-4 h-4 flex items-center justify-center shrink-0">
    <svg x-show="!copied" class="absolute inset-0 transition-opacity" width="16" height="16" ...>
      <!-- Normal Icon -->
    </svg>
    <svg x-show="copied" x-cloak class="absolute inset-0 transition-opacity text-emerald-600" x-transition.opacity.duration.150ms width="16" height="16" ...>
      <!-- Checkmark Icon -->
    </svg>
  </span>
  <span x-text="copied ? 'Tersalin!' : 'Salin Data'"></span>
</button>
```

### C. Standard Standar Hit Area Fisik ($\ge 40$ px)
Pastikan setiap elemen yang dapat diklik (preset chips, tabs, selector nodes, submit buttons) memiliki class minimal `min-h-[40px]` hingga `min-h-[44px]` agar mudah ditekan jempol di perangkat mobile.

---

## 14. Headless OpenGraph Graphic Card Generator (Python Pillow 1200x630)

Untuk menghasilkan kartu grafis OpenGraph pratinjau sosial atau struk bukti servis fisik tanpa menjalankan browser emulator (Chromium/Puppeteer) yang memakan RAM ratusan megabyte:

```python
import io
from PIL import Image, ImageDraw, ImageFont

def buat_kartu_apple_crystal(data: dict) -> io.BytesIO:
    """Render kartu grafis audit 1200x630 px dalam <30ms via Pillow."""
    width, height = 1200, 630
    img = Image.new("RGB", (width, height), color=(15, 23, 42))  # Slate 900
    draw = ImageDraw.Draw(img)

    # Font fallback aman (Linux system font)
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_score = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except Exception:
        font_title = font_score = font_body = ImageFont.load_default()

    # Header Card
    draw.text((60, 50), "MEGAPASS INTRA SOLUSINDO", fill=(56, 189, 248), font=font_body)
    draw.text((60, 85), data.get("title", "Laporan Servis & Audit"), fill=(255, 255, 255), font=font_title)

    # Score Box Crystal
    draw.rectangle([(60, 160), (320, 480)], fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((105, 260), str(data.get("score", 95)), fill=(16, 185, 129), font=font_score)

    # Simpan ke stream buffer in-memory
    out = io.BytesIO()
    img.save(out, format="PNG", optimize=True)
    out.seek(0)
    return out
```

---

## 15. Zero-Bloat Standalone Stack & Pre-Flight Verification

### Checklist Arsitektur:
- [ ] Standalone Tailwind CSS dimuat via `<script src="https://cdn.tailwindcss.com"></script>`.
- [ ] Alpine.js dimuat via deferred script tag (`<script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>`).
- [ ] Zero `node_modules` di runtime server.
- [ ] Cold-start instan, pure client wire size < 60 KB.

### Pre-Flight Inspection (Wajib Verifikasi Sebelum Selesai):
1. **Verifikasi Transparansi Wrapper**:
   Pastikan tidak ada `<div class="bg-[#F5F5F7] ...">` atau `<main class="bg-...">` yang menutupi `apple-ambient-canvas` pada `<body>`.
2. **Verifikasi CSS Reset Body**:
   Pastikan tidak ada stylesheet eksternal (`app.css`) dengan rule `body { background: ...; }` yang merusak radial gradient dan `background-attachment: fixed`.
3. **Verifikasi Eliminasi `transition-all`**:
   Jalankan: `grep -rn "transition-all" templates/` wajib menghasilkan **0 hasil**.
4. **Verifikasi Residu Dark Mode**:
   Jalankan: `grep -rn "dark:" templates/` wajib menghasilkan **0 hasil**.
5. **Verifikasi Target Sentuh Mobile**:
   Setiap tombol interaktif wajib memenuhi `min-h-[40px]` atau `min-h-[44px]`.
6. **Verifikasi DOM Balance**:
   Selisih tag pembuka vs penutup `<div>`, `<section>`, `<nav>`, `<button>` harus sama dengan 0.
