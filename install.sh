#!/usr/bin/env bash
set -e

REPO="https://raw.githubusercontent.com/SpritexAI/hello-coder/main"
SKILLS=("planning" "ui" "debug" "decisions" "workflow" "review" "testing")
PROFILES=("frontend" "backend" "fullstack")
INSTALLED=0

echo ""
echo "👷 Hello Coder — Installing skills..."
echo ""

download_skills() {
  local dest="$1"
  mkdir -p "$dest/skills" "$dest/profiles"

  for skill in "${SKILLS[@]}"; do
    curl -fsSL "$REPO/skills/$skill.md" -o "$dest/skills/$skill.md"
  done

  for profile in "${PROFILES[@]}"; do
    curl -fsSL "$REPO/profiles/$profile.md" -o "$dest/profiles/$profile.md"
  done
}

# Claude Code
if command -v claude &>/dev/null || [ -f "$HOME/.claude/CLAUDE.md" ]; then
  DIR="$HOME/.claude/hello-coder"
  download_skills "$DIR"
  curl -fsSL "$REPO/CLAUDE.md" -o "$HOME/.claude/CLAUDE.md"
  echo "✓ Claude Code — installed"
  INSTALLED=$((INSTALLED + 1))
fi

# Cursor
if [ -d "$HOME/.cursor" ]; then
  DIR="$HOME/.cursor/hello-coder"
  download_skills "$DIR"
  echo "✓ Cursor — installed"
  INSTALLED=$((INSTALLED + 1))
fi

# Windsurf
if [ -d "$HOME/.windsurf" ]; then
  DIR="$HOME/.windsurf/hello-coder"
  download_skills "$DIR"
  echo "✓ Windsurf — installed"
  INSTALLED=$((INSTALLED + 1))
fi

# Gemini CLI
if command -v gemini &>/dev/null || [ -f "$HOME/.gemini/GEMINI.md" ]; then
  DIR="$HOME/.gemini/hello-coder"
  download_skills "$DIR"
  curl -fsSL "$REPO/GEMINI.md" -o "$HOME/.gemini/GEMINI.md"
  echo "✓ Gemini CLI — installed"
  INSTALLED=$((INSTALLED + 1))
fi

# Codex
if command -v codex &>/dev/null || [ -f "$HOME/.codex/AGENTS.md" ]; then
  DIR="$HOME/.codex/hello-coder"
  download_skills "$DIR"
  curl -fsSL "$REPO/AGENTS.md" -o "$HOME/.codex/AGENTS.md"
  echo "✓ Codex — installed"
  INSTALLED=$((INSTALLED + 1))
fi

# Cline
if [ -d "$HOME/.cline" ]; then
  DIR="$HOME/.cline/hello-coder"
  download_skills "$DIR"
  echo "✓ Cline — installed"
  INSTALLED=$((INSTALLED + 1))
fi

echo ""

if [ "$INSTALLED" -eq 0 ]; then
  echo "⚠ No supported agents found on this machine."
  echo ""
  echo "Manual install — add this to your agent's context file:"
  echo "  Read and apply all skills from hello-coder/profiles/fullstack.md before starting any task."
else
  echo "✓ Hello Coder installed for $INSTALLED agent(s)."
fi

echo ""
echo "👷 Done. Your agents now behave like senior developers."
echo "   → https://github.com/SpritexAI/hello-coder"
echo ""
