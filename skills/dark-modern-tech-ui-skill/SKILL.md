---
name: dark-modern-tech-ui-skill
description: "Dark Modern Tech and Slate Glassmorphism UI engineering patterns: Deep Slate foundation (#0B1220), frosted dark glassmorphism (backdrop-blur 16px), electric cyan accents (#22D3EE), Bento grid modular service cards, pricing tier matrix, coverage radius indicators, zero-bloat FAQ accordion, and floating mobile thumb CTA dock without Node.js or bundlers."
---

# Dark Modern Tech UI Skill (Slate Glassmorphism Architecture)

Design system and frontend engineering patterns for building high-conversion, technical workbench interfaces, repair service landing pages, developer consoles, and high-trust digital storefronts without Node.js, npm, or bundler compilation steps.

Directly reverse-engineered and extracted from the production-tested **Megapass Intra Solusindo** flagship web platform (`megapass.web.id`, `install-windows/`, and `home-service/`).

---

## 1. Visual Foundation & Slate Dark Matrix

Strictly avoid flat muddy grays or harsh, eye-straining `#000000` pitch blacks. The authentic Dark Modern Tech aesthetic uses a rich **Deep Slate / Navy Ink** base (`#0B1220`) illuminated by ambient radial cyan gradients and precision frosted glass surfaces.

### Core Color Palette Tokens

```javascript
// Standalone Tailwind Play CDN Theme Extension
tailwind.config = {
  theme: {
    extend: {
      colors: {
        ink: '#0B1220',       // Base canvas foundation (Deep Midnight Slate)
        ink2: '#111A2E',      // Card surface layer 1 (Elevated panel)
        ink3: '#1E293B',      // Inset wells, borders, and input backgrounds
        accent: '#22D3EE',    // Primary high-voltage Electric Cyan (Tailwind cyan-400)
        accent2: '#0891B2',   // Secondary Dark Cyan for gradient stops (cyan-600)
        paper: '#F8FAFC',     // Crisp high-contrast heading text (slate-50)
        muted: '#7E8EA6',     // Secondary readable body text
        muted2: '#94A3B8',    // Subtle metadata, captions, and inactive borders
        body: '#0F172A',      // Alternate dark slate surface
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
      },
    },
  },
};
```

### Depth & Material Elevation Hierarchy

| Surface Level | Visual Specification | CSS Implementation | Semantic Purpose |
|---|---|---|---|
| **Root Canvas** | `#0B1220` with Dual Radial Cyan Fog | `.glow-bg` | Deepest foundation layer; zero layout shifts |
| **Frosted Glass Nav** | `rgba(11, 18, 32, 0.72)` + Blur 16px | `.glass-nav` | Sticky top app bar and floating controls |
| **Elevated Bento Card** | `#111A2E` / `rgba(17, 26, 46, 0.8)` + Border `rgba(255,255,255,0.08)` | `bg-ink2/80 border border-white/8` | Primary feature panels, trust metrics, and service cards |
| **Sunken Inset Well** | `#1E293B` with Inset Shadow | `bg-ink3 border border-white/5` | Code preview wells, input fields, terminal displays |
| **Primary Action Pill** | Linear Gradient `#22D3EE` ➔ `#0891B2` | `.btn-primary` + `.pulse-glow` | Direct conversion triggers (WhatsApp, Checkout, Booking) |
| **Secondary Glass Pill** | `rgba(255,255,255,0.06)` + Border `rgba(255,255,255,0.12)` | `hover:bg-white/10 text-paper` | Learn more triggers, modal dismiss, auxiliary actions |

### Ambient Glow Background & Glass Styling

```css
/* Ambient Radial Cyan Gradients (Lightweight GPU Overhead) */
.glow-bg {
  background:
    radial-gradient(800px 500px at 70% 10%, rgba(34, 211, 238, 0.12), transparent 60%),
    radial-gradient(600px 400px at 20% 90%, rgba(34, 211, 238, 0.06), transparent 60%);
}

/* Frosted Dark Glassmorphism Header */
.glass-nav {
  background: rgba(11, 18, 32, 0.72);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* Electric Cyan Gradient Text */
.text-gradient {
  background: linear-gradient(135deg, #22D3EE 0%, #0891B2 50%, #22D3EE 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Pulse Glow Shadow for Primary Actions */
.pulse-glow {
  box-shadow: 0 8px 30px rgba(34, 211, 238, 0.25);
}
```

