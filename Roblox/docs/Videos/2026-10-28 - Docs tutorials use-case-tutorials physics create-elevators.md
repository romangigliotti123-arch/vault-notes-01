---
title: "Docs: tutorials / use-case-tutorials / physics / create-elevators"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / physics / create-elevators

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building a basic elevator: a block platform sliding on a PrismaticConstraint along a track, triggered by a ProximityPrompt and controlled by a short Script that toggles TargetPosition based on CurrentPosition.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) **[[building-and-level-design]]** Move constraint attachments outside their parent parts and align them on X and Z so the platform slides freely without colliding with the track.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) **[[physics-pathfinding-and-npc-ai]]** Use PrismaticConstraint with Limits Enabled and ActuatorType Servo to drive a platform along one axis with fixed orientation.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) **[[physics-pathfinding-and-npc-ai]]** Set Restitution to 0 on prismatic limits so the platform does not bounce when reaching the upper or lower limit.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) **[[physics-pathfinding-and-npc-ai]]** Set ServoMaxForce high enough (example 10000) so the platform holds its weight against gravity while moving.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) **[[combat-and-gameplay-systems]]** Trigger interactive objects with a ProximityPrompt on the part, and connect its Triggered event on the server to start movement.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) Platform size: **8x1x4 studs** (Block platform in elevator tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) Track height: **20 studs** (Track Y size; platform travels 10 studs each way)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) LowerLimit / UpperLimit: **-10 / 10** (PrismaticConstraint range of motion around TrackAttachment)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) ServoMaxForce / Speed: **10000 / 10** (Servo settings used for elevator motion)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-elevators) Script threshold: **CurrentPosition 9** (Tutorial checks position against 9 to decide direction)

## Tools
Roblox Studio, PrismaticConstraint, ProximityPrompt, Servo actuator

## He points to
- Roblox Creator Docs: Create elevators tutorial

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
