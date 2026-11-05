---
name: rbx-light-on
description: "Turn Obsidian light mode ON for the claudes-vault on this computer: hides Imported, Library, Assets and source notes so Obsidian opens fast. Switch only, no update, works offline. Use when the user says /rbx-light-on, light mode on, turn on light mode, hide the big folders, make Obsidian faster, or go back to the light view after full view. Opposite: /rbx-light-off."
disable-model-invocation: true
allowed-tools: Bash(bash *claude-kit/tools/pyrun *rbx-quick.py*)
---

!`bash "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/pyrun" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/rbx-quick.py" light on`

Reply with the output above exactly as printed. Nothing else: no commentary, no code fence, no footer, no tool calls.
