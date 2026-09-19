---
name: liquid-apple-ui-skill
description: "Apple-inspired Cupertino liquid crystal UI v2.1 design system: iridescent ambient mesh canvas (#F5F5F7), frosted translucent glass cards (backdrop-blur 32px), soft dual-shadow neumorphism (.neo-groove, .neo-tab-active), glassmorphism + neumorphism harmonization matrix, radial dial gauges, multi-segment waterfall timeline, radar scanning HUD, scoped transitions, concentric radii, and zero-bloat standalone Tailwind implementation without node_modules."
---

# Liquid Apple UI Skill (v2.1)

Design system and frontend engineering patterns for crafting authentic Apple Cupertino-caliber light liquid crystal interfaces without heavyweight framework dependencies (React, Next.js, or runtime `node_modules`).

Directly reverse-engineered and extracted from the production-tested **AGY Router** mission-control console and **CekWeb Megapass** workbench applications.

---

## 1. Cupertino Canvas & Color Palette Tokens

Strictly avoid generic flat muddy grays. The authentic Apple light-mode aesthetic uses an ultra-clean platinum foundation (`#F5F5F7`), dynamic ambient iridescent mesh gradients, and translucent frosted glass cards. For dark mode tokens, see Section 10.

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
| **Frosted Glass Cards** | `rgba(255,255,255,0.92)` + `blur(32px) saturate(190%)` | `.crystal-card` | Main content panels, data containers, and fixed sidebar navigation |
| **Hero Crystal Island** | 135deg gradient `rgba(255,255,255,0.97)` ➔ `rgba(244,248,255,0.94)` | `.hero-crystal` | Top-level active status banner, widget islands, elevated cards |
| **Neomorphic Inset Groove** | Sunken ambient inset shadow + 1px white bottom highlight | `.neo-groove` | Recessed segmented track, tab wells, gauge slots |
| **Neomorphic Active Pill** | Crisp elevated drop shadow + 1px white top highlight | `.neo-tab-active` | Selected tab state, active toggle switch, convex buttons |
| **Neomorphic Crystal Box** | Dual specular highlight + frosted backdrop blur 24px | `.neo-crystal-box` | GTmetrix grade boxes, telemetry plaques, metric plaques |
| **Primary Tactile Button** | `#0077ED` ➔ `#0066CC` gradient + 1px white top inset | `.btn-apple-blue` | Main call-to-action with Cupertino spring click haptics |
| **Tactile Pill Button** | `rgba(255,255,255,0.94)` + border `rgba(0,0,0,0.08)` | `.btn-apple-pill` | Secondary controls, modal triggers, segmented buttons |
| **Tactile Action Chip** | Micro-scaling `scale(0.95)` with cubic-bezier dampening | `.btn-tactile` | Interactive chips, copy buttons, dropdown items, switches |
| **Sidebar Navigation** | Tinted translucent fill `rgba(brand, 0.12)` + brand text | `.nav-item` / `.nav-item.active` | Left rail navigation with subtle horizontal sliding |
| **Form Inputs & Search** | `bg-white/95` + Neomorphic recessed well + blue glow ring | `.apple-input` | Clean form controls with keyboard shortcut badges |
| **Progress Meters** | Silk flow ease with inset track shadow | `.fuel-progress-fill` + `.apple-meter-track` | Quota visualizers, usage histograms, fuel gauges |
| **Fluid Scrollbar** | Native 8px bordered translucent track + light/dark/hidden variants | `::-webkit-scrollbar` / `.custom-scrollbar` / `.custom-scrollbar-dark` / `.no-scrollbar` | Discrete, unobtrusive scrolling for cards, terminals, and timelines |

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

## 3. Liquid Glassmorphism Surface Architecture

Cupertino glassmorphism is not a simple generic blur. It is an optical simulation of high-transmission frosted crystal acrylic: high light refraction, ambient iridescent colors shining through, and sharp specular chamfer reflections along the perimeter edges.

Directly extracted from the production architecture of **AGY Router** (`http://localhost:7890/`) and **CekWeb Megapass** (`https://cekweb.megapass.web.id/`).

### A. The Standard Frosted Crystal Card (`.crystal-card`)
The workhorse container for content panels, telemetry tables, and navigation sidebars:

```css
.crystal-card {
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(32px) saturate(190%);
  -webkit-backdrop-filter: blur(32px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.98);
  border-radius: 20px;
  box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.02),
    0 4px 12px -2px rgba(0, 0, 0, 0.04),
    0 8px 24px -4px rgba(0, 113, 227, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 1),
    inset 0 -1px 0 rgba(0, 0, 0, 0.02);
  transition-property: transform, box-shadow, border-color;
  transition-duration: 180ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.crystal-card:not(aside):hover {
  box-shadow:
    0 2px 4px rgba(0, 0, 0, 0.02),
    0 8px 24px -4px rgba(0, 0, 0, 0.05),
    0 16px 40px -8px rgba(0, 113, 227, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 1),
    inset 0 -1px 0 rgba(0, 0, 0, 0.02);
}
```

### B. The Hero Crystal Island (`.hero-crystal` & `.crystal-card-elevated`)
The flagship centerpiece panel used for mission status banners, widget islands, and primary audit modules:

```css
/* AGY Router Hero Widget Island */
.hero-crystal {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.97) 0%, rgba(244, 248, 255, 0.94) 50%, rgba(254, 244, 249, 0.95) 100%);
  backdrop-filter: blur(40px) saturate(200%);
  -webkit-backdrop-filter: blur(40px) saturate(200%);
  border: 1.5px solid rgba(255, 255, 255, 1);
  border-radius: 24px;
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.02),
    0 8px 24px -4px rgba(0, 113, 227, 0.06),
    0 16px 48px -8px rgba(0, 113, 227, 0.08),
    inset 0 1px 1px rgba(255, 255, 255, 1),
    inset 0 -1px 0 rgba(0, 0, 0, 0.015);
}

/* CekWeb Elevated Centerpiece Card */
.crystal-card-elevated {
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(32px) saturate(200%);
  -webkit-backdrop-filter: blur(32px) saturate(200%);
  border: 1px solid rgba(255, 255, 255, 0.96);
  box-shadow: 
    0 20px 48px -12px rgba(0, 113, 227, 0.09), 
    0 8px 24px -4px rgba(0, 0, 0, 0.03), 
    inset 0 1px 0 rgba(255, 255, 255, 1),
    inset 0 -1px 0 rgba(0, 0, 0, 0.02);
  transition-property: transform, box-shadow, border-color;
  transition-duration: 180ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### C. The 4 Glass Optical Constants
1. **Saturate Boost (`saturate(190% - 200%)`)**: Without saturation boosting, browser blur algorithms desaturate the iridescent background into a muddy, milky haze. `saturate(190%)` preserves the dynamic colors of the underlying canvas.
2. **Specular Top Chamfer (`inset 0 1px 0 rgba(255, 255, 255, 1)`)**: Simulates the polished top edge of an acrylic block catching overhead light.
3. **Under-Bevel Ambient Occlusion (`inset 0 -1px 0 rgba(0, 0, 0, 0.02)`)**: A hairline 1px micro-shadow on the bottom edge that gives the floating glass slab physical thickness.
4. **Tinted Ambient Drop Shadow (`rgba(0, 113, 227, 0.05 - 0.09)`)**: Shadows are never harsh pure black; they carry a subtle 5% to 9% Apple blue dispersion tint matching natural light refraction.

---

## 4. Cupertino Physics & Animation Engine

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
  transform: scale(0.97) translateY(0.5px);
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
  background: rgba(0, 113, 227, 0.12);
  color: #0071E3;
  font-weight: 700;
  border: 1px solid rgba(0, 113, 227, 0.08);
  box-shadow: none;
}
.nav-item.active:hover {
  background: rgba(0, 113, 227, 0.18);
  transform: translateX(0);
}
.nav-item.active:active {
  transform: scale(0.98);
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
  background: rgba(0, 0, 0, 0.06);
  border-radius: 9999px;
  padding: 2px;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.08), inset 0 1px 1px rgba(0,0,0,0.04), 0 1px 0 rgba(255,255,255,0.9);
}
```

### E. Micro-Hover Tactile Data Rows (`.rack-row`)

In dense dashboards (e.g. AGY Router cluster node list, CekWeb server racks, or test history), table rows must provide subtle haptic feedback when hovered without causing layout shifts:

```css
.rack-row {
  transition-property: transform, border-color, background-color, box-shadow;
  transition-duration: 160ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.rack-row:hover {
  transform: translateY(-0.5px);
  box-shadow: 0 4px 16px -3px rgba(0, 113, 227, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 0.95);
}
```


### F. Scrollbar Variants (Light, Dark, No-Scrollbar)

Three scrollbar variants from AGY Router production. Global uses 8px width with bordered thumb for tactile visibility. `.custom-scrollbar` for inner card panels, `.custom-scrollbar-dark` for terminal/console containers, and `.no-scrollbar` for navigation rails.

```css
/* Native Apple Fluid Scrollbar (Global) */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.03); border-radius: 9999px; }
::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.25); border-radius: 9999px; border: 1px solid rgba(255, 255, 255, 0.6); background-clip: padding-box; }
::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.8); background-clip: padding-box; }
* { scrollbar-width: thin; scrollbar-color: rgba(0, 0, 0, 0.25) transparent; }

/* Inner Card Container Scrollbar (Light) */
.custom-scrollbar::-webkit-scrollbar { width: 7px; height: 7px; }
.custom-scrollbar::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.02); border-radius: 9999px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.25); border-radius: 9999px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.45); }
.custom-scrollbar { scrollbar-width: thin; scrollbar-color: rgba(0, 0, 0, 0.25) transparent; }

/* Dark Terminal Container Scrollbar */
.custom-scrollbar-dark::-webkit-scrollbar { width: 7px; height: 7px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.03); border-radius: 9999px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.25); border-radius: 9999px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.45); }
.custom-scrollbar-dark { scrollbar-width: thin; scrollbar-color: rgba(255, 255, 255, 0.25) transparent; }

/* Hide Scrollbar Completely */
.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
```

