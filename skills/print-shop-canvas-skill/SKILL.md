---
name: print-shop-canvas-skill
description: "Generator grafis dinamis dan layout percetakan presisi fisik via Python PIL/Pillow: rendering 300 DPI, margin bleed mesin potong, dan ekspor PDF siap cetak workshop."
---

# Print Shop Canvas Engine Skill

Design guide for generating physical print-ready documents (warranty cards, service tickets, component bin labels, dynamic calendars) with millimeter dimensional accuracy, 300 DPI resolution, and bleed margins for industrial cutter blades.

---

## 1. Screen Displays vs Physical Press Specifications

- **Screen Displays (Web/UI)**: Operate on pixels (typically 72-96 DPI) in RGB color space.
- **Physical Offset / Digital Press**:
  - Exact dimensions measured in millimeters (mm).
  - Minimum visual sharpness standard: **300 DPI** (Dots Per Inch).
  - Requires perimeter bleed margins (+3mm on all outer edges) to prevent unprinted white borders during mechanical guillotine cutting.

---

## 2. Pillow High-DPI Coordinate Calculations

Millimeter-to-pixel conversion at 300 DPI:
$$\text{Pixels} = \frac{\text{mm} \times 300}{25.4}$$

```python
from PIL import Image, ImageDraw

def mm_to_px(mm: float, dpi: int = 300) -> int:
    return int((mm * dpi) / 25.4)

# Example: Repair Bench Warranty Card (90mm x 54mm) + 3mm Bleed per edge
WIDTH_MM = 90 + 6
HEIGHT_MM = 54 + 6

canvas_w = mm_to_px(WIDTH_MM)
canvas_h = mm_to_px(HEIGHT_MM)

# Instantiate high-resolution white canvas (300 DPI RGB)
img = Image.new("RGB", (canvas_w, canvas_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Outline safe cutting margin (5mm inside trim line)
safe_margin = mm_to_px(5)
draw.rectangle(
    [safe_margin, safe_margin, canvas_w - safe_margin, canvas_h - safe_margin],
    outline=(220, 220, 220),
    width=2
)
```

---

## 3. Print-Ready PDF Export (Preserving Exact DPI)

When exporting canvas outputs to PDF, explicit DPI metadata must be preserved:

```python
# Export to PDF embedding explicit 300 DPI resolution headers
img.save(
    "service_warranty_print_ready.pdf",
    "PDF",
    resolution=300.0,
    save_all=True
)
print("[+] Press-ready PDF with cutter bleed generated successfully.")
```
