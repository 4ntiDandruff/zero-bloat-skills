---
name: zero-bloat-web-stack-skill
description: "Arsitektur web zero-bloat ultra-ringan: FastAPI/Flask + SQLite WAL + HTMX + Alpine.js + Tailwind CSS + Lucide SVG (tanpa node_modules di runtime, RAM <40MB, cold-start <100ms)."
---

# Zero-Bloat Web Stack Skill

Panduan pengembangan aplikasi web modern berkinerja tinggi, responsif di HP, dan hemat memori (<40MB RAM) tanpa beban ratusan megabyte dependensi Node.js di server.

---

## 1. Filosofi Beban Arus Nol (Zero-Bloat Creed)

- **Menolak React/Next.js untuk Aplikasi Internal**: Bundling kompleks, konsumsi RAM server ratusan megabyte, dan kerentanan breaking-changes antar rilis.
- **Memilih Native Web Standards**:
  - **Kerangka**: HTML5 SSR (Jinja2 / FastAPI) untuk load awal instan (FCP <100ms).
  - **Tampilan**: Tailwind CSS (CDN standalone atau micro-compiled file tunggal).
  - **Gerakan**: Alpine.js (state lokal reaktif tanpa bundle build).
  - **Arus Data**: HTMX (AJAX HTML swap langsung dari server tanpa menulis custom fetch API).
  - **Simbol**: Lucide inline SVG (nol dependensi font icon atau emoji murahan).

---

## 2. Struktur Dasar Aplikasi Single-File (`app.py`)

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
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

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
    
    # Kembalikan partial HTML instan untuk di-swap oleh HTMX
    return HTMLResponse(f"""
        <li class="p-3 bg-slate-900 border border-slate-800 rounded-lg flex justify-between">
            <span>{title}</span>
            <span class="text-xs text-emerald-400">Baru</span>
        </li>
    """)
```

---

## 3. Template HTML Bersih (`templates/index.html`)

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zero-Bloat Console</title>
    <!-- Tailwind CSS Standalone & Alpine.js -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans antialiased">
    <div class="max-w-2xl mx-auto space-y-6">
        <!-- Form Input Instan via HTMX -->
        <form hx-post="/items/add" hx-target="#item-list" hx-swap="afterbegin" class="flex gap-2">
            <input type="text" name="title" placeholder="Catat order servis baru..." required
                   class="flex-1 bg-slate-900 border border-slate-800 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-cyan-500">
            <button type="submit" class="bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-lg text-sm font-medium transition">
                Tambah
            </button>
        </form>

        <!-- Daftar Reaktif -->
        <ul id="item-list" class="space-y-2">
            {% for item in items %}
            <li class="p-3 bg-slate-900 border border-slate-800 rounded-lg flex justify-between">
                <span>{{ item.title }}</span>
                <span class="text-xs text-slate-500">#{{ item.id }}</span>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```
