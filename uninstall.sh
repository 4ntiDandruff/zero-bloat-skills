#!/usr/bin/env bash
# =====================================================================
# ZERO-BLOAT-SKILLS — Uninstaller Aman (Pencabutan Symlink)
# Megapass Intra Solusindo • Sidoarjo, Indonesia
# =====================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

echo "[*] Mencabut symlink zero-bloat-skills secara aman..."

TARGET_DIRS=(
    "$HOME/.gemini/config/skills"
    "$HOME/.claude/skills"
    "$HOME/.config/everything-claude-code/skills"
    "$HOME/.omp/skills"
    "$HOME/.config/opencode/skills"
    "$HOME/.hermes/skills"
    "$HOME/.codex/skills"
)

REMOVED_COUNT=0

for TARGET in "${TARGET_DIRS[@]}"; do
    if [[ -d "$TARGET" ]]; then
        for SKILL_PATH in "$SKILLS_DIR"/*; do
            if [[ -d "$SKILL_PATH" ]]; then
                SKILL_NAME="$(basename "$SKILL_PATH")"
                TARGET_LINK="$TARGET/$SKILL_NAME"
                
                # Cabut HANYA jika file tersebut benar adalah symlink ke repo ini
                if [[ -L "$TARGET_LINK" ]]; then
                    DEST="$(readlink "$TARGET_LINK" || true)"
                    if [[ "$DEST" == "$SKILL_PATH" ]]; then
                        rm -f "$TARGET_LINK"
                        REMOVED_COUNT=$((REMOVED_COUNT + 1))
                    fi
                fi
            fi
        done
    fi
done

echo "[+] $REMOVED_COUNT symlink berhasil dicabut tanpa merusak skill lainnya."
