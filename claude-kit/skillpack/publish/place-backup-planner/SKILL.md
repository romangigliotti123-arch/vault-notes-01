---
name: place-backup-planner
description: "Plan and verify backups of places and assets beyond the cloud version history: exported .rbxl copies, the Rojo project, asset lists and settings notes, with a sha256 manifest you can verify, a place-size warning, and a tested restore. Use before launch, before big refactors and before transferring a game."
category: publish
tags: backup, restore, rbxl, rbxlx, place file, manifest, sha256, place size, disaster recovery, assets
kb: Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: version-history-keeper, publish-readiness-gate, group-ownership-setup, asset-license-checker, rollback-planner, project-kickoff
---

# place-backup-planner

One job: a backup you have proven you can restore. Cloud Version History is one copy under the same account; this skill adds independent copies (exported place files, the source project, an asset list, a settings snapshot) with `scripts/backup_check.py`, which writes a path/size/sha256 manifest and later verifies it, warning when a place file nears the size limit. The size limit and export formats are `live-check`: the Creator Docs change.

## When to use
Before launch, before large refactors, before a transfer to a group, and on a schedule during live operation. Not for: the release log (`version-history-keeper`), rollback decisions (`rollback-planner`), asset licence status (`asset-license-checker`).

## Inputs (max 2)
1. What to back up (default: place files, project folder, asset list, settings sheet). 2. Where copies go (default: one local folder plus one off-machine location the owner names).

## Procedure
1. Open the live place-files page (Evidence); note the export formats and the place size limit with the date.
2. Export every place: `.rbxl` (compact, binary) for storage, `.rbxlx` (XML, readable, much larger) only when diffing. In Studio: File > Save to File As.
3. Collect: exported places, the Rojo project folder (excluding `Packages` and `.git`), `release/` records, an asset list (`build/asset-license-checker/scripts/list_assets.luau` output) and the settings sheet.
4. Make the manifest: `python -I ~/.claude/claude-kit/skillpack/publish/place-backup-planner/scripts/backup_check.py make backups/<date>/manifest.json <paths...>`. WARN lines name place files over the limit; if the live limit differs, state it in the notes and trim the place (`optimization` skills) or split places.
5. Copy the folder to the second location, then verify the COPY: `python -I .../backup_check.py verify <copy>/manifest.json` (the manifest stores absolute paths, so re-make it on the copy before verifying, or verify before moving).
6. Restore test: open the exported `.rbxl` in a fresh Studio session, confirm it loads, scripts are present, and a short play session runs. Record the date. An untested backup is a hope.
7. Schedule: before each release (tied to `version-history-keeper`), before transfers, and weekly during live ops; keep the last several copies, delete older ones only with the owner's approval.
8. Write `release/backup.md`: what, where, manifest hash, restore-test result, next due date.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> no MCP tool saves a place file; `execute_luau` (Server, Edit) can list `game:GetDescendants()` counts and script sources for a text snapshot -> `get_console_output`. Saving to file and opening it are Studio UI steps by the owner.

## Fallback
Everything but the export and the restore test runs offline. The restore test stays `untested` until the owner opens the exported file.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs projects place-files.md` (.rbxl vs .rbxlx, 100 MB place limit and how to shrink, split into places), `... Docs production publishing publish-games-and-places.md` (publish early to the cloud; places over the limit may fail to save), `... Docs projects version-history.md`. Pack: `Roblox/roblox-kb/version-control-and-tooling.md`, `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`.

## Output
`backups/<date>/manifest.json` and `release/backup.md`.

## Acceptance checks
- [ ] `backup_check.py make` printed the file count and byte total (quote it).
- [ ] `backup_check.py verify` printed `verify ok` on the copy.
- [ ] A restore test was done, or the row says `untested`.
- [ ] No place file is silently over the size limit.
- [ ] `backup_check.py --selftest` prints `selftest ok`.

## Pitfalls
Backing up only into the same cloud account. Verifying a manifest after the originals moved. Exporting `.rbxlx` for storage and blowing the size. Keeping secrets (API keys) in the backup folder.

## Related
`version-history-keeper`, `publish-readiness-gate`, `group-ownership-setup`, `asset-license-checker`, `rollback-planner`.
