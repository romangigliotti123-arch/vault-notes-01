---
title: "Docs: physics"
url: https://create.roblox.com/docs/physics.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox physics docs overview: rigid body engine, assemblies formed by parts joined with constraints or motors, mechanical and mover constraints, collision events and filtering, distributed network ownership between server and clients, adaptive timestepping into three simulation rates, and the sleep system for idle assemblies. Mostly a map to linked guides.

## Tips
- [page](https://create.roblox.com/docs/physics) **[[physics-pathfinding-and-npc-ai]]** For complex mechanisms like tanks, set a fixed timestep to improve stability instead of relying on adaptive timestepping.
- [page](https://create.roblox.com/docs/physics) **[[optimization-and-streaming]]** Engine automatically sleeps assemblies that are not moving or accelerating; keep idle physics objects still to benefit from lower simulation cost.
- [page](https://create.roblox.com/docs/physics) **[[client-server-and-remotes]]** Physics is distributed: the engine assigns network ownership of simulated parts to a client or server. Review the network ownership guide when building responsive physics.
- [page](https://create.roblox.com/docs/physics) **[[physics-pathfinding-and-npc-ai]]** Use collision groups or part-to-part filtering to control which assemblies collide with each other.

## Numbers
- [page](https://create.roblox.com/docs/physics) simulation rates: **3 (adaptive timestepping assigns assemblies)** (Engine automatically assigns assemblies to one of three simulation rates)
- [page](https://create.roblox.com/docs/physics) example assembly sizes: **1, 18, 179 parts** (Example assembly captions shown in docs; illustrative only)

## Tools
Roblox physics engine, Constraints (hinge, spring, rope, mover), Collision groups, Attachments

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
