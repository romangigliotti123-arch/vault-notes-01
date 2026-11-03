---
title: "How to Create a Realistic NPC Eyesight System"
url: https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-07-07
views: 147
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Create a Realistic NPC Eyesight System

[Open](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) | Roblox DevForum | 147 views | 2023-07-07

## Summary
Tutorial on building a basic NPC eyesight system in Luau: tagging NPCs and detectable objects, field-of-view and distance checks via dot product, raycast line-of-sight occlusion, and a per-NPC detection loop running once per second.

## Tips
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) **[[genre-mechanics]]** Tag NPCs with 'NPC' and objects to detect with 'Detectable' via CollectionService; players are detected automatically. Detectable tag only works on Models with a valid PrimaryPart.
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) **[[scripting-and-performance]]** Run each NPC's sight check in its own coroutine on a loop with task.wait(1) rather than every frame to limit cost.
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) **[[scripting-and-performance]]** Use a raycast from the NPC head to block sight through walls; exclude the NPC and all character models from RaycastParams filter.
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) **[[scripting-and-performance]]** Check field of view with the dot product of the direction-to-target and head LookVector, and cheap distance check before the raycast to avoid unnecessary raycasts.
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) **[[luau-language-and-types]]** The tutorial suggests using the task library instead of coroutine.wrap for spawning loops.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) View range: **30 studs** (Default viewRange in the example script)
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) Field of view: **70 degrees** (Default fieldOfView in the example script (angle check))
- [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) Detection tick rate: **1 second** (task.wait(1) loop interval per NPC)

## Tools
CollectionService, RaycastParams, workspace:Raycast

## He points to
- Dot Product - Wikipedia
- Coroutine - Roblox Documentation

## Topics
[[genre-mechanics]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
