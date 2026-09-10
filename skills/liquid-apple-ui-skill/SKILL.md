---
name: liquid-apple-ui-skill
description: "Apple-inspired Cupertino liquid crystal UI design system: iridescent ambient mesh canvas (#F5F5F7), frosted translucent glass cards (backdrop-blur 32px), Apple tactile spring buttons, dynamic status pills, zero-flicker Alpine.js transitions, and zero-bloat standalone Tailwind implementation without node_modules."
---

# Liquid Apple UI Skill

Design system and frontend engineering patterns for crafting authentic Apple Cupertino-caliber light liquid crystal interfaces without heavyweight framework dependencies (React, Next.js, or runtime `node_modules`).

Directly reverse-engineered and extracted from the production-tested **AGY Router** (`~/agy-router/templates/index.html`) mission-control console and **Megapass** workbench applications.

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
| **Primary Tactile Button** | `#0077ED` ➔ `#0066CC` gradient + 1px white top inset | `.btn-apple-blue` | Main call-to-action with Cupertino spring click haptics |
| **Tactile Pill Button** | `rgba(255,255,255,0.94)` + border `rgba(0,0,0,0.08)` | `.btn-apple-pill` | Secondary controls, modal triggers, segmented buttons |
| **Tactile Action Chip** | Micro-scaling `scale(0.95)` with cubic-bezier dampening | `.btn-tactile` | Interactive chips, copy buttons, dropdown items, switches |
| **Sidebar Navigation** | Dynamic active gradient `#0077ED` ➔ `#0066CC` | `.nav-item` / `.nav-item.active` | Left rail navigation with subtle horizontal sliding |
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

## 4. Status Indicators & Dynamic Island Elements

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

## 5. Modal & Dialog Windows (Frosted Glass Sheet)

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

## 6. Concentric Nested Radii & Typography Rules

To avoid awkward optical clashes, corner radii must be scaled concentrically based on nesting depth:

1. **Outer Modal / Main Page Wrapper**: `rounded-3xl` (24px)
2. **Elevated Panels & Crystal Cards**: `rounded-2xl` (20px)
3. **Inner Grouped Containers / Rows**: `rounded-xl` (12px)
4. **Action Buttons / Form Inputs**: `rounded-xl` (10px) or `rounded-lg` (8px)
5. **Pills & Badges**: `rounded-full` (9999px)

### Typography Stack
- **Prose & Headings**: `-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', 'SF Pro Text', system-ui, sans-serif` with `-0.015em` letter-spacing on titles.
- **Data & Numbers**: `'JetBrains Mono', -apple-system-monospaced, monospace` with `font-variant-numeric: tabular-nums` (`.font-mono-apple`).

---

## 7. Zero-Bloat Standalone Stack Checklist

- Standalone Tailwind CSS loaded via `<script src="https://cdn.tailwindcss.com"></script>`.
- Alpine.js loaded via deferred script tag (`<script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>`).
- Zero `node_modules` required at runtime.
- Fast initial cold-start, pure client wire size < 60 KB.
