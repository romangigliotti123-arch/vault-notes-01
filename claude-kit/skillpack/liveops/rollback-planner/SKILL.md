---
name: rollback-planner
description: "Plan a reversible release before shipping: classify each change (config, code, data, asset, purchase, event), record the revert path, protect save compatibility, define the trigger and decision owner, and check the manifest with a script. Use before every major update, migration or event launch."
category: liveops
tags: rollback, release plan, revert, migration, data safety, backup, kill switch, release, regression, versioning
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: hotfix-playbook, feature-flag-config-builder, event-planner, update-cadence-planner, datastore-schema-builder, live-balance-tuner, rbx-publish
---

# rollback-planner

"Roll back first, then profile" only works if rolling back was possible. This skill runs before a release: for every change it records how to undo it and what undoing costs, and flags the changes that cannot be undone (data migrations, purchases) so they get a backup or a staged rollout. The emergency itself is `hotfix-playbook`.

## When to use
Before a major update, a data or schema change, a monetisation change, or an event launch. Not for: the incident (`hotfix-playbook`) or tuning a number (`live-balance-tuner`).

## Inputs (max 2)
1. The release content as a list of changes. 2. Who decides a rollback, how long you will watch, and the trigger (default: owner, 30 minutes, client crash rate above 5 percent for 5 minutes, the vault's example alert).

## Procedure
1. List every change and classify it: `config` (undo = restore the previous version), `code` (undo = republish the previous version), `data` (migration; undo needs a backup), `asset`, `purchase` (undo needs a refund or compensation plan), `event` (undo = kill flag).
2. Put risky behaviour behind flags and configs (`feature-flag-config-builder`), deploy the content hidden, and flip it at launch time. Record the previous config value or version before changing it (publishing a config draft is only undone by restoring a previous version).
3. Save compatibility: if new code adds save fields, old code must tolerate them, or a code rollback corrupts or drops data. Prefer additive schema changes with a version field (`datastore-schema-builder`). For data migrations: export or back up the affected records first and decide whether the migration is reversible.
4. Write `release.json` (`name`, `kind`, `revert`, plus `previous_value_recorded`, `adds_save_fields`/`old_code_reads_new_data`, `backup`, `reversible_migration`, `refund_plan`, `kill_flag`; top level `owner`, `watch_minutes`, `trigger`) and run `python -I .rbx/claude-kit/skillpack/liveops/rollback-planner/scripts/rollback.py release.json`. Every BLOCK must be fixed before shipping; read every warning. Exit 1 means do not ship.
5. Decide the restart strategy for the publish (players move to the new version only as old servers empty; use a delayed restart with a warning) and the order: config first, then code, then event start.
6. Rehearse: in Studio, publish to a test place, flip the kill flag, and confirm the revert path works (restore previous version in the place history). Time it.
7. During the watch window follow the trigger exactly; the decision owner is named in advance. If triggered, roll back, announce briefly, then profile.
8. After: compare the metrics against the pre-release same-weekday baseline (`cohort-reader`), record the outcome, and delete flags that are now permanent.

## Studio MCP path
`script_grep` for save-field access and config reads (to verify old-code tolerance) -> `multi_edit` to add flags or version fields -> `start_stop_play` + `execute_luau` (Server) to load an old-format profile into the new code and the reverse -> `get_console_output`.

## Fallback
The manifest check is Python 3. Publishing, place version history and Creator Hub config restores are the owner's actions; this skill prepares and checks the plan. Rehearsal results stay `untested` until run.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: if an update severely hurts metrics, roll back first then profile; set a crash-rate alert and webhook before release; test every update and watch the first minutes; deploy time-sensitive content behind a config then flip it; restart strategy and delayed restart with a warning. `ab-testing-and-experiments.md` (Roblox Creator Docs 2026-10): gradual rollout of 15 minutes; publishing a config draft is irreversible except by restoring a previous version. Migration and backup rules are this skill's standard practice, labelled as such (the vault notes it has no rollback timing guidance).

## Output
`liveops/release-<name>.json` + `liveops/release-<name>.md` (checked manifest, trigger, owner, rehearsal result, order of operations).

## Acceptance checks
- [ ] `rollback.py --selftest` prints "selftest ok (4 checks)" and the real manifest prints "0 blocking".
- [ ] Every data change has a backup; every config change has the previous value recorded.
- [ ] Old code tolerates new save fields, or the change is behind a flag until the old code is gone.
- [ ] The trigger, the watch window and the decision owner are written down.
- [ ] A rehearsal of the revert was run, or is marked untested.

## Pitfalls
Calling a migration reversible without a backup. Assuming a code rollback restores data. Rolling back a purchase flow without compensation. Forgetting that older servers keep running the old version for a while. Leaving flags in forever.

## Related
`hotfix-playbook`, `feature-flag-config-builder`, `event-planner`, `datastore-schema-builder`, `live-balance-tuner`.
