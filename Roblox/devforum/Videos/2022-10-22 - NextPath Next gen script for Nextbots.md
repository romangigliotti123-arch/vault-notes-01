---
title: "NextPath: Next gen script for Nextbots"
url: https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-10-22
views: 119
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# NextPath: Next gen script for Nextbots

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) | Roblox DevForum | 119 views | 2022-10-22

## Summary
Free open-source-style Nextbot AI script "NextPath" by foodman54. Combines SimplePath pathfinding with Humanoid:MoveTo() dash mode within a configurable run distance. Configurable settings include tick rate, max search distance, visibility checks, jumping, damage, and ambient sound timing.

## Tips
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) **[[core-loops-and-game-design]]** Avoid relying solely on Humanoid:MoveTo() for NPC chasing; it makes NPCs get stuck on walls. Use pathfinding for long range and switch to MoveTo only when close.
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) **[[physics-pathfinding-and-npc-ai]]** Use a hybrid chase: SimplePath pathfinding when outside RunDistance (default 20 studs), then Humanoid:MoveTo() inside it for a clear, direct approach.
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) **[[physics-pathfinding-and-npc-ai]]** Use raycast visibility checks to pick targets so NPCs only chase players they could realistically see; disable the check (VisibilityCheck=false) to queue all players.
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) **[[physics-pathfinding-and-npc-ai]]** Tune Rate (default 0.1 s tick) and MaxDistance (default 500 studs) to control NPC thinking cost; the author did not performance-test the script.

## Numbers
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) RunDistance: **20 studs** (default distance before switching from pathfinding to Humanoid:MoveTo())
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) Rate: **0.1** (default NPC tick rate setting)
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) MaxDistance: **500 studs** (default max search distance for NPC targets)
- [page](https://devforum.roblox.com/t/nextpath-next-gen-script-for-nextbots/2030360) MaxJumpTicks: **20** (ticks NPC waits before jumping toward a higher target)

## Tools
NextPath script (NextPathHandler), SimplePath (by GrayzcaIe), Roblox Toolbox, Humanoid:MoveTo()

## Topics
[[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
