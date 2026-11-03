---
title: "Simple pathfinding ai"
url: https://devforum.roblox.com/t/simple-pathfinding-ai/1815347
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-05-29
views: 101
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Simple pathfinding ai

[Open](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) | Roblox DevForum | 101 views | 2022-05-29

## Summary
DevForum tutorial on building a simple pathfinding NPC in Roblox Luau. Covers finding the nearest player character, computing paths with PathfindingService (CreatePath/ComputeAsync), walking waypoints with MoveTo and jumping on Jump actions, and re-pathing every Heartbeat toward a predicted target position. Author notes the twitch comes from the 7-stud lead offset.

## Tips
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[physics-pathfinding-and-npc-ai]]** Set the NPC's PrimaryPart network owner to nil (SetNetworkOwner(nil)) so the server controls NPC movement instead of a client.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[physics-pathfinding-and-npc-ai]]** Compute paths with PathfindingService:CreatePath() then path:ComputeAsync(start, destination); walk the result from path:GetWaypoints().
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[physics-pathfinding-and-npc-ai]]** When a waypoint's Action is Enum.PathWaypointAction.Jump, set humanoid.Jump = true before calling MoveTo on that waypoint.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[physics-pathfinding-and-npc-ai]]** Wait on humanoid.MoveToFinished between waypoints so each step completes before the next MoveTo.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[scripting-and-performance]]** Re-path inside RunService.Heartbeat only if needed; the author re-computes every frame, which is simple but costly. Consider throttling path recomputation.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[physics-pathfinding-and-npc-ai]]** Predicting target position by adding HumanoidRootPart.Velocity.Unit * 7 causes visible twitching; tune the lead distance (the author's 7 studs) or drop it.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[combat-and-gameplay-systems]]** Check target.Humanoid.Health > 0 before following a target so the NPC stops chasing dead characters.
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) **[[client-server-and-remotes]]** Use WaitForChild on HumanoidRootPart rather than assuming it exists when reading a character's position, to avoid errors during spawn.

## Numbers
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) Max target search distance: **5000 studs (author's default maxDistance)** (Initial distance cap in findTarget loop)
- [page](https://devforum.roblox.com/t/simple-pathfinding-ai/1815347) Predictive lead offset: **7 studs (Velocity.Unit * 7)** (Author says to tune this; causes twitch at this value)

## Tools
PathfindingService, RunService, Humanoid

## He points to
- Roblox Creator Hub: Character Pathfinding
- Roblox Creator Hub: RunService

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
