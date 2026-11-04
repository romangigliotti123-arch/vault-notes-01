---
name: rbx-light-on
description: "Turn Obsidian light mode ON for the claudes-vault on this computer: hides Imported, Library, Assets and source notes so Obsidian opens fast. Switch only, no update, works offline. Use when the user says /rbx-light-on, light mode on, turn on light mode, hide the big folders, make Obsidian faster, or go back to the light view after full view. Opposite: /rbx-light-off."
disable-model-invocation: true
---

# rbx-light-on

Run without questions. Switch only: no git fetch, no update, works offline.

1. Find the vault (first existing wins): `$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`. If none exists, say so in one line and stop.
2. Run the script in the vault root:
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "<vault>\vault-update.ps1" -SetView light`
   - macOS/Linux: `bash "<vault>/vault-update.sh" --set-view light`
3. Report its one output line (it ends with "Reopen Obsidian."). Do not run /rbx-update, do not edit .obsidian by hand. The choice survives later updates.
