---
title: "Path Finding For NPCs - Handling Blocked Paths In Roblox"
url: https://youtu.be/lJktfRT2pbg
creator: SimTek Game Development
official: false
advice_density: medium
date: 2021-07-04
views: 7383
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Path Finding For NPCs - Handling Blocked Paths In Roblox

[Watch](https://youtu.be/lJktfRT2pbg) | SimTekGameDevelopment | 7,383 views | 2021-07-04

## Summary
Tutorial on making Roblox NPCs path dynamically with PathfindingService: computing waypoints with ComputeAsync, walking them via MoveToFinished, jumping on Jump waypoints, and recomputing the path when the Blocked event fires from newly appearing walls. Ends with the no-path-available case.

## Tips
- [5:32](https://youtu.be/lJktfRT2pbg?t=332) **[[scripting-and-performance]]** Compute waypoints dynamically with PathfindingService:CreatePath and ComputeAsync instead of hardcoding waypoint folders; hardcoded points break when the map changes.
- [5:32](https://youtu.be/lJktfRT2pbg?t=332) **[[scripting-and-performance]]** Check path.Status == Enum.PathStatus.Success before reading waypoints; otherwise handle the 'no path' case to avoid nil errors when the NPC is boxed in.
- [7:37](https://youtu.be/lJktfRT2pbg?t=457) **[[scripting-and-performance]]** Drive movement with Humanoid:MoveTo one waypoint at a time, advancing the index in MoveToFinished only when reached is true.
- [8:58](https://youtu.be/lJktfRT2pbg?t=538) **[[scripting-and-performance]]** Honour waypoint.Action == Enum.PathWaypointAction.Jump by calling Humanoid.Jump; the default action is walk.
- [14:46](https://youtu.be/lJktfRT2pbg?t=886) **[[scripting-and-performance]]** Connect path.Blocked and recompute the path only if the blocked waypoint index is ahead of the current index; ignore blockages behind the NPC.
- [11:00](https://youtu.be/lJktfRT2pbg?t=660) **[[building-and-level-design]]** Test dynamic obstacles with a trigger pad that makes a hidden wall appear (Transparency 1, CanCollide false, then toggled on) to verify re-routing works.
- [18:13](https://youtu.be/lJktfRT2pbg?t=1093) **[[genre-mechanics]]** Pathfinding jump only clears about 3.5 studs in the speaker's test even though the character can jump higher; keep jumpable obstacles low or expect NPCs to get stuck.

## Numbers
- [18:13](https://youtu.be/lJktfRT2pbg?t=1093) Jump obstacle height: **~3.5 studs cleared by pathfinding jump in speaker's test (wall 11.5 studs high was not cleared)** (Speaker's own test with Roblox pathfinding jump)

## Tools
Roblox Studio, PathfindingService, Luau, Output window

## He points to
- Roblox PathfindingService documentation (implied via Blocked and MoveToFinished events)

## Topics
[[building-and-level-design]] [[genre-mechanics]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
