---
title: "Docs: production / recommendation"
url: https://create.roblox.com/docs/production/recommendation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / recommendation

[Open](https://create.roblox.com/docs/production/recommendation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Recommendation Service docs: how to register items, log impressions once per session, log quality play actions only (e.g. >60s sessions) using Enum.RecommendationActionType.Play, fetch via MaximizePlays config, and monitor metrics in Creator Hub under Engagement > Recommendation Service.

## Tips
- [page](https://create.roblox.com/docs/production/recommendation) **[[social-features-and-virality]]** Register recommendation items as soon as they are created so the recommendation pool stays fresh.
- [page](https://create.roblox.com/docs/production/recommendation) **[[discovery-algorithm]]** Log impressions only once per session per item; logging every appearance creates noisy data that interferes with the model.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** Pass the itemId returned by RegisterItemAsync or GenerateItemListAsync to LogImpressionEvent, not a raw referenceId string.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** For static cards without video, set impression Duration to 1 to get clean 'user viewed this item' data.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** Only log play actions when a user passes a satisfaction threshold (e.g. over 60 seconds), not on every Play click.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** Use Enum.RecommendationActionType.Play for play-session actions; other enums won't register correctly with MaximizePlays.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** Never log plays from Search, random picks, or past plays as recommendation actions, and never use dummy tracing IDs; the model expects realistic impression-to-play ratios.
- [page](https://create.roblox.com/docs/production/recommendation) **[[discovery-algorithm]]** Use the MaximizePlays config over MaximizeTimeSpent when fetching recommendations to optimise for quality play, not just time spent.
- [page](https://create.roblox.com/docs/production/recommendation) **[[analytics-metrics]]** Track Total Actions, Total Unique Users, Average Items Impressed per User, and Average Time Spent per User in Creator Hub Recommendation Service analytics.

## Numbers
- [page](https://create.roblox.com/docs/production/recommendation) Quality play session threshold: **> 60 seconds (example)** (Example threshold before logging a LogActionEvent play)
- [page](https://create.roblox.com/docs/production/recommendation) Impression Duration for static cards: **1** (Recommended value when not using video)

## Tools
Roblox Recommendation Service API, Creator Hub Recommendation Service analytics

## He points to
- Class.RecommendationService.RegisterItemAsync
- Class.RecommendationService.LogImpressionEvent
- Class.RecommendationService.LogActionEvent
- Class.RecommendationService.GenerateItemListAsync

## Quotes
- [page](https://create.roblox.com/docs/production/recommendation) "Log the impression only once per session for a specific item. Do not log every time the item appears."
- [page](https://create.roblox.com/docs/production/recommendation) "The model expects a realistic ratio. If you serve 1 impression but log 10 plays from external traffic, you confuse the training data."

## Topics
[[analytics-metrics]] [[discovery-algorithm]] [[social-features-and-virality]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
