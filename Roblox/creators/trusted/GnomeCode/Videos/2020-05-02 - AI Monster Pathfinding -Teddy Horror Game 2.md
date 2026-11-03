---
title: "AI Monster Pathfinding -Teddy Horror Game #2"
url: https://youtu.be/uF-BGGv6otQ
creator: GnomeCode
official: false
advice_density: medium
date: 2020-05-02
views: 504624
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# AI Monster Pathfinding -Teddy Horror Game #2

[Watch](https://youtu.be/uF-BGGv6otQ) | GnomeCode | 504,624 views | 2020-05-02

## Summary
Part 2 of a Roblox horror game tutorial series (Teddy). Builds a monster AI: moves a character to a destination with Humanoid:MoveTo, loops patrol points, uses PathfindingService with ComputePath and agent parameters (height, radius, CanJump) to route around walls, and randomly patrols waypoints from a folder. Player detection is deferred to the next episode.

## Tips
- [0:52](https://youtu.be/uF-BGGv6otQ?t=52) **[[ai-and-tools]]** Copy the default Animate LocalScript from the character into a server Script so NPC animations play when no player controls it.
- [5:39](https://youtu.be/uF-BGGv6otQ?t=339) **[[physics-pathfinding-and-npc-ai]]** Use PathfindingService:CreatePath and ComputeAsync instead of Humanoid:MoveTo directly, so NPCs route around walls instead of getting stuck.
- [10:24](https://youtu.be/uF-BGGv6otQ?t=624) **[[physics-pathfinding-and-npc-ai]]** Set AgentHeight, AgentRadius and AgentCanJump in CreatePath to match your NPC's size; default agent settings make big rigs snag on walls.
- [11:46](https://youtu.be/uF-BGGv6otQ?t=706) **[[physics-pathfinding-and-npc-ai]]** Recompute the path on each move; pathfinding is dynamic so NPCs take the new shortest route when obstacles move.
- [12:48](https://youtu.be/uF-BGGv6otQ?t=768) **[[physics-pathfinding-and-npc-ai]]** Store patrol points as Parts in a Waypoints folder and pick random children with math.random(1, #waypoints) for simple random patrol.
- [4:42](https://youtu.be/uF-BGGv6otQ?t=282) **[[scripting-and-performance]]** Wait on Humanoid.MoveToFinished before issuing the next move; wrap loops in a wait so the while loop does not spin unbounded.
- [7:46](https://youtu.be/uF-BGGv6otQ?t=466) **[[code-architecture-and-frameworks]]** Split path computation (getPath) from movement (walkTo) into separate functions so each can be reused or changed independently.
- [15:55](https://youtu.be/uF-BGGv6otQ?t=955) **[[physics-pathfinding-and-npc-ai]]** Patrol AI alone does not detect players; add a line-of-sight or range check to trigger chase, which the speaker defers to the next part.

## Numbers
- [11:04](https://youtu.be/uF-BGGv6otQ?t=664) AgentHeight: **15 studs** (Monster height measured in-world, used for pathfinding agent)
- [11:04](https://youtu.be/uF-BGGv6otQ?t=664) AgentRadius: **4 studs** (Half of ~8-stud diameter monster width)
- [14:54](https://youtu.be/uF-BGGv6otQ?t=894) Patrol pause: **2 seconds** (Wait between waypoints in patrol example)
- [0:00](https://youtu.be/uF-BGGv6otQ?t=0) Subscribers: **1000** (Channel milestone mentioned at start of video)

## Games
- **Piggy** [0:43](https://youtu.be/uF-BGGv6otQ?t=43): Referenced as the game this series is not a remake of; Teddy is an original horror concept.
- **Missing Granny** [0:43](https://youtu.be/uF-BGGv6otQ?t=43): Referenced as a comparison; Teddy is positioned as distinct from it.

## Tools
Roblox Studio, Luau, PathfindingService, Humanoid, Animate script

## Topics
[[ai-and-tools]] [[code-architecture-and-frameworks]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[GnomeCode - How to make successful Roblox games]]
