---
title: "Find Terrain Height with Ray Casting | Roblox Studio"
url: https://youtu.be/mrmB0hQGCXE
creator: SimTek Game Development
official: false
advice_density: medium
date: 2022-12-10
views: 1880
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Find Terrain Height with Ray Casting | Roblox Studio

[Watch](https://youtu.be/mrmB0hQGCXE) | SimTekGameDevelopment | 1,880 views | 2022-12-10

## Summary
Shows how to place parts on uneven Roblox terrain by randomly picking X/Z, then using workspace:Raycast from high above downward to find the terrain Y and offsetting the pickup 3 studs above it. Covers cloning from ServerStorage in a server script.

## Tips
- [4:52](https://youtu.be/mrmB0hQGCXE?t=292) **[[common-mistakes]]** Don't hard-code Y positions for terrain-placed objects; terrain height changes and hard-coded values break silently.
- [5:34](https://youtu.be/mrmB0hQGCXE?t=334) **[[scripting-and-performance]]** Use workspace:Raycast from above the map (e.g. Y=300) straight down to find ground height instead of hard-coded Y values.
- [6:58](https://youtu.be/mrmB0hQGCXE?t=418) **[[scripting-and-performance]]** Pass RaycastParams (or nil for defaults) as third raycast argument; use ignore lists to skip water or other non-ground objects.
- [6:58](https://youtu.be/mrmB0hQGCXE?t=418) **[[scripting-and-performance]]** Always check that the raycast returned a result, since it can miss (e.g. off the edge of the map).
- [7:40](https://youtu.be/mrmB0hQGCXE?t=460) **[[scripting-and-performance]]** Return the full hit position from a cast function so callers get X, Y, Z and can offset Y as needed.
- [2:03](https://youtu.be/mrmB0hQGCXE?t=123) **[[building-and-level-design]]** Keep template parts in ServerStorage and clone them at runtime to place many copies without polluting the workspace.

## Numbers
- [2:03](https://youtu.be/mrmB0hQGCXE?t=123) Pickups placed: **500 clones at random X/Z in a ±500 stud area** (Tutorial example spawning loop)
- [5:34](https://youtu.be/mrmB0hQGCXE?t=334) Raycast origin height: **300 studs above; map max height 256 studs** (Ray starts above highest terrain point)
- [6:16](https://youtu.be/mrmB0hQGCXE?t=376) Raycast length: **from Y=300 down to Y=-100** (Stop point 100 studs below origin)
- [7:40](https://youtu.be/mrmB0hQGCXE?t=460) Pickup offset above ground: **3 studs** (Added to raycast hit Y)

## Tools
Roblox Studio, workspace:Raycast, Random.new, ServerStorage, ServerScriptService

## Topics
[[building-and-level-design]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
