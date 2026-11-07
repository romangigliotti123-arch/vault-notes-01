---
name: rbx-light-off
description: "Turn Obsidian light mode OFF (full view) for the claudes-vault on this computer: everything except Assets becomes visible in Obsidian (slower, about 14,000 more notes). Switch only, no update, works offline. Use when the user says /rbx-light-off, light mode off, turn off light mode, full view, show everything, show Library and Imported. Opposite: /rbx-light-on."
disable-model-invocation: true
allowed-tools: Bash(bash *claude-kit/tools/pyrun *rbx-quick.py*)
---

!`bash ".rbx/claude-kit/tools/pyrun" ".rbx/claude-kit/tools/rbx-quick.py" light off`

Reply with the output above exactly as printed. Nothing else: no commentary, no code fence, no footer, no tool calls.
