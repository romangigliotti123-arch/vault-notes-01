#!/bin/bash
# mac-sync-setup.sh - keeps the Obsidian vault "claudes-vault" fresh on this Mac: clone, kit install, asset sync, and a launchd agent that updates at every login
# (RunAtLoad only, NO 15-minute polling). On demand: bash vault-update.sh in the vault folder, or /rbx-update in Claude.
# Assets (1.02 GB of zips the first time) are synced into <vault>/Assets from the host PC's Tailscale share, never from GitHub.
# User-level only: no sudo, no system settings. Safe to run again.
set -u
REPO="romangigliotti123-arch/claudes-vault"
# ONE FOLDER: the vault folder is where everything lives (default ~/Obsidian/rbx-dev-vault; an existing claudes-vault folder keeps its name; a moved folder is found through the pointer file)
DEST="$HOME/Obsidian/rbx-dev-vault"; [ -d "$HOME/Obsidian/claudes-vault/.git" ] && [ ! -e "$DEST" ] && DEST="$HOME/Obsidian/claudes-vault"
PTRF="${CLAUDE_CONFIG_DIR:-${CLAUDE_KIT_HOME:-$HOME}/.claude}/rbx-dev-vault.path"; PV="$(head -n 1 "$PTRF" 2>/dev/null)"; [ -n "$PV" ] && [ -d "$PV/.git" ] && DEST="$PV"
LABEL="com.roman.vaultpull"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG="$HOME/Library/Logs/vaultpull.log"

for p in /opt/homebrew/bin /usr/local/bin; do [ -d "$p" ] && PATH="$p:$PATH"; done
export PATH

