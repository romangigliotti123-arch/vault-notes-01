---
name: rbx-unload
description: "Run /rbx-unload to turn Roblox dev mode off for this folder: removes exactly the vault skills and agents /rbx-load copied here (never your own). Use for unload the vault, leave Roblox dev mode, turn the vault off."
---

# rbx-unload

1. Run: `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" unload` (it already uses `$CLAUDE_CONFIG_DIR` when set; else `python3` / `python` / `py -3`). Add `--all` only if the user asks to unload every folder.
2. Reply with what it printed in 1-2 lines. From now on stop following the Roblox dev mode rules from /rbx-load in this session (vault skills already listed stay listed in this chat; open a new chat for a clean list; do not use them unless the user asks).
3. A file you changed is kept and named in the output; only unchanged copies are removed. The vault, its notes, assets and your games are not touched.