---

## 2. Flagship Master Landing Page Architecture (`/`)

The flagship landing page establishes immediate institutional trust within 3 seconds of load time.

### A. High-Trust Hero Section

Features a social proof pill, high-contrast headline with cyan gradient accents, and a dual CTA matrix:

```html
<section class="relative pt-32 pb-20 px-4 sm:px-6 max-w-7xl mx-auto text-center">
  <!-- Social Proof Rating Pill -->
  <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-ink2/90 border border-white/10 mb-8 backdrop-blur-md">
    <div class="flex items-center text-cyan-400">
      <!-- 5-Star Lucide Inline SVG Vector -->
      <svg class="w-4 h-4 fill-cyan-400 text-cyan-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <svg class="w-4 h-4 fill-cyan-400 text-cyan-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <svg class="w-4 h-4 fill-cyan-400 text-cyan-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <svg class="w-4 h-4 fill-cyan-400 text-cyan-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <svg class="w-4 h-4 fill-cyan-400 text-cyan-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
    </div>
    <span class="text-xs font-semibold text-paper">Rating 4.9/5 dari 300+ Ulasan Pelanggan</span>
  </div>

  <!-- Primary Headline with Gradient Shimmer -->
  <h1 class="text-4xl sm:text-6xl font-extrabold text-paper tracking-tight max-w-4xl mx-auto leading-tight sm:leading-none mb-6">
    Solusi Servis Hardware & Laptop <span class="text-gradient">Presisi Bersertifikat</span>
  </h1>

  <p class="text-muted text-base sm:text-lg max-w-2xl mx-auto mb-10 leading-relaxed">
    Perbaikan motherboard, reballing chipset, instalasi sistem operasi bebas bloatware, dan penggantian sparepart bergaransi resmi.
  </p>

  <!-- High-Conversion Action Matrix -->
  <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
    <a href="https://wa.me/628xxxxxxxxxx?text=Halo%20Admin,%20saya%20mau%20konsultasi%20servis"
       class="w-full sm:w-auto px-8 py-4 rounded-xl bg-gradient-to-r from-cyan-400 to-cyan-600 text-slate-950 font-bold text-base flex items-center justify-center gap-2 pulse-glow hover:opacity-95 active:scale-[0.98] transition-transform">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
      Konsultasi Meja Servis
    </a>
    <a href="#layanan"
       class="w-full sm:w-auto px-8 py-4 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-paper font-semibold text-base flex items-center justify-center transition-colors">
      Lihat Daftar Layanan
    </a>
  </div>
</section>
```

### B. Modular Bento Grid Layout

Organizes hardware capabilities into scannable, dense cards with nested icon badges:

