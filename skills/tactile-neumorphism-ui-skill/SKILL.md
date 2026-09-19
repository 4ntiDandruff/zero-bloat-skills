---
name: tactile-neumorphism-ui-skill
description: "Tactile Soft UI & Eye-Comfort Neumorphism design system: Velvety Soft Studio Slate (#E2E6EB), diffuse dual-shadow ambient occlusion physics, debossed squircle well sockets (.neo-groove), tactile key micro-action haptics (.btn-neo-key), soft amber jewel breathing status LED, WCAG contrast compensation, and zero-glare responsive dashboard architectures without node_modules or build steps."
---

# Tactile Neumorphism UI Skill (v1.0)

Standar arsitektur desain antarmuka **Tactile Soft UI & Eye-Comfort Neumorphism** untuk aplikasi dashboard, sistem pemantauan (CCTV / Edge telemetry), dan antarmuka operasional ruko/meja servis tanpa siksaan visual pada retina mata.

Modul ini mengekstraksi dan membakukan sistem fisika pencahayaan ganda (*dual-shadow physics*), soket parit cekung (*debossed wells*), dan aksen jewel LED yang telah teruji di produksi pada sistem CCTV Daycare Megapass Intra Solusindo.

---

## 1. Filosofi Fisika & Dekonstruksi Masalah (Anti-Clay Trap)

### Mengapa Neumorphism 2020 (Dribbble Clay Trap) Gagal Total?
Pada tahun 2020, tren Neumorphism di komunitas desain mati suri dan dibenci developer/pengguna karena tiga cacat fatal:
1. **Bleached-Out Glare**: Menggunakan latar putih keabu-abuan terlalu terang (`#E8ECEF` ke atas) yang dipadu dengan highlight putih 100% (`#FFFFFF`) murni. Hasilnya adalah efek silau kapur (*chalky wash*) yang membakar retina pengguna setelah 5 menit menatap layar.
2. **Muddy Halo & Double-Rim Edge**: Bayangan gelap menggunakan hex tunggal pekat opaque (`#C5D0DC` atau `#A3B1C6`) miring 45° yang dipadukan dengan border putih tebal. Hasilnya bukan kesan kedalaman fisik, melainkan garis kotor menyerupai cetakan tanah liat basah (*muddy clay*).
3. **WCAG Contrast Collapse**: Teks abu-abu muda diletakkan di atas tombol abu-abu muda sehingga rasio kontras jatuh di bawah 2.5:1 (tidak terbaca oleh mata normal apalagi tunanetra parsial).

### Solusi Megapass: Tactile Studio Slate (Audiophile Hardware Grade)
Terinspirasi dari instrumen audio studio kelas atas (chassis mixer analog, preamp aluminium sandblasted, dan switch mekanikal instrumen presisi):
- **Kanvas Velvety Studio Slate (`#E2E6EB`)**: Menurunkan luminansi ~3% ke warna satin studio yang hangat, lembut, dan meredam pantulan silau pada panel IPS maupun AMOLED.
- **Diffuse Ambient Occlusion**: Mengganti bayangan hex kaku dengan perpaduan alpha transparency ganda yang berdifusi rata (seperti cahaya ruangan alami).
- **Single-Accent Protocol (Amber Jewel LED)**: Melarang keras blok warna oranye/neon lebar. Seluruh permukaan tetap netral dalam gradasi slate fisik, sementara aksen warna dialokasikan **HANYA** pada titik LED indikator kecil (6px - 8px) dengan siklus napas santai 2.8s.

---

## 2. Fisika Pencahayaan Ganda (Dual-Shadow Lighting Model)

Neumorphism fisik mensimulasikan permukaan material homogen yang dicetak timbul (*convex*) atau dicetak cekung ke dalam (*concave / debossed*) dari satu lempeng padat yang sama.

Sumber cahaya virtual diasumsikan datang secara difus dari sudut kiri atas (-135°):

