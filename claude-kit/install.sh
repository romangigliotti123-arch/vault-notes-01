#!/bin/bash
# claude-kit installer for macOS/Linux (also works in Git Bash on Windows). Safe to run again. No questions, no sudo, sets nothing global.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents/* -> ~/.claude/claude-kit/vault-mode/.claude/agents/   skills/* -> ~/.claude/claude-kit/vault-mode/.claude/skills/   mode/CLAUDE.md -> ~/.claude/claude-kit/vault-mode/CLAUDE.md
#   /rbx-load copies the store's skills+agents into the CURRENT PROJECT's .claude/ (tools/vault-mode.py); /rbx-unload removes exactly those copies.
#   COLD AREA: mode/cold/<topic>/* rides the mode/* mapping -> ~/.claude/claude-kit/vault-mode/cold/ (installed, refreshed, in installed.tsv, removed by uninstall; never copied into a project; read with tools/vault-mode.py cold).
#   ALWAYS-ON (the only kit skills in ~/.claude/skills, listed in mode/always-on.txt): rbx-load rbx-unload rbx-update rbx-check rbx-uninstall
#   tools/* -> ~/.claude/claude-kit/tools/        systems/* -> ~/.claude/claude-kit/systems/        skillpack/* -> ~/.claude/claude-kit/skillpack/ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in ~/.claude/skills and /agents) is migrated by tools/vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# The vault owns every file it installs: an install/update overwrites each one with the incoming version and removes files that left the kit (no keep, no conflicts). The only content that is yours is your project's Games/ and Models/ folders and anything outside the vault's own paths; nothing here touches them. claude-kit/state/ holds a few tiny settings (rbx-mockup on/off) that are never deleted.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: bash install.sh [--home DIR] [--dry-run] [--with-hooks | --remove-hooks] [--with-mods]     (--home / env CLAUDE_KIT_HOME: install under DIR instead of $HOME, for tests)
#   --with-mods (opt-in): also install the /rbx-subagent-hud and /rbx-graph Claude Code plugins (plugins load in every session, so they are no longer installed by default).
#   --with-hooks / --remove-hooks (opt-in, never automatic): merge into / remove from ~/.claude/settings.json the two /rbx-low-usage hooks and the rbx-mentor suggestion hook (backup first, idempotent, keeps all other settings).
set -u
KIT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
H="${CLAUDE_KIT_HOME:-$HOME}"; DRY=0; HOOKS=""; MODS_ON=0; HOME_GIVEN=0; [ -n "${CLAUDE_KIT_HOME:-}" ] && HOME_GIVEN=1
while [ $# -gt 0 ]; do
  case "$1" in --home) [ $# -ge 2 ] || { echo "install.sh: --home needs a folder" >&2; exit 2; }; H="$2"; HOME_GIVEN=1; shift 2;; --dry-run) DRY=1; shift;; --with-hooks) HOOKS=install-hooks; shift;; --remove-hooks) HOOKS=uninstall-hooks; shift;; --with-mods) MODS_ON=1; shift;; *) shift;; esac
done
C="$H/.claude"; [ $HOME_GIVEN = 0 ] && [ -n "${CLAUDE_CONFIG_DIR:-}" ] && C="$CLAUDE_CONFIG_DIR"
MAN="$C/claude-kit/installed.tsv"; TMP="$(mktemp "${TMPDIR:-/tmp}/claude-kit.XXXXXX" 2>/dev/null)" || TMP="${TMPDIR:-/tmp}/claude-kit.$$"
trap 'rm -f "$TMP"' EXIT
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
sha() { local o; o="$($SHA "$1")"; o="${o#\\}"; printf '%s' "${o%% *}"; }   # GNU sha256sum starts the line with a backslash when the file name contains one (Windows-style --home)
MANTXT=""; [ -s "$MAN" ] && MANTXT=1      # old manifest present: look entries up with awk
n_new=0; n_upd=0; n_same=0; n_gone=0; n_fail=0; first_wf=0
SM="claude-kit/vault-mode"; AO="rbx-load rbx-unload rbx-update rbx-check rbx-uninstall"
[ -f "$KIT/mode/always-on.txt" ] && AO="$(grep -v '^#' "$KIT/mode/always-on.txt" | tr -d '\r' | tr '\n' ' ')"
[ -f "$MAN" ] || first_wf=1      # fresh install: print the welcome text at the end
# an older layout: keep its manifest for the migration step (only once; vault-mode.py migrate moves it into its backup folder)
if [ -f "$MAN" ] && [ ! -f "$C/$SM/layout.json" ] && [ ! -f "$C/claude-kit/installed.tsv.pre-mode" ] && [ $DRY = 0 ]; then cp "$MAN" "$C/claude-kit/installed.tsv.pre-mode"; fi

# one-time rename migration (old generic command names -> <verb>-<slug>-vault; names in tools/vault-names.json): removes the OLD-named vault skills/agents that the kit installed and that are
# unchanged (backup + undo: kit-rename.py migrate --revert); never touches a skill/agent of yours with an old name. Runs BEFORE the copy so the old manifest still lists the old names. Silent when nothing is to do.
RENAME_MSG=""; RENAMED=0
if [ -f "$KIT/tools/kit-rename.py" ] && [ -s "$MAN" ]; then
  RPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then RPY="$p"; break; fi; done
  if [ -n "$RPY" ]; then
    if [ $DRY = 1 ]; then RENAME_MSG="$(CLAUDE_CONFIG_DIR="$C" "$RPY" -I "$KIT/tools/kit-rename.py" migrate --config "$C" --dry-run 2>&1)"
    else RENAME_MSG="$(CLAUDE_CONFIG_DIR="$C" "$RPY" -I "$KIT/tools/kit-rename.py" migrate --config "$C" 2>&1)"; fi
    if [ $MODS_ON = 1 ] && [ $DRY = 0 ]; then PL_MSG="$(CLAUDE_CONFIG_DIR="$C" "$RPY" -I "$KIT/tools/kit-rename.py" plugins --config "$C" 2>&1)"; [ -n "$PL_MSG" ] && echo "$PL_MSG"; fi   # enabledPlugins keys of the mods under their old names
    case "$RENAME_MSG" in *"commands renamed"*|*"commands merged"*) RENAMED=1;; esac
  else echo "kit-rename: no working Python 3, so old command names were not migrated; install Python 3 and run the update again"; fi
