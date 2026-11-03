---
title: "Docs: parts"
url: https://create.roblox.com/docs/parts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts

[Open](https://create.roblox.com/docs/parts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Parts: primitive part shapes, physics defaults (rigid bodies), assemblies via welds/joints, key properties (Anchored, CanCollide, Transparency), and Studio tools for inserting, selecting, moving, scaling, rotating, grouping, anchoring, coloring, and materials.

## Tips
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Anchor most parts; unanchored parts are affected by gravity and physics as soon as the game runs.
- [page](https://create.roblox.com/docs/parts) **[[scripting-and-performance]]** Many partially transparent parts can slow performance; merge them using solid modeling to reduce the count.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Use WeldConstraint or Motor6D/Bone to connect related parts into one rigid assembly; group them in a Model for easy handling.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Set CanCollide to false only when parts should pass through things; physics ignores non-colliding parts entirely.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Material affects physical traits (density, sinking in water), not just looks; pick materials with real-world weight in mind.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Use Visualization Options > Anchored parts to see which parts cannot move under physics.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** Use Ctrl+L (Mac Cmd+L) to toggle local vs world orientation when transforming parts.
- [page](https://create.roblox.com/docs/parts) **[[building-art-and-assets]]** For detailed or organic shapes, import third-party models as MeshParts rather than building from primitives.

## Numbers
- [page](https://create.roblox.com/docs/parts) Transparency range: **0 (fully visible) to 1 (fully transparent)** (Default is 0 for BasePart.Transparency)
- [page](https://create.roblox.com/docs/parts) Snapping increments: **Studs for move/scale; degrees for rotate** (Adjustable in toolbar; hold Shift to toggle temporarily)
- [page](https://create.roblox.com/docs/parts) Rotation shortcuts: **90° increments (Ctrl+T about X, Ctrl+R about Y)** (Quick rotation of selected objects in Studio)

## Tools
Roblox Studio, Properties window, Explorer, Visualization Options widget, Model/Home toolbar

## He points to
- Meshes
- Models
- Materials
- object selection

## Topics
[[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
