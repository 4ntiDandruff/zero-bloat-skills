---
name: liquid-apple-ui-skill
description: "Apple-inspired liquid dark UI design system: slate glassmorphism, glowing status pill badges, zero-flicker Alpine.js tab transitions, optical icon-text alignment, and zero-bloat standalone Tailwind implementation without node_modules."
---

# Liquid Apple UI Skill

Design system and engineering patterns for crafting Apple-caliber dark interfaces in web applications without heavyweight frontend framework dependencies (React, Next.js, or runtime `node_modules`).

Battle-tested in the **AGY Router** mission-control console and **Megapass** workbench applications.

---

## 1. Visual Hierarchy & Slate Palette

Never use pure flat black (`#000000`) for surfaces or plain gray for cards. Use cohesive cool-slate depth:

| Component Level | Tailwind Class | Semantic Purpose |
|---|---|---|
| Background Canvas | `bg-slate-950` | Deepest foundation layer |
| Secondary Navigation | `bg-slate-900/60 backdrop-blur-md` | Glass sidebar & sticky topbars |
| Elevated Cards | `bg-slate-900/40 border border-slate-800/80` | Interactive panels & data containers |
| Accent Hairlines | `border-cyan-800/50` or `border-slate-800/80` | Subtle razor-sharp 1px dividers |
| Active Highlights | `text-cyan-400 bg-cyan-950/60 border-cyan-800/50` | Focused buttons, active tabs |
| Monospace Metadata | `font-mono text-xs text-slate-400` | Hardware IDs, status badges, metrics |

---

## 2. The Apple Liquid Pill Badge Pattern

Signature rounded capsule badge with a glowing real-time status beacon (as seen in AGY Router's `LIQUID POOL` indicator):

```html
<!-- Apple-Style Liquid Status Pill -->
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900/90 border border-slate-800/80 shadow-inner">
    <!-- Pulsing Radar Indicator Beacon -->
    <span class="relative flex h-2 w-2">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
    </span>
    
    <!-- Optical Typography -->
    <span class="text-[11px] font-mono font-bold tracking-wider text-slate-200 uppercase">
        LIQUID POOL
    </span>
    
    <!-- Subtle Tag Separator -->
    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-cyan-950/80 text-cyan-400 border border-cyan-800/40">
        ACTIVE
    </span>
</div>
```

---

## 3. Zero-Flicker Tab Transitions (Alpine.js)

Eliminate white-screen flashes, layout shifts (CLS), and jarring DOM jumps during panel switching:

```html
<div x-data="{ currentTab: 'dashboard' }" class="space-y-4">
    <!-- Navigation Buttons -->
    <nav class="flex items-center gap-1 p-1 bg-slate-900/80 rounded-xl border border-slate-800/80 max-w-fit">
        <button @click="currentTab = 'dashboard'"
                :class="currentTab === 'dashboard' 
                    ? 'bg-slate-800 text-cyan-400 shadow-sm border border-slate-700/60' 
                    : 'text-slate-400 hover:text-slate-200'"
                class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-150 flex items-center gap-2">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            Dashboard
        </button>

        <button @click="currentTab = 'settings'"
                :class="currentTab === 'settings' 
                    ? 'bg-slate-800 text-cyan-400 shadow-sm border border-slate-700/60' 
                    : 'text-slate-400 hover:text-slate-200'"
                class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-150 flex items-center gap-2">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
            Settings
        </button>
    </nav>

    <!-- Content Panels with Gentle Fade & Subtle Rise -->
    <section x-show="currentTab === 'dashboard'"
             x-transition:enter="transition ease-out duration-150"
             x-transition:enter-start="opacity-0 translate-y-1"
             x-transition:enter-end="opacity-100 translate-y-0"
             class="p-6 rounded-2xl bg-slate-900/40 border border-slate-800/80">
        <!-- Dashboard Panel Content -->
    </section>

    <section x-show="currentTab === 'settings'"
             x-cloak
             x-transition:enter="transition ease-out duration-150"
             x-transition:enter-start="opacity-0 translate-y-1"
             x-transition:enter-end="opacity-100 translate-y-0"
             class="p-6 rounded-2xl bg-slate-900/40 border border-slate-800/80">
        <!-- Settings Panel Content -->
    </section>
</div>
```

---

## 4. Optical Alignment Rules

1. **Icons and Capital Letters**:
   * Standard 16px SVG icons paired with 14px text often look sunken or low.
   * Apply `flex items-center gap-2` and ensure icons have `shrink-0`.
2. **Monospace Badges with Geometric Headings**:
   * Pair bold geometric sans-serif headings with high-contrast, uppercase monospace tags (`tracking-wider text-[10px] font-mono font-semibold`).
3. **Corner Radius Nesting**:
   * Exterior container radius: `rounded-2xl` (16px).
   * Interior card/panel radius: `rounded-xl` (12px).
   * Interior button/input radius: `rounded-lg` (8px).
   * Capsule badge radius: `rounded-full` (9999px).
   * This nested scaling prevents awkward corner gaps (*optical clash*).

---

## 5. Zero-Bloat Standalone Stack Checklist

- Load Tailwind CSS via standalone script or pre-compiled single CSS file.
- Load Alpine.js via deferred script tag (`<script defer src="..."></script>`).
- Use inline SVG for symbols (Heroicons / Lucide format) rather than icon-font stylesheets.
- Ensure total client bundle size remains **< 60 KB** over the wire.
