---
title: "Docs: physics / constraints / prismatic"
url: https://create.roblox.com/docs/physics/constraints/prismatic.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / prismatic

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/prismatic.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for PrismaticConstraint: a rigid one-axis slide joint between two attachments, powered via Motor (Velocity, MotorMaxAcceleration, MotorMaxForce) or Servo (TargetPosition, Speed, LinearResponsiveness, ServoMaxForce), with optional limits, and attachment Axis alignment controlling movement direction.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/prismatic) **[[building-and-level-design]]** Point each attachment's Axis (yellow arrow) in the same direction so the prismatic slides along the desired axis.
- [page](https://create.roblox.com/docs/physics/constraints/prismatic) **[[physics-pathfinding-and-npc-ai]]** Use ActuatorType Motor to drive toward a Velocity, limited by MotorMaxAcceleration and MotorMaxForce.
- [page](https://create.roblox.com/docs/physics/constraints/prismatic) **[[physics-pathfinding-and-npc-ai]]** Use ActuatorType Servo to move to a TargetPosition, tuned with Speed, LinearResponsiveness and ServoMaxForce.
- [page](https://create.roblox.com/docs/physics/constraints/prismatic) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled and set LowerLimit/UpperLimit to restrict sliding range; Restitution sets elasticity at limits.

## Tools
PrismaticConstraint

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
