---
name: cohort-reader
description: "Compare retention of players who first played before and after a change: choose cohorts by first-play date, drop immature ones, test the difference with a confidence interval, and check source and weekday mix before crediting the change. Use after any update, thumbnail or onboarding change."
category: liveops
tags: cohort, retention, before after, first play date, update impact, d1, d7, significance, analytics
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/_tools/BENCHMARKS.md
related: retention-diagnoser, funnel-analyzer, ab-result-reader, experiment-designer, metrics-snapshot-logger, dau-drop-investigator, rbx-analytics
---

# cohort-reader

Retention charts are drawn by first play date, so a change shows up in that day's new cohort, not in the live graph. This skill reads that correctly: group by first-play date around the change, throw away cohorts that have not had time to return, and say how sure the difference is. It is the cheap read when you shipped without an experiment; a real test is `experiment-designer`.

## When to use
After an update, onboarding change, thumbnail swap or ad push, when you want to know if new players behave differently. Not for: a sudden drop in total players (`dau-drop-investigator`), or deciding a tested variant (`ab-result-reader`).

## Inputs (max 3)
1. The change date (UTC) and what changed. 2. Per first-play date: new users, D1 returned, D7 returned (Creator Hub retention or `analytics-pull.py`; blanks allowed). 3. The window: D1 (default) or D7.

## Procedure
1. Put the data in `cohorts.csv` with columns `first_play_date,new_users,d1_returned,d7_returned`. Note the traffic events in the window (ad start or stop, creator video, front-page feature, bot clean-up) from your own log.
2. Run `python -I ~/.claude/claude-kit/skillpack/liveops/cohort-reader/scripts/cohort.py --csv cohorts.csv --change 2026-10-20 --window d1 --as-of <today>`. It skips the change day itself, skips cohorts younger than the window (D7 needs 7 days; recent dates are empty by design), pools before and after, and prints both rates, the gap in points, a 95 percent interval and a two-proportion z test.
3. Stop condition: if it prints CANNOT READ (fewer than 200 users in a group), widen the window or wait; do not read noise.
4. Check what else moved: compare the share of new users by acquisition source, platform and weekday before and after (Creator Hub breakdowns). A retention change that is only a traffic-mix change is not the update's effect (vault: a retention drop may only reflect a traffic source shift).
5. Use a same-weekday comparison when you have the history, and read the post-spike baseline about a week later, not the first days (novelty and spikes fade; vault).
6. Write the verdict in one of three forms: lifted (interval above zero and the mix is stable), no detectable change, or worse. State what could still explain it.
7. If the stake is high or the mix shifted, move to a Creator Hub experiment for the next change (`experiment-designer`) and log this read in `decisions.md` with the numbers.

## Studio MCP path
Not needed (analysis only). If the change was an instrumentation fix, `script_grep` the Analytics calls to confirm the new cohort is counted the same way as the old one.

## Fallback
Paste the numbers and run the script; everything is Python 3. Without Creator Hub access, count returners from your own session log.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: read retention as first-play-date cohorts; D7 and D30 are empty for recent dates; slice by acquisition source; judge a change by the baseline a week later; treat every update as a hypothesis and verify afterwards; do not sum daily uniques into weekly totals. `retention-d1-d7.md` and `_tools/BENCHMARKS.md` for what D1 and D7 usually look like (indie flags apply).

## Output
```
COHORT READ <change> <date>  window D1
before n=... rate ...%   after n=... rate ...%   diff +x.x pts  95% CI [a, b]  p=...
Mix check: source/platform/weekday shares before vs after
Verdict: lifted | no detectable change | worse   Confounders: ...
Next: experiment or keep, re-read on <date>
```

## Acceptance checks
- [ ] `cohort.py --selftest` prints "selftest ok (4 checks)".
- [ ] Immature cohorts and the change day were skipped; the count of skipped cohorts is stated.
- [ ] Both groups have at least 200 users, or the read says CANNOT READ.
- [ ] Source, platform and weekday mix were compared before crediting the change.
- [ ] The verdict says correlation, with the confounders named.

## Pitfalls
Reading D7 for last week's cohort. Crediting an update for a thumbnail or ad change that landed the same day. Pooling cohorts with very different traffic. Treating p below 0.05 as proof of cause. Comparing a weekend cohort to a weekday one.

## Related
`retention-diagnoser`, `ab-result-reader`, `experiment-designer`, `metrics-snapshot-logger`, `dau-drop-investigator`.
