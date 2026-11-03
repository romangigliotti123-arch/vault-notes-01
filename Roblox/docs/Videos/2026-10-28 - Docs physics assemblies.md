---
title: "Docs: physics / assemblies"
url: https://create.roblox.com/docs/physics/assemblies.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / assemblies

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/assemblies.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on assemblies: how welded/jointed parts form a single rigid body, how forces apply to the assembly, assembly properties, how the AssemblyRootPart is chosen, and how anchoring splits assemblies.

## Tips
- [page](https://create.roblox.com/docs/physics/assemblies) **[[scripting-and-performance]]** Anchor only the assembly's root part to anchor a whole assembly; anchoring every part is less performant because it creates more assemblies.
- [page](https://create.roblox.com/docs/physics/assemblies) **[[scripting-and-performance]]** Don't set AssemblyLinearVelocity/AngularVelocity directly; use VectorForce, LinearVelocity, Torque, AngularVelocity constraints, or ApplyImpulse/ApplyAngularImpulse, to avoid unrealistic motion.
- [page](https://create.roblox.com/docs/physics/assemblies) **[[scripting-and-performance]]** Store physics-joined parts only in Workspace or a WorldModel; welds/joints in other containers are non-functional.
- [page](https://create.roblox.com/docs/physics/assemblies) **[[building-and-level-design]]** Use Models to group assembly parts and related objects so they organise as a single asset.

## Numbers
- [page](https://create.roblox.com/docs/physics/assemblies) Assembly mass: **Sum of Mass of all parts; infinite if any part is anchored** (AssemblyMass property behaviour)
- [page](https://create.roblox.com/docs/physics/assemblies) Root part precedence: **Anchored > non-massless > higher RootPriority > largest face area (Seat/VehicleSeat highest multiplier, then HumanoidRootPart, then Torso)** (Ordered from highest to lowest probability)

## Tools
Roblox Studio Visualization Options (Assemblies toggle)

## Topics
[[building-and-level-design]] [[common-mistakes]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
