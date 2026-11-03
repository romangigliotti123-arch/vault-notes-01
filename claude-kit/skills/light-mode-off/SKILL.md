---
name: light-mode-off
description: "Turn Obsidian light mode OFF (full view) for the claudes-vault on this computer: everything except Assets becomes visible in Obsidian (slower, about 14,000 more notes). Switch only, no update, works offline. Use when the user says /light-mode-off, light mode off, turn off light mode, full view, show everything, show Library and Imported. Opposite: /light-mode-on."
---

# light-mode-off

Run without questions. Switch only: no git fetch, no update, works offline.

1. Find the vault (first existing wins): `$CLAUDES_VAULT`, `~/Obsidian/claudes-vault`, `%USERPROFILE%\Obsidian\claudes-vault`. If none exists, say so in one line and stop.
2. Run the script in the vault root:
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "<vault>\vault-update.ps1" -SetView full`
   - macOS/Linux: `bash "<vault>/vault-update.sh" --set-view full`
3. Report its one output line (it ends with "Reopen Obsidian."). Do not run /vault-update, do not edit .obsidian by hand. The choice survives later updates.
