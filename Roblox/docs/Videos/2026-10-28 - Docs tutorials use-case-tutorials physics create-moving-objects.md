---
title: "Docs: tutorials / use-case-tutorials / physics / create-moving-objects"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / physics / create-moving-objects

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on moving objects physics: linear motion, force, and velocity concepts; three techniques: LinearVelocity constraint, PrismaticConstraint (Motor), and ApplyImpulse for an initial launch that decelerates via friction/drag.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[building-and-level-design]]** Use LinearVelocity constraints to move a whole assembly at constant velocity; it can rotate on collisions, making gameplay less predictable.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[physics-pathfinding-and-npc-ai]]** Set LinearVelocity MaxForce high enough to reach target speed; too low and the object accelerates slowly or never reaches it.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[physics-pathfinding-and-npc-ai]]** Use PrismaticConstraint to lock movement to one axis for stable, predictable motion, e.g. moving platforms players must time jumps on.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[physics-pathfinding-and-npc-ai]]** Anchor one attachment's parent part with a PrismaticConstraint in Motor mode so only the unanchored assembly moves at the set velocity.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[combat-and-gameplay-systems]]** Use ApplyImpulse for instant feedback after events like explosions or jump pads; the object then decelerates under friction.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[physics-pathfinding-and-npc-ai]]** Balance impulse force per character: player characters have different masses, so a fixed impulse may launch light players too high.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[scripting-and-performance]]** Connect Touched events on a jump pad part and check the Humanoid before applying impulse so only characters trigger it.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) **[[physics-pathfinding-and-npc-ai]]** Set RelativeTo to World, not Attachment, if the object should keep its world orientation; attachment-relative motion rotates after collisions.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) LinearVelocity MaxForce: **5000 Rowtons (sample lily pad at 15 studs/s)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) PrismaticConstraint MotorMaxForce: **50000 Rowtons (sample log at 40 studs/s)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) ApplyImpulse jump pad force: **Vector3(0, 2500, 0) Rowton-seconds**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-moving-objects) Stud size: **about 28 cm real-world**

## Tools
Roblox Studio, Constraints (LinearVelocity, PrismaticConstraint), Attachments, BasePart.ApplyImpulse

## He points to
- Roblox Units documentation
- Exporting Requirements documentation
- Moving Objects sample .rbxl file

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
