---
title: "Docs: resources / battle-royale / the-storm"
url: https://create.roblox.com/docs/resources/battle-royale/the-storm.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / the-storm

[Open](https://create.roblox.com/docs/resources/battle-royale/the-storm.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the battle-royale storm template: a shrinking cylindrical damage barrier built from thin rectangular parts, configured via MainConfiguration (map_offset, radius, time_before_start, debug_time_scale, and per-stage transition_length, wait_length, damage, move_scale, shrinkage_factor).

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) **[[building-and-level-design]]** Use map_offset in MainConfiguration to shift the storm's final center away from map center and steer players toward a chosen point.
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) **[[core-loops-and-game-design]]** Shrinking storm damage forces players closer together, which helps battle royale matches end in a reasonable time.
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) **[[development-process-and-speed]]** Set debug_time_scale above 1 to run storm stages faster when tuning stage timing.
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) **[[core-loops-and-game-design]]** Set move_scale to 0 so each stage's storm stays fully inside the previous stage's bounds, keeping shrink predictable.

## Numbers
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) Default storm radius: **6000** (Starting radius in storm table of MainConfiguration)
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) Time before storm starts: **120 s** (time_before_start default)
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) Number of stages: **10** (number_of_stages default; stage 0 is starting circle)
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) Stage 0 wait_length: **150 s** (Starting circle shown with no transition)
- [page](https://create.roblox.com/docs/resources/battle-royale/the-storm) Map size / offset example: **map_size 9800, map_offset (4900,0,4900)** (Example values: 2450*4 map size with offset)

## Tools
Roblox Studio, Luau

## He points to
- ServerScriptService/Core/ShrinkingBarrier
- ReplicatedStorage/Core/ShrinkingBarrierVisualization
- ReplicatedFirst/Configurations/MainConfiguration

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[development-process-and-speed]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
