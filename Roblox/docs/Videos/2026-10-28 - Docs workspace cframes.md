---
title: "Docs: workspace / cframes"
url: https://create.roblox.com/docs/workspace/cframes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / cframes

[Open](https://create.roblox.com/docs/workspace/cframes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox creator docs on CFrames: constructing CFrames with CFrame.new (coordinates or Vector3), rotating with fromEulerAnglesXYZ (radians), facing with lookAt, offsetting, relative transforms via ToWorldSpace, and interpolating with Lerp.

## Tips
- [page](https://create.roblox.com/docs/workspace/cframes) **[[building-and-level-design]]** Use CFrame.fromEulerAnglesXYZ for rotation; its parameters are radians, so convert degrees with math.rad().
- [page](https://create.roblox.com/docs/workspace/cframes) **[[core-loops-and-game-design]]** Use CFrame:ToWorldSpace for offsets and rotations relative to an object's own orientation, not fixed world coordinates, when the target's position or facing can vary.
- [page](https://create.roblox.com/docs/workspace/cframes) **[[scripting-and-performance]]** Use CFrame.lookAt(pos, target) to orient a part's front surface toward a point; then apply a relative rotation to aim a different face.
- [page](https://create.roblox.com/docs/workspace/cframes) **[[building-and-level-design]]** Use CFrame:Lerp(other, alpha) to position an object between two points; alpha 0.7 places it 70% of the way from the first CFrame.
- [page](https://create.roblox.com/docs/workspace/cframes) **[[building-and-level-design]]** To offset a part by studs from its current position, add a Vector3 to CFrame.new(part.Position) rather than to the part's CFrame.

## Numbers
- [page](https://create.roblox.com/docs/workspace/cframes) Lerp alpha example: **0.7 = 70% of distance from start point** (CFrame:Lerp example between greenCube and cyanCube)
- [page](https://create.roblox.com/docs/workspace/cframes) Rotation example: **45 degrees on Y axis** (fromEulerAnglesXYZ example using math.rad(45))

## Tools
CFrame.new, CFrame.fromEulerAnglesXYZ, CFrame.lookAt, CFrame:ToWorldSpace, CFrame:Lerp, math.rad

## He points to
- Roblox creator docs: CFrames

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
