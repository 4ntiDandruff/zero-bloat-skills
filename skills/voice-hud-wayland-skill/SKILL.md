---
name: voice-hud-wayland-skill
description: "Pola arsitektur Voice-to-Text HUD hands-free untuk teknisi meja servis di Linux Wayland: local streaming STT via faster-whisper, blur overlay KWin, dan post-transcript LLM polishing."
---

# Voice HUD Wayland Skill

Panduan integrasi HUD pendiktean suara (speech-to-text) hands-free untuk teknisi saat kedua tangan memegang solder, pinset micro-soldering, atau probe multimeter.

---

## 1. Arsitektur Low-Latency: Local Whisper + LLM Polishing

```
[ Mikrofon USB / Headset ]
          ↓
[ PyAudio / SoundDevice (VAD: Voice Activity Detection Silero) ]
          ↓
[ faster-whisper (CTranslate2 Model INT8 di CPU Lokal - Latensi <200ms) ]
          ↓
[ Teks Mentah (Raw Transcript) ]
          ↓
[ LLM Post-Processor (Perbaikan istilah teknis meja servis: MOSFET, VCC, ALW) ]
          ↓
[ Wayland KWin HUD Overlay (Tampil mengambang) & Auto-Type ke Window Aktif ]
```

---

## 2. Wayland Overlay Transparan (PyQt6 / Layer-Shell)

Pada sesi Wayland (KDE Plasma 6 / GNOME), aplikasi dilarang meletakkan window secara absolut sembarangan. Gunakan protokol layer-shell atau window flag khusus:

```python
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
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
        
        # Style kartu gelap dengan radius dan efek kaca
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

## 3. Post-Processing Istilah Teknis Meja Servis

Whisper umum sering salah mengeja akronim elektronika (misal: "mosfet" terbaca "most fat", "vcc" terbaca "visisi"). Pasang kamus mapping ringan sebelum teks diketikkan:

```python
TERM_MAP = {
    "most fat": "MOSFET",
    "visisi": "VCC",
    "pi si h": "PCH",
    "b ios": "BIOS",
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

## 4. Pengetikan Otomatis ke Window Aktif di Wayland

Gunakan utilitas `ydotool` atau `wtype` (bukan `xdotool` yang gagal di Wayland):
```bash
wtype "$CLEANED_TEXT"
```
