# Changelog

Semua perubahan penting pada proyek ZERO-BLOAT-SKILLS didokumentasikan di berkas ini.

Format berbasis [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
dan proyek ini mematuhi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2026-09-16

### Added
- Tambah modul ke-24 `human-copywriting-id-skill` (`skills/human-copywriting-id-skill/`) memuat standar copywriting manusiawi meja servis, 4 Hukum Emas (Tes Warung Kopi, Rasio Anda vs Kami 3:1, Tes Sekarang Anda Bisa, First-Person CTA), formula konversi PAS & BAB, 7 putaran audit teks, dan 4 sekring pembalik risiko (Zero-Traps).
- Tambah 9 titik tautan symlink baru ke lingkungan runtime AI ruko, meningkatkan total distribusi aktif menjadi 216 symlink di 9 direktori coding agent.
- Tambah pemetaan direktif R11 di `AGENTS.md` untuk pemicu otomatis frasa copywriting manusiawi, bahasa awam, anti-robot, kata-kata enak, bikin kalimat, dan anti-ai slop.

### Changed
- Perbarui logika katalog pada `./install.sh --list` menjadi dinamis membaca total folder modul (`24 Modules`).
- Perbarui ambang batas verifikasi di `./install.sh --verify` dan `./test.sh` untuk memvalidasi penuh 24 skill dan 216 symlink.

### Fixed
- Pangkas dan eliminasi seluruh karakter em dash pada formula PAS dan BAB di `skills/human-copywriting-id-skill/SKILL.md` demi kepatuhan mutlak aturan zero em-dash R3.

---

## [2.3.1] - 2026-09-16

### Added
- Tambah skrip uji mandiri terpadu lokal `./test.sh` dengan 5 lapisan verifikasi otomatis (sintaks Bash, YAML frontmatter, audit CSS viewport, smoke test starter-app, dan OPSEC secret scan) dengan durasi eksekusi <1 detik.
- Tambah pipeline CI otomatis GitHub Actions (`.github/workflows/ci.yml`) berbasis Ubuntu runner dengan durasi eksekusi 16 detik.
- Tambah opsi CLI `--list`, `--verify`, dan `--test` pada skrip pengelola `install.sh`.

### Fixed
- Ganti deklarasi `overflow-x: hidden` pada `html, body` dengan `overflow-x: clip;` pada `body` di `mobile-thumb-ergonomics-skill` guna memotong kebocoran horizontal tanpa memicu konversi otomatis W3C yang mengunci scrollbar vertikal native browser.
- Cabut `overscroll-behavior-y: contain` dari root `html, body` dan lokalisasikan penggunaannya hanya pada wadah laci internal (`.overscroll-contain`).
- Sinkronkan class `overflow-hidden` pada watcher Alpine.js di drawer Bottom Sheet dan Keypad agar tidak tersangkut permanen di `document.body`.
- Tambahkan target direktori `.agents/skills` dan `.config/omp/skills` ke dalam array `TARGET_DIRS` di `uninstall.sh` agar simetris 100% dengan `install.sh`.
- Selaraskan pragma `PRAGMA busy_timeout = 5000;` dan `PRAGMA foreign_keys = ON;` di `zero-bloat-web-stack-skill` dan `examples/starter-app/db.py` untuk mencegah galat lock contention saat beban transaksi tinggi.

---

## [2.3.0] - 2026-09-15

### Added
- Tambah modul ke-23 `dark-modern-tech-ui-skill` berbasis palet Deep Slate (`#0B1220`), frosted dark glassmorphism (blur 16px), aksen electric cyan, Bento grid modular, pricing matrix, dan zero-bloat FAQ accordion.
- Tambah 27 titik symlink baru, memperluas distribusi aktif dari 180 menjadi 207 titik di 9 direktori AI coding ruko.
- Tambah pemetaan pemicu auto-load R11 untuk kata kunci dark modern tech, ui megapass, tema gelap, dark mode, dan slate glassmorphism.

### Changed
- Perbarui dokumentasi dwibahasa `README.md` dan `README.id.md` untuk mencatat ekspansi 23 modul dan arsitektur slate glassmorphism.

---

## [2.2.0] - 2026-09-13

### Added
- Tambah modul ke-22 `mobile-thumb-ergonomics-skill` memisahkan arsitektur rangka jempol viewport ponsel (`100dvh`, bottom dock, clearance `pb-32`, target sentuh 44px) dari tema gaya visual.
- Tambah pola laci geser bawah Bottom Sheet dan Keypad drawer dengan transisi CSS murni serta penghindaran visualViewport soft-keyboard.

---

## [2.1.0] - 2026-09-10

### Changed
- Tingkatkan `liquid-apple-ui-skill` ke versi 2.0 dengan kanvas iridescent ambient mesh (`#F5F5F7`), kartu kaca kristal translusen (blur 32px), dan kurva taktil pegas `cubic-bezier(0.16, 1, 0.3, 1)`.
- Harmonisasi alur neumorphism sunken (`.neo-groove` dan `.neo-tab-active`) dengan glassmorphism Apple.

---

## [2.0.0] - 2026-09-09

### Added
- Tambah skrip universal installer multi-agent `install.sh` untuk symlink atomik otomatis ke seluruh agent coding AI.
- Tambah modul `ai-rotary-shield-skill` untuk mitigasi limit HTTP 429 via rotary multi-akun dan streaming SSE zero-buffer.
- Tambah modul `browser-speech-to-text-skill` untuk dikte suara peramban lokal tanpa biaya server via Web Speech API.
- Tambah modul `token-frugal-intent-ladder-skill` untuk parsing nominal terbilang dan pencatatan transaksi keuangan tanpa token LLM.

---

## [1.0.0] - 2026-08-15

### Added
- Rilis perdana 17 modul spesialis meja servis hardware:
  - `hardware-boardview-skill`: Suntik tegangan aman 1A dan pembacaan skema rail S5-S0.
  - `eeprom-flashing-skill`: Pemrograman SPI flash 24/25 series via CH341A dan Intel Clean ME.
  - `windows-repair-from-linux-skill`: Reset password SAM offline dan penyelamatan ddrescue.
  - `zero-cpu-daemon-skill`: Daemon inotifywait event-driven dengan 0.0% CPU standby.
  - `watchdog-resilience-skill`: Auto-heal restart loop PM2 dan pembersih DNS cache AdGuard.
  - `telegram-ops-control-skill`: Saklar inline keyboard bot Telegram dan pemicu Wake-on-LAN.
  - `android-bench-debloat-skill`: Debloater ADB non-root dengan whitelist sistem kritis.
  - `sqlite-wal-fortress-skill`: Konfigurasi SQLite WAL anti padam listrik dan hot-backup online.
  - `zero-transcode-media-skill`: Streaming CCTV RTSP ke WebRTC tanpa beban transkoding CPU.
  - `mesh-and-tunnel-ops-skill`: Ingress aman Cloudflare Tunnel dan mesh privat Tailscale WireGuard.
  - `zero-bloat-web-stack-skill`: Arsitektur FastAPI + SQLite WAL + HTMX + Alpine.js + Tailwind (<40MB RAM).
  - `privacy-analytics-waf-skill`: Analitik pengunjung zero-cookie dan WAF rate limiter bounded.
  - `print-shop-canvas-skill`: Generator grafis percetakan fisik 300 DPI dengan margin bleed pisau potong.
  - `browser-pdf-canvas-skill`: Penampil PDF.js HTML5 canvas dengan virtualisasi lazy rendering.
  - `longform-reader-ux-skill`: Tata letak membaca artikel teknis dengan indikator baca dan copy kode.
  - `portfolio-timeline-lightbox-skill`: Peta jalan karir teknisi dan lightbox gambar touch-swipe.
  - `voice-hud-wayland-skill`: HUD dikte suara hands-free teknisi di Linux Wayland via faster-whisper.
