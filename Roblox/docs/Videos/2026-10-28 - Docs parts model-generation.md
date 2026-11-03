---
title: "Docs: parts / model-generation"
url: https://create.roblox.com/docs/parts/model-generation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / model-generation

[Open](https://create.roblox.com/docs/parts/model-generation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page on GenerationService:GenerateModelAsync for creating multi-mesh, functional 3D models from text prompts and preset schemas (Car5, Body1). Covers schema-based part separation, bounding-box scaling, anchoring, and retargetable behavior scripts (car and airplane examples).

## Tips
- [page](https://create.roblox.com/docs/parts/model-generation) **[[building-art-and-assets]]** Use PredefinedSchema "Car5" for a car with body and four wheels; functional vehicles need at least five separate MeshParts.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[scripting-and-performance]]** Wrap GenerateModelAsync in pcall and warn on failure; always check success before using the returned model.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[building-art-and-assets]]** Scale generated models with GetExtentsSize and ScaleTo to a target size, using the largest axis as the reference.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[building-art-and-assets]]** Anchor all BaseParts of a generated model so separate meshes do not fall apart when spawned.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[client-server-and-remotes]]** Generate models on the server; generated objects replicate to all players so players can build together in real time.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[development-process-and-speed]]** Use retargetable behavior scripts (makeFunctional modules) to attach driving or flying behavior to arbitrary generated geometry instead of hand-building each model.
- [page](https://create.roblox.com/docs/parts/model-generation) **[[scripting-and-performance]]** Set an optional max triangle count and specify bounding boxes to keep generated objects performant and correctly proportioned.

## Numbers
- [page](https://create.roblox.com/docs/parts/model-generation) MeshParts required for a drivable car: **at least 5 (body + 4 wheels)** (Car5 schema minimum for functional wheeled vehicle)
- [page](https://create.roblox.com/docs/parts/model-generation) Example target size for car: **16 studs (largest axis)** (Scale factor computed from math.max of extents)
- [page](https://create.roblox.com/docs/parts/model-generation) Example target size for airplane: **30 studs (largest axis)** (Body1 paper airplane example)
- [page](https://create.roblox.com/docs/parts/model-generation) Airplane forwardSpeed / turnSpeed config: **80 / 8** (Example config for Body1 plane behavior)

## Tools
GenerationService:GenerateModelAsync, Roblox Studio Explorer, Import Roblox Model (Behaviors.rbxm)

## He points to
- Behaviors.rbxm (retargetable behavior assets)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
