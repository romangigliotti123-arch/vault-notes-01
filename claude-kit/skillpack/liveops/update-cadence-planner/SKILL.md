---
name: update-cadence-planner
description: "Set a realistic update cadence from team size and effort: cadence drops on existing systems plus periodic major updates, as a dated Friday calendar with dev cutoffs, announcement dates and a sustainability verdict. Use when starting live ops, after burnout, or before promising players a schedule."
category: liveops
tags: cadence, update schedule, live ops, roadmap, weekly, monthly, major update, pipeline, burnout, friday
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/team-and-budget.md, Roblox/roblox-kb/events-and-seasonal-content.md
related: event-planner, seasonal-calendar-builder, patch-notes-writer, hotfix-playbook, rollback-planner, game-dev-update, game-dev-weekly
---

# update-cadence-planner

A cadence is a promise. The vault is blunt: weekly is the ideal, monthly the floor, and many big games moved from weekly to bi-weekly or monthly because the team could not sustain it. This skill turns your capacity into a schedule you can keep. One event is `event-planner`; the holiday map is `seasonal-calendar-builder`; the kit `game-dev-update` runs a single update.

## When to use
Starting live ops, restarting after a hiatus, or players ask "when is the next update". Not for: planning one event, fixing a crash (`hotfix-playbook`) or deciding whether to continue a game with no traction (vault: gate continue-or-abandon on traction, see `idea-validator`).

## Inputs (max 3)
1. Team: people and focused days per person per week (default: 1 person, 4 days). 2. Typical effort of one cadence drop and one major update in person-days (default: 4 and 30). 3. Start date and horizon (default: next Friday, 12 weeks).

## Procedure
1. Collect the inputs. Cadence content must reuse existing systems (new currencies and mechanics go into major updates first). If a drop needs over three weeks of effort, split it (vault: keep recurring content under three weeks).
2. Run `python -I ~/.claude/claude-kit/skillpack/liveops/update-cadence-planner/scripts/cadence.py --team <n> --start <date> --weeks 12 --minor-days <d> --major-days <d> --days-per-week 4 --major-every 10`. It splits capacity 60 percent cadence and 40 percent major (this skill's default, not a sourced rule), picks 1, 2 or 4 week intervals, and prints Friday launch dates, Wednesday dev cutoffs and announcement dates at least 3 days apart. Stop condition: if it prints NOT SUSTAINABLE or a NOTE, change scope or people before showing the calendar to anyone.
3. Keep cadence running while the major update is built (vault: dropping cadence launches the expansion to a shrunken base). Alternate minor and major so the workload spreads.
4. Add the fixed slots the schedule must survive: a bug-fix week after any major update (first post-launch release: a dedicated fix and polish update), holidays (`seasonal-calendar-builder`), and your lowest-staff days. Same-day silent patches are outside the calendar (`hotfix-playbook`).
5. Pick the one metric each drop targets (vault: aim at your weakest stat; D1 or D7). After each drop, read D1, D7, session time, conversion and new users against the pre-update baseline over the same weekdays (`cohort-reader`).
6. Publish the promise carefully: announce dates only for the next one or two drops, keep a backlog for slips, and announce delays rather than going silent (vault).
7. Review monthly: if two drops in a row slipped or were rushed, move one step down (weekly to bi-weekly to monthly) on purpose and say so.

## Studio MCP path
Not needed. If the plan includes a config-gated release, `script_grep` for the config reads first (`feature-flag-config-builder`).

## Fallback
Pure Python 3 and a text file. Nothing here touches a place.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: cadence 1-2 weeks, at least monthly (Roblox Creators talks, official); keep cadence to existing systems; do not drop cadence during a big update; expansions about quarterly; weekly the ideal and monthly the floor (single official source); cadence updates under three weeks of effort; Friday launch with Wednesday-night cutoff; announcements at most one per 3 days; Jailbreak ran weekly two years then monthly (reported). Indie claims (daily updates in week one) are labelled indie there.

## Output
`liveops/cadence.md`: capacity line, interval, dated table (date, kind, content theme, target metric, cutoff, announce), sustainability notes, review date.

## Acceptance checks
- [ ] `cadence.py --selftest` prints "selftest ok (5 checks)" and the real run ended without NOT SUSTAINABLE.
- [ ] Every launch is a Friday with a Wednesday cutoff; announcements are at least 3 days apart.
- [ ] Each drop has a target metric and a re-read date.
- [ ] A bug-fix slot follows every major update and cadence continues during major builds.
- [ ] The promise to players covers at most the next two drops.
- [ ] A team that cannot ship at least monthly gets the schedule risk flagged with a recovery phase (not silence); time-sensitive content ships hidden behind a config value that is flipped, not a republish (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, updates-live-ops).

## Pitfalls
Copying a big game's cadence. Adding new systems in cadence drops. Announcing dates you cannot hold. Letting content bloat (vault: too much content makes players quit or feel they cannot keep up). Stopping updates on a game that has traction.

## Related
`event-planner`, `seasonal-calendar-builder`, `patch-notes-writer`, `hotfix-playbook`, `game-dev-update`.
