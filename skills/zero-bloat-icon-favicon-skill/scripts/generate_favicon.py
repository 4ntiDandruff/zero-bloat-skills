#!/usr/bin/env python3
"""
=============================================================================
ZERO-BLOAT ICON & FAVICON ENGINE (Slicing & Generation Utility)
Megapass Intra Solusindo • Sidoarjo, Indonesia
Fail-safe circuit mindset, zero Node.js bloat, C-native SVG rendering.
=============================================================================
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image

# ---------------------------------------------------------------------------
# Visual Presets & Master SVG Builders (Pure Mathematical Vectors)
# ---------------------------------------------------------------------------

def build_squircle_path(size: int = 512, r: float = 0.22) -> str:
    """
    Continuous curvature Apple-style squircle path for 512x512 canvas.
    """
    c = size
    radius = c * r
    # Superellipse approximate cubic beziers
    return f"""
    M 0,{radius}
    C 0,{radius * 0.44} {radius * 0.44},0 {radius},0
    L {c - radius},0
    C {c - radius * 0.44},0 {c},{radius * 0.44} {c},{radius}
    L {c},{c - radius}
    C {c},{c - radius * 0.44} {c - radius * 0.44},{c} {c - radius},{c}
    L {radius},{c}
    C {radius * 0.44},{c} 0,{c - radius * 0.44} 0,{c - radius}
    Z
    """.strip()


def build_svg_preset(
    preset_type: str,
    text: str = "M",
    bg_color: str = "#0B1220",
    fg_color: str = "#22D3EE",
    secondary_color: str = "#0891B2",
    has_squircle: bool = True
) -> str:
    """
    Generates high-aesthetic, anti-norak vector SVG source code.
    Strictly follows Swiss typography & Dark Modern Tech guidelines.
    """
    squircle_path = build_squircle_path(512, 0.24) if has_squircle else ""
    
    # Base container
    bg_element = f'<path d="{squircle_path}" fill="{bg_color}"/>' if has_squircle else f'<rect width="512" height="512" rx="112" fill="{bg_color}"/>'

    if preset_type == "monogram":
        # Swiss-style heavy typographic monogram with subtle optical offset
        symbol_content = f"""
        <text x="256" y="342" 
              font-family="-apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', 'Inter', 'Segoe UI', sans-serif" 
              font-size="288" 
              font-weight="900" 
              letter-spacing="-12"
              text-anchor="middle" 
              fill="{fg_color}">{text[:2].upper()}</text>
        """
    elif preset_type == "circuit":
        # Hardware logic / circuit traces glyph
        symbol_content = f"""
        <g stroke="{fg_color}" stroke-width="28" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Center Processing Die -->
            <rect x="176" y="176" width="160" height="160" rx="32" fill="{bg_color}" stroke="{fg_color}" stroke-width="28"/>
            <circle cx="256" cy="256" r="32" fill="{fg_color}"/>
            
            <!-- Circuit Traces North -->
            <path d="M 216,176 L 216,104"/>
            <path d="M 296,176 L 296,104"/>
            <circle cx="216" cy="92" r="14" fill="{secondary_color}" stroke="none"/>
            <circle cx="296" cy="92" r="14" fill="{secondary_color}" stroke="none"/>
            
            <!-- Circuit Traces South -->
            <path d="M 216,336 L 216,408"/>
            <path d="M 296,336 L 296,408"/>
            <circle cx="216" cy="420" r="14" fill="{secondary_color}" stroke="none"/>
            <circle cx="296" cy="420" r="14" fill="{secondary_color}" stroke="none"/>
            
            <!-- Circuit Traces East -->
            <path d="M 336,256 L 408,256"/>
            <circle cx="420" cy="256" r="14" fill="{secondary_color}" stroke="none"/>
            
            <!-- Circuit Traces West -->
            <path d="M 176,256 L 104,256"/>
            <circle cx="92" cy="256" r="14" fill="{secondary_color}" stroke="none"/>
        </g>
        """
    elif preset_type == "prompt":
        # Terminal prompt >_ glyph
        symbol_content = f"""
        <g stroke="{fg_color}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <path d="M 136,176 L 244,256 L 136,336"/>
            <line x1="284" y1="336" x2="384" y2="336" stroke="{secondary_color}"/>
        </g>
        """
    elif preset_type == "bolt":
        # High-voltage minimal electric bolt
        symbol_content = f"""
        <path d="M 284,80 L 156,268 L 264,268 L 228,432 L 364,244 L 256,244 Z" 
              fill="{fg_color}" 
              stroke="{secondary_color}" 
              stroke-width="12" 
              stroke-linejoin="round"/>
        """
    else:
        # Default: Minimal geometric node hexagon
        symbol_content = f"""
        <g stroke="{fg_color}" stroke-width="28" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polygon points="256,112 384,186 384,334 256,408 128,334 128,186" fill="{bg_color}"/>
            <circle cx="256" cy="256" r="48" fill="{secondary_color}" stroke="{fg_color}" stroke-width="20"/>
        </g>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
    <defs>
        <radialGradient id="ambientGlow" cx="50%" cy="25%" r="75%">
            <stop offset="0%" stop-color="{secondary_color}" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="{bg_color}" stop-opacity="0"/>
        </radialGradient>
    </defs>
    {bg_element}
    <rect width="512" height="512" rx="112" fill="url(#ambientGlow)"/>
    {symbol_content}
