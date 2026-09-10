---
name: sqlite-wal-fortress-skill
description: "Fortified SQLite configuration for sudden power outages in workshop servers: WAL mode, PRAGMA synchronous=NORMAL, busy_timeout tuning, atomic online hot-backups, and single-command .recover triage."
---

# SQLite WAL Fortress Skill

Standard configuration and operational procedures for running SQLite on workshop servers and bench workstations, engineered to remain invulnerable to sudden electrical power loss, high concurrency lock contention, and non-blocking online hot-backups.

---

## 1. Risks of Default Rollback Journaling

Under default journaling (`PRAGMA journal_mode = DELETE`):
- Active write operations lock the entire database exclusively, blocking all concurrent readers.
- Sudden electrical blackouts occurring mid-write risk leaving partial journal locks or corrupting database page headers.

---

## 2. Mandatory Circuit PRAGMAs for Power Resilience & Lock Contention

Execute these pragmas immediately whenever a database connection opens:

```python
import sqlite3

def get_db_connection(db_path: str) -> sqlite3.Connection:
    # Set generous connection timeout to handle lock contention gracefully
    conn = sqlite3.connect(db_path, timeout=30.0)
    conn.row_factory = sqlite3.Row
    
    # 1. Enable Write-Ahead Logging (readers never block writers)
    conn.execute("PRAGMA journal_mode = WAL;")
    
    # 2. Synchronous NORMAL (resilient to sudden power cutoffs & 10x faster)
    conn.execute("PRAGMA synchronous = NORMAL;")
    
    # 3. Busy Timeout (wait up to 5000ms before raising OperationalError: database is locked)
    conn.execute("PRAGMA busy_timeout = 5000;")
    
    # 4. Allocate in-memory page cache (-64000 = 64 MB RAM)
    conn.execute("PRAGMA cache_size = -64000;")
    
    # 5. Direct temporary storage to RAM
    conn.execute("PRAGMA temp_store = MEMORY;")
    
    # 6. Checkpoint WAL log automatically every 1000 pages (~4MB)
    conn.execute("PRAGMA wal_autocheckpoint = 1000;")
    
    # 7. Enforce relational foreign keys
    conn.execute("PRAGMA foreign_keys = ON;")
    
    return conn
```

---

## 3. Atomic Online Hot-Backup (Zero-Downtime)

NEVER use `cp database.db backup.db` on active databases; concurrent writes will produce torn, unrecoverable images.

Leverage Python's built-in SQLite Online Backup API:

```python
import sqlite3
import time

def perform_atomic_backup(source_db: str, backup_dir: str):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    target_file = f"{backup_dir}/backup_{timestamp}.db"
    
    src = sqlite3.connect(source_db)
    dst = sqlite3.connect(target_file)
    
    with dst:
        # Incrementally copy pages without locking application writes
        src.backup(dst, pages=100)
        
    dst.close()
    src.close()
    print(f"[+] Hot backup completed safely: {target_file}")
```

---

## 4. Emergency Database Recovery (Corrupted Database Salvage)

When a sudden power loss leaves a database with `database disk image is malformed`:

### Step 1: Force WAL Checkpoint Flush
```bash
sqlite3 damaged.db "PRAGMA wal_checkpoint(TRUNCATE);"
```

### Step 2: Single-Command Stream Recovery
The `.recover` command parses uncorrupted B-tree pages even if root pointers are damaged:
```bash
sqlite3 damaged.db ".recover" | sqlite3 recovered.db
```

### Step 3: Integrity Verification
```bash
sqlite3 recovered.db "PRAGMA integrity_check;"
# Output must return: ok
```
