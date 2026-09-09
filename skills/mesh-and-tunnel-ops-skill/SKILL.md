---
name: mesh-and-tunnel-ops-skill
description: "Zero-port-forwarding workshop networking: Cloudflare Tunnel for secure public HTTPS ingress and Tailscale WireGuard subnet mesh for private node interconnects."
---

# Mesh & Tunnel Ops Skill

Zero-port-forwarding network topology pattern for workshop servers and homelab machines without exposing ports on consumer ISP routers (anti-DDoS, zero static IP dependencies, and automatic SSL encryption).

---

## 1. Dual-Layer Topology (Public vs Private)

```
[ Public Internet Traffic ] 
             ↓
  [ Cloudflare Edge (WAF + DDoS Protection + Free SSL Certificate) ]
             ↓ (Outbound Encrypted Tunnel)
  [ Local Workbench Server (cloudflared daemon) ]
             ↓
[ Local Application Endpoints (localhost:8000) ]

-----------------------------------------------------

[ Technician & Point-to-Point Node Traffic ]
             ↓
  [ Tailscale WireGuard Mesh (100.x.y.z) ]
             ↓
[ Direct SSH & Bulk File Transfers Bypassing Cloudflare Limits ]
```

---

## 2. Production Cloudflare Tunnel Configuration

Official service configuration lives at `/etc/cloudflared/config.yml`:

```yaml
tunnel: a1b2c3d4-xxxx-xxxx-xxxx-xxxxxxxxxxxx
credentials-file: /etc/cloudflared/cert.json

ingress:
  # Service Endpoint 1
  - hostname: app.example.com
    service: http://localhost:8000
    originRequest:
      noTLSVerify: true
      connectTimeout: 10s

  # Service Endpoint 2
  - hostname: cctv.example.com
    service: http://localhost:1984

  # Mandatory 404 security fallback
  - service: http_status:404
```

---

## 3. Tailscale Subnet Router Configuration

Expose entire local workshop LAN subnets without installing Tailscale clients on legacy printers or test benches:

```bash
# Enable IPv4 packet forwarding in Linux kernel
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf

# Advertise local LAN subnet routes
sudo tailscale up --advertise-routes=192.168.1.0/24 --accept-routes
```

---

## 4. Verification Routines

```bash
# Inspect Cloudflare Tunnel service status
sudo systemctl status cloudflared

# Check mesh node status
tailscale status
tailscale ping 100.100.100.1
```
