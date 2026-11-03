---
title: "[Improved] How to Actually Improve Performance in Your Games"
url: https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-05-12
views: 628
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Improved] How to Actually Improve Performance in Your Games

[Open](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) | Roblox DevForum | 628 views | 2021-05-12

## Summary
Bearturnedhuman's DevForum post (May 2021) listing performance tips for Roblox games, split into general advice and Luau scripting practices. Covers collision/render fidelity, CanQuery, lighting, anchoring, textures vs materials, humanoid cost, task library, and Instance.new parenting. Author warns the earlier post is outdated.

## Tips
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Disable CanTouch and CanCollide (and CanQuery) on parts that need no physics or interaction; they can still be hit by raycasts and Region3 queries.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Use Voxel lighting or skip ShadowMap/Future if you don't need them; this can dramatically reduce lag.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Set CollisionFidelity to Box on Unions and MeshParts to reduce physics work for server and client.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Set RenderFidelity to Performance on distant BaseParts/MeshParts to reduce rendering cost.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Anchor parts that shouldn't move; unanchored parts force extra physics calculation and cause lag.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Use partial transparency sparingly; merge several transparent parts into one transparent union for better rendering optimization.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[building-art-and-assets]]** Prefer built-in materials and MaterialService over textures, since textures use more memory (GraphicsTexture in Developer Console).
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Stress test with many players and lower MaxPlayers per server if performance suffers.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Avoid dozens of humanoids clustered together; disabling HumanoidStateTypes made no measurable difference per the author. Consider non-humanoid NPCs.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[client-server-and-remotes]]** Keep server-only objects in ServerStorage instead of ReplicatedStorage; anything in replicated containers must be sent to clients, costing resources.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Use in-experience content streaming to dynamically load and unload world regions.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[optimization-and-streaming]]** Split large games into multiple places and teleport players between them so each place loads less.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[scripting-and-performance]]** Replace while true do loops with .Changed, GetPropertyChangedSignal, or RunService events where possible.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[scripting-and-performance]]** Use task.wait() instead of wait(); it is safe and equivalent to RunService.Heartbeat:Wait().
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[scripting-and-performance]]** Set Instance parent on a separate line (instance.Parent = x) instead of Instance.new(class, parent); the latter is slower.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[scripting-and-performance]]** Store expensive results like GetChildren() or threshold calculations outside loops instead of recomputing per iteration.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[luau-language-and-types]]** Use the task library (task.spawn, task.defer) in place of wait-based spawn(); use += and -= operators.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[common-mistakes]]** Don't blindly avoid FindFirstChild; avoid it only where it isn't needed. Don't avoid _G just because it's called bad practice; storing everything in it is the problem.
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) **[[client-server-and-remotes]]** Disconnect event connections with Disconnect() or Once() for one-time events; Destroy() on a script disconnects its connections.

## Numbers
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) Voxel lighting impact: **can make performance do a '180' in lag terms (author's claim, no figure)**
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) Textures vs materials: **textures use more memory than materials**

## Tools
Developer Console (Memory tab), MaterialService, RunService, task library

## He points to
- Roblox official Improve Performance docs
- Roblox Handling Events doc
- Roblox Lighting doc
- Roblox content streaming doc

## Quotes
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) "Use partial object Transparency sparingly, as semi-transparent objects inhibit a lot of internal rendering optimizations."
- [page](https://devforum.roblox.com/t/improved-how-to-actually-improve-performance-in-your-games/1221842) "Anchor things that shouldn't move! This makes Roblox calculate more physics, thus causing beautiful lag."

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[luau-language-and-types]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
