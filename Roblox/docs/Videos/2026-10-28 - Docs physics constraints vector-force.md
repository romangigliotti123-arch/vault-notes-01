---
title: "Docs: physics / constraints / vector-force"
url: https://create.roblox.com/docs/physics/constraints/vector-force.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / vector-force

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/vector-force.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the VectorForce constraint: applies constant linear force to an assembly, with options for attachment, center-of-mass, and world-relative application. Warns constant force can cause very high speeds.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/vector-force) **[[physics-pathfinding-and-npc-ai]]** VectorForce applies constant force, so speed grows unbounded without opposing forces; use LinearVelocity for steady velocity instead.
- [page](https://create.roblox.com/docs/physics/constraints/vector-force) **[[physics-pathfinding-and-npc-ai]]** To set only initial velocity, assign AssemblyLinearVelocity directly on the assembly rather than using VectorForce.
- [page](https://create.roblox.com/docs/physics/constraints/vector-force) **[[physics-pathfinding-and-npc-ai]]** By default VectorForce applies at Attachment0; if center of mass is misaligned, torque results. Enable ApplyAtCenterOfMass to avoid unwanted rotation.
- [page](https://create.roblox.com/docs/physics/constraints/vector-force) **[[physics-pathfinding-and-npc-ai]]** Use RelativeTo=Attachment0 for thruster-like forces that follow rotation, and RelativeTo=World for fixed directional forces like wind.

## Tools
VectorForce constraint, LinearVelocity constraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
