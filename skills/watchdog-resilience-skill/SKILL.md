---
name: watchdog-resilience-skill
description: "SOP sistem self-healing Linux ruko: recovery loop PM2 & systemd, perbaikan DNS negative cache lockout AdGuard Home, watchdog Cloudflare Tunnel, dan sinkronisasi multi-agent symlink hub."
---

# Watchdog Resilience & Self-Healing Skill

SOP sistem self-healing tingkat daemon untuk mendeteksi service macet, mengatasi kebocoran memori, memulihkan kegagalan DNS seketika, dan menjaga integritas cluster mesin ruko.

---

## 1. SOP Penanganan Cache Negatif DNS AdGuard Home

### Gejala:
Domain publik baru didaftarkan atau subdomain Cloudflare Tunnel diubah. Domain dapat di-resolve via DNS publik (1.1.1.1), tetapi seluruh komputer di LAN ruko mengalami `NXDOMAIN` atau gagal koneksi saat diarahkan ke IP AdGuard Home.

### Akar Masalah:
AdGuard Home menyimpan respon NXDOMAIN sebelumnya ke dalam cache memori persisten mengikuti nilai SOA TTL. Me-restart service saja tidak selalu menghapus entri negatif ini.

### Solusi Resiliensi 10 Detik:
1. Tambahkan DNS rewrite sementara di konfigurasi `/opt/AdGuardHome/AdGuardHome.yaml`:
   ```yaml
   rewrites:
     - domain: "subdomain.example.com"
       answer: "192.168.1.50"
       enabled: true # WAJIB: Tanpa ini AdGuard mengabaikan rewrite
   ```
2. Restart service:
   ```bash
   sudo systemctl restart AdGuardHome
   ```
3. Verifikasi instan:
   ```bash
   dig @127.0.0.1 subdomain.example.com +short
   ```

---

## 2. Watchdog Pemulih Cloudflare Tunnel

Skrip cron yang memeriksa kelancaran arus tunnel publik setiap 3 menit:

```bash
#!/usr/bin/env bash
CHECK_URL="https://health.example.com/ping"

STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$CHECK_URL" || true)

if [[ "$STATUS_CODE" != "200" ]]; then
    echo "[!] Tunnel drop terdeteksi (HTTP $STATUS_CODE). Merestart cloudflared..."
    sudo systemctl restart cloudflared
    sleep 5
fi
```

---

## 3. PM2 Safety & Anti-Disaster Rule

- **DILARANG**: `pm2 delete all` (menghapus seluruh konfigurasi proses lain yang sedang aktif melayani klien).
- **Wajib Selalu Spesifik**: `pm2 restart <nama-aplikasi>` atau `pm2 reload <nama-aplikasi>`.
- **Prosedur Pemulihan Bencana**:
  Jika terjadi reboot mendadak atau kecelakaan terminal:
  ```bash
  pm2 resurrect
  ```
  Selalu simpan snapshot konfigurasi setelah menambah service baru:
  ```bash
  pm2 save
  ```

---

## 4. Sinkronisasi Hub Multi-Agent Simetris

Gunakan skrip `update-agents.sh` untuk memelihara symlink skill secara otomatis ke seluruh platform coding AI:
```bash
ln -sfn ~/.hermes/skills/* ~/.claude/skills/
ln -sfn ~/.hermes/skills/* ~/.gemini/config/skills/
ln -sfn ~/.hermes/skills/* ~/.omp/skills/
```
