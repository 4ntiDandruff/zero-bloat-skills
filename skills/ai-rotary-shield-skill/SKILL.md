---
name: ai-rotary-shield-skill
description: "Reverse proxy gateway and multi-account token pooling architecture for AI agent CLIs: automated HTTP 429 and quota exhaustion detection, instantaneous rotary failover, and cooldown dampers."
---

# AI Rotary Shield Pool Skill

Intelligent reverse proxy gateway architecture engineered to preserve execution continuity for autonomous AI coding agents (Claude Code, Google Antigravity CLI, Oh My Pi, OpenCode) when upstream API quotas are exhausted (HTTP 429 Too Many Requests / Resource Exhausted).

---

## 1. The Autonomous Coding Quota Challenge

- Agentic coding loops consume tens of thousands of tokens per minute during multi-file refactoring and AST inspections.
- When an account hits minute rate limits or daily usage caps, the agent session terminates immediately, discarding intermediate working state.
- Conventional manual interventions (waiting for reset windows) waste hours of productive workbench time.

---

## 2. Rotary Shield Circuit Topology

```
[ AI Agent Terminal (Claude / Antigravity / OMP) ]
                      ↓
[ Local Reverse Proxy Gateway (FastAPI / Node.js) ]
                      ↓
  [ Token Rotary Circuit Pool ]
    ├── Pool Account 1 (Active - Primary)
    ├── Pool Account 2 (Standby - Warm)
    └── Pool Account 3 (Standby)
                      ↓
  [ Upstream Provider API (Google / Anthropic / OpenRouter) ]
```

### Fail-Safe Relay Logic:
1. Incoming agent payloads route to `Pool Account 1`.
2. If the upstream provider returns status **429**, **403 Quota**, or `RESOURCE_EXHAUSTED`:
   * Intercept the error response; do not propagate it back to the agent CLI.
   * Mark `Pool Account 1` with a `COOLING_DOWN` timestamp (15-60 minute dampening period).
   * Instantly switch the relay to `Pool Account 2`.
   * Transparently replay the failed request.
3. The coding agent receives an HTTP 200 payload without session disruption.

---

## 3. Rotary Switch Implementation (Python FastAPI)

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
    return None # Entire pool is currently cooling down

@app.post("/v1/chat/completions")
async def proxy_completions(request: Request):
    global current_index
    body = await request.body()
    headers = dict(request.headers)
    
    for attempt in range(3):
        acc = get_next_available_token()
        if not acc:
            return Response("Entire account pool is cooling down.", status_code=429)
            
        headers["Authorization"] = f"Bearer {acc['token']}"
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post("https://api.upstream.example.com/v1/chat/completions", content=body, headers=headers)
            
            if resp.status_code in [429, 403] or "RESOURCE_EXHAUSTED" in resp.text:
                acc["cooling_until"] = time.time() + 900 # 15-minute cooldown
                current_index = (current_index + 1) % len(TOKEN_POOL)
                continue # Retry next account in rotary sequence
                
            return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
            
    return Response("Gateway failed across all pool retries.", status_code=500)
```
