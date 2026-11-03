---
title: "Docs: matchmaking / scoring"
url: https://create.roblox.com/docs/matchmaking/scoring.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: matchmaking / scoring

[Open](https://create.roblox.com/docs/matchmaking/scoring.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on server scoring for matchmaking. Explains the weighted-sum server score (attributes → signals → weights), categorical vs numerical attributes, normalization with clamping, and the default configuration weights. Friends weight outweighs all other signals combined, so friend-containing servers are always preferred when available.

## Tips
- [page](https://create.roblox.com/docs/matchmaking/scoring) **[[matchmaking-and-teleport]]** Default matchmaking config gives Friends weight 15, more than all other default signals combined, so joiners always land with friends or same-IP players when available.
- [page](https://create.roblox.com/docs/matchmaking/scoring) **[[matchmaking-and-teleport]]** Set a signal's weight to 0 to exclude it from scoring. Signal weights cannot be negative.
- [page](https://create.roblox.com/docs/matchmaking/scoring) **[[matchmaking-and-teleport]]** Only relative weight magnitudes matter. Scale all weights together and the server ranking does not change.
- [page](https://create.roblox.com/docs/matchmaking/scoring) **[[matchmaking-and-teleport]]** Choose a normalizing factor per numerical signal. Smaller factors amplify small differences; values beyond the factor clamp to the worst score.
- [page](https://create.roblox.com/docs/matchmaking/scoring) **[[matchmaking-and-teleport]]** Use a weight ratio to set priority: Occupancy at 5x Friends outranks Friends, while 1.5x does not, in the docs' example.

## Numbers
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Friends signal weight: **15** (Roblox default matchmaking configuration)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Latency weight: **3** (Roblox default matchmaking configuration)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Text Chat weight: **3** (Roblox default matchmaking configuration)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Occupancy / Play History / Language weight: **2 each** (Roblox default matchmaking configuration)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Age / Voice Chat weight: **1 each** (Roblox default matchmaking configuration)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Default Device Type weight: **0** (Exists but ignored by default)
- [page](https://create.roblox.com/docs/matchmaking/scoring) Age signal normalizing factor example: **25** (Age difference of 25+ years scores 0; 12-year difference scores 0.52)

## Tools
Roblox matchmaking configuration (custom signals, custom attributes)

## He points to
- Roblox docs: Existing attributes
- Roblox docs: Custom attributes
- Roblox docs: Existing signals
- Roblox docs: Custom signals

## Topics
[[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
