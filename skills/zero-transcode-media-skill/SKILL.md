---
name: zero-transcode-media-skill
description: "Edge CCTV media streaming architecture on constrained hardware (STB/i3) without CPU transcoding: RTSP to WebRTC/HLS pass-through via go2rtc and memory footprint <30MB."
---

# Zero-Transcode Edge Media Skill

Real-time CCTV and bench monitoring streaming pattern for low-power edge hardware (Armbian TV boxes, repurposed laptops, or edge single-board computers) without exhausting CPU cores on software video re-encoding.

---

## 1. The Cost of Transcoding on Constrained Hardware

- Re-encoding incoming H.264/H.265 video streams via FFmpeg CPU decoders absorbs 80-100% of CPU capacity on non-GPU edge appliances.
- High thermal throttling, frame stuttering, and eventual system freeze follow within hours.

---

## 2. Circuit Solution: Native RTP Pass-Through (go2rtc)

Utilize a compiled Go binary (`go2rtc`) that forwards raw RTP packets directly to browser endpoints without decoding video frames:

### `go2rtc.yaml` Configuration:
```yaml
streams:
  bench_camera:
    - rtsp://admin:pass@192.168.1.100:554/stream1
  workshop_overhead:
    - rtsp://admin:pass@192.168.1.101:554/live/ch0

api:
  listen: ":1984"

webrtc:
  listen: ":8555"
```

---

## 3. Data Flow & Efficiency Comparison

| Metric | FFmpeg Transcoder | go2rtc Pass-Through | Real Gain |
|---|---|---|---|
| CPU Utilization | 65% - 95% | 0.2% - 1.5% | ~98% CPU reduction |
| Memory Allocation | ~250 MB / stream | ~15 MB / stream | ~94% RAM reduction |
| Glass-to-Glass Latency | 3.0 - 5.0 seconds | <0.3 seconds (WebRTC) | Sub-second real-time |

---

## 4. Minimalist Web Client Integration

Render live video feeds into browser interfaces using standard HTML5 WebRTC:

```html
<div class="rounded-xl overflow-hidden bg-slate-900 border border-slate-800">
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
    
    const resp = await fetch('/api/webrtc?src=bench_camera', {
        method: 'POST',
        body: offer.sdp
    });
    const answer = await resp.text();
    await pc.setRemoteDescription({ type: 'answer', sdp: answer });
}
connectStream();
</script>
```
