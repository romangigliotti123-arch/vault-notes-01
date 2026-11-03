---
title: "How to Make an OFFLINE PROGRESSION System in Roblox"
url: https://youtu.be/Gk-iTN8Ru_Q
creator: BloxxedDev
official: false
advice_density: medium
date: 2025-06-07
views: 2955
transcript: auto-captions
confidence: medium
tags: [roblox, bloxxeddev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Make an OFFLINE PROGRESSION System in Roblox

[Watch](https://youtu.be/Gk-iTN8Ru_Q) | BloxxedDev | 2,955 views | 2025-06-07

## Summary
Tutorial showing how to build an offline-progression plant-growing system in Roblox (Grow Garden-style). Plants keep growing while players are offline; state is saved to a DataStore and growth is calculated from elapsed time on rejoin. Covers growth-rate/height config and color-by-growth tweaks.

## Tips
- [1:15](https://youtu.be/Gk-iTN8Ru_Q?t=75) **[[data-persistence]]** Store each planted item's plant timestamp in DataStore so growth can be computed from elapsed time on rejoin instead of simulating while offline.
- [1:15](https://youtu.be/Gk-iTN8Ru_Q?t=75) **[[core-loops-and-game-design]]** Expose growth speed, max height and base height as top-of-script constants so you can tune the growth feel without rewriting logic.
- [2:37](https://youtu.be/Gk-iTN8Ru_Q?t=157) **[[data-persistence]]** Keep all live player data in one central table and route saves through shared core functions to keep the leave/rejoin logic in one place.
- [3:25](https://youtu.be/Gk-iTN8Ru_Q?t=205) **[[building-art-and-assets]]** Drive visual state (color) from growth progress with a single base color plus an impact multiplier, so one parameter controls how much growth changes appearance.

## Numbers
- [0:00](https://youtu.be/Gk-iTN8Ru_Q?t=0) Growth rate constant: **0.2** (Example growth speed value set at top of script)
- [1:15](https://youtu.be/Gk-iTN8Ru_Q?t=75) Max height: **2** (Example max growth height in script config)

## Games
- **Grow Garden** [0:00](https://youtu.be/Gk-iTN8Ru_Q?t=0): Popular for online growing mechanics; the video recreates a similar game with offline progression.

## Tools
Roblox Studio, Luau, DataStoreService

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[data-persistence]]

Back to [[BloxxedDev - How to make successful Roblox games]]