fi

cpf() { cp "$1" "$2" 2>/dev/null || { chmod u+w "$2" 2>/dev/null; cp "$1" "$2"; }; }
put() { # put <src> <rel under ~/.claude>: missing -> copy, identical -> same, anything else -> overwrite
  local src="$1" rel="$2" dst="$C/$2" ns ds="" old=""
  ns="$(sha "$src")"
  [ -n "$MANTXT" ] && old="$(awk -F'\t' -v r="$rel" '$1==r{print $2; exit}' "$MAN" 2>/dev/null)"
  [ -e "$dst" ] && ds="$(sha "$dst")"
  if [ ! -e "$dst" ]; then
    [ $DRY = 1 ] || { mkdir -p "$(dirname "$dst")" && cpf "$src" "$dst"; } || { echo "claude-kit: could not write $rel"; n_fail=$((n_fail+1)); [ -n "$old" ] && printf '%s\t%s\n' "$rel" "$old" >> "$TMP"; return; }
    n_new=$((n_new+1))
  elif [ "$ds" = "$ns" ]; then
    n_same=$((n_same+1))
  else
    [ $DRY = 1 ] || cpf "$src" "$dst" || { echo "claude-kit: could not write $rel"; n_fail=$((n_fail+1)); printf '%s\t%s\n' "$rel" "${old:-$ds}" >> "$TMP"; return; }
    n_upd=$((n_upd+1))
  fi
  printf '%s\t%s\n' "$rel" "$ns" >> "$TMP"
}

