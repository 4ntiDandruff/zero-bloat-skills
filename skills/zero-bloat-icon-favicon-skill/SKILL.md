---
name: zero-bloat-icon-favicon-skill
description: "Generator icon, favicon, app touch icon, dan PWA web asset berstandar ganda: Cupertino Crystal Glass (skill.megapass.web.id) dan Minimalist Flat (pastree.megapass.web.id): grid 64x64, rasio squircle emas, Lucide-scale 24x24 geometry, highlight refraction bevel, multi-size C-native slicing (ICO 16/32/48/64, Apple 180, PWA 192/512), tanpa dependensi Node.js."
---

# Zero-Bloat Icon & Favicon Engine Skill (Cupertino Glass & Pastree Standard)

SOP rekayasa dan generator aset visual digital web (favicon, touch-icon, app icon, dan manifest) berbasis siluet vektor geometris presisi, zero build-step, dan bebas dependensi Node.js/npm. Terinspirasi langsung dari dua proyek kanonikal ruko Megapass Intra Solusindo:
1. `skill.megapass.web.id`: Apple Cupertino Crystal Glass squircle (`rx="18"`), gradien dua arah (`#2563EB` -> `#6366F1`), highlight bevel refleksi atas, dan simbol vektor Lucide scale-2.
2. `pastree.megapass.web.id`: Minimalist flat squircle (`rx="16"`), latar warna Deep Emerald (`#0E7C61`), dan siluet kanopi organik padat.

---

## 1. Dua Standar Fisika Visual Favicon Ruko

### A. Gaya Cupertino Crystal Glass (`--style glass`)
Merupakan standar visual utama pada portal modern (`skill.megapass.web.id`). Memiliki 4 elemen konstruksi fisik:
1. **Lempengan Gradien Direksional**: Kanvas `64x64` dengan `rx="18"` diisi gradien diagonal dari kiri-bawah ke kanan-atas (`x1="0%" y1="100%"` ke `x2="100%" y2="0%"`).
2. **Highlight Refraction Bevel (Efek Kaca Kristal)**: Stroke bagian dalam selebar 1.5px (`rect x="1" y="1" width="62" height="62" rx="17"`) dengan gradien putih vertikal opasitas 0.45 di bagian atas meredup ke 0 di bagian bawah. Memberikan efek bias cahaya kaca tebal tanpa membebani GPU.
3. **Geometri Vektor Lucide Scale-2**: Menggunakan koordinat baku ikon 24x24 yang ditransformasikan via `<g transform="translate(8, 8) scale(2)">`. Menghasilkan simbol berukuran 48x48 tepat di tengah kanvas dengan margin 8px (25% breathing room).
4. **Stroke Membulat Anti-Pixelation**: Menggunakan `stroke-width="2.2"` hingga `2.5"`, `stroke-linecap="round"`, dan `stroke-linejoin="round"` sehingga tidak bergerigi saat diperkecil ke ukuran tab 16px.

### B. Gaya Minimalist Flat (`--style flat`)
Merupakan standar visual minimalis pada utilitas cepat (`pastree.megapass.web.id`):
1. **Lempengan Warna Solid Matang**: Kanvas `64x64` dengan rasio squircle emas 25% (`rx="16"`), tanpa gradasi maupun bayangan semu.
2. **Siluet Geometris Padat**: Simbol tunggal berbobot tebal yang menyatu kontras dengan latar belakang. Lolos The Squint Test 16px seketika.
3. **Ukuran File Ultra-Kecil**: Hanya berkisar 290 byte, tercepat diakses dan nol latensi render.

---

## 2. Katalog 10 Preset Vektor Siap Pakai

Semua preset terkalibrasi presisi pada kanvas 64x64 dan mendukung kedua mode visual (`glass` dan `flat`):

