#!/bin/bash
# claude-kit installer for macOS/Linux (also works in Git Bash on Windows). Safe to run again. No questions, no sudo, sets nothing global.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents/* -> ~/.claude/claude-kit/vault-mode/.claude/agents/   skills/* -> ~/.claude/claude-kit/vault-mode/.claude/skills/   mode/CLAUDE.md -> ~/.claude/claude-kit/vault-mode/CLAUDE.md
#   /load-vault copies the store's skills+agents into the CURRENT PROJECT's .claude/ (tools/vault-mode.py); /unload-vault removes exactly those copies.
#   ALWAYS-ON (the only kit skills in ~/.claude/skills, listed in mode/always-on.txt): load-vault unload-vault vault-update update-check uninstall
#   tools/* -> ~/.claude/claude-kit/tools/        systems/* -> ~/.claude/claude-kit/systems/        skillpack/* -> ~/.claude/claude-kit/skillpack/ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in ~/.claude/skills and /agents) is migrated by tools/vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# Kit wins: a target file the user changed is replaced by the kit version, no question. The user's version is first copied to ~/.claude/claude-kit/backup/<date>/<relpath>, so nothing is lost.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: bash install.sh [--home DIR] [--dry-run] [--with-hooks | --remove-hooks] [--with-mods]     (--home / env CLAUDE_KIT_HOME: install under DIR instead of $HOME, for tests)
#   --with-mods (opt-in): also install the /hud and /graph Claude Code plugins (plugins load in every session, so they are no longer installed by default).
#   --with-hooks / --remove-hooks (opt-in, never automatic): merge into / remove from ~/.claude/settings.json the two /low-usage-mode hooks and the vault-mentor suggestion hook (backup first, idempotent, keeps all other settings).
set -u
KIT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
H="${CLAUDE_KIT_HOME:-$HOME}"; DRY=0; HOOKS=""; MODS_ON=0
while [ $# -gt 0 ]; do
  case "$1" in --home) H="$2"; shift 2;; --dry-run) DRY=1; shift;; --with-hooks) HOOKS=install-hooks; shift;; --remove-hooks) HOOKS=uninstall-hooks; shift;; --with-mods) MODS_ON=1; shift;; *) shift;; esac
done
C="$H/.claude"; MAN="$C/claude-kit/installed.tsv"; TMP="$(mktemp "${TMPDIR:-/tmp}/claude-kit.XXXXXX")"
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
sha() { local o; o="$($SHA "$1")"; o="${o#\\}"; printf '%s' "${o%% *}"; }   # GNU sha256sum starts the line with a backslash when the file name contains one (Windows-style --home)
MANTXT=""; [ -s "$MAN" ] && MANTXT=1      # old manifest present: look entries up with awk
n_new=0; n_upd=0; n_same=0; n_repl=0; first_wf=0; BK="$C/claude-kit/backup/$(date +%Y-%m-%d)"
SM="claude-kit/vault-mode"; AO="load-vault unload-vault vault-update update-check uninstall"
[ -f "$KIT/mode/always-on.txt" ] && AO="$(grep -v '^#' "$KIT/mode/always-on.txt" | tr -d '\r' | tr '\n' ' ')"
[ -f "$MAN" ] || first_wf=1      # fresh install: print the welcome text at the end
# an older layout: keep its manifest for the migration step (only once; vault-mode.py migrate moves it into its backup folder)
if [ -f "$MAN" ] && [ ! -f "$C/$SM/layout.json" ] && [ ! -f "$C/claude-kit/installed.tsv.pre-mode" ] && [ $DRY = 0 ]; then cp "$MAN" "$C/claude-kit/installed.tsv.pre-mode"; fi

put() { # put <src> <rel under ~/.claude>
  local src="$1" rel="$2" dst="$C/$2" ns old rec ds="" t
  ns="$(sha "$src")"; old=""; rec="$ns"
  [ -n "$MANTXT" ] && old="$(awk -F'\t' -v r="$rel" '$1==r{print $2; exit}' "$MAN" 2>/dev/null)"
  [ -e "$dst" ] && ds="$(sha "$dst")"
  if [ ! -e "$dst" ]; then
    [ $DRY = 1 ] || { mkdir -p "$(dirname "$dst")"; cp "$src" "$dst"; }
    n_new=$((n_new+1))
  elif [ "$ds" = "$ns" ]; then
    n_same=$((n_same+1))
  elif [ -n "$old" ] && [ "$ds" = "$old" ]; then
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

# FAST PATH (default): one Python process does the whole copy loop (tools/kit-install-files.py; the shell loop below spawned ~7 processes per file: ~4 minutes on Git Bash).
FASTPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then FASTPY="$p"; break; fi; done
FASTDONE=0
if [ -n "$FASTPY" ] && [ -f "$KIT/tools/kit-install-files.py" ] && [ "${CLAUDE_KIT_SLOW:-0}" != 1 ]; then
  fo="$("$FASTPY" -I "$KIT/tools/kit-install-files.py" --kit "$KIT" --config "$C" --always-on "$AO" $([ $DRY = 1 ] && echo --dry-run) 2>&1)"
  case "$fo" in
    *"RESULT new="*) r="$(printf '%s\n' "$fo" | grep '^RESULT new=' | tail -1)"
       n_new="${r#*new=}"; n_new="${n_new%% *}"; n_upd="${r#*upd=}"; n_upd="${n_upd%% *}"; n_same="${r#*same=}"; n_same="${n_same%% *}"; n_repl="${r#*repl=}"; n_repl="${n_repl%% *}"; FASTDONE=1;;
    *) echo "claude-kit: fast installer failed, using the slow shell loop ($(printf '%s' "$fo" | tail -1 | cut -c1-160))";;
  esac
