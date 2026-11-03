---
name: feature-prioritizer
description: "Rank candidate features by loop impact, cost and risk with an explicit score table and a budget cut line (featureprio.py), and explain the ranking in one line each. Use when choosing the next update's content or ordering a backlog; scope-cutter calls it for the cut."
category: design
tags: prioritise, backlog, ranking, features, roadmap, score, impact, effort, update planning
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/_tools/DECISION-RULES.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/analytics-metrics.md
related: scope-cutter, mvp-definer, core-loop-designer, update-cadence-planner, retention-diagnoser, sequel-planner
---

# feature-prioritizer

Vault: every new system must feed the core loop or be cut; fix unpopular features within a week; verify that a new feature actually changes behaviour (a sprint button cut D1 in one official example). This skill makes the order explicit and checks it against data when data exists.

## When to use
Choosing among several features that could all be good, or planning the next update. Not for: trimming an oversized plan to a budget with reasons (`scope-cutter` uses this script and adds the deferred list), or cadence planning (`update-cadence-planner`).

## Inputs (max 2)
1. Candidate features, one line each (default: GDD systems plus the backlog). 2. Budget in days (default: 14) and the metric you want to move (default: D1 or session length).

## Procedure
1. For each feature record `loop_layer` (1 minute-to-minute, 2 session, 3 progression, 0 none), `impact` 0-5 on the chosen metric, `cost_days` including testing, `risk` 1-5 (technical, balance, moderation, exploit). Impact is a hypothesis: write the evidence line (a vault rule, a retention symptom, a player quote) or mark it `judgment`.
2. Save `features.csv` and run `python feature-prioritizer/scripts/featureprio.py features.csv --budget-days 14`. Score = impact x layer weight / (cost x risk factor). The weights favour minute-to-minute work (1.5), then session (1.2), then progression (1.0). They are this skill's defaults.
3. Sanity-check the top three against live data if any: retention funnel step, drop-off, feedback counts (`retention-diagnoser`, `feedback-synthesizer`). Move a feature up only when data names the problem it fixes.
4. Resolve ties with: smaller first, reversible first, the one that makes later features cheaper first.
5. Write one line per feature: "Rank N because <loop layer + impact evidence>, costs D days, risk R (<why>)". Anything with layer 0 is CUT.
6. Pair each KEEP with its success metric and a revert rule ("revert if D1 drops by more than X over 3 days" with X set from your baseline).
7. Save `design/priorities.md` with the table.

## Studio MCP path
Design only.

## Fallback
Run the Python script on a hand-written CSV, or score by hand with the same formula.

## Evidence
`core-loops-and-game-design` (tie every system to the loop; avoid tumors; prioritise long-engagement systems over cosmetics, a single-mention view), `development-process-and-speed` (MVP first; cut under deadline), `updates-live-ops` (cadence releases stay inside existing systems; major updates add systems), `_tools/DECISION-RULES.md`, `analytics-metrics`.

## Output
`design/priorities.md`: the table from the script (rank, layer, days, score, KEEP/DEFER/CUT), the one-line reasons, success metric and revert rule per KEEP.

## Acceptance checks
- [ ] Executed: `python feature-prioritizer/scripts/featureprio.py --selftest` prints `selftest ok (4 checks)`.
- [ ] Project run ends with the `budget used` line and no KEEP exceeds the budget.
- [ ] Every impact has an evidence line or `judgment`.
- [ ] Every KEEP has a metric and a revert rule.

## Pitfalls
Scoring everything 5. Treating the formula as truth instead of a conversation starter. Ignoring risk until the exploit ships. Adding a feature because a competitor has it.

## Related
`scope-cutter`, `mvp-definer`, `update-cadence-planner`, `retention-diagnoser`, `sequel-planner`.
