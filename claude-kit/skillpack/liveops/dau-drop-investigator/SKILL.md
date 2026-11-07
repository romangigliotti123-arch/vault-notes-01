---
name: dau-drop-investigator
description: "Investigate a sudden drop in players: measure it against the same weekday last week, classify it as a step, slide or one-off, then walk the ordered checks (publish timing, platform-wide, traffic, segments, health, retention) to one cause and one action. Use the day numbers fall and you do not know why."
category: liveops
tags: dau drop, player drop, ccu drop, investigation, step change, regression, traffic, segments, rollback, analytics
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: hotfix-playbook, rollback-planner, retention-diagnoser, cohort-reader, metrics-snapshot-logger, churn-reason-finder, funnel-analyzer, rbx-analytics
---

# dau-drop-investigator

Vault: do not trust aggregates; slice by platform, device, source, version, country and age until you find the smallest affected segment. A drop exactly at a publish points at that update; a drop on low-memory Android points at resources, not design; a drop during a bot clean-up is an accuracy correction. This skill makes that order explicit. Slow decline in retention is `retention-diagnoser`; this is for the sudden fall.

## When to use
Daily players or concurrents fell sharply or are sliding week over week. Not for: explaining a metric you have not measured (log it first, `metrics-snapshot-logger`), or a normal post-event fade (`ccu-forecaster`).

## Inputs (max 2)
1. Daily players (DAU or peak CCU) for at least 15 days as CSV (`date,dau`) or an `analytics-pull.py --json` file. 2. What shipped, started or ended in the last two weeks (updates, config pushes, ad campaigns, events, thumbnail changes).

## Procedure
1. Measure first: `python -I .rbx/claude-kit/skillpack/liveops/dau-drop-investigator/scripts/dau_drop.py --csv dau.csv --date 2026-11-02` (or `--pull pull.json --metric DailyActiveUsers`). It compares the day to the same weekday last week (this removes the weekly cycle), shows the change of the 7-day average, and classifies: STEP (fell at once and stayed down), ONE-OFF (recovered within two days), SLIDE (gradual, no single bad day) or NO CLEAR DROP. Thresholds are this skill's defaults. Stop condition: if it says NO CLEAR DROP, the feeling may be seasonality or a spike last week; report that.
2. Check dates against the changelog: did a publish, config change, event end or ad stop land on or just before the first bad day? A STEP at a publish is a strong lead; consider rollback first if harm is severe (`hotfix-playbook`), then profile.
3. Platform-wide causes: Roblox status, bot-removal or accuracy corrections, other games in your genre moving the same way, seasonal shifts (school terms, holidays). Check 28-day period-over-period and 7-day averages before blaming the game.
4. Traffic: Acquisition by source and Home Recommendations (play-through rate first). Did an ad campaign end, did a creator video age out, was a thumbnail changed? A drop in new players with stable returning players is a discovery problem (`ctr-ab-test-planner`, `thumbnail-maker`), not a game problem.
5. Slice: platform, device tier, country, age, new vs returning, version. Stop at the smallest affected segment and state it.
6. Health: crash rate, error counts grouped by message hash, join failures, DataStore errors for the same hours; Performance by place version.
7. Retention: did D1 of new cohorts fall (onboarding, `funnel-analyzer`) or did returning players stop coming (content or economy, `churn-reason-finder`)? Use `cohort-reader` for the before/after.
8. Decide: one cause, one action, one re-check date. Roll back if a publish is the clear cause; otherwise one hypothesis and one test (`experiment-designer`). Write the finding in `decisions.md`.

## Studio MCP path
`get_console_output` after a Play test of the new build; `script_grep` for the area touched by the suspect publish. The investigation itself is data work in Creator Hub.

## Fallback
Python 3 and a CSV; the check list is plain text. Without segment data say so and limit the finding to the pattern.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: slice data to find the cause of a change (a drop exactly at publish points to that update; low-memory Android points to resources); compare with the same weekday last week; account for seasonality with 28-day overlays and 7-day averages; break retention by acquisition source; read bot-removal drops as accuracy correction; group errors by message hash; check Performance by place version after each publish. `updates-live-ops.md`: roll back severe regressions then profile; monitor the first minutes after publishing. `discovery-algorithm.md` for the recommendation signals.

## Output
```
DAU DROP <date>: <value> vs same weekday last week <+/-%>; 7-day average <+/-%>
Pattern: STEP | SLIDE | ONE-OFF | none
Checks 1-7: finding or "clear"
Cause (confidence), action, re-check date
```

## Acceptance checks
- [ ] `dau_drop.py --selftest` prints "selftest ok (5 checks)".
- [ ] The drop was measured against the same weekday, and the pattern named.
- [ ] Each of the seven checks has a finding or "clear".
- [ ] The affected segment is the smallest found, or "none found" is stated.
- [ ] One action and a re-check date; a rollback decision if a publish is implicated.

## Pitfalls
Reading a weekend-to-weekday gap as a drop. Blaming the last update because it was last. Ignoring a traffic-source change. Changing three things at once and losing the cause. Declaring a platform correction a retention problem.

## Related
`hotfix-playbook`, `rollback-planner`, `retention-diagnoser`, `cohort-reader`, `metrics-snapshot-logger`.
