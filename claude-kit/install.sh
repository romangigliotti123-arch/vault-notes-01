#!/bin/bash
# claude-kit installer for macOS/Linux (also works in Git Bash on Windows). Safe to run again. No questions, no sudo, sets no environment variables or shell profiles; the two mods (see MODS below) are the one thing that touches your Claude plugin settings.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents/* -> ~/.claude/claude-kit/vault-mode/.claude/agents/   skills/* -> ~/.claude/claude-kit/vault-mode/.claude/skills/   mode/CLAUDE.md -> ~/.claude/claude-kit/vault-mode/CLAUDE.md
#   The VAULT FOLDER (the notes clone, e.g. ~/Obsidian/claudes-vault) is permanently loaded: tools/vault-mode.py load --project <vault> (run here at the end, quietly, and by every update) copies the store's skills+agents+rules into <vault>/.claude/, hidden from git together with Games/, Models/, My-Skills/ and My-Agents/ (your own skills and agents are copied in too; the vault never changes those folders). Older loaded project folders are cleaned. No load/unload commands exist.
#   COLD AREA: mode/cold/<topic>/* rides the mode/* mapping -> ~/.claude/claude-kit/vault-mode/cold/ (installed, refreshed, in installed.tsv, removed by uninstall; never copied into a folder; read with tools/vault-mode.py cold).
#   ALWAYS-ON (the only kit skills in ~/.claude/skills, listed in mode/always-on.txt): rbx-update rbx-check rbx-uninstall
#   tools/* -> ~/.claude/claude-kit/tools/        systems/* -> ~/.claude/claude-kit/systems/        skillpack/* -> ~/.claude/claude-kit/skillpack/ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in ~/.claude/skills and /agents) is migrated by tools/vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# The vault owns every file it installs: an install/update overwrites each one with the incoming version and removes files that left the kit (no keep, no conflicts). The only content that is yours is your project's Games/, Models/, My-Skills/ and My-Agents/ folders and anything outside the vault's own paths; nothing here touches them. claude-kit/state/ holds a few tiny settings (rbx-mockup on/off) that are never deleted.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: bash install.sh [--home DIR] [--dry-run] [--with-hooks | --remove-hooks] [--no-mods] [--no-assets]     (--home / env CLAUDE_KIT_HOME: install under DIR instead of $HOME, for tests)
#   ONE RUN DOES EVERYTHING: after the kit files, the two mods and the vault load, this script runs tools/vault-sync-all.py for the resolved vault folder: extra notes repositories (vault-shards.py), the Roblox reference screenshots (refs-sync.py, ~30 MB) and the asset zips (assets-sync.py, ~1 GB), with short progress lines (`assets: 3/6 zips ...`). It FAILS SOFT: a failed download prints ONE `Assets incomplete: <reason>. To finish, run (resumes): <command>` line and the script still exits 0; running it again resumes. --no-assets (env CLAUDE_ASSETS_SKIP=1) skips the asset zips only. Callers that sync themselves (kit-refresh, the sync-setup scripts: env CLAUDE_KIT_NOFOOTER=1 or CLAUDE_KIT_NOLOAD=1) skip this part. Test knobs: env CLAUDE_SYNC_BASE (a mirror URL), CLAUDE_SYNC_DRY=1 (report only).
#   MODS (default ON, no flag): tools/kit-mods.py installs the /rbx-subagent-hud (agent sidebar) and /rbx-graph (vault graph link) Claude Code plugins from the vault's claude-kit/mods at PROJECT scope of the VAULT FOLDER (claude plugin ... --scope project, enabledPlugins in <vault>/.claude/settings.json, hidden from git): the hooks apply only to sessions started in the vault folder, never to other sessions. An older USER-scope install is migrated (uninstalled from user scope, installed at project scope, one notice line). --no-mods: do not install them and uninstall them (both scopes) if present (a later update will not bring them back); --with-mods: accepted (old docs), also re-installs them after --no-mods or after you removed them with /plugin. Any problem (no claude CLI, offline, plugins disabled by policy, plugin errors) prints ONE "Mods skipped: <reason>. Run again later: <command>" line and the install still succeeds.
#   --with-hooks / --remove-hooks (opt-in, never automatic): merge into / remove from ~/.claude/settings.json the two /rbx-low-usage hooks and the rbx-mentor suggestion hook (backup first, idempotent, keeps all other settings).
set -u
KIT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
H="${CLAUDE_KIT_HOME:-$HOME}"; DRY=0; HOOKS=""; MODS_ON=1; FORCE=0; ASSETS_ON=1; [ "${CLAUDE_ASSETS_SKIP:-0}" = 1 ] && ASSETS_ON=0; HOME_GIVEN=0; [ -n "${CLAUDE_KIT_HOME:-}" ] && HOME_GIVEN=1
while [ $# -gt 0 ]; do
  case "$1" in --home) [ $# -ge 2 ] || { echo "install.sh: --home needs a folder" >&2; exit 2; }; H="$2"; HOME_GIVEN=1; shift 2;; --dry-run) DRY=1; shift;; --with-hooks) HOOKS=install-hooks; shift;; --remove-hooks) HOOKS=uninstall-hooks; shift;; --with-mods) MODS_ON=1; FORCE=1; shift;; --no-mods) MODS_ON=0; shift;; --no-assets) ASSETS_ON=0; shift;; *) shift;; esac
done
C="$H/.claude"; [ $HOME_GIVEN = 0 ] && [ -n "${CLAUDE_CONFIG_DIR:-}" ] && C="$CLAUDE_CONFIG_DIR"
MAN="$C/claude-kit/installed.tsv"; TMP="$(mktemp "${TMPDIR:-/tmp}/claude-kit.XXXXXX" 2>/dev/null)" || TMP="${TMPDIR:-/tmp}/claude-kit.$$"
trap 'rm -f "$TMP"' EXIT
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
sha() { local o; o="$($SHA "$1")"; o="${o#\\}"; printf '%s' "${o%% *}"; }   # GNU sha256sum starts the line with a backslash when the file name contains one (Windows-style --home)
MANTXT=""; [ -s "$MAN" ] && MANTXT=1      # old manifest present: look entries up with awk
n_new=0; n_upd=0; n_same=0; n_gone=0; n_fail=0; first_wf=0
SM="claude-kit/vault-mode"; AO="rbx-update rbx-check rbx-uninstall"
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
      case "$orel" in claude-kit/*) ;; skills/*) nm="${orel#skills/}"; nm="${nm%%/*}"; case " $AO rbx-load rbx-unload " in *" $nm "*) ;; *) continue;; esac;; *) continue;; esac
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
# the vault folder is THE loaded environment: resolve it (the clone that holds this claude-kit folder, $CLAUDES_VAULT, the registered one, ~/Obsidian/claudes-vault) and load it quietly (env CLAUDE_KIT_NOLOAD=1: the caller, kit-refresh, does it)
VH=""; LOADOUT=""
for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then LPY="$p"; break; fi; done
if [ -n "${LPY:-}" ] && [ -f "$KIT/tools/vault-mode.py" ]; then
  VH="$(CLAUDE_KIT_HOME="$H" CLAUDE_CONFIG_DIR="$C" "$LPY" -I "$KIT/tools/vault-mode.py" home --kit "$KIT" --config "$C" 2>/dev/null | tail -n 1)"
  if [ -n "$VH" ] && [ $DRY = 0 ] && [ "${CLAUDE_KIT_NOLOAD:-0}" != 1 ] && [ -f "$C/claude-kit/tools/vault-mode.py" ]; then
    LOADOUT="$(CLAUDE_KIT_HOME="$H" CLAUDE_CONFIG_DIR="$C" "$LPY" -I "$C/claude-kit/tools/vault-mode.py" load --project "$VH" --quiet $([ "$first_wf" = 0 ] && echo --announce) --config "$C" 2>&1)"
  fi
fi
echo "claude-kit: installed $n_new new, updated $n_upd, unchanged $n_same$([ "$n_gone" -gt 0 ] && echo ", removed $n_gone no longer in the kit")$([ "$n_fail" -gt 0 ] && echo ", FAILED $n_fail") (into $C)"
[ -n "$RENAME_MSG" ] && printf '%s\n' "$RENAME_MSG"
[ -n "$LOADOUT" ] && printf '%s\n' "$LOADOUT"
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
# kit mods (Claude Code plugins: /rbx-subagent-hud agent sidebar, /rbx-graph vault graph link): tools/kit-mods.py, PROJECT scope of the vault folder (see the header). ON BY DEFAULT (opt out: --no-mods).
# Never fails the install: any problem prints ONE "Mods skipped: <reason>. Run again later: <command>" line. State file claude-kit/state/mods-choice: "on" after a successful install, "off" after --no-mods. Mods installed once and later removed with /plugin are NOT brought back by updates (--with-mods forces).
# Legacy plugin names (workflow-hud, vault-graph, hud-rbxdev-vault, graph-rbxdev-vault) are uninstalled on every run that can list plugins; user-scope copies of the two mods are migrated to the vault folder.
SD="$C/claude-kit/state"
INST="$KIT/install.sh"; [ -n "$VH" ] && [ -f "$VH/claude-kit/install.sh" ] && INST="$VH/claude-kit/install.sh"   # a path that survives (the installer may run from a temporary clone of the kit repository)
MCMD="bash \"$INST\" --with-mods"; MOFF="bash \"$INST\" --no-mods"
KPY=""; for p in python3 python py; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then KPY="$p"; break; fi; done
MB=""; rm -f "$SD/mods-block.txt" 2>/dev/null
if [ -n "$KPY" ] && [ -f "$KIT/tools/kit-mods.py" ]; then
  "$KPY" -I "$KIT/tools/kit-mods.py" --kit "$KIT" --config "$C" --vault "$VH" --on-cmd "$MCMD" --off-cmd "$MOFF" $([ $DRY = 1 ] && echo --dry-run) $([ $MODS_ON = 0 ] && echo --no-mods) $([ $FORCE = 1 ] && echo --with-mods) 2>&1
  MB="$(cat "$SD/mods-block.txt" 2>/dev/null)"
else
  echo "Mods skipped: no working Python 3 on this computer. Run again later: $MCMD"
fi
[ -n "$MB" ] || MB="**THE TWO MODS (NOT INSTALLED)**
- Skipped: the mods step did not run. Install them: $MCMD   then start a new session in the vault folder."
# the single run also downloads the rest: extra notes repositories, reference screenshots, assets (tools/vault-sync-all.py; fails soft, prints ONE retry line, exits 0)
SYNCRAN=0; ASSETB=""
if [ $DRY = 0 ] && [ -n "$VH" ] && [ -d "$VH" ] && [ "${CLAUDE_KIT_NOFOOTER:-0}" != 1 ] && [ "${CLAUDE_KIT_NOLOAD:-0}" != 1 ] && [ "${CLAUDE_KIT_NOSYNC:-0}" != 1 ]; then
  if [ -n "$KPY" ] && [ -f "$KIT/tools/vault-sync-all.py" ]; then
    SYNCRAN=1
    "$KPY" -I "$KIT/tools/vault-sync-all.py" --vault "$VH" --config "$C" --retry-cmd "bash \"$INST\"" $([ $ASSETS_ON = 0 ] && echo --no-assets) $([ -n "${CLAUDE_SYNC_BASE:-}" ] && echo --base "$CLAUDE_SYNC_BASE") $([ "${CLAUDE_SYNC_DRY:-0}" = 1 ] && echo --dry-run) 2>&1
    ASSETB="$(sed -n 2p "$SD/assets-status.txt" 2>/dev/null)"; [ "$(sed -n 1p "$SD/assets-status.txt" 2>/dev/null)" = complete ] && ASSETB=""
  else
    echo "Assets incomplete: no working Python 3 on this computer. To finish, install Python 3 and run (resumes): bash \"$INST\""
    ASSETB="- Assets: INCOMPLETE (no working Python 3). Install Python 3, then run this (it resumes): bash \"$INST\""
  fi
fi
if [ -n "$VH" ]; then VSAY="$VH"; else VSAY="your vault folder (not found on this computer: clone the vault first, see SETUP-FOR-CLAUDE.md, then run this installer again)"; fi
[ "$first_wf" = 1 ] && [ $DRY = 0 ] && echo "The Roblox Dev Mastery Vault kit is installed. Start a new Claude session in $VSAY to use it. Always available: /rbx-update /rbx-check /rbx-uninstall. Two mods (agent sidebar, graph view) are enabled for the vault folder only; turn them off with /plugin or --no-mods. More details: MANUAL-READ.md in the vault folder (or https://vault-hhmi60uo.netlify.app/manual). Built and maintained by Roman (GitHub: romangigliotti123-arch)"
CB="$(printf '%s
' "**HOW TO START USING**" "- Start a new Claude session in $VSAY; that folder has everything loaded." ${ASSETB:+"$ASSETB"} "" "**HOW TO SEE SKILLS AND AGENTS**" "- Type /rbx-list in that session, or / then rbx-. Make your own skill: ask Claude to use /rbx-new-skill." "" "$MB" "" "**HOW TO MAKE A GAME IDEA**" "- /rbx-ideas finds one fresh idea (reply another, build it or plan); /rbx-idea-creator starts from yours." "" "**HOW TO BUILD A GAME**" "- /rbx-workflow builds a game stage by stage; resume with \"I want to work on <game name>\"." "" "**HOW TO UPDATE**" "- Type /rbx-update (works from any session)." "" "**NOT SURE WHICH SKILL?**" "- Just describe what you want; Claude offers the right skill and you reply yes." "" "More details: MANUAL-READ.md in the vault folder (or https://vault-hhmi60uo.netlify.app/manual).")"
CLOSE_BEGIN="=== COPY THIS TO THE USER EXACTLY, AS THE END OF YOUR FINAL MESSAGE (nothing after it; also saved as START-HERE.md in the vault folder) ==="; CLOSE_END="=== END OF THE BLOCK TO COPY ==="
if [ $DRY = 0 ] && [ -n "$VH" ] && [ -d "$VH" ]; then
  printf '%s\n' "$CB" > "$VH/START-HERE.md" 2>/dev/null
  if git -C "$VH" rev-parse --git-dir >/dev/null 2>&1; then ex="$(git -C "$VH" rev-parse --git-path info/exclude)"; case "$ex" in /*|?:*) ;; *) ex="$VH/$ex";; esac; grep -qxF "/START-HERE.md" "$ex" 2>/dev/null || printf '/START-HERE.md\n' >> "$ex" 2>/dev/null; fi
fi
if [ "${CLAUDE_KIT_NOFOOTER:-0}" != 1 ]; then echo; echo "$CLOSE_BEGIN"; printf '%s\n' "$CB"; echo "$CLOSE_END"; fi
[ "$n_fail" -gt 0 ] && exit 1
exit 0
