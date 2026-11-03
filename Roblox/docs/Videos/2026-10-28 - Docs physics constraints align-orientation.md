---
title: "Docs: physics / constraints / align-orientation"
url: https://create.roblox.com/docs/physics/constraints/align-orientation.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / align-orientation

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/align-orientation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox API docs for the AlignOrientation mover constraint: how it applies torque to align attachments or match a goal orientation, and the settings controlling affected axes, torque magnitude, reactionary torque, and one- vs two-attachment mode.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/align-orientation) **[[physics-pathfinding-and-npc-ai]]** By default AlignOrientation only applies torque to Attachment0; enable ReactionTorqueEnabled to apply equal and opposite torque to Attachment1 too.
- [page](https://create.roblox.com/docs/physics/constraints/align-orientation) **[[physics-pathfinding-and-npc-ai]]** Use AlignType PrimaryAxisParallel, PrimaryAxisPerpendicular or PrimaryAxisLookAt to apply torque only when primary axes misalign, instead of AllAxes.
- [page](https://create.roblox.com/docs/physics/constraints/align-orientation) **[[physics-pathfinding-and-npc-ai]]** Set RigidityEnabled to true for the solver to align as fast as possible; when false, tune MaxTorque, MaxAngularVelocity and Responsiveness instead.
- [page](https://create.roblox.com/docs/physics/constraints/align-orientation) **[[physics-pathfinding-and-npc-ai]]** Use OneAttachment mode to align Attachment0 to a CFrame goal or to PrimaryAxis/SecondaryAxis; TwoAttachment mode ignores those properties.

## Tools
AlignOrientation constraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
