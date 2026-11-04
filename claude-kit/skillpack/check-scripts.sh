#!/bin/bash
# check-scripts.sh [skill-folder ...]  Run the kit's Luau checks (stylua --check, selene, luau-lsp) on every skillpack scripts/*.luau
# (tests excluded) and run every scripts/tests/*.test.luau under Lune. Default: the whole skillpack. Exit 0 = all passed.
KIT="$(cd "$(dirname "$0")/.." && pwd)"
SP="$KIT/skillpack"
rc=0
targets=("$@"); [ ${#targets[@]} -eq 0 ] && targets=("$SP")
abs=(); for t in "${targets[@]}"; do abs+=("$(cd "$t" 2>/dev/null && pwd || echo "$t")"); done; targets=("${abs[@]}")
files=()
for t in "${targets[@]}"; do
  while IFS= read -r f; do files+=("$f"); done < <(find "$t" -name '*.luau' -path '*/scripts/*' ! -path '*/tests/*' | sort)
done
echo "checking ${#files[@]} Luau files"
out="$(bash "$KIT/tools/roblox-project-template/luau-check.sh" "${files[@]}" 2>&1)"; code=$?
echo "$out" | grep -v -E "^== " | grep -v -E "^(Results:|0 errors|0 warnings|0 parse errors)$"
echo "luau-check exit $code"
if [ $code -ne 0 ] || echo "$out" | grep -q -E "TypeError|SyntaxError|LocalUnused|^error|stylua.*Diff|^Diff in"; then rc=1; echo "LUAU CHECK FAILED"; fi
cd "$KIT/systems" || exit 1
n=0; fail=0
for t in "${targets[@]}"; do
  while IFS= read -r f; do
    n=$((n+1)); rel="$(sh "$KIT/tools/pyrun" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$f" "$KIT/systems")"
    res="$(lune run "$rel" 2>&1 | tail -1)"; echo "lune $(basename "$f"): $res"
    case "$res" in *" 0 failed"*) ;; *) fail=$((fail+1));; esac
  done < <(find "$t" -name '*.test.luau' | sort)
done
echo "$n lune test files, $fail failing"
[ $fail -ne 0 ] && rc=1
exit $rc