fi
if [ $FASTDONE = 0 ]; then
for sub in agents skills mode tools systems skillpack; do
  [ -d "$KIT/$sub" ] || continue
  while IFS= read -r f; do
    r="${f#$KIT/}"
    case "$sub" in
      tools|systems|skillpack) rel="claude-kit/$r";;
      agents) rel="$SM/.claude/$r";;
      mode) rel="$SM/${r#mode/}";;
      skills) nm="${r#skills/}"; nm="${nm%%/*}"; case " $AO " in *" $nm "*) rel="$r";; *) rel="$SM/.claude/$r";; esac;;
    esac
    put "$f" "$rel"
  done < <(find "$KIT/$sub" -type f ! -path '*/__pycache__/*' ! -name '*.pyc' | sort)
done

fi

if [ $DRY = 0 ]; then
  [ $FASTDONE = 1 ] || { mkdir -p "$(dirname "$MAN")"; sort -u "$TMP" > "$MAN"; }
  chmod +x "$C/claude-kit/tools/roblox-project-template/luau-check.sh" "$C/claude-kit/tools/studio-setup.sh" 2>/dev/null || true
fi
# move an older always-on layout into the store (idempotent; silent when there is nothing to move)
if [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/vault-mode.py" ]; then
  MPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then MPY="$p"; break; fi; done
  if [ -n "$MPY" ]; then CLAUDE_CONFIG_DIR="$C" "$MPY" -I "$C/claude-kit/tools/vault-mode.py" migrate --config "$C" 2>&1
  elif [ -f "$C/claude-kit/installed.tsv.pre-mode" ]; then echo "vault-mode: no working Python 3, so the old always-on kit skills were not moved; install Python 3 and run /vault-update"; fi
fi
rm -f "$TMP"
echo "claude-kit: installed $n_new new, updated $n_upd, unchanged $n_same, replaced-yours $n_repl (into $C)"
[ "$n_repl" -gt 0 ] && echo "claude-kit: replaced $n_repl of your edited files with the kit version (kit wins); your originals are saved under $BK"
if [ -n "$HOOKS" ]; then
  PY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then PY="$p"; break; fi; done
  if [ -z "$PY" ]; then echo "low-usage-mode hooks: skipped (no working Python 3)"
  elif [ $DRY = 1 ]; then echo "low-usage-mode hooks: dry run, settings.json not touched"
  elif [ ! -f "$C/$SM/.claude/skills/low-usage-mode/scripts/lum.py" ]; then echo "low-usage-mode hooks: skipped (skill not installed)"
  else CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/$SM/.claude/skills/low-usage-mode/scripts/lum.py" "$HOOKS" --config "$C"; fi
  # vault-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  if [ -n "$PY" ] && [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/mentor-hook.py" ]; then CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/claude-kit/tools/mentor-hook.py" "$HOOKS" --config "$C"; fi
fi
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
if [ -f "$KIT/tools/similar-skills.py" ]; then for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then "$p" -I "$KIT/tools/similar-skills.py" --kit "$KIT" --config "$C" 2>/dev/null; break; fi; done; fi
# kit mods (Claude Code plugins: /hud workflow tree, /graph vault graph) from <vault>/claude-kit/mods. OPT-IN (--with-mods): plugins load in every Claude session. Needs the claude CLI; idempotent (already installed = OK).
MODS="$KIT/mods"; MK="roblox-vault-kit-mods"
if [ -f "$MODS/.claude-plugin/marketplace.json" ] && [ $DRY = 0 ] && [ $MODS_ON = 1 ]; then
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
[ "$first_wf" = 1 ] && [ $DRY = 0 ] && echo "The Roblox Dev Mastery Vault kit is installed and OFF by default, so your other Claude sessions stay clean (nothing from the vault is loaded). In a Roblox project folder start Claude and type /load-vault: that session enters Roblox dev mode (the vault skills, agents, art-direction and visual-QA rules, reference images, learn step) and /unload-vault turns it off again. Always available: /load-vault /unload-vault /vault-update /update-check /uninstall. After /load-vault: /game-idea (one fresh idea) or /game-dev-workflow (idea, rating, plan, build); /make-roblox-game; judgement and your games (kept in the vault under Games/, never overwritten by updates): /game-dev-critic /game-dev-weekly /game-dev-launch-kit /game-dev-harvest /vault-contribute; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; looks (a game is never called done without it): /game-dev-art-direction /game-dev-visual-qa; mentor: /vault-mentor; research: /deep-topic-research; manager: /manager-mode; vault: /vault-update-clean /setup-check /light-mode-on /light-mode-off /kit-list; usage: /low-usage-mode. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)"
if [ "${CLAUDE_KIT_NOFOOTER:-0}" != 1 ]; then echo; echo ">>> Type /load-vault in a Roblox project folder to use the kit (then /kit-list shows everything it contains)."; fi
exit 0
