---
name: hotfix-playbook
description: "Steps to ship and verify an emergency fix on a live Roblox game: severity, rollback-or-fix decision, minimal change, test, restart strategy with warning, post-publish watch, status post and changelog, tracked in a validated incident record. Use when something live is broken now."
category: liveops
tags: hotfix, incident, emergency, patch, rollback, outage, silent patch, restart, crash rate, status
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: rollback-planner, patch-notes-writer, dau-drop-investigator, feature-flag-config-builder, exploit-audit, discord-server-setup, rbx-publish
---

# hotfix-playbook

The vault gives short, blunt rules: roll back a severe regression first and profile after; do not hold critical fixes for the weekly cycle; test before release and watch the first minutes; post status updates during outages. It also says it has no incident severity levels or compensation guide, so the severity scale here is this skill's own. Planning reversible releases ahead of time is `rollback-planner`.

## When to use
A live bug, exploit, crash spike, data problem or broken event. Not for: planned content (`update-cadence-planner`), diagnosing a slow decline (`dau-drop-investigator`), or a purely cosmetic bug (queue it).

## Inputs (max 2)
1. What is wrong, since when, and how many players it touches. 2. What changed recently (last publish, config push, event start).

## Procedure
1. Triage and name a severity (S1 data loss, exploit or unplayable; S2 major feature or economy harm; S3 annoying). Start the record: `python -I .rbx/claude-kit/skillpack/liveops/hotfix-playbook/scripts/hotfix.py new --title "..." --severity S1 > hotfix-<date>-<slug>.md`.
2. Stop the bleeding first. If a config or flag controls it, flip it (`feature-flag-config-builder`: kill switch; config changes take about 5 minutes). If an event or item is exploited, disable it and, for exploits, stop grants before fixing the cause (`exploit-audit`). If a publish caused a severe regression, roll back (restore the previous version), then profile (Developer Console, Script Profiler, MicroProfiler).
3. Post a status line within minutes for S1 and S2 (Discord and in-game banner if you have one): what is known, what is being done, when the next update comes. Silence reads as abandonment (vault).
4. Reproduce and fix with the smallest change that removes the cause. No refactors, no content. Data-affecting fixes need a backup and a note on who gets compensated (decide the rule before announcing; never promise items you cannot grant).
5. Test the exact path: Studio Play test with two clients if networked, plus the regression you are fixing. A hotfix that skips tests is how half the players left in one reported case.
6. Publish. Choose the restart strategy deliberately: players only move to the new version as old servers empty; either restart only servers with outdated versions or use the delayed restart (1-60 minutes) with a warning so players leave on their own and data saves. Protect saves (soft shutdown to a lobby per the vault; BindToClose save handling is general practice, not covered in the vault).
7. Watch the first 30 minutes: error count grouped by message, crash rate, join success, the specific KPI, and Discord. Have a crash-rate alert in place (vault example: client crash rate above 5 percent for 5 minutes) and a webhook. If it is worse, roll back again.
8. Close out: verify the metric recovered against the same weekday baseline, fill the record, and add the fix to the next changelog (`patch-notes-writer`; silent patches are still logged). Run `hotfix.py check <file>` and fix every FAIL line. Add a regression check so it cannot recur.

## Studio MCP path
`get_console_output` and `script_grep` to find the failing path -> `multi_edit` for the minimal change -> `start_stop_play` -> `execute_luau` (Server) to reproduce and assert the fix -> publish by hand. Publishing a live place is the owner's action; the skill prepares everything.

## Fallback
Without Studio: write the exact diff and test steps for the owner; the incident record and its check are plain text.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: roll back severe regressions then profile; alert on crash rate before pushing an update with a webhook; test every update and watch the first minutes (a rushed update broke the game); ship same-day silent patches for bugs and add them to the changelog; choose server restart strategy and use a delay with a warning; minimise shutdowns, soft-shutdown to a lobby; post live status during outages (indie guide). Gaps stated there: no severity levels, compensation or rollback timing guidance.

## Output
`liveops/hotfix-<date>-<slug>.md` (validated record: severity, detected, impact, cause, fix, rollback, tested, verify metric and window, status post, changelog) plus the status message text.

## Acceptance checks
- [ ] `hotfix.py --selftest` prints "selftest ok (5 checks)"; `hotfix.py check` on the record returns 0 problems.
- [ ] A rollback path is named; an S1/S2 status post exists.
- [ ] The fix was tested on the failing path, or the record says why not.
- [ ] A watch window and a recovery metric are defined and read.
- [ ] The fix is in the next changelog.

## Pitfalls
Fixing forward when rollback is faster. Bundling features into a hotfix. Skipping the restart warning and losing unsaved progress. Promising compensation first. Not writing the regression check.

## Related
`rollback-planner`, `patch-notes-writer`, `dau-drop-investigator`, `feature-flag-config-builder`, `exploit-audit`.
