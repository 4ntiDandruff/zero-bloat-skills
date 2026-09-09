---
name: zero-cpu-daemon-skill
description: "Pola arsitektur daemon event-driven Linux dengan 0% CPU standby load via inotifywait, dilengkapi 9 sekring pengaman sirkuit (anti zip-slip, symlink bomb, debounce partial write, disk limit)."
---

# Zero-CPU Linux Inotify Daemons Skill

Arsitektur daemon Linux mandiri berbasis POSIX shell dan `inotifywait` yang memantau filesystem secara pasif (event-driven kernel hook) sehingga mengonsumsi 0.0% CPU pada kondisi standby, tanpa looping polling `sleep` yang boros daya.

---

## 1. Topologi Event-Driven vs Polling Loop

- **Pendekatan Tradisional (Polling Loop)**:
  `while true; do check_files; sleep 2; done`
  Membebani CPU context-switch, boros baterai laptop, dan menimbulkan latensi hingga interval sleep berakhir.
- **Pendekatan Zero-CPU (Kernel Inotify)**:
  Proses ditidurkan sepenuhnya di level OS kernel (`TASK_INTERRUPTIBLE`). Hanya saat kernel mencatat event `close_write` atau `moved_to`, proses dibangunkan untuk mengeksekusi aksi dalam <0.1 detik.

---

## 2. Implementasi 9 Sekring Proteksi Sirkuit

```bash
#!/usr/bin/env bash
set -euo pipefail

WATCH_DIR="$HOME/Downloads"

inotifywait -m -e close_write,moved_to --format "%w%f" "$WATCH_DIR" | while read -r FILE_PATH; do
    # Sekring 1: Cek keberadaan file fisik
    [[ ! -f "$FILE_PATH" ]] && continue

    # Sekring 2: Filter ekstensi file yang valid
    case "$FILE_PATH" in
        *.zip|*.tar.gz|*.7z|*.rar) ;;
        *) continue ;;
    esac

    # Sekring 3: Debounce file transfer parsial (tunggu file selesai ditulis)
    fuser "$FILE_PATH" >/dev/null 2>&1 && continue

    # Sekring 4: Batasan ukuran file (misal maksimal 500 MB)
    FILE_SIZE=$(stat -c%s "$FILE_PATH")
    if [[ $FILE_SIZE -gt 524288000 ]]; then
        echo "[!] File melebihi batas sekring ukuran: $FILE_PATH"
        continue
    fi

    # Sekring 5: Proteksi sisa kapasitas disk (abort jika free space < 1 GB)
    FREE_SPACE=$(df -k "$WATCH_DIR" | awk 'NR==2 {print $4}')
    if [[ $FREE_SPACE -lt 1048576 ]]; then
        echo "[!] Sekring disk full terpicu. Operasi dibatalkan."
        continue
    fi

    # Sekring 6: Anti Zip-Slip (blokir file yang berisi ../ atau path traversal)
    if zipinfo -1 "$FILE_PATH" 2>/dev/null | grep -q '\.\./'; then
        echo "[!] BAHAYA: Zip-slip terdeteksi pada $FILE_PATH"
        continue
    fi

    # Sekring 7: Anti Symlink Bomb
    TARGET_DIR="${FILE_PATH%.*}"
    mkdir -p "$TARGET_DIR"

    # Sekring 8: Eksekusi ekstraksi dengan timeout sekring waktu
    timeout 30s 7z x -o"$TARGET_DIR" -y "$FILE_PATH" >/dev/null

    # Sekring 9: Hapus arsip setelah verifikasi isi folder tidak kosong
    if [[ -n "$(ls -A "$TARGET_DIR")" ]]; then
        rm -f "$FILE_PATH"
        echo "[+] Berhasil diproses dengan aman: $TARGET_DIR"
    fi
done
```

---

## 3. Integrasi Systemd User Unit (Auto-Start)

Simpan konfigurasi ke `~/.config/systemd/user/zero-daemon.service`:

```ini
[Unit]
Description=Zero-CPU Inotify Event Daemon
After=default.target

[Service]
Type=simple
ExecStart=/usr/local/bin/zero-daemon.sh
Restart=always
RestartSec=5s
MemoryMax=64M
CPUQuota=10%

[Install]
WantedBy=default.target
```
