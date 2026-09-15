# Changelog

Semua perubahan penting pada proyek ZERO-BLOAT-SKILLS didokumentasikan di berkas ini.

Format berbasis [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
dan proyek ini mematuhi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2026-09-15

### Penambahan Modul Dark Modern Tech UI, Ekosistem 23 Skill & Ekspansi 207 Symlink Multi-Agent

#### 1. Modul Baru: Dark Modern Tech UI Skill (`skills/dark-modern-tech-ui-skill/`)
- **[ui]** **Desain Sistem Slate Dark Matrix**: Meracik standar desain mode gelap kelas industri berbasis Deep Slate (`ink: #0B1220`, `ink2: #111A2E`, `ink3: #1E293B`) dengan kontras teks tinggi (`paper: #F8FAFC`, rasio kontras 16.5:1 lolos uji AAA WCAG).
- **[ui]** **Frosted Dark Glassmorphism**: Formula kaca es gelap `.glass-nav` (`rgba(11, 18, 32, 0.72)` dipadu `backdrop-filter: blur(16px)` dan border tipis `rgba(255, 255, 255, 0.08)`).
- **[ui]** **Ambient Radial Cyan Glow**: Kanvas latar belakang berpedar halus (`.glow-bg`) yang mensimulasikan pencahayaan sirkuit presisi tanpa membebani GPU perangkat mobile.
- **[ui]** **Bento Grid Layanan & Matriks Masalah**: Tata letak kartu modular untuk katalog servis hardware dan diagnosa gejala kerusakan pelanggan (*Customer Pain Points Matrix*).
- **[ui]** **Pricing Tier Cards Bergaransi**: Tiga tingkat paket harga terstruktur (Paket Standar, Komplit, Rescue) dengan badge rekomendasi dan link WhatsApp otomatis.
- **[ui]** **Pola Teknisi Panggilan (Home Service)**: Badge visual jangkauan wilayah (Coverage Radius kecamatan) dan 4 langkah SOP pengerjaan di tempat pelanggan.
- **[ui]** **Floating Mobile Thumb Action Dock**: Tombol konversi mengambang di 35% zona bawah layar HP dengan target klik >44px ramah jangkauan jempol satu tangan.
- **[ui]** **Zero-Bloat Accordion FAQ**: Dropdown tanya-jawab murni transisi CSS `max-height` tanpa library eksternal, tersinkronisasi dengan Schema.org FAQPage JSON-LD.

#### 2. Infrastruktur & Universal Multi-Agent Symlink (`install.sh`)
- **[installer]** **Ekspansi 207 Symlink Aktif**: Skrip `install.sh` memperluas instalasi ke 9 platform AI coding: Google Antigravity CLI, Claude Code, OpenCode, Hermes Agent, Oh My Pi (OMP), dan Codex CLI.
- **[orchestrator]** **Pembaruan Direktif Universal (`AGENTS.md`)**: Menambahkan pemetaan pemicu auto-load R11 untuk frasa `dark modern tech`, `ui megapass`, `tema gelap`, `dark mode`, `slate glassmorphism`, dan `landing page servis`.

#### 3. Higienitas & Kepatuhan Standar Meja Servis
- **[audit]** **Zero Em Dash Compliance**: Verifikasi 0 pelanggaran karakter em dash pada seluruh modul baru.
- **[audit]** **Zero Unicode Emoji**: Eliminasi seluruh emoji di antarmuka diganti vektor inline Lucide SVG murni.
- **[audit]** **Keseimbangan Tag DOM**: 8 cuplikan kode HTML diuji dengan hasil 100% balanced (selisih tag = 0).

---

## [2.2.0] - 2026-09-13

### Pemisahan Rangka Tata Letak Ponsel (Universal Mobile Thumb Ergonomics)

#### 1. Modul Baru: Mobile Thumb Ergonomics Skill (`skills/mobile-thumb-ergonomics-skill/`)
- **[mobile]** **Fisika Viewport Dinamis (`100dvh`)**: Mengatasi masalah dynamic address bar browser mobile Android/iOS yang menutupi bagian bawah layar.
- **[mobile]** **Geometri Natural Thumb Zone**: Menetapkan aturan penempatan tombol aksi di area 35% bawah layar HP dan melarang penempatan tombol utama di sudut kanan atas.
- **[mobile]** **Bottom Sheet Drawer & Keypad Well**: Pola laci geser bawah dengan transisi transform CSS murni dan penghindaran keyboard virtual visualViewport.
- **[mobile]** **Pemisahan Peran Arsitektur**: Memisahkan rangka tata letak jempol (*skeleton*) dari tema gaya visual (*skin*).

---

## [2.1.0] - 2026-09-10

### Peningkatan Liquid Apple UI ke Versi 2.0 (Cupertino Crystal Glass)

#### 1. Modul: Liquid Apple UI Skill v2.0 (`skills/liquid-apple-ui-skill/`)
- **[ui]** **Ambient Iridescent Mesh Canvas**: Kanvas 5 titik gradien radial platinum (`#F5F5F7`).
- **[ui]** **Harmonisasi Glassmorphism & Neumorphism**: Penggabungan kartu kaca buram (`.crystal-card` blur 32px) dengan alur sunken neumorphism (`.neo-groove` dan `.neo-tab-active`).
- **[ui]** **Kurva Respon Taktil Pegas**: Haptik klik Cupertino dengan kurva `cubic-bezier(0.16, 1, 0.3, 1)`.

---

## [2.0.0] - 2026-09-09

### Universal Symlink Installer & Otomasi Gateway Multi-Akun

#### 1. Ekosistem Tooling & Gateway
- **[tooling]** **Universal Symlink Installer (`install.sh`)**: Arsitektur tautan simetris satu baris perintah untuk 9 platform AI tanpa duplikasi penyimpanan.
- **[ai-shield]** **Rotary Shield Gateway (`ai-rotary-shield-skill`)**: Deteksi HTTP 429 otomatis dan rotasi multi-akun AI dengan pass-through streaming SSE tanpa buffer.
- **[audio]** **Browser-Native Web Speech STT (`browser-speech-to-text-skill`)**: Dikte suara lokal peramban tanpa biaya server.
- **[nlp]** **Token-Frugal AI Ladder (`token-frugal-intent-ladder-skill`)**: Parsing nominal terbilang dan pencatatan transaksi keuangan tanpa memanggil API LLM (0 token).

---

## [1.0.0] - 2026-08-15

### Rilis Awal: 21 Modul Spesialis Meja Servis & Linux Bare-Metal

#### 1. Koleksi 21 Modul Awal
- **[hardware]** `hardware-boardview-skill`: Suntik tegangan 1A, pencegahan tembus MOSFET high-side, dan pembacaan skema rail S5-S0.
- **[eeprom]** `eeprom-flashing-skill`: Pemrograman SPI flash 24/25 series via CH341A dengan adaptor 1.8V dan pembersihan Intel ME Region.
- **[windows]** `windows-repair-from-linux-skill`: Reset password SAM offline, rekonstruksi BCD bootloader, dan pencadangan bad-sector ddrescue.
- **[daemon]** `zero-cpu-daemon-skill`: Daemon inotifywait event-driven dengan 0% CPU standby dan 9 sekring sirkuit.
- **[resilience]** `watchdog-resilience-skill`: Auto-heal restart loop PM2 dan flusher DNS cache AdGuard Home.
- **[remote]** `telegram-ops-control-skill`: Saklar inline keyboard bot Telegram dan pemicu Wake-on-LAN (WOL).
- **[debloat]** `android-bench-debloat-skill`: Debloater ADB non-root dengan whitelist paket vital sistem.
- **[database]** `sqlite-wal-fortress-skill`: Fortifikasi SQLite WAL anti padam listrik mendadak dan cadangan panas atomik online.
- **[media]** `zero-transcode-media-skill`: Streaming CCTV RTSP ke WebRTC tanpa CPU transcoding via go2rtc.
- **[network]** `mesh-and-tunnel-ops-skill`: Jaringan publik aman Cloudflare Tunnel dan privat Tailscale WireGuard mesh.
- **[web]** `zero-bloat-web-stack-skill`: Arsitektur FastAPI + SQLite WAL + HTMX + Alpine.js + Tailwind (<40MB RAM).
- **[analytics]** `privacy-analytics-waf-skill`: Analitik web mandiri tanpa cookie dan pembatas laju WAF memori bounded.
- **[print]** `print-shop-canvas-skill`: Generator grafis layout percetakan fisik 300 DPI dengan margin bleed pisau potong.
- **[canvas]** `browser-pdf-canvas-skill`: Penampil PDF.js HTML5 canvas dengan virtualisasi lazy rendering.
- **[reader]** `longform-reader-ux-skill`: Tata letak membaca artikel teknis dengan indikator baca dan hover copy kode.
- **[portfolio]** `portfolio-timeline-lightbox-skill`: Peta jalan karir teknisi dan penampil lightbox gambar aksesibel.
- **[voice]** `voice-hud-wayland-skill`: HUD dikte suara hands-free teknisi di Linux Wayland via faster-whisper.
