#!/usr/bin/env bash
# =====================================================================
# ZERO-BLOAT-SKILLS — Universal Multi-Agent Symlink Installer & Updater
# Megapass Intra Solusindo • Sidoarjo, Indonesia
# =====================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

# Tampilkan panduan jika parameter --help diberikan
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    echo "Usage: $0 [OPTION]"
    echo ""
    echo "Options:"
    echo "  (no args)    Install and symlink all 16 skills to detected AI coding agents"
    echo "  --update, -u Pull latest updates from Git repository and refresh symlinks"
    echo "  --help, -h   Display this help message"
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

# Target direktori skills untuk masing-masing agent coding AI
TARGET_DIRS=(
    "$HOME/.gemini/config/skills"
    "$HOME/.claude/skills"
    "$HOME/.config/everything-claude-code/skills"
    "$HOME/.omp/skills"
    "$HOME/.config/opencode/skills"
    "$HOME/.hermes/skills"
    "$HOME/.codex/skills"
)

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
                
                # Buat symlink atomik (-sfn: symbolic, force, no-dereference)
                ln -sfn "$SKILL_PATH" "$TARGET_LINK"
                LINKED_COUNT=$((LINKED_COUNT + 1))
            fi
        done
        echo "    └─ 16 skills symlinked to $TARGET"
    fi
done

echo ""
echo "====================================================================="
echo "[+] SUCCESS: $LINKED_COUNT symlinks actively configured."
echo "[+] All detected coding agents are now equipped with zero-bloat-skills."
echo "====================================================================="
