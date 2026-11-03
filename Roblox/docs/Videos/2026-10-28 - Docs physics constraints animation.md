---
title: "Docs: physics / constraints / animation"
url: https://create.roblox.com/docs/physics/constraints/animation.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / animation

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/animation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for AnimationConstraint: explains how it constrains Attachments via an offset Transform, either kinematically (snap instantly, bypass physics) or non-kinematically (follow trajectory using MaxForce/MaxTorque limits).

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/animation) **[[physics-pathfinding-and-npc-ai]]** Use IsKinematic=true when connected parts must snap precisely to the transform without participating in physics simulation.
- [page](https://create.roblox.com/docs/physics/constraints/animation) **[[physics-pathfinding-and-npc-ai]]** Set IsKinematic=false when parts should follow the target trajectory via force and torque rather than snapping.
- [page](https://create.roblox.com/docs/physics/constraints/animation) **[[physics-pathfinding-and-npc-ai]]** For non-kinematic constraints, tune MaxForce and MaxTorque to limit how strongly parts are driven toward the transform.

## Tools
AnimationConstraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
