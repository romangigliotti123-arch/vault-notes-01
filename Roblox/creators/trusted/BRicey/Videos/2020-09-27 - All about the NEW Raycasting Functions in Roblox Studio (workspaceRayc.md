---
title: "All about the NEW Raycasting Functions in Roblox Studio (workspace:Raycast())"
url: https://youtu.be/4fJBWFz9I-E
creator: B Ricey
official: false
advice_density: low
date: 2020-09-27
views: 30299
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# All about the NEW Raycasting Functions in Roblox Studio (workspace:Raycast())

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/4fJBWFz9I-E) | BRicey | 30,299 views | 2020-09-27

## Summary
Tutorial on Roblox's newer raycasting API: workspace:Raycast(origin, direction, optional RaycastParams), RaycastResult properties (Position, Instance, Normal, Material), and RaycastParams filtering (FilterDescendantsInstances, FilterType Blacklist/Whitelist, IgnoreWater, CollisionGroup). Notes the old FindPartOnRay family is deprecated.

## Tips
- [1:46](https://youtu.be/4fJBWFz9I-E?t=106) **[[scripting-and-performance]]** Use workspace:Raycast(origin, direction, params) instead of the deprecated FindPartOnRay family; pass origin and direction directly rather than building a Ray object.
- [4:02](https://youtu.be/4fJBWFz9I-E?t=242) **[[scripting-and-performance]]** Always check that the RaycastResult is non-nil before reading it, since a raycast into empty space returns nil.
- [8:37](https://youtu.be/4fJBWFz9I-E?t=517) **[[scripting-and-performance]]** Use RaycastParams.FilterType Blacklist or Whitelist with FilterDescendantsInstances to skip or restrict hit objects.
- [9:32](https://youtu.be/4fJBWFz9I-E?t=572) **[[scripting-and-performance]]** Use RaycastParams.CollisionGroup to control which parts rays hit; note rays can hit parts in groups that are set to collide with each other.

## Numbers
- [2:33](https://youtu.be/4fJBWFz9I-E?t=153) Raycast direction length: **10 studs in example; 100 studs used in later test** (Example ray length used in demo)

## Tools
Roblox Studio, workspace:Raycast(), RaycastParams, RaycastResult

## Topics
[[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
