---
title: "The ULTIMATE Guide to Pathfinding Links"
url: https://youtu.be/Om2vAKMW1Pw
creator: Crit
official: false
advice_density: medium
date: 2025-08-18
views: 3405
transcript: auto-captions
confidence: high
tags: [roblox, critdev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# The ULTIMATE Guide to Pathfinding Links

[Watch](https://youtu.be/Om2vAKMW1Pw) | CritDEV | 3,405 views | 2025-08-18

## Summary
Tutorial on customizing Roblox PathfindingService NPC traversal using PathfindingLink objects (attachments, bidirectional, labels) and the Forbidden pathfinding module. Shows a teleport link with a delay, then a reusable module-based manager for custom link handlers that return true to resume pathing.

## Tips
- [0:00](https://youtu.be/Om2vAKMW1Pw?t=0) **[[physics-pathfinding-and-npc-ai]]** Use PathfindingLinks when default pathing handles stairs poorly or when a route is otherwise unpathable (e.g. a wall you want NPCs to teleport over).
- [0:37](https://youtu.be/Om2vAKMW1Pw?t=37) **[[physics-pathfinding-and-npc-ai]]** Create a PathfindingLink with two attachments placed in two parts, enable Bidirectional unless one-way is intended, and set a Label to identify its behaviour.
- [2:11](https://youtu.be/Om2vAKMW1Pw?t=131) **[[physics-pathfinding-and-npc-ai]]** Assign the link-reached handler without parentheses (hooks.PathfindingLinkReached = fn) so the function is set, not called.
- [3:32](https://youtu.be/Om2vAKMW1Pw?t=212) **[[physics-pathfinding-and-npc-ai]]** Always return true from the PathfindingLinkReached handler after custom movement, otherwise pathfinding will not continue.
- [4:09](https://youtu.be/Om2vAKMW1Pw?t=249) **[[code-architecture-and-frameworks]]** Put each custom link handler in its own module script and dispatch from a single manager keyed by link label to keep the NPC script clean.
- [4:51](https://youtu.be/Om2vAKMW1Pw?t=291) **[[physics-pathfinding-and-npc-ai]]** Reset the NPC config to default before changing it, since it may have been altered elsewhere; enable visualization while debugging to see waypoints.

## Numbers
- [0:37](https://youtu.be/Om2vAKMW1Pw?t=37) Teleport delay in demo: **3 seconds** (Intentional wait after teleporting NPC over wall before resuming path)
- [3:32](https://youtu.be/Om2vAKMW1Pw?t=212) Custom wait in handler: **5 seconds** (Teleport-and-wait link handler in external module example)

## Tools
Forbidden (pathfinding module by Arman501, inserted into ReplicatedStorage), PathfindingLink, Roblox Studio

## He points to
- Forbidden pathfinding module (description by Arman501)

## Topics
[[code-architecture-and-frameworks]] [[physics-pathfinding-and-npc-ai]]

Back to [[CritDEV - How to make successful Roblox games]]
