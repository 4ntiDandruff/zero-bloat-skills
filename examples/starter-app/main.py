from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import os
from db import init_db, get_connection

app = FastAPI(title="Zero-Bloat Meja Servis Starter")

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

init_db()

@app.get("/health", response_class=JSONResponse)
def health():
    conn = get_connection()
    wal_mode = conn.execute("PRAGMA journal_mode;").fetchone()[0]
    conn.close()
    return {"status": "ok", "journal_mode": wal_mode, "architecture": "zero-bloat-single-worker"}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = get_connection()
    tickets = conn.execute("SELECT * FROM service_tickets ORDER BY id DESC LIMIT 50").fetchall()
    conn.close()
    return templates.TemplateResponse(request=request, name="index.html", context={"tickets": tickets})

@app.post("/tickets/add", response_class=HTMLResponse)
def add_ticket(
    customer_name: str = Form(...),
    device_model: str = Form(...),
    issue_description: str = Form(...)
):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO service_tickets (customer_name, device_model, issue_description) VALUES (?, ?, ?)",
        (customer_name, device_model, issue_description)
    )
    new_id = cur.lastrowid
    conn.commit()
    conn.close()

    # Kembalikan partial HTML komponen baris baru untuk di-swap instan oleh HTMX
    return HTMLResponse(f"""
        <tr class="border-b border-slate-800/60 hover:bg-slate-900/40 transition">
            <td class="px-4 py-3 font-mono text-xs text-cyan-400">#{new_id}</td>
            <td class="px-4 py-3 font-medium text-slate-200">{customer_name}</td>
            <td class="px-4 py-3 text-slate-400">{device_model}</td>
            <td class="px-4 py-3 text-slate-300 text-sm">{issue_description}</td>
            <td class="px-4 py-3">
                <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-amber-950/60 text-amber-400 border border-amber-800/40">
                    PENGECEKAN
                </span>
            </td>
        </tr>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8099, workers=1)
