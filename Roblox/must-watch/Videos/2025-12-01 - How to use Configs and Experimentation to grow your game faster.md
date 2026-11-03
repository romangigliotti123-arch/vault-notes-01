---
title: "How to use Configs and Experimentation to grow your game faster"
url: https://youtu.be/-CdXP025MvU
creator: Roblox Creators
official: true
advice_density: high
date: 2025-12-01
views: 4674
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# How to use Configs and Experimentation to grow your game faster

[Watch](https://youtu.be/-CdXP025MvU) | MustWatch | 4,674 views | 2025-12-01

## Summary
Roblox official talk on Configs (real-time server-to-client value changes without redeploy) and Experiments (in-game A/B tests measuring KPIs). Live shop demo wiring config values to UI via player attributes, then reading experiment results (confidence intervals, static vs non-static metrics, MDE, run length) and best practices.

## Tips
- [1:04](https://youtu.be/-CdXP025MvU?t=64) **[[development-process-and-speed]]** Wrap game values (shop text, colors, features, event toggles) in configs so you can change them live without redeploying servers.
- [13:51](https://youtu.be/-CdXP025MvU?t=831) **[[playtesting-and-feedback]]** Test staged configs in Studio first (dogfood) before publishing to production.
- [13:51](https://youtu.be/-CdXP025MvU?t=831) **[[common-mistakes]]** Config snapshots are static by default; listen for update events and reload them manually or changes won't apply.
- [13:51](https://youtu.be/-CdXP025MvU?t=831) **[[development-process-and-speed]]** Keep config keys composable (e.g. checkout.buyButton.Text vs buttonText) so configs stay organised as they grow.
- [14:08](https://youtu.be/-CdXP025MvU?t=848) **[[analytics-metrics]]** Check minimum detectable effect before launching an experiment; if the required effect is too high you won't measure anything.
- [14:32](https://youtu.be/-CdXP025MvU?t=872) **[[common-mistakes]]** Don't peek at experiment results after 24 hours; novelty effects mislead. Wait for the planned duration.
- [14:32](https://youtu.be/-CdXP025MvU?t=872) **[[analytics-metrics]]** Only trust statistically significant (shaded) metrics; non-significant ones can be positive or negative per the confidence interval.
- [12:32](https://youtu.be/-CdXP025MvU?t=752) **[[analytics-metrics]]** If an experiment is non-significant across all metrics, go with informed intuition, but don't ramp a change that is significantly negative.
- [13:13](https://youtu.be/-CdXP025MvU?t=793) **[[analytics-metrics]]** Monetisation and D1 retention metrics are noisier with wider intervals; run monetisation experiments longer or with larger samples.
- [18:16](https://youtu.be/-CdXP025MvU?t=1096) **[[pricing]]** Test starter pack prices, included items and presentation; payer conversion rate is a key metric to watch.
- [17:34](https://youtu.be/-CdXP025MvU?t=1054) **[[analytics-metrics]]** Use 2-3 variants rather than many fine-grained ones; splitting users into tiny buckets makes significance nearly impossible.
- [20:18](https://youtu.be/-CdXP025MvU?t=1218) **[[analytics-metrics]]** Run experiments rather than guessing; without them you can't tell if a metric change came from your update or from a weekend or holiday.
- [20:18](https://youtu.be/-CdXP025MvU?t=1218) **[[development-process-and-speed]]** Avoid running overlapping experiments on the same features since they can interact and skew results.

## Numbers
- [0:47](https://youtu.be/-CdXP025MvU?t=47) Playtime lift from experiments (alpha): **up to 21%**
- [8:33](https://youtu.be/-CdXP025MvU?t=513) Experiment statistical confidence level: **95% CI**
- [11:51](https://youtu.be/-CdXP025MvU?t=711) Example experiment duration deemed sufficient: **18 days (~2.5 weeks)**
- [12:32](https://youtu.be/-CdXP025MvU?t=752) Example non-static experiment duration: **21 days**
- [13:13](https://youtu.be/-CdXP025MvU?t=793) ARPU confidence interval width (example): **+10% to -15%**
- [13:13](https://youtu.be/-CdXP025MvU?t=793) Playtime confidence interval width (example): **+2% to -4%**
- [15:29](https://youtu.be/-CdXP025MvU?t=929) Config JSON max size (unverified, speaker unsure): **~100,000 characters**
- [17:34](https://youtu.be/-CdXP025MvU?t=1054) Suggested variant count example: **3 variants (e.g. 0.5, 2, 3)**

## Games
- **Unnamed creator game (tutorial rewards experiment)** [9:47](https://youtu.be/-CdXP025MvU?t=587): Positive, significant monetisation and D1/playtime results across tutorial rewards test; creator ramped it.
- **Unnamed creator game (improved tutorial design)** [11:10](https://youtu.be/-CdXP025MvU?t=670): Playtime static-negative on new tutorial design; team chose not to ramp without strong conviction.

## Tools
Roblox Configs (Studio config editor and Creator Hub), Roblox Experiments (Creator Hub), Minimum detectable effect estimator, Config service (Luau)

## He points to
- create.roblox.com/docs/production/configs
- create.roblox.com/docs/production/experiments

## Quotes
- [13:51](https://youtu.be/-CdXP025MvU?t=831) "Test stage configs in Studio first. You always want to dog food before you publish so that you don't miss something."
- [14:32](https://youtu.be/-CdXP025MvU?t=872) "Don't make decisions too early... there's like a lot of novelty effect potentially, and you can be making the wrong decisions."
- [20:18](https://youtu.be/-CdXP025MvU?t=1218) "If you don't run experiments... you have no clue is it because of the update you made or is it because the weekend happened."

## On screen
Contact sheet shows Studio config editor with staged configs and a publish dialog, experiment creation flow with MDE/estimated audience, and Creator Hub experiment results: ARPU and D1 retention scorecards with green (static positive) cells, a confidence interval popup for D1 retention, and an ARPU interval popup showing roughly -15% to +10%. Final best-practices slide lists the same three points per feature.</visual_notes>

## Topics
[[analytics-metrics]] [[common-mistakes]] [[development-process-and-speed]] [[playtesting-and-feedback]] [[pricing]]

Back to [[MustWatch - How to make successful Roblox games]]
