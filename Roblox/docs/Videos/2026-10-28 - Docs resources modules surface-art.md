---
title: "Docs: resources / modules / surface-art"
url: https://create.roblox.com/docs/resources/modules/surface-art.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / surface-art

[Open](https://create.roblox.com/docs/resources/modules/surface-art.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs for the SurfaceArt package module: lets players place art on tagged SurfaceCanvas parts. Covers installation, canvas face attribute, custom assets, configure options (quota, prompt keys, grid), placeArt/removeAllArt/getCanvases functions, and client events.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[building-art-and-assets]]** Install SurfaceArt from Creator Store Packages, move the SurfaceArt model into ReplicatedStorage; module starts automatically on run.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[building-art-and-assets]]** Any BasePart tagged SurfaceCanvas works as a canvas; set its SurfaceCanvasFace attribute (Front/Back/Right/Left/Top/Bottom). Default is Right.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[scripting-and-performance]]** Call SurfaceArt.configure from a Script in ServerScriptService only; it is server-only and overrides defaults via a config table.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[building-art-and-assets]]** Custom art assets currently apply to all tagged canvases; you cannot give different canvases different asset sets.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[player-psychology-and-game-feel]]** Let players leave a visible mark on the world; the docs note players enjoy feeling part of constructing the space. Default quota is 2 pieces per player.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[client-server-and-remotes]]** Connect artChanged and promptShown/selectorShown only in LocalScripts; use artChanged to add client-side particle effects when art is placed.
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[client-server-and-remotes]]** Use placeArt(player, canvas, artId) on the server for programmatic placement; the canvas must be tagged SurfaceCanvas at server init, so use getCanvases().
- [page](https://create.roblox.com/docs/resources/modules/surface-art) **[[data-persistence]]** Player art is removed when they leave the game by default; plan persistence separately if art must survive sessions.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/surface-art) default quotaPerPlayer: **2 art pieces per player** (Max placed art per player across all tagged surfaces by default)
- [page](https://create.roblox.com/docs/resources/modules/surface-art) default grid: **2 rows x 5 columns** (rowsPerCanvas and colsPerCanvas defaults for canvas selection grid)
- [page](https://create.roblox.com/docs/resources/modules/surface-art) itemsPerPage default: **3** (Items skipped when paging left/right in art selector)
- [page](https://create.roblox.com/docs/resources/modules/surface-art) promptMaxActivationDistance default: **10 studs** (Max distance from canvas for interaction prompt to appear)

## Tools
SurfaceArt module (Creator Store package), CollectionService, SurfaceGui, ProximityPrompt

## He points to
- Roblox Creator Store Packages

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[data-persistence]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
