#!/bin/bash
# kit-refresh.sh - run right after the vault update (self-healing fetch + fast-forward) (by vault-update.sh, the login agent/timer, or by hand) so installed copies of the kit
# (agents, skills such as /rbx-workflow, tools) refresh whenever the vault updates, and then syncs <vault>/Assets from the public vault-assets repositories.
# 1) install.sh (idempotent; every vault file is overwritten with the incoming version, files that left the kit are removed). Env CLAUDE_KIT_SKIP=1 skips this part.
# 2) tools/assets-sync.py --vault <this vault>: downloads only new/changed asset files (1.02 GB of zips the first time), deletes removed ones.
#    Quiet unless something changed; skips with one line when no asset source is reachable (offline). Env CLAUDE_ASSETS_SKIP=1 skips this part.
# 3) tools/refs-sync.py: fetches/updates the public Roblox reference screenshots (repos vault-refs-NN from repos.json, ~30 MB) into <vault>/.rbx/claude-kit/roblox-reference and
#    writes <vault>/.rbx/claude-kit/reference-path.txt (read by the visual-QA / art-direction skills). Silent when offline or up to date. Env CLAUDE_REFS_SKIP=1 skips this part.
# 1b) vault folder load (see below): the vault folder is permanently loaded; every update rewrites its .claude (skills, agents, rules) and cleans folders an older kit loaded. Env CLAUDE_MODE_SKIP=1 skips it.
# Prints a line only when something changed, so the log stays quiet. Never fails the caller.
# Last line (only when the kit changed and the caller is not the current vault-update.sh, which prints it itself): "Your vault is up to date as of ... (local time)" (tools/vault-published.py).
{
D="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
if [ "${CLAUDE_KIT_SKIP:-0}" != 1 ] && [ -f "$D/install.sh" ]; then
  out="$(CLAUDE_KIT_NOLOAD=1 CLAUDE_KIT_NOFOOTER=1 bash "$D/install.sh" 2>&1)" || out="kit refresh failed: $out"
  chk="$(printf '%s\n' "$out" | grep -v -E '^(similar skills of yours|Mods up to date|Mods skipped)')"   # the informational list of similar user skills alone is not a change
  if [ "$(printf '%s\n' "$chk" | wc -l)" = 1 ] && printf '%s\n' "$chk" | grep -Eq '^claude-kit: installed 0 new, updated 0, unchanged [0-9]+ \(into .*\)$'; then :
  else KCHANGED=1; printf '%s kit-refresh: %s\n' "$(date '+%F %T')" "$(printf '%s' "$out" | tr '\n' ' ')"; fi
fi
# 1b) tools/vault-mode.py load --project <this vault> --quiet --announce: the vault folder is THE loaded environment (its .claude gets the skills, agents and rules; Games/ and Models/ stay out of git); folders an older kit loaded are cleaned
#     (prints one line then); silent when nothing changed. Env CLAUDE_MODE_SKIP=1 skips this part.
if [ "${CLAUDE_MODE_SKIP:-0}" != 1 ] && [ -f "$D/tools/vault-mode.py" ]; then
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then
      CFG="${CLAUDE_CONFIG_DIR:-${CLAUDE_KIT_HOME:-$HOME}/.claude}"; [ -n "${CLAUDE_CONFIG_DIR:-}" ] || [ -n "${CLAUDE_KIT_HOME:-}" ] || CFG="$HOME/.claude"
      KHD="$CFG"; [ -d "$(dirname "$D")/.rbx/claude-kit" ] && KHD="$(dirname "$D")/.rbx"      # ONE FOLDER: the installed kit is <vault>/.rbx/claude-kit
      [ -f "$KHD/claude-kit/tools/vault-mode.py" ] && RBX_KIT_HOME="$KHD" CLAUDE_CONFIG_DIR="$CFG" "$p" -I "$KHD/claude-kit/tools/vault-mode.py" load --project "$(dirname "$D")" --quiet --announce --config "$CFG" 2>&1; break
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
if [ "${KCHANGED:-0}" = 1 ] && [ -z "${VAULT_UPDATE_LINE:-}" ]; then
  PL=""
  for p in python3 python; do
    if command -v "$p" >/dev/null 2>&1 && "$p" -c "import sys" >/dev/null 2>&1; then [ -f "$D/tools/vault-published.py" ] && PL="$("$p" -I "$D/tools/vault-published.py" --vault "$(dirname "$D")" --where 2>/dev/null | tail -n 2)"; break; fi
  done
  echo "${PL:-Your vault is up to date.}"
fi
exit 0
}
