---
name: print-shop-canvas-skill
description: "Generator grafis dinamis dan layout percetakan presisi fisik via Python PIL/Pillow: rendering 300 DPI, margin bleed mesin potong, dan ekspor PDF siap cetak workshop."
---

# Print Shop Canvas Engine Skill

Panduan pembuatan modul generator dokumen siap cetak (kartu nama, nota servis, stiker label komponen, kalender dinamis) dengan akurasi dimensi fisik milimeter, resolusi 300 DPI, dan batas margin potong (*bleed*).

---

## 1. Perbedaan Desain Layar vs Desain Cetak Fisik

- **Desain Layar (Web/UI)**: Bekerja pada satuan piksel (biasanya 72-96 DPI), ruang warna RGB.
- **Desain Cetak Fisik (Offset / Digital Press)**:
  - Satuan ukuran nyata adalah milimeter (mm).
  - Standar ketajaman minimal: **300 DPI** (Dots Per Inch).
  - Membutuhkan margin potong (*bleed area* ±3mm) di sekeliling desain agar tidak meninggalkan garis putih saat dipotong pisau mesin potong kertas.

---

## 2. Perhitungan Dimensi Kanvas Pillow (Python)

Formula konversi milimeter ke piksel pada 300 DPI:
$$\text{Pixel} = \frac{\text{mm} \times 300}{25.4}$$

```python
from PIL import Image, ImageDraw, ImageFont

def mm_to_px(mm: float, dpi: int = 300) -> int:
    return int((mm * dpi) / 25.4)

# Contoh: Kartu Garansi Meja Servis (90mm x 54mm) + Bleed 3mm tiap sisi
WIDTH_MM = 90 + 6
HEIGHT_MM = 54 + 6

canvas_w = mm_to_px(WIDTH_MM)
canvas_h = mm_to_px(HEIGHT_MM)

# Buat kanvas putih beresolusi tinggi (RGB 300 DPI)
img = Image.new("RGB", (canvas_w, canvas_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Gambar batas potong aman (Safe Zone)
safe_margin = mm_to_px(5)
draw.rectangle(
    [safe_margin, safe_margin, canvas_w - safe_margin, canvas_h - safe_margin],
    outline=(220, 220, 220),
    width=2
)
```

---

## 3. Ekspor PDF Siap Cetak (Preserve Exact DPI)

Saat menyimpan ke format PDF, parameter resolusi DPI wajib disematkan pada metadata file:

```python
# Simpan sebagai PDF dengan resolusi eksplisit 300 DPI
img.save(
    "kartu_servis_siap_cetak.pdf",
    "PDF",
    resolution=300.0,
    save_all=True
)
print("[+] File PDF siap potong berhasil dibuat.")
```
