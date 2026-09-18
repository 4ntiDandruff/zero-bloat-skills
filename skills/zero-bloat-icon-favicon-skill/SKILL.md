---
name: zero-bloat-icon-favicon-skill
description: "Generator icon, favicon, app touch icon, dan PWA web asset berbasis siluet geometris solid Pastree-grade: grid 64x64, rasio squircle emas 25%, breathing room 22%, multi-size C-native slicing (ICO 16/32/48/64, Apple 180, PWA 192/512), tanpa dependensi Node.js."
---

# Zero-Bloat Icon & Favicon Engine Skill (Pastree Standard)

SOP rekayasa dan generator aset visual digital web (favicon, touch-icon, app icon, dan manifest) berbasis siluet vektor geometris padat (solid silhouettes), zero build-step, dan bebas dependensi Node.js/npm. Terinspirasi langsung dari standar minimalis elegan `pastree.megapass.web.id` yang terbukti tajam di tab browser (16x16 px) maupun layar Retina resolusi tinggi.

---

## 1. Empat Hukum Fisika Favicon Pastree-Grade

Favicon yang tampak murahan atau buram umumnya diakibatkan oleh pemaksaan detail 3D, gradasi pelangi acak, atau garis-garis mikro tipis yang saat mengecil ke 16x16 px berubah menjadi noda kabur.

Modul ini mewajibkan 4 sekring estetika:

1. **Siluet Geometris Padat (Solid Silhouette)**:
   - Simbol WAJIB berupa bidang padat berbobot tebal (solid filled shapes), BUKAN garis goresan tipis (*hairline strokes*).
   - Bentuk siluet tunggal atau ganda (maksimal 2 elemen geometris tegas).
   - Lolos The Squint Test 16px: bentuk tetap terbaca seketika saat mata disipitkan.
2. **Rasio Squircle Emas 25% (`rx=16` di Kanvas `64x64`)**:
   - Kanvas berukuran `viewBox="0 0 64 64"` dengan radius sudut `<rect width="64" height="64" rx="16"/>`.
   - Rasio 16/64 = 0.25 (25%) menghasilkan kontur kurva squircle continuous curvature khas ekosistem Apple yang menyatu dengan browser modern.
3. **Ruang Bernapas Lega (Breathing Room 22-25% Margin)**:
   - Simbol foreground hanya menempati 55-60% area kanvas dan terpusat (centered) secara presisi.
   - Margin atas, bawah, kiri, dan kanan minimal 14px (22%) dari tepi kanvas 64x64. Simbol dilarang menabrak atau mepet ke pinggir squircle.
4. **Warna Datar Bermartabat & Kontras Tinggi (Zero-Glow)**:
   - Gunakan latar warna solid matang: Deep Emerald (`#0E7C61`), Deep Slate (`#0B1220`), Royal Indigo (`#2563EB`), atau Kas Emerald (`#0AA477`).
   - Simbol foreground: Pure White (`#FFFFFF`) dengan `opacity=".95"` atau Electric Cyan (`#22D3EE`).
   - DILARANG menggunakan efek glow semu (`radialGradient` kabur) yang merusak kontras dan membuat ikon terlihat buram.

---

## 2. Katalog Preset Siluet Geometris Solid

### Preset 1: `tree` (Signature Pastree Organic)
Terinspirasi langsung dari `pastree.megapass.web.id`. Siluet canopy tetes air dan batang silinder membulat di atas lempengan Deep Emerald.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#0E7C61"/>
  <path d="M32 14c-8 8-12 13-12 20a12 12 0 0 0 24 0c0-7-4-12-12-20z" fill="#FFFFFF" opacity=".95"/>
  <rect x="29.5" y="38" width="5" height="12" rx="2.5" fill="#FFFFFF"/>
</svg>
```

### Preset 2: `bolt` (High-Voltage Energy & Skill Hub)
Siluet petir tebal solid terpusat dengan sudut potong tajam. Sangat pas untuk aplikasi performa tinggi, AI accelerator, atau alat diagnosa hardware.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#2563EB"/>
  <path d="M34 13L19 33h9l-3 18 17-23h-10l4-15z" fill="#FFFFFF"/>
</svg>
```

### Preset 3: `circuit` (Solid Processor Die & Pins)
Die silikon prosesor tebal dengan pin sirkuit 4px padat berkepala kapsul (pill). Nol garis tipis, menjamin keterbacaan penuh di ukuran 16 piksel.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#0B1220"/>
  <rect x="22" y="22" width="20" height="20" rx="5" fill="#22D3EE"/>
  <circle cx="32" cy="32" r="3.5" fill="#0B1220"/>
  <rect x="25" y="14" width="4" height="6" rx="2" fill="#22D3EE"/>
  <rect x="35" y="14" width="4" height="6" rx="2" fill="#22D3EE"/>
  <rect x="25" y="44" width="4" height="6" rx="2" fill="#22D3EE"/>
  <rect x="35" y="44" width="4" height="6" rx="2" fill="#22D3EE"/>
  <rect x="14" y="25" width="6" height="4" rx="2" fill="#22D3EE"/>
  <rect x="14" y="35" width="6" height="4" rx="2" fill="#22D3EE"/>
  <rect x="44" y="25" width="6" height="4" rx="2" fill="#22D3EE"/>
  <rect x="44" y="35" width="6" height="4" rx="2" fill="#22D3EE"/>