</svg>"""
    return svg.strip()


# ---------------------------------------------------------------------------
# Slicing Engine (rsvg-convert / cairosvg / Pillow)
# ---------------------------------------------------------------------------

def render_svg_to_png(svg_path: Path, output_png: Path, size: int) -> bool:
    """
    Renders SVG to PNG using the fastest and sharpest available system renderer.
    Priority:
    1. rsvg-convert (GNOME C-native librsvg: sub-millisecond, perfect font hinting)
    2. cairosvg (Python Cairo bindings)
    """
    # 1. Try rsvg-convert
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        cmd = [rsvg, "-w", str(size), "-h", str(size), str(svg_path), "-o", str(output_png)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            return True

    # 2. Try cairosvg
    cairosvg = shutil.which("cairosvg")
    if cairosvg:
        cmd = [cairosvg, "-w", str(size), "-h", str(size), str(svg_path), "-o", str(output_png)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            return True

    try:
        import cairosvg as csvg_mod
        csvg_mod.svg2png(url=str(svg_path), write_to=str(output_png), output_width=size, output_height=size)
        return True
    except Exception:
        pass

    return False


def generate_asset_bundle(
    source_svg: Path,
    out_dir: Path,
    app_name: str = "Megapass App",
    theme_color: str = "#0B1220"
) -> dict:
    """
    Compiles complete production web favicon package from a single SVG master:
    - favicon.ico (multi-res 16, 32, 48)
    - favicon-16x16.png
    - favicon-32x32.png
    - apple-touch-icon.png (180x180)
    - android-chrome-192x192.png
    - android-chrome-512x512.png
    - site.webmanifest
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    # Target PNG sizes
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
    }

    temp_pngs = {}
    for filename, dim in sizes.items():
        dest = out_dir / filename
        success = render_svg_to_png(source_svg, dest, dim)
        if not success:
            raise RuntimeError(f"Gagal me-render SVG ke PNG ukuran {dim}x{dim}. Pastikan rsvg-convert atau cairosvg terinstall.")
        temp_pngs[dim] = dest
        generated_files.append(filename)

    # Compile Multi-Resolution favicon.ico using Pillow
    ico_dest = out_dir / "favicon.ico"
    # Open 48, 32, 16 images
    img_48 = Image.open(temp_pngs[48])
    img_48.save(
        ico_dest,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)]
    )
    # Clean up intermediate 48x48 if not strictly needed
    if (out_dir / "favicon-48x48.png").exists():
        (out_dir / "favicon-48x48.png").unlink()
    if "favicon-48x48.png" in generated_files:
        generated_files.remove("favicon-48x48.png")
    generated_files.insert(0, "favicon.ico")

    # Generate site.webmanifest
    manifest = {
        "name": app_name,
        "short_name": app_name,
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": theme_color,
        "background_color": theme_color,
        "display": "standalone"
    }
    manifest_dest = out_dir / "site.webmanifest"
    with open(manifest_dest, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    generated_files.append("site.webmanifest")

    return {
        "out_dir": str(out_dir),
        "files": generated_files,
        "html_tags": f"""<!-- Favicon & Touch Assets Generated by zero-bloat-icon-favicon-skill -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="{theme_color}">"""
    }


# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Zero-Bloat Icon & Favicon Slicing Generator")
    parser.add_argument("--input", "-i", type=str, help="Path ke master SVG jika sudah memiliki desain sendiri")
    parser.add_argument("--type", "-t", choices=["monogram", "circuit", "prompt", "bolt", "node"], default="monogram", help="Preset visual geometris jika membuat dari awal")
    parser.add_argument("--text", type=str, default="M", help="Huruf inisial jika memakai preset monogram (maks 2 huruf)")
    parser.add_argument("--bg", type=str, default="#0B1220", help="Warna latar (Hex, default: Deep Slate #0B1220)")
    parser.add_argument("--fg", type=str, default="#22D3EE", help="Warna simbol (Hex, default: Electric Cyan #22D3EE)")
    parser.add_argument("--accent", type=str, default="#0891B2", help="Warna aksen kedua (Hex, default: Dark Cyan #0891B2)")
    parser.add_argument("--out", "-o", type=str, default="./public", help="Direktori output aset")
    parser.add_argument("--name", type=str, default="Megapass Web", help="Nama aplikasi untuk site.webmanifest")
    
    args = parser.parse_args()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.input:
        src_svg = Path(args.input).resolve()
        if not src_svg.exists():
            print(f"[-] ERROR: File master SVG '{src_svg}' tidak ditemukan!")
            sys.exit(1)
    else:
        # Generate SVG from clean preset
        svg_content = build_svg_preset(
            preset_type=args.type,
            text=args.text,
            bg_color=args.bg,
            fg_color=args.fg,
            secondary_color=args.accent,
            has_squircle=True
        )
        src_svg = out_dir / "master_icon.svg"
        with open(src_svg, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[+] Master SVG berhasil diracik: {src_svg}")

    print(f"[*] Menjalankan C-native slicing engine ke direktori: {out_dir} ...")
    bundle = generate_asset_bundle(
        source_svg=src_svg,
        out_dir=out_dir,
        app_name=args.name,
        theme_color=args.bg
    )

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
