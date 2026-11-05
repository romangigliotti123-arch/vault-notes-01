---
name: rbx-check
description: "Check whether a newer vault or kit exists, changing nothing: fetches the git remote, compares local HEAD and the installed kit with the vault's claude-kit, reports UP TO DATE or new commits and changed kit skills, then offers /rbx-update."
allowed-tools: Bash(bash *claude-kit/tools/pyrun *rbx-quick.py*)
---

!`bash "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/pyrun" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/rbx-quick.py" check`

Reply with the output above exactly as printed. Nothing else: no commentary, no code fence, no footer, no tool calls.