# FAST PATH (default): one Python process does the whole copy loop (tools/kit-install-files.py; the shell loop below spawned ~7 processes per file: ~4 minutes on Git Bash).
FASTPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then FASTPY="$p"; break; fi; done
FASTDONE=0
if [ -n "$FASTPY" ] && [ -f "$KIT/tools/kit-install-files.py" ] && [ "${CLAUDE_KIT_SLOW:-0}" != 1 ]; then
  fo="$("$FASTPY" -I "$KIT/tools/kit-install-files.py" --kit "$KIT" --config "$C" --always-on "$AO" $([ $DRY = 1 ] && echo --dry-run) 2>&1)"
  case "$fo" in
    *"RESULT new="*) r="$(printf '%s\n' "$fo" | grep '^RESULT new=' | tail -1)"
       n_new="${r#*new=}"; n_new="${n_new%% *}"; n_upd="${r#*upd=}"; n_upd="${n_upd%% *}"; n_same="${r#*same=}"; n_same="${n_same%% *}"
       n_gone="${r#*gone=}"; n_gone="${n_gone%% *}"; n_fail="${r#*fail=}"; n_fail="${n_fail%% *}"
       printf '%s\n' "$fo" | grep '^FAILED ' | head -5; FASTDONE=1;;
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

if [ $DRY = 0 ] && [ $FASTDONE = 0 ]; then   # fallback loop: files that left the kit are removed (the old manifest is still in $MAN here)
  if [ -n "$MANTXT" ] && [ -s "$MAN" ]; then
    cut -f1 "$TMP" | sort -u > "$TMP.rels" 2>/dev/null
    [ -s "$TMP.rels" ] || : > "$TMP.skip"
    while [ ! -e "$TMP.skip" ] && IFS="$(printf '\t')" read -r orel _; do
      case "$orel" in ""|/*|*..*|*:*|*"\\"*) continue;; esac
      case "$orel" in claude-kit/*) ;; skills/*) nm="${orel#skills/}"; nm="${nm%%/*}"; case " $AO " in *" $nm "*) ;; *) continue;; esac;; *) continue;; esac
      grep -qxF -- "$orel" "$TMP.rels" 2>/dev/null && continue
      if [ -f "$C/$orel" ] && [ ! -L "$C/$orel" ]; then rm -f "$C/$orel"; n_gone=$((n_gone+1)); d="$(dirname "$C/$orel")"; while [ "$d" != "$C" ] && [ "$d" != "$C/claude-kit" ] && [ "$d" != "$C/skills" ] && rmdir "$d" 2>/dev/null; do d="$(dirname "$d")"; done; fi
    done < "$MAN"
    rm -f "$TMP.rels" "$TMP.skip"
  fi
fi
if [ $DRY = 0 ]; then
  [ $FASTDONE = 1 ] || { mkdir -p "$(dirname "$MAN")"; sort -u "$TMP" > "$MAN"; }
  chmod +x "$C/claude-kit/tools/roblox-project-template/luau-check.sh" "$C/claude-kit/tools/studio-setup.sh" 2>/dev/null || true
fi
# move an older always-on layout into the store (idempotent; silent when there is nothing to move)
if [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/vault-mode.py" ]; then
  MPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then MPY="$p"; break; fi; done
  if [ -n "$MPY" ]; then CLAUDE_CONFIG_DIR="$C" "$MPY" -I "$C/claude-kit/tools/vault-mode.py" migrate --config "$C" 2>&1
  elif [ -f "$C/claude-kit/installed.tsv.pre-mode" ]; then echo "vault-mode: no working Python 3, so the old always-on kit skills were not moved; install Python 3 and run /rbx-update"; fi
fi
rm -f "$TMP"
# folders that have Roblox dev mode loaded: swap the old-named copies for the new-named ones (vault-mode.py sync is idempotent)
if [ $RENAMED = 1 ] && [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/vault-mode.py" ]; then
  MPY2=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then MPY2="$p"; break; fi; done
  [ -n "$MPY2" ] && CLAUDE_CONFIG_DIR="$C" "$MPY2" -I "$C/claude-kit/tools/vault-mode.py" sync --config "$C" 2>&1
fi
echo "claude-kit: installed $n_new new, updated $n_upd, unchanged $n_same$([ "$n_gone" -gt 0 ] && echo ", removed $n_gone no longer in the kit")$([ "$n_fail" -gt 0 ] && echo ", FAILED $n_fail") (into $C)"
[ -n "$RENAME_MSG" ] && printf '%s\n' "$RENAME_MSG"
# UI mockups default to automatic design-first: ONE non-blocking NOTICE FOR THE USER line per install (marker claude-kit/ui-mockup-notice.done); a fresh install only sets the marker (the setup text asks the question)
if [ $DRY = 0 ] && [ -f "$KIT/tools/ui_pref.py" ]; then
  UPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then UPY="$p"; break; fi; done
  if [ -n "$UPY" ]; then
    UIARG=""; [ "$first_wf" = 1 ] && UIARG="--mark-only"
    UIM="$(CLAUDE_CONFIG_DIR="$C" "$UPY" -I "$KIT/tools/ui_pref.py" notice $UIARG 2>/dev/null)"; [ -n "$UIM" ] && printf '%s\n' "$UIM"
  fi
fi
if [ -n "$HOOKS" ]; then
  PY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then PY="$p"; break; fi; done
  if [ -z "$PY" ]; then echo "rbx-low-usage hooks: skipped (no working Python 3)"
  elif [ $DRY = 1 ]; then echo "rbx-low-usage hooks: dry run, settings.json not touched"
  elif [ ! -f "$C/$SM/.claude/skills/rbx-low-usage/scripts/lum.py" ]; then echo "rbx-low-usage hooks: skipped (skill not installed)"
  else CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/$SM/.claude/skills/rbx-low-usage/scripts/lum.py" "$HOOKS" --config "$C"; fi
  # rbx-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  if [ -n "$PY" ] && [ $DRY = 0 ] && [ -f "$C/claude-kit/tools/mentor-hook.py" ]; then CLAUDE_CONFIG_DIR="$C" "$PY" -I "$C/claude-kit/tools/mentor-hook.py" "$HOOKS" --config "$C"; fi
fi
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
if [ -f "$KIT/tools/similar-skills.py" ]; then for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then "$p" -I "$KIT/tools/similar-skills.py" --kit "$KIT" --config "$C" 2>/dev/null; break; fi; done; fi
# kit mods (Claude Code plugins: /rbx-subagent-hud workflow tree, /rbx-graph vault graph) from <vault>/claude-kit/mods. OPT-IN (--with-mods): plugins load in every Claude session. Needs the claude CLI; idempotent (already installed = OK).
MODS="$KIT/mods"; MK="roblox-vault-kit-mods"
if [ -f "$MODS/.claude-plugin/marketplace.json" ] && [ $DRY = 0 ] && [ $MODS_ON = 1 ]; then
  if command -v claude >/dev/null 2>&1; then
    ok=1; why=""; export CLAUDE_CONFIG_DIR="$C"
    lst="$(claude plugin list --json 2>&1)"; have=0
    if printf '%s' "$lst" | grep -q "rbx-subagent-hud@$MK" && printf '%s' "$lst" | grep -q "rbx-graph@$MK"; then have=1; fi
    # plugins installed under their previous names (before the vault-suffixed rename): uninstall them, refresh the marketplace listing, install the new ones below
    oldmods=0; for om in workflow-hud vault-graph hud-rbxdev-vault graph-rbxdev-vault rbx-subagent-hud; do if printf '%s' "$lst" | grep -q "$om@$MK"; then claude plugin uninstall "$om@$MK" >/dev/null 2>&1; oldmods=1; fi; done  # legacy plugin names
    [ $oldmods = 1 ] && { claude plugin marketplace update "$MK" >/dev/null 2>&1; have=0; }   # REL4: a plugin was uninstalled above (rbx-subagent-hud is in the list on purpose, to refresh it): install both again, never leave one missing
    if [ $have = 0 ]; then
      r="$(claude plugin marketplace add "$MODS" 2>&1)" || { printf '%s' "$r" | grep -qi already || { ok=0; why="marketplace add failed"; }; }
      for m in rbx-subagent-hud rbx-graph; do
        [ $ok = 1 ] || break
        r="$(claude plugin install "$m@$MK" 2>&1)" || { printf '%s' "$r" | grep -qi already || { ok=0; why="install of $m failed"; }; }
      done
    fi
    if [ $ok = 1 ]; then   # SM: copy semantics: a plugin that was already installed keeps its old copy until updated (rbx-graph 0.2.0 = link only)
      claude plugin marketplace update "$MK" >/dev/null 2>&1
      for m in rbx-subagent-hud rbx-graph; do claude plugin update "$m@$MK" >/dev/null 2>&1; done
    fi
    if [ $ok = 1 ]; then echo "mods: rbx-subagent-hud (/rbx-subagent-hud), rbx-graph (/rbx-graph): installed"
    else echo "mods: not installed ($why). In a Claude session run: /plugin marketplace add $MODS  then  /plugin install rbx-subagent-hud@$MK  and  /plugin install rbx-graph@$MK  then  /reload-plugins"; fi
  else
    echo "mods: claude CLI not found. In a Claude session run: /plugin marketplace add $MODS  then  /plugin install rbx-subagent-hud@$MK  and  /plugin install rbx-graph@$MK  then  /reload-plugins"
  fi
fi
# legacy kit-mod plugins (workflow-hud, vault-graph, hud-rbxdev-vault, graph-rbxdev-vault from marketplace roblox-vault-kit-mods; the marketplace now lists only rbx-subagent-hud and rbx-graph) make "not found in marketplace" load errors.
# On EVERY run without --with-mods (with it, the mods block above already did this): uninstall them with the claude CLI (best effort, never fails the update, silent without the CLI or without legacy plugins).
if [ $DRY = 0 ] && [ $MODS_ON = 0 ] && command -v claude >/dev/null 2>&1; then
  lst="$(CLAUDE_CONFIG_DIR="$C" claude plugin list --json 2>/dev/null)"; oldmods=0
  for om in workflow-hud vault-graph hud-rbxdev-vault graph-rbxdev-vault; do if printf '%s' "$lst" | grep -q "$om@roblox-vault-kit-mods"; then CLAUDE_CONFIG_DIR="$C" claude plugin uninstall "$om@roblox-vault-kit-mods" >/dev/null 2>&1; oldmods=1; fi; done  # legacy plugin names
  if [ $oldmods = 1 ]; then
    for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then CLAUDE_CONFIG_DIR="$C" "$p" -I "$KIT/tools/kit-rename.py" plugins --drop-legacy --config "$C" >/dev/null 2>&1; break; fi; done
    if ! { printf '%s' "$lst" | grep -q "rbx-subagent-hud@roblox-vault-kit-mods" && printf '%s' "$lst" | grep -q "rbx-graph@roblox-vault-kit-mods"; }; then echo "Old vault plugins removed. To add the HUD and graph: run the installer with --with-mods (claude-kit/install.sh --with-mods or install.ps1 -WithMods), then /reload-plugins."; fi
  fi
fi
[ "$first_wf" = 1 ] && [ $DRY = 0 ] && echo "The Roblox Dev Mastery Vault kit is installed and OFF by default, so your other Claude sessions stay clean (nothing from the vault is loaded). In a Roblox project folder start Claude and type /rbx-load: that session enters Roblox dev mode (the vault skills, agents, art-direction, placement, lighting and visual-QA rules, reference images) and /rbx-unload turns it off again. Always available: /rbx-load /rbx-unload /rbx-update /rbx-check /rbx-uninstall. After /rbx-load: /rbx-idea-quick (one fresh idea) or /rbx-workflow (idea, rating, plan, build); /rbx-make; judgement and your games (in your project's Games/ folder, never touched by updates): /rbx-critic /rbx-weekly /rbx-launch-kit /rbx-harvest; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; placement, lighting and looks (a game is never called done without them): /rbx-placement /rbx-lighting /rbx-art /rbx-visual; measure the vault itself: /rbx-bench; mentor: /rbx-mentor; research: /rbx-research; manager: /rbx-manager; vault: /rbx-clean /rbx-setup /rbx-light-on /rbx-light-off /rbx-list; usage: /rbx-low-usage. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)"
if [ "${CLAUDE_KIT_NOFOOTER:-0}" != 1 ]; then echo; echo ">>> Type /rbx-load in a Roblox project folder to use the kit (then /rbx-list shows everything it contains)."; fi
[ "$n_fail" -gt 0 ] && exit 1
exit 0
