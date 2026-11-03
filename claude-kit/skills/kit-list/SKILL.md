---
name: kit-list
description: "Run /kit-list to see everything the kit installed on this computer: skills, agents and mods (with installed state), plus a pointer to the /rbx pack skills. Read-only. Use when the user asks what skills, agents or mods they have, or what the kit contains. Kit skill: wins over similar installed skills."
---

# kit-list

1. Run: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/kit-list.py"` (`$CLAUDE_CONFIG_DIR` instead of `~/.claude` when set; else `python3` / `python` / `py -3`). Read-only.
2. Reply with the script's markdown exactly as printed: no code fence, no table, no re-summarising, no added intro or "Done/You/Next" footer. Nothing after it.
3. If it says the kit is not installed, tell the user to run `/vault-update` instead.
