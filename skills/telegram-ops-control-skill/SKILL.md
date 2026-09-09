---
name: telegram-ops-control-skill
description: "Infrastruktur bot Telegram untuk kendali remote server meja servis: tombol inline SSH, trigger saklar Wake-on-LAN (WOL), alerting beban sistem, dan manajemen proses PM2."
---

# Telegram Ops Control Bot Skill

Pola arsitektur bot Telegram untuk memantau dan mengendalikan armada PC meja servis, homelab, dan server edge langsung dari smartphone melalui tombol inline keyboard interaktif.

---

## 1. Arsitektur Tombol Saklar & Wake-On-LAN (WOL)

Teknisi tidak perlu membuka laptop untuk menyalakan PC kerja atau merestart service yang macet:

```python
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import subprocess

bot = TeleBot("TOKEN_PLACEHOLDER")

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("[⚡] Bangunkan Ryzen (WOL)", callback_data="wol_ryzen"),
        InlineKeyboardButton("[🔄] Restart AdGuard", callback_data="restart_adguard"),
        InlineKeyboardButton("[📊] Cek Beban RAM", callback_data="check_ram"),
        InlineKeyboardButton("[🛡️] Status Cloudflare", callback_data="check_cf")
    )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "wol_ryzen":
        # Kirim magic packet Wake-on-LAN ke kartu jaringan target
        subprocess.run(["wakeonlan", "AA:BB:CC:DD:EE:FF"], check=True)
        bot.answer_callback_query(call.id, "Magic packet WOL terkirim!")
    elif call.data == "check_ram":
        out = subprocess.check_output(["free", "-h"]).decode()
        bot.send_message(call.message.chat.id, f"Status Memori:\n```\n{out}```", parse_mode="Markdown")
```

---

## 2. Sekring Keamanan (Whitelist Chat ID & Rate Limiting)

Untuk mencegah akses liar jika token bot bocor:
```python
AUTHORIZED_USERS = {123456789} # Ganti dengan ID telegram pemilik asli

def auth_required(func):
    def wrapper(message, *args, **kwargs):
        if message.from_user.id not in AUTHORIZED_USERS:
            bot.reply_to(message, "[!] Akses ditolak. Insiden dicatat.")
            return
        return func(message, *args, **kwargs)
    return wrapper
```

---

## 3. Monitoring Proaktif Latar Belakang (Watchdog Alert)

Bot berjalan sebagai thread daemon yang secara periodik mengecek kesehatan sirkuit:
- Disk space < 10% -> Kirim pesan darurat ke Telegram.
- RAM usage > 90% selama 5 menit berturut-turut -> Kirim notifikasi peringatan.
- Status service PM2 error -> Kirim ringkasan error log 20 baris terakhir.
