---
title: "Docs: physics / constraints / angular-velocity"
url: https://create.roblox.com/docs/physics/constraints/angular-velocity.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / angular-velocity

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/angular-velocity.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs for the AngularVelocity constraint, which applies torque to hold an assembly at a constant angular velocity. Covers the RelativeTo property (World vs Attachment1) and when ReactionTorqueEnabled becomes available. Points to Torque constraints and AssemblyAngularVelocity for other cases.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/angular-velocity) **[[physics-pathfinding-and-npc-ai]]** Use AngularVelocity only when you need a constant spin; it applies torque to maintain the target velocity.
- [page](https://create.roblox.com/docs/physics/constraints/angular-velocity) **[[physics-pathfinding-and-npc-ai]]** Use a Torque constraint instead if you need to control the amount of torque applied.
- [page](https://create.roblox.com/docs/physics/constraints/angular-velocity) **[[physics-pathfinding-and-npc-ai]]** For only an initial spin, set BasePart.AssemblyAngularVelocity on the assembly directly rather than adding a constraint.
- [page](https://create.roblox.com/docs/physics/constraints/angular-velocity) **[[physics-pathfinding-and-npc-ai]]** Set RelativeTo to World to use the angular velocity vector as-is; use Attachment1 to make it relative to the other attachment's motion.

## Tools
AngularVelocity constraint, Torque constraint, AssemblyAngularVelocity property

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
