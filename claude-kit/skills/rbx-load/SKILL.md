---
name: rbx-load
description: "Run /rbx-load to turn on Roblox dev mode for this project folder: loads the vault kit (skills, agents, art-direction and visual-QA rules, reference images, learn step); other sessions stay clean. Use when the user wants to make or work on a Roblox game and the vault skills are not loaded."
---

# rbx-load

The kit is installed but NOT loaded by default; this loads it for the current folder.

1. Run: `K="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"; bash "$K/claude-kit/tools/pyrun" "$K/claude-kit/tools/vault-mode.py" load` (it already uses `$CLAUDE_CONFIG_DIR` when set; without `pyrun` use `python3` / `python` / `py -3` on `$K/claude-kit/tools/vault-mode.py`). If the vault skills (for example `rbx-workflow`) already appear in your skill list because Claude was started with `--add-dir <config>/claude-kit/vault-mode`, add `--no-link` (writes nothing).
2. Reply with the first line it printed (`Roblox dev mode on: N skills, M agents, ...`) and then only the extra lines it printed about restarting, collisions or skipped items. Do not paraphrase them.
3. Everything after the blank line is the mode rules: follow them for the rest of this session. Skills copied into a folder that already had `.claude/skills` appear in the skill list a few seconds later (not instantly).
4. If it says the kit is not installed, tell the user to run `/rbx-update`. In the home or config folder it loads for this session only (nothing written; the output ends with a skill index: Read a SKILL.md from its path when a task matches). `/rbx-unload` there only stops the mode.

It only writes inside this folder's `.claude/` (skills and agents it lists in `.claude/vault-mode.json`, hidden from git). It never edits `settings.json`, your global CLAUDE.md or your own skills; a skill or agent of yours with the same name is skipped and yours wins.
