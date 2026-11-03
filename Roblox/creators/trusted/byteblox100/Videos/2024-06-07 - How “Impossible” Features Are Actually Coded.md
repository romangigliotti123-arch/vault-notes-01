---
title: "How “Impossible” Features Are Actually Coded"
url: https://youtu.be/s2XUzTyCdK4
creator: ByteBlox
official: false
advice_density: medium
date: 2024-06-07
views: 97126
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How “Impossible” Features Are Actually Coded

[Watch](https://youtu.be/s2XUzTyCdK4) | byteblox100 | 97,126 views | 2024-06-07

## Summary
Tutorial showing how an "infinite hallway" illusion is built in Roblox Studio: a player-triggered system that clones room modules at a start/end attachment point, with fog and lighting to hide the seams. Explains that infinity is impossible, so the goal is perceived infinity. Ends with a promotional pitch for a course and Discord.

## Tips
- [1:22](https://youtu.be/s2XUzTyCdK4?t=82) **[[common-mistakes]]** A while true loop with no yield will exhaust execution time and hang the game; games cannot run true infinity, so simulate it instead.
- [2:03](https://youtu.be/s2XUzTyCdK4?t=123) **[[player-psychology-and-game-feel]]** Illusions work if the player is never given reason to doubt them; consistency matters more than objective truth.
- [3:52](https://youtu.be/s2XUzTyCdK4?t=232) **[[building-and-level-design]]** Duplicate and scale a part instead of eyeballing placement, so the start/end points sit exactly at the room's midpoint or edge.
- [5:42](https://youtu.be/s2XUzTyCdK4?t=342) **[[building-and-level-design]]** Place start and end attachment parts outside the room geometry, with orientation set consistently, so rooms chain end-to-start.
- [7:43](https://youtu.be/s2XUzTyCdK4?t=463) **[[scripting-and-performance]]** Set a model's PrimaryPart and use PivotTo to position cloned rooms, rather than moving each part manually.
- [9:55](https://youtu.be/s2XUzTyCdK4?t=595) **[[client-server-and-remotes]]** Use an invisible trigger part at the room's end to spawn new rooms on demand, so you do not load everything at once.
- [10:37](https://youtu.be/s2XUzTyCdK4?t=637) **[[scripting-and-performance]]** Store Touched connections in a variable and disconnect them after the first trigger to avoid duplicate room spawns.
- [10:37](https://youtu.be/s2XUzTyCdK4?t=637) **[[scripting-and-performance]]** Check for a Humanoid on the touching part's parent so only players, not arbitrary parts, trigger room generation.
- [13:56](https://youtu.be/s2XUzTyCdK4?t=836) **[[code-architecture-and-frameworks]]** Use separate ModuleScripts per direction and an attribute (e.g. IsDirectionOne) on each trigger to choose which module to call.
- [16:45](https://youtu.be/s2XUzTyCdK4?t=1005) **[[testing-debugging-and-qa]]** Verify generation by placing marker parts and checking whether they disappear after touching the trigger.
- [17:10](https://youtu.be/s2XUzTyCdK4?t=1030) **[[building-and-level-design]]** Use Lighting fog, darkness, and color correction to hide seams and sell a limitless environment.
- [18:33](https://youtu.be/s2XUzTyCdK4?t=1113) **[[common-mistakes]]** Ensure triggers have CanCollide off and transparency off so they do not block the player while remaining invisible when intended.

## Numbers
- [1:22](https://youtu.be/s2XUzTyCdK4?t=82) execution limit: **infinite loop exhausts allowed execution time** (while true loop without yield in Roblox)
- [15:21](https://youtu.be/s2XUzTyCdK4?t=921) initial rooms generated: **5 per direction** (preloaded rooms in the test hallway)
- [8:24](https://youtu.be/s2XUzTyCdK4?t=504) room spawn interval in test: **3 seconds** (first test loop before trigger-based generation)

## Games
- **Eternal Hallways (creator's own demo)** [0:00](https://youtu.be/s2XUzTyCdK4?t=0): Illusion of infinity via procedural room cloning triggered by player position, with fog to hide the loop.

## Tools
Roblox Studio, Luau, ModuleScript, Lighting (fog, color correction)

## Quotes
- [1:22](https://youtu.be/s2XUzTyCdK4?t=82) "games can't handle infinity... what's really possible is the perception of an eternal hallway"
- [2:03](https://youtu.be/s2XUzTyCdK4?t=123) "if you make the players believe that it is and you don't leave any room for doubt then it's a real optical illusion"

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[byteblox100 - How to make successful Roblox games]]
