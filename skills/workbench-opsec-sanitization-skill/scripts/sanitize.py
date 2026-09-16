#!/usr/bin/env python3
"""
=====================================================================
WORKBENCH-OPSEC-SANITIZATION-SKILL: Zero-Bloat Regex Sanitizer
Megapass Intra Solusindo • Sidoarjo, Indonesia
=====================================================================
Zero-dependency sanitizer using pure Python standard library.
Detects, flags, and sanitizes:
- OS user filesystem paths (Linux /home/ and Windows Users)
- Terminal prompts with usernames and hostnames (user@host:~$ -> $)
- Tailscale CGNAT WireGuard IPs (100.64.0.0/10)
- Local workshop LAN subnets (192.168.110.x)
- Customer hardware identifiers (Service Tag, Motherboard S/N)
- Network physical MAC addresses
- Telegram bot tokens and API secrets (OpenAI, Anthropic, Gemini, AWS)
- Authentication blockers (SSH private keys, GitHub PATs)
=====================================================================
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Whitelisted documentation placeholders & public network standards
WHITELISTED_PATTERNS = [
    re.compile(r"\b100\.100\.100\.[0-9]{1,3}\b"),             # Tailscale MagicDNS quad-100
    re.compile(r"\b100\.64\.0\.[01]\b"),                      # CGNAT RFC base network and gateway
    re.compile(r"\b00:11:22:33:44:55\b", re.IGNORECASE),       # Standard dummy MAC
    re.compile(r"\bAA:BB:CC:DD:EE:FF\b", re.IGNORECASE),       # Standard dummy Wake-on-LAN MAC
    re.compile(r"\bFF:FF:FF:FF:FF:FF\b", re.IGNORECASE),       # Standard Wake-on-LAN broadcast MAC
    re.compile(r"/home/(?:<[a-zA-Z0-9_\-]+>|user|username)\b"),# Generic doc placeholders
    re.compile(r"[a-zA-Z]:\\Users\\(?:<[a-zA-Z0-9_\-]+>|user|username)\b", re.IGNORECASE),
    re.compile(r"\b(?:user|username)@(?:host|hostname):", re.IGNORECASE), # Generic doc prompt
    re.compile(r"\[REDACTED_[A-Z_]+\]"),                      # Already redacted markers
    re.compile(r"\bAKIAIOSFODNN7EXAMPLE\b"),                  # AWS documentation dummy key
]

# Sensitive patterns and their safe replacements
SANITIZATION_RULES = [
    # 1. Linux home directory: /home/<user>/ -> ~/ (excludes URLs like https://host/home/)
    {
        "name": "Linux Home Path",
        "pattern": re.compile(r"(?<![a-zA-Z0-9+.-]:/)(?:^|(?<=[\s\"\'\`:=(\[]))/home/[a-zA-Z0-9_\-\.]+(?=/|\b)"),
        "replacement": "~",
        "severity": "HIGH",
    },
    # 2. Windows user profile: C:\Users\<user>\ -> %USERPROFILE%\
    {
        "name": "Windows User Profile",
        "pattern": re.compile(r"(?<![a-zA-Z0-9+.-]:/)(?:^|(?<=[\s\"\'\`:=(\[]))[a-zA-Z]:\\Users\\[a-zA-Z0-9_\-\.]+(?=\\|\b)", re.IGNORECASE),
        "replacement": "%USERPROFILE%",
        "severity": "HIGH",
    },
    # 3. Terminal Prompt with OS username/hostname: user@host:~$ -> $
    {
        "name": "Terminal User Prompt",
        "pattern": re.compile(r"\b[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+:[~/\w\.-]*([\$#])\s*"),
        "replacement": r"\1 ",
        "severity": "MEDIUM",
    },
    # 4. Tailscale CGNAT IPs (100.64.0.0/10 range): 100.64-127.x.x -> localhost
    {
        "name": "Tailscale CGNAT IP",
        "pattern": re.compile(r"\b100\.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7])\.[0-9]{1,3}\.[0-9]{1,3}\b"),
        "replacement": "localhost",
        "severity": "MEDIUM",
    },
    # 5. Internal workshop LAN subnet (e.g. 192.168.110.x) -> 192.168.1.1
    {
        "name": "Workshop LAN Subnet",
        "pattern": re.compile(r"\b192\.168\.110\.[0-9]{1,3}\b"),
        "replacement": "192.168.1.1",
        "severity": "MEDIUM",
    },
    # 6. Customer hardware identifiers (Service Tag, Motherboard S/N)
    {
        "name": "Hardware Serial Number",
        "pattern": re.compile(r"\b(SN|Service Tag|Serial Number|S/N)[:=\s]+(?=[A-Za-z0-9]*\d)([A-Za-z0-9]{7,24})\b", re.IGNORECASE),
        "replacement": r"\1: [REDACTED_SERIAL]",
        "severity": "MEDIUM",
    },
    # 7. Telegram Bot Tokens: 9-10 digits : 35 alphanumeric characters
    {
        "name": "Telegram Bot Token",
        "pattern": re.compile(r"\b[0-9]{9,10}:[a-zA-Z0-9_\-]{35}\b"),
        "replacement": "[REDACTED_TELEGRAM_TOKEN]",
        "severity": "CRITICAL",
    },
    # 8. Physical MAC Addresses: AA:BB:CC:DD:EE:FF -> 00:11:22:33:44:55
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
        "name": "GitHub Token",
        "pattern": re.compile(r"\b(?:gh[pousr]_[a-zA-Z0-9]{36,255}|github_pat_[a-zA-Z0-9_]{60,100})\b"),
        "severity": "CRITICAL",
    },
    {
        "name": "OpenAI API Key",
        "pattern": re.compile(r"\bsk-(?:proj-)?[a-zA-Z0-9_\-]{40,}\b"),
        "severity": "CRITICAL",
    },
    {
        "name": "Anthropic API Key",
        "pattern": re.compile(r"\bsk-ant-[a-zA-Z0-9_\-]{32,}\b"),
        "severity": "CRITICAL",
    },
    {
        "name": "Google Gemini API Key",
        "pattern": re.compile(r"\bAIzaSy[a-zA-Z0-9_\-]{33,39}\b"),
        "severity": "CRITICAL",
    },
    {
        "name": "AWS Access Key",
        "pattern": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "severity": "CRITICAL",
    },
]

SKIP_DIRS = {".git", "__pycache__", "venv", ".venv", "node_modules", ".pytest_cache", ".ruff_cache"}
ALLOWED_EXTENSIONS = {
    ".md", ".txt", ".sh", ".py", ".json", ".yaml", ".yml",
    ".html", ".js", ".ts", ".toml", ".ini", ".conf", ".cfg", ".env"
}

def is_scannable_file(file_path: Path) -> bool:
    """Determine if a file should be scanned based on name and extension."""
    if file_path.name == "sanitize.py":
        return False
    if file_path.name.startswith(".env"):
        return True
    if file_path.name in {"Dockerfile", "Makefile", "Containerfile"}:
        return True
    return file_path.suffix.lower() in ALLOWED_EXTENSIONS

def scan_file(file_path: Path, fix: bool = False) -> list:
    """Scan a single file for sensitive patterns, optionally fixing in-place."""
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return issues

    modified_content = content
    has_changes = False

    # Check unfixable blockers first
    for rule in BLOCKER_RULES:
        for match in rule["pattern"].finditer(content):
            val = match.group(0)
            if "\\b" in val or "re.compile" in val:
                continue
            if any(wl.search(val) for wl in WHITELISTED_PATTERNS):
                continue
            issues.append({
                "file": str(file_path),
                "rule": rule["name"],
                "severity": rule["severity"],
                "action": "MANUAL REMOVAL REQUIRED",
                "match": val[:24] + ("..." if len(val) > 24 else ""),
                "is_blocker": True,
            })

    # Check and optionally fix sanitization rules
    for rule in SANITIZATION_RULES:
        matches = list(rule["pattern"].finditer(modified_content))
        if matches:
            for match in matches:
                val = match.group(0)
                # Avoid self-sanitizing regex declarations
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
                    "is_blocker": False,
                })
            if fix:
                def replace_func(m):
                    v = m.group(0)
                    if any(wl.search(v) for wl in WHITELISTED_PATTERNS):
                        return v
                    return m.expand(rule["replacement"])
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
        if target_path.name != "sanitize.py":
            files_to_check.append(target_path)
    else:
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                p = Path(root) / f
                if is_scannable_file(p):
                    files_to_check.append(p)

    all_issues = []
    for file_path in files_to_check:
        issues = scan_file(file_path, fix=is_fix_mode)
        all_issues.extend(issues)

    print("=====================================================================")
    print(f"[*] WORKBENCH OPSEC SCANNER: {'FIX MODE' if is_fix_mode else 'AUDIT MODE'}")
    print(f"[*] Inspected {len(files_to_check)} file(s) across {target_path}")
    print("=====================================================================")

    if not all_issues:
        print("[+] PASS: Zero OPSEC leaks detected. Workspace is 100% sanitized!")
        print("=====================================================================")
        sys.exit(0)

    for issue in all_issues:
        status = "[*] FIXED" if is_fix_mode and not issue.get("is_blocker") else "[-] LEAK"
        print(f"{status} [{issue['severity']}] {issue['file']}: {issue['rule']} ({issue['match']}) -> {issue['action']}")

    print("=====================================================================")
    blockers = [i for i in all_issues if i.get("is_blocker")]
    fixable = [i for i in all_issues if not i.get("is_blocker")]

    if is_fix_mode:
        if blockers:
            print(f"[-] FAILED: Cleaned {len(fixable)} string(s), but {len(blockers)} CRITICAL BLOCKER(S) remain unresolved!")
            print("[-] Manual removal of private keys or secret tokens is required before committing.")
            print("=====================================================================")
            sys.exit(2)
        else:
            print(f"[+] Cleaned {len(fixable)} sensitive string(s).")
            print("=====================================================================")
            sys.exit(0)
    else:
        print(f"[-] Found {len(all_issues)} sensitive string(s) that need sanitization.")
        print("=====================================================================")
        sys.exit(1)

if __name__ == "__main__":
    main()
