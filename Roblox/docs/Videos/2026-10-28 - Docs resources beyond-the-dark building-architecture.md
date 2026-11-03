---
title: "Docs: resources / beyond-the-dark / building-architecture"
url: https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / beyond-the-dark / building-architecture

[Open](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on building the Kerr-Newman DSR-14 space station modularly: uniform grid, stud-scale units, trim sheets with SurfaceAppearance, and packages for propagating updates across many instances.

## Tips
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-and-level-design]]** Start with Parts and rough meshes to test scale, room arrangement and paths before final art; this early stage is the most dynamic.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-and-level-design]]** Give players a clear goal, then break the direct path so they pass other areas of interest first.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Settle on one uniform grid size (station used 16 studs) for all artists and pieces so modules snap and swap easily.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Treat DCC units as studs: Studio does not convert meters or feet. One stud is roughly 28 cm real-world.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Keep the modular kit small with a few versatile pieces; each extra piece costs creation time and memory/performance budget.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Use trim sheets with multiple surface treatments per sheet to reduce draw calls and avoid splitting meshes; station used them for about 90% of architecture.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Make a trim sheet template first so map sets (e.g. clean vs rusted metal) can be swapped without rework.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[3d-modeling-rigging-and-animation]]** Use SurfaceAppearance on MeshParts only; Parts lack UV data. If trim maps have alpha, set AlphaMode from Overlay to Transparency.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Convert modular pieces and materials into packages before populating the world so updates can be pushed to all instances.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[version-control-and-tooling]]** Enable auto-update on PackageLink so package edits apply to all uses without manual 'update all'.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) **[[building-art-and-assets]]** Create a master SurfaceAppearance material library as packages; edit the master and republish to update every object using it.

## Numbers
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) Grid size: **16 studs** (Uniform grid used for station's modular set)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) Stud real-world scale: **28 cm** (Closest real-world scale for one Roblox stud)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) Trim sheet share of architecture: **90%** (Architectural elements using swappable trim sheet sets)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) Package instances: **over 1,000 wall panels** (Wall panel package instances updated instantly via package edit)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture) Target player count: **50 players** (Station size had to accommodate 50 players)

## Games
- **Beyond the Dark (Kerr-Newman DSR-14 station)**: Modular packages and trim sheets let layout and art change during playtests without rebuilding each asset.

## Tools
Roblox Studio, Packages (PackageLink), SurfaceAppearance, Maya, Blender, Substance Designer, Photoshop, 3ds Max

## He points to
- Adobe Substance Designer documentation Part 1 and Part 2 (PBR)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-and-level-design]] [[building-art-and-assets]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
