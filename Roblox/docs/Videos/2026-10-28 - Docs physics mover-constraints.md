---
title: "Docs: physics / mover-constraints"
url: https://create.roblox.com/docs/physics/mover-constraints.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / mover-constraints

[Open](https://create.roblox.com/docs/physics/mover-constraints.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs overview of mover constraints (LinearVelocity, AngularVelocity, AlignPosition, AlignOrientation, VectorForce, Torque, LineForce, AnimationConstraint), how to create and attach them via Studio picker or Explorer, visualization toggles, Physical vs Geometric simulation, and conversion guidance from deprecated BodyMover classes.

## Tips
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Replace deprecated BodyPosition with AlignPosition; set ForceLimitMode to PerAxis to get independent per-axis force limits like BodyPosition.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Replace deprecated BodyGyro with AlignOrientation; use AlignType PrimaryAxisLookAt for cameras or guided missiles that track a target.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Replace deprecated BodyVelocity with LinearVelocity; use Line, Plane, or Vector VelocityConstraintMode to disable motion along chosen dimensions instead of zeroing MaxForce.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Replace BodyForce or BodyThrust with VectorForce; use RelativeTo to apply force at an offset from center, like BodyThrust.Location.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Replace RocketPropulsion with LineForce for follow-target behaviour plus AlignOrientation with LookAtPosition for face-target behaviour.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Use AngularVelocity with Attachments and RelativeTo (World or Attachment1) to control the frame of applied torque; note it has behavioural discrepancies vs BodyAngularVelocity.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[development-process-and-speed]]** Enable Show Constraint Details (Alt+D / Option+D) and Show Welds (Alt+W / Option+W) in Studio to visually debug constraints.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[physics-pathfinding-and-npc-ai]]** Switch Studio from Geometric to Physical mode to test realistic constraint behaviour, e.g. ropes becoming taut when dragging a part.
- [page](https://create.roblox.com/docs/physics/mover-constraints) **[[optimization-and-streaming]]** Use the Mechanisms visualization option to see groups of parts sharing simulation step and network ownership when debugging physics.

## Tools
Roblox Studio Constraint picker, Explorer window, Visualization Options widget

## He points to
- Class.BodyPosition (deprecated)
- Class.BodyGyro (deprecated)
- Class.BodyVelocity (deprecated)
- Class.RocketPropulsion (deprecated)

## Topics
[[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