GIT="$(command -v git || true)"
GH="$(command -v gh || true)"
if [ -n "${VAULT_STATE_DIR:-}" ]; then STATE="$VAULT_STATE_DIR"
elif [ "$(uname -s)" = Darwin ]; then STATE="$HOME/Library/Application Support/claudes-vault-sync"
else STATE="${XDG_STATE_HOME:-$HOME/.local/state}/claudes-vault-sync"; fi
# --- vault-heal (same block in vault-update.sh, mac-sync-setup.sh, linux-sync-setup.sh) ---
# Self-healing update of the READ-ONLY vault clone. Never fails, never runs git clean. Prints at most one line.
# core.autocrlf/safecrlf off, fetch, fast-forward; if local changes or divergence block that, the real changes are saved to
# <state>/local-changes-<timestamp>.patch (+ untracked list; newest 5 kept) and the vault is reset to origin/main.
# Full view (marker <vault>/.full-view): after every update .obsidian/app.json gets userIgnoreFilters = ["Assets/", "Games/", "Models/"] only; never saved as a local change.
vault_json() { # $1 = mode (strip|set) ; reads JSON text on stdin, writes JSON text on stdout
  local PY="" c; for c in python3 python; do if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import json' >/dev/null 2>&1; then PY="$(command -v "$c")"; break; fi; done
  if [ -n "$PY" ]; then
    "$PY" -c '
import sys, json
mode = sys.argv[1]
t = sys.stdin.read().strip() or "{}"
o = json.loads(t)
if mode == "strip":
    o.pop("userIgnoreFilters", None); print(json.dumps(o, sort_keys=True))
else:
    o["userIgnoreFilters"] = ["Assets/", "Games/", "Models/"]; print(json.dumps(o, indent=2, ensure_ascii=False))
' "$1"
  elif command -v node >/dev/null 2>&1; then
    node -e '
const m = process.argv[1]; let t = require("fs").readFileSync(0, "utf8").trim() || "{}"; const o = JSON.parse(t);
if (m === "strip") { delete o.userIgnoreFilters; const k = {}; Object.keys(o).sort().forEach(x => k[x] = o[x]); console.log(JSON.stringify(k)); }
else { o.userIgnoreFilters = ["Assets/", "Games/", "Models/"]; console.log(JSON.stringify(o, null, 2)); }
' "$1"
  else return 1; fi
}
vault_fullview_apply() { # $1 = vault
  [ -f "$1/.full-view" ] || return 0
  local F="$1/.obsidian/app.json" TMP
  mkdir -p "$1/.obsidian"; [ -f "$F" ] || echo '{}' > "$F"
  TMP="$(vault_json set < "$F" 2>/dev/null)" && [ -n "$TMP" ] && printf '%s\n' "$TMP" > "$F"
  return 0
}
# PROTECTED USER DATA: <vault>/My Research/ and every folder that holds PROTECTED-RESEARCH.md are added to .git/info/exclude on every run (git never treats them as
# removable), are never in a patch and never touched by reset. Untracked files are never removed by a normal update;
vault_protected() { # $1=git $2=vault ; prints protected dirs (relative, no trailing slash), 'My Research' first
  local G="$1" V="$2" REG="$2/.git/info/protected-folders.txt" d
  { echo 'My Research'; echo 'Games'; echo 'Models'; echo 'My-Skills'; echo 'My-Agents'
    [ -f "$REG" ] && cat "$REG"
    "$G" -C "$V" -c core.quotepath=false ls-files -o --exclude-standard -- '*PROTECTED-RESEARCH.md' 2>/dev/null | sed -n 's#^\(.*\)/PROTECTED-RESEARCH\.md$#\1#p'
  } | awk 'NF && !seen[$0]++' | while IFS= read -r d; do
    case "$d" in "My Research/"*|"Games/"*|"Models/"*|"My-Skills/"*|"My-Agents/"*) continue;; esac
    if [ "$d" = "My Research" ] || [ "$d" = "Games" ] || [ "$d" = "Models" ] || [ "$d" = "My-Skills" ] || [ "$d" = "My-Agents" ] || [ -f "$V/$d/PROTECTED-RESEARCH.md" ]; then echo "$d"; fi
  done
}
vault_protect() { # $1=git $2=vault ; sets PROT (newline list) and adds /<dir>/ lines to .git/info/exclude (idempotent)
  local V="$2" EX="$2/.git/info/exclude" REG="$2/.git/info/protected-folders.txt" d
  PROT="$(vault_protected "$1" "$2")"
  mkdir -p "$V/.git/info"
  printf '%s\n' "$PROT" | tail -n +6 > "$REG"; [ -s "$REG" ] || rm -f "$REG"
  while IFS= read -r d; do
    [ -n "$d" ] || continue
    grep -qxF "/$d/" "$EX" 2>/dev/null || echo "/$d/" >> "$EX"
  done <<EOF_PROT
$PROT
EOF_PROT
  return 0
}
vault_own_count() { # $1=git $2=vault ; number of your own files (untracked + inside protected folders)
  local G="$1" V="$2" n d c
  n="$("$G" -C "$V" ls-files -o --exclude-standard 2>/dev/null | wc -l | tr -d ' ')"
  while IFS= read -r d; do
    [ -n "$d" ] && [ -d "$V/$d" ] || continue
    c="$(find "$V/$d" -type f 2>/dev/null | wc -l | tr -d ' ')"; n=$((n + c))
  done <<EOF_PROT
$PROT
EOF_PROT
  echo "$n"
}
PUBLIC_NOTES_GIT="https://github.com/romangigliotti123-arch/vault-notes-01.git"   # set in the public copy by the site build: the GitHub repo that replaces the old website vault.git remote
vault_migrate_origin() { # $1=git $2=vault ; an origin on the old *.netlify.app/vault.git (the website only redirects now) is moved to the GitHub repo once
  [ -n "$PUBLIC_NOTES_GIT" ] || return 0
  case "$("$1" -C "$2" remote get-url origin 2>/dev/null)" in
    *.netlify.app/vault.git*) "$1" -C "$2" remote set-url origin "$PUBLIC_NOTES_GIT" 2>/dev/null && echo "rbx-update: origin moved to $PUBLIC_NOTES_GIT";;
  esac
  return 0
}
vault_heal() { # $1=git $2=vault $3=state dir ; echoes one line when something notable happened
  local G="$1" V="$2" S="$3" T BASE TS P SAVED=0 CUR HEAD MSG=""
  "$G" -C "$V" config core.autocrlf false 2>/dev/null; "$G" -C "$V" config core.safecrlf false 2>/dev/null
  vault_migrate_origin "$G" "$V"
  vault_protect "$G" "$V"
  if ! "$G" -C "$V" fetch -q origin >/dev/null 2>&1; then MSG="rbx-update: fetch failed (offline?), vault left as it is"
  else
    T=origin/main
    "$G" -C "$V" rev-parse -q --verify "$T" >/dev/null 2>&1 || { T='@{u}'; "$G" -C "$V" rev-parse -q --verify "$T" >/dev/null 2>&1 || T=""; }
    if [ -z "$T" ]; then MSG="rbx-update: no upstream branch, vault left as it is"
    else
      if [ -f "$V/.full-view" ] && [ -f "$V/.obsidian/app.json" ]; then
        CUR="$(vault_json strip < "$V/.obsidian/app.json" 2>/dev/null)"; HEAD="$("$G" -C "$V" show HEAD:.obsidian/app.json 2>/dev/null | vault_json strip 2>/dev/null)"
        [ -n "$CUR" ] && [ "$CUR" = "$HEAD" ] && "$G" -C "$V" checkout -q -- .obsidian/app.json 2>/dev/null
      fi
      "$G" -C "$V" update-index -q --refresh >/dev/null 2>&1
      if "$G" -C "$V" diff HEAD --quiet >/dev/null 2>&1 && "$G" -C "$V" merge --ff-only -q "$T" >/dev/null 2>&1; then :
      else
        BASE="$("$G" -C "$V" merge-base HEAD "$T" 2>/dev/null)"; [ -n "$BASE" ] || BASE=HEAD
        mkdir -p "$S"; TS="$(date +%Y%m%d-%H%M%S)"; P="$S/local-changes-$TS.patch"
        if [ -n "$("$G" -C "$V" diff "$BASE" --ignore-cr-at-eol 2>/dev/null | head -c 1)" ]; then
          "$G" -C "$V" diff "$BASE" --binary > "$P" 2>/dev/null && SAVED=1
        fi
        "$G" -C "$V" -c core.quotepath=false ls-files --others --exclude-standard > "$S/local-changes-$TS.untracked.txt" 2>/dev/null
        [ -s "$S/local-changes-$TS.untracked.txt" ] || rm -f "$S/local-changes-$TS.untracked.txt"
        # untracked files that upstream now tracks would be overwritten by the reset: copy them aside first
        if [ -s "$S/local-changes-$TS.untracked.txt" ]; then
          LC_ALL=C sort "$S/local-changes-$TS.untracked.txt" > "$S/.u.$$"; "$G" -C "$V" -c core.quotepath=false ls-tree -r --name-only "$T" 2>/dev/null | LC_ALL=C sort > "$S/.t.$$"
          LC_ALL=C comm -12 "$S/.u.$$" "$S/.t.$$" | while IFS= read -r f; do mkdir -p "$(dirname "$S/collision-backup-$TS/$f")"; cp -p "$V/$f" "$S/collision-backup-$TS/$f" 2>/dev/null; done
          rm -f "$S/.u.$$" "$S/.t.$$"
        fi
        ls -1d "$S"/collision-backup-* 2>/dev/null | sort -r | tail -n +6 | while IFS= read -r f; do rm -rf "$f"; done
        ls -1 "$S"/local-changes-*.patch 2>/dev/null | sort -r | tail -n +6 | while IFS= read -r f; do rm -f "$f"; done
        ls -1 "$S"/local-changes-*.untracked.txt 2>/dev/null | sort -r | tail -n +6 | while IFS= read -r f; do rm -f "$f"; done
        if ! "$G" -C "$V" reset --hard -q "$T" >/dev/null 2>&1; then MSG="rbx-update: could not reset the vault to the latest (left as it is)"
        elif [ "$SAVED" = 1 ]; then MSG="rbx-update: local changes saved to $P; vault reset to the latest"; fi
      fi
    fi
  fi
  vault_fullview_apply "$V"
  [ -n "$MSG" ] && echo "$MSG"
  return 0
}
# --- end vault-heal ---

