#!/usr/bin/env python3
"""
=====================================================================
VENTOY-SERVICING-SKILL: USB Multiboot Workbench Helper
Megapass Intra Solusindo • Sidoarjo, Indonesia
=====================================================================
Zero-dependency Python utility to initialize and audit Ventoy USB drives:
- Generates optimal ventoy.json (Global CLI display + Win11 bypasses)
- Sets up .ventoyignore in non-boot directories (Drivers, Tools)
- Creates directory structure for ISOs and Intel Gen 11-14 VMD storage drivers
=====================================================================
"""

import argparse
import json
import os
import sys
from pathlib import Path

STANDARD_VENTOY_CONFIG = {
    "control": [
        {"VTOY_DEFAULT_MENU_MODE": "list"},
        {"VTOY_WIN11_BYPASS_CHECK": "1"},
        {"VTOY_WIN11_BYPASS_NRO": "1"}
    ],
    "theme": {
        "display_mode": "CLI"
    }
}

def init_ventoy(drive_path: Path):
    """Initialize a mounted Ventoy partition with optimal workbench settings."""
    if not drive_path.exists() or not drive_path.is_dir():
        print(f"[-] Error: Target drive path does not exist: {drive_path}", file=sys.stderr)
        sys.exit(1)

    print("=====================================================================")
    print(f"[*] INITIALIZING VENTOY WORKBENCH USB: {drive_path}")
    print("=====================================================================")

    # 1. Create /ventoy/ directory and ventoy.json
    ventoy_dir = drive_path / "ventoy"
    ventoy_dir.mkdir(parents=True, exist_ok=True)
    config_file = ventoy_dir / "ventoy.json"

    config_file.write_text(json.dumps(STANDARD_VENTOY_CONFIG, indent=2), encoding="utf-8")
    print(f"[+] Created: {config_file.relative_to(drive_path)} (Global CLI + Win11 Bypass)")

    # 2. Setup standard folders
    folders = [
        ("ISO", False),
        ("ISO/Windows", False),
        ("ISO/Linux", False),
        ("ISO/Rescue", False),
        ("Drivers", True),
        ("Drivers/Obat_VMD_Intel_Gen11_14", False),
        ("Tools", True),
    ]

    for rel_path, needs_ignore in folders:
        d = drive_path / rel_path
        d.mkdir(parents=True, exist_ok=True)
        if needs_ignore:
            ignore_file = d / ".ventoyignore"
            if not ignore_file.exists():
                ignore_file.touch()
                print(f"[+] Created: {ignore_file.relative_to(drive_path)} (Menu Scan Excluded)")
        print(f"[+] Prepared: {d.relative_to(drive_path)}/")

    # 3. Create README instruction for Intel VMD drivers
    vmd_readme = drive_path / "Drivers" / "Obat_VMD_Intel_Gen11_14" / "PETUNJUK_DRIVER_VMD.txt"
    if not vmd_readme.exists():
        vmd_readme.write_text(
            "OBAT VMD INTEL GEN 11-14 (TIGER LAKE S/D METEOR LAKE)\n"
            "=======================================================\n"
            "1. Ekstrak driver Intel RST (iaStorVD.sys, iaVD.inf, iaVD.cat) ke folder ini.\n"
            "2. Saat installer Windows 10/11 tidak mendeteksi SSD NVMe:\n"
            "   - Klik 'Load driver' -> 'Browse'.\n"
            "   - Pilih folder ini.\n"
            "   - Partisi NVMe akan langsung terbaca tanpa perlu ubah BIOS ke AHCI.\n",
            encoding="utf-8"
        )
        print(f"[+] Created: {vmd_readme.relative_to(drive_path)}")

    print("=====================================================================")
    print("[+] Ventoy USB configuration completed successfully!")
    print("[*] Ingat: Jalankan 'sync' sebelum mencabut flashdisk dari sistem Linux.")
    print("=====================================================================")

def verify_ventoy(drive_path: Path):
    """Audit an existing Ventoy USB partition for compliance."""
    if not drive_path.exists() or not drive_path.is_dir():
        print(f"[-] Error: Target drive path does not exist: {drive_path}", file=sys.stderr)
        sys.exit(1)

    print("=====================================================================")
    print(f"[*] AUDITING VENTOY WORKBENCH USB: {drive_path}")
    print("=====================================================================")

    issues = []
    config_file = drive_path / "ventoy" / "ventoy.json"

    # 1. Check ventoy.json
    if not config_file.exists():
        issues.append("Missing /ventoy/ventoy.json configuration file")
    else:
        try:
            cfg = json.loads(config_file.read_text(encoding="utf-8"))
            theme = cfg.get("theme", {})
            if theme.get("display_mode") != "CLI":
                issues.append("Display mode is not set to 'CLI' (risk of graphical lag on older monitors)")

            control = cfg.get("control", [])
            ctrl_keys = {}
            for item in control:
                ctrl_keys.update(item)

            if ctrl_keys.get("VTOY_WIN11_BYPASS_CHECK") != "1":
                issues.append("Win11 TPM/SecureBoot/RAM bypass is disabled")
            if ctrl_keys.get("VTOY_WIN11_BYPASS_NRO") != "1":
                issues.append("Win11 Offline Account (NRO) bypass is disabled")
            if ctrl_keys.get("VTOY_DEFAULT_MENU_MODE") != "list":
                issues.append("Default menu mode is not 'list'")
        except Exception as e:
            issues.append(f"Invalid JSON format in ventoy.json: {e}")

    # 2. Check .ventoyignore in Drivers and Tools
    for folder_name in ["Drivers", "Tools"]:
        target_dir = drive_path / folder_name
        if target_dir.exists():
            ignore_file = target_dir / ".ventoyignore"
            if not ignore_file.exists():
                issues.append(f"Missing .ventoyignore in {folder_name}/ (causes slow menu parsing)")

    # 3. Check VMD driver directory
    vmd_dir = drive_path / "Drivers" / "Obat_VMD_Intel_Gen11_14"
    if not vmd_dir.exists():
        issues.append("Missing Drivers/Obat_VMD_Intel_Gen11_14/ directory")

    if issues:
        for iss in issues:
            print(f"[-] WARN: {iss}")
        print("=====================================================================")
        print(f"[-] Audit completed with {len(issues)} warning(s).")
        sys.exit(1)
    else:
        print("[+] PASS: Config ventoy.json valid, CLI mode active, bypass enabled.")
        print("[+] PASS: .ventoyignore terpasang pada folder Drivers dan Tools.")
        print("[+] PASS: Struktur partisi Ventoy memenuhi standar meja servis!")
        print("=====================================================================")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Zero-Bloat Ventoy USB Servicing Helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: init
    parser_init = subparsers.add_parser("init", help="Initialize a mounted Ventoy drive with optimal config")
    parser_init.add_argument("drive", help="Mount point of Ventoy partition (e.g., /media/user/Ventoy)")

    # Subcommand: verify
    parser_verify = subparsers.add_parser("verify", help="Verify Ventoy USB configuration compliance")
    parser_verify.add_argument("drive", help="Mount point of Ventoy partition")

    args = parser.parse_args()
    drive_path = Path(args.drive).resolve()

    if args.command == "init":
        init_ventoy(drive_path)
    elif args.command == "verify":
        verify_ventoy(drive_path)

if __name__ == "__main__":
    main()
