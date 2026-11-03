---
name: version-history-keeper
description: "Keep a release log with restore points tied to Studio Version History: semantic version labels, a place version number per release, player-facing notes, a named restore point, and the rollback procedure that actually reaches players. Use at every publish and when rolling back."
category: publish
tags: version history, release log, versioning, restore point, rollback, publish notes, semantic version, releases
kb: Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: place-backup-planner, publish-readiness-gate, post-launch-monitor, update-cadence-planner, rollback-planner, regression-checklist-builder
---

# version-history-keeper

One job: every publish leaves a record you can act on. Roblox keeps cloud versions of a place; this skill adds the human layer on top: a release number, the place version it maps to, notes written for players, a named restore point, and the gate verdict. `scripts/release_log.py` keeps an append-only `release/release-log.jsonl` and refuses entries that are not greater than the last, have empty notes, no restore point or a backwards place version. The Studio Version History features and menus are `live-check`: the Creator Docs change.

## When to use
At every publish, before risky changes, and the moment a rollback is needed. Not for: backing up files outside the cloud (`place-backup-planner`), planning the rollback decision tree (`rollback-planner`), the go/no-go (`publish-readiness-gate`).

## Inputs (max 2)
1. What changed for players (one or two sentences). 2. Bump size: patch, minor or major (default: patch for fixes, minor for content, major for rewrites).

## Procedure
1. Open the live Version History page (Evidence) and copy the current save/publish/restore steps with the date.
2. Save with notes at every meaningful checkpoint (Save to Roblox with Notes); publish notes auto-draft only from notes logged between publishes, so gaps give no summary.
3. After the gate says GO (`publish-readiness-gate`), get the version: `python -I ~/.claude/claude-kit/skillpack/publish/version-history-keeper/scripts/release_log.py next release/release-log.jsonl --bump patch`.
4. Publish (owner action). Read the new place version number off Version History or Creator Hub; never guess it.
5. Record: `python -I .../release_log.py add release/release-log.jsonl --version <v> --place-version <n> --notes "<what changed for players>" --restore "<named restore point, e.g. 'VH #n: release 1.4.2'>" --gate "GO release/gates.json"`. A refusal prints why.
6. Run `python -I .../release_log.py check release/release-log.jsonl`; it must print `log ok`.
7. Rollback: restoring a version in Version History creates a new version and does NOT publish it. Disable Team Create first so collaborators' auto-saves cannot overwrite the revert, restore, publish, restart servers, then add a new log entry that says "rollback to <version>" with the new place version.
8. Tag the repository too (git tag with the same version) when the project is under source control; keep the log file in the repo.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> there is no MCP tool for Version History: it is a Studio/Creator Hub UI feature, so the owner reads the number. `execute_luau` (Server) can print `game.PlaceVersion` in a published session to confirm which version is live -> `get_console_output`.

## Fallback
The log and its checks are plain files. Restore and publish are owner actions in Studio or Creator Hub; they stay `untested` until the owner runs a restore on a test place.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs projects version-history.md` (notes on every save, searchable checkpoints, publish notes from logged notes, restore creates a new version and does not publish, restart servers), `... Docs projects collaboration.md` (disable Team Create before reverting), `... Docs projects activity-history.md` (audit who changed settings). Pack: `Roblox/roblox-kb/version-control-and-tooling.md`, `Roblox/roblox-kb/updates-live-ops.md`.

## Output
`release/release-log.jsonl` and, per release, one line in the changelog for players.

## Acceptance checks
- [ ] `release_log.py check` prints `log ok` (quote it).
- [ ] The new entry's place version came from the dashboard.
- [ ] The restore point is named and findable in Version History.
- [ ] A rollback, if any, is logged as its own entry.
- [ ] `release_log.py --selftest` prints `selftest ok`.

## Pitfalls
Restoring and assuming players got it. Editing old log lines instead of appending. Logging the version before the publish succeeded. Version notes like "fixes" that help nobody on a bad night.

## Related
`place-backup-planner`, `publish-readiness-gate`, `post-launch-monitor`, `update-cadence-planner`, `rollback-planner`.
