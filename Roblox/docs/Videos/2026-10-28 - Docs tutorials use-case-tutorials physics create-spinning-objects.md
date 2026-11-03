---
title: "Docs: tutorials / use-case-tutorials / physics / create-spinning-objects"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / physics / create-spinning-objects

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on making objects spin using three approaches: AngularVelocity constraint (whole assembly, constant speed), HingeConstraint motor (one part spins while base stays anchored), and ApplyAngularImpulse (initial spin that decelerates). Explains torque, moment of inertia, and Rowton-stud units.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[building-and-level-design]]** Use AngularVelocity constraints to spin a whole assembly at constant speed; set MaxTorque high enough to overcome mass and friction.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[physics-pathfinding-and-npc-ai]]** Larger parts have higher moment of inertia and need more torque for the same acceleration; scale MaxTorque with part size.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[physics-pathfinding-and-npc-ai]]** For a part spinning on a stationary base, use a HingeConstraint with ActuatorType Motor and anchor the base so only the spinning part moves.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[physics-pathfinding-and-npc-ai]]** Use ApplyAngularImpulse for an instant spin that decelerates from friction; good for gusts of wind or event feedback.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[physics-pathfinding-and-npc-ai]]** Enable Show Constraint Details in the View menu to visualize constraint axes and rotation direction while configuring.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[physics-pathfinding-and-npc-ai]]** Orient attachment primary axes (yellow arrow) upward on Y to spin counterclockwise; reverse the sign to spin clockwise.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) **[[scripting-and-performance]]** Apply angular impulse from a server Script on the part; example uses part:ApplyAngularImpulse(Vector3.new(0, math.random(0,100), 0)).

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) Radians per full rotation: **2π ≈ 6.283; 6 rad/s ≈ one rotation per second** (Studio angular velocity unit is radians per second)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) MaxTorque in sample (default 4,1,2 block): **1000 Rowton-studs** (Constant angular force for AngularVelocity constraint on default block)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) MaxTorque for 4x-size block on grass: **at least 300000 Rowton-studs** (Needed to overcome mass and grass friction at quadruple sample size)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) Hinge propeller target angular velocity: **3 rad/s with MotorMaxTorque 1000** (HingeConstraint motor on propeller with anchored base)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/create-spinning-objects) Random impulse range on Y axis: **0 to 100 Rowton-studs** (Sample ApplyAngularImpulse script)

## Tools
Roblox Studio, Constraints: AngularVelocity, HingeConstraint, Attachments, BasePart:ApplyAngularImpulse, Creator Store / Toolbox

## He points to
- Spinning Objects .rbxl sample file
- Roblox Units documentation
- Exporting Requirements documentation

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
