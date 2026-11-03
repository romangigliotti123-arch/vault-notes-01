---
title: "SCR's Signalling System - BTS² #03"
url: https://youtu.be/uYIE3IVmKY8
creator: Last Level Studios
official: false
advice_density: medium
date: 2020-08-24
views: 20948
transcript: auto-captions
confidence: high
tags: [roblox, lastlevelstudios, youtube-learn]
creator_trust: MIXED
creator_score: 5.5
---

> [!note] Trust: MIXED (credibility audit score 5.5): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# SCR's Signalling System - BTS² #03

[Watch](https://youtu.be/uYIE3IVmKY8) | LastLevelStudios | 20,948 views | 2020-08-24

## Summary
Behind-the-scenes walkthrough of Stepford County Railway (SCR) v1.6 signalling rewrite. Shows a custom Studio plugin for placing entry/exit sensors and signal aspects, explains block-based occupancy via a server-side in-block table instead of touching-parts collisions, manual signalling permission/state logic, and a centralised signal loop handling 900+ signals.

## Tips
- [1:20](https://youtu.be/uYIE3IVmKY8?t=80) **[[building-and-level-design]]** Use sensor parts (not unioned track bricks) for signal triggers so moving track means moving one part; object values pointing at unions break when you rebuild.
- [3:48](https://youtu.be/uYIE3IVmKY8?t=228) **[[physics-pathfinding-and-npc-ai]]** Put trains in a separate collision group from scenery and use CFrame/BodyMovers with raycasts for sensors to cut physics collision checks.
- [4:29](https://youtu.be/uYIE3IVmKY8?t=269) **[[scripting-and-performance]]** Treat track as blocks with entry and exit sensors; track trains in an in-block table, adding on enter and removing on exit or despawn, instead of GetTouchingParts.
- [5:10](https://youtu.be/uYIE3IVmKY8?t=310) **[[building-and-level-design]]** Write a Studio plugin to create and configure signal entry/exit points and advanced signals; hand-editing object values is error-prone.
- [11:17](https://youtu.be/uYIE3IVmKY8?t=677) **[[code-architecture-and-frameworks]]** Auto-derive aspect count from topology: if no signal ahead can show yellow, drop double-yellow and use a three-aspect signal.
- [17:06](https://youtu.be/uYIE3IVmKY8?t=1026) **[[core-loops-and-game-design]]** Compute signal state with a priority order: hard danger from occupancy overrides manual requests, then advanced signals ahead, then manual state with optional roll-back.
- [19:49](https://youtu.be/uYIE3IVmKY8?t=1189) **[[code-architecture-and-frameworks]]** Check the most dangerous downstream signal first and return immediately; keep looping over lesser signals so a red ahead overrides a yellow.
- [24:36](https://youtu.be/uYIE3IVmKY8?t=1476) **[[client-server-and-remotes]]** Keep occupancy authority on the server; use event-based enter/exit reports plus a periodic safety loop that forces exit for players too far from any sensor.
- [30:33](https://youtu.be/uYIE3IVmKY8?t=1833) **[[scripting-and-performance]]** Avoid per-object background loops; use one centralised table/manager for hundreds of entities and yield to keep the server near 60 fps.
- [28:20](https://youtu.be/uYIE3IVmKY8?t=1700) **[[anti-exploit-and-security]]** Validate manual control requests server-side: check permissions, rank, VIP server, desk ownership, and reject invalid states or double control.
- [31:13](https://youtu.be/uYIE3IVmKY8?t=1873) **[[common-mistakes]]** Lag-skipped sensors can leave a train stuck in a block and hold up the whole network; plan for missed enter/exit events.

## Numbers
- [16:00](https://youtu.be/uYIE3IVmKY8?t=960) Signal control script size: **~1041 lines** (Server script running automated and manual signalling)
- [31:53](https://youtu.be/uYIE3IVmKY8?t=1913) Forced-exit distance threshold: **~1500 studs (about 3x train length)** (Safety loop force-exits trains far from all block sensors)
- [33:57](https://youtu.be/uYIE3IVmKY8?t=2037) Signal count: **over 900** (Signals across the whole game, handled centrally)
- [34:38](https://youtu.be/uYIE3IVmKY8?t=2078) Server frame target: **close to 60 fps** (Signal processing spread to avoid hogging frame time)

## Games
- **Stepford County Railway (SCR)** [00:00](https://youtu.be/uYIE3IVmKY8?t=0): Roblox railway sim; rewrote signalling to block-based sensors with a server-side in-block table for scalability and easier track editing.

## Tools
Custom Roblox Studio signalling plugin (sensor/signal setup and validation), Lua task scheduler

## He points to
- Band Tech Systems BTS² series (episode 1 streaming system, episode 3 reservation/training queue preview)

## Quotes
- [33:57](https://youtu.be/uYIE3IVmKY8?t=2037) "a very much a centralized system on scr and that all of the signals are handled in that one kind of big table"
- [30:33](https://youtu.be/uYIE3IVmKY8?t=1833) "i'm not a big fan of loops running all the time in the background it generally implies some sort of bad programming practice"

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[core-loops-and-game-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[LastLevelStudios - How to make successful Roblox games]]
