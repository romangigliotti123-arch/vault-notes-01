---
title: "Docs: performance-optimization / microprofiler / task-scheduler"
url: https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / microprofiler / task-scheduler

[Open](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on the task scheduler: what runs each frame (input, animation, physics, replication, Heartbeat/render steps), when overload happens, and where to put physics-affecting vs physics-reading logic (PreSimulation vs PostSimulation), plus Motor6D transform timing.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[optimization-and-streaming]]** Don't bind functions to the render step unless necessary; reserve it for work that must run after input but before rendering, like camera movement.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[scripting-and-performance]]** Use RunService:BindToRenderStep() instead of PreRender when you need strict control over execution order.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[physics-pathfinding-and-npc-ai]]** Set physics-affecting gameplay logic (e.g. BasePart.Velocity) in RunService.PreSimulation, which runs before physics.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[physics-pathfinding-and-npc-ai]]** Read physics state (e.g. BasePart.Position for zone entry detection) in RunService.PostSimulation, which runs after physics.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[3d-modeling-rigging-and-animation]]** Apply Motor6D Transform changes in PreSimulation; otherwise Animators overwrite them next frame.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[optimization-and-streaming]]** Avoid overloading the task scheduler: custom character rigs or input schemes, manually animating parts instead of using Animator, heavy precise physics, and frequent replication all add load.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler) **[[scripting-and-performance]]** Be aware Heartbeat script execution timing depends on Workspace.SignalBehavior (see Deferred events).

## Tools
Microprofiler

## He points to
- Deferred events (Workspace.SignalBehavior) docs
- Animator docs
- BindToRenderStep docs

## Topics
[[3d-modeling-rigging-and-animation]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
