---
title: "Docs: performance-optimization / scene-analysis"
url: https://create.roblox.com/docs/performance-optimization/scene-analysis.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / scene-analysis

[Open](https://create.roblox.com/docs/performance-optimization/scene-analysis.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Scene Analysis tool in Studio. Covers how to open it (Window > Performance Summary), its treemap-based modes (script memory, unparented instances, instance composition, audio/animation memory, triangle composition), and the SceneAnalysisService engine API exposed via MCP.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[optimization-and-streaming]]** Use Scene Analysis during play/test sessions to inspect both client and server data models for resource usage.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[optimization-and-streaming]]** Check Instance Composition regularly; each instance has replication and memory cost, so catch unintended counts (e.g. 25,000 particle emitters).
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[optimization-and-streaming]]** Deleting all instances referring to an audio track lets its memory unload; do this for unused audio.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[data-persistence]]** If chasing a memory leak, pair the Unparented Instances view with the Luau heap tool to find root cause.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[optimization-and-streaming]]** Animation assets are a common production memory leak: scripts often keep animations alive after the parent model is destroyed. Destroy all references so they unload.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[testing-debugging-and-qa]]** Scripts holding instance references is normal; only investigate Unparented Instances counts when debugging an actual leak.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[optimization-and-streaming]]** Don't trust Triangle Composition numbers as player-device figures; scaling makes a dev PC vs mid-range phone differ dramatically.
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) **[[scripting-and-performance]]** Use Script Memory view to see Luau VM heap per Script, LocalScript and ModuleScript, separate from asset memory.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/scene-analysis) Example instance count: **25,000 particle emitters (illustrative overspend)** (Example given of an unintended count the Instance Composition view would reveal)

## Tools
Roblox Studio Scene Analysis, Luau heap tool, SceneAnalysisService (Engine API, via MCP server)

## He points to
- Luau heap tool
- Roblox MCP server

## Topics
[[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
