---
name: unload-rbxdev-vault
description: "Run /unload-rbxdev-vault to turn Roblox dev mode off for this project folder: removes exactly the vault skills and agents that /load-rbxdev-vault copied here (never your own), and stops following the vault mode rules. Use when the user says /unload-rbxdev-vault, unload the vault, leave Roblox dev mode, or turn the vault off."
---

# unload-rbxdev-vault

1. Run: `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" unload` (it already uses `$CLAUDE_CONFIG_DIR` when set; else `python3` / `python` / `py -3`). Add `--all` only if the user asks to unload every folder.
2. Reply with what it printed in 1-2 lines. From now on stop following the Roblox dev mode rules from /load-rbxdev-vault in this session (vault skills already listed in this session stay listed until Claude restarts; do not use them unless the user asks).
3. A file you changed is kept and named in the output; only unchanged copies are removed. The vault, its notes, assets and your games are not touched.
