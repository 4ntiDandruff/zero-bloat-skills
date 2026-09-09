<div align="center">

# ZERO-BLOAT-SKILLS

**17 Modul Keahlian Operasional Tingkat Sirkuit Meja Servis, Linux Bare-Metal, dan Multi-Agent AI Gateway**

[![Hardware Lab](https://img.shields.io/badge/Laboratory-Megapass%20Intra%20Solusindo-0284c7?style=flat-square)](https://megapass.web.id)
[![Certification](https://img.shields.io/badge/BNSP%20Certified-Electronics%20Technician-10b981?style=flat-square)](https://github.com/4ntiDandruff)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Bloat%20%7C%20%3C50MB%20RAM-f59e0b?style=flat-square)](https://github.com/4ntiDandruff/zero-bloat-skills)
[![License](https://img.shields.io/badge/License-MIT-6366f1?style=flat-square)](LICENSE)

</div>

---

Koleksi skill ini tidak dirancang di atas server cloud berbayar mahal, melainkan ditempa dan diuji langsung di meja servis **Megapass Intra Solusindo (Sidoarjo, Indonesia)** di atas mesin Intel Core i3 lawas (RAM 7.6GB) untuk menangani diagnosa motherboard, flashing EEPROM, streaming CCTV edge, dan operasional harian ruko tanpa toleransi crash, kebocoran memori, atau dependensi node_modules yang membengkak.

Dapat dipasang dan dimuat secara otomatis oleh **Claude Code**, **Google Antigravity CLI**, **Oh My Pi (OMP)**, **OpenCode**, **Hermes Agent**, dan **Codex CLI**.

---

## 1. Topologi Sirkuit

```
  [ PERALATAN FISIK MEJA SERVIS ]
  ├── Multimeter & Lab Bench Power Supply (Injeksi Arus 1A)
  ├── CH341A USB SPI Flash Programmer (24/25 Series SOIC8)
  └── Ponsel Android & Laptop Servis Konsumen
                    ↓
  [ WORKSTATION LINUX MEJASERVIS (PC MICHAEL / I3-3240) ]
  ├── Kernel Inotify Daemons (0% CPU Standby Load)
  ├── Faster-Whisper Local Streaming (Wayland HUD Hands-Free)
  ├── Linux Repair Tooling (Reset SAM Password, Offline Registry, ddrescue)
  └── Multi-Account Rotary Shield Gateway (Anti-Limit HTTP 429)
                    ↓
  [ JARINGAN RUKO & AKSES JARAK JAUH ]
  ├── Cloudflare Tunnel (Ingress Publik HTTPS Tanpa Buka Port ISP)
  ├── Tailscale WireGuard Mesh (Interkoneksi Privat Antar Node)
  └── Telegram Inline Bot (Saklar Wake-On-LAN & Pemantau Beban Sistem)
                    ↓
  [ PENYIMPANAN DATA & WEB LEAN ]
  ├── SQLite WAL Fortress (Kebal Pemadaman Listrik Mendadak)
  └── Single-Worker FastAPI + HTMX + Alpine (Total RAM <50MB)
```

---

## 2. Bedah Tech Stack Ramah Pemula

* **Frontend (Layar Depan)**:
  * **HTML5 (Kerangka)**: Server-Side Rendering (SSR) via Jinja2 untuk kecepatan tampil awal instan tanpa blank screen.
  * **Tailwind CSS (Tampilan)**: Standalone micro-bundle tanpa build-step Node.js yang membebani disk.
  * **Alpine.js & HTMX (Gerakan & Interaksi)**: Pertukaran data AJAX parsial langsung dari server tanpa menulis fetch API manual.
  * **Lucide SVG (Simbol)**: Ikon vektor inline murni tanpa icon-font berat atau emoji murahan.
* **Backend (Mesin Belakang)**:
  * **Python FastAPI / Flask**: Mode single-worker berkinerja tinggi, menghemat memori hingga <40MB RAM.
  * **Rust & Tauri v2**: Binding native biner ke hardware USB/serial tanpa runtime Electron.
* **Database (Penyimpanan Data)**:
  * **SQLite WAL Mode**: Arsitektur Write-Ahead Logging yang memisahkan arus baca dan tulis secara konkuren, dilengkapi proteksi integritas penuh saat arus listrik terputus mendadak.

---

## 3. Metrik & Benchmark Nyata

Data riil hasil pengujian pada server produksi meja servis Megapass (Intel Core i3-3240, RAM 7.6GB, Ubuntu 24.04 LTS):

| Indikator Evaluasi | Stack Standar Industri | Zero-Bloat Meja Servis | Efisiensi Riil |
|---|---|---|---|
| Konsumsi RAM Web App | 450 MB - 1.2 GB (Node/React/Postgres) | 36 MB - 48 MB (FastAPI + SQLite WAL) | Penghematan RAM hingga 92% |
| CPU Standby Load Daemon | 3% - 8% (Polling Loop `sleep`) | 0.0% (Kernel `inotifywait` event hook) | Nol beban prosesor di standby |
| Transcoding CCTV Edge | 85% CPU load (FFmpeg re-encoding) | 0.8% CPU load (go2rtc RTP pass-through) | CPU tetap dingin di edge STB |
| Ketahanan Mati Lampu | Risiko database locking / malformed | Aman 100% (WAL commit + PRAGMA NORMAL) | Zero corrupt transaction |
| Cold-Start Time | 3.5 - 8.0 detik | < 120 milidetik | Respons instan saat dipanggil |

---

## 4. Valuasi Rekayasa

Tabel perbandingan nilai rekayasa antara menggunakan jasa vendor/software house konvensional vs penerapan mandiri arsitektur `zero-bloat-skills`:

| Pos Kebutuhan Sistem | Metode Vendor / Software House | Metode Mandiri Zero-Bloat | Nilai Penghematan Riil |
|---|---|---|---|
| Server & Database Bulanan | Sewa VPS Cloud 8GB RAM + Managed DB: Rp 650.000 / bulan | PC Bekas Ruko (i3/STB) + SQLite WAL: Rp 0 (Lokal) | Hemat Rp 7.800.000 / tahun |
| Lisensi & Domain IP Publik | Sewa IP Publik Statis ISP: Rp 250.000 / bulan | Cloudflare Tunnel + Tailscale Subnet: Rp 0 | Hemat Rp 3.000.000 / tahun |
| Biaya Jasa Bikin Tool Servis | Pembuatan software desktop internal: Rp 15.000.000 | Ekstraksi 21 modul skill siap pakai: Gratis | Hemat Rp 15.000.000 (One-time) |
| Waktu Diagnosa Teknisi | Pelacakan manual tanpa AI/skema: ~90 menit/unit | Copilot boardview + injeksi arus: ~15 menit/unit | Menghemat 75 menit waktu kerja/unit |

---

## 5. Treeview Repositori

```
zero-bloat-skills/
├── LICENSE                               # Lisensi resmi MIT (Hizam Nahari / Megapass)
├── README.md                             # Dokumentasi komprehensif standar R8
├── install.sh                            # Installer universal multi-agent (symlink otomatis)
├── uninstall.sh                          # Skrip pencabutan symlink bersih
│
├── skills/                               # 21 Modul Keahlian Meja Servis & Zero-Bloat
│   ├── hardware-boardview-skill/         # Diagnosa short circuit, injeksi 1A, urutan rails
│   ├── browser-pdf-canvas-skill/         # PDF.js Canvas, lazy observer, anti-ghost-scroll
│   ├── eeprom-flashing-skill/            # SPI flashrom 24/25 series via CH341A + Clean ME
│   ├── windows-repair-from-linux-skill/  # Reset password SAM chntpw, offline registry, ddrescue
│   ├── android-bench-debloat-skill/      # ADB debloater tanpa root, whitelist modul aman
│   ├── zero-cpu-daemon-skill/            # Inotifywait daemon 0% CPU + 9 sekring sirkuit
│   ├── voice-hud-wayland-skill/          # Hands-free STT HUD teknisi via faster-whisper
│   ├── telegram-ops-control-skill/       # Inline buttons remote server & Wake-on-LAN (WOL)
│   ├── ai-rotary-shield-skill/           # Reverse proxy pool anti-limit HTTP 429
│   ├── watchdog-resilience-skill/        # Auto-heal PM2/systemd & pemulih DNS cache AdGuard
│   ├── sqlite-wal-fortress-skill/        # SQLite WAL anti-mati lampu + hot-backup atomik
│   ├── zero-transcode-media-skill/       # CCTV stream STB edge tanpa beban transcoding CPU
│   ├── mesh-and-tunnel-ops-skill/        # Cloudflare Tunnel publik + Tailscale privat mesh
│   ├── zero-bloat-web-stack-skill/       # FastAPI + Alpine + HTMX + Tailwind (RAM <40MB)
│   ├── privacy-analytics-waf-skill/      # Zero-cookie visitor analytics + WAF rate limiter
│   ├── print-shop-canvas-skill/          # Generator grafis dinamis Pillow/PIL presisi cetak
│   ├── liquid-apple-ui-skill/            # UI web ala Apple liquid dark mode, pill status & transisi
│   ├── longform-reader-ux-skill/         # Table scroll hint, progress bar, copy code, shimmer
│   ├── portfolio-timeline-lightbox-skill/# Milestone roadmap, collapsible phase, lightbox A11y
│   ├── browser-speech-to-text-skill/     # STT Web Speech browser, PWA mic bridge, terbilang
│   └── token-frugal-intent-ladder-skill/ # Tangga AI 0-token, semantik hutang/piutang, clean note
│
└── examples/
    └── starter-app/                      # Aplikasi percontohan meja servis siap jalan
        ├── main.py                       # Backend FastAPI single-worker
        ├── db.py                         # Inisialisasi SQLite WAL & pragma sirkuit
        ├── requirements.txt              # Minimal dependencies
        ├── test_smoke.py                 # Skrip verifikasi mandiri (exit code 0)
        └── templates/
            └── index.html                # Layar depan Jinja2 + Tailwind + HTMX + Alpine
```

---

## 6. Smoke Test (Panduan Verifikasi 1-Klik)

Untuk membuktikan keandalan stack secara mandiri di komputer Anda:

```bash
# 1. Clone repositori
git clone https://github.com/4ntiDandruff/zero-bloat-skills.git
cd zero-bloat-skills

# 2. Pasang skill ke seluruh coding agent yang terinstall
chmod +x install.sh
./install.sh

# 3. Jalankan pengujian otomatis aplikasi percontohan
cd examples/starter-app
python3 test_smoke.py
```

Output terminal terverifikasi:
```
[*] Menjalankan smoke test starter app...
[+] Test 1 PASS: /health aktif dan mode SQLite WAL terverifikasi.
[+] Test 2 PASS: GET / render HTML berhasil (FCP instant).
[+] Test 3 PASS: POST /tickets/add berhasil swap baris HTMX baru.
[+] Test 4 PASS: Data terverifikasi tersimpan atomik di SQLite WAL.

[+] SELURUH SMOKE TEST LOLOS DENGAN EXIT CODE 0.
```

### Cara Memperbarui Skill (Updating)

Karena instalasi menggunakan symlink atomik, menarik pembaruan terbaru akan seketika memperbarui seluruh coding agent tanpa perlu instalasi ulang:

```bash
# Pembaruan 1-perintah via installer
./install.sh --update

# Atau via git pull standar
git pull origin main
```

---

## 7. Potensi Pengembangan

* **Fase 1 (Rilis Saat Ini)**: Paket inti 16 skill, universal installer symlink, dan starter app meja servis.
* **Fase 2 (Berikutnya)**: Penambahan generator konfigurasi Nginx/Caddy zero-bloat satu baris perintah.
* **Fase 3 (Masa Depan)**: CLI terpadu `zero-bloat` untuk scaffolding aplikasi ruko berbasis Rust dan SQLite secara instan.

---

<div align="center">

Megapass Intra Solusindo • Sidoarjo, Indonesia

</div>