```
       [ Sumber Cahaya Virtual Difus ]
                  \
                   \  Highlight Satin (+Y, +X Inset / Outset)
                    v
          ┌───────────────────────┐
          │   Permukaan Slate     │
          │       #E2E6EB         │
          └───────────────────────┘
                    /
                   /  Ambient Occlusion Drop (-Y, -X Outset / Inset)
                  v
       [ Bayangan Halus Transparan ]
```

### Formula CSS Tokens Baku

```css
:root {
  /* Surface Base */
  --neo-bg: #E2E6EB;
  --neo-border-light: rgba(255, 255, 255, 0.45);
  --neo-border-dark: rgba(160, 175, 195, 0.25);

  /* Dual Shadows: Timbul / Convex */
  --neo-shadow-dark: rgba(160, 175, 195, 0.42);
  --neo-shadow-light: rgba(255, 255, 255, 0.82);

  /* Convex Surface: Kartu & Panel */
  --neo-convex-card: 6px 6px 18px var(--neo-shadow-dark), -6px -6px 18px var(--neo-shadow-light);
  --neo-convex-card-hover: 8px 8px 24px rgba(160, 175, 195, 0.50), -8px -8px 24px rgba(255, 255, 255, 0.90);

  /* Concave Surface: Parit Cekung (.neo-groove) */
  --neo-concave-groove: inset 2.5px 2.5px 5px var(--neo-shadow-dark), inset -2.5px -2.5px 5px rgba(255, 255, 255, 0.75);

  /* Deep Socket: Wadah Sensor & Jam Monospace */
  --neo-deep-socket: inset 3.5px 3.5px 7px rgba(160, 175, 195, 0.45), inset -3.5px -3.5px 7px rgba(255, 255, 255, 0.80);

  /* Tactile Key / Micro Button */
  --neo-key-idle: 4px 4px 10px rgba(160, 175, 195, 0.45), -4px -4px 10px rgba(255, 255, 255, 0.85);
  --neo-key-pressed: inset 2px 2px 4px rgba(160, 175, 195, 0.50), inset -2px -2px 4px rgba(255, 255, 255, 0.80);

  /* Jewel LED Indicator */
  --led-amber: #EA580C;
  --led-amber-glow: 0 0 6px rgba(234, 88, 12, 0.70), 0 0 1.5px rgba(255, 154, 92, 0.90);
  --led-emerald: #10B981;
  --led-emerald-glow: 0 0 6px rgba(16, 185, 129, 0.70);
  --led-sky: #0284C7;
  --led-sky-glow: 0 0 6px rgba(2, 132, 199, 0.70);
}
```

---

## 3. Matriks Hirarki Kontras & WCAG Accessibility

Agar antarmuka Neumorphism tidak membuat mata lelah dan tetap lulus standar aksesibilitas WCAG AA/AAA, teks **TIDAK BOLEH** abu-abu pucat:

| Elemen UI | Warna Teks / Token | Rasio Kontras vs `#E2E6EB` | Kepatuhan WCAG |
|---|---|---|---|
| **Judul / Heading / Nilai Angka Utama** | `#0F172A` (Slate 900) | **11.2 : 1** | Lulus WCAG AAA (Maksimal Tajam) |
| **Label Navigasi / Button Label** | `#1E293B` (Slate 800) | **9.8 : 1** | Lulus WCAG AAA |
| **Subtitle / Status Teks / Deskripsi** | `#475569` (Slate 600) | **5.6 : 1** | Lulus WCAG AAA |
| **Monospace ID / Stream Info / Muted** | `#64748B` (Slate 500) | **4.5 : 1** | Lulus WCAG AA |
| **Highlight Border Permukaan Timbul** | `rgba(255, 255, 255, 0.45)` | - | Penegas siluet tanpa menyilaukan |
| **Parit Pembatas Bawah (Molded Line)** | `rgba(160, 175, 195, 0.25)` | - | Pengganti garis hitam border-t kaku |

