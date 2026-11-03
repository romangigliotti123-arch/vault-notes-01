#!/bin/bash
# claude-kit installer for macOS/Linux (also works in Git Bash on Windows). Safe to run again. No questions, no sudo, sets nothing global.
#   agents/*  -> ~/.claude/agents/        skills/*  -> ~/.claude/skills/        tools/* -> ~/.claude/claude-kit/tools/        systems/* -> ~/.claude/claude-kit/systems/        skillpack/* -> ~/.claude/claude-kit/skillpack/ (NOT skills: opened on demand by the /rbx router skill)
# Kit wins: a target file the user changed is replaced by the kit version, no question. The user's version is first copied to ~/.claude/claude-kit/backup/<date>/<relpath>, so nothing is lost.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: bash install.sh [--home DIR] [--dry-run] [--with-hooks | --remove-hooks]     (--home / env CLAUDE_KIT_HOME: install under DIR instead of $HOME, for tests)
#   --with-hooks / --remove-hooks (opt-in, never automatic): merge into / remove from ~/.claude/settings.json the two /low-usage-mode hooks and the vault-mentor suggestion hook (backup first, idempotent, keeps all other settings).
set -u
KIT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
H="${CLAUDE_KIT_HOME:-$HOME}"; DRY=0; HOOKS=""
while [ $# -gt 0 ]; do
  case "$1" in --home) H="$2"; shift 2;; --dry-run) DRY=1; shift;; --with-hooks) HOOKS=install-hooks; shift;; --remove-hooks) HOOKS=uninstall-hooks; shift;; *) shift;; esac
done
C="$H/.claude"; MAN="$C/claude-kit/installed.tsv"; TMP="$(mktemp)"
sha() { if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -d' ' -f1; else shasum -a 256 "$1" | cut -d' ' -f1; fi; }
n_new=0; n_upd=0; n_same=0; n_repl=0; first_wf=0; BK="$C/claude-kit/backup/$(date +%Y-%m-%d)"

put() { # put <src> <rel under ~/.claude>
  local src="$1" rel="$2" dst="$C/$2" ns old rec
  ns="$(sha "$src")"; old="$(awk -F'\t' -v r="$rel" '$1==r{print $2}' "$MAN" 2>/dev/null | head -1)"; rec="$ns"
  if [ ! -e "$dst" ]; then
    [ "$rel" = "skills/game-dev-workflow/SKILL.md" ] && first_wf=1
    [ $DRY = 1 ] || { mkdir -p "$(dirname "$dst")"; cp "$src" "$dst"; }
    n_new=$((n_new+1))
  elif [ "$(sha "$dst")" = "$ns" ]; then
    n_same=$((n_same+1))
  elif [ -n "$old" ] && [ "$(sha "$dst")" = "$old" ]; then
    [ $DRY = 1 ] || cp "$src" "$dst"
    n_upd=$((n_upd+1))
  else
    if [ $DRY = 0 ]; then
      bk="$BK/$rel"; i=1; while [ -e "$bk" ]; do i=$((i+1)); bk="$BK/$rel.$i"; done
      mkdir -p "$(dirname "$bk")"; cp -p "$dst" "$bk"; cp "$src" "$dst"
    fi
    n_repl=$((n_repl+1))
  fi
  [ -n "$rec" ] && printf '%s\t%s\n' "$rel" "$rec" >> "$TMP"
}

for sub in agents skills tools systems skillpack; do
  [ -d "$KIT/$sub" ] || continue
  while IFS= read -r f; do
    r="${f#$KIT/}"
    case "$sub" in tools|systems|skillpack) rel="claude-kit/$r";; *) rel="$r";; esac
    put "$f" "$rel"
  done < <(find "$KIT/$sub" -type f ! -path '*/__pycache__/*' ! -name '*.pyc' | sort)
done

if [ $DRY = 0 ]; then
  mkdir -p "$(dirname "$MAN")"; sort -u "$TMP" > "$MAN"
  chmod +x "$C/claude-kit/tools/roblox-project-template/luau-check.sh" "$C/claude-kit/tools/studio-setup.sh" 2>/dev/null || true
