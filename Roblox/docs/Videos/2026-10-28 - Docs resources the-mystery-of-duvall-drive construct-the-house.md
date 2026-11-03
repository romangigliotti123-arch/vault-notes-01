---
title: "Docs: resources / the-mystery-of-duvall-drive / construct-the-house"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / construct-the-house

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs case study on building "The Mystery of Duvall Drive" house: start with 2D layout and terrain, gray-box with simple parts early for fast playtesting, plan rooms, reuse textures for memory budget, convert CC0 photogrammetry to low-poly PBR assets, and use packages so one edit updates every instance.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[development-process-and-speed]]** Get ideas into 3D and playable quickly; use simple parts and Creator Store assets as temporary placeholders so you can playtest within the first few days.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-and-level-design]]** Sketch a 2D layout first, then block out terrain for surroundings; test how long it takes to reach the main location and avoid a 'straight shot' path.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-and-level-design]]** Use bends, dense trees and elevation changes to hide paths and encourage exploration; raise approaches so players must climb for a more intimidating feel.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-and-level-design]]** Plan puzzle difficulty by placement: put harder puzzles farther from the entrance so players don't stumble onto them first.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[development-process-and-speed]]** Build early versions with an avatar in Studio to check scale of doors, steps and ceilings.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-art-and-assets]]** Track all furniture and props in one planning document, prioritized by room type, to avoid making too few or too many assets.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-art-and-assets]]** Reuse tileable textures and transparent textures with color tint to stay within memory budget instead of making unique albedo maps.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[3d-modeling-rigging-and-animation]]** When using photogrammetry, retopologize and rebake to low-poly with PBR textures free of baked lighting; the team cut a ~1,000,000-vertex scan down to ~1,000 vertices.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[optimization-and-streaming]]** Mobile experiences are limited to 10,000 vertices per mesh; avoid scan UVs made of many separate planes.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[building-art-and-assets]]** Use packages for shared objects, room states and SurfaceAppearance materials so one edit updates every instance; set parent packages to auto-update.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[core-loops-and-game-design]]** Use packages to build alternate states (normal vs corrupt room) from one shared package, keeping only differences outside it.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[development-process-and-speed]]** Keep an asset storage place with package links so package edits propagate to all places without working in the main game file.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) **[[team-and-budget]]** Set the group as package creator so all members can edit packages and share them across every game the group owns.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) Mesh vertex limit on mobile: **10,000 vertices** (Cited as the mobile performance constraint for photogrammetry UV layouts)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) Retopologized asset vertex count: **~1,000 vertices vs ~1,000,000 scan** (Scan-data asset reduced for memory budget; quality trade-off accepted)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) Retopologized texture size: **512px PBR textures** (Size used for newly baked Albedo, Normal, Metalness, Roughness maps)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/construct-the-house) Playtest start: **within the first few days** (Achieved by using placeholder simple parts and Creator Store assets)

## Games
- **The Mystery of Duvall Drive**: House built as main character with exterior terrain, road bends and tree occlusion to draw players toward it; packages used for room states.

## Tools
Roblox Studio, Packages, Creator Store, Blender-style 3D app (unspecified), 3DS Max, ZBrush, Marmoset, Substance Painter

## He points to
- Planning, Reuse, and Budgets (Roblox docs)
- Packages (Roblox docs)
- CC0 museum scan content

## Topics
[[3d-modeling-rigging-and-animation]] [[building-and-level-design]] [[building-art-and-assets]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[optimization-and-streaming]] [[team-and-budget]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
