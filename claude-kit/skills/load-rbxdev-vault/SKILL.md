---
name: load-rbxdev-vault
description: "Run /load-rbxdev-vault to turn on Roblox dev mode for this project folder: loads the Roblox Dev Mastery Vault kit (its skills, agents, art-direction and visual-QA rules, reference images, learn step) which stays out of every other Claude session. Prints a one-line confirmation. Use when the user says /load-rbxdev-vault, load the vault, Roblox dev mode, enable the vault, or wants to make or work on a Roblox game and the vault skills are not loaded. /unload-rbxdev-vault turns it off."
---

# load-rbxdev-vault

The vault kit is installed but NOT loaded by default, so unrelated Claude sessions stay clean. This command loads it for the current folder.

1. Run: `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" load` (it already uses `$CLAUDE_CONFIG_DIR` when set; without `pyrun` use `python3` / `python` / `py -3` on `$K/claude-kit/tools/vault-mode.py`). If the vault skills (for example `game-dev-workflow`) already appear in your skill list because Claude was started with `--add-dir <config>/claude-kit/vault-mode`, add `--no-link` (writes nothing).
2. Reply with the first line it printed (`Roblox dev mode on: N skills, M agents, ...`) and then only the extra lines it printed about restarting, collisions or skipped items. Do not paraphrase them.
3. Everything after the blank line is the mode rules: follow them for the rest of this session. Skills copied into a folder that already had `.claude/skills` appear in the skill list a few seconds later (not instantly).
4. If it says the kit is not installed, tell the user to run `/update-rbxdev-vault`. If it says the folder is the home or config folder, ask the user to open Claude in their project folder.

It only writes inside this folder's `.claude/` (skills and agents it lists in `.claude/vault-mode.json`, hidden from git). It never edits `settings.json`, your global CLAUDE.md or your own skills; a skill or agent of yours with the same name is skipped and yours wins.
