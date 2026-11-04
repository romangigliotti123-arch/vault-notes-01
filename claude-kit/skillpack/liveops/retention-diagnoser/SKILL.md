---
name: retention-diagnoser
description: "Diagnose weak retention or play-through from a game's headline numbers (D1, D7, PTR, session length, conversion): compare with the vault's sourced benchmarks with their flags, name the most likely cause by window, and hand back an ordered list of single changes to test. Use when numbers are low or flat and you do not know what to fix first."
category: liveops
tags: retention, d1, d7, churn, diagnose, analytics, metrics, benchmark, play through, session, funnel
kb: Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/_tools/BENCHMARKS.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/updates-live-ops.md
related: first-minute-designer, funnel-analyzer, cohort-reader, churn-reason-finder, experiment-designer, rbx-analytics, rbx-metrics, rbx-weekly
---

# retention-diagnoser

Metrics say WHERE; this skill says which window is broken and what to test first. Kit skills `rbx-analytics` and `rbx-metrics` read dashboards broadly; this one is the narrow diagnosis with an ordered fix list. The weekly routine is `rbx-weekly`.

## When to use
Low or falling D1/D7/PTR/session length and no clear cause. Not for: a sudden player-count drop (`dau-drop-investigator`) or monetisation (`shop-conversion-optimizer`).

## Inputs (max 3, numbers from Creator Hub, same date range)
1. D1 and D7 retention (percent). 2. Play-through rate / click-through, average session minutes, payer conversion if known. 3. Genre and age of the game (default: unknown; mark benchmarks "indie, any genre").

## Procedure
1. Collect the numbers and the date range; say if the sample is small. If the owner has Creator Hub "similar experiences" benchmarks, those override the vault's rules of thumb.
2. Run the comparison: `python -I ~/.claude/claude-kit/skillpack/liveops/retention-diagnoser/scripts/diagnose.py --d1 <pct> --d7 <pct> --ptr <pct> --conv <pct> --session-min <m>` (add `--first-session-drop <pct>` if known). It prints each metric with its status (LOW / ok / strong) and its source label and flag, then the ordered fix list.
3. Interpret by window (vault analytics rule: low D1 = onboarding; D7 gap = missing hooks):
   - First session/D1 low: onboarding stall, unclear goal, mobile control friction, bugs. Test: `first-minute-designer` timed run, first-session funnel (`funnel-analyzer`), crash/error check.
   - D1 fine, D7 low: nothing pulls them back across days. Test: one return hook (streak or daily reward, timed events, friend loop, unfinished goal), then `event-planner`.
   - PTR low (impressions fine): packaging mismatch. Test: `thumbnail-maker`, `ctr-ab-test-planner`.
   - Session short with ok D1: pacing and stop points. Test: add a goal 2-3 minutes out at each stop point.
   - Conversion low: offers. Test: `shop-conversion-optimizer`.
4. Confirm the diagnosis with a second signal before acting: segment by new vs returning, device (mobile vs PC), country if available, and by version/date of the last update (did it start then? `cohort-reader`).
5. Choose ONE change (highest-impact, cheapest); define the metric, the hold time and the guard metric; use a Creator Hub experiment where it applies (`experiment-designer`, 14-60 day limits are in the KB).
6. Write the diagnosis note and add it to `Games/<slug>/weekly/` or `decisions.md`. Re-measure after the hold time.

## Studio MCP path
Not needed for the diagnosis. If the plan includes an instrumentation fix (events missing): `script_grep` for analytics calls; kit system `Analytics` provides event tracking.

## Fallback
Pure numbers and the script; no tools needed beyond Python 3.

## Evidence
`Roblox/roblox-kb/retention-d1-d7.md` (retention before acquisition and monetisation; first 5 minutes; fix onboarding by finding the drop-off; end onboarding with joy and a reason to return; friends as the top predictor; daily rewards and streaks as D1 hooks), `Roblox/roblox-kb/analytics-metrics.md` (retention by window; first-session data), `Roblox/roblox-kb/_tools/BENCHMARKS.md` (rows carry flags: D1 12-15 percent "very good" and D7 2-3 percent are indie 2026-08 targets; the 2023 same-genre D1 percentile range 12.4-24.1 percent is a DevForum figure; the 1.63 percent payer conversion sample is official 2024-09), `Roblox/roblox-kb/first-session-onboarding.md`.

## Output
```
RETENTION DIAGNOSIS <game> <range>
metric | value | status | benchmark source+flag
Most likely cause: <window -> cause>   Confirmed by: <second signal or "unconfirmed">
Change 1 (test now): ... metric ... hold ... guard ...
Then: change 2, change 3 (only after 1 reads)
Caveats: sample size, genre mismatch, benchmark flags
```

## Acceptance checks
- [ ] Every number has its range/date and benchmark rows show their flags.
- [ ] Exactly one change is recommended to test first, with metric, hold time and guard metric.
- [ ] The diagnosis names the window (first session, D1, D7) and a confirming signal or says unconfirmed.
- [ ] `diagnose.py --selftest` prints "selftest ok" (script sanity).
- [ ] Creator Hub similar-experience benchmarks used when supplied.
- [ ] With D1 under about 10 percent the first 5 minutes, the tutorial funnel and performance are audited BEFORE any reward or feature is added (mixed; Roblox/roblox-kb/_tools/DECISION-RULES.md, retention-d1-d7); lower-is-better metrics (FPS, memory, session time) are read at P10 and P90, never averages alone (official, analytics-metrics).

## Pitfalls
Treating indie rules of thumb as laws (genre and age shift them a lot). Changing five things at once after a bad week. Reading D7 before enough users reached day 7. Optimising retention while the real problem is packaging (PTR). Ignoring mobile-vs-PC splits.

## Related
`first-minute-designer`, `funnel-analyzer`, `cohort-reader`, `churn-reason-finder`, `experiment-designer`, `rbx-analytics`.
