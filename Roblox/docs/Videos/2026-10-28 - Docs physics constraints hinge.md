---
title: "Docs: physics / constraints / hinge"
url: https://create.roblox.com/docs/physics/constraints/hinge.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / hinge

[Open](https://create.roblox.com/docs/physics/constraints/hinge.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for HingeConstraint: rotation about one axis, Motor vs Servo actuator modes, and limits (LowerAngle/UpperAngle/Restitution). Explains attachment axis alignment requirement.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/hinge) **[[physics-pathfinding-and-npc-ai]]** Point both attachments' Axis (yellow arrow) in the same direction, or the hinge will rotate around the wrong axis.
- [page](https://create.roblox.com/docs/physics/constraints/hinge) **[[physics-pathfinding-and-npc-ai]]** Use ActuatorType Motor to drive toward AngularVelocity, limited by MotorMaxAcceleration and MotorMaxTorque.
- [page](https://create.roblox.com/docs/physics/constraints/hinge) **[[physics-pathfinding-and-npc-ai]]** Use ActuatorType Servo to rotate to TargetAngle, controlled by AngularSpeed and ServoMaxTorque.
- [page](https://create.roblox.com/docs/physics/constraints/hinge) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled and set LowerAngle/UpperAngle to restrict swing, e.g. for doors; tune Restitution for bounce at limits.

## Tools
HingeConstraint

## He points to
- Mechanical constraints docs page
- Roblox units docs page

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