### Preset 1: `bolt` (Skill Hub & High-Voltage Energy)
Baku identik dari `skill.megapass.web.id`. Siluet petir dinamis dengan ujung rounded.
```xml
<g transform="translate(8, 8) scale(2)">
  <path d="M13 10V3L4 14h7v7l9-11h-7z" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

### Preset 2: `tree` (Pastree Minimalist Organic)
Baku identik dari `pastree.megapass.web.id`. Kanopi droplet organik dengan batang silinder membulat.
```xml
<path d="M32 14c-8 8-12 13-12 20a12 12 0 0 0 24 0c0-7-4-12-12-20z" fill="#FFFFFF" opacity=".95"/>
<rect x="29.5" y="38" width="5" height="12" rx="2.5" fill="#FFFFFF"/>
```

### Preset 3: `circuit` (Processor Die & Hardware Workbench)
Die silikon prosesor dengan pin rails terhubung. Dirancang untuk diagnosa motherboard dan BIOS.
```xml
<g transform="translate(8, 8) scale(2)">
  <rect x="4" y="4" width="16" height="16" rx="2" fill="none" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="9" y="9" width="6" height="6" fill="#22D3EE" opacity="0.35"/>
  <path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 15h3M1 9h3M1 15h3" fill="none" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

### Preset 4: `terminal` (CLI Chevron & Cursor)
Prompt terminal interaktif dan kursor horizontal tebal. Sempurna untuk konsol admin dan daemon.
```xml
<g transform="translate(8, 8) scale(2)">
  <polyline points="4 17 10 11 4 5" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="12" y1="19" x2="20" y2="19" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
</g>
```

### Preset 5: `shield` (OPSEC Fortress & Security)
Perisai perlindungan solid untuk modul otentikasi, WAF, dan sanitasi kredensial.
```xml
<g transform="translate(8, 8) scale(2)">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M12 8v8M9 12h6" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
</g>
```

### Preset 6: `tools` (Hardware Servicing & Wrench)
Kunci pas mekanik bersudut presisi meja servis untuk perbaikan bare-metal.

### Preset 7: `wifi` (Mesh Network & Tunnel Radar)
Pemancar sinyal dan gelombang konsentris untuk Tailscale dan Cloudflare Tunnel.

### Preset 8: `camera` (CCTV Streaming & Media)
Kamera pengawas dengan lensa terpusat untuk go2rtc dan WebRTC zero-transcode.

### Preset 9: `kas` (Kas Megapass & POS Terminal)
Terminal transaksi dan kartu chip keuangan untuk kasir dan pembukuan ruko.

### Preset 10: `monogram` (Swiss Heavy Initial)
Huruf inisial tebal berbobot 900 dengan kalibrasi baseline optik pada Y=44.

---

## 3. Eksekusi Engine Generator

Skrip generator terletak di:
`~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py`

### 1. Mode Standar Proyek Kanonikal:
```bash
# Hasilkan favicon persis seperti skill.megapass.web.id (Cupertino Crystal Glass)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --preset bolt \
  --theme skill \
  --style glass \
  --out ./public

# Hasilkan favicon persis seperti pastree.megapass.web.id (Minimalist Flat Emerald)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --preset tree \
  --theme pastree \
  --style flat \
  --out ./public
```

### 2. Kustomisasi Gradien dan Tema:
```bash
# Mode Slate Dark Modern Tech dengan custom gradient stops
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --preset circuit \
  --theme slate \
  --style glass \
  --bg "#0B1220" \
  --bg2 "#1E293B" \
  --fg "#22D3EE" \
  --prefix "/static/" \
  --out ./public
```

### 3. Mengiris dari Master File Kustom (SVG / PNG):
```bash
# Dari master SVG eksternal
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --input ./assets/custom_logo.svg \
  --name "Megapass Portal" \
  --out ./public
```


### 4. Glyph Kustom (Siluet SVG Bebas):

Untuk ikon dengan siluet khusus (logo kustom, maskot, bentuk organik) yang tidak tersedia di 10 preset bawaan, gunakan flag `--glyph` (inline SVG fragment) atau `--glyph-file` (path ke file SVG):