---

## 5. Soft Cupertino Neomorphism & Inset Grooves

Apple neumorphism is radically different from the failed 2020 Dribbble trend (muddy dark gray clay with excessive diagonal drop shadows that destroyed contrast and readability).

Authentic Apple Cupertino Neomorphism operates on clean platinum (`#F5F5F7` / `rgba(0,0,0,0.035)`) and follows the physical optics of a **12 o'clock overhead light source** (top-down lighting):
1. **Top Ambient Occlusion**: Soft micro-inset shadow at the top rim representing depth and shadow cast by the bezel edge.
2. **Bottom Specular Reflection**: Crisp 1px pure white (`rgba(255,255,255,0.95)`) highlight at the bottom edge, simulating a CNC-milled chamfer or polished aluminum lip catching overhead room light.

### A. Core Neomorphic Classes & Shadow Physics

```css
/* Neomorphic Inset Groove & Recessed Wells (Segmented Track & Inset Bases) */
.neo-groove {
  background: rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.08), inset 0 1px 1px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 12px;
}

/* Neomorphic Active Pill (Convex Elevated Tab State) */
.neo-tab-active {
  background: #FFFFFF !important;
  color: #1D1D1F !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -0.5px 0 rgba(0, 0, 0, 0.03) !important;
  border: 1px solid rgba(0, 0, 0, 0.06) !important;
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

## 6. The Glassmorphism + Neumorphism Harmonization Matrix

### A. The Core Optical Challenge & Cupertino Solution
- **Pure Glassmorphism Failure**: When interfaces only use frosted glass cards with floating icons and border outlines, elements feel ethereal, intangible, and flat. Interactive form wells cannot be distinguished from static containers.
- **Pure Neumorphism Failure (The 2020 Clay Trap)**: When interfaces only use extruded gray clay buttons and sunken wells, the screen feels claustrophobic, dark, and heavy. Contrast suffers and mobile readability collapses.
- **The Harmonious Symphony (AGY Router + CekWeb Megapass DNA)**:
  - **Glassmorphism acts as the Macroscopic Architecture (Macro)**: Sets the airy room atmosphere, iridescent ambient light passing through from behind, and floating crystal slabs.
  - **Neumorphism acts as the Microscopic Tactile Haptics (Micro)**: Carves precise mechanical wells, tactile buttons, switch tracks, and sensor pedestals inside the glass slabs.

```
       [Top-Down Ambient Light Source (12 O'Clock)]
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: Dynamic Island / Heads-Up Toast (#1A1A1E Glass)   │
└─────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: Hybrid Neomorphic Crystal Plaques (.neo-crystal-box)│
└─────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: Elevated Tactile Pills (.neo-tab-active, .btn-blue)│
└─────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: Sunken Neomorphic Grooves (.neo-groove, inputs)    │
└─────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: Floating Glass Slabs (.crystal-card, .hero-crystal)│
└─────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────┐
│ LAYER 0: Ground Platinum Canvas + 5-Point Iridescent Mesh   │
└─────────────────────────────────────────────────────────────┘
```

### B. The 5-Layer Physical Depth Stack

| Layer | Physical Analogy | Optical Properties | Classes Used | Production Reference |
|---|---|---|---|---|
| **Layer 0: Ground** | Workbench Surface | `#F5F5F7` with fixed 5-point ambient radial mesh | `.apple-ambient-canvas` | AGY Router + CekWeb canvas |
| **Layer 1: Floating Slab** | Milled Frosted Acrylic Sheet | Floating 6px above ground, `blur(32px) saturate(190%)`, white specular rim | `.crystal-card`, `.hero-crystal`, `.crystal-card-elevated` | AGY Router Hero & CekWeb Panels |
| **Layer 2: Sunken Socket** | CNC-Carved Well into the Acrylic | Sunken -2px, dark top shadow `inset 0 2px 4px`, bottom white reflection `0 1px 0` | `.neo-groove`, `.apple-input`, `.apple-meter-track` | CekWeb audit node switcher & input |
| **Layer 3: Tactile Pill** | Polished Ceramic / Aluminum Button | Elevated +2px inside the well, crisp drop shadow `0 2px 8px`, specular top highlight | `.neo-tab-active`, `.btn-apple-brand`, `.btn-apple-pill` | AGY Router quick chips & CekWeb tabs |
| **Layer 4: Hybrid Plaque** | Beveled Glass Telemetry Plaque | Acrylic blur (24px) + milled dual bevels (`inset 0 1px 0` & `inset 0 -1px 0`) | `.neo-crystal-box` | CekWeb GTmetrix grade plaques |
| **Layer 5: Heads-Up HUD** | Floating Sensor Capsule | Pitch-black crystal glass `#1A1A1E/90`, `backdrop-blur-2xl`, white border 20% | Dynamic Island Toast, Modal Backdrop | AGY Router real-time notification |

### C. The 4 Strict Harmonization Rules (Anti-Collisions)

1. **Rule 1: Never Stack Identical Blur on Identical Blur**:
   - DILARANG menaruh `.crystal-card` langsung di dalam `.crystal-card` tanpa membedakan opasitas atau background.
   - Jika membutuhkan kartu anak di dalam panel kaca:
     - Gunakan `.neo-groove` (parit cekung dengan latar `rgba(0,0,0,0.035)`), ATAU
     - Gunakan kartu semi-solid `bg-white/95 border border-black/[0.06] shadow-xs`.
   - Ini mencegah penumpukan blur yang membuat teks blur berkabut dan CPU i3/STB nge-drop.
2. **Rule 2: Light Angle Synchronicity (Mandat Jam 12 Overhead)**:
   - Semua bayangan inset (`inset 0 2px 4px`) WAJIB memiliki perpindahan vertikal positif (cahaya dari atas menyorot ke bawah).
   - Semua specular rim (`inset 0 1px 0 #FFFFFF`) WAJIB berada di sisi atas.
   - Semua highlight bibir parit (`0 1px 0 rgba(255,255,255,0.95)`) WAJIB berada di sisi bawah.
   - Jangan pernah mencampur bayangan diagonal miring 45° dari Neumorphism 2020.
3. **Rule 3: Transparency Hierarchy**:
   - Canvas: Background solid platinum `#F5F5F7` + mesh.
   - Card: 82% - 88% white opacity (membiarkan gradien mesh tembus).
   - Groove: 3.5% black opacity (menonjolkan cekungan di atas kartu kaca).
   - Active Tab: 100% solid white `#FFFFFF` (memastikan kontras teks hitam `#0F172A` terbaca tajam dan lulus audit accessibility WCAG AAA).
4. **Rule 4: Radius Nesting Alignment ($R_{outer} = R_{inner} + P$)**:
   - Jika `.crystal-card` luar bernilai `rounded-3xl` (24px), `.neo-groove` di dalamnya memakai `rounded-[22px]`, dan tombol `.neo-tab-active` di dalamnya memakai `rounded-[16px]`.

### D. Production Blueprint: Complete Component Showcase (Agy Router + CekWeb)

Here is how both live architectures weave together seamlessly in pure HTML + Tailwind CDN:

```html
<!-- LAYER 1: Main Glassmorphic Panel -->
<div class="crystal-card p-6 sm:p-8 rounded-3xl space-y-6 max-w-4xl mx-auto">
  
  <!-- Header with Live Beacon -->
  <div class="flex items-center justify-between">
    <div class="space-y-1">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center font-mono-apple text-[9.5px] font-bold tracking-wider uppercase px-2 py-0.5 rounded-full bg-[#0071E3]/[0.08] text-[#0071E3] border border-[#0071E3]/20">
          PROYEK FLAGSHIP
        </span>
        <h2 class="text-xl font-black text-slate-900 tracking-tight">Symphony Glass & Neumorphism</h2>
      </div>
      <p class="text-xs text-slate-500 font-medium">Harmonisasi material kaca kristal dan parit sentuh taktil.</p>
    </div>

    <!-- LAYER 4: Neomorphic Crystal Grade Plaque -->
    <div class="neo-crystal-box px-4 py-2 rounded-2xl bg-white/60 border border-black/[0.05] flex items-center gap-3">
      <div class="text-right">
        <div class="text-[9px] font-black uppercase text-slate-400">Status Sinyal</div>
        <div class="text-xs font-black text-emerald-600">STABIL 100%</div>
      </div>
      <div class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></div>
    </div>
  </div>

  <!-- LAYER 2 & 3: Neomorphic Tab Switcher inside Glass Card -->
  <div class="neo-groove p-1.5 rounded-[22px] inline-flex items-center gap-1 w-full sm:w-auto">
    <button type="button" class="neo-tab-active flex-1 sm:flex-initial px-5 py-2.5 rounded-[16px] text-xs font-bold btn-tactile min-h-[40px]">
      Konsol Utama
    </button>
    <button type="button" class="flex-1 sm:flex-initial px-5 py-2.5 rounded-[16px] text-xs font-bold text-slate-500 hover:text-slate-800 transition-[color,background-color,border-color,box-shadow,transform] duration-140 ease-out btn-tactile min-h-[40px]">
      Telemetri Jaringan
    </button>
  </div>

  <!-- LAYER 2 & 3: Neomorphic Form Well & Extruded Button -->
  <div class="flex flex-col sm:flex-row items-center gap-3">
    <div class="relative w-full">
      <input type="text"
             placeholder="Masukkan hostname target..."
             class="apple-input w-full rounded-2xl px-4 py-3 text-xs font-mono-apple text-slate-900 placeholder:text-slate-400 outline-none min-h-[44px]">
    </div>
    <button type="button" class="btn-apple-brand w-full sm:w-auto px-6 py-3 rounded-2xl text-xs font-bold flex items-center justify-center gap-2 whitespace-nowrap min-h-[44px]">
      <span>Jalankan Audit</span>
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
      </svg>
    </button>
  </div>
</div>
```

---

## 7. Status Indicators & Dynamic Island Elements

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
     style="top: max(1.5rem, calc(0.75rem + env(safe-area-inset-top)));"
     class="fixed left-1/2 -translate-x-1/2 z-[9999] flex items-center space-x-3 px-6 py-3 rounded-full bg-[#1A1A1E] text-white shadow-2xl border border-white/20 backdrop-blur-2xl text-xs font-semibold tracking-wide pointer-events-none">
  <div class="w-4 h-4 rounded-full bg-[#30D158] flex items-center justify-center flex-shrink-0">
    <svg class="w-2.5 h-2.5 text-black" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>
    </svg>
  </div>
  <span class="text-white text-xs font-medium" x-text="toast.message"></span>
</div>
```

---

## 8. Modal & Dialog Windows (Frosted Glass Sheet)

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

## 9. Cupertino Form Controls & Segmented Switches

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

### D. Button Radius Override Utilities & Image Outline

When buttons sit inside rectangular card contexts (non-pill layouts), override the default `rounded-full` with these utilities. `.img-outline` provides a subtle hairline border for screenshots and preview images without affecting image dimensions.

```css
/* Radius Override Utilities for Rectangular Contexts */
.btn-apple-blue.rounded-2xl, .btn-apple-pill.rounded-2xl { border-radius: 16px !important; }
.btn-apple-blue.rounded-xl, .btn-apple-pill.rounded-xl { border-radius: 12px !important; }

/* Clean Image Outline for Screenshots & Previews */
img.img-outline { outline: 1px solid rgba(0, 0, 0, 0.08); outline-offset: -1px; }
```

---

## 10. Dual-Mode Light & Dark Crystal Discipline

> [!NOTE]
> **Proyek boleh memilih salah satu dari tiga mode operasional:**
> 1. **Light-Only (AGY Router DNA)**: Gunakan hardcoded values dari Section 1-9 tanpa CSS variables. Tidak ada toggle tema.
> 2. **Dual-Mode (Skill Hub DNA)**: Gunakan CSS custom properties (`var(--token)`) agar semua surface classes otomatis beradaptasi saat class `.dark` ditambahkan ke `<html>`. Wajib pakai `darkMode: 'class'` di Tailwind config.
> 3. **Dark-Only**: Gunakan dark token values secara hardcoded. Jarang dipakai.

### A. Dual-Mode CSS Custom Properties Token Table

```css
/* Light tokens (default) */
:root {
  --bg-page: #F5F5F7;
  --text-primary: #1D1D1F;
  --text-secondary: #86868B;
  --card-bg: rgba(255, 255, 255, 0.92);
  --card-border: rgba(255, 255, 255, 0.98);
  --hero-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.97) 0%, rgba(244, 248, 255, 0.94) 50%, rgba(254, 244, 249, 0.95) 100%);
  --hero-border: rgba(255, 255, 255, 1);
  --card-shadow: 0 1px 1px rgba(0, 0, 0, 0.02), 0 4px 12px -2px rgba(0, 0, 0, 0.04), 0 8px 24px -4px rgba(0, 113, 227, 0.05), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
  --card-shadow-hover: 0 2px 4px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 0, 0, 0.05), 0 16px 40px -8px rgba(0, 113, 227, 0.08), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
  --topbar-bg: rgba(255, 255, 255, 0.78);
  --topbar-border: rgba(0, 0, 0, 0.06);
  --pill-bg: rgba(255, 255, 255, 0.94);
  --pill-border: rgba(0, 0, 0, 0.08);
  --pill-text: #1D1D1F;
  --drawer-bg: rgba(255, 255, 255, 0.96);
  --mesh-opacity: 1;
  --groove-bg: rgba(0, 0, 0, 0.05);
  --groove-border: rgba(0, 0, 0, 0.06);
  --groove-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.08), inset 0 1px 1px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.9);
  --tab-active-bg: #FFFFFF;
  --tab-active-text: #1D1D1F;
  --tab-active-border: rgba(0, 0, 0, 0.06);
  --tab-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -0.5px 0 rgba(0, 0, 0, 0.03);
  --input-bg: rgba(255, 255, 255, 0.94);
  --input-border: rgba(0, 0, 0, 0.09);
  --input-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.03), inset 0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 0.9);
}

