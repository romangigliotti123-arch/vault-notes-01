---
title: "Docs: workspace / raycasting"
url: https://create.roblox.com/docs/workspace/raycasting.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / raycasting

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/workspace/raycasting.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs on raycasting: casting rays with Workspace:Raycast from an origin along a direction vector, filtering with RaycastParams (exclude/include lists, IgnoreWater, collision groups), and reading RaycastResult fields. Covers streaming and CanQuery caveats.

## Tips
- [page](https://create.roblox.com/docs/workspace/raycasting) **[[scripting-and-performance]]** Set the direction vector's magnitude to the desired ray length; maximum ray length is 15,000 studs.
- [page](https://create.roblox.com/docs/workspace/raycasting) **[[scripting-and-performance]]** Compute rayDirection as destination minus origin when casting between two moving points, such as two player characters.
- [page](https://create.roblox.com/docs/workspace/raycasting) **[[scripting-and-performance]]** Pass a RaycastParams object to exclude your own character or script parent so the ray does not hit itself.
- [page](https://create.roblox.com/docs/workspace/raycasting) **[[optimization-and-streaming]]** Raycasts may miss distant BaseParts when instance streaming is enabled, since clients may not have them loaded; streamed imposter terrain/models are not targets.

## Numbers
- [page](https://create.roblox.com/docs/workspace/raycasting) Maximum raycast length: **15,000 studs** (Ray length equals magnitude of direction vector; hard maximum)

## Tools
Workspace:Raycast, RaycastParams, RaycastResult

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
