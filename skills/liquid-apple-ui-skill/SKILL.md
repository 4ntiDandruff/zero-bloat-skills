---
name: liquid-apple-ui-skill
description: "Apple-inspired Cupertino liquid crystal UI design system: iridescent ambient mesh canvas (#F5F5F7), frosted translucent glass cards (backdrop-blur 32px), Apple tactile spring buttons, dynamic status pills, zero-flicker Alpine.js transitions, and zero-bloat standalone Tailwind implementation without node_modules."
---

# Liquid Apple UI Skill

Design system and frontend engineering patterns for crafting Apple Cupertino-caliber light liquid crystal interfaces without heavyweight framework dependencies (React, Next.js, or runtime `node_modules`).

Directly reverse-engineered and extracted from the production-tested **AGY Router** mission-control console and **Megapass** workbench web applications.

---

## 1. Cupertino Canvas & Liquid Crystal Palette

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

### Surface Hierarchy Table

| Component Level | Visual Specification | Styling Class / CSS | Semantic Purpose |
|---|---|---|---|
| **Ambient Canvas** | `#F5F5F7` + Iridescent Mesh Radial Gradients | `.apple-ambient-canvas` | Deepest foundation layer; dynamic color hints at corners |
| **Frosted Glass Cards** | `rgba(255,255,255,0.88)` + `blur(32px) saturate(190%)` | `.crystal-card` | Data containers, interactive panels, navigation sidebar |
| **Hero Crystal Island** | `linear-gradient(135deg, rgba(255,255,255,0.96), rgba(244,248,255,0.92))` | `.hero-crystal` | Top-level active status banner, widget islands |
| **Primary Tactile Button** | `#0077ED` ➔ `#0066CC` gradient + 1px white top inset | `.btn-apple-blue` | Main call-to-action with Cupertino spring click haptics |
| **Tactile Pill Button** | `rgba(255,255,255,0.94)` + border `rgba(0,0,0,0.08)` | `.btn-apple-pill` | Secondary controls, modal triggers, segmented buttons |
| **Typography** | `-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans'` | Body text `#1D1D1F` | System-native clarity, optical tracking, no generic fonts |
| **Tabular Monospace** | `'JetBrains Mono', -apple-system-monospaced` | `font-mono-apple` | Tabular numbers, IDs, quotas, timestamp badges |

---

## 2. Essential CSS Stylesheet Foundations

Include this base layer alongside standalone Tailwind CSS:

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/alpinejs@3.13.5/dist/cdn.min.js" defer></script>

<style>
  [x-cloak] { display: none !important; }

  body {
    background-color: #F5F5F7;
    color: #1D1D1F;
    font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', 'SF Pro Text', system-ui, sans-serif;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .font-mono-apple {
    font-family: 'JetBrains Mono', -apple-system-monospaced, monospace;
    font-variant-numeric: tabular-nums;
  }

  /* Ambient Dynamic Iridescent Mesh Canvas */
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

  /* Translucent Liquid Crystal Frosted Glass Cards */
  .crystal-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(32px) saturate(190%);
    -webkit-backdrop-filter: blur(32px) saturate(190%);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    box-shadow: 
      0 1px 2px rgba(0, 0, 0, 0.02),
      0 6px 20px -4px rgba(0, 113, 227, 0.05),
      inset 0 1px 0 rgba(255, 255, 255, 1);
    transition: transform 180ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 180ms cubic-bezier(0.16, 1, 0.3, 1);
  }
  .crystal-card:not(aside):hover {
    transform: translateY(-1px);
    box-shadow: 
      0 4px 14px rgba(0, 0, 0, 0.025),
      0 14px 30px -8px rgba(0, 113, 227, 0.09),
      inset 0 1px 0 rgba(255, 255, 255, 1);
  }

  /* Hero Crystal Island (Apple Widget Aesthetic) */
  .hero-crystal {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(244, 248, 255, 0.92) 50%, rgba(254, 244, 249, 0.94) 100%);
    backdrop-filter: blur(40px) saturate(200%);
    -webkit-backdrop-filter: blur(40px) saturate(200%);
    border: 1.5px solid rgba(255, 255, 255, 1);
    border-radius: 24px;
    box-shadow: 
      0 1px 2px rgba(0, 0, 0, 0.02),
      0 14px 36px -8px rgba(0, 113, 227, 0.08),
      inset 0 1px 1px rgba(255, 255, 255, 1);
  }

  /* Apple Cupertino Tactile Buttons with Spring Haptics */
  .btn-apple-blue {
    background: linear-gradient(180deg, #0077ED 0%, #0066CC 100%);
    color: #FFFFFF;
    font-weight: 700;
    border-radius: 9999px;
    border: 1px solid rgba(255, 255, 255, 0.35);
    box-shadow: 0 4px 14px rgba(0, 113, 227, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.4);
    transition: transform 150ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 150ms cubic-bezier(0.16, 1, 0.3, 1);
    touch-action: manipulation;
    cursor: pointer;
  }
  .btn-apple-blue:hover {
    background: linear-gradient(180deg, #0A84FF 0%, #0071E3 100%);
    box-shadow: 0 6px 20px rgba(0, 113, 227, 0.38);
    transform: translateY(-0.5px);
  }
  .btn-apple-blue:active {
    transform: scale(0.96) translateY(0.5px);
  }

  .btn-apple-pill {
    background: rgba(255, 255, 255, 0.94);
    color: #1D1D1F;
    font-weight: 600;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 9999px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 1);
    transition: transform 150ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 150ms cubic-bezier(0.16, 1, 0.3, 1);
    touch-action: manipulation;
    cursor: pointer;
  }
  .btn-apple-pill:hover {
    background: #FFFFFF;
    border-color: rgba(0, 0, 0, 0.16);
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
    transform: translateY(-0.5px);
  }
  .btn-apple-pill:active {
    transform: scale(0.96) translateY(0.5px);
  }

  /* Tactile class for interactive chips */
  .btn-tactile {
    touch-action: manipulation;
    cursor: pointer;
    user-select: none;
    transition: transform 140ms cubic-bezier(0.16, 1, 0.3, 1), opacity 140ms ease;
  }
  .btn-tactile:hover { transform: translateY(-0.5px); }
  .btn-tactile:active { transform: scale(0.95); }

  /* Silk Flow Progress Fill */
  .fuel-progress-fill {
    transition: width 650ms cubic-bezier(0.16, 1, 0.3, 1), background-color 300ms ease;
    background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.22) 0%, rgba(0, 0, 0, 0.04) 100%);
  }