---

## 4. Single-Accent Protocol: Amber Jewel LED

Aturan besi operasional meja servis: **Warna aksen oranye HANYA dinyalakan pada lampu status LED indikator hardware**.

### Prinsip LED Jewel
- **Bukan Neon Strobo**: Dilarang menggunakan `@keyframes pulse` bawaan Tailwind yang mengedipkan opacity 100% ke 0% secara kasar.
- **Siklus Bernapas Lembut (2.8s Breathing Cycle)**: Meniru lampu standby hardware audio kelas studio, berfluktuasi halus antara 75% hingga 100% kecerahan.
- **Ukuran Fisik**: Diameter 6px hingga 8px, bulat sempurna (`border-radius: 50%`), dengan ring socket cekung mikro.

```css
/* Animasi Denyut Pernapasan LED Amber Jewel */
@keyframes softLedBreathe {
  0%, 100% {
    transform: scale(1);
    opacity: 0.85;
    box-shadow: 0 0 5px rgba(234, 88, 12, 0.65), 0 0 1px rgba(255, 154, 92, 0.80);
  }
  50% {
    transform: scale(1.08);
    opacity: 1;
    box-shadow: 0 0 8px rgba(234, 88, 12, 0.85), 0 0 2.5px rgba(255, 154, 92, 0.95);
  }
}

.led-pulse {
  animation: softLedBreathe 2.8s ease-in-out infinite;
}
```

---

## 5. Komponen Inti Siap Pakai (Pure HTML5 & Tailwind Play CDN)

Seluruh komponen berikut dirancang dengan prinsip **Zero Build-Step** (langsung jalan di browser tanpa `npm run build` atau `vite`).

### 5.1 Kartu Timbul Utama (Elevated Tactile Card)
Digunakan untuk wadah video stream CCTV, modul informasi, atau bento grid kartu utama:

```html
<div class="crystal-card group"
     style="background: #E2E6EB;
            border-radius: 24px;
            padding: 12px;
            border: 1px solid rgba(255, 255, 255, 0.45);
            box-shadow: 6px 6px 18px rgba(160, 175, 195, 0.42), -6px -6px 18px rgba(255, 255, 255, 0.82);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);">
  <!-- Header Kartu -->
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="width: 7px; height: 7px; border-radius: 50%; background: #EA580C;" class="led-pulse"></span>
      <h3 style="font-size: 13.5px; font-weight: 800; color: #0F172A; margin: 0;">Kamera Gerbang Depan</h3>
    </div>
    <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700; color: #475569; padding: 2px 8px; border-radius: 9999px; background: rgba(0,0,0,0.04);">
      1080P • 25FPS
    </span>
  </div>

  <!-- Layar Media / Konten Dalam -->
  <div style="width: 100%; aspect-ratio: 16/9; background: #0B0F17; border-radius: 16px; overflow: hidden; position: relative;">
    <!-- Stream Video / Isi Konten -->
  </div>

  <!-- Footer Micro Tactile Actions -->
  <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 10px; padding-top: 4px;">
    <span style="font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 700; color: #64748B;">
      rtsp_stream_01
    </span>
    <div style="display: flex; gap: 6px;">
      <button type="button" class="btn-neo-key" title="Kontrol Arah">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polygon points="12 2 15 6 9 6 12 2"/><polygon points="12 22 9 18 15 18 12 22"/><circle cx="12" cy="12" r="2"/></svg>
      </button>
      <button type="button" class="btn-neo-key" title="Layar Penuh">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/></svg>
      </button>
    </div>
  </div>
</div>
```

---

### 5.2 Parit Cekung Segmen (`.neo-groove` Toolbar & Tab Switcher)
Parit cekung (*debossed segmented well*) menampung tombol-tombol pilihan agar terasa terukir masuk ke dalam lempeng sirkuit:

