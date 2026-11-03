---
title: "Docs: tutorials / use-case-tutorials / physics / build-a-ferris-wheel"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / physics / build-a-ferris-wheel

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building a motorized ferris wheel with HingeConstraint: attachments, ActuatorType Motor, radians-per-second AngularVelocity, and torque settings. Teaches using as few constraints as possible for stable contraptions.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[physics-pathfinding-and-npc-ai]]** Set a HingeConstraint's ActuatorType to Motor so it turns on its own; by default it only turns when an outside force acts on it.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[physics-pathfinding-and-npc-ai]]** AngularVelocity is in radians per second; use multiples of pi (e.g. pi/10 = 0.314 for a slow turn) for precise rotation speeds.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[physics-pathfinding-and-npc-ai]]** Set MotorMaxTorque to inf (copied from MotorMaxAcceleration) so the mechanism can handle any load, such as player-filled cars.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[physics-pathfinding-and-npc-ai]]** Only one motor is needed per rotating assembly; avoid adding motors on both sides of the wheel.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[physics-pathfinding-and-npc-ai]]** Use as few constraints as possible in contraptions; this keeps them stable and reliable.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[building-and-level-design]]** Align attachment arrows (yellow, pointing along the constraint axis) on both ends so they point the same direction, using the Rotate tool if needed.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) **[[building-and-level-design]]** Enable View > Show Constraint Details in Studio to see constraints and attachments while building.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) AngularVelocity for 1/10 revolution per second: **0.314 rad/s (pi/10)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) Radians per revolution: **2*pi = 6.28 rad per revolution per second**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-ferris-wheel) Half revolution per second: **pi = 3.14 rad/s**

## Tools
Roblox Studio, HingeConstraint, Attachments

## He points to
- Roblox docs: Build a ferris wheel tutorial

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
