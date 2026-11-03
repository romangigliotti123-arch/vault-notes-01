---
title: "Docs: physics / mechanical-constraints"
url: https://create.roblox.com/docs/physics/mechanical-constraints.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / mechanical-constraints

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/mechanical-constraints.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for mechanical constraints: lists constraint types (Ball Socket, Hinge, Prismatic, Cylindrical, Spring, Torsion Spring, Universal, Rope, Rod, Plane, Weld, Rigid, No Collision), how to create them via the Constraint picker or Explorer, visualization toggles, and Physical vs Geometric simulation mode.

## Tips
- [page](https://create.roblox.com/docs/physics/mechanical-constraints) **[[building-and-level-design]]** Use Studio's Show Welds (Alt+W) and Show Constraint Details (Alt+D) to visualize constraints accurately while building mechanisms.
- [page](https://create.roblox.com/docs/physics/mechanical-constraints) **[[physics-pathfinding-and-npc-ai]]** Switch to Physical mode when dragging parts so they obey physical limits; e.g. a taut RopeConstraint will pull the other part along.
- [page](https://create.roblox.com/docs/physics/mechanical-constraints) **[[optimization-and-streaming]]** Enable Mechanisms visualization in the 3D viewport to see groups of parts sharing simulation step and network ownership.
- [page](https://create.roblox.com/docs/physics/mechanical-constraints) **[[physics-pathfinding-and-npc-ai]]** Most mechanical constraints need a secondary Attachment or Bone; WeldConstraint and NoCollisionConstraint instead link Part0/Part1 directly.

## Tools
Roblox Studio, Constraint picker, Explorer

## Topics
[[building-and-level-design]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
