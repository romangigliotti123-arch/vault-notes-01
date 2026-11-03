---
title: "Docs: parts / solid-modeling"
url: https://create.roblox.com/docs/parts/solid-modeling.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / solid-modeling

[Open](https://create.roblox.com/docs/parts/solid-modeling.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on solid modeling: boolean CSG (union, intersect, subtract/negate, separate) in Studio and in-game via GeometryService, plus beta mesh features SweepPartAsync and FragmentAsync. Covers watertight mesh requirements, repair options, and async performance caveats.

## Tips
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[building-and-level-design]]** Do not call GeometryService UnionAsync or similar in rapid succession; the operations are async and can hurt performance. Batch or space them out.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[optimization-and-streaming]]** Fragmenting creates massive numbers of small pieces. Always add a cleanup system, such as Debris service removal after a set time, when letting users fragment objects.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[building-art-and-assets]]** Solid modeling on meshes requires watertight geometry: closed, manifold, non-self-intersecting. Check with DoubleSided toggling; if the mesh looks different, it is a shell and repair tools will fail.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[3d-modeling-rigging-and-animation]]** For thin shell meshes where exact dimensions do not matter, use Blender's Solidify modifier to thicken them into watertight meshes. Repair tools: 3D Print Toolbox, Mesh Repair Tools, MeshLab.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[scripting-and-performance]]** Wrap GeometryService calls in pcall, since operations fail on non-watertight meshes or meshes exceeding limits.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[scripting-and-performance]]** Use SplitApart = false when you want one result part rather than separate bodies; default is true, returning each body as its own part.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[client-server-and-remotes]]** Client-side solid modeling only works on objects created on the client and does not replicate to the server. Do server-side work for shared geometry.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[building-and-level-design]]** Returned parts share the main part's origin, so a part's (0,0,0) is not its center. Parent results to the main part's parent, match its CFrame and Anchored state, then destroy originals.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[optimization-and-streaming]]** Results over 20,000 triangles are simplified to 20,000; operations with thousands of non-overlapping components can error. Keep boolean inputs modest.
- [page](https://create.roblox.com/docs/parts/solid-modeling) **[[combat-and-gameplay-systems]]** For slicing mechanics, record mouse positions as CFrames client-side, send them via RemoteEvent, and build the sweep and subtract on the server.

## Numbers
- [page](https://create.roblox.com/docs/parts/solid-modeling) Max triangles per result part: **20,000 (simplified beyond this)**
- [page](https://create.roblox.com/docs/parts/solid-modeling) Edge rule for watertight meshes: **Each edge shared by exactly two triangles**
- [page](https://create.roblox.com/docs/parts/solid-modeling) Default fragment site spacing (non-localized): **(volume / 5)^(1/3) of part**
- [page](https://create.roblox.com/docs/parts/solid-modeling) Localized fragment spacing default: **radius * 0.5**
- [page](https://create.roblox.com/docs/parts/solid-modeling) Hand-written fragment site generation: **50+ lines of Luau for well-behaved points**

## Tools
Roblox Studio Model tab (Union, Intersect, Separate, Negate), GeometryService (UnionAsync, IntersectAsync, SubtractAsync, SweepPartAsync, FragmentAsync, GenerateFragmentSites), CollectionService rbxNegate tag, Blender Solidify modifier, 3D Print Toolbox, Mesh Repair Tools, MeshLab, Debris service

## He points to
- Roblox docs: PartOperation:SubstituteGeometry()
- Roblox docs: MeshPart:ApplyMesh()

## Topics
[[3d-modeling-rigging-and-animation]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
