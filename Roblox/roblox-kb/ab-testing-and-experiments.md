---
title: Ab Testing And Experiments
topic: ab-testing-and-experiments
theme: Mindset & Process
sources: 38 videos
creators: [CORSO, Deconstructor of Fun, GDC Festival of Gaming, GameMakers, GamesBeat, Last Level Studios, Quez, Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, ThatGuyEvan, janisjanis01]
source_dates: 2020-02-14 to 2026-10-30
tags: [roblox, knowledge-base, ab-testing-and-experiments]
---

# Ab Testing And Experiments

_A/B testing, Roblox Experiments/Configs, hypothesis-driven iteration, statistics for tests._

Evidence base: 94 extracted items from 38 videos by CORSO, Deconstructor of Fun, GDC Festival of Gaming, GameMakers, GamesBeat, Last Level Studios, Quez, Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, ThatGuyEvan, janisjanis01 (2020-02-14 to 2026-10-30). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Creators (mostly Roblox DevForum and Creator Docs, much of it official) teach hypothesis-driven iteration using Roblox Experiments and Configs. Use configs for live-tunable values and feature flags. Create experiments with a baseline plus up to 2 treatments, an exposure percent, a duration of 14–60 days and a goal metric that matches the hypothesis. Configuration is immutable once started, so finalize it in draft. Use Early Harm Detection (first 24 hours, 5-minute updates) only to decide whether to stop, never to launch. Wait for the full duration and check SRM and MDE diagnostics before trusting results. Matchmaking experiments need 100% traffic, or a pre-post analysis when player counts are low. Targeting and conditional configs serve different values to different audiences. Outside Roblox, GDC and others advise small-slice A/B rollouts (5%), testing title and thumbnail as pairs, and continuing to test creatives despite most failing. Indie figures are self-reported.

