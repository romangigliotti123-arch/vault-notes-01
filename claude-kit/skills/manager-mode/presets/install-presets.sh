#!/usr/bin/env bash
# Installs the manager-mode presets into ~/.claude/agents. Never overwrites a differing file: writes <name>.new instead.
set -u
src="$(cd "$(dirname "$0")" && pwd)"
dst="${HOME}/.claude/agents"
mkdir -p "$dst"
for f in sonnet-worker haiku-scout opus-builder; do
  s="$src/$f.md"; t="$dst/$f.md"
  if [ ! -e "$t" ]; then cp "$s" "$t"; echo "installed $t"
  elif cmp -s "$s" "$t"; then echo "unchanged $t"
  else cp "$s" "$t.new"; echo "kept your $t; wrote $t.new"; fi
done
echo "Start a new session or run /agents to load the presets."
