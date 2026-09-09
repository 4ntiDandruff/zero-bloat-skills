---
name: ai-rotary-shield-skill
description: "Arsitektur reverse proxy gateway & multi-account pooling untuk AI agent CLI: deteksi otomatis HTTP 429/quota exhaustion, auto-failover ke token cadangan, dan peredam rate limit rotary."
---

# AI Rotary Shield Pool Skill

Arsitektur gateway proxy cerdas untuk menjaga kontinuitas proses coding agen AI (Claude Code, Google Antigravity CLI, Oh My Pi, OpenCode) agar tidak terhenti di tengah jalan akibat batasan kuota (HTTP 429 Too Many Requests / Resource Exhausted).

---

## 1. Masalah Kuota AI Agentic Coding

- Sesi koding autonomous agents mengonsumsi puluhan ribu token dalam waktu singkat saat menjalankan refactoring atau audit besar.
- Saat akun utama mencapai batas rate limit per-menit atau kuota harian habis, terminal agent akan berhenti mendadak dan membatalkan progres kerja.
- Solusi konvensional (menunggu kuota reset manual) menghabiskan waktu produktif hingga beberapa jam.

---

## 2. Prinsip Sirkuit Rotary Shield

```
[ AI Agent Terminal (Claude / Antigravity / OMP) ]
                      ↓
[ Gateway Reverse Proxy Lokal (FastAPI / Node.js) ]
                      ↓
  [ Token Rotary Circuit Pool ]
    ├── Akun Pool 1 (Aktif - Primary)
    ├── Akun Pool 2 (Siap Siaga - Warm Standby)
    └── Akun Pool 3 (Siap Siaga)
                      ↓
  [ Upstream Provider API (Google / Anthropic / OpenRouter) ]
```

### Logika Fail-Safe:
1. Permintaan masuk dialirkan ke `Akun Pool 1`.
2. Jika upstream mengembalikan kode status **429**, **403 Quota**, atau string error `RESOURCE_EXHAUSTED`:
   * Jangan teruskan error ke terminal agent.
   * Tandai `Akun Pool 1` dalam status `COOLING_DOWN` (periode pendinginan 15-60 menit).
   * Putar relai (*rotate switch*) secara instan ke `Akun Pool 2`.
   * Ulangi (*replay*) request yang gagal secara transparan.
3. Terminal agent menerima response valid HTTP 200 tanpa pernah menyadari adanya pergantian akun di belakang layar.

---

## 3. Implementasi Rotary Switch di Python FastAPI

```python
import httpx
import time
from fastapi import FastAPI, Request, Response

app = FastAPI()

TOKEN_POOL = [
    {"id": "acc_01", "token": "KEY_1", "cooling_until": 0},
    {"id": "acc_02", "token": "KEY_2", "cooling_until": 0},
    {"id": "acc_03", "token": "KEY_3", "cooling_until": 0},
]
current_index = 0

def get_next_available_token():
    global current_index
    now = time.time()
    for _ in range(len(TOKEN_POOL)):
        acc = TOKEN_POOL[current_index]
        if acc["cooling_until"] <= now:
            return acc
        current_index = (current_index + 1) % len(TOKEN_POOL)
    return None # Seluruh pool sedang cooling down

@app.post("/v1/chat/completions")
async def proxy_completions(request: Request):
    global current_index
    body = await request.body()
    headers = dict(request.headers)
    
    for attempt in range(3):
        acc = get_next_available_token()
        if not acc:
            return Response("Seluruh kuota pool sedang habis.", status_code=429)
            
        headers["Authorization"] = f"Bearer {acc['token']}"
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post("https://api.upstream.example.com/v1/chat/completions", content=body, headers=headers)
            
            if resp.status_code in [429, 403] or "RESOURCE_EXHAUSTED" in resp.text:
                acc["cooling_until"] = time.time() + 900 # Pendinginan 15 menit
                current_index = (current_index + 1) % len(TOKEN_POOL)
                continue # Coba akun berikutnya
                
            return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
            
    return Response("Gagal setelah memutar pool.", status_code=500)
```
