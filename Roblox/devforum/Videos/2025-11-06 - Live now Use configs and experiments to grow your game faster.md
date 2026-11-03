---
title: "[Live now] Use configs and experiments to grow your game faster"
url: https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385
creator: Roblox DevForum
official: false
advice_density: high
date: 2025-11-06
views: 536
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Live now] Use configs and experiments to grow your game faster

[Open](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) | Roblox DevForum | 536 views | 2025-11-06

## Summary
Roblox announcement introducing Configs (real-time in-game value/feature toggles without server restarts, staged then published) and Experiments (in-experience and matchmaking A/B tests on retention, engagement, monetization). Covers creation, monitoring, limits, and experiment best practices.

## Tips
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Define a clear cause-and-effect hypothesis with expected metric direction and reasoning before running an experiment, e.g. grow D1 retention via onboarding change.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Check the minimum detectable effect (MDE) before running. MDE around ±100% means significance is unlikely; very low MDE (<0.01%) means a shorter test or less traffic works.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Games under 500 DAU likely need to grow their user base before running experiments; use qualitative feedback instead.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Wait for the full pre-defined experiment duration (at least two weeks suggested) before deciding; early swings can be novelty effects.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Only decide on statistically significant (shaded) metrics; treat non-significant changes as no change, even if the lift looks large.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Expect metric tradeoffs; weigh statistically significant positive vs negative signals and secondary metrics that shift with the primary goal.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[scripting-and-performance]]** Call GetValue for an experiment config key only when the feature is needed, since calling it enrolls the player immediately.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[scripting-and-performance]]** Group related config values into a JSON-type config to namespace keys and simplify management; add configs ahead of time.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Avoid running overlapping experiments on the same features; users can be enrolled in both and interaction effects can distort results.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[common-mistakes]]** Do not act on results that swing between significant and not significant in early days; fluctuations settle only as enrolled traffic grows.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Document setup, learnings, decisions and next steps for each experiment to build a body of knowledge.
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) **[[analytics-metrics]]** Test config changes in Studio before publishing; published changes reach all players within 5 minutes (or 15-minute rollout optionally).

## Numbers
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Minimum daily active users for experiments: **500 DAU (guidance)** (Below this, grow user base before experimenting)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Experiment results appear after start: **24-48 hours** (Metrics in Details and Results tabs)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Recommended minimum experiment duration: **at least 2 weeks** (Avoid novelty effects before deciding)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) MDE warning threshold (high): **±100%** (Significance unlikely at this MDE)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) MDE warning threshold (low): **<0.01%** (Shorter test or less traffic may suffice)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Config publish propagation: **within 5 minutes (or 15-minute rollout)** (Server receipt of new config values)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Active config limit: **1,000** (Maximum active configs at once)
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) Concurrent experiment limit: **10 in-game + 1 matchmaking** (Maximum active experiments at any time)

## Tools
Roblox Creator Hub (Configs and Experiments pages), Roblox Studio (Open Configs in File menu)

## He points to
- Roblox Configs and Experiments documentation
- RDC 2025 session on experiment best practices
- Upcoming Roblox webinar (2 PM PST, next week)

## Quotes
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) "Only access the config when you actually want to enroll a player. A player is added to the experiment the moment you call GetValue for the experiment key."
- [page](https://devforum.roblox.com/t/live-now-use-configs-and-experiments-to-grow-your-game-faster/4051385) "Early swings in metrics could just be novelty effects, so wait for your experiment duration to complete before making any decisions."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
