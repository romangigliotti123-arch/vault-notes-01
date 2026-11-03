---
name: event-planner
description: "Plan one limited-time Roblox game event end to end: goal and metric, theme, player objective, earned rewards, schedule with server-synced time, balance for casual and grinding players, announcement beats, admin test hooks and a rollback plan. Use when D7 or return rate needs a lift, for a holiday, or for an update launch."
category: liveops
tags: event, live ops, limited time, seasonal, holiday, update, fomo, rewards, schedule, return hook
kb: Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/case-studies-grow-a-garden.md
related: update-cadence-planner, seasonal-calendar-builder, patch-notes-writer, rollback-planner, economy-health-monitor, reward-schedule-designer, discord-server-setup, game-dev-update
---

# event-planner

An event is a reason to come back at a specific time. The plan decides the one thing it should change (a metric), then the smallest content that changes it. Cadence across months is `update-cadence-planner`/`seasonal-calendar-builder`; the kit skill `game-dev-update` covers the update pipeline. This plans ONE event.

## When to use
A return-hook is needed, a holiday is coming, or a major update needs a launch moment. Not for: permanent systems (daily rewards: `daily-reward` in the kit systems), or fixing a broken core loop (`core-loop-designer`).

## Inputs (max 3)
1. Goal metric (default: D7 and sessions per user). 2. Team size and time to build (default: solo, 1-2 weeks). 3. Date window and theme ideas (default: none; propose three).

## Procedure
1. Set the goal in one sentence with a number to compare: "lift D7 by moving returning players per day up" or "launch update 12 to a concurrent peak". Pick the guard metric (D1, rewards inflation).
2. Theme and fantasy: tie to the game's world; a constrained theme beats random content (vault: thematic updates over volume). Mix limited-time and permanent: the limited part creates urgency, the permanent part keeps value after the event.
3. Objective: what the player does (collect N, beat a boss, trade, build) that uses the CORE LOOP in a new light. Events that need a new loop or a new tutorial rarely pay back.
4. Rewards: earned, not handed out (tie prizes to a challenge); cosmetic and prestige first; no paid randomness; do not make event modes instantly open to everyone if the point is participation; serve both casual (a free tier reachable in a few short sessions) and grinders (a stretch tier). Do NOT secretly raise drop odds near the end to push spending (vault flags this as a trust-destroying pattern). Frame urgency honestly ("ends Sunday"), not as a threat.
5. Schedule: fixed start time announced in advance (the community arrives together); use the server-synced clock (DateTime/UTC time, never `tick()`, which desyncs across servers); length flexes with engagement (extendable); pre-launch sign-up or teaser; avoid clashes with other updates and with your lowest-staff days.
6. Build list (smallest first): config table with start/end, reward table, objective counters in the save schema (`datastore-schema-builder` step), an admin command to start/stop the event for testing (kit system `Admin`), UI banner and progress bar, announcement assets. Keep event code out of replicated containers until launch.
7. Announcement beats (`discord-server-setup` channels): tease 3-5 days out, countdown, launch post, mid-event reminder, last-day post, thanks + results; patch notes (`patch-notes-writer`).
8. Test: simulate the event via the admin command, run a bot through the objective (`playtest-bot-writer`), test a start/stop across a server restart, test late joiners and players who join after the end.
9. Rollback plan: a config flag that disables the event, how to revoke or keep earned rewards, what message goes out, who decides (`rollback-planner`).
10. Measure after: compare the goal metric and guard against the pre-event baseline over the same weekdays; log the result in `decisions.md`.

## Studio MCP path
`list_roblox_studios` -> `script_read` of the existing economy/config -> `multi_edit` to add the event config and counters (Rojo owners edit files) -> `start_stop_play` -> `execute_luau` (Server) to trigger the event through the admin function and assert state -> `get_console_output`.

## Fallback
Design doc + config file + bot script as files; mark runtime behaviour `untested`.

## Evidence
`Roblox/roblox-kb/events-and-seasonal-content.md` (earned rewards; limited-time exclusives for urgency; frame loss honestly; balance casual and grinding; do not secretly boost odds near the end; fixed launch time; admin commands to trigger events; flexible event length), `Roblox/roblox-kb/updates-live-ops.md` (thematic updates; alternate minor and major; mix permanent and limited; server-synced time), `Roblox/roblox-kb/retention-d1-d7.md`, `Roblox/roblox-kb/community-and-discord.md` (tease and announce), `Roblox/roblox-kb/case-studies-grow-a-garden.md` (pattern reading).

## Output
`liveops/event-<name>.md`: goal + guard metric; theme; objective; reward table (tier, requirement, reward, free/paid note); schedule with UTC times; build list with owners and sizes; announcement beats; test checklist; rollback plan; measurement plan.

## Acceptance checks
- [ ] One goal metric and one guard metric with a baseline source.
- [ ] Rewards are earned; free players can complete the main tier; no paid randomness.
- [ ] Times are UTC/server-synced, with start, end and an extension rule.
- [ ] Admin start/stop and a rollback flag exist in the plan.
- [ ] Late joiners, restarts and post-end joins are covered by tests.
- [ ] No hidden odds change; urgency copy is truthful.

## Pitfalls
Events that need a new tutorial. Rewards so strong they break the economy afterwards (`economy-health-monitor`). Local-time countdowns. Leaving event code in client-readable containers (leaks). Launching when the team cannot respond to bugs. Not measuring.

## Related
`update-cadence-planner`, `seasonal-calendar-builder`, `patch-notes-writer`, `rollback-planner`, `economy-health-monitor`, `game-dev-update`.
