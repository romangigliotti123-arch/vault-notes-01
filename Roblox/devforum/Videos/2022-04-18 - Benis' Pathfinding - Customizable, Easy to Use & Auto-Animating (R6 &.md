---
title: "Benis' Pathfinding - Customizable, Easy to Use & Auto-Animating (R6 & R15 SUPPORT)!"
url: https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-04-18
views: 55
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Benis' Pathfinding - Customizable, Easy to Use & Auto-Animating (R6 & R15 SUPPORT)!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) | Roblox DevForum | 55 views | 2022-04-18

## Summary
DevForum-style resource post for a customizable NPC pathfinding script for Roblox (R6 and R15). Covers options like animateNPC, stopNearPlayer, requiresSight, moveIfNoPath, moveToWait, waitBeforeStart, plus health/jump/walk speed settings. Setup: insert into an unanchored character. Includes v1.01 update log.

## Tips
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) **[[development-process-and-speed]]** Insert the script into an unanchored character; anchored characters will not move with the pathfinding.
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) **[[ai-and-tools]]** Set animateNPC to true to auto-animate the NPC; works with both R6 and R15 rigs.
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) **[[physics-pathfinding-and-npc-ai]]** Use requiresSight to make the NPC only chase targets it can see; this also reduces the effective maxDistance.
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) **[[physics-pathfinding-and-npc-ai]]** Set stopNearPlayer so the NPC halts within 3 studs of its target instead of pushing into them.

## Numbers
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) stopNearPlayer distance: **3 studs** (NPC stops when closer than this to its target)
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) moveIfNoPath distance: **15 studs** (NPC moves this far away when path.Status is not Success)
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) waitBeforeStart delay: **5-10 seconds** (Delay before the AI starts)
- [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994) Script version: **V1.01** (Added stopNearPlayer, moveIfNoPath, waitBeforeStart, requiresSight, createWaypointParts; optimised threads)

## Tools
PathfindingService, Roblox Studio, Roblox Toolbox/Marketplace model

## Topics
[[ai-and-tools]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