```html
<section id="layanan" class="py-16 px-4 sm:px-6 max-w-7xl mx-auto">
  <div class="text-center mb-12">
    <h2 class="text-2xl sm:text-3xl font-bold text-paper tracking-tight">Katalog Solusi Terintegrasi</h2>
    <p class="text-muted text-sm mt-2">Dikerjakan teknisi BNSP dengan peralatan diagnostik osiloskop dan boardview.</p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <!-- Bento Card 1: Motherboard Repair -->
    <div class="bg-ink2/80 border border-white/8 hover:border-cyan-400/30 rounded-2xl p-6 backdrop-blur-md transition-[border-color,transform] duration-300 hover:-translate-y-1">
      <div class="w-12 h-12 rounded-xl bg-cyan-400/10 border border-cyan-400/20 flex items-center justify-center text-cyan-400 mb-4">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
      </div>
      <h3 class="text-lg font-bold text-paper mb-2">Perbaikan Motherboard & IC</h3>
      <p class="text-muted text-sm leading-relaxed mb-4">
        Suntik tegangan jalur pendek, reballing chipset GPU, penggantian IC power, dan reflashing SPI BIOS.
      </p>
      <span class="text-xs font-semibold text-cyan-400 inline-flex items-center gap-1">
        Garansi 30 Hari <span aria-hidden="true">&rarr;</span>
      </span>
    </div>

    <!-- Bento Card 2: Tweaking & OS -->
    <div class="bg-ink2/80 border border-white/8 hover:border-cyan-400/30 rounded-2xl p-6 backdrop-blur-md transition-[border-color,transform] duration-300 hover:-translate-y-1">
      <div class="w-12 h-12 rounded-xl bg-cyan-400/10 border border-cyan-400/20 flex items-center justify-center text-cyan-400 mb-4">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
      </div>
      <h3 class="text-lg font-bold text-paper mb-2">Instalasi & Tweaking Windows</h3>
      <p class="text-muted text-sm leading-relaxed mb-4">
        Windows 10/11 LTSC bebas telemetry, optimasi startup, pembersihan virus rootkit, dan aktivasi driver murni.
      </p>
      <span class="text-xs font-semibold text-cyan-400 inline-flex items-center gap-1">
        Selesai 1-2 Jam <span aria-hidden="true">&rarr;</span>
      </span>
    </div>

    <!-- Bento Card 3: Home Service -->
    <div class="bg-ink2/80 border border-white/8 hover:border-cyan-400/30 rounded-2xl p-6 backdrop-blur-md transition-[border-color,transform] duration-300 hover:-translate-y-1">
      <div class="w-12 h-12 rounded-xl bg-cyan-400/10 border border-cyan-400/20 flex items-center justify-center text-cyan-400 mb-4">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
      </div>
      <h3 class="text-lg font-bold text-paper mb-2">Teknisi Panggilan (Home Service)</h3>
      <p class="text-muted text-sm leading-relaxed mb-4">
        Layanan kunjungan ke rumah atau kantor untuk area Sidoarjo dan sekitarnya tanpa repot membawa perangkat.
      </p>
      <span class="text-xs font-semibold text-cyan-400 inline-flex items-center gap-1">
        Jangkauan 15 KM <span aria-hidden="true">&rarr;</span>
      </span>
    </div>
  </div>
</section>
```

---

## 3. High-Conversion Service Landing Page Patterns (`/install-windows/`)

Dedicated service landing pages convert visitors experiencing specific hardware or software failures.

### A. Customer Pain Points Matrix

Directly mirrors the physical symptoms the customer is suffering from:

```html
<section class="py-12 px-4 sm:px-6 max-w-5xl mx-auto">
  <div class="bg-ink2/60 border border-white/8 rounded-2xl p-6 sm:p-8">
    <h2 class="text-xl font-bold text-paper mb-6 flex items-center gap-2">
      <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
      Gejala Kerusakan yang Biasa Kami Tangani:
    </h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
      <div class="flex items-start gap-3 p-3 rounded-xl bg-ink3/40 border border-white/5">
        <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span class="text-sm text-paper">Laptop terasa lambat, CPU 100%, atau disk usage mentok terus-menerus.</span>
      </div>
      <div class="flex items-start gap-3 p-3 rounded-xl bg-ink3/40 border border-white/5">
        <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span class="text-sm text-paper">Sering muncul Blue Screen (BSOD) saat membuka browser atau game.</span>
      </div>
      <div class="flex items-start gap-3 p-3 rounded-xl bg-ink3/40 border border-white/5">
        <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span class="text-sm text-paper">Gagal booting Windows, hanya berputar di logo merk laptop atau Automatic Repair loop.</span>
      </div>
      <div class="flex items-start gap-3 p-3 rounded-xl bg-ink3/40 border border-white/5">
        <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span class="text-sm text-paper">Iklan malware muncul sendiri di layar dan browser dibajak search engine aneh.</span>
      </div>
    </div>
  </div>
</section>
```

