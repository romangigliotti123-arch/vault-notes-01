---
title: "Docs: workspace / collisions"
url: https://create.roblox.com/docs/workspace/collisions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / collisions

[Open](https://create.roblox.com/docs/workspace/collisions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on collisions: collision events (Touched/TouchEnded vs CanTouch/CanCollide), debounce pattern, collision summaries via BindToCollisionSummaries, collision groups (Studio editor and scripting), part-to-part NoCollision constraints, disabling character collisions, model collision handling, and mesh CollisionFidelity options.

## Tips
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Set CanTouch to false on objects that don't need collision events to improve performance.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[client-server-and-remotes]]** Collision summaries are not replicated; process them on the network owner and send only needed data via your own RemoteEvent.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Don't call BindToCollisionSummaries from inside a Touched handler; it is a separate API. Disconnect the connection when no longer needed.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Debounce Touched handlers with an attribute cooldown, since Touched can fire repeatedly from settling or multi-part contacts.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Register all collision groups in a single script to avoid race conditions where a group is not yet registered when assigned.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Use NoCollisionConstraint for part-to-part filtering (e.g. wheel vs chassis) so models stay shareable without configuration scripts.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[scripting-and-performance]]** Use Box or Hull CollisionFidelity for small or non-interactive meshes; PreciseConvexDecomposition is the most expensive and slowest to compute.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[common-mistakes]]** Touched and TouchEnded do not fire when Position or CFrame is set directly to intersect a part; they only fire from physical movement.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[common-mistakes]]** Models cannot connect Touched directly; loop over child BaseParts and connect each one.
- [page](https://create.roblox.com/docs/workspace/collisions) **[[client-server-and-remotes]]** Disable player character collisions via a server Script that sets a non-collidable 'Characters' group on descendant parts when characters are added.

## Numbers
- [page](https://create.roblox.com/docs/workspace/collisions) Collision summary impact speed threshold (example): **10** (Example code prints hard impact when dot(RelativeVelocity, Normal) > 10)
- [page](https://create.roblox.com/docs/workspace/collisions) Debounce cooldown (example): **1 second** (COOLDOWN_TIME constant in Touched debounce example)
- [page](https://create.roblox.com/docs/workspace/collisions) Brute force raycast (plugin example): **BruteForceAllSlow = true** (Lets parts with CanQuery false be selected in plugin raycasts)

## Tools
Studio Collision Groups editor (Window > 3D), Visualization Options: Collision fidelity toggle, BindToCollisionSummaries, RegisterCollisionGroup / CollisionGroupSetCollidable, NoCollisionConstraint, RaycastParams

## He points to
- Roblox docs: performance optimization (collision fidelity)
- Roblox docs: mesh and solid model collisions

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
