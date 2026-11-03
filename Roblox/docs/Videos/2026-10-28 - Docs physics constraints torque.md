---
title: "Docs: physics / constraints / torque"
url: https://create.roblox.com/docs/physics/constraints/torque.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / torque

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/torque.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Torque mover constraint. Explains that Torque applies constant torque from the assembly's center of mass, warns it can cause very high speeds without other forces, and describes RelativeTo options (Attachment0 default, World, Attachment1).

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/torque) **[[physics-pathfinding-and-npc-ai]]** Torque applies constant torque and angular acceleration; without other forces speeds can get very high. Use AngularVelocity for steady rotation speed.
- [page](https://create.roblox.com/docs/physics/constraints/torque) **[[physics-pathfinding-and-npc-ai]]** To set only an initial spin, set BasePart.AssemblyAngularVelocity directly on the assembly instead of using a constraint.
- [page](https://create.roblox.com/docs/physics/constraints/torque) **[[physics-pathfinding-and-npc-ai]]** Torque defaults to being relative to Attachment0, so it changes direction as the parent assembly rotates. Set RelativeTo to World for fixed world-axis torque.

## Tools
Torque constraint, AngularVelocity constraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
