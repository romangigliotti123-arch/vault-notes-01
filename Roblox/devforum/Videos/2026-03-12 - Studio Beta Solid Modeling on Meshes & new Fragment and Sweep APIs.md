---
title: "[Studio Beta] Solid Modeling on Meshes & new Fragment and Sweep APIs"
url: https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-03-12
views: 1464
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Studio Beta] Solid Modeling on Meshes & new Fragment and Sweep APIs

[Open](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) | Roblox DevForum | 1,464 views | 2026-03-12

## Summary
Roblox Geometry Team announces Studio Beta solid modeling upgrades: GeometryService Union/Intersect/Subtract now accept watertight MeshParts and return MeshParts; new FragmentAsync, GenerateFragmentSites and SweepPartAsync APIs. Covers performance notes, limitations (MeshParts not persisted across sessions, under 20k triangles, Team Test unsupported) and best practices.

## Tips
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[building-art-and-assets]]** Use watertight (closed, non-self-intersecting) meshes for CSG operations; non-watertight meshes will not work with solid modeling APIs.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[optimization-and-streaming]]** Keep watertight meshes under 20k triangles; simplification above that likely makes the mesh non-solid.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[optimization-and-streaming]]** Be judicious with fragment counts: each fragment becomes a simulated physics instance. Use Debris service to clean up unneeded pieces.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[optimization-and-streaming]]** Filter out very close CFrames from mouse/touch input before SweepPartAsync, since many CFrames create very large triangle counts.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[optimization-and-streaming]]** Be aware CSG-created MeshParts keep a copy of mesh data in memory, giving a higher footprint than standard assets.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[optimization-and-streaming]]** The optional MeshPreloader (no-op CSG) cuts first-operation latency but costs memory; enable only if latency matters.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[building-and-level-design]]** Use SubstituteGeometry/ApplyMesh to update a part's shape while keeping its children intact, instead of replacing the part (avoids flicker).
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[client-server-and-remotes]]** Use GeometryService:CalculateConstraintsToPreserve to keep constraints (e.g., a trashcan top attached to a post) when doing solid modeling ops.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[common-mistakes]]** Do not rely on CSG-created MeshParts persisting: they are lost on Studio restart or publish until Roblox lifts this restriction.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[common-mistakes]]** Textures on tool MeshParts are discarded in CSG; only geometry and vertex colors carry over, so the main part's texture is preserved.
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) **[[testing-debugging-and-qa]]** New CSG APIs do not work in Team Test sessions during the beta; test in a published or local play session instead.

## Numbers
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) Face count limit for solid meshes: **under 20k triangles** (Above this, simplification likely makes mesh non-solid)
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) Example watertight assets: **12 asset IDs listed** (Trashcans, barriers, stool, statue, sofa, moon rock, etc.)
- [page](https://devforum.roblox.com/t/studio-beta-solid-modeling-on-meshes-new-fragment-and-sweep-apis/4515374) Sweep example: **50 CFrames** (Spiral sweep of a ball in the demo snippet)

## Tools
GeometryService, FragmentAsync, GenerateFragmentSites, SweepPartAsync, SubtractAsync, CalculateConstraintsToPreserve, SubstituteGeometry/ApplyMesh, Debris service

## He points to
- Solid modeling guide (Roblox docs)
- Solid Modeling on Meshes Studio Beta demo place (RBXL)
- Solid Modeling Early Access program

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
