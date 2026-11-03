---
title: "Building Optimisation | Tips and tricks!"
url: https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059
creator: Roblox DevForum
official: false
advice_density: high
date: 2019-02-02
views: 565
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Building Optimisation | Tips and tricks!

[Open](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) | Roblox DevForum | 565 views | 2019-02-02

## Summary
Mariofly5's 2019 (updated 2021) guide on Roblox build optimisation: texture/decal cost, part vs union vs mesh memory, CollisionFidelity, CanCollide myths, terrain voxels, and transparency. Points to the Performance widget and RDC 2018 talks.

## Tips
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-art-and-assets]]** Don't put textures/decals on every side of a part; only on faces players see. A brick with textures on all 6 sides is roughly 7x more expensive to draw than a plain material brick.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-art-and-assets]]** Use materials instead of textures where possible, but use Neon and Glass sparingly; they are the most costly materials.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[optimization-and-streaming]]** Use the Performance/Memory stats widget and Developer Console to measure memory in Studio and in-game before deciding what to optimise.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-art-and-assets]]** Compare Parts, Unions and MeshParts with the Performance Analyser; Meshes are typically most efficient per unit of detail, Unions medium, welded/squished Parts worst. Union when short on time, but not habitually.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[optimization-and-streaming]]** For unions in detailed areas, set CollisionFidelity to Hull or Box, but only for parts the player will not touch; otherwise optimise or swap to parts/meshes.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[physics-pathfinding-and-npc-ai]]** CanCollide only matters for moving objects near players. For reachable details, set CanCollide false and use a hitbox; unreachable details matter little.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[optimization-and-streaming]]** Monitor Terrain Physics and Voxels in the Performance widget; hollowing terrain reduces memory, but the hollow tool alone can add excess detail (about 3MB voxels and 5MB physics in the author's test).
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-art-and-assets]]** Terrain has little memory impact, so use a variety of terrain materials freely; water has a slight cost but is fine to use.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-art-and-assets]]** Avoid many parts with varying transparency. Use transparency 0 or 1 and merge several glass parts into one part to reduce render work.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[optimization-and-streaming]]** Never put decals or textures on fully transparent objects; this causes mobile performance problems per Zeuxcg.
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) **[[building-and-level-design]]** Match detail to the game style and abstract away unnecessary detail, such as props seen from only 1 or 3 sides.

## Numbers
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) texture render cost: **~7x** (Brick with textures on all 6 sides vs plain material brick)
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) terrain voxel memory after hollow tool: **3 MB** (Author's test on hollowed mountain terrain)
- [page](https://devforum.roblox.com/t/building-optimisation-tips-and-tricks/235059) terrain physics memory after hollow tool: **5 MB** (Author's test on hollowed mountain terrain)

## Tools
Performance widget, Developer Console, Performance Analyser, Blender, CollisionFidelity setting

## He points to
- RDC 2018 'Designing for Performance' panel
- Zeuxcg RDC 18 talk on CanCollide
- Zeuxcg (cited on decals and mobile performance)

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