</svg>
```

### Preset 4: `terminal` (CLI Chevron & Cursor)
Simbol prompt terminal tajam dengan kursor horizontal tebal. Cocok untuk tools CLI, monitoring server Linux, atau AI agent console.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#0B1220"/>
  <path d="M20 19l10 13-10 13" fill="none" stroke="#22D3EE" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="36" y1="45" x2="47" y2="45" stroke="#22D3EE" stroke-width="5" stroke-linecap="round"/>
</svg>
```

### Preset 5: `kas` (Signature Kas Megapass Chevron)
Pilar vertikal tebal dan lengan panah bersudut padat. Representasi arus kas transaksi dan efisiensi moneter.

### Preset 6: `shield` (Security & OPSEC Fortress)
Lempengan perisai solid dengan potongan inti geometris. Cocok untuk modul otentikasi, perlindungan data, atau WAF security.

### Preset 7: `monogram` (Swiss Heavy Initial)
Huruf kapital tebal berbobot 900 dengan kalibrasi baseline Y=44 pada kanvas 64x64 sehingga tepat berada di titik pusat optik mata.

### Preset 8: `camera` (CCTV & Edge Media Stream)
Bodi kamera solid dengan lensa bertingkat dan tonjolan viewfinder atas. Dirancang khusus untuk modul streaming CCTV dan go2rtc.

### Preset 9: `wifi` (Mesh Network & Tunnel Radar)
Titik pemancar solid dengan gelombang radar tebal 5px. Pas untuk infrastruktur Tailscale Mesh, Cloudflare Tunnel, atau jaringan ruko.

### Preset 10: `tools` (Hardware Servicing & Workbench)
Kunci pas mekanik solid dengan sudut 45 derajat dan bukaan rahang tegas. Mewakili meja servis elektronik, hardware, dan perbaikan bare-metal.

---

## 3. Eksekusi Engine Generator

Skrip inti terletak di:
`~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py`

### 1. Menghasilkan dari Preset Bawaan:
Bendera `--preset` atau `--type` dapat digunakan secara bergantian:
```bash
# Preset Pastree standar (Deep Emerald + White)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --preset tree \
  --theme pastree \
  --out ./public

# Preset Lightning dengan palet Royal Indigo
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --type bolt \
  --theme indigo \
  --out ./public

# Preset Hardware Processor dengan palet Deep Slate + Electric Cyan
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --type circuit \
  --theme slate \
  --prefix "/static/" \
  --out ./public
```

### 2. Menghasilkan dari File Master Kustom:
```bash
# Dari file SVG vektor master kustom
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --input ./assets/my_custom_logo.svg \
  --name "Megapass Portal" \
  --out ./public

# Dari file gambar raster PNG/JPG (otomatis dipad ke bujur sangkar anti-distorsi via LANCZOS)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --input ./assets/logo.png \
  --prefix "./" \
  --out ./public
```

---

## 4. Paket Aset Standar yang Dihasilkan

Skrip otomatis merender 8 aset web produksi tanpa meninggalkan file sampah:

| Nama File | Ukuran / Format | Fungsi Teknis |
|---|---|---|
| `favicon.svg` | Vektor 64x64 | Master vektor tajam untuk browser modern |
| `favicon.ico` | Multi-layer (16x16, 32x32, 48x48, 64x64) | Tab browser desktop & bookmark legacy |
| `favicon-16x16.png` | 16x16 PNG RGBA | Tab browser standar |
| `favicon-32x32.png` | 32x32 PNG RGBA | Tab browser display Retina / High-DPI |
| `apple-touch-icon.png` | 180x180 PNG RGBA | Home screen bookmark iOS / Safari |
| `android-chrome-192x192.png` | 192x192 PNG RGBA | PWA manifest Android standard |
| `android-chrome-512x512.png` | 512x512 PNG RGBA | PWA splash screen & Google Play store |
| `site.webmanifest` | JSON UTF-8 | Konfigurasi instalasi aplikasi web PWA |

---

## 5. Standar Injeksi HTML5 (`<head>`)

Selalu tempelkan cuplikan tag berikut di dalam blok `<head>` template HTML:

```html
<!-- Favicon & Touch Assets (Pastree Standard) -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0E7C61">
```

---

## 6. Protokol Verifikasi & Smoke Test

Sebelum menyatakan selesai:
1. Pastikan `favicon.svg` berukuran ringkas (<800 bytes) dan bersih dari elemen filter glow.
2. Pastikan file PNG dan ICO tercipta dengan byte valid (`file *`).
3. Pastikan `favicon.ico` memuat 3 resolusi (16, 32, 48) via utilitas `file favicon.ico`.
4. Pastikan `site.webmanifest` lolos validasi sintaks JSON.
