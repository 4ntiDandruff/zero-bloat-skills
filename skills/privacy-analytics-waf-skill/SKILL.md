---
name: privacy-analytics-waf-skill
description: "Engine analitik pengunjung web mandiri berbasis SQLite (zero-cookie, tanpa Google Analytics) dan sekring pengaman WAF ringan penyaring brute-force IP rate limiting."
---

# Privacy Analytics & Lightweight WAF Skill

Zero-cookie, privacy-friendly visitor analytics engine persisting directly to local SQLite WAL tables without third-party tracking scripts, coupled with an in-memory/sliding-window Web Application Firewall (WAF) circuit breaker.

---

## 1. The Cost of Third-Party Trackers

- Commercial tracking scripts (Google Tag Manager, Meta Pixel) introduce 200-500ms of external network latency to initial page loads.
- They leak user IP addresses and browsing habits to corporate advertising platforms.
- They are frequently blocked by browser extensions and local DNS sinkholes (AdGuard Home, Pi-hole), distorting actual traffic metrics.

---

## 2. Lightweight SQLite Analytics Schema (`visitors.db`)

Collect actionable metrics using anonymized hashes without storing sensitive personal information:

```sql
CREATE TABLE IF NOT EXISTS page_views (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    user_agent_hash TEXT NOT NULL,
    ip_prefix TEXT NOT NULL, -- Only store subnet prefix (e.g., 192.168.1.0/24)
    referer TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_path_time ON page_views(path, timestamp);
```

---

## 3. Lightweight WAF Rate-Limiting Middleware (FastAPI)

Circuit breaker operating at the ASGI middleware level to intercept abusive bots before queries reach the database layer:

```python
import time
from fastapi import Request, HTTPException

REQUEST_BUCKET = {}
BAN_LIST = set()

RATE_LIMIT = 60 # Maximum 60 requests per minute
BAN_DURATION = 1800 # 30-minute block upon violation

async def waf_rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    now = time.time()
    
    # 1. Check blacklist
    if client_ip in BAN_LIST:
        raise HTTPException(status_code=403, detail="Access denied by circuit WAF.")
        
    # 2. Sliding window check
    timestamps = REQUEST_BUCKET.get(client_ip, [])
    timestamps = [t for t in timestamps if now - t < 60]
    
    if len(timestamps) >= RATE_LIMIT:
        BAN_LIST.add(client_ip)
        raise HTTPException(status_code=429, detail="Request threshold exceeded. IP frozen.")
        
    timestamps.append(now)
    REQUEST_BUCKET[client_ip] = timestamps
    
    response = await call_next(request)
    return response
```