/* Dark tokens (activated by .dark on <html>) */
.dark {
  --bg-page: #07090E;
  --text-primary: #F9FAFB;
  --text-secondary: #9CA3AF;
  --card-bg: rgba(15, 20, 32, 0.78);
  --card-border: rgba(255, 255, 255, 0.08);
  --hero-bg: linear-gradient(135deg, rgba(20, 27, 45, 0.88) 0%, rgba(13, 19, 33, 0.88) 100%);
  --hero-border: rgba(255, 255, 255, 0.12);
  --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  --card-shadow-hover: 0 8px 30px rgba(0, 113, 227, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  --topbar-bg: rgba(7, 9, 14, 0.82);
  --topbar-border: rgba(255, 255, 255, 0.08);
  --pill-bg: rgba(20, 27, 45, 0.92);
  --pill-border: rgba(255, 255, 255, 0.12);
  --pill-text: #F3F4F6;
  --drawer-bg: rgba(10, 14, 23, 0.96);
  --mesh-opacity: 0.85;
  --groove-bg: rgba(255, 255, 255, 0.06);
  --groove-border: rgba(255, 255, 255, 0.09);
  --groove-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.20), inset 0 1px 1px rgba(0, 0, 0, 0.12), 0 1px 0 rgba(255, 255, 255, 0.06);
  --tab-active-bg: rgba(255, 255, 255, 0.12);
  --tab-active-text: #F9FAFB;
  --tab-active-border: rgba(255, 255, 255, 0.15);
  --tab-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.08);
  --input-bg: rgba(15, 20, 32, 0.80);
  --input-border: rgba(255, 255, 255, 0.10);
  --input-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 0 rgba(255, 255, 255, 0.04);
}
```

### B. Dual-Mode Surface Class Rewiring

Jika memilih dual-mode, hardcoded values di `.crystal-card`, `.hero-crystal`, `.neo-groove`, `.neo-tab-active`, `.apple-input`, dan `.btn-apple-pill` WAJIB diganti dengan `var(--token)` references. Berikut 6 class yang sudah di-rewire:

```css
/* Dual-Mode Crystal Card */
.crystal-card {
  background: var(--card-bg);
  backdrop-filter: blur(32px) saturate(190%);
  -webkit-backdrop-filter: blur(32px) saturate(190%);
  border: 1px solid var(--card-border);
  border-radius: 20px;
  box-shadow: var(--card-shadow);
  transition-property: transform, box-shadow, border-color, background-color;
  transition-duration: 180ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.crystal-card:not(aside):hover {
  box-shadow: var(--card-shadow-hover);
}

/* Dual-Mode Hero Crystal */
.hero-crystal {
  background: var(--hero-bg);
  backdrop-filter: blur(40px) saturate(200%);
  -webkit-backdrop-filter: blur(40px) saturate(200%);
  border: 1.5px solid var(--hero-border);
  border-radius: 24px;
  box-shadow: var(--card-shadow);
  transition: background 200ms ease, border-color 200ms ease;
}

/* Dual-Mode Neomorphic Groove */
.neo-groove {
  background: var(--groove-bg);
  border: 1px solid var(--groove-border);
  box-shadow: var(--groove-shadow);
  border-radius: 12px;
}

/* Dual-Mode Active Tab Pill */
.neo-tab-active {
  background: var(--tab-active-bg) !important;
  color: var(--tab-active-text) !important;
  border: 1px solid var(--tab-active-border) !important;
  box-shadow: var(--tab-active-shadow) !important;
}

/* Dual-Mode Form Input */
.apple-input {
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  box-shadow: var(--input-shadow);
  transition-property: border-color, box-shadow, background-color;
  transition-duration: 140ms;
  transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}
.apple-input:focus {
  border-color: var(--apple-blue);
  box-shadow: 0 0 0 3.5px rgba(0, 113, 227, 0.16), inset 0 1px 2px rgba(0, 0, 0, 0.02);
}

/* Dual-Mode Pill Button */
.btn-apple-pill {
  background: var(--pill-bg);
  color: var(--pill-text);
  border: 1px solid var(--pill-border);
  /* ...rest unchanged... */
}
```

### C. Dual-Mode Canvas Adaptation

Untuk dark mode, canvas mesh tetap menggunakan gradient 5 titik yang sama, tetapi di-dim di atas latar hitam pekat. Body wajib menggunakan CSS variables dan transisi untuk pergantian tema yang mulus:

```css
/* Dark canvas uses same mesh but dimmed on deep black */
.apple-ambient-canvas {
  background-color: var(--bg-page);
  /* background-image stays the same 5-point mesh */
  opacity: var(--mesh-opacity, 1);
}

/* Body must use variables for seamless theme transition */
body {
  background-color: var(--bg-page);
  color: var(--text-primary);
  transition-property: background-color, color;
  transition-duration: 200ms;
}
```

### D. Theme Toggle Pattern (Alpine.js)

Gunakan Alpine.js untuk toggle tema tanpa framework tambahan:

```html
<html :class="{ 'dark': theme === 'dark' }">
```

```javascript
// In x-data or initApp()
theme: localStorage.getItem('theme') || 'light',
toggleTheme() {
  this.theme = this.theme === 'light' ? 'dark' : 'light';
  localStorage.setItem('theme', this.theme);
}
```

Tailwind config wajib menyertakan `darkMode: 'class'` agar utility classes `dark:` berfungsi jika diperlukan:

```javascript
tailwind.config = {
  darkMode: 'class',
  theme: { ... }
}
```

### E. Dual-Mode Anti-Pattern Rules

1. **DILARANG mencampur hardcoded dan var()**: Jika memilih dual-mode, SEMUA surface classes WAJIB pakai CSS variables. Mencampur menyebabkan kartu putih mencolok di atas latar gelap.
2. **DILARANG menggunakan `text-slate-900` hardcoded di dual-mode template**: Gunakan `style="color: var(--text-primary)"` atau Tailwind arbitrary `text-[var(--text-primary)]`.
3. **DILARANG lupa transisi pada body**: Tanpa `transition-property: background-color, color` pada body, pergantian tema terasa kasar.
4. **Proyek light-only (AGY Router) tetap valid**: Hardcoded values di Section 1-9 adalah referensi resmi untuk proyek tanpa dark mode. Tidak perlu diubah ke variables.
---

## 11. Concentric Nested Radii & Optical Geometry Formula

To avoid awkward optical clashes, corner radii MUST be mathematically aligned based on nesting depth using Apple's concentric radius formula:

$$R_{outer} = R_{inner} + Padding$$

If an outer track container has `padding: 6px` (`p-1.5`) and an inner button has `border-radius: 16px` (`rounded-[16px]`), the outer container MUST have:
$$16\text{px} + 6\text{px} = 22\text{px} \rightarrow \text{rounded-[22px]}$$

### Concentric Pairing Cheatsheet:
- **Track `p-1.5` (6px gap)**: Outer `rounded-[22px]` wraps Inner `rounded-[16px]`.
- **Track `p-1` (4px gap)**: Outer `rounded-[20px]` wraps Inner `rounded-[16px]`, or Outer `rounded-[16px]` wraps Inner `rounded-[12px]`.
- **Card Wrapper**: Outer `rounded-3xl` (24px) wraps child Bento boxes `rounded-2xl` (16px to 20px).
- **Pills & Badges**: Fully circular `rounded-full` (9999px) for capsule chips and beacons.

### Typography Stack & Optical Density Scale

For maximum readability and native macOS/iOS compactness, load Google Fonts `Plus Jakarta Sans` + `JetBrains Mono` and configure Tailwind's font-size scale:

```html
<!-- Font Imports in <head> -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">

<!-- Tailwind Density Scale in <script> -->
<script>
  tailwind.config = {
    theme: {
      fontSize: {
        'xs':   ['12px', '16px'],
        'sm':   ['13px', '18px'],
        'base': ['14px', '20px'],
        'lg':   ['16px', '22px'],
        'xl':   ['18px', '24px'],
        '2xl':  ['20px', '26px'],
        '3xl':  ['24px', '30px'],
      },
      extend: {
        fontFamily: {
          sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'sans-serif'],
          mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
        }
      }
    }
  }
