---
title: "Improved AnimationConstraint: Stable, Mass-Independent Tracking for Physically-Simulated Joints"
url: https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-06-23
views: 131
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Improved AnimationConstraint: Stable, Mass-Independent Tracking for Physically-Simulated Joints

[Open](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) | Roblox DevForum | 131 views | 2026-06-23

## Summary
Roblox Physics Team announces a 3-phase rollout of AnimationConstraint improvements (Workspace.ImprovedAnimationConstraint) replacing the PD controller for non-kinematic constraints with a soft-constraint formulation. Adds four mass-independent properties (AngularStrength, AngularDamping, LinearStrength, LinearDamping) and explains tuning for chains and held objects.

## Tips
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** Test on your game now by setting Workspace.ImprovedAnimationConstraint = Enabled; Phase 1 feedback shapes Phase 2/3 timing.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** Strength/Damping properties only apply when IsKinematic = false; kinematic constraints are unchanged.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** Pin AngularStrength = 1 (60 Hz) and tune AngularDamping upward rather than raising AngularStrength, which can cause overcorrection/wobble.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** When a held object's effective inertia changes, scale upstream AngularDamping by the square root of the new/original inertia ratio (e.g., inertia x4 means damping x2).
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** For a root joint with a BallSocketConstraint handling position, set LinearStrength = 0 and drive orientation with angular parameters only.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** Keep MaxForce and MaxTorque as hard limits; they still cap the resulting force and torque.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[common-mistakes]]** Do not assume legacy PD overshoot or wobble is preserved; games relying on it may change behaviour, so test before Phase 2.
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[roblox-platform-changes]]** Phase 2 target is July 21, 2026 (Default becomes Enabled; opt out with Disabled); Phase 3 target is September 15, 2026 (flag removed, changes unconditional).
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) **[[physics-pathfinding-and-npc-ai]]** Use damping ratio 1 for critically damped, below 1 for ringing/oscillation, above 1 for slow approach without overshoot.

## Numbers
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) Default property value: **1 (AngularStrength, AngularDamping, LinearStrength, LinearDamping)**
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) AngularStrength frequency mapping: **AngularStrength = f/60; 1 = 60 Hz**
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) Phase 1 date: **June 23, 2026 (opt-in, Default = Disabled)**
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) Phase 2 target: **July 21, 2026 (Default = Enabled)**
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) Phase 3 target: **September 15, 2026 (flag removed)**
- [page](https://devforum.roblox.com/t/improved-animationconstraint-stable-mass-independent-tracking-for-physically-simulated-joints/4700211) Damping scaling rule: **Multiply AngularDamping by sqrt(new/original effective inertia); x4 inertia -> x2 damping**

## Tools
Roblox Studio, AnimationConstraint, BallSocketConstraint

## He points to
- Roblox Physics Team rollout thread (DevForum, by m0bsterlobster)

## Topics
[[common-mistakes]] [[physics-pathfinding-and-npc-ai]] [[roblox-platform-changes]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
