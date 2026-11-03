---
title: "I Tried Pushing Roblox To It's Absolute Limits"
url: https://youtu.be/_E1stqb2fNw
creator: Roox4
official: false
advice_density: low
date: 2024-12-06
views: 92413
transcript: auto-captions
confidence: medium
tags: [roblox, roox4official, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I Tried Pushing Roblox To It's Absolute Limits

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/_E1stqb2fNw) | Roox4Official | 92,413 views | 2024-12-06

## Summary
Experiment pushing player position far from the world origin in Roblox. Teleports cap near 1M studs, client-only parts reach ~20M, scaling objects up reduces glitches, and the creator reaches about 2B studs. Raycasts are limited to 15,000 studs. Entertainment-focused, little transferable advice.

## Tips
- [0:40](https://youtu.be/_E1stqb2fNw?t=40) **[[physics-pathfinding-and-npc-ai]]** Server-side teleports beyond about 1,000,000 studs snap back to 1M; client-created parts can still exist farther, but this is an unsupported edge case.
- [3:26](https://youtu.be/_E1stqb2fNw?t=206) **[[building-and-level-design]]** Scale up objects when working far from origin; the creator found larger parts glitch less than small ones, making the game more playable.
- [6:14](https://youtu.be/_E1stqb2fNw?t=374) **[[scripting-and-performance]]** Raycasts have a 15,000-stud max range; at extreme distances, chain multiple raycasts to hit nearby targets.
- [6:14](https://youtu.be/_E1stqb2fNw?t=374) **[[building-and-level-design]]** Parts have a maximum size limit; building large walls may require stacking many parts instead of resizing one.

## Numbers
- [0:40](https://youtu.be/_E1stqb2fNw?t=40) Teleport cap: **1,000,000 studs** (Server teleports beyond this snap back to 1M studs)
- [2:45](https://youtu.be/_E1stqb2fNw?t=165) Max reached via client-created parts: **20,000,000 studs** (Game barely playable; camera stutter, movement issues)
- [4:09](https://youtu.be/_E1stqb2fNw?t=249) Playable distance after scaling up: **2,000,000,000 studs** (Game looked decent at 500M-1B; 5B killed player instantly)
- [4:52](https://youtu.be/_E1stqb2fNw?t=292) Max scale factor observed: **1,000x** (Creator concluded scaling only worked to about 1,000)

## Tools
Roblox Studio

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roox4Official - How to make successful Roblox games]]
