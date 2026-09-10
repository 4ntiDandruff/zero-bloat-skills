---
name: telegram-ops-control-skill
description: "Telegram bot infrastructure for remote server management: interactive inline keyboard buttons, Wake-on-LAN (WOL) triggers, HTML safe parsing, proactive resource alerting, and infinity polling auto-reconnect."
---

# Telegram Ops Control Bot Skill

Architectural pattern for monitoring and controlling workbench machines, edge servers, and homelab nodes directly from a mobile device via interactive Telegram inline keyboard buttons, fortified against API parser crashes and network disconnection loops.

---

## 1. Remote Trigger Buttons & Wake-On-LAN (WOL)

Control remote hardware without requiring an SSH terminal session on a laptop:

```python
import html
import subprocess
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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
        # Enforce HTML escaping to prevent Telegram API 400 Bad Request
        safe_out = html.escape(out)
        bot.send_message(
            call.message.chat.id, 
            f"<b>Memory Health State:</b>\n<pre>{safe_out}</pre>", 
            parse_mode="HTML"
        )
```

---

## 2. Authentication Gate & Rate Limiting

Mitigate security exposure if bot tokens leak:

```python
AUTHORIZED_USERS = {123456789}  # Replace with verified operator Telegram ID

def auth_required(func):
    def wrapper(message, *args, **kwargs):
        if message.from_user.id not in AUTHORIZED_USERS:
            bot.reply_to(message, "[!] Access denied. Incident logged.")
            return
        return func(message, *args, **kwargs)
    return wrapper
```

---

## 3. Resilient Long-Polling Guard (Infinity Polling)

Never use bare `bot.polling()` in production; transient Wi-Fi drops or DNS timeouts will terminate the Python script:

```python
import time
import logging

logging.basicConfig(level=logging.INFO)

def run_resilient_bot():
    while True:
        try:
            logging.info("[*] Starting Telegram bot infinity polling...")
            bot.infinity_polling(
                timeout=20,
                long_polling_timeout=10,
                logger_level=logging.WARNING
            )
        except Exception as e:
            logging.error(f"[!] Polling connection crashed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    run_resilient_bot()
```

---

## 4. Safe Formatting Rule: HTML > Markdown

- Telegram's MarkdownV2 parser throws fatal HTTP 400 exceptions if characters like `_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``, `>`, `#`, `+`, `-`, `=`, `|`, `{`, `}`, `.`, or `!` are unescaped.
- **Mandatory Standard**: Always use `parse_mode="HTML"` combined with Python's built-in `html.escape()` for terminal outputs, log snippets, and exception traces.
