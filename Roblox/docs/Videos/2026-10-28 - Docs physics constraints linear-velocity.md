---
title: "Docs: physics / constraints / linear-velocity"
url: https://create.roblox.com/docs/physics/constraints/linear-velocity.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / linear-velocity

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/linear-velocity.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the LinearVelocity mover constraint. Explains it applies force to hold a constant linear velocity on an assembly, can act along a Vector3, a line, or a 2D plane, and how the RelativeTo property (World, Attachment0, Attachment1) sets the reference frame. Contrasts it with VectorForce and AssemblyLinearVelocity.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/linear-velocity) **[[physics-pathfinding-and-npc-ai]]** Use LinearVelocity when you need to maintain a constant velocity; use VectorForce when you need to control the amount of force applied.
- [page](https://create.roblox.com/docs/physics/constraints/linear-velocity) **[[physics-pathfinding-and-npc-ai]]** For only an initial velocity, set BasePart.AssemblyLinearVelocity directly on the assembly instead of using a constraint.
- [page](https://create.roblox.com/docs/physics/constraints/linear-velocity) **[[physics-pathfinding-and-npc-ai]]** Set LinearVelocity.RelativeTo to World for world-space force, or to Attachment0/Attachment1 to follow that attachment's orientation.

## Tools
LinearVelocity constraint, VectorForce constraint, AssemblyLinearVelocity property

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