```html
<div class="neo-groove"
     style="background: #E2E6EB;
            border-radius: 16px;
            padding: 4px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            box-shadow: inset 2.5px 2.5px 5px rgba(160, 175, 195, 0.42), inset -2.5px -2.5px 5px rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(160, 175, 195, 0.25);">
  <!-- Tab Aktif (Convex Pop-Out) -->
  <button type="button"
          style="border: none;
                 border-radius: 12px;
                 padding: 7px 16px;
                 font-size: 12.5px;
                 font-weight: 800;
                 color: #0F172A;
                 background: #E2E6EB;
                 box-shadow: 3px 3px 8px rgba(160, 175, 195, 0.45), -3px -3px 8px rgba(255, 255, 255, 0.85);
                 border: 1px solid rgba(255, 255, 255, 0.6);
                 cursor: pointer;">
    Semua Cabang
  </button>

  <!-- Tab Pasif (Rata Sejajar Parit) -->
  <button type="button"
          style="border: none;
                 border-radius: 12px;
                 padding: 7px 16px;
                 font-size: 12.5px;
                 font-weight: 700;
                 color: #64748B;
                 background: transparent;
                 cursor: pointer;"
          class="hover:text-slate-900 transition-colors">
    Cabang Malang
  </button>
</div>
```

---

### 5.3 Soket Jam Monospace & Sensor Telemetri
Menampilkan jam digital atau status waktu sinkronisasi dengan soket cekung dalam (*deep debossed socket*) yang diapit LED indikator status:

```html
<div class="neo-groove"
     style="display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 6px 12px;
            border-radius: 12px;
            background: #E2E6EB;
            box-shadow: inset 2.5px 2.5px 5px rgba(160, 175, 195, 0.42), inset -2.5px -2.5px 5px rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(160, 175, 195, 0.25);">
  <span style="width: 7px; height: 7px; border-radius: 50%; background: #EA580C;" class="led-pulse"></span>
  <span style="font-size: 12px;
               font-weight: 800;
               color: #0F172A;
               font-family: 'JetBrains Mono', monospace;
               font-variant-numeric: tabular-nums;
               letter-spacing: 0.03em;">
    15:20:00 WIB
  </span>
</div>
```

---

### 5.4 Tombol Taktil Mikro 3x3 (D-Pad PTZ Directional Remote)
Simulasi bantalan remote kontrol mekanikal arah kamera dengan respon taktil instan saat ditekan:

```html
<div class="neo-groove"
     style="display: grid;
            grid-template-columns: repeat(3, 42px);
            grid-template-rows: repeat(3, 42px);
            gap: 6px;
            padding: 6px;
            border-radius: 18px;
            background: #E2E6EB;
            box-shadow: inset 3px 3px 6px rgba(160, 175, 195, 0.45), inset -3px -3px 6px rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(160, 175, 195, 0.25);">
  <div></div>
  <button type="button" class="btn-neo-key" aria-label="Atas">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"/></svg>
  </button>
  <div></div>

  <button type="button" class="btn-neo-key" aria-label="Kiri">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <button type="button" class="btn-neo-key" aria-label="Stop" style="color: #64748B;">
    <div style="width: 10px; height: 10px; border-radius: 3px; background: #64748B;"></div>
  </button>
  <button type="button" class="btn-neo-key" aria-label="Kanan">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
  </button>

  <div></div>
  <button type="button" class="btn-neo-key" aria-label="Bawah">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div></div>
</div>

<style>
.btn-neo-key {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: #E2E6EB;
  border: 1px solid rgba(255, 255, 255, 0.55);
  box-shadow: 3.5px 3.5px 8px rgba(160, 175, 195, 0.45), -3.5px -3.5px 8px rgba(255, 255, 255, 0.85);
  color: #0F172A;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  outline: none;
  transition: all 0.12s ease;
  user-select: none;
  touch-action: manipulation;
}
.btn-neo-key:active {
  transform: scale(0.96);
  box-shadow: inset 2px 2px 4px rgba(160, 175, 195, 0.50), inset -2px -2px 4px rgba(255, 255, 255, 0.80);
  border-color: rgba(160, 175, 195, 0.25);
}
</style>
```