```bash
# Inline SVG glyph: siluet payung gaya Umbrel di atas squircle ungu
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --glyph '<g transform="translate(14, 14) scale(1.5)"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.1.9 2 2 2h2v-2H4c0-4.42 3.58-8 8-8s8 3.58 8 8h-2v2h2c1.1 0 2-.9 2-2 0-5.52-4.48-10-10-10zm0 6c-2.21 0-4 1.79-4 4v6h2v-6c0-1.1.9-2 2-2s2 .9 2 2v6h2v-6c0-2.21-1.79-4-4-4z" fill="#FFFFFF"/></g>' \
  --bg "#5351FB" \
  --style flat \
  --out ./public

# Dari file SVG eksternal (wrapper <svg> otomatis di-strip, isi diekstrak)
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py \
  --glyph-file ./assets/my-logo-glyph.svg \
  --bg "#1E40AF" \
  --bg2 "#7C3AED" \
  --style glass \
  --out ./public
```

**Aturan koordinat glyph kustom:**
- ViewBox kanvas adalah `0 0 64 64`. Semua koordinat glyph relatif terhadap grid ini.
- Gunakan `<g transform="translate(X, Y) scale(S)">` untuk memposisikan dan menskala glyph agar terpusat.
- Untuk ikon Lucide/Material 24x24, transformasi baku: `translate(8, 8) scale(2)` (menghasilkan 48x48 di tengah dengan 8px margin).
- Untuk siluet organik yang sudah di-design pada grid 64x64, tidak perlu transform.
- Elemen `<script>`, atribut `on*` (onclick, onload), dan `javascript:` URI otomatis ditolak oleh sanitizer keamanan.
---

## 4. Paket 11 Aset Produksi yang Dihasilkan

Engine secara otomatis menyusun bundel lengkap yang mencakup standar Google Search Console, Apple Safari, dan PWA:

| Nama File | Ukuran / Format | Fungsi Teknis |
|---|---|---|
| `favicon.svg` | Vektor 64x64 (<1.2 KB) | Master vektor tajam untuk browser modern |
| `favicon.ico` | Multi-layer (16, 32, 48, 64) | Tab desktop legacy, bookmark, dan URL bar |
| `favicon-16x16.png` | 16x16 PNG RGBA | Tab browser standar |
| `favicon-32x32.png` | 32x32 PNG RGBA | Tab browser display Retina / High-DPI |
| `favicon-48x48.png` | 48x48 PNG RGBA | Rekomendasi resmi Google Search Crawler |
| `favicon-96x96.png` | 96x96 PNG RGBA | Desktop shortcut dan Google TV / Smart TV |
| `favicon-192x192.png` | 192x192 PNG RGBA | PWA manifest Android standard |
| `apple-touch-icon.png` | 180x180 PNG RGBA | Home screen bookmark iOS Safari |
| `android-chrome-192x192.png` | 192x192 PNG RGBA | Android launcher icon |
| `android-chrome-512x512.png` | 512x512 PNG RGBA | PWA splash screen & Google Play store |
| `site.webmanifest` | JSON UTF-8 | Konfigurasi instalasi aplikasi web PWA |

---

## 5. Standar Injeksi Template HTML5 (`<head>`)

Tempelkan cuplikan berikut pada `<head>` dokumen web:

```html
<!-- Favicon & Touch Assets (Skill & Pastree Standard) -->
<link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
<link rel="icon" type="image/x-icon" href="/static/favicon.ico">
<link rel="icon" type="image/png" sizes="48x48" href="/static/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
<link rel="manifest" href="/static/site.webmanifest">
<meta name="theme-color" content="#2563EB">
```

---

## 6. Protokol Verifikasi Mandiri

Jalankan self-test diagnostik terpadu:
```bash
python3 ~/zero-bloat-skills/skills/zero-bloat-icon-favicon-skill/scripts/generate_favicon.py --test
```
Kriteria kelulusan:
1. Paritas 100% bit-for-bit dengan master `skill.megapass.web.id` dan `pastree.megapass.web.id`.
2. Seluruh 10 preset menghasilkan vektor SVG valid berukuran ringkas (<1400 byte).
3. Bundel aset 11 file terkompilasi sempurna di direktori pengujian `/tmp/`.
4. File `favicon.ico` memuat 4 layer multi-resolusi (16, 32, 48, 64).
5. File `site.webmanifest` lolos validasi W3C PWA.
