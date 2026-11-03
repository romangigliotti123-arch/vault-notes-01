---
title: "Learn Raycasting in 7 minutes - Advanced Roblox Scripting"
url: https://youtu.be/Wl3mXFlRPo4
creator: GnomeCode
official: false
advice_density: low
date: 2022-12-22
views: 153390
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Learn Raycasting in 7 minutes - Advanced Roblox Scripting

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/Wl3mXFlRPo4) | GnomeCode | 153,390 views | 2022-12-22

## Summary
Beginner Luau tutorial on raycasting: using workspace:Raycast from one part toward another to test line of sight. Covers computing the direction vector, printing the result, recoloring hit parts, ignoring a semi-transparent window via RaycastParams with a Blacklist filter, and looping with task.wait(1) to color a target yellow when visible or red when hidden.

## Tips
- [1:34](https://youtu.be/Wl3mXFlRPo4?t=94) **[[scripting-and-performance]]** Raycast direction is target.Position minus origin.Position; Workspace:Raycast takes origin, direction, and optional RaycastParams.
- [5:27](https://youtu.be/Wl3mXFlRPo4?t=327) **[[scripting-and-performance]]** Use RaycastParams with FilterType Blacklist and FilterDescendantsInstances to ignore transparent parts like windows instead of hitting them.
- [5:27](https://youtu.be/Wl3mXFlRPo4?t=327) **[[optimization-and-streaming]]** Wrap raycast checks in a loop with task.wait(1) so they run once per second rather than every frame or in a tight infinite loop.

## Tools
Roblox Studio, Workspace:Raycast, RaycastParams, Output window

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[GnomeCode - How to make successful Roblox games]]
