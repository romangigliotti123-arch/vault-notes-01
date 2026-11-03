---
title: "Docs: performance-optimization / design"
url: https://create.roblox.com/docs/performance-optimization/design.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / design

[Open](https://create.roblox.com/docs/performance-optimization/design.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on designing for performance: target baseline low-end devices, watch draw calls/triangles and memory, use instance streaming, reuse assets and built-in materials, avoid partial transparency, and keep per-frame scripting cheap by spreading work across frames.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[optimization-and-streaming]]** Choose one baseline low-end device and test on it throughout development; watch frame rate and memory, not just Studio results.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[optimization-and-streaming]]** Keep draw calls under about 1,000 and triangles under about 1,000,000 on your baseline device, per the docs' example thresholds.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[optimization-and-streaming]]** Don't rely on the Studio device emulator for memory; Studio runs server and client together, so memory use is significantly higher than on a real device.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[optimization-and-streaming]]** Enable instance streaming for most places, especially large ones; it improves join times, reduces memory, and raises frame rate.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[optimization-and-streaming]]** Splitting a large place into multiple places reduces initial join time but adds join time on each teleport; weigh this against streaming.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[building-art-and-assets]]** Use built-in materials where possible to save memory budget for the custom textures central to your game.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[building-art-and-assets]]** Convert assets into packages during creation to avoid duplicate assets with different IDs, which hurt performance.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[building-art-and-assets]]** Reuse meshes and textures instead of importing duplicates; resize, rotate and overlap them to build varied environments with few draw calls.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[vfx-and-particles]]** Avoid transparency values other than 0 and 1; partial transparency causes high overdraw, so use it sparingly.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Prefer event-driven code over per-frame calculations; at 60 FPS each frame has a 16.67 ms budget.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Break long-running work into chunks (e.g. 5 ms per frame with task.wait) instead of one 100 ms block, which would cap a per-frame task at 10 FPS or cause stutter.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Consider Parallel Luau (multithreading) for heavy work that can run off the main thread.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Call Disconnect() on connections you no longer need so functions stop firing unnecessarily on later events.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Call a method once, store the result in a variable, and update it when needed instead of calling it every time you need the value.
- [page](https://create.roblox.com/docs/performance-optimization/design) **[[scripting-and-performance]]** Don't put everything in ReplicatedStorage, since clients load all of it; put server-only assets in ServerStorage.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/design) Draw calls budget (baseline device): **< 1,000** (Docs example threshold for smooth play on a baseline device)
- [page](https://create.roblox.com/docs/performance-optimization/design) Triangles budget (baseline device): **< 1,000,000** (Docs example threshold for smooth play on a baseline device)
- [page](https://create.roblox.com/docs/performance-optimization/design) Frame budget at 60 FPS: **16.67 ms** (Total per-frame time available at 60 FPS)
- [page](https://create.roblox.com/docs/performance-optimization/design) Example long task: **100 ms -> 10 FPS** (Running a 100 ms task every frame caps the game at 10 FPS)

## Tools
Roblox Studio, Render and Summary debug stats, Developer Console (F9), Device emulator

## He points to
- Real World Building and Scripting Optimization
- SLIM and Improve performance docs
- Remove duplicate textures docs

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
