---
title: "Docs: resources / the-mystery-of-duvall-drive / stream-in-immersion"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / stream-in-immersion

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on using instance streaming in The Mystery of Duvall Drive. Covers three streaming dependency issues, hiding streaming gaps with winding paths and blocking geometry, and using scale and tree height to keep distant content visible.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[building-and-level-design]]** Enable streaming on the workspace with default settings first, then tune min/max streaming distance to suit your game.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[building-and-level-design]]** Place nearby blocking geometry (trees, bushes, hills) along all player paths so players are always surrounded by streamable assets.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[building-and-level-design]]** Use winding paths to hide distant unloaded content from the player's line of sight.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[building-and-level-design]]** Make distant sky or large assets big enough to fall within the streaming distance so they load before the player expects them.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[building-and-level-design]]** Increase height of surrounding trees to block the view of distant assets that have not loaded yet.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[scripting-and-performance]]** Do not have client scripts scan the workspace for required instances at game start; streamed instances may not be loaded yet.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) **[[scripting-and-performance]]** Check whether scripts or elements depend on other content, since dependencies may be unloaded at certain times.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) Streaming max distance example: **64 studs (small) vs 1024 studs (large)** (Example streaming max distance settings shown in docs)

## Games
- **The Mystery of Duvall Drive**: Used winding driveway, blocking trees, and oversized sky models to hide streaming load gaps while keeping the world immersive.

## Tools
Roblox Studio instance streaming

## Topics
[[building-and-level-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
