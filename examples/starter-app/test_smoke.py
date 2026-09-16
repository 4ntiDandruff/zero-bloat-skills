import sys
import os
import tempfile

# Gunakan database sementara untuk pengujian
test_dir = tempfile.mkdtemp()
os.environ["STARTER_DB_PATH"] = os.path.join(test_dir, "test_app.db")

from fastapi.testclient import TestClient
from main import app
from db import get_connection

def run_smoke_test():
    print("[*] Menjalankan smoke test starter app...")
    client = TestClient(app)
    
    # 1. Uji endpoint /health
    res = client.get("/health")
    assert res.status_code == 200, f"Health check gagal: {res.status_code}"
    data = res.json()
    assert data["journal_mode"].lower() == "wal", f"Journal mode bukan WAL: {data['journal_mode']}"
    print("[+] Test 1 PASS: /health aktif dan mode SQLite WAL terverifikasi.")
    
    # 2. Uji endpoint index /
    res_index = client.get("/")
    assert res_index.status_code == 200, f"Index check gagal: {res_index.status_code}"
    assert "MEGAPASS INTRA SOLUSINDO" in res_index.text, "Branding Megapass tidak ditemukan di index HTML"
    print("[+] Test 2 PASS: GET / render HTML berhasil (FCP instant).")
    
    # 3. Uji tambah tiket via POST /tickets/add
    payload = {
        "customer_name": "Pak Joko Santoso",
        "device_model": "Asus ROG GL553VD",
        "issue_description": "Short 19V VIN rail, kapasitor PC102 terbakar"
    }
    res_post = client.post("/tickets/add", data=payload)
    assert res_post.status_code == 200, f"Insert ticket gagal: {res_post.status_code}"
    assert "Pak Joko Santoso" in res_post.text, "Nama pelanggan tidak ada di respons HTMX"
    assert "Asus ROG GL553VD" in res_post.text, "Model perangkat tidak ada di respons HTMX"
    print("[+] Test 3 PASS: POST /tickets/add berhasil swap baris HTMX baru.")
    
    # 4. Verifikasi persistensi dan pragma di file database SQLite
    conn = get_connection(os.environ["STARTER_DB_PATH"])
    row = conn.execute("SELECT * FROM service_tickets WHERE customer_name = 'Pak Joko Santoso'").fetchone()
    assert row is not None, "Data tidak ditemukan di database!"
    assert row["device_model"] == "Asus ROG GL553VD"
    
    sync_mode = conn.execute("PRAGMA synchronous;").fetchone()[0]
    busy_to = conn.execute("PRAGMA busy_timeout;").fetchone()[0]
    fk = conn.execute("PRAGMA foreign_keys;").fetchone()[0]
    assert sync_mode == 1, f"Synchronous mode bukan NORMAL (1): {sync_mode}"
    assert busy_to == 5000, f"Busy timeout bukan 5000: {busy_to}"
    assert fk == 1, f"Foreign keys bukan ON: {fk}"
    conn.close()
    print("[+] Test 4 PASS: Data terverifikasi tersimpan atomik di SQLite WAL (synchronous=NORMAL, busy_timeout=5000, fk=ON).")
    
    print("\n[+] SELURUH SMOKE TEST LOLOS DENGAN EXIT CODE 0.")
    return 0

if __name__ == "__main__":
    sys.exit(run_smoke_test())
