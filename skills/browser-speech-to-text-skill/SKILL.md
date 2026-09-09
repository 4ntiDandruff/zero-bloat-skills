---
name: browser-speech-to-text-skill
description: "Zero-server-cost browser-native Speech-to-Text (STT) architecture: Web Speech API, Android PWA microphone permission bridge, dynamic visualViewport soft-keyboard avoidance, and spoken Indonesian number parsing."
---

# Browser Speech-to-Text (STT) Skill

Zero-server-cost, near-zero latency Speech-to-Text architecture using native browser APIs (`SpeechRecognition`). Completely eliminates the CPU, RAM, and GPU hosting overhead of Whisper or cloud speech APIs for mobile web applications.

Battle-tested in the **Kas Megapass** daily bookkeeping platform (`kas.megapass.web.id`).

---

## 1. Architectural Principles

* **0 MB Server RAM**: Processing happens on the client browser / OS speech engine. The server receives only lightweight normalized text payloads.
* **Instant Start (<100ms)**: Eliminates file buffering, audio encoding/decoding, and multi-megabyte audio uploads over cellular connections.
* **Native Indonesian Acoustic Model (`id-ID`)**: Built-in system recognition handles local accents and dialects natively.
* **Graceful Degradation**: Seamless fallback to standard text input when mic permissions are blocked or browser lacks API support.

---

## 2. Client-Side Web Speech Implementation

### The Android PWA Permission Trap
On Android PWAs, calling `SpeechRecognition.start()` directly often fails silently with a `not-allowed` error. The bulletproof workaround is to trigger a lightweight `navigator.mediaDevices.getUserMedia({ audio: true })` call first to open the native OS permission prompt, immediately release the audio track, and then start `SpeechRecognition`:

```javascript
// static/js/voice-input.js
(function() {
  var activeRec = null;

  function micSupported() {
    return "webkitSpeechRecognition" in window || "SpeechRecognition" in window;
  }

  function micFallback() {
    var label = document.getElementById("voice-label");
    if (label) label.textContent = "Mikrofon tidak aktif, silakan ketik manual";
    var ring = document.getElementById("voice-ring");
    if (ring) ring.classList.remove("animate-pulse");
    var recBtn = document.getElementById("voice-rec-btn");
    if (recBtn) recBtn.classList.remove("recording");
    var textInput = document.getElementById("voice-fallback-input");
    if (textInput) textInput.focus();
  }

  function startListening(onResultCallback) {
    if (!micSupported()) { micFallback(); return; }

    // Toggle stop if already recording
    if (activeRec) {
      try { activeRec.abort(); } catch (_) {}
      activeRec = null;
      return;
    }

    var label = document.getElementById("voice-label");
    var transcript = document.getElementById("voice-transcript");
    var ring = document.getElementById("voice-ring");
    var recBtn = document.getElementById("voice-rec-btn");

    function runRecognition() {
      var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
      var rec = new SR();
      rec.lang = "id-ID";
      rec.continuous = false;
      rec.interimResults = true;
      activeRec = rec;

      var fullText = "";

      rec.onstart = function() {
        if (label) label.textContent = "Mendengarkan...";
        if (ring) ring.classList.add("animate-pulse");
        if (recBtn) recBtn.classList.add("recording");
      };

      rec.onresult = function(e) {
        var str = "";
        for (var i = 0; i < e.results.length; i++) {
          str += e.results[i][0].transcript;
        }
        fullText = str;
        if (transcript) transcript.textContent = str.trim();
      };

      rec.onend = function() {
        activeRec = null;
        if (ring) ring.classList.remove("animate-pulse");
        if (recBtn) recBtn.classList.remove("recording");
        var finalClean = fullText.trim();
        if (finalClean) {
          if (label) label.textContent = "Memproses...";
          onResultCallback(finalClean);
        } else {
          if (label) label.textContent = "Suara tidak terdengar, coba lagi";
        }
      };

      rec.onerror = function(e) {
        activeRec = null;
        if (e.error !== "aborted") {
          micFallback();
        }
      };

      try { rec.start(); } catch (_) { micFallback(); }
    }

    // Permission Bridge: pre-flight request for Android PWA / TWA
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function(stream) {
          stream.getTracks().forEach(function(t) { t.stop(); });
          runRecognition();
        })
        .catch(function() { micFallback(); });
    } else {
      runRecognition();
    }
  }

  window.VoiceSTT = { start: startListening, supported: micSupported };
})();
```

