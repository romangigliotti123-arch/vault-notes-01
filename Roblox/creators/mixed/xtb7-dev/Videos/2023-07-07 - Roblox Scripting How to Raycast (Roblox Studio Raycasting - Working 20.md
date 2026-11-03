---
title: "Roblox Scripting: How to Raycast (Roblox Studio Raycasting - Working 2023)"
url: https://youtu.be/WfZhGsivpBM
creator: XTB7
official: false
advice_density: medium
date: 2023-07-07
views: 1311
transcript: auto-captions
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Roblox Scripting: How to Raycast (Roblox Studio Raycasting - Working 2023)

[Watch](https://youtu.be/WfZhGsivpBM) | xtb7-dev | 1,311 views | 2023-07-07

## Summary
Beginner Roblox Studio raycasting tutorial: how to call workspace:Raycast with origin and direction (destination minus origin), read the RaycastResult, recolor the hit part, and filter results with RaycastParams (FilterType Exclude/Include, FilterDescendantsInstances, RespectCanCollide, CanQuery). Prerequisite for gun systems.

## Tips
- [0:00](https://youtu.be/WfZhGsivpBM?t=0) **[[scripting-and-performance]]** Always check that Raycast returned a result before indexing it; an unsuccessful raycast returns nil and will error otherwise.
- [1:22](https://youtu.be/WfZhGsivpBM?t=82) **[[scripting-and-performance]]** Raycast direction must be destination minus origin (target position - origin), not the target position itself.
- [5:30](https://youtu.be/WfZhGsivpBM?t=330) **[[scripting-and-performance]]** Use RaycastParams FilterDescendantsInstances with Exclude to ignore parts; be careful not to filter out things the ray should hit.
- [7:33](https://youtu.be/WfZhGsivpBM?t=453) **[[scripting-and-performance]]** Set CanQuery to false on a part to make raycasts ignore it; simpler than using RaycastParams RespectCanCollide.
- [4:06](https://youtu.be/WfZhGsivpBM?t=246) **[[combat-and-gameplay-systems]]** Raycasting is the basis for weapon hit detection: the hit part's ancestor Humanoid can be found to remove health.

## Numbers
- [1:22](https://youtu.be/WfZhGsivpBM?t=82) Example direction calculation: **destination (0.5, 11, 12.5)... result (-12, -1) from origin minus target example** (Worked example from tutorial; distance result is approximate, round it)

## Tools
Roblox Studio, Workspace:Raycast, RaycastParams, RaycastResult

## He points to
- Roblox Creator documentation (raycasting), linked in video description

## Topics
[[combat-and-gameplay-systems]] [[scripting-and-performance]]

Back to [[xtb7-dev - How to make successful Roblox games]]
