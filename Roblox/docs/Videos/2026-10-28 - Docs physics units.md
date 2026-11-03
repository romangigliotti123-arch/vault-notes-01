---
title: "Docs: physics / units"
url: https://create.roblox.com/docs/physics/units.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / units

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/units.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation on physical units: primary conversions (1 stud = 28 cm, 1 RMU = 21.952 kg, 1 s = 1 s), derived units (water density, velocity, force, torque), default vs realistic gravity, PhysicalProperties limits, and guidance on keeping unit interpretations consistent.

## Tips
- [page](https://create.roblox.com/docs/physics/units) **[[building-and-level-design]]** Use standard Roblox units rather than custom interpretations; it makes the game behave as expected in all scenarios, including VR controls.
- [page](https://create.roblox.com/docs/physics/units) **[[scripting-and-performance]]** If you redefine studs or RMUs, apply the interpretation consistently across the whole game so physics and conversions stay coherent.
- [page](https://create.roblox.com/docs/physics/units) **[[physics-pathfinding-and-npc-ai]]** Keep PhysicalProperties within limits: density 0.0001–100 RMU/stud³, friction 0–2, elasticity 0–1, friction/elasticity weight 0–100.
- [page](https://create.roblox.com/docs/physics/units) **[[physics-pathfinding-and-npc-ai]]** Default gravity is 196.2 studs/s² (≈54.936 m/s² metric), about 5.6× real-world 35 studs/s² (9.8 m/s²); tune constraint and mover forces with these units in mind.

## Numbers
- [page](https://create.roblox.com/docs/physics/units) Stud length: **1 stud = 28 cm** (Primary length conversion for Roblox units)
- [page](https://create.roblox.com/docs/physics/units) Mass: **1 RMU = 21.952 kg** (Roblox Mass Unit primary conversion)
- [page](https://create.roblox.com/docs/physics/units) Water density: **1 g/cm³ = 1 RMU/stud³** (Derived unit equivalence)
- [page](https://create.roblox.com/docs/physics/units) Velocity: **1 m/s = 3.57 studs/s** (Derived unit conversion)

## Tools
Datatype.PhysicalProperties

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