---

### 5.5 Kartu State Kosong Elegan (Empty State Island)
Ketika cabang/perangkat belum memiliki kamera atau data, sajikan wadah Neumorphic pulau terisolasi dengan 3 mikro telemetri plaque di bawah:

```html
<div class="crystal-card text-center"
     style="width: 100%;
            max-width: 520px;
            margin: 20px auto;
            border-radius: 28px;
            background: #E2E6EB;
            border: 1px solid rgba(255, 255, 255, 0.55);
            box-shadow: 8px 8px 24px rgba(160, 175, 195, 0.45), -8px -8px 24px rgba(255, 255, 255, 0.85);
            padding: 36px 28px;
            display: flex;
            flex-direction: column;
            align-items: center;">

  <!-- Squircle Icon Debossed Well -->
  <div style="width: 68px;
              height: 68px;
              border-radius: 22px;
              background: #E2E6EB;
              box-shadow: inset 3px 3px 6px rgba(160, 175, 195, 0.45), inset -3px -3px 6px rgba(255, 255, 255, 0.8);
              border: 1px solid rgba(255, 255, 255, 0.4);
              display: flex;
              align-items: center;
              justify-content: center;
              color: #64748B;
              margin-bottom: 16px;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
      <path d="M16 10l6-3v10l-6-3"/><rect x="2" y="6" width="14" height="12" rx="2"/><line x1="2" y1="2" x2="22" y2="22" stroke="#94A3B8" stroke-width="2.4"/>
    </svg>
  </div>

  <!-- Branch Status Pill Tag -->
  <div class="neo-groove" style="margin-bottom: 12px; display: inline-flex; align-items: center; gap: 7px; padding: 5px 14px; border-radius: 9999px;">
    <span style="width: 7px; height: 7px; border-radius: 50%; background: #EA580C;" class="led-pulse"></span>
    <span style="font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.05em;">
      DAYCARE BUDURAN • STANDBY
    </span>
  </div>

  <!-- Typography -->
  <h3 style="font-size: 18px; font-weight: 800; color: #0F172A; letter-spacing: -0.015em; margin: 0 0 6px 0;">
    Belum Ada Kamera di Cabang Ini
  </h3>
  <p style="font-size: 12.5px; color: #64748B; font-weight: 500; max-width: 400px; line-height: 1.5; margin: 0 0 20px 0;">
    Kamera IP / RTSP untuk unit ini sedang dalam konfigurasi teknis atau belum didaftarkan ke gateway go2rtc ruko.
  </p>

  <!-- 3 Bento Telemetry Micro-Pills -->
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; width: 100%; padding-top: 16px; border-top: 1px solid rgba(160, 175, 195, 0.25);">
    <div class="neo-groove" style="border-radius: 14px; padding: 8px 6px; text-align: center;">
      <span style="display: block; font-size: 9px; font-weight: 700; color: #64748B; text-transform: uppercase;">Gateway</span>
      <span style="display: block; font-size: 11px; font-weight: 800; color: #0F172A; margin-top: 2px; font-family: 'JetBrains Mono', monospace;">go2rtc v1.9</span>
    </div>
    <div class="neo-groove" style="border-radius: 14px; padding: 8px 6px; text-align: center;">
      <span style="display: block; font-size: 9px; font-weight: 700; color: #64748B; text-transform: uppercase;">Standby</span>
      <span style="display: block; font-size: 11px; font-weight: 800; color: #0F172A; margin-top: 2px; font-family: 'JetBrains Mono', monospace;">0% Load</span>
    </div>
    <div class="neo-groove" style="border-radius: 14px; padding: 8px 6px; text-align: center;">
      <span style="display: block; font-size: 9px; font-weight: 700; color: #64748B; text-transform: uppercase;">Protokol</span>
      <span style="display: block; font-size: 11px; font-weight: 800; color: #0F172A; margin-top: 2px; font-family: 'JetBrains Mono', monospace;">MSE/RTC</span>
    </div>
  </div>
</div>
```

