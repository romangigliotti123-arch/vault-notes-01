---
title: "Docs: physics / constraints / torsion-spring"
url: https://create.roblox.com/docs/physics/constraints/torsion-spring.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / torsion-spring

[Open](https://create.roblox.com/docs/physics/constraints/torsion-spring.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the TorsionSpringConstraint: applies torque from relative angle and angular velocity to bring two attachment SecondaryAxes into alignment, useful for spring-back hinged doors. Covers Damping, Stiffness, and LimitsEnabled/MaxAngle/Restitution for cone-limited range.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/torsion-spring) **[[building-and-level-design]]** Make attachments' SecondaryAxis perpendicular to the intended rotation axis; the constraint aligns SecondaryAxes, so wrong orientation breaks swinging doors.
- [page](https://create.roblox.com/docs/physics/constraints/torsion-spring) **[[physics-pathfinding-and-npc-ai]]** Set Damping above 0 to stop endless oscillation; Damping = 0 oscillates forever, higher values settle the spring faster.
- [page](https://create.roblox.com/docs/physics/constraints/torsion-spring) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled and set MaxAngle to restrict the spring's range within a cone; use Restitution to control elasticity at the limit.

## Tools
Studio constraints: TorsionSpringConstraint

## He points to
- Mechanical constraints docs page
- Roblox units docs page

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