if [ -z "$GIT" ]; then
  echo "Missing: git. Install with Homebrew:  brew install git   (or: xcode-select --install)"
  exit 1
fi

mkdir -p "$HOME/Obsidian" "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
if [ ! -d "$DEST/.git" ]; then
  CLONED=0
  # 1) Tailscale share (no GitHub login needed)
  for B in https://vault-hhmi60uo.netlify.app; do
    curl -fsS -m 8 -o /dev/null "$B/vault.git/HEAD" 2>/dev/null || continue
    echo "Cloning from $B/vault.git (first time can take several minutes)..."
    for TRY in 1 2; do
      if [ -d "$DEST/My Research" ] || [ -d "$DEST/Games" ] || { [ "$TRY" = 1 ] && [ -n "$(ls -A "$DEST" 2>/dev/null)" ]; }; then echo "Refusing to clear $DEST: it is not a clone and it is not empty (your own files could be in it). Move it away and run again."; exit 1; fi
      rm -rf "$DEST"
      if "$GIT" -c core.autocrlf=false -c core.safecrlf=false clone "$B/vault.git" "$DEST"; then CLONED=1; break; fi
    done
    [ "$CLONED" -eq 1 ] && break
  done
  # 2) GitHub via gh
  if [ "$CLONED" -ne 1 ]; then
    if [ -z "$GH" ]; then echo "Share unreachable (sign in to Tailscale) and gh is missing. Install: brew install gh, or sign in to Tailscale."; exit 1; fi
    if ! "$GH" auth status >/dev/null 2>&1; then
      echo "NEEDS_LOGIN: share unreachable and not logged in to GitHub. Sign in to Tailscale (preferred) or run: gh auth login (GitHub.com, HTTPS, web browser), then run this script again."
      exit 2
    fi
    "$GH" auth setup-git >/dev/null 2>&1 || true
    echo "Cloning $REPO from GitHub (first time can take several minutes)..."
    "$GH" repo clone "$REPO" "$DEST" -- -c core.autocrlf=false -c core.safecrlf=false || { echo "Clone failed."; exit 1; }
  fi
