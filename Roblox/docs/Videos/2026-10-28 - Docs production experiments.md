---
title: "Docs: production / experiments"
url: https://create.roblox.com/docs/production/experiments.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / experiments

[Open](https://create.roblox.com/docs/production/experiments.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Hub docs for Experiments: how to set up in-game (config A/B) and matchmaking experiments, targeting, enrollment code, metrics, early-harm and SRM checks, reading daily results, and deciding winners.

## Tips
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Compute minimum detectable effect (MDE) before running; if MDE exceeds ~100% for your goal metric, significance is unlikely. Games under 1,000 DAU may struggle to get useful data.
- [page](https://create.roblox.com/docs/production/experiments) **[[playtesting-and-feedback]]** Use a simple 50/50 split of one variant vs control on large rollouts; it is easier to configure and interpret than multi-variant splits.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Let experiments run their full 14-60 day duration; ending early risks acting on novelty-effect spikes.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Only act on statistically significant results, i.e. where the confidence interval for percent change does not overlap 0%. Ignore non-significant changes.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Write a cause-and-effect hypothesis (change, expected effect, reason) before each experiment and keep them with results.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Stop and restart an experiment if a Sample Ratio Mismatch banner appears; SRM can invalidate results.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Do not use first-24-hour early-harm metrics for launch decisions; use them only to guide early stopping.
- [page](https://create.roblox.com/docs/production/experiments) **[[common-mistakes]]** Do not call GetConfigAsync for experiment players; use GetConfigForPlayerAsync per player, otherwise experiments don't apply.
- [page](https://create.roblox.com/docs/production/experiments) **[[common-mistakes]]** Delay calling GetValue until the player reaches the feature being tested, otherwise you enroll players who never see it.
- [page](https://create.roblox.com/docs/production/experiments) **[[common-mistakes]]** Avoid content changes during an experiment, even unrelated-seeming ones, as they can invalidate results. Don't run overlapping experiments unless confident they don't interact.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** Use confidence intervals for deep dives and borderline significance; very wide intervals may never reach significance.
- [page](https://create.roblox.com/docs/production/experiments) **[[retention-d1-d7]]** For multi-session experiences targeted at new players, persist the variant yourself (e.g. data store), since targeting is re-evaluated per session.
- [page](https://create.roblox.com/docs/production/experiments) **[[pricing]]** Use shop visibility, starter pack type and pricing as monetisation experiment candidates, measured by ARPU, ARPPU and payer conversion rate.
- [page](https://create.roblox.com/docs/production/experiments) **[[core-loops-and-game-design]]** Test onboarding flows, progression systems, control schemes and custom matchmaking as engagement experiments measured by playtime and D1/D7 retention.
- [page](https://create.roblox.com/docs/production/experiments) **[[common-mistakes]]** Don't rely on the Details tab early for decisions; it's only for checking the experiment runs properly.
- [page](https://create.roblox.com/docs/production/experiments) **[[analytics-metrics]]** For matchmaking experiments, use 100% rollout; it minimizes risk of isolating players and gives faster, more reliable results.

## Numbers
- [page](https://create.roblox.com/docs/production/experiments) Experiment duration: **14-60 days** (Allowed planned duration for both in-game and matchmaking experiments)
- [page](https://create.roblox.com/docs/production/experiments) Early harm threshold Playtime: **-10%** (Lift below this classed as critically harmful during early harm window)
- [page](https://create.roblox.com/docs/production/experiments) Early harm threshold ARPU: **-20%** (Critical harm threshold in first 24 hours)
- [page](https://create.roblox.com/docs/production/experiments) Early harm threshold payer conversion: **-20%** (Critical harm threshold in first 24 hours)
- [page](https://create.roblox.com/docs/production/experiments) Harm decision sample minimum: **10,000 players** (Below this across variant and control, harm decisions are not made)
- [page](https://create.roblox.com/docs/production/experiments) Variants allowed: **2 variants + control (in-game); up to 3 variants (matchmaking)** (Maximum variants per experiment type)
- [page](https://create.roblox.com/docs/production/experiments) Daily active users for useful data: **1,000 DAU** (Games below this might struggle to get useful experiment data)
- [page](https://create.roblox.com/docs/production/experiments) Early metric update frequency: **every 5 min for first 24h, then every 24h** (Playtime, payer conversion and ARPU update in 5-minute intervals initially)
- [page](https://create.roblox.com/docs/production/experiments) Statistical significance rule: **CI for % change does not overlap 0%** (Dashboard highlights significant changes green or red)

## Tools
Roblox Creator Hub Experiments page, ConfigService (GetConfigForPlayerAsync, ConfigSnapshot:GetValue), Custom matchmaking configuration, Data stores (for persisting variants)

## He points to
- Target experiments to specific audiences (Creator Hub doc)

## Quotes
- [page](https://create.roblox.com/docs/production/experiments) "Let experiments run for their full durations. The novelty effect can heavily skew early results, sometimes causing them to swing in and out of statistical significance."
- [page](https://create.roblox.com/docs/production/experiments) "If a change isn't statistically significant, ignore it."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[core-loops-and-game-design]] [[playtesting-and-feedback]] [[pricing]] [[retention-d1-d7]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