### B. Structured Pricing Tier Matrix

Transparent pricing cards eliminate client anxiety. The middle tier is highlighted with cyan accents:

```html
<section class="py-12 px-4 sm:px-6 max-w-6xl mx-auto">
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
    <!-- Tier 1: Hemat / Basic -->
    <div class="bg-ink2/70 border border-white/8 rounded-2xl p-6 flex flex-col justify-between">
      <div>
        <span class="text-xs font-bold text-muted2 uppercase tracking-wider">Paket Standar</span>
        <h3 class="text-xl font-bold text-paper mt-1">Fresh Install Windows</h3>
        <div class="my-4">
          <span class="text-3xl font-extrabold text-paper">Rp 50.000</span>
        </div>
        <ul class="space-y-3 text-sm text-muted mb-6">
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Windows 10 / 11 Original ISO</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Driver Motherboard & Display Lengkap</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Software Standar (Office, Browser, PDF)</li>
        </ul>
      </div>
      <a href="https://wa.me/628xxxxxxxxxx?text=Halo%20Admin,%20saya%20mau%20ambil%20Paket%20Fresh%20Install"
         class="w-full py-3 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-paper font-semibold text-center text-sm transition-colors">
        Pilih Paket Standar
      </a>
    </div>

    <!-- Tier 2: Highlighted Pro Tweaking (Most Popular) -->
    <div class="bg-ink2/90 border-2 border-cyan-400/50 rounded-2xl p-6 flex flex-col justify-between relative shadow-[0_0_30px_rgba(34,211,238,0.1)]">
      <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-cyan-400 text-slate-950 text-[11px] font-extrabold uppercase tracking-wider">
        Paling Direkomendasikan
      </div>
      <div>
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Paket Komplit</span>
        <h3 class="text-xl font-bold text-paper mt-1">Install + Debloat Gaming</h3>
        <div class="my-4">
          <span class="text-3xl font-extrabold text-paper">Rp 75.000</span>
        </div>
        <ul class="space-y-3 text-sm text-paper mb-6">
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Semua Fitur Paket Standar</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Windows LTSC / Ghost Spectre Edition</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Tweaking RAM & Latensi Low-Ping</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Garansi Sistem 14 Hari</li>
        </ul>
      </div>
      <a href="https://wa.me/628xxxxxxxxxx?text=Halo%20Admin,%20saya%20mau%20ambil%20Paket%20Debloat%20Gaming"
         class="w-full py-3 rounded-xl bg-gradient-to-r from-cyan-400 to-cyan-600 text-slate-950 font-bold text-center text-sm pulse-glow hover:opacity-95 active:scale-[0.98] transition-transform">
        Pilih Paket Komplit
      </a>
    </div>

    <!-- Tier 3: Rescue & Backup -->
    <div class="bg-ink2/70 border border-white/8 rounded-2xl p-6 flex flex-col justify-between">
      <div>
        <span class="text-xs font-bold text-muted2 uppercase tracking-wider">Paket Rescue</span>
        <h3 class="text-xl font-bold text-paper mt-1">Backup Data + Install</h3>
        <div class="my-4">
          <span class="text-3xl font-extrabold text-paper">Rp 125.000</span>
        </div>
        <ul class="space-y-3 text-sm text-muted mb-6">
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Penyelamatan File Dokumen & Foto</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Scanning Bad Sector SSD/Harddisk</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Instalasi Sistem Operasi Baru Bersih</li>
        </ul>
      </div>
      <a href="https://wa.me/628xxxxxxxxxx?text=Halo%20Admin,%20saya%20mau%20ambil%20Paket%20Rescue"
         class="w-full py-3 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-paper font-semibold text-center text-sm transition-colors">
        Pilih Paket Rescue
      </a>
    </div>
  </div>
</section>
```

---

## 4. Field Technician & Home Service Patterns (`/home-service/`)

Designed specifically for on-site services, emergency calls, and home visits.

### A. Coverage Radius & District List

Visual badges reassuring local visitors that their specific area is covered:

