---
title: "Docs: physics / constraints / align-position"
url: https://create.roblox.com/docs/physics/constraints/align-position.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / align-position

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/align-position.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox API docs for the AlignPosition mover constraint. Covers force application location (Attachment0, optional ApplyAtCenterOfMass), force magnitude via RigidityEnabled or MaxForce/MaxVelocity/Responsiveness, optional reactionary force on Attachment1, and TwoAttachment vs OneAttachment modes.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/align-position) **[[physics-pathfinding-and-npc-ai]]** By default AlignPosition only applies force to Attachment0; Attachment1 is unaffected unless ReactionForceEnabled is true.
- [page](https://create.roblox.com/docs/physics/constraints/align-position) **[[physics-pathfinding-and-npc-ai]]** Enable ApplyAtCenterOfMass to avoid unwanted torque when the parent's center of mass is off the force direction.
- [page](https://create.roblox.com/docs/physics/constraints/align-position) **[[physics-pathfinding-and-npc-ai]]** Use RigidityEnabled=true for the fastest possible alignment; use MaxForce, MaxVelocity and Responsiveness when you need controlled, non-rigid movement.
- [page](https://create.roblox.com/docs/physics/constraints/align-position) **[[physics-pathfinding-and-npc-ai]]** Set Mode to OneAttachment to move Attachment0 to the Position property; TwoAttachment (default) moves Attachment0 to Attachment1's position.

## Tools
AlignPosition

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
