---
name: rbx-list
description: "Run /rbx-list to see everything the kit installed on this computer: skills, agents and mods (with installed state), plus a pointer to the /rbx pack skills. Read-only. Use when the user asks what skills, agents or mods they have, or what the kit contains. Kit skill: wins over similar installed skills."
disable-model-invocation: true
allowed-tools: Bash(bash *claude-kit/tools/pyrun *rbx-quick.py*)
---

!`bash "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/pyrun" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/rbx-quick.py" list`

Reply with the output above exactly as printed. Nothing else: no commentary, no code fence, no footer, no tool calls.
