---
name: mesh-and-tunnel-ops-skill
description: "Topologi jaringan ruko zero-port-forwarding: Cloudflare Tunnel untuk ingress publik HTTPS gratis + Tailscale subnet mesh privat antar PC/node."
---

# Mesh & Tunnel Ops Skill

Panduan topologi jaringan aman untuk server homelab dan ruko tanpa membuka port publik di router ISP (anti-DDoS, zero IP publik statis, dan HTTPS otomatis).

---

## 1. Topologi Dual-Layer (Publik vs Privat)

```
[ Internet Publik ] 
        ↓
  [ Cloudflare Edge (WAF + DDOS Shield + SSL Gratis) ]
        ↓ (Outbound Encrypted Tunnel)
  [ PC Server Ruko (cloudflared daemon) ]
        ↓
[ Aplikasi Web Lokal (localhost:8000) ]

-----------------------------------------------------

[ Akses Teknisi / Antar-Node Privat ]
        ↓
  [ Tailscale WireGuard Mesh (100.x.y.z) ]
        ↓
[ Akses SSH Direct / Transfer File Antar PC Tanpa Batasan Cloudflare ]
```

---

## 2. Konfigurasi Cloudflare Tunnel Standar Produksi

File konfigurasi resmi berada di `/etc/cloudflared/config.yml`:

```yaml
tunnel: a1b2c3d4-xxxx-xxxx-xxxx-xxxxxxxxxxxx
credentials-file: /etc/cloudflared/cert.json

ingress:
  # Endpoint Layanan 1
  - hostname: app.domain.com
    service: http://localhost:8000
    originRequest:
      noTLSVerify: true
      connectTimeout: 10s

  # Endpoint Layanan 2
  - hostname: cctv.domain.com
    service: http://localhost:1984

  # Fallback 404 wajib untuk keamanan
  - service: http_status:404
```

---

## 3. Tailscale Subnet Router

Agar seluruh perangkat di LAN ruko dapat diakses dari luar tanpa memasang client Tailscale di setiap printer atau CCTV:

```bash
# Aktifkan IP Forwarding di kernel Linux
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf

# Pasang subnet router LAN
sudo tailscale up --advertise-routes=192.168.1.0/24 --accept-routes
```

---

## 4. SOP Verifikasi Jaringan

```bash
# Uji status tunnel Cloudflare
sudo systemctl status cloudflared

# Uji konektivitas mesh Tailscale
tailscale status
tailscale ping 100.100.100.1
```
