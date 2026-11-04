---
name: ab-result-reader
description: "Read an A/B or Creator Hub experiment result honestly: lift with a confidence interval, the sample-ratio check, guardrail metrics against the platform's harm lines, run length, and a rollout, keep-testing or stop verdict. Use when an experiment finishes or you want to double-check a result before shipping the winner."
category: liveops
tags: ab test, experiment results, significance, confidence interval, srm, guardrail, early harm, rollout, lift
kb: Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/updates-live-ops.md
related: experiment-designer, cohort-reader, feature-flag-config-builder, ctr-ab-test-planner, retention-diagnoser, live-balance-tuner, rbx-analytics
---

# ab-result-reader

A result has four parts: how big the lift is, how sure you are, whether the split was valid, and what it cost on other metrics. Creator Hub computes the official numbers; this skill double-checks a copied result, reads a hand-run test, and applies the platform's own gates so a winner is not shipped on a hunch. Designing the test is `experiment-designer`.

## When to use
An experiment reached its end (or you are tempted to stop it early), a thumbnail or UI test has counts, or a stakeholder asks "is this real". Not for: a before/after with no control (`cohort-reader`) or sizing a test (`experiment-designer`).

## Inputs (max 3)
1. Control and treatment: players enrolled and players who hit the goal (a proportion metric: D1, conversion, click-through). 2. Guardrails: relative change and 95 percent interval for playtime, ARPU, payer conversion if Creator Hub shows them. 3. Planned and elapsed days, and the intended split.

## Procedure
1. Check validity before reading lift. Run: `python -I ~/.claude/claude-kit/skillpack/liveops/ab-result-reader/scripts/abread.py --a-n 6000 --a-x 720 --b-n 5900 --b-x 790 --split 50 --duration-days 14 --planned-days 14 --guard "playtime:-4.2:-9.0:+0.6"`. A sample-ratio mismatch (p under 0.001) makes the verdict INVALID: stop and restart the experiment; Creator Hub shows the same flag in the Results tab.
2. Check duration and size: wait for the full planned duration and the daily results (early swings are novelty); at least 10,000 enrolled players for harm decisions; stats are not available before 24 hours. Early-harm alerts are stop signals only, never launch decisions.
3. Read the lift: the script prints control and treatment rates, difference in points and relative, 95 percent CI, z and p (two-proportion normal approximation, a check, not Creator Hub's own computation). WIN needs the whole interval above zero; LOSS the whole interval below.
4. Guardrails: a guardrail is critically harmed if the WHOLE confidence interval is below playtime -10 percent, ARPU -20 percent or payer conversion -20 percent (platform early-harm thresholds, live-check). Any critical harm means STOP regardless of the goal metric. A guardrail that fell with an interval wholly below zero is a real cost to weigh.
5. LEAN POSITIVE (about 80 percent confidence, no negative signals) is an indie heuristic: rolling out may be worth it with a rollback ready, but say it is a judgment, not a win. NO DETECTABLE DIFFERENCE is not proof of no effect; the test may be underpowered.
6. Segment before shipping: new vs returning, platform, payer status. Conditional Configs can ship different values per segment if the result differs.
7. Decide: roll out the winner gradually (config gradual rollout), keep the control for a week to catch a durable-effect gap, complete with no winner (the config reverts), or restart with a bolder variant.
8. Log hypothesis, metric, result, interval and decision in `decisions.md` (a test vault improves prioritisation, vault) and re-measure after rollout (launch lifts can shrink over months, one reported case: +20 percent at launch, 10-12 percent after three months).

## Studio MCP path
Not needed to read results. To ship: `multi_edit` the default of the config key to the winner only after the experiment is completed; the Creator Hub step is the owner's.

## Fallback
Counts typed into the script; for mean metrics (playtime, ARPU) use the interval Creator Hub shows and the guardrail input. The script does not compute mean-metric significance.

## Evidence
`Roblox/roblox-kb/ab-testing-and-experiments.md` (Roblox DevForum and Creator Docs 2026-08 to 2026-10, live-check): early harm detection first 24 hours every 5 minutes, thresholds -10/-20/-20 percent with the whole interval below, 10,000 enrolled minimum, wait for full duration and daily results, SRM means restart, stats after 24 hours, complete without winner reverts. Indie, labelled: about 80 percent confidence heuristic (GameMakers 2022), re-measure after launch (GameMakers 2024).

## Output
```
EXPERIMENT <name> day X of Y
control r1% (n) | treatment r2% (n) | diff +x pts [CI] | p
SRM: ok | INVALID
Guardrails: playtime ..., ARPU ..., conversion ...
VERDICT: WIN | LOSS | LEAN POSITIVE | NO DIFFERENCE | STOP (harm) | INVALID
Decision + rollout/restart plan + re-measure date
```

## Acceptance checks
- [ ] `abread.py --selftest` prints "selftest ok (6 checks)".
- [ ] SRM, duration and enrolment were checked before the lift was read.
- [ ] Guardrails were compared with the platform harm lines on the whole interval.
- [ ] LEAN POSITIVE is labelled as an indie heuristic.
- [ ] The decision names a rollout method and a re-measure date.

## Pitfalls
Stopping at the first significant day. Declaring a winner on the goal metric while ARPU falls. Ignoring SRM. Reading "no difference" as "no effect". Shipping a thumbnail winner without testing the title pair. Testing many variants and picking the best of noise.

## Related
`experiment-designer`, `cohort-reader`, `feature-flag-config-builder`, `ctr-ab-test-planner`, `live-balance-tuner`.
