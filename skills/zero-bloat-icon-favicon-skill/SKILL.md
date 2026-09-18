---
name: zero-bloat-icon-favicon-skill
description: "Generator icon, favicon, app touch icon, dan PWA web asset berbasis vektor SVG geometris murni: multi-size C-native slicing (ICO 16/32/48, Apple touch icon 180x180, PWA 192/512), 3 preset visual anti-norak (Minimal Monogram, Circuit Tech Glyph, Cupertino Squircle), zero-bloat engine Python Pillow/rsvg-convert, dan auto-wiring HTML meta tags tanpa dependensi Node.js."
---

# Zero-Bloat Icon & Favicon Engine Skill

SOP rekayasa dan generator aset visual digital web (favicon, touch-icon, app icon, dan manifest) berbasis vektor geometris presisi, zero build-step, dan bebas dependensi Node.js/npm. Menjamin tampilan tajam di layar Retina, terbaca jelas di tab browser (16x16 px), dan steril dari kesan norak (*anti-AI slop*).

---

## 1. Tiga Hukum Desain Favicon (Anti-Norak Guardrails)

Favicon yang tampak murahan atau norak umumnya diakibatkan oleh AI yang memaksakan detail 3D, gradasi pelangi acak, atau ilustrasi kartun yang ketika mengecil menjadi 16x16 px berubah menjadi noda buram tak terbaca.

Modul ini mewajibkan 3 sekring estetika:

1. **The Squint Test (Hukum Keterbacaan 16 Piksel)**:
   - Desain master (512x512) WAJIB tetap dikenali saat mata disipitkan (*squinted*) atau dikecilkan ke 16x16 piksel di tab browser.
   - Dilarang garis tipis (<20px pada canvas 512x512).
   - Dilarang teks panjang atau slogan (maksimal 1-2 huruf kapital tebal).
   - Maksimalkan kontras antara latar belakang (*Deep Slate*) dan simbol (*Electric Cyan* / *White*).
2. **Kontur Continuous Curvature (Apple Squircle)**:
   - Hindari kotak bersudut kaku (terkesan purba) atau lingkaran bola biasa (membuang 21% luas area efektif).
   - Gunakan formula *superellipse squircle* kurva Bezier kontinu khas iOS/macOS agar icon tampak menyatu dengan browser modern.
3. **Restrained Color Palette (Maksimal 2-3 Warna)**:
   - Kanvas dasar: Deep Slate (`#0B1220`) atau Matte Obsidian (`#111827`).
   - Warna simbol utama: Electric Cyan (`#22D3EE`), Pure White (`#FFFFFF`), atau Amber Gold (`#F59E0B`).
   - Warna aksen/bayangan sekunder: Dark Cyan (`#0891B2`) atau Slate Ink (`#1E293B`).

---

## 2. Tiga Preset Visual Standar

### Preset A: Minimal Swiss Monogram
Cocok untuk branding personal, nama ruko, atau inisial brand (contoh: huruf "M" Megapass). Menggunakan tipografi grotesque tebal (Plus Jakarta Sans / Inter style) dengan bobot 900 dan tracking ketat.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <path d="M 0,112 C 0,49 49,0 112,0 L 400,0 C 463,0 512,49 512,112 L 512,400 C 512,463 463,512 400,512 L 112,512 C 49,512 0,463 0,400 Z" fill="#0B1220"/>
  <text x="256" y="342" font-family="-apple-system, sans-serif" font-size="288" font-weight="900" text-anchor="middle" fill="#22D3EE">M</text>