else
  echo "Vault already cloned at $DEST"
fi

# Self-heal the (read-only) clone: autocrlf/safecrlf off, fetch, fast-forward; local changes are saved to $STATE/local-changes-<timestamp>.patch, then reset to origin/main
vault_heal "$GIT" "$DEST" "$STATE"

# Companion AI Library Vault (private repo ai-library-vault) -> next to this vault ($(dirname "$DEST")/ai-library-vault). Share first, then GitHub; non-fatal. Skip: AI_VAULT_SKIP=1
if [ "${AI_VAULT_SKIP:-0}" != 1 ] && [ -f "$DEST/ai-vault-sync.sh" ]; then bash "$DEST/ai-vault-sync.sh" --dest "$(dirname "$DEST")/ai-library-vault" || echo "AI Library Vault setup failed (non-fatal; run vault-update.sh later)."; fi

# Claude kit (Roblox agents, skills, tools) -> ~/.claude. Idempotent, no questions, the vault owns its files: every update overwrites them with the new version. Skip: CLAUDE_KIT_SKIP=1
if [ "${CLAUDE_KIT_SKIP:-0}" != 1 ] && [ -f "$DEST/claude-kit/install.sh" ]; then CLAUDE_KIT_NOFOOTER=1 bash "$DEST/claude-kit/install.sh" || echo "Kit install failed (non-fatal)."; fi

# Assets -> <vault>/Assets from the share (first run downloads everything, 1.02 GB of zips; later runs only changes). No questions. Skip: CLAUDE_ASSETS_SKIP=1
if [ "${CLAUDE_ASSETS_SKIP:-0}" != 1 ] && [ -f "$DEST/claude-kit/kit-refresh.sh" ]; then CLAUDE_KIT_SKIP=1 bash "$DEST/claude-kit/kit-refresh.sh" || echo "Asset sync failed (non-fatal; run vault-update.sh later)."; fi

