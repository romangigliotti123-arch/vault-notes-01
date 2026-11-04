---
name: experiment-designer
description: "Design a Creator Hub experiment before starting it: one hypothesis, one goal metric, 1 baseline plus up to 2 treatments, exposure, a 14-60 day duration sized by a sample-size script, guardrail metrics, and the stop and rollout rules. Use before changing onboarding, prices, difficulty or UI on a live game."
category: liveops
tags: experiment, a/b test, hypothesis, configs, creator hub experiments, sample size, mde, guardrail, exposure
kb: Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/first-session-onboarding.md
related: ab-result-reader, feature-flag-config-builder, cohort-reader, retention-diagnoser, ctr-ab-test-planner, live-balance-tuner, rbx-analytics
---

# experiment-designer

A test only helps if the metric, the size and the stop rule were fixed before it started. Creator Hub Experiments plus Configs let you serve two or three values of one config key to a slice of players and read a goal metric. This skill writes that plan. Thumbnail and title tests are `ctr-ab-test-planner`; reading the result is `ab-result-reader`.

## When to use
A change to a live value (boss health, price, reward, onboarding hint, UI) where you can name the metric it should move. Not for: a change you will ship regardless, a game too small to test (see step 3), or a thumbnail test.

## Inputs (max 3)
1. The change and the hypothesis in one sentence ("if the first boss has 30 percent less health, D1 rises"). 2. Goal metric (proportion metrics size best: D1, payer conversion) and its current value. 3. New players per day (default: read from Creator Hub).

## Procedure
1. Write the hypothesis as "if I change X, metric Y moves by at least Z percent" and the guardrails (playtime, ARPU, payer conversion are the three the platform watches for early harm). One variable per test (indie rule, labelled); make the variant bold enough to move the metric (indie: tiny 5 percent tweaks rarely do; 50-100 percent value changes or key-screen changes).
2. Put the value behind a config key with a safe default (`feature-flag-config-builder`) so the control is the current behaviour and a failure falls back to it.
3. Size it: `python -I ~/.claude/claude-kit/skillpack/liveops/experiment-designer/scripts/experiment.py --metric d1 --baseline 12 --mde-rel 25 --daily-new 400 --exposure 50 --treatments 1`. It prints players needed per arm, days needed with your traffic, expected enrolment, and ERROR/NOTE lines against the platform limits. Stop condition: if it says underpowered, make the change bolder, raise exposure or accept a weaker read; for a very small game use before-after cohorts (`cohort-reader`) instead.
4. Set the structure: 1 baseline and at most 2 treatments; exposure percent (a risky variant gets a small slice and you watch ratings and retention); a duration between 14 and 60 days; configuration is immutable once started or scheduled, so finish it in draft.
5. Write the stop rules: early-harm detection checks playtime, ARPU and payer conversion every 5 minutes for the first 24 hours and flags critical harm only if the whole confidence interval is below the limit (playtime -10 percent, ARPU -20, conversion -20); it is a stop signal, never a launch decision. Harm decisions need at least 10,000 enrolled players. A sample-ratio-mismatch alert means stop and restart.
6. Write the decision rule up front: winner needs the full duration, daily results settled, SRM clear, guardrails not harmed. Stats are available after 24 hours. Completing without a variant id stops with no winner and the config reverts.
7. Ramp: roll the winner out gradually (publish with a gradual rollout rather than immediately, 15 minutes in the docs). Record hypothesis, metric, result and confidence in `decisions.md` (a test vault improves later prioritisation, vault).
8. Matchmaking experiments are a special case: one per universe, run at 100 percent traffic. Treat as a separate plan.

## Studio MCP path
Experiments and Configs are created in Creator Hub (or the Experiments API with a key); there is no Studio tool for them. Studio side: `script_grep` for the config reads, `multi_edit` to read the key with a default, `start_stop_play` + `execute_luau` (Server) to check both variants run.

## Fallback
Write the plan as a Markdown spec and have the owner create the experiment in Creator Hub. API field names are not written here; live-check the Experiments API page. All numbers below stay `untested` until the experiment runs.

## Evidence
`Roblox/roblox-kb/ab-testing-and-experiments.md` (Roblox Creator Docs and DevForum 2026-08 to 2026-10, live-check): duration 14-60 days; 1 baseline plus up to 2 treatments; exactly one baseline; config immutable once started; early harm thresholds and 10,000-player minimum; SRM restart; stats after 24 hours; complete without winner reverts; gradual rollout 15 minutes; config deploys about 5 minutes. Indie (GameMakers, labelled): bold variants, small slices for risky tests, test vault, one variable at a time.

## Output
`liveops/experiment-<name>.md`: hypothesis, metric and baseline, variants, exposure, duration, sizing line from `experiment.py`, guardrails, stop rules, decision rule, rollout plan, owner.

## Acceptance checks
- [ ] `experiment.py --selftest` prints "selftest ok (6 checks)" and the real run shows no ERROR.
- [ ] One hypothesis, one goal metric, at most 2 treatments, duration 14-60 days.
- [ ] Enrolment is expected to reach 10,000, or the plan says harm decisions will not be made.
- [ ] Stop rules and the decision rule were written before launch.
- [ ] The control is the current live behaviour and the config has a safe default.

## Pitfalls
Testing five things at once. Peeking at day 3 and shipping. Reading the first 24 hours as a result. Changing configuration after start. Judging a thumbnail-pair test by the thumbnail alone. Running a test on a game with 50 new players a day.

## Related
`ab-result-reader`, `feature-flag-config-builder`, `cohort-reader`, `ctr-ab-test-planner`, `live-balance-tuner`.
