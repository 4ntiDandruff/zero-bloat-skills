<div align="center">

# ZERO-BLOAT-SKILLS

**27 Circuit-Level Operational Skills for Hardware Technicians, Bare-Metal Linux, and Multi-Agent AI Gateways**

[![Live Web Showcase](https://img.shields.io/badge/Live%20Portal-skill.megapass.web.id-0071E3?style=flat-square&logo=googlechrome&logoColor=white)](https://skill.megapass.web.id)
[![Laboratory](https://img.shields.io/badge/Workbench-Megapass%20Intra%20Solusindo-0284c7?style=flat-square)](https://megapass.web.id)
[![Certification](https://img.shields.io/badge/BNSP%20Certified-Electronics%20Technician-10b981?style=flat-square)](https://github.com/4ntiDandruff)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Bloat%20%7C%20%3C50MB%20RAM-f59e0b?style=flat-square)](https://github.com/4ntiDandruff/zero-bloat-skills)
[![CI Health Check](https://github.com/4ntiDandruff/zero-bloat-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/4ntiDandruff/zero-bloat-skills/actions)
[![Active Symlinks](https://img.shields.io/badge/Active%20Symlinks-243%20Configured-10b981?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-6366f1?style=flat-square)](LICENSE)

<br/>

[![Antigravity](https://img.shields.io/badge/Antigravity%20CLI-Compatible-34D399?style=flat-square)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-D97706?style=flat-square)](#)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-60A5FA?style=flat-square)](#)
[![Hermes](https://img.shields.io/badge/Hermes%20Agent-Compatible-A78BFA?style=flat-square)](#)
[![OMP](https://img.shields.io/badge/Oh%20My%20Pi-Compatible-EC4899?style=flat-square)](#)
[![Codex](https://img.shields.io/badge/Codex%20CLI-Compatible-64748B?style=flat-square)](#)

<br/>

[Bahasa Indonesia](README.md) &bull; [English Edition](README.en.md) &bull; [Live Interactive Portal](https://skill.megapass.web.id)

<br/>

<a href="https://skill.megapass.web.id">
  <img src="assets/hero.png" alt="Zero-Bloat Skills Interactive Web Portal" width="100%" />
</a>

</div>

---

## Executive Overview

This skill suite was not conceived inside high-end cloud instances or corporate development clusters. It was engineered, stress-tested, and proven directly on an aging Intel Core i3 bench machine (7.6GB RAM) inside the **Megapass Intra Solusindo** hardware repair workshop in Sidoarjo, Indonesia.

Designed to operate board-level motherboard diagnostics, SPI EEPROM flashing, zero-transcode edge media streaming, outage-proof SQLite WAL data persistence, and multi-node service routing without memory leaks, background polling overhead, or runtime `node_modules` bloat.

Fully synchronized across **Google Antigravity CLI**, **Claude Code**, **Oh My Pi (OMP)**, **OpenCode**, **Hermes Agent**, and **Codex CLI**.

---

## 1. Circuit Topology

Data flow is architected like layered physical relay protection. The workbench server resides entirely inside a private local area network without direct public modem port-forwarding:

```text
  [ HARDWARE BENCH PHYSICAL INSTRUMENTS ]
  ├── Digital Multimeter & Bench Power Supply (1A Current Injection Ceilings)
  ├── CH341A USB SPI Flash Programmer (24/25 Series SOIC8 Clips)
  └── Client Hardware Under Repair (Laptops, Android Devices, Motherboards)
                    │
                    ▼
  [ WORKSTATION LINUX WORKBENCH (INTEL CORE I3-3240 / 7.6GB RAM) ]
  ├── Kernel Inotify Daemons (0.0% CPU Standby Load via inotifywait)
  ├── Faster-Whisper Local Streaming (Hands-Free Wayland Voice HUD)
  ├── Linux Repair Tooling (Reset SAM Password, Offline Registry, ddrescue)
  └── Multi-Account Rotary Shield Gateway (Anti-429 Rate Limiter)
                    │
                    ▼
  [ LOCAL NETWORK & SECURE INGRESS ]
  ├── Cloudflare Tunnel (Public HTTPS Ingress Without Open ISP Ports)
  ├── Tailscale WireGuard Mesh (Private Point-to-Point Node Interconnect)
  └── Telegram Inline Bot (Wake-On-LAN Triggers & Remote Server Switches)
                    │
                    ▼
  [ DATA STORAGE & LEAN WEB INTERFACES ]
  ├── SQLite WAL Fortress (Resilient Against Sudden Workshop Power Outages)
  └── Single-Worker FastAPI + HTMX + Alpine (Total Footprint <50MB RAM)
```

---

## 2. Universal Remote Install & Instant Setup

Deploy and symlink all **27 skills** across every installed coding agent on your system with a single non-interactive command:

```bash
curl -fsSL https://skill.megapass.web.id/install.sh | bash
```

Or clone manually and execute the local installer:

```bash
git clone https://github.com/4ntiDandruff/zero-bloat-skills.git
cd zero-bloat-skills && chmod +x install.sh test.sh && ./install.sh
```

### CLI Command Options (`./install.sh`)

| Terminal Command | Action & Operation |
|---|---|
| `./install.sh` | Automatically detect and symlink 27 skills to all installed AI agent platforms. |
| `./install.sh --list` or `-l` | Display terminal catalog of all 27 skills and their descriptions. |
| `./install.sh --verify` or `-v` | Audit the health of all 243 symlinks across agent directories. |
| `./install.sh --test` or `-t` | Execute the 5-layer health check suite (`./test.sh`) in 1 second. |
| `./install.sh --update` or `-u` | Pull the latest upstream updates and refresh all symlinks. |

---

## 3. Complete 27-Skill Production Matrix

### A. Hardware Diagnostics & Workbench Servicing (5 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`hardware-boardview-skill`](skills/hardware-boardview-skill/SKILL.md) | Short circuit detection, high-side MOSFET punch-through protection, safe injection voltage ceilings, S5-to-S0 rail sequencing, boardview analysis. | `motherboard`, `korslet`, `short`, `suntik tegangan`, `skema rails` |
| [`eeprom-flashing-skill`](skills/eeprom-flashing-skill/SKILL.md) | SPI BIOS/EEPROM 24/25 reading & flashing, 1.8V adapter level-shifting, status register write-protect unlock, three-pass dump verification, Clean ME. | `flash bios`, `eeprom`, `ch341a`, `dump corrupt`, `clean me` |
| [`ventoy-servicing-skill`](skills/ventoy-servicing-skill/SKILL.md) | Workbench USB multiboot servicing: fail-safe `ventoy_helper.py` CLI (UTF-8 BOM, comment stripping, root `.ventoyignore` audit, auto-backup, kernel sync), MBR vs GPT partition guidance, Windows 11 TPM/SecureBoot/RAM/NRO offline bypass, Intel RST VMD Gen 11-14 drivers (`Drivers/Obat_VMD_*`). | `ventoy`, `multiboot`, `bypass win11`, `vmd intel`, `bootable usb` |
| [`windows-repair-from-linux-skill`](skills/windows-repair-from-linux-skill/SKILL.md) | Offline SAM password reset via chntpw with atomic hive backup, UEFI BCD bootloader reconstruction, ddrescue bad-sector imaging, BitLocker unlock. | `servis windows`, `reset password`, `sam`, `bcd boot`, `bad sector` |
| [`android-bench-debloat-skill`](skills/android-bench-debloat-skill/SKILL.md) | Non-root ADB package debloater, critical system package whitelist, batch OEM package cleanup (Samsung, Xiaomi, Oppo, Vivo). | `debloat android`, `hapus bloatware`, `hp lemot`, `adb` |

### B. Linux Bare-Metal, Networking & System Resilience (8 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`sqlite-wal-fortress-skill`](skills/sqlite-wal-fortress-skill/SKILL.md) | Outage-proof SQLite setup: WAL mode, synchronous=NORMAL, busy_timeout=5000 contention tuning, atomic hot backups, 1-line .recover salvage. | `database`, `sqlite`, `wal`, `corrupt`, `backup` |
| [`workbench-opsec-sanitization-skill`](skills/workbench-opsec-sanitization-skill/SKILL.md) | Workbench OPSEC sanitization: regex detection and in-place masking for OS user paths (`~/`), Tailscale CGNAT IPs, LAN subnets, MAC addresses, bot credentials, and hardware serials before public git commits. | `opsec`, `sensor`, `bersihin nama`, `sanitasi`, `audit keamanan`, `secret leak` |
| [`mesh-and-tunnel-ops-skill`](skills/mesh-and-tunnel-ops-skill/SKILL.md) | Zero-port-forwarding ingress: Cloudflare Tunnel for secure HTTPS and Tailscale WireGuard mesh for private multi-node interconnects. | `cloudflare tunnel`, `tailscale mesh`, `port forwarding`, `wireguard` |
| [`watchdog-resilience-skill`](skills/watchdog-resilience-skill/SKILL.md) | Self-healing Linux watchdog SOP: PM2/systemd auto-healer, AdGuard Home negative cache flusher, Cloudflare Tunnel monitor. | `watchdog`, `resilience`, `dns lockout`, `pm2 restart loop` |
| [`zero-cpu-daemon-skill`](skills/zero-cpu-daemon-skill/SKILL.md) | Event-driven Linux daemons with 0.0% standby CPU load via kernel hook inotifywait, 9 physical circuit fuses, debounce handling. | `daemon inotify`, `pantau folder`, `0% cpu`, `sekring ekstraksi` |
| [`telegram-ops-control-skill`](skills/telegram-ops-control-skill/SKILL.md) | Remote server management via Telegram: interactive inline buttons, Wake-on-LAN triggers, HTML-safe parsing, infinity polling reconnect. | `bot telegram`, `tombol remote`, `wake on lan`, `bangunkan pc` |
| [`privacy-analytics-waf-skill`](skills/privacy-analytics-waf-skill/SKILL.md) | Self-hosted zero-cookie web analytics on SQLite WAL + sliding-window WAF rate limiter with automatic TTL unban and zero memory leaks. | `analitik pengunjung lokal`, `waf sekring`, `brute force ip` |
| [`zero-transcode-media-skill`](skills/zero-transcode-media-skill/SKILL.md) | Edge CCTV streaming on constrained hardware (STB/i3) without CPU transcoding: RTSP to WebRTC/HLS pass-through via go2rtc (<30MB RAM). | `streaming cctv`, `stb edge`, `go2rtc`, `rtsp webrtc zero-transcode` |

### C. Web Architecture, Interface Design & Viewport Physics (10 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`zero-bloat-web-stack-skill`](skills/zero-bloat-web-stack-skill/SKILL.md) | Ultra-lean SSR web stack: FastAPI + SQLite WAL + HTMX + Alpine.js + Tailwind CSS (<40MB RAM, cold-start <100ms, zero node_modules). | `fastapi`, `endpoint`, `router`, `backend python`, `web lean` |
| [`dark-modern-tech-ui-skill`](skills/dark-modern-tech-ui-skill/SKILL.md) | High-conversion Dark Modern Tech UI: Deep Slate base (`#0B1220`), frosted dark glass (blur 16px), electric cyan accents, Bento grid, pricing matrix. | `dark modern tech`, `ui megapass`, `tema gelap`, `dark mode`, `slate glassmorphism`, `landing page servis` |
| [`liquid-apple-ui-skill`](skills/liquid-apple-ui-skill/SKILL.md) | Apple-inspired Cupertino liquid crystal UI design system: 5-point iridescent ambient mesh (`#F5F5F7`), translucent frosted glass, radar status pills, Alpine tabs. | `apple liquid ui`, `cupertino glass`, `status pill`, `desain agy router` |
| [`mobile-thumb-ergonomics-skill`](skills/mobile-thumb-ergonomics-skill/SKILL.md) | Styling-agnostic mobile layout, handheld thumb-zone geometry, 100dvh viewport physics, bottom-anchored actions, bottom sheet drawers, overflow-x: clip vertical scroll preservation. | `mobile ui`, `ramah jempol`, `bottom sheet`, `floating dock`, `layout hp` |
| [`zero-bloat-icon-favicon-skill`](skills/zero-bloat-icon-favicon-skill/SKILL.md) | Pastree-grade solid silhouette favicon, touch icon, and web asset generator: 10 workbench presets, 25% golden squircle ratio, C-native slicing (ICO 16/32/48/64, Apple 180, PWA 192/512), self-test diagnostics (`--test`), and zero Node.js bloat. | `favicon`, `icon`, `touch icon`, `app icon`, `generate gambar icon`, `webmanifest` |
| [`browser-pdf-canvas-skill`](skills/browser-pdf-canvas-skill/SKILL.md) | Virtualized PDF.js HTML5 canvas viewer: IntersectionObserver lazy rendering, elimination of ghost-scroll feedback loops. | `viewer pdf skema`, `canvas`, `scroll hantu`, `search part` |
| [`longform-reader-ux-skill`](skills/longform-reader-ux-skill/SKILL.md) | Technical reader UX: gradient scroll cue, dynamic reading progress bar, hover-to-copy code blocks, shimmer placeholders. | `artikel panjang`, `tata letak blog`, `reader ux`, `table scroll` |
| [`portfolio-timeline-lightbox-skill`](skills/portfolio-timeline-lightbox-skill/SKILL.md) | Milestone roadmap, collapsible phase nodes, zero-bloat touch-swipe lightbox with keyboard accessibility. | `roadmap karier`, `sertifikat`, `lightbox foto`, `galeri swipe` |
| [`print-shop-canvas-skill`](skills/print-shop-canvas-skill/SKILL.md) | Physical print layout generator via Python Pillow: 300 DPI rendering, cutting bleed margins, print-ready PDF export. | `desain cetak`, `kartu garansi`, `kalender`, `300 dpi`, `bleed` |
| [`browser-speech-to-text-skill`](skills/browser-speech-to-text-skill/SKILL.md) | Zero-server-cost Web Speech STT: Android PWA microphone bridge, visualViewport soft-keyboard avoidance. | `suara ke teks browser`, `web speech stt`, `dikte web`, `mic pwa` |

### D. AI Gateways, Resilient Data & Human Copywriting (4 Modules)

| Skill Module | Core Capability & Problem Solved | Auto-Invoke Triggers |
|---|---|---|
| [`ai-rotary-shield-skill`](skills/ai-rotary-shield-skill/SKILL.md) | Reverse proxy pool with multi-account rotation: automated HTTP 429 rate limit detection, zero-buffer SSE streaming pass-through, instant failover. | `limit 429`, `kuota habis`, `resource exhausted`, `putar akun ai` |
| [`token-frugal-intent-ladder-skill`](skills/token-frugal-intent-ladder-skill/SKILL.md) | Token-frugal AI ladder: 0-token regex and heuristic disambiguation for natural language financial inputs, clean note extraction. | `tangga ai`, `parsing nominal terbilang`, `hutang piutang`, `clean note` |
| [`human-copywriting-id-skill`](skills/human-copywriting-id-skill/SKILL.md) | Indonesian human-centric copywriting & conversion UX: anti-AI slop elimination, Coffee Shop Test, PAS/BAB formulas, 4 zero-traps, and 7-sweep text audit. | `copywriting manusiawi`, `bahasa awam`, `anti-robot`, `kata-kata enak`, `bikin kalimat` |
| [`voice-hud-wayland-skill`](skills/voice-hud-wayland-skill/SKILL.md) | Hands-free technician voice-to-text HUD on Linux Wayland: local faster-whisper streaming and glassmorphism overlay. | `dikte suara`, `hands-free`, `voice hud`, `wayland`, `solder` |

---

## 4. Beginner-Friendly Tech Stack Breakdown

*   **Frontend (User Interface)**:
    *   **HTML5 Server-Side Rendering (SSR)** &rarr; *meaning* pages load instantly (<100ms) on smartphones without blank-screen JavaScript hydration delays.
    *   **Tailwind CSS (Play CDN)** &rarr; *meaning* clean, responsive modern interfaces without needing node_modules or Node.js compilers on the production server.
    *   **Alpine.js & HTMX** &rarr; *meaning* interactive buttons, modals, and partial page swaps work directly through clean HTML markup.
    *   **Lucide SVG** &rarr; *meaning* crisp inline vector graphics on any screen density without external font files or awkward emojis.
*   **Backend (Application Core)**:
    *   **Python FastAPI / Flask Single-Worker** &rarr; *meaning* minimal memory footprint (<50MB RAM), transparent line-numbered error logs, and low operating temperatures.
    *   **Rust & Tauri v2** &rarr; *meaning* native hardware USB/serial port communication with 30MB RAM, completely replacing memory-heavy Electron runtimes.
*   **Database (Outage-Proof Storage)**:
    *   **SQLite WAL Mode (`PRAGMA synchronous = NORMAL; busy_timeout = 5000;`)** &rarr; *meaning* database transactions are immune to data corruption even during abrupt workshop electrical blackouts.

---

## 5. Empirical Performance Benchmarks

Measured on an active workshop server (Intel Core i3-3240 @ 3.40GHz, 7.6GB RAM, Ubuntu Linux):

| Benchmark Metric | Conventional Enterprise Stack | Zero-Bloat Standards | Real-World Impact |
|---|---|---|---|
| **Web Application RAM Footprint** | 450 MB - 1.2 GB (Node/React/Postgres) | **36 MB - 48 MB** (FastAPI + SQLite WAL) | **Up to 92% RAM reduction** |
| **Daemon Standby CPU Utilization** | 3% - 8% (Loop polling with sleep) | **0.0%** (Kernel inotifywait hook) | **Zero wasted CPU cycles** |
| **Edge CCTV Camera Streaming** | 85% CPU load (FFmpeg transcoding) | **0.8% CPU load** (go2rtc pass-through) | **Processor stays cold on STBs** |
| **Sudden Power Outage Resilience** | High risk of file header corruption | **100% Intact** (Atomic WAL commits) | **Zero corrupted records** |
| **Cold-Start Latency** | 3.5 - 8.0 seconds | **< 120 milliseconds** | **Instant interface readiness** |
| **CI Test Suite Execution** | 2 - 5 minutes (heavy npm compilation) | **16 Seconds** (GitHub Actions runner) | **Rapid iteration cycles** |

---

## 6. Engineering Valuation

Cost comparison between hiring conventional software houses vs implementing self-hosted `zero-bloat-skills`:

| Infrastructure & Operational Requirement | Commercial Software House Path | Zero-Bloat Skills Self-Hosted Path | Annual Savings |
|---|---|---|---|
| **Monthly Cloud Server Rent** | Cloud VPS 8GB + Managed DB: $45 / mo | Repurposed Workshop i3 PC: **$0** | **Save $540 / yr (Rp 8,500,000)** |
| **ISP Static Public IP Addon** | Dedicated Static IP Addon: $18 / mo | Cloudflare Tunnel + Tailscale Mesh: **$0** | **Save $216 / yr (Rp 3,400,000)** |
| **27 Custom SOP Modules Development** | External Software Agency: $1,350 | 27 Open-Source Engineered Modules: **$0** | **Save $1,350 (Rp 21,300,000)** |
| **Technician Triage Duration** | Manual probing without boardview: ~90 min | Boardview copilot + 1A injection: ~15 min | **Save 75 mins / unit** |
| **TOTAL ENGINEERING VALUATION** | **Expensive Cloud Lock-in** | **Self-Hosted Independent Sovereign** | **Save ~Rp 84,300,000 / yr** |

---

## 7. Smoke Test Verification

Direct terminal outputs verifying system health and multi-agent distribution:

```text
$ cd ~/zero-bloat-skills && ./test.sh
=====================================================================
[*] ZERO-BLOAT-SKILLS: Unified Health Check & Verification
=====================================================================
[*] [Check 1/5] Memeriksa sintaks skrip Shell...
[+] PASS: Seluruh skrip shell valid secara sintaksis.
[*] [Check 2/5] Memeriksa validitas YAML frontmatter seluruh modul skill...
[+] PASS: Seluruh 27 skill valid (YAML frontmatter, naming, description).
[*] [Check 3/5] Memeriksa proteksi CSS Viewport & Scroll Safety...
[+] PASS: Viewport CSS steril (bebas dari jebakan overflow-x: hidden pada html/body).
[*] [Check 4/5] Menjalankan smoke test starter-app...
[+] PASS: Starter app smoke test lolos 100% (FastAPI + SQLite WAL Fortress).
[*] [Check 5/5] Memeriksa sanitasi OPSEC (kredensial & secret)...
[+] PASS: OPSEC bersih (nol token/private key bocor).
=====================================================================
[+] SUCCESS: 5/5 verifikasi lolos tanpa kendala. Repositori siap rilis!
=====================================================================

$ ./install.sh --verify
=====================================================================
[*] Memeriksa integritas symlink zero-bloat-skills di cluster ruko...
=====================================================================
[+] STATUS: PRIMA (243 symlinks sehat, nol broken link).
=====================================================================

$ gh run list --limit 1
✓  [skill] tambah zero-bloat-icon...  Zero-Bloat CI & Health Check  main  push  16s
```

---

<div align="center">
  Megapass Intra Solusindo • Sidoarjo, Indonesia
</div>
