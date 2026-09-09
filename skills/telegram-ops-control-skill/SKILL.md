---
name: telegram-ops-control-skill
description: "Telegram bot infrastructure for remote server management: interactive inline keyboard buttons, Wake-on-LAN (WOL) triggers, proactive resource alerting, and PM2 process monitoring."
---

# Telegram Ops Control Bot Skill

Architectural pattern for monitoring and controlling workbench machines, edge servers, and homelab nodes directly from a mobile device via interactive Telegram inline keyboard buttons.

---

## 1. Remote Trigger Buttons & Wake-On-LAN (WOL)

Control remote hardware without requiring a laptop terminal session:

```python
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import subprocess

bot = TeleBot("TOKEN_PLACEHOLDER")

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("[⚡] Wake Workbench PC (WOL)", callback_data="wol_pc"),
        InlineKeyboardButton("[🔄] Restart DNS Service", callback_data="restart_dns"),
        InlineKeyboardButton("[📊] Memory Health Check", callback_data="check_ram"),
        InlineKeyboardButton("[🛡️] Cloudflare Tunnel Status", callback_data="check_cf")
    )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "wol_pc":
        subprocess.run(["wakeonlan", "AA:BB:CC:DD:EE:FF"], check=True)
        bot.answer_callback_query(call.id, "WOL magic packet dispatched.")
    elif call.data == "check_ram":
        out = subprocess.check_output(["free", "-h"]).decode()
        bot.send_message(call.message.chat.id, f"Memory State:\n```\n{out}```", parse_mode="Markdown")
```

---

## 2. Authentication Gate & Rate Limiting

Mitigate security exposure if bot tokens leak:

```python
AUTHORIZED_USERS = {123456789} # Replace with verified operator Telegram ID

def auth_required(func):
    def wrapper(message, *args, **kwargs):
        if message.from_user.id not in AUTHORIZED_USERS:
            bot.reply_to(message, "[!] Access denied. Incident logged.")
            return
        return func(message, *args, **kwargs)
    return wrapper
```

---

## 3. Proactive Health Watchdog Loop

Runs as an unprivileged background daemon checking system telemetry:
- Available storage < 10% -> Immediate urgent alert dispatched.
- Memory usage > 90% sustained for 5 consecutive minutes -> Warning alert dispatched.
- Monitored process crashes -> Tail 20 lines of diagnostic error logs to chat.