</svg>
```

### Preset B: Hardware & Circuit Tech Glyph
Cocok untuk aplikasi servis teknisi, server console, tools sysadmin, atau platform IoT. Menampilkan siluet die prosesor dan jalur trace sirkuit dengan terminal point presisi.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <path d="M 0,112 C 0,49 49,0 112,0 L 400,0 C 463,0 512,49 512,112 L 512,400 C 512,463 463,512 400,512 L 112,512 C 49,512 0,463 0,400 Z" fill="#0B1220"/>
  <g stroke="#22D3EE" stroke-width="28" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <rect x="176" y="176" width="160" height="160" rx="32" fill="#0B1220" stroke="#22D3EE" stroke-width="28"/>
    <circle cx="256" cy="256" r="32" fill="#22D3EE"/>
    <path d="M 216,176 L 216,104 M 296,176 L 296,104 M 216,336 L 216,408 M 296,336 L 296,408 M 336,256 L 408,256 M 176,256 L 104,256"/>
    <circle cx="216" cy="92" r="14" fill="#0891B2" stroke="none"/>
    <circle cx="296" cy="92" r="14" fill="#0891B2" stroke="none"/>
    <circle cx="216" cy="420" r="14" fill="#0891B2" stroke="none"/>
    <circle cx="296" cy="420" r="14" fill="#0891B2" stroke="none"/>
    <circle cx="420" cy="256" r="14" fill="#0891B2" stroke="none"/>
    <circle cx="92" cy="256" r="14" fill="#0891B2" stroke="none"/>
  </g>
</svg>
```

### Preset C: Developer Terminal Prompt (`>_`)
Simbol chevron terminal prompt tajam dengan kursor aktif horizontal. Sangat pas untuk web developer CLI, AI orchestrator, atau dashboard monitoring Linux.

---

## 3. Eksekusi Engine Generator (Slicing Otomatis)

Skrip inti terletak di:
`~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py`

### 1. Menghasilkan dari Preset Bawaan:
```bash
# Monogram huruf 'M' dengan palet Deep Slate + Electric Cyan
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --type monogram \
  --text "M" \
  --bg "#0B1220" \
  --fg "#22D3EE" \
  --out ./public

# Simbol sirkuit hardware dengan prefix path static
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --type circuit \
  --bg "#0B1220" \
  --fg "#22D3EE" \
  --prefix "/static/icons/" \
  --out ./public
```

### 2. Menghasilkan dari File Logo Kustom (Dual-Source: SVG atau Raster PNG):
```bash
# Dari file SVG vektor master
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --input ./assets/my_custom_logo.svg \
  --name "Megapass Portal" \
  --out ./public

# Dari file gambar raster PNG/JPG (otomatis di-pad ke rasio persegi tanpa distorsi)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --input ./assets/logo_rectangular.png \
  --prefix "./" \
  --out ./public
```

---

## 4. Paket Aset Standar yang Dihasilkan

Skrip otomatis merender paket aset web komplit tanpa sisa sampah:

| Nama File | Ukuran / Format | Fungsi Teknis |
|---|---|---|
| `master_icon.svg` | Vektor 512x512 | Master source matematika (resolusi independen) |
| `favicon.ico` | Multi-layer (16x16, 32x32, 48x48) | Tab browser legacy & desktop bookmark |
| `favicon-16x16.png` | 16x16 PNG RGBA | Tab browser modern standar |
| `favicon-32x32.png` | 32x32 PNG RGBA | Tab browser display Retina / High-DPI |
| `apple-touch-icon.png` | 180x180 PNG RGBA | Home screen bookmark iOS / iPadOS Safari |
| `android-chrome-192x192.png` | 192x192 PNG RGBA | PWA manifest Android standard |
| `android-chrome-512x512.png` | 512x512 PNG RGBA | PWA splash screen & Google Play store listing |
| `site.webmanifest` | JSON UTF-8 | Konfigurasi instalasi aplikasi web PWA |

---

## 5. Standar Injeksi HTML5 (`<head>`)

Selalu tempelkan cuplikan tag berikut di dalam blok `<head>` template HTML:

```html
<!-- Favicon & PWA Touch Assets -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0B1220">
```

---

## 6. Protokol Verifikasi & Smoke Test

Sebelum menyatakan selesai:
1. Pastikan seluruh file PNG dan ICO tercipta dengan ukuran byte valid (`file *`).
2. Pastikan file `favicon.ico` memiliki multi-layer (terkonfirmasi via utilitas `file favicon.ico`).
3. Pastikan `site.webmanifest` lolos validasi sintaks JSON.
