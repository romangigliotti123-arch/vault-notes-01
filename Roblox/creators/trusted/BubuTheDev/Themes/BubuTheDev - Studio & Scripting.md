---
title: BubuTheDev - Studio & Scripting
creator: BubuTheDev
tags: [roblox, bubuthedev, theme]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BubuTheDev: Studio & Scripting

All BubuTheDev tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2024-09-06 [2:45](https://youtu.be/oYQ5jIZKE8s?t=165) Add a short wait (about 0.25s) before the death fade so it doesn't play instantly on death. ([[2024-09-06 - DON’T do this mistake in your Roblox games!|DON’T do this mistake in your Roblox games!]])
- 2024-09-06 [0:00](https://youtu.be/oYQ5jIZKE8s?t=0) Cache a service-level local for character debugging: store Humanoid via character:FindFirstChildOfClass('Humanoid') and check it exists before connecting Died. ([[2024-09-06 - DON’T do this mistake in your Roblox games!|DON’T do this mistake in your Roblox games!]])
- 2024-09-08 [0:41](https://youtu.be/zc7vWpLOejE?t=41) Count frames in RunService.RenderStepped and update the label once per second (update rate = 1) instead of every frame to keep the readout stable and cheap. ([[2024-09-08 - How to add a FPS COUNTER to your Roblox game!|How to add a FPS COUNTER to your Roblox game!]])

## [[building-art-and-assets]]
- 2024-09-07 [0:41](https://youtu.be/xVUqKk3OnnU?t=41) Make a script-free conveyor by setting the belt part's AssemblyLinearVelocity in Properties to the axis speed (e.g. X = -50). ([[2024-09-07 - This makes your Roblox game slow, here’s how to fix it!|This makes your Roblox game slow, here’s how to fi]])

## [[ai-and-tools]]
- 2025-06-09 [0:08](https://youtu.be/0UYtSJvYe4U?t=8) Install a service autocomplete plugin so typing a service name like 'players' and pressing Tab auto-adds the local variable line. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])
- 2025-06-09 [3:28](https://youtu.be/0UYtSJvYe4U?t=208) Use the Reclass plugin to convert an instance to a different class (e.g. Frame to ImageLabel or ImageButton) while keeping its properties. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])

## [[physics-pathfinding-and-npc-ai]]
- 2024-09-17 [0:51](https://youtu.be/UM7UtF4e0-0?t=51) Use a pathfinding module (Forbidden API from Toolbox) placed in ReplicatedStorage to make NPCs navigate around barriers and mazes. ([[2024-09-17 - How to make an advanced NPC CHASE AI in Roblox Studio SIMPLE|How to make an advanced NPC CHASE AI in Roblox Stu]])
- 2024-09-17 [0:40](https://youtu.be/UM7UtF4e0-0?t=40) Tune the AI script's shortest-distance value (example: 300) to control how far the NPC will path to chase the player. ([[2024-09-17 - How to make an advanced NPC CHASE AI in Roblox Studio SIMPLE|How to make an advanced NPC CHASE AI in Roblox Stu]])

## [[building-and-level-design]]
- 2024-09-07 [2:04](https://youtu.be/xVUqKk3OnnU?t=124) If the belt is oriented on a different axis, set the velocity on that axis (e.g. Z = 50) instead; flip the sign if it moves the wrong way. ([[2024-09-07 - This makes your Roblox game slow, here’s how to fix it!|This makes your Roblox game slow, here’s how to fi]])
- 2025-06-09 [1:02](https://youtu.be/0UYtSJvYe4U?t=62) Make ladders climbable by placing transparent (transparency 1) but collidable Truss Ladder parts from the toolbox behind the ladder. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])
- 2025-06-09 [2:25](https://youtu.be/0UYtSJvYe4U?t=145) Fix tall stairs that block the character by adding a transparent, collidable WedgePart ramp over the steps so they can be walked up. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])

## [[vfx-and-particles]]
- 2024-09-06 [0:00](https://youtu.be/oYQ5jIZKE8s?t=0) Use TweenService with TweenInfo on Humanoid.Died to fade character parts on death instead of the default instant reset, for a smoother feel. ([[2024-09-06 - DON’T do this mistake in your Roblox games!|DON’T do this mistake in your Roblox games!]])

## [[ui-ux-design]]
- 2024-09-08 [2:48](https://youtu.be/zc7vWpLOejE?t=168) Place the FPS label in a screen corner (right-aligned, slightly down) so it does not block gameplay HUD. ([[2024-09-08 - How to add a FPS COUNTER to your Roblox game!|How to add a FPS COUNTER to your Roblox game!]])

## [[optimization-and-streaming]]
- 2024-09-07 [0:00](https://youtu.be/xVUqKk3OnnU?t=0) Delete the Toolbox conveyor's per-0.1-second script; it runs constantly and is unnecessary for moving a belt. ([[2024-09-07 - This makes your Roblox game slow, here’s how to fix it!|This makes your Roblox game slow, here’s how to fi]])
- 2024-09-08 [2:05](https://youtu.be/zc7vWpLOejE?t=125) Test FPS under different Roblox Settings > Maximum frame rate values (e.g. 120, 144) to verify the counter tracks the cap. ([[2024-09-08 - How to add a FPS COUNTER to your Roblox game!|How to add a FPS COUNTER to your Roblox game!]])
- 2025-06-09 [4:37](https://youtu.be/0UYtSJvYe4U?t=277) Set CanTouch to false on decorative parts that don't use Touched events to reduce per-frame touch checks on large maps; keep it true for triggers. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])
- 2025-06-09 [5:47](https://youtu.be/0UYtSJvYe4U?t=347) Use transparency exactly 0 or 1 instead of near-zero values like 0.05, since fractional transparency adds rendering cost across large maps. ([[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]])

Up: [[BubuTheDev - How to make successful Roblox games]]
