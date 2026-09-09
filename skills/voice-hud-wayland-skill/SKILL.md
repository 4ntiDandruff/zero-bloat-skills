---
name: voice-hud-wayland-skill
description: "Hands-free Voice-to-Text HUD architecture for workbench technicians under Linux Wayland: local faster-whisper streaming, KWin overlay glassmorphism, and post-transcript LLM polishing."
---

# Voice HUD Wayland Skill

Design pattern for a hands-free speech-to-text heads-up display (HUD) allowing technicians to dictate repair notes while hands are occupied holding soldering irons, tweezers, or multimeter probes.

---

## 1. Low-Latency Pipeline: Local Whisper + LLM Polishing

```
[ Bench USB Microphone / Headset ]
                ↓
[ PyAudio / SoundDevice (Silero VAD: Voice Activity Detection) ]
                ↓
[ faster-whisper (CTranslate2 INT8 Model on Local CPU - Latency <200ms) ]
                ↓
[ Raw Text Stream ]
                ↓
[ LLM Post-Processor (Repair Electronics Jargon: MOSFET, VCC, ALW) ]
                ↓
[ Wayland KWin HUD Overlay & Direct Keystroke Injection ]
```

---

## 2. Floating Transparent Overlay (PyQt6 / Wayland)

Under Wayland sessions (KDE Plasma 6 / GNOME), windows cannot be arbitrarily positioned without protocol flags:

```python
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt

class WaylandHud(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setStyleSheet("""
            background-color: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: #f1f5f9;
            padding: 12px;
            font-family: monospace;
        """)
```

---

## 3. Hardware Jargon Normalization

General acoustic models frequently misinterpret hardware electronics acronyms. Apply deterministic translation maps:

```python
TERM_MAP = {
    "most fat": "MOSFET",
    "visisi": "VCC",
    "pi si h": "PCH",
    "b bios": "BIOS",
    "es i o": "Super I/O",
    "ground": "GND",
}

def sanitize_technical_transcript(raw_text: str) -> str:
    cleaned = raw_text
    for slang, formal in TERM_MAP.items():
        cleaned = cleaned.replace(slang, formal)
    return cleaned
```

---

## 4. Keystroke Emulation Under Wayland

Use native Wayland tools `ydotool` or `wtype` (avoid `xdotool` which fails under Wayland compositors):
```bash
wtype "$CLEANED_TEXT"
```
