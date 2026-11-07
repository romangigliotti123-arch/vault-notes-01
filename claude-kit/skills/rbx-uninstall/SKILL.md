---
name: rbx-uninstall
description: "Remove the whole Roblox Dev Mastery Vault kit from this computer, keeping only the user's games (Games/ incl. _Reusable, plus My Research, Models/, My-Skills/ and My-Agents/). Dry-run first; nothing is deleted until the user says yes. Use for /rbx-uninstall, uninstall the vault, remove the kit."
disable-model-invocation: true
---

# rbx-uninstall

Removes the kit (agents, skills, tools, hooks, auto-sync job, `<config>/claude-kit`) and the vault folder, and keeps only the user's games. Python 3 only: `scripts/uninstall.py` (config dir: `$CLAUDE_CONFIG_DIR`, else `~/.claude`).

1. Run the plan (changes nothing): `python "<config>/skills/rbx-uninstall/scripts/uninstall.py"` (use `python3`/`py` if `python` is missing). Add `--vault DIR` if it says it cannot find the vault or finds several.
2. Show the user the plan in plain words: where the games will be copied (default `~/Roblox Games`, change with `--keep-dir DIR`), what will be removed, kit files they edited (backed up to `<keep-dir>/_edited-kit-files`, or left in place with `--keep-edited`), and what is NOT touched (credentials, other skills/agents/settings, MCP servers, Rokit/Luau tools, projects under `$ROBLOX_PROJECTS`, which stay in place).
3. Ask: "Remove everything except your games? yes/no". Do NOT continue without an explicit yes in the chat. Never pass `--yes` on your own.
4. After the yes, run the same command with `--yes` (plus the same other flags). It copies the games first and checks the copy byte for byte, removes hooks (settings.json backed up), deletes the kit, then the vault, and the skill itself last. If the copy check fails nothing is deleted.
5. Report the summary it prints: where the games are now, anything left, `CLAUDE.md` lines that mention the kit (list them, never edit them). To reinstall later: follow the website setup (`SETUP-FOR-CLAUDE.md`) or the vault README.

Never delete anything by hand around this script. Never run it on a vault path the user did not confirm.
