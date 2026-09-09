<div align="center">

# ZERO-BLOAT-SKILLS

**17 Circuit-Level Operational Skills for Hardware Technicians, Bare-Metal Linux, and Multi-Agent AI Gateways**

[![Hardware Lab](https://img.shields.io/badge/Laboratory-Megapass%20Intra%20Solusindo-0284c7?style=flat-square)](https://megapass.web.id)
[![Certification](https://img.shields.io/badge/BNSP%20Certified-Electronics%20Technician-10b981?style=flat-square)](https://github.com/4ntiDandruff)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Bloat%20%7C%20%3C50MB%20RAM-f59e0b?style=flat-square)](https://github.com/4ntiDandruff/zero-bloat-skills)
[![License](https://img.shields.io/badge/License-MIT-6366f1?style=flat-square)](LICENSE)

<br/>

[English](README.md) &bull; [Bahasa Indonesia](README.id.md)

</div>

---

This skill suite was not conceived inside high-end cloud instances. It was engineered, tested, and proven directly on an aging Intel Core i3 bench machine (7.6GB RAM) inside the **Megapass Intra Solusindo** hardware repair workshop in Sidoarjo, Indonesia.

Designed to operate board-level motherboard diagnostics, SPI EEPROM flashing, zero-transcode edge media streaming, and multi-node service routing without memory leaks, background polling overhead, or runtime `node_modules` bloat.

Fully compatible with **Claude Code**, **Google Antigravity CLI**, **Oh My Pi (OMP)**, **OpenCode**, **Hermes Agent**, and **Codex CLI**.

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

## 2. Beginner-Friendly Tech Stack Breakdown

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

## 3. Real Metrics & Benchmarks

Empirical data recorded on the active Megapass workshop workbench server (Intel Core i3-3240 @ 3.40GHz, 7.6GB RAM, Ubuntu 24.04 LTS):

| Evaluation Metric | Conventional Industry Stack | Zero-Bloat Meja Servis | Real Efficiency Gain |
|---|---|---|---|
| Web App RAM Footprint | 450 MB - 1.2 GB (Node/React/Postgres) | 36 MB - 48 MB (FastAPI + SQLite WAL) | Up to 92% RAM reduction |
| Daemon Idle CPU Load | 3% - 8% (Polling loops with `sleep`) | 0.0% (Kernel `inotifywait` hook) | Zero idle CPU cycles |
| Edge CCTV Video Stream | 85% CPU load (FFmpeg re-encoding) | 0.8% CPU load (go2rtc RTP pass-through) | CPU runs cold on edge STBs |
| Sudden Outage Recovery | Corrupt journal / lock recovery required | 100% Intact (WAL commit + PRAGMA NORMAL) | Zero corrupt transactions |
| Cold-Start Latency | 3.5 - 8.0 seconds | < 120 milliseconds | Instant readiness |

---

## 4. Engineering Valuation

Cost and resource analysis comparing commercial software house deliverables against self-hosted `zero-bloat-skills` architecture:

| Infrastructure Need | Commercial Software House Path | Zero-Bloat Workbench Path | Real Savings Value |
|---|---|---|---|
| Monthly Cloud Hosting | 8GB RAM Cloud VPS + Managed DB: $45 / mo | Repurposed i3 Workshop PC + SQLite WAL: $0 | Saves $540 / year |
| Static Public IP Fee | Business ISP Static IP Addon: $18 / mo | Cloudflare Tunnel + Tailscale Subnet: $0 | Saves $216 / year |
| Custom Internal Tooling | Commercial desktop tooling contract: $1,200 | 17 Specialized modular skills: Included | Saves $1,200 one-time |
| Technician Triage Time | Manual probing without boardview copilot: ~90 min | Boardview copilot + current injection: ~15 min | Saves 75 min bench time / unit |

---

## 5. Repository Treeview

```
zero-bloat-skills/
├── LICENSE                               # Official MIT License (Hizam Nahari / Megapass)
├── README.md                             # Comprehensive global documentation
├── README.id.md                          # Indonesian language edition
├── install.sh                            # Universal multi-agent installer (auto-symlink)
├── uninstall.sh                          # Clean symlink removal script
│
├── skills/                               # 17 Specialized Workbench & Systems Skills
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
│   └── liquid-apple-ui-skill/            # Apple-style liquid dark UI, pill badges, Alpine tabs
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

## 6. Smoke Test (1-Click Verification Guide)

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
[*] Running starter app smoke test...
[+] Test 1 PASS: /health is operational and SQLite WAL mode is verified.
[+] Test 2 PASS: GET / renders HTML successfully (instant FCP).
[+] Test 3 PASS: POST /tickets/add successfully performs HTMX row swap.
[+] Test 4 PASS: Ticket persistence verified atomically in SQLite WAL.

[+] ALL SMOKE TESTS PASSED WITH EXIT CODE 0.
```

### Keeping Skills Updated

Because installation relies on atomic symlinks, fetching updates immediately refreshes all connected AI agents without re-running full configuration:

```bash
# Quick update via installer flag
./install.sh --update

# Or standard git pull
git pull origin main
```

---

## 7. Future Roadmap

* **Phase 1 (Current Release)**: Core 16-skill package, multi-agent symlink installer, and workbench starter app.
* **Phase 2 (Upcoming)**: Automated zero-bloat reverse-proxy config generator for Caddy and Nginx.
* **Phase 3 (Long-Term)**: Standalone `zero-bloat` CLI binary in Rust for instant zero-dependency project scaffolding.

---

<div align="center">

Megapass Intra Solusindo • Sidoarjo, Indonesia

</div>
