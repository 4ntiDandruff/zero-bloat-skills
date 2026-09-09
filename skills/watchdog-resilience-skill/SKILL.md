---
name: watchdog-resilience-skill
description: "Self-healing Linux workbench SOP: PM2 and systemd restart loops, AdGuard Home DNS negative cache lockout flusher, Cloudflare Tunnel watchdog, and symmetric multi-agent hub sync."
---

# Watchdog Resilience & Self-Healing Skill

Operating procedures for daemon self-healing: detecting frozen processes, mitigating memory leaks, instantly clearing persistent DNS resolver blackholes, and keeping multi-agent hub symlinks synchronized.

---

## 1. AdGuard Home DNS Negative Cache Lockout Remediation

### Symptom:
A new public domain or Cloudflare Tunnel subdomain is provisioned. The domain resolves properly via upstream resolvers (1.1.1.1), but all LAN workstation machines return `NXDOMAIN` or connection timeouts when querying the local AdGuard Home resolver.

### Root Cause:
AdGuard Home retains negative `NXDOMAIN` records in memory cache respecting authoritative SOA TTL values (often 30+ minutes). Simply restarting the service frequently fails to flush persistent zone caches.

### 10-Second Resilience Procedure:
1. Inject a transient explicit DNS rewrite in `/opt/AdGuardHome/AdGuardHome.yaml`:
   ```yaml
   rewrites:
     - domain: "subdomain.example.com"
       answer: "192.168.1.50"
       enabled: true # MANDATORY: Without enabled: true AdGuard ignores rewrite
   ```
2. Restart the daemon:
   ```bash
   sudo systemctl restart AdGuardHome
   ```
3. Verify resolution immediately:
   ```bash
   dig @127.0.0.1 subdomain.example.com +short
   ```

---

## 2. Cloudflare Tunnel Health Watchdog

A lightweight cron watchdog verifying public ingress health every 3 minutes:

```bash
#!/usr/bin/env bash
CHECK_URL="https://health.example.com/ping"

STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$CHECK_URL" || true)

if [[ "$STATUS_CODE" != "200" ]]; then
    echo "[!] Tunnel drop detected (HTTP $STATUS_CODE). Restarting cloudflared..."
    sudo systemctl restart cloudflared
    sleep 5
fi
```

---

## 3. PM2 Operational Safety & Anti-Disaster Rule

- **STRICTLY PROHIBITED**: `pm2 delete all` (wipes active configurations of all running production services).
- **Mandatory Targeted Commands**: `pm2 restart <app_name>` or `pm2 reload <app_name>`.
- **Disaster Recovery**:
  In the event of an unexpected power failure or accidental PM2 state loss:
  ```bash
  pm2 resurrect
  ```
  Always commit state snapshots after adding or updating services:
  ```bash
  pm2 save
  ```

---

## 4. Symmetric Multi-Agent Skill Synchronization

Maintain synchronized symlinks across all AI coding agent directories via an automated script (`update-agents.sh`):
```bash
ln -sfn ~/.hermes/skills/* ~/.claude/skills/
ln -sfn ~/.hermes/skills/* ~/.gemini/config/skills/
ln -sfn ~/.hermes/skills/* ~/.omp/skills/
```
