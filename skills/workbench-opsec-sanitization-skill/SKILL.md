---
name: workbench-opsec-sanitization-skill
description: "Workbench and Linux sysadmin OPSEC sanitization SOP: automated regex detection and in-place masking for OS user paths (~/), Tailscale CGNAT IPs, LAN subnets, hardware serial numbers, and bot credentials before public git commits."
---

# WORKBENCH-OPSEC-SANITIZATION-SKILL
### SOP Sanitasi OPSEC Meja Servis & Pengaburan Jejak Sensitif Linux Bare-Metal

Modul ini adalah sekring gerbang logika (*pre-flight circuit breaker*) yang memastikan seluruh kode, log terminal, skrip, dan dokumentasi markdown steril dari identitas personal, topologi jaringan privat ruko, dan data pelanggan meja servis sebelum dipublikasikan ke repositori publik.

---

## 1. Topologi Risiko & Vektor Kebocoran Meja Servis

```text
[ Terminal Meja Servis / Log Nyata ]
      │
      ├─► Jalur File OS (/home/user/, C:\Users\user\)
      ├─► Mesh & IP Privat (100.x.y.z Tailscale, 192.168.110.x LAN)
      ├─► Data Pelanggan (Service Tag laptop, Serial Number board, MAC)
      └─► Kredensial Daemon (Telegram Bot Token, SSH Keys, .session)
      │
      ▼ (Filter Sekring OPSEC)
[ scripts/sanitize.py / Linter CI ]
      │
      ▼ (100% Steril & Aman Rilis)
[ Repositori Publik GitHub / Web Showcase ]
```

---

## 2. Lima Sekring Sirkuit OPSEC (The 5 Circuit Fuses)

| Sekring | Target Pola Sensitif | Pengaburan Baku (Replacement) | Dampak Fisik / Risiko |
|---|---|---|---|
| **FUSE-01: User Paths** | `/home/[a-zA-Z0-9_-]+/` | `~/` atau `$HOME/` | Mencegah pelacakan identitas akun OS teknisi. |
| **FUSE-01b: Win Paths** | `[A-Z]:\\Users\\[a-zA-Z0-9_-]+\\` | `%USERPROFILE%\` | Menyamarkan akun pada dual-boot Windows ruko. |
| **FUSE-02: Mesh IPs** | `100\.(6[4-9]\|[7-9][0-9]\|1[0-1][0-9]\|12[0-7])\.[0-9]{1,3}\.[0-9]{1,3}` | `localhost` atau `100.64.0.1` | Mengamankan rute subnet router WireGuard ruko. |
| **FUSE-03: Subnet LAN** | `192\.168\.110\.[0-9]{1,3}` | `192.168.1.1` | Menyembunyikan segmen IP DNS server AdGuard ruko. |
| **FUSE-04: Hardware SN** | `(SN\|Service Tag\|Serial Number)[:= ]+[A-Z0-9]{7,24}` | `[REDACTED_SERIAL]` | Melindungi privasi laptop pelanggan servis. |
| **FUSE-04b: MAC Addr** | `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})` | `00:11:22:33:44:55` | Menyamarkan identitas fisik kartu jaringan LAN/WLAN. |
| **FUSE-05: Bot & Secret**| `[0-9]{9,10}:[a-zA-Z0-9_-]{35}` | `[REDACTED_BOT_TOKEN]` | Mencegah pembajakan bot remote control ruko. |
| **FUSE-05b: SSH Keys** | `-----BEGIN [A-Z]+ PRIVATE KEY-----` | `[-] BLOCK COMMIT` | Sekring mutlak pemutus commit kunci otentikasi. |

---

## 3. Utilitas Sanitasi Otomatis (`scripts/sanitize.py`)

Gunakan skrip Python bawaan modul (murni pustaka standar tanpa dependensi luar) untuk memindai dan membersihkan berkas secara cepat:

### A. Mode Pindai (Dry-Run / Audit Saja)
```bash
# Pindai direktori tanpa mengubah isi berkas
python3 skills/workbench-opsec-sanitization-skill/scripts/sanitize.py --scan .
```

### B. Mode Perbaiki Otomatis (In-Place Fix)
```bash
# Bersihkan seluruh pola sensitif secara langsung pada berkas target
python3 skills/workbench-opsec-sanitization-skill/scripts/sanitize.py --fix README.md
python3 skills/workbench-opsec-sanitization-skill/scripts/sanitize.py --fix docs/
```

---

## 4. SOP Pre-Flight Sanitasi Sebelum Commit Publik

Setiap kali menyelesaikan pekerjaan di terminal dan bersiap melakukan commit atau push:

1. **Jalankan Scanner Mandiri**:
   ```bash
   python3 skills/workbench-opsec-sanitization-skill/scripts/sanitize.py --scan .
   ```
2. **Periksa Output Terminal Sebelum Salin ke README**:
   * Jangan salin teks terminal mentah yang menampilkan prompt `username@hostname:~$`.
   * Ganti prompt menjadi tanda dolar universal: `$ command`.
3. **Verifikasi Jalur Symlink**:
   * Pastikan output `./install.sh --verify` di dokumentasi menggunakan prefix `~/.gemini/` bukan `/home/<user>/.gemini/`.
4. **Verifikasi Ekstensi Terlarang di Git**:
   * Pastikan `.gitignore` selalu mengecualikan berkas sesi MTProto:
     ```gitignore
     *.session
     *.session-journal
     .env
     *.map
     ```

---

## 5. Integrasi ke Test Suite (`test.sh`)

Modul ini dihubungkan langsung ke **Check 5/5** di skrip `test.sh`. Seluruh CI build di GitHub Actions dan eksekusi rilis lokal wajib lolos validasi tanpa adanya kebocoran string sensitif.
