---
title: "Docs: matchmaking / attributes-and-signals"
url: https://create.roblox.com/docs/matchmaking/attributes-and-signals.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: matchmaking / attributes-and-signals

[Open](https://create.roblox.com/docs/matchmaking/attributes-and-signals.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox matchmaking docs defining default attributes and signals (age, device, friends, latency, language, occupancy, play history, voice/text chat) and how to build custom numerical and categorical signals from player/server attributes using DataStore and MatchmakingService.

## Tips
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[matchmaking-and-teleport]]** Use custom attributes plus custom signals to matchmake on data Roblox doesn't include by default, such as skill level or guild.
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[data-persistence]]** Store persistent player attributes (level, Elo) in DataStores; store non-persistent server attributes (game mode, level) via MatchmakingService.
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[matchmaking-and-teleport]]** Use MatchmakingService:InitializeServerAttributesForStudio to set up server attribute schema for testing in Studio.
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[matchmaking-and-teleport]]** Numerical signals score by difference from server average; differences beyond the max relevant difference score 0.
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[matchmaking-and-teleport]]** Categorical signals use Clustering (maximize same-attribute ratio) or Diversifying (maximize different-attribute ratio) depending on the design goal.
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) **[[matchmaking-and-teleport]]** Voice Chat signal weight is automatically 0 if the place has voice chat disabled.

## Numbers
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) Age signal max relevant difference: **25 years**
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) Latency signal max relevant delta ping: **100 ms**
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) Play History max relevant difference: **4.6 (log10 minutes over past 28 days)**
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) Friends signal max relevant value: **1 (preferred player present)**
- [page](https://create.roblox.com/docs/matchmaking/attributes-and-signals) Custom numerical signal max relevant difference example: **1000 default cutoff; example 1500**

## Tools
MatchmakingService, DataStoreService

## He points to
- Roblox docs: Create a custom attribute
- Roblox docs: Create a custom signal
- Roblox docs: Existing attributes
- Roblox docs: Existing signals

## Topics
[[data-persistence]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
