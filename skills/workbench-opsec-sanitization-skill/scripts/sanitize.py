#!/usr/bin/env python3
"""
=====================================================================
WORKBENCH-OPSEC-SANITIZATION-SKILL: Zero-Bloat Regex Sanitizer
Megapass Intra Solusindo • Sidoarjo, Indonesia
=====================================================================
Zero-dependency sanitizer using Python standard library.
Detects and sanitizes OS user paths, private Tailscale IPs, LAN subnets,
MAC addresses, and Telegram bot tokens from logs and documentation.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Whitelisted documentation placeholders
WHITELISTED_PATTERNS = [
    re.compile(r"\b100\.100\.100\.[0-9]{1,3}\b"),  # Official Tailscale MagicDNS quad-100
    re.compile(r"\b100\.64\.0\.1\b"),              # Standard CGNAT example IP
    re.compile(r"00:11:22:33:44:55", re.IGNORECASE), # Standard dummy MAC
    re.compile(r"AA:BB:CC:DD:EE:FF", re.IGNORECASE), # Standard dummy Wake-on-LAN MAC
    re.compile(r"/home/(?:<[a-zA-Z0-9_\-]+>|user|username)\b"), # Generic doc placeholders
    re.compile(r"[a-zA-Z]:\\Users\\(?:<[a-zA-Z0-9_\-]+>|user|username)\b", re.IGNORECASE),
]

# Sensitive patterns and their safe replacements
SANITIZATION_RULES = [
    # 1. User home paths: /home/<user>/ -> ~/ (excluding generic placeholders)
    {
        "name": "Linux Home Path",
        "pattern": re.compile(r"/home/[a-zA-Z0-9_\-\.]+(?=/|\b)"),
        "replacement": "~",
        "severity": "HIGH",
    },
    # 2. Windows user profile paths: C:\Users\<user>\ -> %USERPROFILE%\
    {
        "name": "Windows User Profile",
        "pattern": re.compile(r"[a-zA-Z]:\\Users\\[a-zA-Z0-9_\-\.]+(?=\\|\b)", re.IGNORECASE),
        "replacement": "%USERPROFILE%",
        "severity": "HIGH",
    },
    # 3. Tailscale CGNAT IPs (100.64.0.0/10 range): 100.64-127.x.x
    {
        "name": "Tailscale CGNAT IP",
        "pattern": re.compile(r"\b100\.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7])\.[0-9]{1,3}\.[0-9]{1,3}\b"),
        "replacement": "localhost",
        "severity": "MEDIUM",
    },
    # 4. Internal workshop LAN subnet (e.g., 192.168.110.x)
    {
        "name": "Workshop LAN Subnet",
        "pattern": re.compile(r"\b192\.168\.110\.[0-9]{1,3}\b"),
        "replacement": "192.168.1.1",
        "severity": "MEDIUM",
    },
    # 5. Telegram Bot Tokens: 9-10 digits : 35 alphanumeric characters
    {
        "name": "Telegram Bot Token",
        "pattern": re.compile(r"\b[0-9]{9,10}:[a-zA-Z0-9_\-]{35}\b"),
        "replacement": "[REDACTED_TELEGRAM_TOKEN]",
        "severity": "CRITICAL",
    },
    # 6. Physical MAC Addresses: AA:BB:CC:DD:EE:FF
    {
        "name": "Physical MAC Address",
        "pattern": re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b"),
        "replacement": "00:11:22:33:44:55",
        "severity": "LOW",
    },
]

# Blockers: if present, cannot be auto-fixed safely and must be removed manually
BLOCKER_RULES = [
    {
        "name": "SSH Private Key",
        "pattern": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "severity": "CRITICAL",
    },
    {
        "name": "GitHub Personal Access Token",
        "pattern": re.compile(r"\bghp_[a-zA-Z0-9]{36}\b"),
        "severity": "CRITICAL",
    },
]

SKIP_DIRS = {".git", "__pycache__", "venv", ".venv", "node_modules"}
ALLOWED_EXTENSIONS = {".md", ".txt", ".sh", ".py", ".json", ".yaml", ".yml", ".html", ".js", ".ts"}

def scan_file(file_path: Path, fix: bool = False) -> list:
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return issues

    modified_content = content
    has_changes = False

    # Check blockers
    for rule in BLOCKER_RULES:
        for match in rule["pattern"].finditer(content):
            issues.append({
                "file": str(file_path),
                "rule": rule["name"],
                "severity": rule["severity"],
                "action": "MANUAL REMOVAL REQUIRED",
                "match": match.group(0)[:20] + "...",
            })

    # Check and optionally fix sanitization rules
    for rule in SANITIZATION_RULES:
        matches = list(rule["pattern"].finditer(modified_content))
        if matches:
            for match in matches:
                # Avoid self-sanitizing regex declarations
                val = match.group(0)
                if "\\b" in val or "re.compile" in val:
                    continue
                # Skip officially whitelisted dummy documentation values
                if any(wl.search(val) for wl in WHITELISTED_PATTERNS):
                    continue
                issues.append({
                    "file": str(file_path),
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "action": "REPLACE -> " + rule["replacement"] if fix else "FLAGGED",
                    "match": val,
                })
            if fix:
                # Only replace non-whitelisted items
                def replace_func(m):
                    v = m.group(0)
                    if any(wl.search(v) for wl in WHITELISTED_PATTERNS):
                        return v
                    return rule["replacement"]
                new_content = rule["pattern"].sub(replace_func, modified_content)
                if new_content != modified_content:
                    modified_content = new_content
                    has_changes = True

    if fix and has_changes and modified_content != content:
        try:
            file_path.write_text(modified_content, encoding="utf-8")
        except Exception as e:
            print(f"[-] Error writing {file_path}: {e}", file=sys.stderr)

    return issues

def main():
    parser = argparse.ArgumentParser(description="Zero-Bloat Workbench OPSEC Sanitizer")
    parser.add_argument("path", nargs="?", default=".", help="File or directory to scan/fix (default: current directory)")
    parser.add_argument("--scan", action="store_true", help="Audit mode (dry-run, no changes made)")
    parser.add_argument("--fix", action="store_true", help="In-place replacement mode")
    args = parser.parse_args()

    target_path = Path(args.path).resolve()
    if not target_path.exists():
        print(f"[-] Path not found: {target_path}", file=sys.stderr)
        sys.exit(1)

    is_fix_mode = args.fix and not args.scan
    files_to_check = []

    if target_path.is_file():
        files_to_check.append(target_path)
    else:
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                ext = Path(f).suffix.lower()
                if ext in ALLOWED_EXTENSIONS:
                    # Skip self to prevent false positive on regex rules
                    p = Path(root) / f
                    if p.name == "sanitize.py":
                        continue
                    files_to_check.append(p)

    all_issues = []
    for file_path in files_to_check:
        issues = scan_file(file_path, fix=is_fix_mode)
        all_issues.extend(issues)

    print("=====================================================================")
    print(f"[*] WORKBENCH OPSEC SCANNER: {'FIX MODE' if is_fix_mode else 'AUDIT MODE'}")
    print(f"[*] Inspected {len(files_to_check)} files across {target_path}")
    print("=====================================================================")

    if not all_issues:
        print("[+] PASS: Zero OPSEC leaks detected. Workspace is 100% sanitized!")
        print("=====================================================================")
        sys.exit(0)

    for issue in all_issues:
        status = "[*] FIXED" if is_fix_mode and "REPLACE" in issue["action"] else "[-] LEAK"
        print(f"{status} [{issue['severity']}] {issue['file']}: {issue['rule']} ({issue['match']}) ➔ {issue['action']}")

    print("=====================================================================")
    if is_fix_mode:
        print(f"[+] Cleaned {len(all_issues)} sensitive string(s).")
        sys.exit(0)
    else:
        print(f"[-] Found {len(all_issues)} sensitive string(s) that need sanitization.")
        sys.exit(1)

if __name__ == "__main__":
    main()