---

## 3. Dynamic Soft-Keyboard Viewport Avoidance

On mobile browsers, opening a bottom sheet alongside a virtual keyboard causes viewport occlusion. By attaching to `window.visualViewport`, the voice sheet dynamically hovers right above the keyboard without layout shifting:

```javascript
function setupViewportLift(sheetSelector, panelSelector) {
  if (!window.visualViewport) return;
  var panel = document.querySelector(panelSelector);
  if (!panel) return;

  var onResize = function() {
    var sheet = document.querySelector(sheetSelector);
    if (!sheet || sheet.style.display === "none") return;
    
    // Keyboard height = layout viewport - visual viewport
    var kbHeight = window.innerHeight - window.visualViewport.height;
    panel.style.transform = kbHeight > 50 ? "translateY(-" + kbHeight + "px)" : "";
  };

  window.visualViewport.addEventListener("resize", onResize);
  window.visualViewport.addEventListener("scroll", onResize);
}

// Attach during initialization
setupViewportLift("#voice-sheet", "#voice-panel");
```

---

## 4. Spoken Indonesian Number Parser (Verbal-to-Integer)

Speech recognition transcribes numbers as words (e.g. *"lima puluh ribu"* instead of *50000*). This deterministic Python parser translates spoken Indonesian numbers into numeric values without calling an LLM:

```python
# verbal_numbers.py
import re

_SATUAN = {
    "nol": 0, "satu": 1, "dua": 2, "tiga": 3, "empat": 4,
    "lima": 5, "enam": 6, "tujuh": 7, "delapan": 8, "sembilan": 9,
}

_SINGLE = {
    "sepuluh": 10, "sebelas": 11,
    "seratus": 100, "seribu": 1_000,
    "sejuta": 1_000_000, "semiliar": 1_000_000_000, "semilyar": 1_000_000_000,
}

_SCALE = {"ribu": 1_000, "juta": 1_000_000, "miliar": 1_000_000_000, "milyar": 1_000_000_000}

_AMOUNT_MARKER = frozenset({
    "belas", "puluh", "ratus", "ribu", "juta", "miliar", "milyar",
    "sepuluh", "sebelas", "seratus", "seribu", "sejuta", "semiliar", "semilyar"
})

_NUM_WORDS = frozenset(_SATUAN) | frozenset(_SINGLE) | frozenset(_SCALE) | frozenset({"belas", "puluh", "ratus"})


def parse_terbilang(words: list[str]) -> int | None:
    """Parses verbal Indonesian number words into an integer.
    Rejects bare digits (e.g. 'beli dua bensin' returns None).
    """
    if not any(w in _AMOUNT_MARKER for w in words):
        return None

    total = 0
    current = 0
    i, n = 0, len(words)

    while i < n:
        w = words[i]
        if w in _SINGLE:
            v = _SINGLE[w]
            if v >= 1000:
                total += (current if current else 1) * v
                current = 0
            else:
                current += v
            i += 1
        elif w in _SATUAN:
            v = _SATUAN[w]
            nxt = words[i + 1] if i + 1 < n else ""
            if nxt == "ratus":
                current += v * 100
                i += 2
            elif nxt == "puluh":
                current += v * 10
                i += 2
            elif nxt == "belas":
                current += v + 10
                i += 2
            else:
                current += v
                i += 1
        elif w in _SCALE:
            total += (current if current else 1) * _SCALE[w]
            current = 0
            i += 1
        else:
            return None

    return total + current


def extract_spoken_nominal(text: str) -> int | None:
    """Extracts first valid verbal spoken number sequence from speech transcripts."""
    tokens = text.lower().split()
    i = 0
    while i < len(tokens):
        if tokens[i] not in _NUM_WORDS:
            i += 1
            continue
        j = i
        while j < len(tokens) and tokens[j] in _NUM_WORDS:
            j += 1
        val = parse_terbilang(tokens[i:j])
        if val is not None:
            return val
        i = j
    return None
```
