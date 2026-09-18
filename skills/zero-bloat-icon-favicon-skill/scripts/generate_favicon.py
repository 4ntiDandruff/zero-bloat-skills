#!/usr/bin/env python3
"""
=============================================================================
ZERO-BLOAT ICON & FAVICON ENGINE (Pastree-Grade Slicing & Generation Utility)
Megapass Intra Solusindo • Sidoarjo, Indonesia
Fail-safe circuit mindset, zero Node.js bloat, C-native SVG rendering.
Inspired by pastree.megapass.web.id: pure geometric silhouettes & 25% squircle.
=============================================================================
"""

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageOps

# ---------------------------------------------------------------------------
# Input Sanitization & Palette Standards
# ---------------------------------------------------------------------------

HEX_COLOR_PATTERN = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")

THEMES = {
    "pastree": {"bg": "#0E7C61", "fg": "#FFFFFF"},
    "slate": {"bg": "#0B1220", "fg": "#22D3EE"},
    "indigo": {"bg": "#2563EB", "fg": "#FFFFFF"},
    "obsidian": {"bg": "#111827", "fg": "#F59E0B"},
    "kas": {"bg": "#0AA477", "fg": "#FFFFFF"},
}

def sanitize_hex_color(color_str: str, default: str = "#0E7C61") -> str:
    """
    Validates hex color string. Falls back to safe default if invalid.
    Prevents XML/SVG attribute injection.
    """
    if color_str and HEX_COLOR_PATTERN.match(color_str.strip()):
        return color_str.strip()
    return default


# ---------------------------------------------------------------------------
# Visual Presets (Pastree-Grade Solid Silhouettes on 64x64 Grid)
# ---------------------------------------------------------------------------

def build_svg_preset(
    preset_type: str = "tree",
    text: str = "M",
    bg_color: str = "#0E7C61",
    fg_color: str = "#FFFFFF"
) -> str:
    """
    Generates high-aesthetic, Pastree-grade vector SVG code on a 64x64 grid.
    Hukum Desain:
    1. Kanvas 64x64 dengan rx="16" (rasio squircle emas 25%).
    2. Siluet solid padat (bukan garis tipis) yang lolos The Squint Test 16px.
    3. Ruang bernapas 22-25% margin (simbol centered proporsional).
    4. Nol gradasi kabur / radial glow buatan yang merusak kontras.
    """
    bg = sanitize_hex_color(bg_color, "#0E7C61")
    fg = sanitize_hex_color(fg_color, "#FFFFFF")

    # Base squircle canvas (25% corner radius)
    canvas = f'<rect width="64" height="64" rx="16" fill="{bg}"/>'

    if preset_type in ["tree", "organic"]:
        # Signature Pastree Style: Canopy droplet + rounded trunk
        symbol = f"""  <path d="M32 14c-8 8-12 13-12 20a12 12 0 0 0 24 0c0-7-4-12-12-20z" fill="{fg}" opacity=".95"/>
  <rect x="29.5" y="38" width="5" height="12" rx="2.5" fill="{fg}"/>"""

    elif preset_type in ["bolt", "lightning"]:
        # Signature Skill Megapass Style: High-voltage solid sharp lightning
        symbol = f"""  <path d="M34 13L19 33h9l-3 18 17-23h-10l4-15z" fill="{fg}"/>"""

    elif preset_type in ["circuit", "chip"]:
        # Hardware & Servicing Workbench: Solid processor die with 4px punchy pins
        symbol = f"""  <rect x="22" y="22" width="20" height="20" rx="5" fill="{fg}"/>
  <circle cx="32" cy="32" r="3.5" fill="{bg}"/>
  <rect x="25" y="14" width="4" height="6" rx="2" fill="{fg}"/>
  <rect x="35" y="14" width="4" height="6" rx="2" fill="{fg}"/>
  <rect x="25" y="44" width="4" height="6" rx="2" fill="{fg}"/>
  <rect x="35" y="44" width="4" height="6" rx="2" fill="{fg}"/>
  <rect x="14" y="25" width="6" height="4" rx="2" fill="{fg}"/>
  <rect x="14" y="35" width="6" height="4" rx="2" fill="{fg}"/>
  <rect x="44" y="25" width="6" height="4" rx="2" fill="{fg}"/>
  <rect x="44" y="35" width="6" height="4" rx="2" fill="{fg}"/>"""

    elif preset_type in ["terminal", "prompt"]:
        # CLI & AI Orchestrator: Thick solid chevron and horizontal cursor
        symbol = f"""  <path d="M20 19l10 13-10 13" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="36" y1="45" x2="47" y2="45" stroke="{fg}" stroke-width="5" stroke-linecap="round"/>"""

    elif preset_type in ["kas", "chevron"]:
        # Signature Kas Megapass Style: Pillar and angled chevron arrow
        symbol = f"""  <rect x="19" y="17" width="7" height="30" rx="3.5" fill="{fg}"/>
  <path d="M29 34.5L41.5 20.5c1-1 2.8-1 3.8 0 .9.9.9 2.5 0 3.5L34 35l11.5 12c1 1 1 2.6 0 3.5-1 1-2.8 1-3.8 0L29 37.5z" fill="{fg}"/>"""

    elif preset_type in ["shield", "fortress"]:
        # Security & Fortress Style: Solid protective shield with core cutout
        symbol = f"""  <path d="M32 14c6 4 12 5 16 5 0 14-6 24-16 31C22 43 16 33 16 19c4 0 10-1 16-5z" fill="{fg}"/>
  <path d="M32 21c4 2.8 8 3.5 11 3.5 0 10-4 17-11 22-7-5-11-12-11-22 3 0 7-.7 11-3.5z" fill="{bg}"/>"""

    elif preset_type in ["monogram", "initial"]:
        # Swiss Bold Monogram: Clean centered text with calibrated baseline
        safe_text = html.escape(text[:2].upper())
        symbol = f"""  <text x="32" y="44" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', 'Inter', 'Segoe UI', sans-serif" font-size="34" font-weight="900" fill="{fg}">{safe_text}</text>"""

    else:
        # Fallback to Pastree Tree
        symbol = f"""  <path d="M32 14c-8 8-12 13-12 20a12 12 0 0 0 24 0c0-7-4-12-12-20z" fill="{fg}" opacity=".95"/>
  <rect x="29.5" y="38" width="5" height="12" rx="2.5" fill="{fg}"/>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  {canvas}
{symbol}
</svg>""".strip()


