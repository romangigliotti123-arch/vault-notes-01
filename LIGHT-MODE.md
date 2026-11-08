# Light mode (why the Roblox Dev Mastery Vault opens fast)

Light mode hides only the big supporting folders (Library, Imported, Assets) from Obsidian; the Roblox knowledge base and the Manager notes stay visible.

The vault holds 8,069 notes. Indexing all of them makes Obsidian lag, so the synced `.obsidian` config opens it light:

- `Games/` and `Models/` (your own games and saved models; always hidden from Obsidian and git), `Imported/`, `Library/` and `Assets/` (the synced Roblox assets, 31,615 files) are set under Settings > Files and links > Excluded files. Obsidian does not index, search, or graph them. `Roblox/` and `Manager/` stay indexed.
- The default graph shows only `Roblox/roblox-kb`, `Manager/` and the Roblox home note (about 620 nodes), with no orphans, tags or attachments.
- Backlinks, outgoing-links, word-count, Sync and Canvas core plugins are off.

To see Library and Imported (full view), use the switch; do not edit Obsidian's settings by hand, because every update resets `.obsidian` to the repo's version:

- Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Obsidian\rbx-dev-vault\vault-update.ps1" -FullView on`
- macOS/Linux: `bash ~/Obsidian/rbx-dev-vault/vault-update.sh --full-view on`
- Back to light mode: the same command with `-FullView off` / `--full-view off`. In Claude: /rbx-update with full view on or off.

Full view keeps only `Assets/`, `Games/` and `Models/` excluded and is slower: Obsidian indexes about 2,500 more notes (Library and Imported). The choice is a marker file `.full-view` in the vault root (ignored by git) and survives every update: after each update `.obsidian/app.json` is rewritten with `userIgnoreFilters` = `Assets/` only, all other keys untouched, and that rewrite is never treated as a local change. Close and reopen Obsidian after switching.

Updates are self-healing: if the vault has local changes (for example Windows line endings or Obsidian rewriting `.obsidian/graph.json`), the update saves them to `local-changes-<timestamp>.patch` in the sync state folder, resets to the latest, and prints one line.

All files stay on disk and in git, untouched. Claude, grep, query-vault.ps1 and graphify still search everything.

Your own work is safe: `Games/` (your per-game communities and `Games/_Reusable`, made by /rbx-workflow), `My Research/` (default output folder of the research skill), any folder containing `PROTECTED-RESEARCH.md` and every untracked file you created are never deleted by `/rbx-update` (git-excluded); only edits to tracked (generated) files are patched and reset. `My Research` is a reserved name: the main vault never ships files there. Two commands: `/rbx-update` (safe, keeps everything of yours) and `/rbx-clean` (exact copy of the main vault, still keeps My Research; prints a dry run, asks once, backs up what it removes). One-liners: `vault-update.ps1 -Clean [-Yes] [-IncludeMine]` / `bash vault-update.sh --clean [--yes] [--include-mine]` (`-IncludeMine` also deletes My Research, only when you type it).

Quick switch (no update, works offline): `/rbx-light-on` and `/rbx-light-off` in Claude, or `vault-update.ps1 -SetView light|full` / `bash vault-update.sh --set-view light|full`. Reopen Obsidian after.