</script>
```

CSS typography smoothing & balance rules:
```css
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', system-ui, sans-serif;
  font-size: 14px;
  min-height: 100dvh;
  overflow-x: clip;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
h1, h2, h3, h4 {
  text-wrap: balance;
  letter-spacing: -0.015em;
}
p, .desc-text {
  text-wrap: pretty;
}
.font-mono-apple {
  font-family: 'JetBrains Mono', -apple-system-monospaced, monospace;
  font-variant-numeric: tabular-nums;
}

/* Mobile Viewport Defensive Styles */
@media (max-width: 768px) {
  input:not([readonly]), select, textarea {
    font-size: 16px !important; /* Prevents iOS Safari auto-zoom on focus */
  }
}

/* Global Cupertino Input Focus Ring (Applied to all form elements) */
input:not([type="checkbox"]):not([type="radio"]), select, textarea {
  transition: border-color 150ms ease, box-shadow 150ms ease, background-color 150ms ease;
}
input:not([type="checkbox"]):not([type="radio"]):focus, select:focus, textarea:focus {
  outline: none;
  border-color: #0071E3 !important;
  box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.16) !important;
}
```

---

## 12. Radial Circular Dial Gauge & Rolling Number Engine

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

## 13. Multi-Segmented Waterfall Timeline & Metric Bento Cards

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

### B. The 3-Tier Bento Metric Card (The Cupertino Card Triad)

Extracted directly from CekWeb (Core Web Vitals) and AGY Router (Cluster Telemetry). A high-clarity 3-tier card:
1. **Tier 1 (Header)**: Micro uppercase label (`text-[10px] sm:text-[11px] font-bold uppercase tracking-wider text-slate-500`) + semantic status beacon dot.
2. **Tier 2 (Hero Value)**: Tabular bold number (`text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple`).
3. **Tier 3 (Context Footnote)**: Subtle benchmark hint (`text-[11px] text-slate-400 font-medium`).

```html
<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
  <!-- Card 1: Excellent State -->
  <div class="crystal-card rounded-2xl sm:rounded-3xl p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
    <div class="flex items-center justify-between">
      <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">First Contentful Paint</span>
      <span class="w-2 h-2 rounded-full bg-emerald-500 shadow-xs shadow-emerald-500/40"></span>
    </div>
    <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">0.8 s</div>
    <div class="text-[11px] text-slate-400 font-medium">Batas optimal Google: &lt; 1.8 s</div>
  </div>

  <!-- Card 2: Warning State -->
  <div class="crystal-card rounded-2xl sm:rounded-3xl p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
    <div class="flex items-center justify-between">
      <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Total Blocking Time</span>
      <span class="w-2 h-2 rounded-full bg-amber-500 shadow-xs shadow-amber-500/40"></span>
    </div>
    <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">180 ms</div>
    <div class="text-[11px] text-slate-400 font-medium">Batas optimal Google: &lt; 200 ms</div>
  </div>

  <!-- Card 3: Neutral Benchmark -->
  <div class="crystal-card rounded-2xl sm:rounded-3xl p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
    <div class="flex items-center justify-between">
      <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Kapasitas Token Pool</span>
      <span class="w-2 h-2 rounded-full bg-blue-500 shadow-xs shadow-blue-500/40"></span>
    </div>
    <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">98.4%</div>
    <div class="text-[11px] text-slate-400 font-medium">6 dari 6 akun aktif sehat</div>
  </div>

  <!-- Card 4: Micro Latency -->
  <div class="crystal-card rounded-2xl sm:rounded-3xl p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
    <div class="flex items-center justify-between">
      <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">RTT Latensi Ruko</span>
      <span class="w-2 h-2 rounded-full bg-emerald-500 shadow-xs shadow-emerald-500/40"></span>
    </div>
    <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">12 ms</div>
    <div class="text-[11px] text-slate-400 font-medium">Jaringan LAN Tailscale mesh</div>
  </div>
