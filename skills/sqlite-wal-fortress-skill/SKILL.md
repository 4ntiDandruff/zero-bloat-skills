---
name: sqlite-wal-fortress-skill
description: "Konfigurasi SQLite anti-korup saat pemadaman listrik mendadak di server ruko: WAL mode, PRAGMA synchronous=NORMAL, auto-checkpoint, dan atomic online hot-backup."
---

# SQLite WAL Fortress Skill

SOP konfigurasi dan pemeliharaan SQLite untuk sistem operasional meja servis dan server ruko agar kebal terhadap pemadaman listrik mendadak, konkurensi pembacaan tinggi, serta backup tanpa henti layanan (zero-downtime).

---

## 1. Masalah Database Ruko Tanpa WAL

Pada mode rollback journal default (`PRAGMA journal_mode = DELETE`):
- Proses tulis mengunci (*exclusive lock*) seluruh database sehingga pembacaan (*readers*) terblokir.
- Pemadaman listrik mendadak saat file rollback journal sedang ditulis dapat menyebabkan header database korup (*malformed image*).

---

## 2. Inisialisasi PRAGMA Wajib Anti-Mati Lampu

Setiap koneksi database dibuka, selalu eksekusi parameter sirkuit berikut:

```python
import sqlite3

def get_db_connection(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, timeout=20.0)
    conn.row_factory = sqlite3.Row
    
    # 1. Aktifkan mode WAL (Write-Ahead Logging)
    conn.execute("PRAGMA journal_mode = WAL;")
    
    # 2. Synchronous NORMAL (Aman dari korupsi saat mati lampu + 10x lebih cepat)
    conn.execute("PRAGMA synchronous = NORMAL;")
    
    # 3. Alokasikan cache memori (misal -64000 = 64 MB RAM)
    conn.execute("PRAGMA cache_size = -64000;")
    
    # 4. Simpan file sementara di RAM
    conn.execute("PRAGMA temp_store = MEMORY;")
    
    # 5. Pasang batas ukuran file WAL sebelum auto-checkpoint (misal 1000 halaman ~ 4MB)
    conn.execute("PRAGMA wal_autocheckpoint = 1000;")
    
    # 6. Aktifkan foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON;")
    
    return conn
```

---

## 3. Atomic Online Hot-Backup (Zero-Downtime)

DILARANG menggunakan `cp database.db backup.db` saat aplikasi sedang berjalan (akan menghasilkan backup korup jika terjadi penulisan pada saat bersamaan).

Gunakan SQLite Online Backup API bawaan Python:

```python
import sqlite3
import shutil
import time

def perform_atomic_backup(source_db: str, backup_dir: str):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    target_file = f"{backup_dir}/backup_{timestamp}.db"
    
    src = sqlite3.connect(source_db)
    dst = sqlite3.connect(target_file)
    
    with dst:
        # Salin halaman secara bertahap tanpa mengunci operasi tulis aplikasi
        src.backup(dst, pages=100)
        
    dst.close()
    src.close()
    print(f"[+] Hot backup sukses: {target_file}")
```

---

## 4. SOP Pemulihan Database Korup (Emergency Recovery)

Jika database mengalami anomali akibat crash kernel:

```bash
# 1. Uji integritas
sqlite3 database.db "PRAGMA integrity_check;"

# 2. Dump darurat ke format SQL mentah
sqlite3 database.db ".recover" | sqlite3 recovered.db

# 3. Verifikasi ulang file hasil pemulihan
sqlite3 recovered.db "PRAGMA integrity_check;"
```
