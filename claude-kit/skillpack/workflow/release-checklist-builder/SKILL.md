---
name: release-checklist-builder
description: "Build the per-release checklist for an update to a Roblox game: gates with a command or owner for each, a rollback step, and a sign-off line, tailored to what this release touches (data, monetisation, map, UI). Use before every update publish; the first launch uses the publish gates instead."
category: workflow
tags: release, update, checklist, gate, rollback, sign-off, publish, version, ship
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md, Manager/topic-report-formats-and-verification.md, Mentor/Combined-Brain.md
related: publish-readiness-gate, rbx-publish, rbx-launch-check, regression-checklist-builder, changelog-writer, version-history-keeper, rbx-game-update
---

# release-checklist-builder

One checklist per release, short enough to finish. First-launch go/no-go is `publish-readiness-gate` and `rbx-launch-check`; a general regression suite is `regression-checklist-builder` (qa); the player announcement is `rbx-game-update` and `update-announcement-writer`. This skill picks only the gates this release's diff makes relevant, with a rollback step for each risky area.

## When to use
You are about to publish an update to a live or soft-launched place. Not for: the very first publish, or experiments that never leave Studio.

## Inputs (max 2)
1. The diff scope (default: `git diff --stat <last-release-tag>..HEAD`). 2. The last known-good version reference (a git tag or the Creator Hub version number; if none, say so and make "create a restore point" gate zero).

## Procedure
1. Classify what changed from the diff: data schema or save code, monetisation (passes, products, prices), map or streaming, UI, remotes or security, balance numbers. Stop and ask if the diff is empty.
2. Start from gate zero: a restore point exists (`git tag rel-<date>` and the Creator Hub version or place backup noted; see `version-history-keeper`, `place-backup-planner`). No restore point, no release.
3. Add the always-gates, each with a command or an owner: `luau-check.sh src` clean; `rojo build -o build.rbxl` succeeds; a 3-minute playtest with no red Output lines (`playtest-evidence-logger` format); version string and `docs/CHANGELOG.md` updated (`changelog-writer`).
4. Add the conditional gates only for the classes found in step 1: data change -> old-record fixture test and migration run; monetisation -> `receipt-flow-tester` and prices checked against the source of truth; remote change -> server validation review; map -> mobile device check and streaming check; balance -> the numbers diff read by a human.
5. Write the rollback plan per risky class: what to revert (git revert of a tag range, restore previous published version) and who decides within the first hour; for data changes, say whether the migration is reversible.
6. Add the sign-off: the human owner's name or `pending`, because publishing is the user's action, never a worker's.
7. Save `docs/release-<version>.md` (headings Gate, Rollback, Sign-off; under 90 lines). Every gate ends as `[met]` with evidence, `[unmet]`, or `[untested]` with the reason.

## Studio MCP path
`list_roblox_studios`, `start_stop_play`, `get_console_output` for the playtest gate; the checklist records `Studio MCP: yes/no`. Publishing itself is never done through the worker.

## Fallback
Shell gates plus a manual playtest; the Studio-only gates are `untested` and block the release unless the owner accepts them in writing.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md` (update rhythm and what breaks live games), `Roblox/roblox-kb/testing-debugging-and-qa.md`, `Roblox/roblox-kb/version-control-and-tooling.md` (meaningful publish messages for audit and rollback; commit a snapshot before risky changes), `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`, `Manager/topic-report-formats-and-verification.md` (every done line carries evidence). Version History behaviour (restore creates a new version) is a live-check against the current Creator docs.

## Output
`docs/release-<version>.md` with gates (status plus evidence), rollback plan and sign-off line.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/release-<version>.md --kind release` prints PASS.
- [ ] Executed: `luau-check.sh src` and `rojo build -o build.rbxl` were run this session and their last lines pasted.
- [ ] Gate zero (restore point) is `[met]` with a tag or version reference.
- [ ] Every conditional gate maps to a class found in the diff; none are copied blindly.
- [ ] Before each release a crash-rate alert, a webhook and written rollback thresholds exist; on a major CCU or crash-rate regression the plan is to roll back first, then profile (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, analytics-metrics, updates-live-ops).

## Pitfalls
Generic 40-line lists nobody finishes. Releasing on a Friday evening with no one to roll back. Changing save code and monetisation in the same release. Treating `untested` as a pass.

## Related
`publish-readiness-gate`, `rbx-publish`, `regression-checklist-builder`, `changelog-writer`, `version-history-keeper`, `rbx-game-update`.
