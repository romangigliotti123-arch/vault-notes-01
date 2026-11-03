---
name: funnel-analyzer
description: "Define, instrument and read an onboarding or purchase funnel: choose 5-10 steps, log them server-side with the kit Analytics system, then compute conversion per step and name the biggest drop to fix first. Use when players leave early or buy rarely and you do not know where."
category: liveops
tags: funnel, onboarding, first session, drop-off, purchase funnel, analytics, conversion, steps, tutorial
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/_tools/BENCHMARKS.md
related: retention-diagnoser, first-minute-designer, churn-reason-finder, cohort-reader, shop-conversion-optimizer, roblox-analytics-review, game-dev-weekly
---

# funnel-analyzer

Retention says someone leaves; a funnel says where. Two funnels cover most games: first session (spawn to first reward to first upgrade) and first purchase (see shop, open, select, buy, equip). `retention-diagnoser` picks the broken window; this finds the step inside it.

## When to use
Low D1 or first-session completion, or low purchase conversion, and no named stall. Not for: a sudden player-count drop (`dau-drop-investigator`) or why mid-game players leave (`churn-reason-finder`).

## Inputs (max 3)
1. Which funnel: onboarding or purchase (default: onboarding). 2. Step names in order, or the game's first five minutes in plain words (default: propose steps). 3. Counts per step from Creator Hub, if they exist already.

## Procedure
1. List 5-10 steps that each happen once and need a player action (vault: log after the step completes, track micro-steps inside tutorials). Name each with a short fixed string; funnel steps are integers 1-100 in the kit Analytics system and at most 10 funnels.
2. Instrument from the SERVER at the moment progress happens (vault: for example just before a teleport loads): kit `Analytics:Onboarding(player, step, name)` or `:Funnel(...)`. Never from the client (fakeable), never per frame. Add a test: run the path in Studio and confirm each call returned true.
3. Wait for data (events take up to a day to show; funnel steps only appear on days a user reached them, so use a 90-day lookback to discover rarely-reached steps).
4. Pull counts (Creator Hub funnels, or `python -I ~/.claude/claude-kit/tools/analytics-pull.py --universe <id> --metric <FunnelMetric> --dry-run` to see the query; the metric spelling is on the Supported-metrics page) and run `python -I ~/.claude/claude-kit/skillpack/liveops/funnel-analyzer/scripts/funnel.py --steps "Spawn:1000,Moved:860,..."`.
5. Read the table: the biggest ABSOLUTE loss is the first fix (vault: fix the biggest red drop first); a step with MORE players than the one before means the steps are out of order or counted per event. Steps losing 30 percent or more at once are flagged (this skill's default).
6. Segment the worst step by platform, device and new vs returning before changing anything (a console-only tutorial bug hid inside 77 percent overall completion, self-reported in the vault).
7. Pick one change and a re-measure date; hand off to `first-minute-designer` (onboarding), `shop-conversion-optimizer` (purchase) or `experiment-designer` (to test it).

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `AnalyticsService` / `Onboarding(` calls to see what already logs -> `multi_edit` to add step calls -> `start_stop_play` -> `execute_luau` (Server) to walk the path and `get_console_output` for rejections.

## Fallback
Without Studio: write the step list and the exact call sites as a patch for the owner; counts can be pasted in by hand. Instrumentation stays `untested` until run in Play.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: use funnels for onboarding and feature flows; log funnel steps server-side at real progress points; fix the biggest red drop first; discover steps with a 90-day lookback; instrument server-only and after success; slice before trusting aggregates. `first-session-onboarding.md` and `retention-d1-d7.md` for what the first minutes must do. Kit `systems/Analytics/README.md` for caps.

## Output
`liveops/funnel-<name>.md`: step list with call sites, the conversion table from `funnel.py`, the worst step with its segment check, the one change and the re-measure date.

## Acceptance checks
- [ ] `funnel.py --selftest` prints "selftest ok (4 checks)".
- [ ] All steps are logged from the server after success; none is per-frame or carries a user id or free text.
- [ ] No step shows more players than the one before it (or the reason is stated).
- [ ] The chosen fix targets the biggest absolute loss, after a segment check.
- [ ] Sample size at step 1 is stated (under 100 is flagged noisy).

## Pitfalls
Too many steps. Logging before the action succeeds. Reading a funnel before the first day of data. Comparing funnels across different traffic sources. Treating a 30 percent drop at a step that is meant to filter (a hard boss) as a bug.

## Related
`retention-diagnoser`, `first-minute-designer`, `churn-reason-finder`, `cohort-reader`, `shop-conversion-optimizer`.