</div>
```

---

## 14. Radar Pulse Scanning HUD & Status Step Ticker

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

## 15. Scoped Transitions Anti-Jank & Zero-Shift State Swaps

> [!CAUTION]
> **DILARANG MENGGUNAKAN `transition-all` BLANKET DI MANAPUN DALAM TEMPLATE!**
> Blanket `transition-all` memaksa engine layout browser menghitung ulang geometri halaman saat pengguna menggerakkan kursor, memicu lag dan stutter pada CPU i3/STB/ponsel entry-level.

### A. Scoped Transition Property Matrix

Selalu definisikan properti yang ditransisikan secara eksplisit:

| Komponen | Styling Transisi Scoped Baku | Timing & Durasi |
|---|---|---|
| **Buttons & Chips** | `transition-[color,background-color,border-color,box-shadow,transform]` | `duration-140 ease-out` |
| **Bento & Crystal Cards** | `transition-[border-color,box-shadow,transform]` | `duration-180 ease-out` |
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

## 16. Headless OpenGraph Graphic Card Generator (Python Pillow 1200x630)

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

## 17. Zero-Bloat Standalone Stack & Pre-Flight Verification

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
7. **Verifikasi iOS Input Zoom**:
   Pastikan rule `@media (max-width: 768px) { input:not([readonly]) ... font-size: 16px }` ada di `<style>` untuk mencegah auto-zoom Safari iOS saat fokus input.

---

## 18. Master Turnkey Production Template (Ready-to-Deploy Shell)

### A. Light-Only Master Template (Hardcoded Values)

For instant zero-guesswork bootstrapping, use this complete single-file HTML shell that weaves together all 17 chapters (Canvas Mesh + Frosted Cards + Neomorphic Wells + Bento Grid + Dynamic Island):

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Cupertino Liquid Crystal - Master Console</title>
  
  <!-- Font Imports -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  
  <!-- Standalone Tailwind CDN & Density Scale -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        fontSize: {
          'xs':   ['12px', '16px'],
          'sm':   ['13px', '18px'],
          'base': ['14px', '20px'],
          'lg':   ['16px', '22px'],
          'xl':   ['18px', '24px'],
          '2xl':  ['20px', '26px'],
          '3xl':  ['24px', '30px'],
        },
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
          }
        }
      }
    }
  </script>
  
  <!-- Alpine.js CDN -->
  <script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>
  
  <style>
    [x-cloak] { display: none !important; }

    :root {
      --apple-blue: #0071E3;
      --apple-blue-hover: #0077ED;
      --text-primary: #1D1D1F;
      --text-secondary: #86868B;
    }

    body {
      background-color: #F5F5F7;
      color: var(--text-primary);
      font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', system-ui, sans-serif;
      font-size: 14px;
      min-height: 100vh;
      min-height: 100dvh;
      overflow-x: clip;
      -webkit-tap-highlight-color: transparent;
      width: 100%;
      max-width: 100%;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    h1, h2, h3, h4 { text-wrap: balance; letter-spacing: -0.015em; }
    p, .desc-text { text-wrap: pretty; }
    .font-mono-apple { font-family: 'JetBrains Mono', -apple-system-monospaced, monospace; font-variant-numeric: tabular-nums; }

    /* Canvas Iridescent Mesh */
    .apple-ambient-canvas {
      background-color: #F5F5F7;
      background-image: 
        radial-gradient(at 0% 0%, rgba(94, 92, 230, 0.14) 0px, transparent 45%),
        radial-gradient(at 100% 0%, rgba(0, 113, 227, 0.15) 0px, transparent 45%),
        radial-gradient(at 50% 30%, rgba(255, 159, 10, 0.10) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(48, 209, 88, 0.12) 0px, transparent 50%),
        radial-gradient(at 0% 100%, rgba(255, 55, 95, 0.11) 0px, transparent 45%);
      background-attachment: fixed;
    }

    /* Glass Surfaces */
    .crystal-card {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(32px) saturate(190%);
      -webkit-backdrop-filter: blur(32px) saturate(190%);
      border: 1px solid rgba(255, 255, 255, 0.98);
      border-radius: 20px;
      box-shadow: 0 1px 1px rgba(0, 0, 0, 0.02), 0 4px 12px -2px rgba(0, 0, 0, 0.04), 0 8px 24px -4px rgba(0, 113, 227, 0.05), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
      transition-property: transform, box-shadow, border-color;
      transition-duration: 180ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .crystal-card:not(aside):hover {
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 0, 0, 0.05), 0 16px 40px -8px rgba(0, 113, 227, 0.08), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
    }
    .hero-crystal {
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.97) 0%, rgba(244, 248, 255, 0.94) 50%, rgba(254, 244, 249, 0.95) 100%);
      backdrop-filter: blur(40px) saturate(200%);
      -webkit-backdrop-filter: blur(40px) saturate(200%);
      border: 1.5px solid rgba(255, 255, 255, 1);
      border-radius: 24px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 113, 227, 0.06), 0 16px 48px -8px rgba(0, 113, 227, 0.08), inset 0 1px 1px rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.015);
    }

    /* Neomorphic Insets & Sockets */
    .neo-groove {
      background: rgba(0, 0, 0, 0.05);
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.08), inset 0 1px 1px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(0, 0, 0, 0.06);
      border-radius: 12px;
    }
    .neo-tab-active {
      background: #FFFFFF !important;
      color: #1D1D1F !important;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -0.5px 0 rgba(0, 0, 0, 0.03) !important;
      border: 1px solid rgba(0, 0, 0, 0.06) !important;
    }
    .neo-crystal-box {
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 0.9), inset 0 -1px 0 rgba(0, 0, 0, 0.03);
    }
    .apple-input {
      background: rgba(255, 255, 255, 0.94);
      border: 1px solid rgba(0, 0, 0, 0.09);
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.03), inset 0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 0.9);
      transition-property: border-color, box-shadow, background-color;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .apple-input:focus {
      background: #FFFFFF;
      border-color: #0071E3;
      box-shadow: 0 0 0 3.5px rgba(0, 113, 227, 0.16), inset 0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 1);
    }

    /* Tactile Buttons */
    .btn-apple-brand {
      background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.35);
      box-shadow: 0 4px 14px rgba(0, 113, 227, 0.30), 0 1px 2px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.45), inset 0 -1px 0 rgba(0, 0, 0, 0.15);
      transition-property: transform, box-shadow, filter;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
      touch-action: manipulation;
      cursor: pointer;
      user-select: none;
    }
    .btn-apple-brand:hover {
      filter: brightness(1.03);
      box-shadow: 0 6px 20px rgba(0, 113, 227, 0.38), inset 0 1px 0 rgba(255, 255, 255, 0.5);
      transform: translateY(-1px);
    }
    .btn-apple-brand:active {
      transform: scale(0.975) translateY(0.5px);
      box-shadow: 0 1px 4px rgba(0, 113, 227, 0.20), inset 0 2px 4px rgba(0, 0, 0, 0.20);
    }
    .btn-tactile {
      touch-action: manipulation;
      cursor: pointer;
      user-select: none;
      transition-property: transform, opacity, background-color, border-color, box-shadow;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-tactile:hover { transform: translateY(-0.5px); }
    .btn-tactile:active { transform: scale(0.96); }

    /* Native Apple Fluid Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.03); border-radius: 9999px; }
    ::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.25); border-radius: 9999px; border: 1px solid rgba(255, 255, 255, 0.6); background-clip: padding-box; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.8); background-clip: padding-box; }
    * { scrollbar-width: thin; scrollbar-color: rgba(0, 0, 0, 0.25) transparent; }

    /* Global Cupertino Input Focus Ring */
    input:not([type="checkbox"]):not([type="radio"]), select, textarea {
      transition: border-color 150ms ease, box-shadow 150ms ease, background-color 150ms ease;
    }
    input:not([type="checkbox"]):not([type="radio"]):focus, select:focus, textarea:focus {
      outline: none;
      border-color: #0071E3 !important;
      box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.16) !important;
    }

    /* Mobile Zoom Prevention */
    @media (max-width: 768px) {
      input:not([readonly]), select, textarea { font-size: 16px !important; }
    }
  </style>
</head>
<body class="min-h-screen apple-ambient-canvas p-4 sm:p-8 space-y-6 relative"
      x-data="{ activeTab: 'audit', toast: { visible: false, message: '' } }">

  <!-- Dynamic Island Notification -->
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

  <!-- Main Container Wrapper (Zero Background to preserve Canvas Mesh) -->
  <div class="max-w-6xl mx-auto space-y-6">

    <!-- Top Header Bar -->
    <header class="crystal-card p-4 sm:p-5 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
        <h1 class="text-base sm:text-lg font-black tracking-tight text-slate-900">MEGAPASS CLUSTER</h1>
        <span class="font-mono-apple text-[9.5px] font-bold tracking-wider uppercase px-2 py-0.5 rounded-full bg-[#0071E3]/[0.08] text-[#0071E3] border border-[#0071E3]/20">
          V2.0 LIQUID
        </span>
      </div>
      <div class="neo-groove p-1 rounded-2xl inline-flex items-center gap-1">
        <button type="button" @click="activeTab = 'audit'"
                :class="activeTab === 'audit' ? 'neo-tab-active shadow-xs' : 'text-slate-500 hover:text-slate-900 border border-transparent'"
                class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition-[color,background-color,border-color,box-shadow,transform] duration-140 btn-tactile min-h-[36px]">
          Audit
        </button>
        <button type="button" @click="activeTab = 'telemetry'"
                :class="activeTab === 'telemetry' ? 'neo-tab-active shadow-xs' : 'text-slate-500 hover:text-slate-900 border border-transparent'"
                class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition-[color,background-color,border-color,box-shadow,transform] duration-140 btn-tactile min-h-[36px]">
          Telemetri
        </button>
      </div>
    </header>

    <!-- 4-Column Bento Metric Cards -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Kapasitas Slot</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">100%</div>
        <div class="text-[11px] text-slate-400 font-medium">Rotasi akun otomatis aktif</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Throughput AI</span>
          <span class="w-2 h-2 rounded-full bg-blue-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">182 t/s</div>
        <div class="text-[11px] text-slate-400 font-medium">Zero-buffer streaming pass</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Latensi RTT</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black text-slate-900 tabular-nums font-mono-apple">14 ms</div>
        <div class="text-[11px] text-slate-400 font-medium">Subnet Tailscale ruko</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Status Gateway</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black text-emerald-600 font-mono-apple">ONLINE</div>
        <div class="text-[11px] text-slate-400 font-medium">Uptime 99.98% 30 hari</div>
      </div>
    </div>

    <!-- Centerpiece Hero Console Island -->
    <main class="hero-crystal p-6 sm:p-8 space-y-6">
      <div class="space-y-1">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Konsol Servis Mandiri</h2>
        <p class="text-xs sm:text-sm text-slate-500">Ketik hostname atau parameter untuk memicu radar diagnosa.</p>
      </div>

      <div class="flex flex-col sm:flex-row items-center gap-3">
        <input type="text"
               placeholder="Contoh: cekweb.megapass.web.id"
               class="apple-input w-full rounded-2xl px-4 py-3 text-xs font-mono-apple text-slate-900 placeholder:text-slate-400 outline-none min-h-[44px]">
        <button type="button"
                @click="toast.message = 'Memulai proses diagnosa...'; toast.visible = true; setTimeout(() => toast.visible = false, 2500)"
                class="btn-apple-brand w-full sm:w-auto px-6 py-3 rounded-2xl text-xs font-bold flex items-center justify-center gap-2 whitespace-nowrap min-h-[44px]">
          <span>Mulai Analisis</span>
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
          </svg>
        </button>
      </div>
    </main>

  </div>
</body>
</html>
```

### B. Dual-Mode Master Template (Light + Dark Toggle)