</style>
```

---

## 3. Real AGY Router Status Pill Patterns

Signature rounded capsule badges from the AGY Router production console:

### A. Liquid Pool Pill Badge (Header / Logo Chip)

```html
<span class="inline-flex items-center font-mono-apple text-[9.5px] font-bold tracking-wider uppercase px-2 py-0.5 rounded-full bg-[#0071E3]/[0.08] text-[#0071E3] border border-[#0071E3]/20">
  LIQUID POOL
</span>
```

### B. Primary Active Beacon Pill (Hero Section)

```html
<span class="inline-flex items-center space-x-1.5 px-2 py-0.5 rounded-full text-[11px] sm:text-[13px] font-bold bg-[#30D158] text-white shadow-sm shadow-emerald-500/25">
  <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
  <span>PRIMARY ACTIVE</span>
</span>
```

### C. Dynamic Island Toast Notification

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

## 4. Silk Flow Meter & Concentric Nested Radii

### Concentric Radius Nesting Rules

- Exterior container: `rounded-3xl` (24px) or `rounded-2xl` (20px).
- Internal cards: `rounded-2xl` (16px) or `rounded-xl` (12px).
- Inner buttons / inputs: `rounded-xl` (10px) or `rounded-lg` (8px).
- Capsule pills: `rounded-full` (9999px).

### Silk Flow Quota Progress Bar

```html
<div class="bg-white/90 rounded-2xl p-3 sm:p-3.5 border border-black/[0.05] shadow-[0_1px_3px_rgba(0,0,0,0.02)] flex flex-col justify-between space-y-1.5">
  <div class="flex justify-between items-center text-[11px] font-bold">
    <span class="text-[#86868B]">QUOTA CAPACITY</span>
    <span class="font-mono-apple text-[#30D158]">88%</span>
  </div>
  <div class="w-full bg-black/[0.06] rounded-full h-2 overflow-hidden p-0.5">
    <div class="h-full rounded-full fuel-progress-fill bg-[#30D158]" style="width: 88%"></div>
  </div>
</div>
```

---

## 5. Zero-Flicker Tab Navigation (Alpine.js)

Seamless tab switching styled in authentic Cupertino navigation cards:

```html
<div x-data="{ activeTab: 'dashboard' }" class="space-y-4">
  <!-- Sidebar / Nav Tab Item -->
  <button type="button" @click="activeTab = 'dashboard'"
          class="w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-2xl text-xs font-semibold transition-all duration-150 cursor-pointer"
          :class="activeTab === 'dashboard' 
            ? 'bg-gradient-to-b from-[#0077ED] to-[#0066CC] text-white shadow-md shadow-blue-500/25 border border-white/25' 
            : 'text-[#1D1D1F] hover:bg-white/80'">
    <span>Dashboard</span>
  </button>

  <!-- Tab Content with Subtle Rise -->
  <div x-show="activeTab === 'dashboard'"
       x-cloak
       x-transition:enter="transition ease-out duration-200"
       x-transition:enter-start="opacity-0 translate-y-1"
       x-transition:enter-end="opacity-100 translate-y-0"
       class="crystal-card p-6">
    <!-- Panel Content -->
  </div>
</div>
```

---

## 6. Zero-Bloat Standalone Stack Checklist

- Zero `node_modules` at runtime.
- Pure Standalone CDN / Local Single Script for Tailwind CSS & Alpine.js.
- Native Lucide / Heroicons inline SVG.
- Client wire transfer < 60 KB.
