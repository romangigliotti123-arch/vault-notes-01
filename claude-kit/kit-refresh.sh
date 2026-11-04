#!/bin/bash
# kit-refresh.sh - run right after the vault update (self-healing fetch + fast-forward) (by vault-update.sh, the login agent/timer, or by hand) so installed copies of the kit
# (agents, skills such as /rbx-workflow, tools) refresh whenever the vault updates, and then syncs <vault>/Assets from the public vault-assets repositories.
# 1) install.sh (idempotent; kit wins: a file you changed is backed up to claude-kit/backup/<date>/ and replaced). Env CLAUDE_KIT_SKIP=1 skips this part.
# 2) tools/assets-sync.py --vault <this vault>: downloads only new/changed asset files (about 2.7 GB the first time), deletes removed ones.
#    Quiet unless something changed; skips with one line when no asset source is reachable (offline). Env CLAUDE_ASSETS_SKIP=1 skips this part.
# 3) tools/refs-sync.py: fetches/updates the public Roblox reference screenshots (repos vault-refs-NN from repos.json, ~30 MB) into <claude config dir>/claude-kit/roblox-reference and
#    writes <claude config dir>/claude-kit/reference-path.txt (read by the visual-QA / art-direction skills). Silent when offline or up to date. Env CLAUDE_REFS_SKIP=1 skips this part.
# 4) tools/learn.py flush --quiet: sends the notes queued by /rbx-learn to the public inbox repo vault-learnings. Silent when nothing is queued, offline, or this machine has no write
#    access (the notes then stay queued). Env CLAUDE_LEARN_SKIP=1 skips this part.
# 1b) mode sync (see below): refreshes the project folders where /rbx-load copied the skills/agents. Env CLAUDE_MODE_SKIP=1 skips it.
# Prints a line only when something changed, so the log stays quiet. Never fails the caller.
# Last line (only when the kit changed and the caller is not the current vault-update.sh, which prints it itself): "Your vault is up to date as of ... (local time)" (tools/vault-published.py).
{
D="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
if [ "${CLAUDE_KIT_SKIP:-0}" != 1 ] && [ -f "$D/install.sh" ]; then
  out="$(CLAUDE_KIT_NOFOOTER=1 bash "$D/install.sh" 2>&1)" || out="kit refresh failed: $out"
  case "$out" in
    *"installed 0 new, updated 0, unchanged "*"replaced-yours 0 "*) ;;
    *) KCHANGED=1; printf '%s kit-refresh: %s\n' "$(date '+%F %T')" "$(printf '%s' "$out" | tr '\n' ' ')" ;;
  esac
fi
# 1b) tools/vault-mode.py sync --quiet: folders that have Roblox dev mode loaded (/rbx-load) get the updated skills/agents; silent when nothing changed. Env CLAUDE_MODE_SKIP=1 skips this part.
if [ "${CLAUDE_MODE_SKIP:-0}" != 1 ] && [ -f "$D/tools/vault-mode.py" ]; then
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then
      CFG="${CLAUDE_CONFIG_DIR:-${CLAUDE_KIT_HOME:-$HOME}/.claude}"; [ -n "${CLAUDE_CONFIG_DIR:-}" ] || [ -n "${CLAUDE_KIT_HOME:-}" ] || CFG="$HOME/.claude"
      [ -f "$CFG/claude-kit/tools/vault-mode.py" ] && "$p" -I "$CFG/claude-kit/tools/vault-mode.py" sync --quiet --config "$CFG" 2>&1; break
    fi
  done
fi
DO_ASSETS=0; DO_REFS=0
[ "${CLAUDE_ASSETS_SKIP:-0}" != 1 ] && [ -f "$D/tools/assets-sync.py" ] && DO_ASSETS=1
[ "${CLAUDE_REFS_SKIP:-0}" != 1 ] && [ -f "$D/tools/refs-sync.py" ] && DO_REFS=1
if [ "$DO_ASSETS" = 1 ] || [ "$DO_REFS" = 1 ]; then
  PY=""
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then PY="$p"; break; fi
  done
  if [ -z "$PY" ]; then
    printf '%s assets-sync: skipped (no working python3; install Python 3 and run vault-update.sh)\n' "$(date '+%F %T')"
  else
    [ "$DO_ASSETS" = 1 ] && [ -f "$D/tools/vault-shards.py" ] && "$PY" -I "$D/tools/vault-shards.py" --vault "$(dirname "$D")" 2>&1   # extra repo shards (vault-notes-02, ...) from repos.json; silent when there are none
    [ "$DO_REFS" = 1 ] && "$PY" -I "$D/tools/refs-sync.py" 2>&1   # reference screenshots (vault-refs-NN) + reference-path.txt; silent when offline or unchanged
    [ "$DO_ASSETS" = 1 ] && "$PY" -I "$D/tools/assets-sync.py" --vault "$(dirname "$D")" 2>&1   # streams its own progress lines (first sync); prints nothing when nothing changed
  fi
fi
if [ "${CLAUDE_LEARN_SKIP:-0}" != 1 ] && [ -f "$D/tools/learn.py" ]; then
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then "$p" -I "$D/tools/learn.py" flush --quiet >/dev/null 2>&1; break; fi
  done
fi
if [ "${KCHANGED:-0}" = 1 ] && [ -z "${VAULT_UPDATE_LINE:-}" ]; then
  PL=""
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then [ -f "$D/tools/vault-published.py" ] && PL="$("$p" -I "$D/tools/vault-published.py" --vault "$(dirname "$D")" 2>/dev/null | tail -n 1)"; break; fi
  done
  echo "${PL:-Your vault is up to date.}"
fi
exit 0
}
