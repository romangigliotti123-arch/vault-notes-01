---
name: ctr-ab-test-planner
description: "Plan a test of the game's thumbnail, icon or title: one variable per variant, which Roblox mechanism to use (thumbnail personalization, ad-driven splits, sequential changes), how long to hold, what the metric is and the decision rule for the winner. Use after thumbnail-maker produces variants or when click-through or play-through is the problem."
category: marketing
tags: ab test, ctr, thumbnail test, icon test, title test, split test, experiment, play through, decision rule, impressions
kb: Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/titles-descriptions.md
related: thumbnail-maker, game-icon-maker, game-description-writer, experiment-designer, discovery-signal-reader, ab-result-reader, sponsored-ad-reviewer
---

# ctr-ab-test-planner

A test that cannot be read is worse than no test. This skill fixes the design before any image goes live: one variable, one metric, one hold time, one decision rule. In-game feature tests use `experiment-designer` (Creator Hub experiments); this is for packaging.

## When to use
You have two or more thumbnail/icon/title candidates, or CTR/PTR is low. Not for: in-game tuning, ad budget planning (`rbx-ad-plan`).

## Inputs (max 3)
1. The candidates (default: `art/thumbnail-plan.md`). 2. Traffic: impressions and visits per day (Creator Hub analytics; default: unknown = plan for low traffic). 3. Which mechanism is available (default: check live).

## Procedure
1. Live-check the current testing mechanisms in Creator Docs and Creator Hub (names change): thumbnail personalization with several active thumbnails (vault: 2-5 active; the system retunes hourly, starts optimising within hours, finds winners in about 48 hours); any official thumbnail/icon test tool; ad-driven comparisons. Write what exists today with source and date.
2. Define the hypothesis: "Thumbnail B (close-up hero, warm background) will raise CTR over A because the subject reads bigger on phones." One variable only (subject size, background colour, emotion, text/no text, title wording).
3. Choose the mechanism:
   - Personalization (preferred when available): upload 3-5 variants that differ by one variable family; let the system route; read per-thumbnail results after about 48 hours and again after a week; retire the worst, keep 3.
   - Sequential: run A for a week, then B for a week at similar traffic (no update, no event, same weekday mix). Weak, because traffic changes; use only with high volume.
   - Ads: show the same placements with different creatives (paid, so the owner decides the budget; this skill never spends).
4. Metric: CTR from impressions (thumbnail), then play-through/conversion to the first minute (to catch clickbait); guard metrics: D1 retention and bounce must not fall (a higher CTR with worse retention is a loss). Minimum sample: decide before starting (e.g. several hundred clicks per variant; state the number you choose and why).
5. Decision rule written in advance: "Keep B if CTR is at least X relative better at the end of the hold AND D1/bounce not worse by more than Y; otherwise keep A and try the next variable." Pick X and Y from your baseline noise, not from folklore.
6. Calendar: avoid launching during events or updates; refresh packaging at major updates (vault).
7. Log every test in `decisions.md`: date, variants, mechanism, metric values, decision. Read results with `ab-result-reader`.
8. Output the plan.

## Studio MCP path
Not needed. Optional: `execute_luau` (Edit) to capture variant screenshots in the place for `thumbnail-maker`.

## Fallback
Pure planning. If no analytics access, list the numbers the owner must copy from Creator Hub and the cells to fill.

## Evidence
`Roblox/roblox-kb/thumbnails-icons.md` (packaging gates discovery; personalization with 2-5 thumbnails; check at mobile size), `Roblox/roblox-kb/ab-testing-and-experiments.md` (one hypothesis and matching goal metric; experiment mechanics for in-game tests, limits are in the KB), `Roblox/roblox-kb/discovery-algorithm.md`, `Roblox/roblox-kb/analytics-metrics.md`, `Roblox/roblox-kb/titles-descriptions.md` (test names before committing). Mechanism availability is a fast-moving fact: live-check.

## Output
`marketing/ctr-test-<date>.md`: hypothesis; variants (id, the one difference, file); mechanism + source/date; metric and guard metrics; sample and hold time; decision rule; calendar notes; result table to fill in.

## Acceptance checks
- [ ] Exactly one variable differs between any two variants.
- [ ] Metric, guard metric, sample size and hold time were fixed before launch.
- [ ] The decision rule is written with numbers, not adjectives.
- [ ] Mechanism availability has a source/date from this run.
- [ ] No spending or uploading was done by the skill.
- [ ] Under about 500-1,000 DAU the plan uses qualitative feedback, not an experiment (above it: minimum detectable effect checked first); results flagged NotStatisticallySignificant or Projected are not acted on; a risky change runs as a 50/50 split against control for about one week (mixed/official; Roblox/roblox-kb/_tools/DECISION-RULES.md, analytics-metrics, playtesting-and-feedback).

## Pitfalls
Testing during an update or event. Calling a winner after a day of data. Clickbait winners with worse retention. Changing the title and thumbnail together. Running many variants on tiny traffic (nothing reaches significance; test bigger differences).

## Related
`thumbnail-maker`, `game-icon-maker`, `game-description-writer`, `experiment-designer`, `ab-result-reader`, `rbx-thumbnail` (thumbnail personalization protocol and the results ledger `thumb_record.py`).
