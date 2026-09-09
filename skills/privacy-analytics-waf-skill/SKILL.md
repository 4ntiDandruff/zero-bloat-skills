---
name: privacy-analytics-waf-skill
description: "Engine analitik pengunjung web mandiri berbasis SQLite (zero-cookie, tanpa Google Analytics) dan sekring pengaman WAF ringan penyaring brute-force IP rate limiting."
---

# Privacy Analytics & Lightweight WAF Skill

Pola arsitektur pencatatan statistik pengunjung ramah privasi yang berjalan mandiri di database lokal SQLite WAL tanpa skrip pelacak pihak ketiga (Google Tag Manager / Meta Pixel), dilengkapi sekring pemblokir serangan brute-force otomatis.

---

## 1. Masalah Tracker Pihak Ketiga

- Skrip pelacak seperti Google Analytics memperlambat loading halaman (menambah latensi eksternal 200-500ms).
- Membocorkan data IP dan kebiasaan browsing pengguna ke raksasa teknologi.
- Sering diblokir oleh AdBlocker/AdGuard sehingga statistik menjadi tidak akurat.

---

## 2. Skema SQLite Ringan (`visitors.db`)

Pencatatan metrik menggunakan hash anonymized tanpa menyimpan data pribadi:

```sql
CREATE TABLE IF NOT EXISTS page_views (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    user_agent_hash TEXT NOT NULL,
    ip_prefix TEXT NOT NULL, -- Hanya simpan 192.168.1.0/24 (privasi)
    referer TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_path_time ON page_views(path, timestamp);
```

---

## 3. Middleware WAF Sekring Brute-Force (Python FastAPI)

Sekring sirkuit di level middleware untuk mencegat bot penyerang sebelum query menyentuh database:

```python
import time
from fastapi import Request, HTTPException

# Cache memori sederhana untuk rate-limiting per IP
REQUEST_BUCKET = {}
BAN_LIST = set()

RATE_LIMIT = 60 # Maksimal 60 request per menit
BAN_DURATION = 1800 # Blokir 30 menit jika melanggar

async def waf_rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    now = time.time()
    
    # 1. Cek status blacklist
    if client_ip in BAN_LIST:
        raise HTTPException(status_code=403, detail="Akses diblokir oleh WAF sirkuit.")
        
    # 2. Catat dan bersihkan jendela waktu geser (sliding window)
    timestamps = REQUEST_BUCKET.get(client_ip, [])
    timestamps = [t for t in timestamps if now - t < 60]
    
    if len(timestamps) >= RATE_LIMIT:
        BAN_LIST.add(client_ip)
        raise HTTPException(status_code=429, detail="Batas request terlampaui. IP dibekukan.")
        
    timestamps.append(now)
    REQUEST_BUCKET[client_ip] = timestamps
    
    response = await call_next(request)
    return response
```
