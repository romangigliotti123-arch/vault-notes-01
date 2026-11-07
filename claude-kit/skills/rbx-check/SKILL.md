---
name: rbx-check
description: "Check whether a newer vault or kit exists, changing nothing: fetches the git remote, compares local HEAD and the installed kit with the vault's claude-kit, reports UP TO DATE or new commits and changed kit skills, then offers /rbx-update."
allowed-tools: Bash(bash *claude-kit/tools/pyrun *rbx-quick.py*)
---

The stub in `~/.claude/skills/rbx-check` ran `where.py`, which printed `VAULT <folder>` and `KIT <folder>` (the kit lives in the vault folder: `<vault>/.rbx/claude-kit`; the folder may have been moved, where.py finds it again). Run this one command with `<KIT>` = the printed KIT folder:

`bash "<KIT>/tools/pyrun" "<KIT>/tools/rbx-quick.py" check`

Reply with its output exactly as printed. Nothing else: no commentary, no code fence, no footer, no other tool calls.