fi
rm -f "$TMP"
echo "claude-kit: installed $n_new new, updated $n_upd, unchanged $n_same, replaced-yours $n_repl (into $C)"
[ "$n_repl" -gt 0 ] && echo "claude-kit: replaced $n_repl of your edited files with the kit version (kit wins); your originals are saved under $BK"
if [ -n "$HOOKS" ]; then
  PY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then PY="$p"; break; fi; done
  if [ -z "$PY" ]; then echo "low-usage-mode hooks: skipped (no working Python 3)"
  elif [ $DRY = 1 ]; then echo "low-usage-mode hooks: dry run, settings.json not touched"
  elif [ ! -f "$C/skills/low-usage-mode/scripts/lum.py" ]; then echo "low-usage-mode hooks: skipped (skill not installed)"
  else CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/skills/low-usage-mode/scripts/lum.py" "$HOOKS" --config "$C"; fi
  # vault-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  if [ -n "$PY" ] && [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/mentor-hook.py" ]; then CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/claude-kit/tools/mentor-hook.py" "$HOOKS" --config "$C"; fi
fi
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
if [ -f "$KIT/tools/similar-skills.py" ]; then for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then "$p" -I "$KIT/tools/similar-skills.py" --kit "$KIT" --config "$C" 2>/dev/null; break; fi; done; fi
# kit mods (Claude Code plugins: /hud workflow tree, /graph vault graph) from <vault>/claude-kit/mods. Needs the claude CLI; idempotent (already installed = OK).
MODS="$KIT/mods"; MK="roblox-vault-kit-mods"
if [ -f "$MODS/.claude-plugin/marketplace.json" ] && [ $DRY = 0 ]; then
  if command -v claude >/dev/null 2>&1; then
    ok=1; why=""; export CLAUDE_CONFIG_DIR="$C"
    lst="$(claude plugin list --json 2>&1)"; have=0
    if printf '%s' "$lst" | grep -q "workflow-hud@$MK" && printf '%s' "$lst" | grep -q "vault-graph@$MK"; then have=1; fi
    if [ $have = 0 ]; then
      r="$(claude plugin marketplace add "$MODS" 2>&1)" || { printf '%s' "$r" | grep -qi already || { ok=0; why="marketplace add failed"; }; }
      for m in workflow-hud vault-graph; do
        [ $ok = 1 ] || break
        r="$(claude plugin install "$m@$MK" 2>&1)" || { printf '%s' "$r" | grep -qi already || { ok=0; why="install of $m failed"; }; }
      done
    fi
    if [ $ok = 1 ]; then echo "mods: workflow-hud (/hud), vault-graph (/graph): installed"
    else echo "mods: not installed ($why). In a Claude session run: /plugin marketplace add $MODS  then  /plugin install workflow-hud@$MK  and  /plugin install vault-graph@$MK  then  /reload-plugins"; fi
  else
    echo "mods: claude CLI not found. In a Claude session run: /plugin marketplace add $MODS  then  /plugin install workflow-hud@$MK  and  /plugin install vault-graph@$MK  then  /reload-plugins"
  fi
fi
[ "$first_wf" = 1 ] && [ $DRY = 0 ] && echo "The Roblox Dev Mastery Vault is now set up. Start a new Claude session and run /game-idea (one fresh idea) or /game-dev-workflow (idea, rating, plan, build). Judgement and your games (kept in the vault under Games/, never overwritten by updates): /game-dev-critic /game-dev-weekly /game-dev-launch-kit /game-dev-harvest /vault-contribute. Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>. Side skills: /game-dev-rate /game-dev-plan /game-dev-ads /game-dev-update /game-dev-playtest /game-dev-thumbnail; looks (a game is never called done without it): /game-dev-art-direction /game-dev-visual-qa; mentor (start here): /vault-mentor (works with you on any job and suggests the right skill, agent or note at each step); research: /deep-topic-research; find skills and agents: /use-the-ai-library; manager: /manager-mode; vault: /vault-update /vault-update-clean /update-check (newer version? changes nothing) /setup-check (missing software + install commands) /light-mode-on /light-mode-off; usage: /low-usage-mode. How it works: the vault Roblox knowledge base feeds the agents; /game-dev-workflow elaborates, rates and plans your idea, then builds it after you say Ready to build. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)"
if [ "${CLAUDE_KIT_NOFOOTER:-0}" != 1 ]; then echo; echo ">>> Use /kit-list to see all the new installed skills, agents and mods (one line each)."; fi
exit 0
