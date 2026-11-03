---
title: "How to make a Tower Defense Game -  #1 Path Navigation"
url: https://youtu.be/DanjB0cTfw0
creator: GnomeCode
official: false
advice_density: medium
date: 2021-12-14
views: 2961618
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Tower Defense Game -  #1 Path Navigation

[Watch](https://youtu.be/DanjB0cTfw0) | GnomeCode | 2,961,618 views | 2021-12-14

## Summary
Beginner tutorial on making a tower defense enemy path in Roblox Studio. Uses a Toolbox zombie, numbered waypoint parts in a folder, and a Luau for-loop with Humanoid:MoveTo and MoveToFinished to walk the enemy through each waypoint in order.

## Tips
- [0:14](https://youtu.be/DanjB0cTfw0?t=14) **[[development-process-and-speed]]** Use a fixed path with manually placed waypoints for tower defense; it avoids building many invisible walls for PathfindingService.
- [3:27](https://youtu.be/DanjB0cTfw0?t=207) **[[development-process-and-speed]]** Organise path pieces and waypoints into separate folders in Workspace to keep the map manageable.
- [4:29](https://youtu.be/DanjB0cTfw0?t=269) **[[scripting-and-performance]]** Anchor waypoint parts, disable their collision and make them semi-transparent so enemies don't bump into them.
- [5:44](https://youtu.be/DanjB0cTfw0?t=344) **[[scripting-and-performance]]** Loop over waypoints with a numbered for-loop using waypoints:GetChildren() and #waypoints to drive movement.
- [6:24](https://youtu.be/DanjB0cTfw0?t=384) **[[scripting-and-performance]]** Call Humanoid:MoveTo then Humanoid.MoveToFinished:Wait() so each enemy reaches a waypoint before heading to the next.
- [7:05](https://youtu.be/DanjB0cTfw0?t=425) **[[testing-debugging-and-qa]]** Keep the Output window open while scripting; a MoveTo error (passing a Part instead of .Position) only shows there.

## Numbers
- [4:29](https://youtu.be/DanjB0cTfw0?t=269) waypoints: **12** (Numbered waypoints placed at each turn of the example path)

## Tools
Roblox Studio, Toolbox, Luau

## He points to
- PathfindingService

## Topics
[[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[GnomeCode - How to make successful Roblox games]]
