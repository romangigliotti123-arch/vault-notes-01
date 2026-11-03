---
title: "NPC AI: Advanced PathFinding - Run, Climb, Swim"
url: https://youtu.be/tjwI4b2ZRZk
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-01-28
views: 33217
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# NPC AI: Advanced PathFinding - Run, Climb, Swim

[Watch](https://youtu.be/tjwI4b2ZRZk) | SimTekGameDevelopment | 33,217 views | 2023-01-28

## Summary
Tutorial on Roblox NPC pathfinding using PathfindingService: rigging an R15 NPC, copying the Animate script to a server Script, computing and following waypoints with jump handling, recomputing on blocked paths, and adding PathfindingLinks for ladders. Notes that swimming needs no link.

## Tips
- [3:12](https://youtu.be/tjwI4b2ZRZk?t=192) **[[physics-pathfinding-and-npc-ai]]** Copy the Animate LocalScript into a server Script under the NPC, since NPCs are server entities and cannot use LocalScripts.
- [3:12](https://youtu.be/tjwI4b2ZRZk?t=192) **[[common-mistakes]]** Delete the setup emote chat hook block in the copied Animate script; it causes output errors on NPCs because it is player-specific.
- [0:54](https://youtu.be/tjwI4b2ZRZk?t=54) **[[physics-pathfinding-and-npc-ai]]** Set the NPC's HumanoidRootPart Anchored to false so it can move; PathfindingService works with R6 or R15.
- [11:05](https://youtu.be/tjwI4b2ZRZk?t=665) **[[physics-pathfinding-and-npc-ai]]** Connect the Path Blocked event and only recompute when the blocked waypoint index is ahead of the current one, ignoring obstacles behind the NPC.
- [9:43](https://youtu.be/tjwI4b2ZRZk?t=583) **[[physics-pathfinding-and-npc-ai]]** Check each waypoint's Action for Enum.PathWaypointAction.Jump and set humanoid.Jump = true while moving to that waypoint.
- [14:47](https://youtu.be/tjwI4b2ZRZk?t=887) **[[physics-pathfinding-and-npc-ai]]** Check path status and handle non-Success results, since a climbable obstacle with no link otherwise leaves the NPC standing still with no error.
- [15:28](https://youtu.be/tjwI4b2ZRZk?t=928) **[[physics-pathfinding-and-npc-ai]]** Add two Attachments (bottom and top of a ladder) and a PathfindingLink between them, with bidirectional on, so the NPC can climb.
- [17:30](https://youtu.be/tjwI4b2ZRZk?t=1050) **[[physics-pathfinding-and-npc-ai]]** NPCs can swim without any extra setup; pathfinding routes them through water automatically.
- [12:26](https://youtu.be/tjwI4b2ZRZk?t=746) **[[development-process-and-speed]]** Build a simple test arena with a blocked path and a trigger plate to verify recomputation before adding real gameplay.

## Numbers
- [1:50](https://youtu.be/tjwI4b2ZRZk?t=110) Animate script length: **about 800 lines copied** (Default Animate script copied from player to NPC)

## Tools
PathfindingService, PathfindingLink, Animate script, Avatar Rig Builder, Roblox Studio toolbox

## Topics
[[common-mistakes]] [[development-process-and-speed]] [[physics-pathfinding-and-npc-ai]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