```html
<section class="py-12 px-4 sm:px-6 max-w-5xl mx-auto">
  <div class="bg-ink2/70 border border-white/8 rounded-2xl p-6 sm:p-8">
    <div class="flex items-center gap-3 mb-6">
      <div class="w-10 h-10 rounded-lg bg-cyan-400/10 border border-cyan-400/20 flex items-center justify-center text-cyan-400">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
      </div>
      <div>
        <h2 class="text-lg font-bold text-paper">Wilayah Layanan Teknisi Panggilan</h2>
        <p class="text-xs text-muted">Radius maksimal 15 KM dari workshop pusat Candi, Sidoarjo.</p>
      </div>
    </div>

    <!-- District Badges Grid -->
    <div class="flex flex-wrap gap-2">
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Candi
      </span>
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Sidoarjo Kota
      </span>
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Tanggulangin
      </span>
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Buduran
      </span>
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Porong
      </span>
      <span class="px-3 py-1.5 rounded-lg bg-ink3/80 border border-white/5 text-xs text-paper font-medium flex items-center gap-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> Tulangan
      </span>
    </div>
  </div>
</section>
```

### B. 4-Step Home Service Protocol

```html
<section class="py-12 px-4 sm:px-6 max-w-5xl mx-auto">
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
    <!-- Step 1 -->
    <div class="bg-ink2/50 border border-white/5 rounded-xl p-5 relative">
      <span class="text-3xl font-black text-white/10 absolute top-3 right-4">01</span>
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Langkah 1</span>
      <h3 class="text-base font-bold text-paper mt-1 mb-2">Konsultasi Kerusakan</h3>
      <p class="text-xs text-muted leading-relaxed">Kirim foto/video gejala laptop melalui WhatsApp untuk perkiraan biaya awal.</p>
    </div>

    <!-- Step 2 -->
    <div class="bg-ink2/50 border border-white/5 rounded-xl p-5 relative">
      <span class="text-3xl font-black text-white/10 absolute top-3 right-4">02</span>
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Langkah 2</span>
      <h3 class="text-base font-bold text-paper mt-1 mb-2">Penjadwalan Kunjungan</h3>
      <p class="text-xs text-muted leading-relaxed">Tentukan jam kedatangan teknisi ke rumah atau kantor sesuai waktu luang Anda.</p>
    </div>

    <!-- Step 3 -->
    <div class="bg-ink2/50 border border-white/5 rounded-xl p-5 relative">
      <span class="text-3xl font-black text-white/10 absolute top-3 right-4">03</span>
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Langkah 3</span>
      <h3 class="text-base font-bold text-paper mt-1 mb-2">Pengerjaan di Tempat</h3>
      <p class="text-xs text-muted leading-relaxed">Teknisi memeriksa dan memperbaiki unit secara transparan di depan pemilik.</p>
    </div>

    <!-- Step 4 -->
    <div class="bg-ink2/50 border border-white/5 rounded-xl p-5 relative">
      <span class="text-3xl font-black text-white/10 absolute top-3 right-4">04</span>
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Langkah 4</span>
      <h3 class="text-base font-bold text-paper mt-1 mb-2">Pengujian & Garansi</h3>
      <p class="text-xs text-muted leading-relaxed">Uji coba bersama hingga normal 100%, disertai nota fisik dan kartu garansi resmi.</p>
    </div>
  </div>
</section>
```

---

## 5. Mobile Ergonomics & Micro-Interactions

### A. Floating Mobile Thumb Action Dock

Permanent conversion dock positioned directly in the natural thumb zone (bottom 35% of the viewport). Automatically hides on desktop (`md:hidden`):

