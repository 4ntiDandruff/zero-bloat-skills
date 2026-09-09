import sqlite3
import os

DB_PATH = os.environ.get("STARTER_DB_PATH", "app.db")

def init_db(db_path: str = None):
    if db_path is None:
        db_path = os.environ.get("STARTER_DB_PATH", "app.db")
    conn = get_connection(db_path)
    conn.close()

def get_connection(db_path: str = None) -> sqlite3.Connection:
    if db_path is None:
        db_path = os.environ.get("STARTER_DB_PATH", "app.db")
    conn = sqlite3.connect(db_path, timeout=20.0)
    conn.row_factory = sqlite3.Row
    
    # Pragma wajib WAL mode & synchronous NORMAL
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA cache_size = -32000;")
    conn.execute("PRAGMA temp_store = MEMORY;")
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS service_tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                device_model TEXT NOT NULL,
                issue_description TEXT NOT NULL,
                status TEXT DEFAULT 'PENGECEKAN',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
    return conn
