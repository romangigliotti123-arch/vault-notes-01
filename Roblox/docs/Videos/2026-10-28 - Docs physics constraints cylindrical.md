---
title: "Docs: physics / constraints / cylindrical"
url: https://create.roblox.com/docs/physics/constraints/cylindrical.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / cylindrical

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/cylindrical.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for CylindricalConstraint: sliding along one axis plus rotation about another, usable for vehicle suspensions with SpringConstraint. Covers Motor and Servo actuator modes for both angular and linear power, sliding and angular limits, and InclinationAngle for rotation axis direction.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/cylindrical) **[[physics-pathfinding-and-npc-ai]]** For vehicle suspensions, pair CylindricalConstraint (wheel slides up/down and spins) with a SpringConstraint for shock absorption.
- [page](https://create.roblox.com/docs/physics/constraints/cylindrical) **[[physics-pathfinding-and-npc-ai]]** Align each attachment's Axis and SecondaryAxis to point the same direction so rotation occurs around the intended axis.
- [page](https://create.roblox.com/docs/physics/constraints/cylindrical) **[[physics-pathfinding-and-npc-ai]]** Use ActuatorType/AngularActuatorType Motor to drive toward a Velocity/AngularVelocity; control with MotorMaxForce/MotorMaxTorque and acceleration limits.
- [page](https://create.roblox.com/docs/physics/constraints/cylindrical) **[[physics-pathfinding-and-npc-ai]]** Use Servo actuator mode to move to a TargetPosition or TargetAngle; tune Speed/AngularSpeed, responsiveness, and ServoMaxForce/ServoMaxTorque.

## Numbers
- [page](https://create.roblox.com/docs/physics/constraints/cylindrical) InclinationAngle range: **-180 to 180 degrees** (Angle from X axis in Attachment0 X/Y plane)

## Tools
Roblox Studio, CylindricalConstraint, SpringConstraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
