<div align="center">

# ZERO-BLOAT-SKILLS

**21 Circuit-Level Operational Skills for Hardware Technicians, Bare-Metal Linux, and Multi-Agent AI Gateways**

[![Live Web Showcase](https://img.shields.io/badge/Live%20Portal-skill.megapass.web.id-0071E3?style=flat-square&logo=googlechrome&logoColor=white)](https://skill.megapass.web.id)
[![Laboratory](https://img.shields.io/badge/Workbench-Megapass%20Intra%20Solusindo-0284c7?style=flat-square)](https://megapass.web.id)
[![Certification](https://img.shields.io/badge/BNSP%20Certified-Electronics%20Technician-10b981?style=flat-square)](https://github.com/4ntiDandruff)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Bloat%20%7C%20%3C50MB%20RAM-f59e0b?style=flat-square)](https://github.com/4ntiDandruff/zero-bloat-skills)
[![License](https://img.shields.io/badge/License-MIT-6366f1?style=flat-square)](LICENSE)

<br/>

[![Antigravity](https://img.shields.io/badge/Antigravity%20CLI-Compatible-34D399?style=flat-square)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-D97706?style=flat-square)](#)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-60A5FA?style=flat-square)](#)
[![Hermes](https://img.shields.io/badge/Hermes%20Agent-Compatible-A78BFA?style=flat-square)](#)
[![OMP](https://img.shields.io/badge/Oh%20My%20Pi-Compatible-EC4899?style=flat-square)](#)
[![Codex](https://img.shields.io/badge/Codex%20CLI-Compatible-64748B?style=flat-square)](#)

<br/>

[English](README.md) &bull; [Bahasa Indonesia](README.id.md) &bull; [Live Interactive Portal](https://skill.megapass.web.id)

<br/>

<a href="https://skill.megapass.web.id">
  <img src="assets/hero.png" alt="Zero-Bloat Skills Interactive Web Portal" width="100%" />
</a>

</div>

---

This skill suite was not conceived inside high-end cloud instances. It was engineered, tested, and proven directly on an aging Intel Core i3 bench machine (7.6GB RAM) inside the **Megapass Intra Solusindo** hardware repair workshop in Sidoarjo, Indonesia.

Designed to operate board-level motherboard diagnostics, SPI EEPROM flashing, zero-transcode edge media streaming, and multi-node service routing without memory leaks, background polling overhead, or runtime `node_modules` bloat.

Fully compatible with **Google Antigravity CLI**, **Claude Code**, **Oh My Pi (OMP)**, **OpenCode**, **Hermes Agent**, and **Codex CLI**.

---

## ⚡ 1-Line Universal Remote Install

Deploy and symlink all 21 skills across every installed coding agent on your system with a single command:

```bash
curl -sSL https://skill.megapass.web.id/install.sh | bash
```

Or clone manually and run the local installer:

```bash
git clone https://github.com/4ntiDandruff/zero-bloat-skills.git
cd zero-bloat-skills && chmod +x install.sh && ./install.sh
```

To update all skills anytime:

```bash
./install.sh --update
```

---

## 🌐 Live Interactive Portal & Playground

Explore the entire suite live on the web at **[skill.megapass.web.id](https://skill.megapass.web.id)**:

* **Live Laboratory: Token-Frugal AI Ladder**: Test real-time spoken amount parsing in English (USD) and Indonesian (IDR) with sub-millisecond response times and **0 LLM API calls, 0 tokens burned**.
* **Browser-Native Web Speech STT**: Hands-free voice recognition directly from your browser microphone with automatic language detection.
* **Full Specification Viewer**: Inspect comprehensive SOP markdown documentation for all 21 skills through an in-browser slide-over drawer with one-click path and code copying.

<p align="center">
  <a href="https://skill.megapass.web.id">
    <img src="assets/playground.png" alt="Live Laboratory: Token-Frugal AI Ladder" width="100%" />
  </a>
</p>

---

## 1. Circuit Topology

```
  [ HARDWARE BENCH PHYSICAL INSTRUMENTS ]
  ├── Digital Multimeter & Bench Power Supply (1A Current Injection)
  ├── CH341A USB SPI Flash Programmer (24/25 Series SOIC8)
  └── Client Android Devices & Laptops Under Service
                    ↓
  [ WORKSTATION LINUX WORKBENCH (INTEL CORE I3-3240 / 7.6GB RAM) ]
  ├── Kernel Inotify Daemons (0.0% CPU Standby Load)
  ├── Faster-Whisper Local Streaming (Hands-Free Wayland HUD)
  ├── Linux Repair Tooling (Reset SAM Password, Offline Registry, ddrescue)
  └── Multi-Account Rotary Shield Gateway (Anti-429 Rate Limiter)
                    ↓
  [ LOCAL NETWORK & SECURE INGRESS ]
  ├── Cloudflare Tunnel (Public HTTPS Ingress Without Open ISP Ports)
  ├── Tailscale WireGuard Mesh (Private Point-to-Point Interconnect)
  └── Telegram Inline Bot (Wake-On-LAN Triggers & Resource Monitors)
                    ↓
  [ DATA STORAGE & LEAN WEB INTERFACES ]
  ├── SQLite WAL Fortress (Resilient Against Sudden Power Outages)
  └── Single-Worker FastAPI + HTMX + Alpine (Total Footprint <50MB RAM)
```

---

## 2. Complete 21-Skill Production Matrix

<p align="center">
  <a href="https://skill.megapass.web.id#catalog">
    <img src="assets/catalog.png" alt="Production Skills Catalog" width="100%" />
  </a>
</p>

### Hardware & Diagnostics (3 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`hardware-boardview-skill`](skills/hardware-boardview-skill/SKILL.md) | Short circuit detection, safe 1A current injection, power rails sequencing (19V VIN, 3.3V/5V ALW, S3/S0), boardview analysis. | `motherboard`, `korslet`, `short`, `suntik tegangan`, `skema rails` |
| [`eeprom-flashing-skill`](skills/eeprom-flashing-skill/SKILL.md) | SPI BIOS/EEPROM (24/25 series) read/verification/flashing using CH341A and flashrom, Intel ME Region cleanup. | `flash bios`, `eeprom`, `ch341a`, `dump corrupt`, `clean me` |
| [`windows-repair-from-linux-skill`](skills/windows-repair-from-linux-skill/SKILL.md) | Offline SAM password reset via chntpw, registry hive repair, BCD bootloader recovery, ddrescue bad-sector imaging. | `servis windows`, `reset password`, `sam`, `bcd boot`, `bad sector` |

### Linux Bare-Metal & Daemons (5 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`zero-cpu-daemon-skill`](skills/zero-cpu-daemon-skill/SKILL.md) | Event-driven Linux daemons with 0.0% standby CPU load via inotifywait, fortified with 9 physical circuit fuses. | `daemon inotify`, `pantau folder`, `0% cpu`, `sekring ekstraksi` |
| [`watchdog-resilience-skill`](skills/watchdog-resilience-skill/SKILL.md) | PM2/systemd restart loop recovery, AdGuard Home DNS negative-cache flusher, Cloudflare Tunnel watchdog. | `watchdog`, `resilience`, `dns lockout`, `pm2 restart loop` |
| [`mesh-and-tunnel-ops-skill`](skills/mesh-and-tunnel-ops-skill/SKILL.md) | Zero-port-forwarding Cloudflare Tunnel for secure public HTTPS ingress + Tailscale WireGuard subnet interconnects. | `cloudflare tunnel`, `tailscale`, `port forwarding`, `wireguard` |
| [`telegram-ops-control-skill`](skills/telegram-ops-control-skill/SKILL.md) | Interactive Telegram bot with inline keyboard buttons, Wake-on-LAN (WOL) remote triggers, resource alerting. | `bot telegram`, `tombol remote`, `wake on lan`, `bangunkan pc` |
| [`android-bench-debloat-skill`](skills/android-bench-debloat-skill/SKILL.md) | Non-root ADB package debloater, critical system package whitelist, batch OEM package cleanup (Samsung, Xiaomi, Oppo, Vivo). | `debloat android`, `hapus bloatware`, `hp lemot`, `adb` |

### Web Architecture & Cupertino UI (6 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`zero-bloat-web-stack-skill`](skills/zero-bloat-web-stack-skill/SKILL.md) | Ultra-lean SSR web stack: FastAPI + SQLite WAL + HTMX + Alpine.js + Tailwind CSS (<40MB RAM, cold-start <100ms). | `fastapi`, `endpoint`, `router`, `backend python`, `web lean` |
| [`liquid-apple-ui-skill`](skills/liquid-apple-ui-skill/SKILL.md) | Apple-inspired liquid dark UI design system: slate glassmorphism, glowing status pills, zero-flicker Alpine tabs. | `apple liquid ui`, `dark glass`, `status pill`, `desain agy router` |
| [`browser-pdf-canvas-skill`](skills/browser-pdf-canvas-skill/SKILL.md) | Virtualized PDF.js HTML5 canvas viewer: IntersectionObserver lazy rendering, elimination of ghost-scroll feedback loops. | `viewer pdf skema`, `canvas`, `scroll hantu`, `search part` |
| [`longform-reader-ux-skill`](skills/longform-reader-ux-skill/SKILL.md) | Technical reader UX: gradient scroll cue, dynamic reading progress bar, hover-to-copy code blocks, shimmer placeholders. | `artikel panjang`, `tata letak blog`, `reader ux`, `table scroll` |
| [`portfolio-timeline-lightbox-skill`](skills/portfolio-timeline-lightbox-skill/SKILL.md) | Milestone roadmap, collapsible phase nodes, zero-bloat touch-swipe lightbox with keyboard accessibility. | `roadmap karier`, `sertifikat`, `lightbox foto`, `galeri swipe` |
| [`print-shop-canvas-skill`](skills/print-shop-canvas-skill/SKILL.md) | Physical print layout generator via Python Pillow: 300 DPI rendering, cutting bleed margins, print-ready PDF export. | `desain cetak`, `kartu garansi`, `kalender`, `300 dpi`, `bleed` |

### AI Ladder & Edge Media (7 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`token-frugal-intent-ladder-skill`](skills/token-frugal-intent-ladder-skill/SKILL.md) | Deterministic transactional parser: 0-token regex ladder, active vs passive cashflow disambiguation, clean notes. | `tangga ai`, `parsing nominal`, `terbilang`, `hutang piutang` |
| [`ai-rotary-shield-skill`](skills/ai-rotary-shield-skill/SKILL.md) | Reverse proxy pool with multi-account rotation: automated HTTP 429 rate limit detection and instant cooldown failover. | `limit 429`, `kuota habis`, `resource exhausted`, `putar akun ai` |
| [`browser-speech-to-text-skill`](skills/browser-speech-to-text-skill/SKILL.md) | Zero-server-cost Web Speech STT: Android PWA microphone bridge, visualViewport soft-keyboard avoidance. | `suara ke teks browser`, `web speech stt`, `dikte web`, `mic pwa` |
| [`voice-hud-wayland-skill`](skills/voice-hud-wayland-skill/SKILL.md) | Hands-free technician voice HUD under Linux Wayland: local faster-whisper streaming and KWin glass overlay. | `dikte suara`, `hands-free`, `voice hud`, `wayland`, `solder` |
| [`privacy-analytics-waf-skill`](skills/privacy-analytics-waf-skill/SKILL.md) | Self-hosted zero-cookie web analytics on SQLite WAL + lightweight IP rate limiting WAF security fuse. | `analitik pengunjung lokal`, `waf sekring`, `brute force ip` |
| [`sqlite-wal-fortress-skill`](skills/sqlite-wal-fortress-skill/SKILL.md) | Outage-proof SQLite configuration: WAL mode, PRAGMA synchronous=NORMAL, auto-checkpoint tuning, atomic hot backups. | `database`, `sqlite`, `wal`, `corrupt`, `backup` |
| [`zero-transcode-media-skill`](skills/zero-transcode-media-skill/SKILL.md) | Edge CCTV streaming on constrained hardware (STBs/i3): RTSP to WebRTC/HLS pass-through via go2rtc (<30MB RAM). | `streaming cctv`, `stb edge`, `go2rtc`, `rtsp webrtc zero-transcode` |

<br/>

<p align="center">
  <a href="https://skill.megapass.web.id">
    <img src="assets/drawer.png" alt="In-Browser SOP Markdown Specification Reader" width="100%" />
  </a>
</p>

---

## 3. Beginner-Friendly Tech Stack Breakdown

* **Frontend (Display Layer)**:
  * **HTML5 (Structure)**: Server-Side Rendering (SSR) via Jinja2 for instant First Contentful Paint (<100ms) without blank-screen hydration lag.
  * **Tailwind CSS (Visuals)**: Standalone single-file bundle without Node.js build-step overhead on the server.
  * **Alpine.js & HTMX (Motion & Interaction)**: Direct partial DOM swaps over HTTP without writing custom client-side fetch logic.
  * **Lucide SVG (Icons)**: Pure inline SVG vectors. Zero external icon fonts or emoji artifacts.
* **Backend (Engine Layer)**:
  * **Python FastAPI / Flask**: High-throughput single-worker mode consuming <40MB RAM under active load.
  * **Rust & Tauri v2**: Native binary bindings directly to USB/serial hardware, eliminating Electron memory bloat.
* **Database (Persistence Layer)**:
  * **SQLite WAL Mode**: Write-Ahead Logging separating readers from writers concurrently, fortified against database corruption during sudden bench power cuts.

---

## 4. Real Metrics & Benchmarks

Empirical data recorded on the active Megapass workshop workbench server (Intel Core i3-3240 @ 3.40GHz, 7.6GB RAM, Ubuntu 24.04 LTS):

| Evaluation Metric | Conventional Industry Stack | Zero-Bloat Meja Servis | Real Efficiency Gain |
|---|---|---|---|
| Web App RAM Footprint | 450 MB - 1.2 GB (Node/React/Postgres) | 36 MB - 48 MB (FastAPI + SQLite WAL) | Up to 92% RAM reduction |
| Daemon Idle CPU Load | 3% - 8% (Polling loops with `sleep`) | 0.0% (Kernel `inotifywait` hook) | Zero idle CPU cycles |
| Edge CCTV Video Stream | 85% CPU load (FFmpeg re-encoding) | 0.8% CPU load (go2rtc RTP pass-through) | CPU runs cold on edge STBs |
| Sudden Outage Recovery | Corrupt journal / lock recovery required | 100% Intact (WAL commit + PRAGMA NORMAL) | Zero corrupt transactions |
| Cold-Start Latency | 3.5 - 8.0 seconds | < 120 milliseconds | Instant readiness |

---

## 5. Engineering Valuation

Cost and resource analysis comparing commercial software house deliverables against self-hosted `zero-bloat-skills` architecture:

| Infrastructure Need | Commercial Software House Path | Zero-Bloat Workbench Path | Real Savings Value |
|---|---|---|---|
| Monthly Cloud Hosting | 8GB RAM Cloud VPS + Managed DB: $45 / mo | Repurposed i3 Workshop PC + SQLite WAL: $0 | Saves $540 / year |
| Static Public IP Fee | Business ISP Static IP Addon: $18 / mo | Cloudflare Tunnel + Tailscale Subnet: $0 | Saves $216 / year |
| Custom Internal Tooling | Commercial desktop tooling contract: $1,200 | 21 Specialized modular skills: Included | Saves $1,200 one-time |
| Technician Triage Time | Manual probing without boardview copilot: ~90 min | Boardview copilot + current injection: ~15 min | Saves 75 min bench time / unit |

---

## 6. Repository Treeview

```
zero-bloat-skills/
├── LICENSE                               # Official MIT License (Hizam Nahari / Megapass)
├── README.md                             # Comprehensive global documentation
├── README.id.md                          # Indonesian language edition
├── install.sh                            # Universal multi-agent installer (auto-symlink)
├── uninstall.sh                          # Clean symlink removal script
│
├── assets/                               # High-resolution retina showcases & UI captures
│   ├── hero.png                          # Web portal hero showcase
│   ├── playground.png                    # Live Laboratory Token-Frugal AI Ladder
│   ├── catalog.png                       # 21-skill catalog card grid
│   └── drawer.png                        # Slide-over in-browser SOP reader
│
├── skills/                               # 21 Specialized Workbench & Systems Skills
│   ├── hardware-boardview-skill/         # Short-circuit diagnostics, 1A injection, rails tracing
│   ├── browser-pdf-canvas-skill/         # PDF.js Canvas, lazy virtualization, anti-ghost-scroll
│   ├── eeprom-flashing-skill/            # SPI flashrom 24/25 series via CH341A + Clean ME
│   ├── windows-repair-from-linux-skill/  # Reset SAM password, offline registry, ddrescue
│   ├── android-bench-debloat-skill/      # Non-root ADB debloater, vital package whitelist
│   ├── zero-cpu-daemon-skill/            # Inotifywait daemon 0% CPU with 9 physical fuses
│   ├── voice-hud-wayland-skill/          # Hands-free technician STT HUD via faster-whisper
│   ├── telegram-ops-control-skill/       # Inline remote control buttons & Wake-on-LAN (WOL)
│   ├── ai-rotary-shield-skill/           # Reverse proxy pool mitigating HTTP 429 rate limits
│   ├── watchdog-resilience-skill/        # Auto-heal PM2/systemd & AdGuard DNS cache flusher
│   ├── sqlite-wal-fortress-skill/        # SQLite WAL anti-power-outage & online hot-backup
│   ├── zero-transcode-media-skill/       # Edge CCTV streaming without CPU transcoding
│   ├── mesh-and-tunnel-ops-skill/        # Cloudflare Tunnel ingress + Tailscale private mesh
│   ├── zero-bloat-web-stack-skill/       # FastAPI + Alpine + HTMX + Tailwind (<40MB RAM)
│   ├── privacy-analytics-waf-skill/      # Zero-cookie visitor analytics + WAF rate limiter
│   ├── print-shop-canvas-skill/          # High-DPI Pillow canvas generator for physical print
│   ├── liquid-apple-ui-skill/            # Apple-style liquid dark UI, pill badges, Alpine tabs
│   ├── longform-reader-ux-skill/         # Table scroll cue, reading bar, copy-code, shimmer
│   ├── portfolio-timeline-lightbox-skill/# Milestone roadmap, collapsible phases, A11y lightbox
│   ├── browser-speech-to-text-skill/     # Zero-server Web Speech STT, PWA mic, spoken numbers
│   └── token-frugal-intent-ladder-skill/ # 0-token regex ladder, debt vs receivable, clean notes
│
└── examples/
    └── starter-app/                      # Complete runnable workbench ticketing demo
        ├── main.py                       # Single-worker FastAPI backend
        ├── db.py                         # SQLite WAL initialization & circuit pragmas
        ├── requirements.txt              # Minimal runtime dependencies
        ├── test_smoke.py                 # Self-contained verification test (exit code 0)
        └── templates/
            └── index.html                # SSR HTML + Tailwind + HTMX + Alpine UI
```

---

## 7. Smoke Test (1-Click Verification Guide)

Validate the stack independently on your local workstation:

```bash
# 1. Clone repository
git clone https://github.com/4ntiDandruff/zero-bloat-skills.git
cd zero-bloat-skills

# 2. Symlink skills across all installed coding agents
chmod +x install.sh
./install.sh

# 3. Execute automated starter app verification
cd examples/starter-app
python3 test_smoke.py
```

Expected terminal output:
```
[*] Menjalankan smoke test starter app...
[+] Test 1 PASS: /health aktif dan mode SQLite WAL terverifikasi.
[+] Test 2 PASS: GET / render HTML berhasil (FCP instant).
[+] Test 3 PASS: POST /tickets/add berhasil swap baris HTMX baru.
[+] Test 4 PASS: Data terverifikasi tersimpan atomik di SQLite WAL.

[+] SELURUH SMOKE TEST LOLOS DENGAN EXIT CODE 0.
```

---

## 8. Future Roadmap

* **Phase 1 (Current Release)**: Core 21-skill package, multi-agent symlink installer, live interactive web portal at `skill.megapass.web.id`, and workbench starter app.
* **Phase 2 (Upcoming)**: Automated zero-bloat reverse-proxy config generator for Caddy, Nginx, and Traefik.
* **Phase 3 (Long-Term)**: Standalone `zero-bloat` CLI binary in Rust for instant zero-dependency project scaffolding and hardware workbench probing.

---

<div align="center">

Megapass Intra Solusindo • Sidoarjo, Indonesia

</div>
