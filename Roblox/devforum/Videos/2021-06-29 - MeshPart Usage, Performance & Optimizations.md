---
title: "MeshPart Usage, Performance & Optimizations"
url: https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-06-29
views: 337
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# MeshPart Usage, Performance & Optimizations

[Open](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) | Roblox DevForum | 337 views | 2021-06-29

## Summary
Community tutorial on MeshPart usage and optimization in Roblox Studio: when to use MeshParts over UnionOperations, triangle count, recycling MeshIds to cut load times, RenderFidelity and CollisionFidelity choices, CanCollide/CanTouch, SpecialMesh avoidance, and CastShadow. Author notes the post is partly outdated.

## Tips
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[building-art-and-assets]]** Only import MeshParts when an object can't be built efficiently from primitives; fewer triangles is the goal.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Avoid UnionOperations for most cases: they create excess triangles, bad collision wedges, and break part instancing when scripts change properties.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[building-art-and-assets]]** If a UnionOperation will be copied multiple times, export it via Export Selection and reimport as an .obj MeshPart instead.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Reuse MeshIds across objects; the engine downloads each unique MeshId once, cutting join times. Vary size, color, and rotation to hide repetition.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Don't leave RenderFidelity on Precise by default. Use Automatic for high-poly vegetation and objects, Performance for decorative or distant objects, Precise only for always-visible landmarks.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Automatic degrades triangles with distance (e.g. 3,000 tris stay full under 250 studs, halved at 250-500 studs). Performance also drops detail to protect FPS on weak devices.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Choose CollisionFidelity by cost: Box is cheapest, then Hull, then Default, with PreciseConvexDecomposition most costly and rarely justified. Test in game starting from the cheapest.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** For walk-through objects like bushes, set CanCollide and CanTouch off and CollisionFidelity to Box. Keep CanTouch on only for parts you need to script touch events on.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Stop using SpecialMeshes; they add an instance, have no RenderFidelity or CollisionFidelity, and always render full triangle count. Use MeshParts instead unless you need runtime VertexColor changes.
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) **[[optimization-and-streaming]]** Disable CastShadow on objects already in shadow, and on tiny or minor mid/high-poly details players won't look for shadows under.

## Numbers
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) RenderFidelity distance threshold: **Full triangles under 250 studs; 250-500 studs cuts 3,000 tris to half** (Automatic/Performance example from RenderFidelity API chart, 3,000-tri MeshPart)
- [page](https://devforum.roblox.com/t/meshpart-usage-performance-optimizations/1319217) Target framerate: **~60 FPS** (Author's stated goal for developers)

## Tools
Roblox Studio Wireframe Rendering, Mesh Optimization Tools plugin (CloneTrooper1019), Blender

## He points to
- RenderFidelity API documentation
- Mesh Optimization Tools plugin by CloneTrooper1019

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
