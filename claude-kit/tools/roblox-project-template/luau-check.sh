#!/usr/bin/env bash
# luau-check.sh <file-or-dir>...   Static checks for Luau: stylua --check, selene (roblox std), luau-lsp analyze (Roblox definitions).
# stylua/selene run from this folder; luau-lsp runs from the Rojo project root found above the target (this folder if none).
# Runs from this folder (rokit.toml, selene.toml, stylua.toml, roblox.yml, globalTypes.d.luau live here).
# Tools come from Rokit (`rokit install` in this folder). A missing tool is reported as SKIPPED, not as a pass.
# Exit: 0 all present tools passed, 1 a check failed, 2 no tool at all was available (do a manual review instead).
cd "$(dirname "$0")" || exit 1
TPL="$(pwd)"
rc=0; ran=0
for p in "$@"; do
  case "$p" in /*|[A-Za-z]:*) a="$p";; *) a="$OLDPWD/$p";; esac
  if command -v stylua >/dev/null 2>&1; then ran=1; echo "== stylua --check $a"; stylua --check "$a" || rc=1; else echo "== stylua: SKIPPED (not installed)"; fi
  if command -v selene >/dev/null 2>&1; then ran=1; echo "== selene $a"; selene "$a" || rc=1; else echo "== selene: SKIPPED (not installed)"; fi
  if command -v luau-lsp >/dev/null 2>&1; then
    ran=1; echo "== luau-lsp analyze $a"
    # find the Rojo project (default.project.json) above the target so instance-path requires resolve
    sm=""; root="$TPL"; d="$a"; [ -f "$d" ] && d="$(dirname "$d")"
    while [ -n "$d" ] && [ "$d" != "/" ] && [ "$d" != "." ] && [ "${d%:}" = "$d" ]; do
      if [ -f "$d/default.project.json" ]; then
        if command -v rojo >/dev/null 2>&1 && rojo sourcemap "$d/default.project.json" -o "$d/sourcemap.json" >/dev/null 2>&1; then sm="--sourcemap=sourcemap.json"; fi
        root="$d"   # sourcemap filePaths are relative to the Rojo project, so analyze must run from there
        break
      fi
      d="$(dirname "$d")"
    done
    (cd "$root" && luau-lsp analyze --definitions="$TPL/globalTypes.d.luau" $sm "$a") 2>&1 | grep -v -E "^\[(INFO|WARN)\]|^WARNING" || true
  else echo "== luau-lsp: SKIPPED (not installed)"; fi
done
[ "$ran" -eq 0 ] && { echo "NO CHECK TOOLS INSTALLED: run 'rokit install' in $(pwd) (see README.md) or review manually"; exit 2; }
exit $rc
