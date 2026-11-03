---
title: "The Hitchhiker's Guide To Optimization - Optimize Your Game Using Just One Post Instead of Many"
url: https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345
creator: Roblox DevForum
official: false
advice_density: high
date: 2025-01-08
views: 136
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# The Hitchhiker's Guide To Optimization - Optimize Your Game Using Just One Post Instead of Many

[Open](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) | Roblox DevForum | 136 views | 2025-01-08

## Summary
Craixzo's DevForum guide to Roblox optimization: MeshPart/Union render fidelity, StreamingEnabled, terrain hollowing, part/voxel budgets, texture size and SurfaceAppearance use, collision fidelity, and scripting habits (task.wait, avoiding while true, ServerStorage, centralized scripts). Community-tested, not formally benchmarked.

## Tips
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Replace every wait() with task.wait(); wait() is deprecated and can be unoptimized.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Avoid while true do loops; use event-driven code unless no other option exists.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Use one central script in ServerScriptService to control many similar parts (e.g. streetlights) instead of one script per part.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Keep the number of Heartbeat connections as low as possible.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Skip FindFirstChild when the child is guaranteed to exist.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Do not use anti-lag scripts; the guide says they do the opposite of what they claim.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Enable StreamingEnabled; for models that break under streaming, set the model's ModelStreamingMode to Persistent.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Set MeshParts to Performance render fidelity and Unions to Automatic via command-bar scripts run separately.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Hollow out terrain with Subtract and remove hidden terrain that players never see; keep voxel count under 100 million.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Keep parts (including MeshParts) around 75k so mobile devices can manage them.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Avoid flat terrain surfaces where possible; the author reports FPS gains of 15 to up to 48 in team tests.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Avoid bulk regular water; use a toolbox infinite water mesh for ocean scenes.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Convert Unions to MeshParts via Export Selection, since Roblox optimizes MeshParts better; resize and reposition after.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Set CollisionFidelity to Box on non-collidable MeshParts and Unions, but not for parts used with CanTouch.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Avoid DoubleSided and PreciseConvexDecomposition on MeshParts; they are not optimized.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Keep textures and decals around 512x512; keep decals under 500x500 for mobile players.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Prefer SurfaceAppearance or custom materials over Textures, since Textures are checked on all six faces and hurt mobile.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Disable shadows on very small parts and on parts players rarely see.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Reuse meshes and be careful changing transparency or color on shared meshes.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[building-art-and-assets]]** Compress images before upload (e.g. imagecompressor.com) to cut texture size.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[optimization-and-streaming]]** Keep CanTouch and CanQuery off unless needed; they cause lag when many build up. CanQuery only appears when CanCollide is off.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[testing-debugging-and-qa]]** Use a part counter plugin to find part-count problems; use Bulk Audio Manager to find broken audio IDs.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Set all RaycastFilterTypes to Include or Exclude rather than deprecated options.
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) **[[scripting-and-performance]]** Store rarely client-needed assets in ServerStorage instead of ReplicatedStorage to reduce client load.

## Numbers
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) Voxel budget: **Under 100 million voxels for ideal experience on all devices** (Author's guideline for terrain voxel count)
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) Part count target: **~75k parts** (Level manageable by mobile devices, per author)
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) FPS gain from flattening terrain: **15 to up to 48 FPS** (Internal team test results reported by author)
- [page](https://devforum.roblox.com/t/the-hitchhikers-guide-to-optimization-optimize-your-game-using-just-one-post-instead-of-many/3358345) Texture/decal size: **512x512 (decals under 500x500 for mobile)** (Recommended for mobile rendering)

## Tools
Command bar scripts (MeshPart/Union fidelity), Bulk Audio Manager plugin, Part Counter plugin, imagecompressor.com

## He points to
- imagecompressor.com
- 440obama command-bar script
- sandofamber CollisionFidelity script
- AGoodGuyHere (FindFirstChild advice)
- wastbo (mesh reuse)

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
