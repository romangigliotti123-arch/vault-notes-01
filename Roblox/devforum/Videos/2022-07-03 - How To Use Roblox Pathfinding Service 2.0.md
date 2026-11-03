---
title: "How To Use Roblox Pathfinding Service 2.0"
url: https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779
creator: Roblox DevForum
official: false
advice_density: high
date: 2022-07-03
views: 165
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How To Use Roblox Pathfinding Service 2.0

[Open](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) | Roblox DevForum | 165 views | 2022-07-03

## Summary
Step-by-step scripting tutorial for Roblox PathfindingService: computing paths with retries, following waypoints via MoveToFinished, handling Path.Blocked, yielding, cleaning up connections, animation setup, and AgentParameters/PathfindingModifiers/PathfindingLink for custom path costs.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[scripting-and-performance]]** Wrap path:ComputeAsync in pcall with a retry loop (MAX_RETRIES=5, RETRY_COOLDOWN=5s) since it makes network calls and can fail.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[scripting-and-performance]]** Call pcall(path.ComputeAsync, path, start, goal) rather than wrapping in an anonymous function, to avoid unnecessary closure creation.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[scripting-and-performance]]** Follow waypoints with humanoid.MoveToFinished rather than a for loop; the event fires per waypoint and lets you handle blocking and timeouts.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[common-mistakes]]** Unanchor every BasePart in an NPC model, otherwise anchored parts stop it from walking.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[client-server-and-remotes]]** Disconnect MoveToFinished and Path.Blocked connections and set variables to nil when a path finishes to avoid memory leaks.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[combat-and-gameplay-systems]]** Handle Path.Blocked by recomputing the path only when the blocked waypoint index is ahead of the current waypoint.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[genre-mechanics]]** Use the Animate script copied from a player character (or the uploaded Animate-R15/R6 scripts) under the NPC humanoid so it plays idle and run animations; convert to server script.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Set AgentRadius above default 2 to keep a minimum separation of (value - 2) studs from obstacles.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Set Costs multipliers below 1 (e.g. Metal = 0.1) to make pathfinding prefer those materials; above 1 to avoid them.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Use a Costs value of math.huge on a PathfindingModifier label to exclude a region from paths entirely.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Use a PathfindingModifier with PassThrough enabled (non-collidable, transparent part) to mark traversable regions such as hinged doors without setting a cost.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Use PathfindingLink with attachments to make humanoids traverse gaps (e.g. jumps) that ComputeAsync cannot find on its own, and trigger custom events on those waypoints.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[physics-pathfinding-and-npc-ai]]** Setting WaypointSpacing to math.huge yields the fewest waypoints for the shortest path, but it breaks the MoveToFinished reached-within-8s check.
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) **[[optimization-and-streaming]]** Old pathfinding tutorial code was inefficient and buggy; prefer the revamped pattern with proper connection cleanup.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) ComputeAsync retry limit: **MAX_RETRIES = 5, RETRY_COOLDOWN = 5 seconds** (Tutorial's pcall retry constants for path computation)
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) Default AgentRadius / AgentHeight / WaypointSpacing: **2 / 5 / 4** (Roblox rig defaults from AgentParameters)
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) Waypoint reach timeout: **8 seconds** (MoveToFinished reached check window used in tutorial)
- [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779) AgentRadius separation formula: **Separation = AgentRadius - 2 studs** (Minimum separation from obstacles)

## Tools
PathfindingService, Rig Builder plugin, Roblox Studio, Animate scripts (R15/R6)

## He points to
- Roblox Developer Hub PathfindingService docs
- Hexcede (cost multiplier explanation)
- Memory leak tutorial linked by author

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[genre-mechanics]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