```html
<!-- Floating Mobile Bottom Dock (Thumb Ergonomics 44px+ Hit Area) -->
<div class="fixed bottom-0 left-0 right-0 z-40 p-3 bg-ink/90 border-t border-white/10 backdrop-blur-xl md:hidden">
  <div class="flex items-center gap-2 max-w-md mx-auto">
    <!-- Secondary Direct Call / Chat Trigger -->
    <a href="tel:+628xxxxxxxxxx"
       class="w-12 h-12 rounded-xl bg-ink2 border border-white/10 flex items-center justify-center text-paper shrink-0 active:scale-95 transition-transform">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
    </a>

    <!-- Primary Full-Width WhatsApp CTA -->
    <a href="https://wa.me/628xxxxxxxxxx?text=Halo%20Admin,%20saya%20mau%20konsultasi%20servis"
       class="flex-1 h-12 rounded-xl bg-gradient-to-r from-cyan-400 to-cyan-600 text-slate-950 font-bold text-sm flex items-center justify-center gap-2 pulse-glow active:scale-[0.98] transition-transform">
      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.076-1.928-.46-1.512-.628-2.47-2.15-2.545-2.251-.074-.102-.619-.824-.619-1.572 0-.749.393-1.117.532-1.269.14-.153.305-.192.407-.192.102 0 .204.002.293.007.094.004.22-.036.344.263.129.313.441 1.077.48 1.155.04.079.066.171.013.275-.053.104-.08.169-.158.261-.079.092-.166.206-.237.276-.079.078-.162.163-.07.321.092.158.409.675.877 1.092.602.536 1.109.702 1.267.78.158.079.251.066.344-.04.093-.105.397-.463.503-.621.106-.158.212-.132.357-.079.146.053.924.436 1.083.515.159.079.265.118.305.184.039.066.039.382-.105.787z"/></svg>
      Chat Teknisi Langsung
    </a>
  </div>
</div>
```

### B. Zero-Bloat FAQ Accordion Pattern

Pure CSS `max-height` transition with accessible keyboard toggling. Zero jQuery, zero external libraries:

```html
<div class="faq-item border-b border-white/8">
  <button type="button"
          onclick="toggleFaq(this)"
          class="w-full py-5 flex items-center justify-between text-left focus:outline-none">
    <span class="text-base font-bold text-paper">Berapa lama waktu pengerjaan servis laptop?</span>
    <svg class="w-5 h-5 text-cyan-400 transition-transform duration-300 transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
  </button>
  <div class="faq-answer max-h-0 overflow-hidden transition-[max-height,padding] duration-300 ease-in-out">
    <p class="text-sm text-muted pb-5 leading-relaxed">
      Kerusakan software dan instalasi ulang selesai dalam 1-2 jam. Untuk perbaikan motherboard atau penggantian IC, estimasi waktu 1-3 hari kerja tergantung ketersediaan part.
    </p>
  </div>
</div>

<script>
function toggleFaq(btn) {
  const answer = btn.nextElementSibling;
  const icon = btn.querySelector('svg');
  const isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';

  // Close all open FAQs
  document.querySelectorAll('.faq-answer').forEach(el => el.style.maxHeight = '0px');
  document.querySelectorAll('.faq-item svg').forEach(el => el.classList.remove('rotate-180'));

  if (!isOpen) {
    answer.style.maxHeight = answer.scrollHeight + 'px';
    icon.classList.add('rotate-180');
  }
}
</script>
```

---

## 6. Implementation & Verification Checklist

When constructing a new page using this skill, verify against these strict rules:

- [ ] **Zero-Emoji Compliance**: No Unicode emoji icons allowed in UI markup. Use crisp inline Lucide SVG vectors.
- [ ] **Zero-Em-Dash Typography**: No `&mdash;` or raw em dashes in copy. Use standard hyphens (`-`) or directional arrows (`→`).
- [ ] **DOM Balance Validation**: Opening and closing tags for `<div>`, `<section>`, `<nav>`, `<header>` must match exactly (`diff = 0`).
- [ ] **Colocation Principle**: Theme config, styling classes, and markup must reside together in the template. No webpack/vite compilation steps.
- [ ] **Tactile Press States**: Interactive buttons must declare `active:scale-[0.98]` with explicit transition scoping (`transition-[transform,opacity,border-color]`).
- [ ] **OPSEC Sanitization**: Never hardcode production phone numbers or private coordinates in public-facing templates without environment injection.