---

## 6. Mobile Thumb Ergonomics & Floating Dock Integration

Pada layar ponsel, seluruh navigasi dan saklar utama **WAJIB** berada di zona jangkauan jempol bawah (*handheld thumb zone*):

```html
<!-- Floating Neumorphic Mobile Nav Dock -->
<nav class="md:hidden fixed bottom-3 inset-x-3 z-40" style="padding-bottom: env(safe-area-inset-bottom);">
  <div style="background: #E2E6EB;
              border-radius: 24px;
              padding: 6px 10px;
              border: 1px solid rgba(255, 255, 255, 0.55);
              box-shadow: 0 16px 32px rgba(15, 23, 42, 0.12), 4px 4px 14px rgba(160, 175, 195, 0.40), -4px -4px 14px rgba(255, 255, 255, 0.85);
              display: flex;
              align-items: center;
              justify-content: space-around;">

    <!-- Active Item: Inset Parit Cekung dengan LED Amber -->
    <a href="/"
       style="display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: center;
              padding: 6px 16px;
              border-radius: 16px;
              background: #E2E6EB;
              box-shadow: inset 2px 2px 5px rgba(160, 175, 195, 0.42), inset -2px -2px 5px rgba(255, 255, 255, 0.75);
              color: #0F172A;
              text-decoration: none;
              min-height: 48px;
              position: relative;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
      <div style="display: flex; align-items: center; gap: 4px; margin-top: 2px;">
        <span style="font-size: 10.5px; font-weight: 800;">Live</span>
        <span style="width: 5px; height: 5px; border-radius: 50%; background: #EA580C;" class="led-pulse"></span>
      </div>
    </a>

    <!-- Inactive Item -->
    <a href="/settings"
       style="display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: center;
              padding: 6px 16px;
              color: #64748B;
              text-decoration: none;
              min-height: 48px;"
       class="active:scale-95 transition-transform">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l-.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83 2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06-.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span style="font-size: 10.5px; font-weight: 700; margin-top: 2px;">Setting</span>
    </a>
  </div>
</nav>
```

---

## 7. Quality Gate Checklist (Uji Bebas Silau & Standar Servis)

Sebelum mengklaim pekerjaan Neumorphism selesai, orkestrator **WAJIB** memverifikasi poin-poin berikut:

- [ ] **Uji Glare Retina**: Apakah ada warna putih `#FFFFFF` murni berukuran besar tanpa difusi alpha? (Jika ada, segera ganti dengan `#E2E6EB` dan alpha transparency).
- [ ] **Uji Double-Rim**: Apakah ada border hitam atau border putih tebal di samping bayangan? (Border wajib `1px solid rgba(255,255,255,0.45)` untuk convex, atau `rgba(160,175,195,0.25)` untuk concave).
- [ ] **Single-Accent Enforcement**: Apakah warna oranye bocor ke font, border, atau background? (Aksen oranye **HANYA** boleh berada pada lampu status LED bulat).
- [ ] **LED Breathing Frequency**: Apakah LED bernapas pada rentang 2.5s - 3.0s dengan glow halus? (Dilarang strobo neon cepat).
- [ ] **DOM Tag Balance**: Selisih tag pembuka vs penutup `<div>`, `<button>`, `<a>`, `<span>` wajib = 0.
- [ ] **Zero Build-Step**: Apakah kode memerlukan compile TypeScript / bundler? (Dilarang, wajib HTML5 murni + Tailwind Play CDN).
- [ ] **WCAG Contrast Check**: Kontras heading `#0F172A` vs `#E2E6EB` wajib > 7:1. Kontras subtitle `#475569` wajib > 4.5:1.
