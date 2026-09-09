#!/usr/bin/env bash
# =====================================================================
# ZERO-BLOAT-SKILLS — Universal Multi-Agent Symlink Installer
# Megapass Intra Solusindo • Sidoarjo, Indonesia
# =====================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

echo "[*] Menjalankan installer universal zero-bloat-skills..."
echo "[*] Sumber skill: $SKILLS_DIR"

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
        echo "[+] Terdeteksi platform di: $TARGET"
        
        for SKILL_PATH in "$SKILLS_DIR"/*; do
            if [[ -d "$SKILL_PATH" ]]; then
                SKILL_NAME="$(basename "$SKILL_PATH")"
                TARGET_LINK="$TARGET/$SKILL_NAME"
                
                # Buat symlink atomik (-sfn: symbolic, force, no-dereference)
                ln -sfn "$SKILL_PATH" "$TARGET_LINK"
                LINKED_COUNT=$((LINKED_COUNT + 1))
            fi
        done
        echo "    └─ 16 skill berhasil di-symlink ke $TARGET"
    fi
done

echo ""
echo "====================================================================="
echo "[+] PEMASANGAN SELESAI: $LINKED_COUNT symlink berhasil dipasang."
echo "[+] Seluruh platform AI kini dapat memuat zero-bloat-skills otomatis."
echo "====================================================================="
