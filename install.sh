#!/usr/bin/env bash
# =====================================================================
# ZERO-BLOAT-SKILLS — Universal Multi-Agent Symlink Installer & Updater
# Megapass Intra Solusindo • Sidoarjo, Indonesia
# =====================================================================
set -euo pipefail

export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export SKILLS_DIR="$SCRIPT_DIR/skills"

# Target direktori skills untuk masing-masing agent coding AI
TARGET_DIRS=(
    "$HOME/.gemini/config/skills"
    "$HOME/.agents/skills"
    "$HOME/.claude/skills"
    "$HOME/.config/everything-claude-code/skills"
    "$HOME/.omp/skills"
    "$HOME/.config/omp/skills"
    "$HOME/.config/opencode/skills"
    "$HOME/.hermes/skills"
    "$HOME/.codex/skills"
)

# Panduan CLI
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    echo "Usage: $0 [OPTION]"
    echo ""
    echo "Options:"
    echo "  (no args)    Install and symlink all zero-bloat skills to detected AI coding agents"
    echo "  --list, -l   Display catalog of all 23 available zero-bloat skills"
    echo "  --verify, -v Verify health and integrity of active symlinks across agents"
    echo "  --test, -t   Run 5-layer health check test suite (./test.sh)"
    echo "  --update, -u Pull latest updates from Git repository and refresh symlinks"
    echo "  --help, -h   Display this help message"
    exit 0
fi

# Katalog Skill
if [[ "${1:-}" == "--list" || "${1:-}" == "-l" ]]; then
    echo "====================================================================="
    echo "ZERO-BLOAT-SKILLS — Available Skills Catalog (23 Modules)"
    echo "====================================================================="
    python3 - <<'EOF'
import os, yaml

skills_dir = os.environ.get("SKILLS_DIR", "skills")
dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
for i, d in enumerate(dirs, 1):
    md_path = os.path.join(skills_dir, d, "SKILL.md")
    desc = "-"
    if os.path.exists(md_path):
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    data = yaml.safe_load(parts[1])
                    desc = data.get("description", "-")
        except Exception:
            pass
    print(f"[{i:02d}] {d}")
    print(f"     -> {desc[:90]}...")
EOF
    echo "====================================================================="
    exit 0
fi

# Eksekusi Test Suite
if [[ "${1:-}" == "--test" || "${1:-}" == "-t" ]]; then
    if [[ -x "$SCRIPT_DIR/test.sh" ]]; then
        exec "$SCRIPT_DIR/test.sh"
    else
        bash "$SCRIPT_DIR/test.sh"
        exit $?
    fi
fi

# Verifikasi Kesehatan Symlink
if [[ "${1:-}" == "--verify" || "${1:-}" == "-v" ]]; then
    echo "====================================================================="
    echo "[*] Memeriksa integritas symlink zero-bloat-skills di cluster ruko..."
    echo "====================================================================="
    TOTAL_VALID=0
    TOTAL_BROKEN=0
    
    for TARGET in "${TARGET_DIRS[@]}"; do
        if [[ -d "$TARGET" ]]; then
            VALID_IN_TARGET=0
            BROKEN_IN_TARGET=0
            for SKILL_PATH in "$SKILLS_DIR"/*; do
                if [[ -d "$SKILL_PATH" ]]; then
                    SKILL_NAME="$(basename "$SKILL_PATH")"
                    TARGET_LINK="$TARGET/$SKILL_NAME"
                    if [[ -L "$TARGET_LINK" ]]; then
                        if [[ -e "$TARGET_LINK" ]]; then
                            VALID_IN_TARGET=$((VALID_IN_TARGET + 1))
                        else
                            BROKEN_IN_TARGET=$((BROKEN_IN_TARGET + 1))
                        fi
                    fi
                fi
            done
            TOTAL_VALID=$((TOTAL_VALID + VALID_IN_TARGET))
            TOTAL_BROKEN=$((TOTAL_BROKEN + BROKEN_IN_TARGET))
            echo "[+] $TARGET:"
            echo "    └─ $VALID_IN_TARGET active symlinks | $BROKEN_IN_TARGET broken"
        fi
    done
    
    echo "====================================================================="
    if [[ $TOTAL_BROKEN -eq 0 ]]; then
        echo "[+] STATUS: PRIMA ($TOTAL_VALID symlinks sehat, nol broken link)."
    else
        echo "[-] WARNING: Ditemukan $TOTAL_BROKEN broken symlink. Jalankan './install.sh' untuk pemulihan."
    fi
    echo "====================================================================="
    exit 0
fi

# Jalankan pembaruan Git jika parameter --update diberikan
if [[ "${1:-}" == "--update" || "${1:-}" == "-u" ]]; then
    echo "[*] Pulling latest updates from upstream repository..."
    if [[ -d "$SCRIPT_DIR/.git" ]]; then
        git -C "$SCRIPT_DIR" pull origin main
        echo "[+] Git repository updated successfully."
    else
        echo "[!] Warning: .git directory not found. Skipping git pull."
    fi
    echo ""
fi

echo "[*] Installing/refreshing zero-bloat-skills symlinks..."
echo "[*] Source path: $SKILLS_DIR"

LINKED_COUNT=0

for TARGET in "${TARGET_DIRS[@]}"; do
    PARENT_DIR="$(dirname "$TARGET")"
    
    # Pasang HANYA jika platform agent tersebut terpasang / foldernya ada di sistem
    if [[ -d "$PARENT_DIR" || -d "$TARGET" ]]; then
        mkdir -p "$TARGET"
        echo "[+] Detected active AI platform environment: $TARGET"
        
        for SKILL_PATH in "$SKILLS_DIR"/*; do
            if [[ -d "$SKILL_PATH" ]]; then
                SKILL_NAME="$(basename "$SKILL_PATH")"
                TARGET_LINK="$TARGET/$SKILL_NAME"
                
                # Buat symlink atomik (hapus link lama dulu agar tidak bersarang)
                rm -f "$TARGET_LINK" 2>/dev/null || true
                ln -s "$SKILL_PATH" "$TARGET_LINK"
                LINKED_COUNT=$((LINKED_COUNT + 1))
            fi
        done
        SKILL_COUNT=$(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l)
        echo "    └─ $SKILL_COUNT skills symlinked to $TARGET"
    fi
done

echo ""
echo "====================================================================="
echo "[+] SUCCESS: $LINKED_COUNT symlinks actively configured."
echo "[+] All detected coding agents are now equipped with zero-bloat-skills."
echo "====================================================================="