For projects requiring both light and dark modes, use this variant that replaces hardcoded values with CSS custom properties and includes an Alpine.js theme toggle. Extracted from the production architecture of **Skill Hub Megapass** (`https://skill.megapass.web.id/`).

```html
<!DOCTYPE html>
<html lang="id" x-data="{ theme: 'light' }" x-init="theme = localStorage.getItem('theme') || 'light'" :class="{ 'dark': theme === 'dark' }">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Cupertino Liquid Crystal - Dual Mode Console</title>

  <!-- Font Imports -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">

  <!-- Standalone Tailwind CDN & Density Scale -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        fontSize: {
          'xs':   ['12px', '16px'],
          'sm':   ['13px', '18px'],
          'base': ['14px', '20px'],
          'lg':   ['16px', '22px'],
          'xl':   ['18px', '24px'],
          '2xl':  ['20px', '26px'],
          '3xl':  ['24px', '30px'],
        },
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
          }
        }
      }
    }
  </script>

  <!-- Alpine.js CDN -->
  <script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>

  <style>
    [x-cloak] { display: none !important; }

    /* ── Light Mode Tokens (Default) ── */
    :root {
      --apple-blue: #0071E3;
      --apple-blue-hover: #0077ED;
      --bg-page: #F5F5F7;
      --text-primary: #1D1D1F;
      --text-secondary: #86868B;
      --card-bg: rgba(255, 255, 255, 0.92);
      --card-border: rgba(255, 255, 255, 0.98);
      --hero-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.97) 0%, rgba(244, 248, 255, 0.94) 50%, rgba(254, 244, 249, 0.95) 100%);
      --hero-border: rgba(255, 255, 255, 1);
      --card-shadow: 0 1px 1px rgba(0, 0, 0, 0.02), 0 4px 12px -2px rgba(0, 0, 0, 0.04), 0 8px 24px -4px rgba(0, 113, 227, 0.05), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
      --card-shadow-hover: 0 2px 4px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 0, 0, 0.05), 0 16px 40px -8px rgba(0, 113, 227, 0.08), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -1px 0 rgba(0, 0, 0, 0.02);
      --topbar-bg: rgba(255, 255, 255, 0.78);
      --topbar-border: rgba(0, 0, 0, 0.06);
      --pill-bg: rgba(255, 255, 255, 0.94);
      --pill-border: rgba(0, 0, 0, 0.08);
      --pill-text: #1D1D1F;
      --drawer-bg: rgba(255, 255, 255, 0.96);
      --mesh-opacity: 1;
      --groove-bg: rgba(0, 0, 0, 0.05);
      --groove-border: rgba(0, 0, 0, 0.06);
      --groove-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.08), inset 0 1px 1px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.9);
      --tab-active-bg: #FFFFFF;
      --tab-active-text: #1D1D1F;
      --tab-active-border: rgba(0, 0, 0, 0.06);
      --tab-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 1), inset 0 -0.5px 0 rgba(0, 0, 0, 0.03);
      --input-bg: rgba(255, 255, 255, 0.94);
      --input-border: rgba(0, 0, 0, 0.09);
      --input-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.03), inset 0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 0.9);
    }

    /* ── Dark Mode Tokens ── */
    .dark {
      --bg-page: #07090E;
      --text-primary: #F9FAFB;
      --text-secondary: #9CA3AF;
      --card-bg: rgba(15, 20, 32, 0.78);
      --card-border: rgba(255, 255, 255, 0.08);
      --hero-bg: linear-gradient(135deg, rgba(20, 27, 45, 0.88) 0%, rgba(13, 19, 33, 0.88) 100%);
      --hero-border: rgba(255, 255, 255, 0.12);
      --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.05);
      --card-shadow-hover: 0 8px 30px rgba(0, 113, 227, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      --topbar-bg: rgba(7, 9, 14, 0.82);
      --topbar-border: rgba(255, 255, 255, 0.08);
      --pill-bg: rgba(20, 27, 45, 0.92);
      --pill-border: rgba(255, 255, 255, 0.12);
      --pill-text: #F3F4F6;
      --drawer-bg: rgba(10, 14, 23, 0.96);
      --mesh-opacity: 0.85;
      --groove-bg: rgba(255, 255, 255, 0.06);
      --groove-border: rgba(255, 255, 255, 0.09);
      --groove-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.20), inset 0 1px 1px rgba(0, 0, 0, 0.12), 0 1px 0 rgba(255, 255, 255, 0.06);
      --tab-active-bg: rgba(255, 255, 255, 0.12);
      --tab-active-text: #F9FAFB;
      --tab-active-border: rgba(255, 255, 255, 0.15);
      --tab-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      --input-bg: rgba(15, 20, 32, 0.80);
      --input-border: rgba(255, 255, 255, 0.10);
      --input-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 0 rgba(255, 255, 255, 0.04);
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-primary);
      font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', system-ui, sans-serif;
      font-size: 14px;
      min-height: 100vh;
      min-height: 100dvh;
      overflow-x: clip;
      -webkit-tap-highlight-color: transparent;
      width: 100%;
      max-width: 100%;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      transition-property: background-color, color;
      transition-duration: 200ms;
    }

    h1, h2, h3, h4 { text-wrap: balance; letter-spacing: -0.015em; }
    p, .desc-text { text-wrap: pretty; }
    .font-mono-apple { font-family: 'JetBrains Mono', -apple-system-monospaced, monospace; font-variant-numeric: tabular-nums; }

    /* Canvas Iridescent Mesh */
    .apple-ambient-canvas {
      background-color: var(--bg-page);
      background-image:
        radial-gradient(at 0% 0%, rgba(94, 92, 230, 0.14) 0px, transparent 45%),
        radial-gradient(at 100% 0%, rgba(0, 113, 227, 0.15) 0px, transparent 45%),
        radial-gradient(at 50% 30%, rgba(255, 159, 10, 0.10) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(48, 209, 88, 0.12) 0px, transparent 50%),
        radial-gradient(at 0% 100%, rgba(255, 55, 95, 0.11) 0px, transparent 45%);
      background-attachment: fixed;
      opacity: var(--mesh-opacity);
    }

    /* Glass Surfaces */
    .crystal-card {
      background: var(--card-bg);
      backdrop-filter: blur(32px) saturate(190%);
      -webkit-backdrop-filter: blur(32px) saturate(190%);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      box-shadow: var(--card-shadow);
      transition-property: transform, box-shadow, border-color, background-color;
      transition-duration: 180ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .crystal-card:not(aside):hover {
      box-shadow: var(--card-shadow-hover);
    }
    .hero-crystal {
      background: var(--hero-bg);
      backdrop-filter: blur(40px) saturate(200%);
      -webkit-backdrop-filter: blur(40px) saturate(200%);
      border: 1.5px solid var(--hero-border);
      border-radius: 24px;
      box-shadow: var(--card-shadow);
    }

    /* Neomorphic Insets & Sockets */
    .neo-groove {
      background: var(--groove-bg);
      box-shadow: var(--groove-shadow);
      border: 1px solid var(--groove-border);
      border-radius: 12px;
    }
    .neo-tab-active {
      background: var(--tab-active-bg) !important;
      color: var(--tab-active-text) !important;
      box-shadow: var(--tab-active-shadow) !important;
      border: 1px solid var(--tab-active-border) !important;
    }
    .apple-input {
      background: var(--input-bg);
      border: 1px solid var(--input-border);
      box-shadow: var(--input-shadow);
      transition-property: border-color, box-shadow, background-color;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .apple-input:focus {
      background: #FFFFFF;
      border-color: #0071E3;
      box-shadow: 0 0 0 3.5px rgba(0, 113, 227, 0.16), inset 0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 1);
    }
    .dark .apple-input:focus {
      background: rgba(20, 27, 45, 0.95);
      box-shadow: 0 0 0 3.5px rgba(0, 113, 227, 0.24), inset 0 1px 2px rgba(0, 0, 0, 0.10);
    }

    /* Pill Button */
    .btn-apple-pill {
      background: var(--pill-bg);
      color: var(--pill-text);
      font-weight: 600;
      border: 1px solid var(--pill-border);
      border-radius: 9999px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      transition-property: transform, background-color, border-color, box-shadow;
      transition-duration: 150ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
      touch-action: manipulation;
      cursor: pointer;
      user-select: none;
      min-height: 32px;
    }
    .btn-apple-pill:hover {
      transform: translateY(-0.5px);
    }
    .btn-apple-pill:active {
      transform: scale(0.97) translateY(0.5px);
    }

    /* Tactile Buttons */
    .btn-apple-brand {
      background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.35);
      box-shadow: 0 4px 14px rgba(0, 113, 227, 0.30), 0 1px 2px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.45), inset 0 -1px 0 rgba(0, 0, 0, 0.15);
      transition-property: transform, box-shadow, filter;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
      touch-action: manipulation;
      cursor: pointer;
      user-select: none;
    }
    .btn-apple-brand:hover {
      filter: brightness(1.03);
      box-shadow: 0 6px 20px rgba(0, 113, 227, 0.38), inset 0 1px 0 rgba(255, 255, 255, 0.5);
      transform: translateY(-1px);
    }
    .btn-apple-brand:active {
      transform: scale(0.975) translateY(0.5px);
      box-shadow: 0 1px 4px rgba(0, 113, 227, 0.20), inset 0 2px 4px rgba(0, 0, 0, 0.20);
    }
    .btn-tactile {
      touch-action: manipulation;
      cursor: pointer;
      user-select: none;
      transition-property: transform, opacity, background-color, border-color, box-shadow;
      transition-duration: 140ms;
      transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-tactile:hover { transform: translateY(-0.5px); }
    .btn-tactile:active { transform: scale(0.96); }

    /* Native Apple Fluid Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.03); border-radius: 9999px; }
    ::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.25); border-radius: 9999px; border: 1px solid rgba(255, 255, 255, 0.6); background-clip: padding-box; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.8); background-clip: padding-box; }
    * { scrollbar-width: thin; scrollbar-color: rgba(0, 0, 0, 0.25) transparent; }
    .dark ::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.04); }
    .dark ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.25); border-color: rgba(0, 0, 0, 0.3); }
    .dark ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.40); }
    .dark * { scrollbar-color: rgba(255, 255, 255, 0.25) transparent; }

    /* Global Cupertino Input Focus Ring */
    input:not([type="checkbox"]):not([type="radio"]), select, textarea {
      transition: border-color 150ms ease, box-shadow 150ms ease, background-color 150ms ease;
    }
    input:not([type="checkbox"]):not([type="radio"]):focus, select:focus, textarea:focus {
      outline: none;
      border-color: #0071E3 !important;
      box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.16) !important;
    }

    /* Mobile Zoom Prevention */
    @media (max-width: 768px) {
      input:not([readonly]), select, textarea { font-size: 16px !important; }
    }
  </style>
</head>
<body class="min-h-screen apple-ambient-canvas p-4 sm:p-8 space-y-6 relative"
      x-data="{
        activeTab: 'audit',
        toast: { visible: false, message: '' },
        theme: 'light',
        toggleTheme() {
          this.theme = this.theme === 'light' ? 'dark' : 'light';
          localStorage.setItem('theme', this.theme);
        }
      }"
      x-init="theme = localStorage.getItem('theme') || 'light'">

  <!-- Dynamic Island Notification -->
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

  <!-- Main Container Wrapper (Zero Background to preserve Canvas Mesh) -->
  <div class="max-w-6xl mx-auto space-y-6">

    <!-- Top Header Bar -->
    <header class="crystal-card p-4 sm:p-5 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
        <h1 class="text-base sm:text-lg font-black tracking-tight" style="color: var(--text-primary)">MEGAPASS CLUSTER</h1>
        <span class="font-mono-apple text-[9.5px] font-bold tracking-wider uppercase px-2 py-0.5 rounded-full bg-[#0071E3]/[0.08] text-[#0071E3] border border-[#0071E3]/20">
          V2.1 DUAL
        </span>
      </div>
      <div class="flex items-center gap-2">
        <div class="neo-groove p-1 rounded-2xl inline-flex items-center gap-1">
          <button type="button" @click="activeTab = 'audit'"
                  :class="activeTab === 'audit' ? 'neo-tab-active shadow-xs' : 'border border-transparent'"
                  :style="activeTab !== 'audit' ? 'color: var(--text-secondary)' : ''"
                  class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition-[color,background-color,border-color,box-shadow,transform] duration-140 btn-tactile min-h-[36px]">
            Audit
          </button>
          <button type="button" @click="activeTab = 'telemetry'"
                  :class="activeTab === 'telemetry' ? 'neo-tab-active shadow-xs' : 'border border-transparent'"
                  :style="activeTab !== 'telemetry' ? 'color: var(--text-secondary)' : ''"
                  class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition-[color,background-color,border-color,box-shadow,transform] duration-140 btn-tactile min-h-[36px]">
            Telemetri
          </button>
        </div>
        <!-- Theme Toggle -->
        <button type="button" @click="toggleTheme()" class="btn-apple-pill p-2 rounded-full" :title="theme === 'light' ? 'Mode Gelap' : 'Mode Terang'">
          <template x-if="theme === 'dark'">
            <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
          </template>
          <template x-if="theme === 'light'">
            <svg class="w-4 h-4" style="color: var(--text-secondary)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
          </template>
        </button>
      </div>
    </header>

    <!-- 4-Column Bento Metric Cards -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider" style="color: var(--text-secondary)">Kapasitas Slot</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black tabular-nums font-mono-apple" style="color: var(--text-primary)">100%</div>
        <div class="text-[11px] font-medium" style="color: var(--text-secondary)">Rotasi akun otomatis aktif</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider" style="color: var(--text-secondary)">Throughput AI</span>
          <span class="w-2 h-2 rounded-full bg-blue-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black tabular-nums font-mono-apple" style="color: var(--text-primary)">182 t/s</div>
        <div class="text-[11px] font-medium" style="color: var(--text-secondary)">Zero-buffer streaming pass</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider" style="color: var(--text-secondary)">Latensi RTT</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black tabular-nums font-mono-apple" style="color: var(--text-primary)">14 ms</div>
        <div class="text-[11px] font-medium" style="color: var(--text-secondary)">Subnet Tailscale ruko</div>
      </div>
      <div class="crystal-card p-4 sm:p-5 flex flex-col justify-between h-full space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[11px] font-bold uppercase tracking-wider" style="color: var(--text-secondary)">Status Gateway</span>
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        </div>
        <div class="text-2xl sm:text-3xl font-black text-emerald-600 dark:text-emerald-400 font-mono-apple">ONLINE</div>
        <div class="text-[11px] font-medium" style="color: var(--text-secondary)">Uptime 99.98% 30 hari</div>
      </div>
    </div>

    <!-- Centerpiece Hero Console Island -->
    <main class="hero-crystal p-6 sm:p-8 space-y-6">
      <div class="space-y-1">
        <h2 class="text-xl sm:text-2xl font-black tracking-tight" style="color: var(--text-primary)">Konsol Servis Mandiri</h2>
        <p class="text-xs sm:text-sm" style="color: var(--text-secondary)">Ketik hostname atau parameter untuk memicu radar diagnosa.</p>
      </div>

      <div class="flex flex-col sm:flex-row items-center gap-3">
        <input type="text"
               placeholder="Contoh: cekweb.megapass.web.id"
               class="apple-input w-full rounded-2xl px-4 py-3 text-xs font-mono-apple placeholder:text-slate-400 dark:placeholder:text-slate-600 outline-none min-h-[44px]"
               style="color: var(--text-primary)">
        <button type="button"
                @click="toast.message = 'Memulai proses diagnosa...'; toast.visible = true; setTimeout(() => toast.visible = false, 2500)"
                class="btn-apple-brand w-full sm:w-auto px-6 py-3 rounded-2xl text-xs font-bold flex items-center justify-center gap-2 whitespace-nowrap min-h-[44px]">
          <span>Mulai Analisis</span>
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
          </svg>
        </button>
      </div>
    </main>

  </div>
</body>
</html>
```

