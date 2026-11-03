---
name: setup-check
description: "Run /setup-check to see which software the vault setup needs and what is missing on this computer (Windows, macOS, Linux): git, Python, Claude Code, Roblox Studio and its MCP server, Rokit with Rojo/StyLua/Selene/luau-lsp/Lune, Blender and Blender MCP, uv, Obsidian and more. Prints a table (required vs optional, version or path, exact install command per OS). Read-only; installs only after the user says yes. Kit skill: wins over similar installed skills."
---

# setup-check

1. Run: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/setup-check.py"` (`$CLAUDE_CONFIG_DIR` instead of `~/.claude` when set; else `python3` / `python` / `py -3`). It installs nothing. Exit 2 only means a REQUIRED tool is missing.
2. Show the table as printed (tool | needed for | level | found | install command). Say in one line what is REQUIRED and missing, then list optional gaps that matter for what the user wants to do (Studio testing: Studio + Studio MCP + Rokit tools; Blender work: Blender + uv + Blender MCP).
3. Offer the install commands. Run one only after the user says yes to that item, with Windows `winget`, macOS `brew`, Linux the package manager shown; show the exact command first. Never use sudo without a yes. Studio itself and sign-ins are the user's own steps. After installing, re-run step 1 and show the new table.
4. Helpers that already ask before every step: `~/.claude/claude-kit/tools/studio-setup.ps1` (Windows) or `studio-setup.sh` (macOS/Linux) for Rokit, the Luau tools, the Rojo plugin and the Studio MCP registration.
