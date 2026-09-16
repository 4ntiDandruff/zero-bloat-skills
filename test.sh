#!/usr/bin/env bash
# =====================================================================
# ZERO-BLOAT-SKILLS — Unified Test Runner & Health Check
# Megapass Intra Solusindo • Sidoarjo, Indonesia
# =====================================================================
set -euo pipefail

export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export SKILLS_DIR="$SCRIPT_DIR/skills"

echo "====================================================================="
echo "[*] ZERO-BLOAT-SKILLS: Unified Health Check & Verification"
echo "====================================================================="

FAILURES=0

# ---------------------------------------------------------------------
# Check 1: Shell Script Syntax
# ---------------------------------------------------------------------
echo "[*] [Check 1/5] Memeriksa sintaks skrip Shell..."
if bash -n "$SCRIPT_DIR/install.sh" "$SCRIPT_DIR/uninstall.sh" "$SCRIPT_DIR/test.sh"; then
    echo "[+] PASS: Seluruh skrip shell valid secara sintaksis."
else
    echo "[-] FAIL: Terdeteksi error sintaksis pada skrip shell!"
    FAILURES=$((FAILURES + 1))
fi

# ---------------------------------------------------------------------
# Check 2: Skill Frontmatter & Directory Name Symmetry
# ---------------------------------------------------------------------
echo "[*] [Check 2/5] Memeriksa validitas YAML frontmatter seluruh modul skill..."
PYTHON_FM_CHECK=$(python3 - <<'EOF'
import os, sys, yaml

skills_dir = os.environ.get("SKILLS_DIR")
dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])

errors = []
for d in dirs:
    md_path = os.path.join(skills_dir, d, "SKILL.md")
    if not os.path.exists(md_path):
        errors.append(f"Missing SKILL.md in {d}")
        continue
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        errors.append(f"Missing frontmatter marker in {d}")
        continue
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"Invalid frontmatter layout in {d}")
        continue
    try:
        data = yaml.safe_load(parts[1])
        if not isinstance(data, dict):
            errors.append(f"Frontmatter is not a mapping in {d}")
        elif data.get("name") != d:
            errors.append(f"Name mismatch in {d}: {data.get('name')} != {d}")
        elif not data.get("description", "").strip():
            errors.append(f"Empty description in {d}")
    except Exception as e:
        errors.append(f"YAML error in {d}: {e}")

if errors:
    for e in errors:
        print(f"[-] FAIL: {e}")
    sys.exit(1)
else:
    print(f"[+] PASS: Seluruh {len(dirs)} skill valid (YAML frontmatter, naming, description).")
    sys.exit(0)
EOF
) || true

echo "$PYTHON_FM_CHECK"
if [[ "$PYTHON_FM_CHECK" =~ "[-] FAIL" ]]; then
    FAILURES=$((FAILURES + 1))
fi

# ---------------------------------------------------------------------
# Check 3: CSS Viewport & Scroll Safety Audit
# ---------------------------------------------------------------------
echo "[*] [Check 3/5] Memeriksa proteksi CSS Viewport & Scroll Safety..."
PYTHON_CSS_CHECK=$(python3 - <<'EOF'
import os, sys

skills_dir = os.environ.get("SKILLS_DIR")
errors = []

for root, _, files in os.walk(skills_dir):
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as file:
                lines = file.readlines()
            for idx, line in enumerate(lines, 1):
                # Deteksi jika ada snippet yang mendikte overflow-x: hidden pada html, body
                if "overflow-x: hidden" in line and ("html" in line or "body" in line) and not (">" in line or "ANTI-PATTERN" in line or "BUKAN" in line or "never" in line):
                    errors.append(f"{p}:{idx} mengandung 'overflow-x: hidden' pada html/body")
                # Deteksi jika ada overscroll-behavior-y: contain pada html, body
                if "overscroll-behavior-y: contain" in line and not (">" in line or "ANTI-PATTERN" in line or "never" in line or "HANYA" in line):
                    errors.append(f"{p}:{idx} mengandung 'overscroll-behavior-y: contain' pada root")

if errors:
    for e in errors:
        print(f"[-] FAIL: {e}")
    sys.exit(1)
else:
    print("[+] PASS: Viewport CSS steril (bebas dari jebakan overflow-x: hidden pada html/body).")
    sys.exit(0)
EOF
) || true

echo "$PYTHON_CSS_CHECK"
if [[ "$PYTHON_CSS_CHECK" =~ "[-] FAIL" ]]; then
    FAILURES=$((FAILURES + 1))
fi

# ---------------------------------------------------------------------
# Check 4: Starter-App Smoke Test (FastAPI + SQLite WAL)
# ---------------------------------------------------------------------
echo "[*] [Check 4/5] Menjalankan smoke test starter-app..."
STARTER_DIR="$SCRIPT_DIR/examples/starter-app"
if [[ -f "$STARTER_DIR/test_smoke.py" ]]; then
    if (cd "$STARTER_DIR" && python3 test_smoke.py >/dev/null 2>&1); then
        echo "[+] PASS: Starter app smoke test lolos 100% (FastAPI + SQLite WAL Fortress)."
    else
        echo "[-] FAIL: Starter app smoke test gagal dieksekusi!"
        FAILURES=$((FAILURES + 1))
    fi
else
    echo "[-] FAIL: test_smoke.py tidak ditemukan!"
    FAILURES=$((FAILURES + 1))
fi

# ---------------------------------------------------------------------
# Check 5: OPSEC & Secret Scanner
# ---------------------------------------------------------------------
echo "[*] [Check 5/5] Memeriksa sanitasi OPSEC (kredensial & secret)..."
PYTHON_OPSEC_CHECK=$(python3 - <<'EOF'
import os, sys, re

base_dir = os.environ.get("SCRIPT_DIR")
patterns = [
    r'-----BEGIN [A-Z]+ PRIVATE KEY-----',
    r'ghp_[a-zA-Z0-9]{36}',
    r'xox[baprs]-[0-9a-zA-Z]{10,48}',
]

errors = []
for root, _, files in os.walk(base_dir):
    if ".git" in root or "__pycache__" in root:
        continue
    for f in files:
        p = os.path.join(root, f)
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                for pat in patterns:
                    if re.search(pat, content):
                        errors.append(f"Secret terdeteksi di {p}")
        except Exception:
            pass

if errors:
    for e in errors:
        print(f"[-] FAIL: {e}")
    sys.exit(1)
else:
    print("[+] PASS: OPSEC bersih (nol token/private key bocor).")
    sys.exit(0)
EOF
) || true

echo "$PYTHON_OPSEC_CHECK"
if [[ "$PYTHON_OPSEC_CHECK" =~ "[-] FAIL" ]]; then
    FAILURES=$((FAILURES + 1))
fi

# ---------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------
echo "====================================================================="
if [[ $FAILURES -eq 0 ]]; then
    echo "[+] SUCCESS: 5/5 verifikasi lolos tanpa kendala. Repositori siap rilis!"
    echo "====================================================================="
    exit 0
else
    echo "[-] FAILED: Ditemukan $FAILURES kegagalan verifikasi. Periksa log di atas!"
    echo "====================================================================="
    exit 1
fi