---

## 19. Clarity & Visual Aesthetics Audit SOP (Anti-Slop Golden Rules)

To verify that an interface achieves the exact optical clarity and beauty of **AGY Router** and **CekWeb Megapass**, perform this 6-point verification before declaring completion:

1. **Contrast Ratio Integrity (WCAG AAA)**:
   - Primary text MUST be `#0F172A` (Slate 900) or `#1D1D1F` on frosted white cards.
   - Secondary labels MUST be `#64748B` (Slate 500) or `#86868B`.
   - Active tab text MUST be high-contrast dark on `#FFFFFF` pill.
   - NEVER use low-contrast light-gray text (`text-slate-300`, `text-gray-400`) on white or frosted cards.
2. **Tabular Number Alignment**:
   - Every numerical score, latency value, clock, or progress counter MUST have `.font-mono-apple` / `tabular-nums`. Numbers must never wobble or jitter as they change.
3. **Overhead Light Angle Uniformity**:
   - The light source is strictly top-down (12 o'clock).
   - Inset shadows always point down (`inset 0 2px 4px`).
   - Specular highlights always sit on the top lip (`inset 0 1px 0`).
   - Chamfer reflections on bottom edges (`0 1px 0 rgba(255,255,255,0.95)`).
4. **Zero Layout Shifts (CLS = 0)**:
   - Status switches and icons must be housed in fixed-size containers (`relative w-4 h-4`) with cross-fading opacities (`transition-opacity duration-150`), preventing buttons from jumping horizontally.
5. **Native Vector Iconography (Zero Emojis)**:
   - Interfaces must use clean inline SVG icons (Lucide or Heroicons).
   - Emojis in buttons, tabs, or card titles are strictly prohibited.
6. **Optical Density Scale**:
   - Interfaces must employ the compact density scale (`text-xs` is 12px, `text-sm` is 13px, `text-base` is 14px) with `-0.015em` letter spacing on headings and `text-wrap: balance` to prevent awkward orphan words.

---

## 20. Apple Liquid Mobile Bottom Dock & Standalone Sideload Card

Diekstrak langsung dari arsitektur produksi **AGY Router** (v2.13.0) yang telah teruji pada berbagai smartphone modern (Android 8.0+ & iOS Safari).

### A. Floating Frosted Glass Bottom Dock with Dynamic Active Pill

Bilah navigasi jempol bawah melayang (*floating bottom dock*) dengan estetika kaca cair Cupertino:
- **Lapisan Kaca**: `bg-white/85 backdrop-blur-2xl border-t border-black/[0.08] shadow-[0_-4px_24px_rgba(0,0,0,0.06)]`.
- **Animasi Indikator Pil Aktif (*Cupertino active pill*)**: `w-3.5 h-1 rounded-full bg-[#0071E3] transition-[opacity,transform] duration-200 :class="activeTab === 'dashboard' ? 'opacity-100 scale-100' : 'opacity-0 scale-50'"`.
- **Micro-Haptic Tactile Spring**: `active:scale-[0.92] transition-[transform,color,background-color] duration-150 active:bg-black/[0.03] rounded-2xl touch-manipulation`.
- **Drop Shadow Halus pada Ikon Aktif**: `:class="activeTab === 'dashboard' ? 'drop-shadow-[0_1px_3px_rgba(0,113,227,0.25)]' : ''"`.
- **Proteksi Safe Area Hardware**: `style="padding-bottom: max(10px, env(safe-area-inset-bottom));"`.
- **Sekring Hindari Keyboard**: `:class="isInputFocused ? 'translate-y-32 pointer-events-none opacity-0' : 'translate-y-0 pointer-events-auto opacity-100'"`.

```html
<!-- Apple Liquid Crystal Bottom Nav Dock (Mobile Viewport) -->
<nav class="lg:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/85 backdrop-blur-2xl border-t border-black/[0.08] px-2 pt-2 flex items-center justify-around shadow-[0_-4px_24px_rgba(0,0,0,0.06)] transition-[transform,opacity] duration-200 ease-out select-none"
     :class="isInputFocused ? 'translate-y-32 pointer-events-none opacity-0' : 'translate-y-0 pointer-events-auto opacity-100'"
     style="padding-bottom: max(10px, env(safe-area-inset-bottom));">
  
  <!-- Tab 1: Dashboard -->
  <button type="button"
          @click="switchTab('dashboard')" 
          class="flex flex-col items-center justify-center flex-1 min-h-[44px] py-1 cursor-pointer transition-[transform,color,background-color] duration-150 active:scale-[0.92] active:bg-black/[0.03] rounded-2xl touch-manipulation select-none group"
          :class="activeTab === 'dashboard' ? 'text-[#0071E3] font-bold' : 'text-[#86868B] hover:text-[#1D1D1F]'">
    <svg class="w-5 h-5 mb-0.5 transition-transform duration-150 group-hover:scale-105" 
         :class="activeTab === 'dashboard' ? 'drop-shadow-[0_1px_3px_rgba(0,113,227,0.25)]' : ''" 
         viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
      <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
      <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
      <rect x="14" y="14" width="7" height="7" rx="1.5"></rect>
      <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
    </svg>
    <span class="text-[10px] leading-tight tracking-tight">Dashboard</span>
    <span class="w-3.5 h-1 rounded-full bg-[#0071E3] mt-0.5 transition-[opacity,transform] duration-200" 
          :class="activeTab === 'dashboard' ? 'opacity-100 scale-100' : 'opacity-0 scale-50'"></span>
  </button>

  <!-- Tab 2: Endpoint -->
  <button type="button"
          @click="switchTab('endpoint')" 
          class="flex flex-col items-center justify-center flex-1 min-h-[44px] py-1 cursor-pointer transition-[transform,color,background-color] duration-150 active:scale-[0.92] active:bg-black/[0.03] rounded-2xl touch-manipulation select-none group"
          :class="activeTab === 'endpoint' ? 'text-[#0071E3] font-bold' : 'text-[#86868B] hover:text-[#1D1D1F]'">
    <svg class="w-5 h-5 mb-0.5 transition-transform duration-150 group-hover:scale-105" 
         :class="activeTab === 'endpoint' ? 'drop-shadow-[0_1px_3px_rgba(0,113,227,0.25)]' : ''" 
         viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
      <path d="M4 11a9 9 0 0 1 9 9"></path>
      <path d="M4 4a16 16 0 0 1 16 16"></path>
      <circle cx="5" cy="19" r="1"></circle>
    </svg>
    <span class="text-[10px] leading-tight tracking-tight">Endpoint</span>
    <span class="w-3.5 h-1 rounded-full bg-[#0071E3] mt-0.5 transition-[opacity,transform] duration-200" 
          :class="activeTab === 'endpoint' ? 'opacity-100 scale-100' : 'opacity-0 scale-50'"></span>
  </button>
</nav>
```

### B. Sideload APK & WebAPK Component (Concentric Radii & QR Modal)

Pola kartu instalasi mandiri PWA & biner Android (.apk) langsung dari server lokal tanpa perantara Google Play Store.

1. **Formula Radius Konsentris**: Kartu induk `rounded-3xl` dengan padding `p-5 sm:p-6` membungkus sub-kartu `rounded-2xl` (`p-3.5 rounded-2xl bg-white/80 backdrop-blur-md border border-white/80 shadow-[0_2px_8px_rgba(0,0,0,0.02)]`).
2. **Badge Versi Anti-Duplikasi**: `x-text="apkInfo.version ? (apkInfo.version.startsWith('v') ? apkInfo.version : 'v' + apkInfo.version) : 'v1.0.0'"` untuk mencegah bug `vv1.0.0`.
3. **QR Code Modal Drawer**: Modal popup berlatar frosted glass untuk transfer unduhan langsung via scan kamera smartphone operator.

```html
<!-- Sideload APK & Standalone PWA Card -->
<div class="crystal-card p-5 sm:p-6 space-y-4">
  <div class="border-b border-black/[0.06] pb-4 space-y-1">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-[#0071E3] to-[#5E5CE6] flex items-center justify-center text-white shadow-sm flex-shrink-0">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <rect x="5" y="2" width="14" height="20" rx="3"></rect>
            <line x1="12" y1="18" x2="12.01" y2="18" stroke-width="3" stroke-linecap="round"></line>
          </svg>
        </div>
        <div>
          <h3 class="font-bold text-base text-[#1D1D1F] tracking-tight">Aplikasi Android Mandiri (.apk)</h3>
          <p class="text-xs text-[#86868B]">Akses dasbor tanpa address bar browser via biner APK native Android.</p>
        </div>
      </div>
      <div class="flex flex-wrap items-center gap-1.5 font-mono text-[11px] self-start sm:self-auto">
        <span class="px-2.5 py-0.5 rounded-md bg-emerald-50/90 text-[#1B803A] font-bold border border-emerald-200/70 shadow-2xs">Android 8.0+</span>
        <span class="px-2.5 py-0.5 rounded-md bg-purple-50/90 text-[#BF5AF2] font-bold border border-purple-200/70 shadow-2xs" 
              x-text="apkInfo.version ? (apkInfo.version.startsWith('v') ? apkInfo.version : 'v' + apkInfo.version) : 'v1.0.0'">v1.0.0</span>
      </div>
    </div>
  </div>

  <!-- Concentric Feature Cards -->
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3.5 rounded-2xl bg-white/80 backdrop-blur-md border border-white/80 shadow-[0_2px_8px_rgba(0,0,0,0.02)] space-y-1.5">
      <div class="flex items-center justify-between text-[#86868B]">
        <span class="font-medium">Biner APK Offline</span>
        <span class="text-[10px] font-mono text-[#0071E3] font-bold px-1.5 py-0.5 rounded bg-blue-50/80 border border-blue-100">Direct Sideload</span>
      </div>
      <div class="text-sm font-bold font-mono text-[#1D1D1F] tabular-nums" x-text="apkInfo.size || '10.5 MB'">10.5 MB</div>
      <p class="text-[11px] text-[#86868B] leading-normal">Instalasi biner mandiri langsung ke smartphone tanpa Google Play Store.</p>
    </div>

    <div class="p-3.5 rounded-2xl bg-white/80 backdrop-blur-md border border-white/80 shadow-[0_2px_8px_rgba(0,0,0,0.02)] space-y-1.5">
      <div class="flex items-center justify-between text-[#86868B]">
        <span class="font-medium">Akses Jaringan</span>
        <span class="text-[10px] font-mono text-[#5E5CE6] font-bold px-1.5 py-0.5 rounded bg-purple-50/80 border border-purple-100">Mesh + LAN</span>
      </div>
      <div class="text-sm font-bold font-mono text-[#0071E3] uppercase tracking-wider">Tailscale & LAN</div>
      <p class="text-[11px] text-[#86868B] leading-normal">Mendukung koneksi aman via Tailscale Mesh atau jaringan lokal ruko.</p>
    </div>
  </div>

  <!-- Primary Sideload CTA & Modal Triggers -->
  <div class="space-y-2 pt-1">
    <a href="/download/apk" download
       class="btn-apple-blue w-full py-2.5 px-4 rounded-xl text-xs font-bold flex items-center justify-center space-x-2 shadow-sm cursor-pointer active:scale-[0.98] transition-transform">
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
        <polyline points="7 10 12 15 17 10"></polyline>
        <line x1="12" y1="15" x2="12" y2="3"></line>
      </svg>
      <span>Unduh APK Android</span>
    </a>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
      <!-- Tactile Copy Link Button with Checkmark Feedback -->
      <button type="button"
              @click="copyDownloadLink()" 
              class="btn-apple-pill w-full py-2 px-3 text-xs font-semibold flex items-center justify-center space-x-1.5 cursor-pointer active:scale-95 transition-[transform,background-color,border-color,box-shadow]">
        <svg class="w-3.5 h-3.5 text-[#0071E3]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>
        <span>Salin Link APK</span>
      </button>

      <!-- Scan QR Button for Instant Camera Handoff -->
      <button type="button"
              @click="showQrApk = true" 
              class="btn-apple-pill w-full py-2 px-3 text-xs font-semibold flex items-center justify-center space-x-1.5 cursor-pointer active:scale-95 transition-[transform,background-color,border-color,box-shadow]">
        <svg class="w-3.5 h-3.5 text-[#0071E3]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="7" height="7"></rect>
          <rect x="14" y="3" width="7" height="7"></rect>
          <rect x="14" y="14" width="7" height="7"></rect>
          <rect x="3" y="14" width="7" height="7"></rect>
        </svg>
        <span>Scan QR</span>
      </button>
    </div>
  </div>
</div>
```

