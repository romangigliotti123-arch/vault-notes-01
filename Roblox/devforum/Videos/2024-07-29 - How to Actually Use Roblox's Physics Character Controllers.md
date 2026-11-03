---
title: "How to Actually Use Roblox's Physics Character Controllers"
url: https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-07-29
views: 358
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Actually Use Roblox's Physics Character Controllers

[Open](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) | Roblox DevForum | 358 views | 2024-07-29

## Summary
DevForum tutorial on using Roblox's physics character controllers (ControllerManager, GroundController, AirController, ControllerPartSensor) without OOP. Covers setup on join, manual ground raycast writing SensedPart/HitNormal/HitFrame (HitFrame needed for slopes), jump impulse, and a speed-scaled air control trick for knockback-friendly movement.

## Tips
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[luau-language-and-types]]** Set Humanoid.EvaluateStateMachine = false on CharacterAdded to disable default humanoid physics before adding a ControllerManager.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[physics-pathfinding-and-npc-ai]]** Set ControllerPartSensor.SensorUpdateType to Manual and feed it your own raycast each frame (SensedPart, HitNormal, HitFrame).
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[physics-pathfinding-and-npc-ai]]** Also write GroundSensor.HitFrame = CFrame.new(hit.Position); the docs omit it and characters can't climb slopes without it.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[physics-pathfinding-and-npc-ai]]** Use a downward raycast of about 4.5 studs from HumanoidRootPart to decide Ground vs Air controller; switch to AirController when it misses.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[combat-and-gameplay-systems]]** Scale AirController.MoveMaxForce by velocity magnitude times BaseMoveSpeed to limit air directional influence, smoothing movement during knockback.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[combat-and-gameplay-systems]]** Set AirController.MoveMaxForce to 0 to disable midair movement entirely, e.g. during a knockback state.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[combat-and-gameplay-systems]]** Apply equal and opposite impulse to the floor part at the sensed hit normal when jumping from ground.
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) **[[client-server-and-remotes]]** Drive controller updates from a LocalScript on RunService each frame, reading Humanoid.MoveDirection to set ControllerManager.MovingDirection.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) BaseMoveSpeed: **25 (example, change as needed)**
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) GroundOffset: **2 studs (leg height of default R6/R15)**
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) AirController.MoveMaxForce: **75000 (example)**
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) Ground raycast length: **-4.5 studs on Y**
- [page](https://devforum.roblox.com/t/how-to-actually-use-robloxs-physics-character-controllers/3092097) Jump impulse: **Vector3(0, 750, 0) (example)**

## Tools
ControllerManager, GroundController, AirController, ControllerPartSensor, RunService, ContextActionService, RaycastParams

## He points to
- Roblox Character Controllers documentation article
- Roblox Platformer template (OOP + physics controllers)

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[luau-language-and-types]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