## Rules and findings
- **Tie each experiment to one hypothesis and a matching goal metric** (multiple-creators): Pick a goal metric that matches the hypothesis, e.g. DAY_1_RETENTION for a boss-health change, or average session time in the 50/50 bossHealth example. Keep the test tied to that metric. For matchmaking configs, measure playtime, retention and revenue per user before full rollout. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676). Newest source 2026-10-28.
- **Use configs for tunable values and feature flags** (single-mention): Put enemy health, weapon damage, item prices and event toggles in configs so you can change them live without restarting servers. Config changes deploy over about 5 minutes. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores). Newest source 2026-10-28.
- **Create experiments through the Experiments API with full parameters** (multiple-creators): Specify variants, exposure percent, duration and goal metric. Example: 50/50 bossHealth, 14 days (1209600 s), 50% exposure. Another example payload used 40% exposure with 50/50 weights; these are examples, not recommendations. Sources: [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments). Newest source 2026-10-28.
- **Respect experiment structural limits** (one-creator-repeated): Duration must be 14–60 days. An in-experience config experiment allows 1 baseline plus up to 2 treatments. Only 1 matchmaking experiment can run per universe. Exactly one variant must have isBaseline true. The productType discriminator must match the populated block (inGameConfigExperimentConfiguration or matchmakingExperimentConfiguration). Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments). Newest source 2026-10-28.
- **Finalize configuration in draft** (single-mention): Experiment configuration becomes immutable once started or scheduled, so edit duration, rollout and variants while still in draft. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments). Newest source 2026-10-28.
- **Add a config before a targeted experiment** (multiple-creators): Targeted experiments require an existing config. Use Experiment Targeting to run tests on specific audiences (e.g. new players) instead of the whole player base. Sources: [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4836039). Newest source 2026-08-28.
- **Use Conditional Configs and order rules deliberately** (multiple-creators): Conditional Configs serve different values for the same key by player attributes (e.g. lower boss health for new players) without separate configs. Rules are evaluated top to bottom and the first matching rule wins, so put specific rules first. Sources: [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4836039). Newest source 2026-08-28.
- **Use Early Harm Detection only as a stop signal** (multiple-creators): For the first 24 hours, Playtime, ARPU and payer conversion update every 5 minutes. The alert fires only if the entire CI falls below a catastrophic threshold. Do not make launch decisions from first-24-hour results. Sources: [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/weekly-recap-september-28%E2%80%93october-2-2026/4910267), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734). Newest source 2026-10-28.
- **Know the early-harm thresholds** (single-mention): Critical harm is flagged only if the whole confidence interval is below the limit: Playtime -10%, ARPU -20%, payer conversion rate -20%. Sources: [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734). Newest source 2026-10-01.
- **Enroll at least 10,000 players** (multiple-creators): Harm decisions need at least 10,000 enrolled players across variant and control; below that, lift is shown but no harm decisions are made. Set the minimum detectable effect (MDE) to size the rollout. Sources: [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676). Newest source 2026-10-01.
- **Wait for the full duration and daily results before rolling out** (single-mention): Novelty effects make early results swing. Wait for daily results and the full duration before rolling out a variant. Sources: [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734). Newest source 2026-10-01.
- **Check SRM and restart if flagged** (multiple-creators): If an SRM alert appears in the Results tab (isSrmDetected true in stats), the split is unreliable. Stop and restart the experiment. Metrics and SRM are checked every 5 minutes for the first 24 hours, then daily. Sources: [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734). Newest source 2026-10-28.
- **Wait 24 hours before pulling /stats** (single-mention): Stats diagnostics are not available until the experiment has run 24 hours. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments). Newest source 2026-10-28.
- **Stop without a winner by omitting variantId** (single-mention): Calling :complete without variantId stops the experiment with no winner and the config reverts to its previous value. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments). Newest source 2026-10-28.
- **Optionally forward harm alerts via webhook** (single-mention): Set up a webhook to send early harm notifications to your own monitoring tools. Sources: [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734). Newest source 2026-10-01.
- **Run matchmaking experiments at 100% traffic** (one-creator-repeated): Players are matched only within the same variant, so lower rollouts shrink the server pool and reduce statistical significance. Sources: [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419), [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419). Newest source 2025-11-06.
- **Fall back to pre-post analysis or dashboards when player counts are low** (one-creator-repeated): Matchmaking experiments need enough servers. Without them, compare matchmaking signal dashboards before and after the change, or monitor via analytics dashboards. Sources: [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419), [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419). Newest source 2025-11-06.
- **Roll out live value changes gradually** (single-mention): Publish with GradualRollout (15-minute rollout) instead of Immediate when changing live gameplay values, to limit blast radius. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/configs). Newest source 2026-10-28.
- **Verify config drafts before publishing** (single-mention): Publishing a config draft is irreversible except by restoring a previous version. GET the draft to verify before POST publish. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten). Newest source 2026-10-28.
- **Ship new onboarding as a small-slice A/B test** (multiple-creators): Glue's Design Home used 5% new onboarding vs 95% control and scaled up only if retention improved. Sources: [GDC Festival of Gaming 2022-02 16:09](https://youtu.be/WGRpglQ87XE?t=969), [GDC Festival of Gaming 2022-02 16:09](https://youtu.be/WGRpglQ87XE?t=969). Newest source 2022-02-01.
- **Iterate onboarding in small steps** (one-creator-repeated): Roblox-featured example: each change retained a bit more while spending on ads, and the algorithm picked the game up around day 7-8. Self-reported. Sources: [Roblox Creators 2026-10 13:45](https://youtu.be/gy_fAtIkqfo?t=825), [Roblox Creators 2026-10 15:49](https://youtu.be/gy_fAtIkqfo?t=949). Newest source 2026-10-30.
- **A/B test thumbnails, and test title and thumbnail as pairs** (multiple-creators): A thumbnail's CTR can change with the title beside it, and vice versa. janisjanis01 noted that a prior owner running no thumbnail tests was a missed opportunity. Sources: [janisjanis01 2026-09 6:27](https://youtu.be/WJpNCB5J9bg?t=387), [Roblox DevForum 2026-09](https://devforum.roblox.com/t/ab-testing-experience-titles-together-with-thumbnails/4900092), [Roblox DevForum 2026-09](https://devforum.roblox.com/t/ab-testing-experience-titles-together-with-thumbnails/4900092). Newest source 2026-09-27.
- **Use ThumbnailWinningSegments and settled analytics for thumbnails** (single-mention): ThumbnailWinningSegments shows which audience segments a thumbnail performs best with (low-advice source). Re-pull analytics several days later so values are settled before comparing results. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/analytics/metrics), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/home-thumbnail-a-b-test/4947121). Newest source 2026-10-28.
- **Expect most creatives to fail; keep testing** (single-mention): Do not cut a channel after a week or two of poor attributed results. Sources: [Deconstructor of Fun 2026-06 43:53](https://youtu.be/2BsMLCk8FEU?t=2633). Newest source 2026-06-01.
- **Test reward value against perceived cost when ad impressions per DAU are low** (single-mention): Experiment with reward size relative to the perceived cost of watching. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/rewarded-video-optimization). Newest source 2026-10-30.
- **Playtest stat-boosting upgrades before shipping** (single-mention): Unlocks like +10 placement limit or +25% starting cash can warp strategy and difficulty. Low-advice source. Sources: [CORSO 2025-05 3:03](https://youtu.be/O2LZcQG5PPQ?t=183). Newest source 2025-05-29.
- **Playtest on low-end devices and with Test, not Run** (multiple-creators): Test on Chromebook-class devices. Use Test or Test Here so your avatar spawns; Run skips avatar insertion and blocks testing avatar-VFX interactions. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/developer/planning-for-educational-settings), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/artist/test-and-save). Newest source 2026-10-28.
- **Consider paid-access alpha for staged player growth** (single-mention): Gradual growth, exclusive alpha-tester rewards and an invested early community. Self-reported. Sources: [Last Level Studios 2020-02 28:34](https://youtu.be/_LdpUJ41cso?t=1714). Newest source 2020-02-14.
- **Mind legal limits and platform constraints when testing** (multiple-creators): Avoid under-13 testers on text platforms like Discord or when an NDA applies; consult a lawyer. Team Create and Team Test are unavailable with Server Authority Studio Beta enabled. Redesign mechanics rather than delete them to keep Kids/Select review status. Sources: [Roblox DevForum 2023-02](https://devforum.roblox.com/t/guide-effectively-qa-testing-your-roblox-experience/2199838), [Roblox DevForum 2025-12](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188). Newest source 2026-08-25.
- **Run and ramp experiments in Studio via Configs and Experiments** (single-mention): Official 2026-04 guidance: use Configs and Experiments in-Studio to run A/B tests and ramp winning variants automatically, rather than checking results on the web. Newer than manual web-based checking. The existing Experiments API rule still applies for creating experiments with full parameters. Sources: [Roblox 2026-04 36:37](https://youtu.be/8IcYpOl4Sdk?t=2197). Newest source 2026-04-16.
- **Answer only the 16+ question when the game has no restricted content** (single-mention): Official DevForum post (2026-09): once the Simplified publishing flow ships, eligible games with no restricted content can answer the single 16+ question instead of the full questionnaire. Not an experiment rule; relevant only to publishing. Sources: [Roblox DevForum 2026-09](https://devforum.roblox.com/t/making-publishing-easier-our-vision-and-whats-coming/4865780). Newest source 2026-09-11.
- **Test one variable at a time** (single-mention): Keep content constant and change a single factor per test (e.g., only duration or only aspect ratio) so results are comparable. Mixing concepts muddies which change caused the effect. Source is an indie creator tagged low-advice, so treat as a practice to verify, not a platform rule. Sources: [GameMakers 2021-11 4:49](https://youtu.be/Ga7g6ZJhFfo?t=289). Newest source 2021-11-10.
- **Read split-test results as a confidence level, not a binary significant/not-significant verdict** (one-creator-repeated): Stat-sig is a continuum. GameMakers (indie, 2022) says ~80% confidence with no negative signals is often worth rolling out. This is an indie heuristic and does not replace the Roblox gates already in this file (full duration, daily results, SRM check, 24h wait before /stats). Sources: [GameMakers 2022-08 16:19](https://youtu.be/JVCao-Yhu2M?t=979), [GameMakers 2022-08 16:19](https://youtu.be/JVCao-Yhu2M?t=979), [GameMakers 2022-08 17:44](https://youtu.be/JVCao-Yhu2M?t=1064). Newest source 2022-08-30.
- **Make test variants bold enough to move metrics** (one-creator-repeated): Tiny tweaks (about 5% value change, a single button colour on one screen) rarely produce a meaningful result. GameMakers suggests 50-100% value changes or reskinning key high-traffic screens. Pair bold variants with the small-slice guard below. Sources: [GameMakers 2022-08 35:11](https://youtu.be/JVCao-Yhu2M?t=2111), [GameMakers 2022-08 35:51](https://youtu.be/JVCao-Yhu2M?t=2151). Newest source 2022-08-30.
- **Contain risky tests to a small audience slice and watch ratings and retention** (single-mention): When a variant could hurt the player base, limit exposure to a small slice and monitor ratings and retention during the test to cap downside. This extends the existing small-slice onboarding rule to all risky tests. Sources: [GameMakers 2022-08 36:32](https://youtu.be/JVCao-Yhu2M?t=2192). Newest source 2022-08-30.
- **Keep a historical test vault** (one-creator-repeated): Store templates, wireframes, hypotheses and past split-test results in one library. GameMakers reports a vault of hundreds of tests improves future prioritisation and prediction. Record each experiment's hypothesis, metric, result and confidence so later tests can build on it. Sources: [GameMakers 2022-08 25:18](https://youtu.be/JVCao-Yhu2M?t=1518), [GameMakers 2022-08 11:17](https://youtu.be/JVCao-Yhu2M?t=677). Newest source 2022-08-30.
- **Track hypothesis outcomes over time, not only at launch** (single-mention): Verify a feature's forecast with real tests and re-measure after launch. The Bejeweled Blitz solo-journey feature beat forecast by about 20% at launch and by 10-12% after three months, so a launch-only read can miss durable effects. Sources: [GameMakers 2024-03 8:19](https://youtu.be/zvNQHk1hUYc?t=499), [GameMakers 2024-03 8:19](https://youtu.be/zvNQHk1hUYc?t=499). Newest source 2024-03-08.
- **Tune reward-to-difficulty ratios per player with multivariate tests** (single-mention): Instead of picking one reward/difficulty formula, run multivariate tests to find the best ratio for each player segment. GameMakers reports LTV lift of up to about 10% from difficulty tuning. Sources: [GameMakers 2025-02 7:00](https://youtu.be/qZRNpN5M8jA?t=420), [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852). Newest source 2025-02-04.
- **Test every monetisation and ad funnel step once at scale** (single-mention): At scale, run experiments across each funnel step (pricing, offers, creatives, ad waterfall, bidding) rather than only gameplay. This applies only once traffic supports it; below that, use the low-player-count fallbacks already in this file. Sources: [GameMakers 2025-02 15:01](https://youtu.be/qZRNpN5M8jA?t=901). Newest source 2025-02-04.
- **Structure ad creative tests as a matrix of variables** (single-mention): Build a grid of creatives across durations and aspect ratios, for example 16 durations from 7.5s to 45s in 2.5s steps by 4 aspect ratios = 64 creatives. Modular builds (5s intro, 2.5s outro, content blocks) make the matrix cheap to produce. Indie, low-advice source. Sources: [GameMakers 2021-11 3:47](https://youtu.be/Ga7g6ZJhFfo?t=227), [GameMakers 2021-11 4:49](https://youtu.be/Ga7g6ZJhFfo?t=289). Newest source 2021-11-10.

## Checklist
- [ ] Write a hypothesis and choose a matching goal metric (e.g. DAY_1_RETENTION)
- [ ] Move the tunable value into a config
- [ ] For a targeted test, create the config first and set targeting (e.g. new players)
- [ ] Order conditional rules so the first match is the intended one
- [ ] Set variants: exactly one isBaseline true, at most 2 treatments
- [ ] Make productType match the configuration block
- [ ] Set duration (14–60 days), exposure percent and weights
- [ ] Set MDE and make sure you can enroll at least 10,000 players
- [ ] Review everything in draft, because it is immutable after start
- [ ] For matchmaking tests, use 100% rollout, and only 1 may run per universe
- [ ] Publish live value changes with GradualRollout (15 minutes)
- [ ] Watch Playtime, ARPU and payer conversion during the first 24 hours (updates every 5 minutes)
- [ ] Optionally set up a webhook for early harm alerts
- [ ] Stop if critical harm is flagged, or if SRM is detected (then restart)
- [ ] Do not decide launch from the first 24 hours
- [ ] Wait at least 24 hours before pulling /stats
- [ ] Wait for the full duration and daily results before picking a winner
- [ ] Complete with variantId to ship a winner, or omit it to revert
- [ ] Test title and thumbnail as pairs
- [ ] Re-pull analytics a few days later before comparing thumbnail tests
- [ ] Use a pre-post dashboard comparison when traffic is too low for an A/B
- [ ] Verify config drafts with GET before POST publish
- [ ] Playtest on low-end devices and with Test/Test Here
- [ ] Check whether ramping a winning variant can be done in-Studio via Configs and Experiments before doing manual web checks.
- [ ] Before launching a test, confirm it changes exactly one variable; split multi-variable ideas into separate tests.
- [ ] Make the variant a meaningful change (roughly 50-100% on a value, or a reskin of a high-traffic screen) rather than a ~5% tweak.
- [ ] Record a confidence level for each split test alongside the Roblox gates (full duration, SRM check, /stats after 24h).
- [ ] Treat about 80% confidence with no negative ratings or retention signals as a candidate for rollout only after the existing gates pass.
- [ ] Set ratings and retention as guard metrics for any risky test and limit it to a small audience slice.
- [ ] Log each experiment (hypothesis, metric, result, confidence, date) in a single test vault.
- [ ] Re-check shipped features at about 3 months against the original forecast.
- [ ] For reward or difficulty tuning, run a multivariate test over player segments instead of one fixed formula.
- [ ] For ad creatives, generate a matrix over duration and aspect ratio and test the grid.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Experiment duration range | 14–60 days | Allowed durationSeconds. Example 14 days = 1209600 s. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments) |
| Example experiment | 14 days, 50% exposure, 50/50 variants (bossHealth) | API snippet example. | [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676), [Roblox DevForum 2026-08](https://devforum.roblox.com/t/x/4828676) |
| Example create payload | 40% exposure, 50/50 weights | Not a recommendation. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments) |
| Variants per in-experience experiment | 1 baseline + up to 2 treatments |  | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments) |
| Concurrent matchmaking experiments | 1 per universe |  | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments) |
| Recommended matchmaking rollout | 100% | Players matched only within the same variant. | [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419), [Roblox DevForum 2025-11](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419) |
| Stats availability | after 24 hours |  | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/experiments) |
| Early harm window | first 24 hours, every 5 minutes | Then daily checks. | [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/weekly-recap-september-28%E2%80%93october-2-2026/4910267) |
| Early harm metrics | 3: playtime, ARPU, payer conversion |  | [Roblox DevForum 2026-08](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462) |
| Playtime harm threshold | -10% (entire CI below) |  | [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734) |
| ARPU harm threshold | -20% |  | [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734) |
| Payer conversion harm threshold | -20% |  | [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734) |
| Minimum enrolled players for harm decisions | 10,000 across variant and control |  | [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734), [Roblox DevForum 2026-10](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734) |
| Config deploy time | 5 minutes |  | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) |
| Gradual rollout duration | 15 minutes |  | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/configs) |
| Onboarding A/B split | 5% new / 95% control | Design Home, self-reported. | [GDC Festival of Gaming 2022-02 16:09](https://youtu.be/WGRpglQ87XE?t=969), [GDC Festival of Gaming 2022-02 16:09](https://youtu.be/WGRpglQ87XE?t=969) |
| Algorithm pickup in onboarding iteration case | around day 7-8 | Self-reported. | [Roblox Creators 2026-10 13:45](https://youtu.be/gy_fAtIkqfo?t=825) |
| Creator-race star progression | 10-40 days | Tangential to testing. | [Deconstructor of Fun 2026-06 22:37](https://youtu.be/2BsMLCk8FEU?t=1357) |
| Age check prompt rate limit | 1 per player per 15 min per session | Tangential. | [Roblox DevForum 2026-04](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091) |
| Age estimation accuracy (facial estimation) | within 1-2 years of real age | Range claimed by Roblox (2026-01, official). Relevant only if age-based segmentation is considered for experiments; it is a claim, not a measured guarantee. | [Roblox 2026-01 4:25](https://youtu.be/m5vqnNSCFCI?t=265) |
| Confidence level accepted for rollout (indie heuristic) | ~80% | GameMakers (indie, self-reported, 2022). Only when there are no negative signals. Not a Roblox official threshold. | [GameMakers 2022-08 17:44](https://youtu.be/JVCao-Yhu2M?t=1064), [GameMakers 2022-08 16:19](https://youtu.be/JVCao-Yhu2M?t=979) |
| Test vault size (indie) | hundreds of split tests | GameMakers internal vault, self-reported, 2022. | [GameMakers 2022-08 11:17](https://youtu.be/JVCao-Yhu2M?t=677) |
| Bejeweled Blitz solo-journey feature vs forecast | +20% at launch; +10-12% after three months | GameMakers, self-reported, 2024. Performance versus forecast. | [GameMakers 2024-03 8:19](https://youtu.be/zvNQHk1hUYc?t=499), [GameMakers 2024-03 8:19](https://youtu.be/zvNQHk1hUYc?t=499) |
| LTV lift from difficulty tuning | up to ~10% | GameMakers, self-reported, 2022-2025. | [GameMakers 2022-08 30:52](https://youtu.be/JVCao-Yhu2M?t=1852), [GameMakers 2025-02 7:00](https://youtu.be/qZRNpN5M8jA?t=420) |
| Creative matrix size | 64 creatives = 16 durations (7.5s to 45s, 2.5s steps) x 4 aspect ratios | GameMakers, low-advice, 2021. Modular build: 5s intro + 2.5s outro + content blocks. | [GameMakers 2021-11 3:47](https://youtu.be/Ga7g6ZJhFfo?t=227) |
| Minor tweak likely to be underpowered | ~5% value change or single button colour | GameMakers guidance: such changes rarely move metrics; try 50-100% changes. | [GameMakers 2022-08 35:11](https://youtu.be/JVCao-Yhu2M?t=2111), [GameMakers 2022-08 35:51](https://youtu.be/JVCao-Yhu2M?t=2151) |

## Where creators agree
- Roblox DevForum and Roblox Creator Docs agree that experiments should run for the full duration and be judged on a defined goal metric.
- Roblox DevForum and Creator Docs agree that SRM signals an unreliable split.
- Roblox DevForum and Roblox Creator Docs agree that targeting and conditional configs enable per-audience values.
- GDC Festival of Gaming and Roblox DevForum both favor limited-exposure or gradual rollouts to limit risk.
- Roblox DevForum and janisjanis01 agree that thumbnails should be A/B tested; DevForum adds that titles and thumbnails go together.
- Roblox Creators and GDC Festival of Gaming both describe iterating in small, measured steps.
- Deconstructor of Fun (Q1916, 2026-06) says you can't work by spray-and-pray; this matches the existing rule to tie each experiment to one hypothesis.
- GameMakers (T18428, 2021) and the existing one-hypothesis rule agree that controlled, single-variable tests make results interpretable.
- GameMakers (Q1874, 2021) and the existing rule 'Expect most creatives to fail; keep testing' agree that testing is ongoing.

## Where creators disagree
- **Rollout size of tests**
  - GDC Festival of Gaming: start with a 5% slice and scale up if retention improves.
  - Roblox DevForum: matchmaking experiments should run at 100% because lower rollouts shrink the server pool.
  - These apply to different contexts; the 5% slice is for onboarding and not matchmaking. Official examples use 40-50% exposure for config tests.
- **How quickly to act on results**
  - Roblox DevForum: do not launch from the first 24 hours, wait for full duration.
  - Roblox Creators: iterate frequently on small changes and judge by retention while spending on ads (different context, not a controlled experiment).
  - Deconstructor of Fun: judge creatives over more than a week or two.
- **Iteration size for onboarding and feature changes**
  - Existing knowledge file: iterate onboarding in small steps and ship it as a small-slice A/B test.
  - GameMakers (T18449, 2022): make tests aggressive, using 50-100% value changes or reskinning key screens, because tiny tweaks rarely move metrics.
  - Reconciliation: keep the small-slice exposure for risky changes, but make the variant bold enough to produce a readable signal.
- **Rollout confidence bar**
  - GameMakers (T18448, 2022): roughly 80% confidence with no negative signals is often enough to roll out.
  - Existing knowledge file: wait for the full duration and daily results, check SRM, and wait 24h before pulling /stats. These gates are stricter and not confidence-based.
  - Reconciliation: treat the 80% figure as a secondary heuristic that never overrides the existing gates.

## Date context (what may be outdated)
- The Roblox Experiments, Early Harm Detection, Targeting and Conditional Configs material dates from 2026-08 to 2026-10 and is the most current.
- Matchmaking experiment guidance dates from 2025-11, earlier than the in-experience config experiment material, so check for later changes.
- The 2022 GDC onboarding A/B example is older and non-Roblox, so use it only as a general pattern.
- The Experiments API is new (2026); limits like 14–60 days and 10,000 players may change, so verify against current docs.
- Only the 2026-10 DevForum posts add the Early Harm Detection thresholds; the 2026-08 posts mention only a 'catastrophic threshold'.
- 2026-04 (official): in-Studio running and automatic ramping of winning variants via Configs and Experiments; treat as the newer path for ramping, while the API rule remains valid for creating experiments with full parameters.
- 2026-09 (official DevForum): Simplified publishing flow allows a single 16+ question for games without restricted content, replacing the full questionnaire once it ships. Eligibility details are not confirmed in the source.
- 2026-01 (official): age estimation accuracy claim of within 1-2 years.
- All new items are indie, self-reported. No [OFFICIAL] Roblox items in this batch.
- Sources span 2021-11 to 2026-06. Most GameMakers items are 2021-2025; the 2021 items are tagged low-advice.
- The newest item (Deconstructor of Fun, 2026-06) reinforces hypothesis-driven testing rather than adding a new tactic.
- Confidence-based rollout advice (2022) predates the current Roblox Experiments tooling. Where it conflicts with existing gates, prefer the existing rules.

## Instructions for an agent using this file
- If a user wants to test a gameplay value, then put it in a config, create a draft experiment with a baseline and at most 2 treatments, and choose a goal metric matching the hypothesis.
- If an experiment's duration is outside 14–60 days, then correct it before creating.
- If the experiment is already started or scheduled, then do not try to edit it; stop it and create a new one.
- If the user asks to launch based on the first 24 hours, then refuse and explain that Early Harm Detection is only for stopping.
- If isSrmDetected is true or the Results tab shows SRM, then recommend stopping and restarting the experiment.
- If enrolled players are below 10,000, then explain that no harm decisions are made and suggest raising exposure or widening the audience.
- If the test is on matchmaking, then use 100% exposure, allow only one running per universe, and fall back to pre-post dashboard analysis if player counts are low.
- If the user wants different values per audience, then add a config first, then use targeting or conditional configs, and order rules most specific first.
- If the user changes live values, then recommend GradualRollout and verify drafts with GET before publishing.
- If the user tests thumbnails, then test title and thumbnail as pairs and wait several days for analytics to settle; label indie revenue or retention claims as unverified and prefer official mechanics.
- If the user asks how to ramp a winning experiment variant, prefer the in-Studio Configs and Experiments flow (T17611) over manual web checks, and still follow the existing gradual-rollout rules.
- If the user asks about publishing age ratings for a game with no restricted content and the Simplified flow is available, answer the single 16+ question (T17646) instead of the full questionnaire.
- Do not treat the age-estimation range (N7460) as a guarantee; cite it as Roblox's claimed accuracy.
- If a proposed test changes more than one variable, split it into separate experiments before setup.
- If a proposed variant is a small tweak (about 5% or a single colour), recommend a bolder variant unless the test is explicitly a guard test.
- If a risky test is proposed, restrict it to a small slice and add ratings and retention as guard metrics.
- If a split test is around 80% confidence with no negative signals, still require the existing Roblox gates (full duration, SRM check, 24h wait before /stats) before recommending rollout.
- After each experiment concludes, log hypothesis, metric, result and confidence in the test vault.
- For reward or difficulty tuning, propose a multivariate test over player segments rather than one fixed formula.
- For ad creatives, propose a matrix over duration and aspect ratio rather than a few hand-picked variants.
- Re-check shipped features at about three months against the original forecast before judging success.

## Not covered here (research elsewhere)
- No guidance on how to compute sample size or statistical power beyond the MDE and 10,000-player minimum.
- There are no guidelines on significance levels, confidence thresholds, multiple comparisons or how to read the final Results.
- No detail on which metrics are available as goal metrics beyond the examples (DAY_1_RETENTION, average session time).
- No guidance on running multiple concurrent in-experience experiments or on interaction effects.
- No concrete thumbnail or ad-creative A/B workflow or tooling steps beyond ThumbnailWinningSegments.
- No case studies with verified results of Roblox Experiments; the indie claims are self-reported.
- The exact API endpoints and authentication for experiments are not covered; check the Roblox Creator Docs.
- No retention benchmarks or thresholds for onboarding A/B tests; the GamesBeat tip (T17597) gives no numbers and is indie self-reported.
- In-Studio auto-ramp mechanics (ramp steps, thresholds, stop conditions) are not described in T17611.
- Simplified publishing flow eligibility criteria and rollout dates are not stated in T17646.
- Whether age estimation (N7460) can be used to segment experiment audiences is not covered.
- Retention-check methodology for onboarding tests (cohort definition, time window) is not covered.
- No Roblox-official guidance on confidence thresholds or minimum sample sizes beyond the 10,000-player enrolment rule.
- No Roblox-specific detail on multivariate experiment setup, or whether the Experiments API supports multivariate tests.
- Ad-creative matrix guidance is indie and mobile-ad oriented (ad waterfall, bidding). Roblox ad creatives may not follow the same constraints.
- No guidance on which guard metrics beyond ratings and retention matter for Roblox experiments.
- No data on how to size a test vault or how long to keep historical results.
- No quantified guidance on how many tests to run per month or how to prioritise them.

## Quotes (near-verbatim)
- "it's the testing is ongoing it's not like no we found out everything about our creative creatives right now" ([GameMakers 2021-11 27:26](https://youtu.be/Ga7g6ZJhFfo?t=1646))
- "statsig is often treated like a binary yes or no result... there's a continuum of confidence" ([GameMakers 2022-08 16:19](https://youtu.be/JVCao-Yhu2M?t=979))
- "don't change a button color on a single screen and expect a statistically meaningful result" ([GameMakers 2022-08 35:51](https://youtu.be/JVCao-Yhu2M?t=2151))
- "You can't work like in a method of spray and pray." ([Deconstructor of Fun 2026-06 42:31](https://youtu.be/2BsMLCk8FEU?t=2551))
- "Conditional Configs let you serve different values for the same config key based on player attributes." ([Roblox DevForum 2026-08 ](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462))
- "Rules are evaluated from top to bottom, and the first matching rule wins." ([Roblox DevForum 2026-08 ](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462))
- "A thumbnail can perform differently depending on the title shown next to it, and vice versa." ([Roblox DevForum 2026-09 ](https://devforum.roblox.com/t/ab-testing-experience-titles-together-with-thumbnails/4900092))
- "Do not launch based on early results. Results in the first 24 hours only test for harm." ([Roblox DevForum 2026-10 ](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734))
- "EHD is only meant to help you decide whether to stop an experiment early. It is not meant for launch decisions." ([Roblox DevForum 2026-10 ](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734))
- "every time we made a change, we would spend more money on ads, get a more influx of players, and we'd retain like a little bit." ([Roblox Creators 2026-10 15:49](https://youtu.be/gy_fAtIkqfo?t=949))

## Verified additions

_Chunk 4 (2026-11-01). Labels: OFFICIAL / CORROBORATED / SINGLE-SOURCE / CONTRADICTED / OUTDATED-UNSURE. Hand-added rows kept in `youtube-learn/supplements/topics/ab-testing-and-experiments.md`; they survive rebuilds._

- **Experiments targeting** (OFFICIAL, DevForum staff weekly recap 2026-08-28): experiments support targeting, segmentation, conditional configs and early harm detection. The 14-day / 50% exposure figures seen in staff posts are API snippet examples, not recommendations.
- **Rewarded video tests** (OFFICIAL, docs promotion/rewarded-video-optimization): when impressions per DAU is low, test reward value against the perceived cost of watching.
- **Iterate onboarding while buying ads** (SINGLE-SOURCE, RIVALS developer on the Roblox Creators channel, self-reported): small onboarding changes each retained a bit more; the algorithm picked the game up around day 7-8.

_Chunk 7 additions (2026-11-01)._

- **Early Harm Detection (EHD) for Experiments** (OFFICIAL, DevForum staff 2026-10-01): for the first 24 hours Playtime, payer conversion and ARPU refresh every 5 minutes and SRM is checked early; critical harm is flagged only when the whole confidence interval is below -10% playtime, -20% ARPU or -20% payer conversion, and only with 10,000+ enrolled players across variant and control. EHD is for stop decisions, not launch decisions. Source: [Experiments: Early Harm Detection](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734).
- **Conditional Configs, Experiment Targeting, segmentation** (OFFICIAL, DevForum 2026-08-24): per-player-attribute config values, targeted experiments, new analytics segment dimensions and an Analytics and LiveOps early access program. Source: [Evolving Experiments and Analytics](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting-early-access-program/4828462).
- **Home thumbnail A/B test attribution concern** (SINGLE-SOURCE, DevForum user 2026-10-20): reports the test credits about half of Home qualified plays since 2026-10-16, which would bias results; no staff reply seen. Treat thumbnail-test lifts from this window with caution. Source: [thread 4947121](https://devforum.roblox.com/t/4947121).

## Appendix: every extracted tip on this topic

- 2020-02-14 Last Level Studios [28:34](https://youtu.be/_LdpUJ41cso?t=1714): Release in paid access alpha: gradual player growth, exclusive alpha-tester rewards, and invested early community.
- 2021-11-10 GameMakers [4:49](https://youtu.be/Ga7g6ZJhFfo?t=289): Test one variable at a time: same content, only duration and aspect ratio changed, so results are comparable instead of muddied by different concepts.
- 2022-02-01 GDC Festival of Gaming [16:09](https://youtu.be/WGRpglQ87XE?t=969): Roll out new onboarding as an A/B test with a small traffic slice (Design Home used 5% vs 95%) and scale up only if retention improves.
- 2022-08-30 GameMakers [16:19](https://youtu.be/JVCao-Yhu2M?t=979): Report split-test results as a confidence percentage rather than binary stat-sig; ~80% confidence with no negative signals is often worth rolling out.
- 2022-08-30 GameMakers [35:11](https://youtu.be/JVCao-Yhu2M?t=2111): Make tests aggressive: tiny tweaks (5% value change, single button colour) rarely move metrics; try 50-100% value changes or reskin key high-traffic screens.
- 2022-08-30 GameMakers [36:32](https://youtu.be/JVCao-Yhu2M?t=2192): Limit risky tests to a small audience slice and watch ratings and retention to contain downside.
- 2022-08-30 GameMakers [25:18](https://youtu.be/JVCao-Yhu2M?t=1518): Keep a design library of templates, wireframes and past test results; a historical test vault makes future prioritisation and predictions better.
- 2023-02-26 Roblox DevForum [page](https://devforum.roblox.com/t/guide-effectively-qa-testing-your-roblox-experience/2199838): Use legal caution: avoid under-13 testers when using text platforms like Discord or when an NDA applies; consult a lawyer for contracts.
- 2024-03-08 GameMakers [8:19](https://youtu.be/zvNQHk1hUYc?t=499): Verify hypotheses with real tests and track results over time; Bejeweled Blitz's solo-journey feature beat forecast by 20% at launch and 10-12% after three months.
- 2025-02-04 GameMakers [7:00](https://youtu.be/qZRNpN5M8jA?t=420): Tune reward-to-difficulty ratios per player with multivariate tests rather than picking a single formula.
- 2025-02-04 GameMakers [13:32](https://youtu.be/qZRNpN5M8jA?t=812): Once you have traffic, roll changes out to a percentage of players against a control group. Untested changes leave growth on the table.
- 2025-02-04 GameMakers [15:01](https://youtu.be/qZRNpN5M8jA?t=901): At scale, build an experimentation machine that tests every funnel step: pricing, offers, creatives, ad waterfall and bidding.
- 2025-05-29 CORSO [3:03](https://youtu.be/O2LZcQG5PPQ?t=183): Playtest stat-boosting upgrades before shipping; unlocks like +10 placement limit or +25% starting cash can warp strategy and difficulty.
- 2025-11-06 Roblox DevForum [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419): Run matchmaking experiments at 100% of traffic; players are matched within the same variant, so lower rollouts shrink the server pool and reduce statistical significance.
- 2025-11-06 Roblox DevForum [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419): Matchmaking experiments need enough servers to choose from; without them, monitor matchmaking changes through analytics dashboards instead.
- 2025-11-06 Roblox DevForum [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419): Without enough players for an A/B test, use a pre-post analysis comparing matchmaking signal dashboards before and after the change.
- 2025-11-06 Roblox DevForum [page](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419): Measure matchmaking configs against playtime, retention and revenue per user before full rollout.
- 2025-12-09 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157): Avoid Team Create and Team Test during the Studio Beta; they are unavailable with Server Authority Studio Beta enabled.
- 2026-03-09 GamesBeat [page](https://gamesbeat.com/roblox-unveils-jumpstart-and-incubator-programs-to-help-creators-expand-possibilities-exclusive/): Use Roblox Experiments to A/B test onboarding tweaks and new mechanics, checking whether retention actually improved.
- 2026-04-16 Roblox [36:37](https://youtu.be/8IcYpOl4Sdk?t=2197): Use Configs and Experiments to run A/B tests in-Studio and ramp winning variants automatically, rather than checking results on the web.
- 2026-06-01 Deconstructor of Fun [43:53](https://youtu.be/2BsMLCk8FEU?t=2633): Expect most creatives to fail; keep testing rather than cutting a channel after a week or two of poor attributed results.
- 2026-07-15 Roblox DevForum [page](https://devforum.roblox.com/t/scribe-v261-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905): Not applicable; omit.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/x/4828676): Create experiments via the Experiments API with variants, exposure percent, duration and a goal metric, then check MDE and sample-ratio-mismatch diagnostics before trusting results.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/x/4828676): Example experiment: 50/50 bossHealth config test, 14-day duration (1209600 seconds), goal metric average session time.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462): Use Experiment Targeting to run tests only on specific audiences (e.g., new players) instead of the whole player base.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462): Add a config before creating a targeted experiment; targeted experiments require an existing config.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462): Order conditional rules carefully: rules are evaluated top to bottom and the first matching rule wins.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462): Use Conditional Configs to serve different values for the same key (e.g., lower boss health for new players) without publishing separate configs.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/evolving-experiments-and-analytics-segmentation-experiment-targeting/4828462): Watch playtime, ARPU and payer conversion during the first 24 hours of an experiment; early harm alerts fire if one drops below a catastrophic threshold.
- 2026-08-25 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188): Redesign mechanics rather than delete them; redesigned games are re-reviewed for Kids and Select acceptance without resetting Engaged Player criteria.
- 2026-08-28 Roblox DevForum [page](https://devforum.roblox.com/t/x/4836039): Use Experiments targeting, segmentation, and conditional configs to serve different values by player type; early harm detection flags metric impact early.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/making-publishing-easier-our-vision-and-whats-coming/4865780): Once Simplified publishing flow ships, answer the single 16+ question instead of the full questionnaire if your game has no restricted content.
- 2026-09-27 janisjanis01 [6:27](https://youtu.be/WJpNCB5J9bg?t=387): Run A/B tests on thumbnails; the previous owner had none running, which was a missed opportunity.
- 2026-09-27 Roblox DevForum [page](https://devforum.roblox.com/t/ab-testing-experience-titles-together-with-thumbnails/4900092): Test title and thumbnail as combined pairs, not separately; a thumbnail's CTR can change depending on the title shown beside it.
- 2026-10-01 Roblox DevForum [page](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734): Use early harm detection only to decide whether to stop an experiment; do not make launch decisions from first-24-hour results.
- 2026-10-01 Roblox DevForum [page](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734): Wait for daily results and full experiment duration before rolling out a variant; early novelty effects can make results swing.
- 2026-10-01 Roblox DevForum [page](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734): Enroll at least 10,000 players across variant and control so harm detection is reliable; set minimum detectable effect to size the rollout.
- 2026-10-01 Roblox DevForum [page](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734): If SRM alert appears in Results tab, stop and restart the experiment because results are unreliable.
- 2026-10-01 Roblox DevForum [page](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734): Set up a webhook to forward early harm notifications to your own monitoring tools, optionally.
- 2026-10-02 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-september-28%E2%80%93october-2-2026/4910267): Use Early Harm Detection in experiments: for the first 24 hours you can watch Playtime, payer conversion rate, and ARPU updated every 5 minutes to catch regressions early.
- 2026-10-20 Roblox DevForum [page](https://devforum.roblox.com/t/home-thumbnail-a-b-test/4947121): Re-pull analytics several days after the fact so values are settled before comparing thumbnail test results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/configs): Publish with GradualRollout (15-minute rollout) instead of Immediate when changing live gameplay values, to limit blast radius.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Exactly one variant must have isBaseline true; the productType discriminator must match the populated configuration block (inGameConfigExperimentConfiguration or matchmakingExperimentConfiguration).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Experiment configuration becomes immutable once started or scheduled; edit duration, rollout and variants while still in draft.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Wait at least 24 hours after starting an experiment before pulling /stats diagnostics.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Check isSrmDetected in stats; a true value signals sample ratio mismatch, so the split may be unreliable.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Omit variantId when calling :complete to stop without a winner; the config reverts to its previous value.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/experiments): Pick a goal metric matching the hypothesis, e.g. DAY_1_RETENTION for a boss-health change, and keep the test tied to it.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores): Use configs for feature flags and tunable values (enemy health, weapon damage, item prices, event toggles) so you can change them live without restarting servers.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/analytics/metrics): Use ThumbnailWinningSegments to see which audience segments a thumbnail performs best with before choosing a creative.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/developer/planning-for-educational-settings): Test games on low-end devices such as Chromebooks, not just high-end PCs, since classrooms commonly use them.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten): Publishing a config draft is irreversible except by restoring a previous version; verify the draft with GET before POST publish.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/artist/test-and-save): Playtest often using Test or Test Here so your avatar spawns; Run skips avatar insertion, which blocks testing in-game VFX interactions.
- 2026-10-30 Roblox Creators [13:45](https://youtu.be/gy_fAtIkqfo?t=825): Iterate onboarding in small steps while spending on ads; each change retained a bit more, and the algorithm picked the game up around day 7-8.
- 2026-10-30 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/rewarded-video-optimization): Test reward value against the perceived cost of watching when impressions per DAU is low.

Index: [[README]] | Master: [[master-playbook]]
