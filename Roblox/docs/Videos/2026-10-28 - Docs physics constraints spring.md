---
title: "Docs: physics / constraints / spring"
url: https://create.roblox.com/docs/physics/constraints/spring.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / spring

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/spring.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for SpringConstraint: explains FreeLength, Damping, Stiffness and optional MinLength/MaxLength limits, with stiffness examples at 25 and 500.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/spring) **[[physics-pathfinding-and-npc-ai]]** Set FreeLength to the spring's natural resting length; attachments farther apart are pulled together, closer ones pushed apart.
- [page](https://create.roblox.com/docs/physics/constraints/spring) **[[physics-pathfinding-and-npc-ai]]** Use Damping 0 only if you want endless oscillation; raise Damping to settle the spring to rest faster.
- [page](https://create.roblox.com/docs/physics/constraints/spring) **[[physics-pathfinding-and-npc-ai]]** Raise Stiffness for a stronger force response to displacement from FreeLength; the docs contrast 25 with 500 as soft versus stiff.
- [page](https://create.roblox.com/docs/physics/constraints/spring) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled and set MinLength/MaxLength to clamp spring travel; attachments stop at these limits without restitution.

## Numbers
- [page](https://create.roblox.com/docs/physics/constraints/spring) Stiffness example values: **25 (soft) and 500 (stiff)** (Docs illustrate spring response at these two Stiffness settings.)
- [page](https://create.roblox.com/docs/physics/constraints/spring) Damping minimum: **0 = endless oscillation** (Higher Damping values bring the spring to rest more quickly.)

## Tools
SpringConstraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
