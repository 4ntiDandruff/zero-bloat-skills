---
name: zero-bloat-web-stack-skill
description: "Arsitektur web zero-bloat ultra-ringan: FastAPI/Flask + SQLite WAL + HTMX + Alpine.js + Tailwind CSS + Lucide SVG (tanpa node_modules di runtime, RAM <40MB, cold-start <100ms)."
---

# Zero-Bloat Web Stack Skill

Architectural guidelines for building high-performance, mobile-responsive web interfaces consuming <40MB RAM without gigabytes of Node.js dependencies on production servers.

---

## 1. The Zero-Bloat Philosophy

- **Say No to Heavy SPA Frameworks for Internal Utilities**: Massive bundles, hundreds of megabytes of server memory overhead, and churn across major library versions.
- **Embrace Native Web Standards**:
  - **Structure**: HTML5 SSR (Jinja2 / FastAPI) for instant First Contentful Paint (<100ms).
  - **Visuals**: Tailwind CSS (standalone CDN or micro-compiled single CSS file).
  - **Reactivity**: Alpine.js (declarative local component state without build steps).
  - **Data Flow**: HTMX (partial AJAX DOM swaps driven directly by server responses).
  - **Icons**: Lucide inline SVG vectors (zero icon-font dependencies or emoji clutter).

---

## 2. Minimalist Single-File Backend Pattern (`app.py`)

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    conn = sqlite3.connect("data.db", timeout=10.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL;")
    return conn

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    conn = get_db()
    items = conn.execute("SELECT * FROM items ORDER BY id DESC LIMIT 20").fetchall()
    conn.close()
    return templates.TemplateResponse(request=request, name="index.html", context={"items": items})

@app.post("/items/add")
async def add_item(request: Request):
    form = await request.form()
    title = form.get("title")
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (title) VALUES (?)", (title,))
    item_id = cur.lastrowid
    conn.commit()
    conn.close()
    
    # Return instantaneous partial HTML swapped directly by HTMX
    return HTMLResponse(f"""
        <li class="p-3 bg-slate-900 border border-slate-800 rounded-lg flex justify-between">
            <span>{title}</span>
            <span class="text-xs text-emerald-400 font-mono">New</span>
        </li>
    """)
```

---

## 3. Clean Responsive Interface Template (`templates/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zero-Bloat Console</title>
    <!-- Standalone Zero-Bloat Assets (No node_modules at runtime) -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans antialiased">
    <div class="max-w-2xl mx-auto space-y-6">
        <!-- Instant Form Submission via HTMX -->
        <form hx-post="/items/add" hx-target="#item-list" hx-swap="afterbegin" class="flex gap-2">
            <input type="text" name="title" placeholder="Record new repair order..." required
                   class="flex-1 bg-slate-900 border border-slate-800 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-cyan-500">
            <button type="submit" class="bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-lg text-sm font-medium transition">
                Submit
            </button>
        </form>

        <!-- Reactive Item List -->
        <ul id="item-list" class="space-y-2">
            {% for item in items %}
            <li class="p-3 bg-slate-900 border border-slate-800 rounded-lg flex justify-between">
                <span>{{ item.title }}</span>
                <span class="text-xs text-slate-500 font-mono">#{{ item.id }}</span>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```
