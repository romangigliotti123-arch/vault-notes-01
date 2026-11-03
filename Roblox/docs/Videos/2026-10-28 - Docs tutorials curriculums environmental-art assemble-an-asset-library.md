---
title: "Docs: tutorials / curriculums / environmental-art / assemble-an-asset-library"
url: https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / environmental-art / assemble-an-asset-library

[Open](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on assembling an environment art asset library in Studio: custom MaterialVariants from tileable textures, SurfaceAppearance packages for trim sheets, applying them to unwrapped meshes, setting anchoring/collision/touch/query/shadow/render parameters for performance, and converting assets to packages for reuse.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Anchor every static environment asset; anchored parts skip physics simulation, freeing GPU for low-end devices. Exception: moving parts like doors.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Disable CanCollide on objects users never touch (e.g. foliage) to reduce physics calculation cost.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Enable CanTouch only on parts that must fire Touched/TouchEnded; the engine checks touch state every frame for every part.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Disable CanQuery on parts raycasts don't need to consider; keep it on surfaces that gameplay like lasers must hit.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Disable CastShadow on geometrically complex objects where users won't notice missing shadows, such as ceiling-piercing foliage.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Enable DoubleSided only where visual realism matters (e.g. foliage) since it renders polygons twice.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Set CollisionFidelity to Box or Hull for meshes where precise hitboxes are unnecessary; Hull for trim so users can still jump near walls.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[optimization-and-streaming]]** Set RenderFidelity to Performance for complex geometry like foliage that need not display fully at distance.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Organise imported assets into folders by data type (trim sheets, decals, modular assets, props) before importing into Studio.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Create MaterialVariants from the base material closest to your texture so it inherits physical properties; enable Set as Override to apply to terrain.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Use Organic pattern on MaterialVariant tiling to randomise output and reduce visible tiling on organic surfaces.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Store trim sheet texture maps in one SurfaceAppearance package and duplicate it onto meshes; edits to the package propagate to all instances.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library) **[[building-art-and-assets]]** Convert assets to packages and enable AutoUpdate on PackageLink so edits propagate across instances and projects.

## Tools
Roblox Studio, Material Manager, Importer, Visualization Options widget

## He points to
- Environment Art - Assembling .rbxl file (sample laser tag environment)

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
