---
title: "Lag reducing tips and Organzation tips!"
url: https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-03-06
views: 149
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Lag reducing tips and Organzation tips!

[Open](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) | Roblox DevForum | 149 views | 2021-03-06

## Summary
Roblox builder AerialsAbove shares five optimization and organization tips from his seven-year showcase Springs Rock: collision fidelity settings, shadow casting under FIB3 lighting, removing hidden parts, keeping mesh triangle counts low, and naming and folder-organizing parts.

## Tips
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Set CanCollide off and Collision Fidelity to Box on plants, grass, vines, mushrooms, and tree leaves so players don't need collision calculations for tiny details.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Use Box collision fidelity for small or out-of-reach items; Default or Hull only for large items players walk on or bump into, like rocks, walls, roofs, stairs, and crates.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Hull collision fidelity is the most resource-heavy; Box is quickest; Default is a mix of both.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Disable Cast Shadow on items that don't need it, such as custom grass, unseen items, and items in pitch black when using FIB3 dynamic lighting.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Spread out light sources and avoid stacking many lights close together; each shadow costs render resources, especially from detailed meshes.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[optimization-and-streaming]]** Delete hidden or unseen parts: assets under terrain, behind walls, outside map view, duplicated copies, and stray parts out of reach.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[building-art-and-assets]]** Keep ordinary meshes like rocks, crates, tables, chairs, barrels, and bricks around 12 to 2,000 triangles instead of maxing out at 10k.
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) **[[building-art-and-assets]]** Name parts, models, and folders with short descriptive names from the start, and group related items into folders to reduce Explorer clutter.

## Numbers
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) Mesh import triangle limit: **10k triangles** (Maximum mesh size Roblox allows on import, per the author)
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) Recommended triangle count for ordinary items: **12 to 2,000 triangles** (Suggested for rocks, crates, tables, chairs, barrels, bricks)
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) Triangle equivalence: **10k tris is roughly 833 parts** (Author's rough comparison of mesh size to parts)
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) Showcase age: **7 years** (Springs Rock worked on since 2014, used as the optimization example)

## Games
- **Springs Rock**: Author's seven-year showcase used as the test case for all optimization and organization tips.

## Tools
Roblox Studio, Explorer, Properties panel

## Quotes
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) "Make sure to set all your vines, mushrooms, grass, and small plant material to off! This will have great FPS benefits in the long run!"
- [page](https://devforum.roblox.com/t/lag-reducing-tips-and-organzation-tips/1087419) "Every shadow costs resources to render."

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
