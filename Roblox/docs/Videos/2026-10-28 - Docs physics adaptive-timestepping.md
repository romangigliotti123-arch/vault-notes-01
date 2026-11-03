---
title: "Docs: physics / adaptive-timestepping"
url: https://create.roblox.com/docs/physics/adaptive-timestepping.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / adaptive-timestepping

[Open](https://create.roblox.com/docs/physics/adaptive-timestepping.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on adaptive timestepping: physics engine assigns parts to 240/120/60 Hz solver islands based on difficulty. Explains how to enable Adaptive mode, read Microprofiler scopes, visualize timesteps, and when to stay on Fixed mode.

## Tips
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[scripting-and-performance]]** Set Workspace PhysicsSteppingMethod to Adaptive; docs say it can improve physics performance by up to 2.5x and is recommended in most cases.
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[optimization-and-streaming]]** Use Microprofiler (Ctrl+F6) and pause (Ctrl+P) to check worldStep - Adaptive and LDLPGSSolver::solve island counts per frequency bucket.
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[testing-debugging-and-qa]]** Enable Studio Settings > Physics > Are Timesteps Shown to see each simulated part's rate; unoutlined parts are sleeping or not simulated.
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[optimization-and-streaming]]** Use Fixed mode (240 Hz) for racing, destruction, or tank-style mechanism games needing high accuracy and stability.
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[optimization-and-streaming]]** Avoid Adaptive if most parts default to 240 Hz; mixing with 60-120 Hz islands converts them to 240 Hz and can negate gains.
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) **[[physics-pathfinding-and-npc-ai]]** Expect high-velocity, high-acceleration and complex mechanism assemblies to be placed in the 240 Hz island; assignment criteria may change.

## Numbers
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) Physics performance gain: **up to 2.5x with Adaptive timestepping** (Docs claim; recommended in most cases)
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) Default physics rate: **240 Hz, about 4 worldsteps per 60 FPS frame** (Default Fixed mode simulation rate)
- [page](https://create.roblox.com/docs/physics/adaptive-timestepping) Solver island frequencies: **240 Hz (1dt), 120 Hz (2dt), 60 Hz (4dt)** (Adaptive buckets; emphasis on 60 Hz for performance)

## Tools
Roblox Studio Microprofiler, Studio Settings Physics tab, Workspace PhysicsSteppingMethod property

## He points to
- Roblox docs: Adaptive timestepping

## Topics
[[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