# ---------------------------------------------------------------------------
# Slicing Engine (C-native librsvg / Pillow ImageOps)
# ---------------------------------------------------------------------------

def render_asset_to_png(source_path: Path, output_png: Path, size: int) -> bool:
    """
    Renders SVG or raster image to PNG.
    Supports both vector (.svg) and raster (.png, .jpg, .webp) source assets.
    Pads rectangular images to square without stretching or distortion.
    """
    ext = source_path.suffix.lower()

    # 1. Raster source handling via Pillow (LANCZOS padding & resampling)
    if ext in [".png", ".jpg", ".jpeg", ".webp"]:
        try:
            with Image.open(source_path) as img:
                img_rgba = img.convert("RGBA")
                padded = ImageOps.pad(img_rgba, (size, size), method=Image.Resampling.LANCZOS, color=(0, 0, 0, 0))
                padded.save(output_png, format="PNG")
                return True
        except Exception:
            return False

    # 2. Vector SVG rendering via rsvg-convert (C-native librsvg)
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        cmd = [rsvg, "-w", str(size), "-h", str(size), str(source_path), "-o", str(output_png)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            return True

    # 3. Vector fallback via cairosvg CLI
    cairosvg = shutil.which("cairosvg")
    if cairosvg:
        cmd = [cairosvg, "-w", str(size), "-h", str(size), str(source_path), "-o", str(output_png)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            return True

    # 4. Vector fallback via cairosvg Python module
    try:
        import cairosvg as csvg_mod
        csvg_mod.svg2png(url=str(source_path), write_to=str(output_png), output_width=size, output_height=size)
        return True
    except Exception:
        pass

    return False


def generate_asset_bundle(
    source_asset: Path,
    out_dir: Path,
    app_name: str = "Megapass App",
    theme_color: str = "#0E7C61",
    prefix: str = "/"
) -> dict:
    """
    Compiles complete production web favicon package:
    - favicon.svg (Pastree-standard vector favicon)
    - favicon.ico (multi-resolution 16, 32, 48)
    - favicon-16x16.png
    - favicon-32x32.png
    - apple-touch-icon.png (180x180)
    - android-chrome-192x192.png
    - android-chrome-512x512.png
    - site.webmanifest
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    # If source is SVG, copy it as favicon.svg (Pastree vector standard)
    if source_asset.suffix.lower() == ".svg":
        target_svg = out_dir / "favicon.svg"
        if source_asset.resolve() != target_svg.resolve():
            shutil.copy2(source_asset, target_svg)
        generated_files.append("favicon.svg")

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
    }

    temp_pngs = {}
    for filename, dim in sizes.items():
        dest = out_dir / filename
        success = render_asset_to_png(source_asset, dest, dim)
        if not success:
            raise RuntimeError(f"Gagal me-render aset ke PNG ukuran {dim}x{dim}. Pastikan rsvg-convert atau cairosvg terinstall.")
        temp_pngs[dim] = dest
        generated_files.append(filename)

    # Compile Multi-Resolution favicon.ico using Pillow context manager
    ico_dest = out_dir / "favicon.ico"
    with Image.open(temp_pngs[512]) as img_master:
        img_master.save(
            ico_dest,
            format="ICO",
            sizes=[(16, 16), (32, 32), (48, 48)]
        )
    generated_files.insert(1 if "favicon.svg" in generated_files else 0, "favicon.ico")

    # Clean URL prefix
    pfx = prefix if prefix.endswith("/") else f"{prefix}/"

    # Generate site.webmanifest
    safe_theme = sanitize_hex_color(theme_color, "#0E7C61")
    manifest = {
        "name": app_name,
        "short_name": app_name,
        "icons": [
            {
                "src": f"{pfx}android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": f"{pfx}android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": safe_theme,
        "background_color": safe_theme,
        "display": "standalone"
    }
    manifest_dest = out_dir / "site.webmanifest"
    with open(manifest_dest, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    generated_files.append("site.webmanifest")

    return {
        "out_dir": str(out_dir),
        "files": generated_files,
        "html_tags": f"""<!-- Favicon & Touch Assets Generated by zero-bloat-icon-favicon-skill (Pastree Standard) -->
<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="icon" type="image/x-icon" href="{pfx}favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="{pfx}favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{pfx}favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{pfx}apple-touch-icon.png">
<link rel="manifest" href="{pfx}site.webmanifest">
<meta name="theme-color" content="{safe_theme}">"""
    }


# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Zero-Bloat Icon & Favicon Slicing Generator (Pastree Standard)")
    parser.add_argument("--input", "-i", type=str, help="Path ke file SVG atau PNG kustom")
    parser.add_argument(
        "--type", "-t",
        choices=["tree", "bolt", "circuit", "terminal", "kas", "shield", "monogram"],
        default="tree",
        help="Preset visual geometris solid Pastree-grade (default: tree)"
    )
    parser.add_argument(
        "--theme",
        choices=["pastree", "slate", "indigo", "obsidian", "kas"],
        default="pastree",
        help="Preset palet warna ruko (default: pastree)"
    )
    parser.add_argument("--text", type=str, default="M", help="Huruf inisial jika memakai preset monogram (maks 2 huruf)")
    parser.add_argument("--bg", type=str, help="Warna latar belakang (Hex, menimpa default theme)")
    parser.add_argument("--fg", type=str, help="Warna simbol foreground (Hex, menimpa default theme)")
    parser.add_argument("--out", "-o", type=str, default="./public", help="Direktori output aset")
    parser.add_argument("--name", type=str, default="Megapass Web", help="Nama aplikasi untuk site.webmanifest")
    parser.add_argument("--prefix", "-p", type=str, default="/", help="URL prefix untuk tag HTML dan manifest (default: '/')")
    
    args = parser.parse_args()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Determine theme colors
    theme_cfg = THEMES.get(args.theme, THEMES["pastree"])
    bg_color = args.bg if args.bg else theme_cfg["bg"]
    fg_color = args.fg if args.fg else theme_cfg["fg"]

    if args.input:
        src_asset = Path(args.input).resolve()
        if not src_asset.exists():
            print(f"[-] ERROR: File master '{src_asset}' tidak ditemukan!", file=sys.stderr)
            sys.exit(1)
    else:
        # Generate Pastree-grade clean SVG
        svg_content = build_svg_preset(
            preset_type=args.type,
            text=args.text,
            bg_color=bg_color,
            fg_color=fg_color
        )
        src_asset = out_dir / "favicon.svg"
        with open(src_asset, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[+] Master SVG berhasil diracik ({len(svg_content)} bytes): {src_asset}")

    print(f"[*] Menjalankan C-native slicing engine ke direktori: {out_dir} ...")
    try:
        bundle = generate_asset_bundle(
            source_asset=src_asset,
            out_dir=out_dir,
            app_name=args.name,
            theme_color=bg_color,
            prefix=args.prefix
        )
    except Exception as err:
        print(f"[-] ERROR: {err}", file=sys.stderr)
        sys.exit(1)

    print(f"[+] SELESAI: Berhasil membuat {len(bundle['files'])} aset produksi:")
    for f in bundle['files']:
        print(f"    - {f}")

    print("\n" + "=" * 60)
    print("HTML HEAD TAGS (Copy & Paste ke file template HTML Anda):")
    print("=" * 60)
    print(bundle["html_tags"])
    print("=" * 60)


if __name__ == "__main__":
    main()
