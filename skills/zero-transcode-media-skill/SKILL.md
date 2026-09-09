---
name: zero-transcode-media-skill
description: "Arsitektur media streaming CCTV di hardware terbatas (edge STB/i3) tanpa beban transcoding CPU: pass-through RTSP ke WebRTC/HLS via go2rtc dan memory limit <30MB."
---

# Zero-Transcode Edge Media Skill

Pola arsitektur streaming video CCTV real-time untuk perangkat edge berdaya rendah (STB Android Armbian, Raspberry Pi, atau PC lawas) tanpa membebani CPU dengan proses re-encoding/transcoding.

---

## 1. Masalah Transcoding Video di Hardware Terbatas

- Memproses ulang stream video H.264/H.265 via FFmpeg CPU software decoding mengonsumsi 80-100% kapasitas prosesor pada mesin non-GPU.
- Akibatnya: suhu CPU melonjak, frame drop, dan perangkat hang dalam beberapa jam.

---

## 2. Solusi Sirkuit: Pure Pass-Through Streaming (go2rtc)

Gunakan engine media biner native Go (`go2rtc`) yang hanya mengalirkan paket RTP tanpa mendekode ulang frame video:

### Konfigurasi `go2rtc.yaml`:
```yaml
streams:
  kamera_depan:
    - rtsp://admin:pass@192.168.1.100:554/stream1
  kamera_servis:
    - rtsp://admin:pass@192.168.1.101:554/live/ch0

api:
  listen: ":1984"

webrtc:
  listen: ":8555"
```

---

## 3. Metrik Efisiensi Arus Data

| Metrik | FFmpeg Transcoder | go2rtc Pass-Through | Efisiensi |
|---|---|---|---|
| Konsumsi CPU | 65% - 95% | 0.2% - 1.5% | Hemat beban ~98% |
| Alokasi RAM | ~250 MB / stream | ~15 MB / stream | Hemat RAM ~94% |
| Latensi Glass-to-Glass | 3.0 - 5.0 detik | <0.3 detik (WebRTC) | Instan tanpa delay |

---

## 4. Integrasi Web UI Minimalis

Tampilkan video ke dashboard web menggunakan tag standar WebRTC atau HLS native:

```html
<div class="rounded-xl overflow-hidden bg-slate-900 border border-slate-800">
    <!-- WebRTC Player Native -->
    <video id="cctv-stream" autoplay muted playsinline class="w-full h-auto"></video>
</div>

<script>
async function connectStream() {
    const pc = new RTCPeerConnection();
    pc.ontrack = (event) => {
        document.getElementById('cctv-stream').srcObject = event.streams[0];
    };
    pc.addTransceiver('video', { direction: 'recvonly' });
    
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    
    const resp = await fetch('/api/webrtc?src=kamera_servis', {
        method: 'POST',
        body: offer.sdp
    });
    const answer = await resp.text();
    await pc.setRemoteDescription({ type: 'answer', sdp: answer });
}
connectStream();
</script>
```