mkdir -p "$STATE"      # the logon job runs this helper: it reads the pointer file at run time, so a moved vault folder still updates
cat > "$STATE/run-update.sh" <<RUNEOF
#!/bin/bash
D='$DEST'
P="\$(head -n 1 '$PTRF' 2>/dev/null)"; [ -f "\$P/vault-update.sh" ] && D="\$P"
if [ -f "\$D/vault-update.sh" ]; then /bin/bash "\$D/vault-update.sh" --quiet; else '$GIT' -C "\$D" pull --ff-only; if [ -f "\$D/claude-kit/kit-refresh.sh" ]; then /bin/bash "\$D/claude-kit/kit-refresh.sh"; fi; fi
RUNEOF
cat > "$PLIST" <<PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>-c</string>
    <string>/bin/bash "$STATE/run-update.sh"</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>$(dirname "$GIT"):/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string></dict>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$LOG</string>
  <key>StandardErrorPath</key><string>$LOG</string>
</dict>
</plist>
PLISTEOF

UIDN="$(id -u)"
launchctl bootout "gui/$UIDN/$LABEL" >/dev/null 2>&1 || launchctl unload "$PLIST" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$UIDN" "$PLIST" 2>/dev/null || launchctl load "$PLIST"

echo
# Software check (read-only table: what is installed, what is missing, install commands per OS; installs nothing). Non-fatal.
if [ "${CLAUDE_KIT_SKIP:-0}" != 1 ] && [ -f "$DEST/claude-kit/tools/setup-check.py" ]; then for p in python3 python; do if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then echo; "$p" -I "$DEST/claude-kit/tools/setup-check.py" || true; break; fi; done; fi
echo "Done. The vault (pull, kit, assets) updates at every login, not on a timer (log: $LOG)."
echo "Update now, any time: bash \"$DEST/vault-update.sh\"   (or /rbx-update in Claude). Assets are in $DEST/Assets."
echo "Next: open Obsidian > File > Open folder as vault > choose $DEST"
echo "Updates appear automatically as files change on disk."
echo "Do not edit notes on the Mac (pull is fast-forward only)."
if [ -f "$DEST/.rbx/claude-kit/vault-mode/.claude/skills/rbx-workflow/SKILL.md" ]; then echo "The Roblox Dev Mastery Vault kit is installed. Start a new Claude session in $DEST to use it. Always available: /rbx-update /rbx-check /rbx-uninstall. Two mods (agent sidebar, graph view) are enabled for the vault folder only; turn them off with /plugin or --no-mods. More details: MANUAL-READ.md in the vault folder (or https://vault-hhmi60uo.netlify.app/manual). Built and maintained by Roman (GitHub: romangigliotti123-arch)"; fi

MODSB="$(cat "$DEST/.rbx/claude-kit/state/mods-block.txt" 2>/dev/null)"; [ -n "$MODSB" ] || MODSB="**THE TWO MODS (NOT INSTALLED)**
- Skipped: the installer did not report them. The vault works without them. To install them run: bash \"$DEST/claude-kit/install.sh\" --with-mods   then type /reload-plugins.
- They are Claude Code plugins that add an agent sidebar (/rbx-subagent-hud) and a graph view (/rbx-graph) and register hooks; they are installed for the vault folder only (project scope), so they apply only to sessions started in that folder. Turn them off any time with /plugin or the installer's --no-mods."
if [ "${CLAUDE_KIT_SKIP:-0}" != 1 ] && [ -f "$DEST/START-HERE.md" ]; then echo; echo "=== COPY THIS TO THE USER EXACTLY, AS THE END OF YOUR FINAL MESSAGE (nothing after it; also saved as START-HERE.md in the vault folder) ==="; cat "$DEST/START-HERE.md"; echo "=== END OF THE BLOCK TO COPY ==="; fi