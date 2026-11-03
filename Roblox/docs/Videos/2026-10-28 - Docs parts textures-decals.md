---
title: "Docs: parts / textures-decals"
url: https://create.roblox.com/docs/parts/textures-decals.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / textures-decals

[Open](https://create.roblox.com/docs/parts/textures-decals.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Textures and Decals. Explains Texture (repeats per StudsPerTileU/V, offsettable and tweenable) versus Decal (stretches to surface), how to add them to a part face, color tint and transparency, and automatic texture streaming with its benefits and asset-atlas guidance.

## Tips
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[building-art-and-assets]]** Use a Texture instead of a Decal when the image must tile across a surface; Texture repeats, Decal stretches to fit the face.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[building-art-and-assets]]** Scaling a part does not change a Texture's tile size; it only changes repeat count. Set StudsPerTileU/V to control tile size.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[optimization-and-streaming]]** Favor unique individual textures over texture atlases unless the atlas is on batchable parts; a high-res request for one atlas tile streams the whole atlas at that resolution.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[optimization-and-streaming]]** Keep near-uniform texel density in UV-mapped meshes so the engine can pick the best resolution per texture.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[optimization-and-streaming]]** Texture streaming is automatic; still manage texture memory for instance types it does not yet support.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[vfx-and-particles]]** Animate Texture OffsetStudsU/V or StudsPerTileU/V with TweenService (repeating, reversed tweens) to fake moving fog or scrolling surfaces.
- [page](https://create.roblox.com/docs/parts/textures-decals) **[[ui-ux-design]]** Enable Show Orientation Indicator in Studio right-click menu to confirm which face is Top/Front before assigning Face.

## Numbers
- [page](https://create.roblox.com/docs/parts/textures-decals) Color3 default: **[255,255,255]; Transparency default 0 (visible), range 0 to 1** (Decal/Texture tint and transparency defaults)
- [page](https://create.roblox.com/docs/parts/textures-decals) StudsPerTile example: **2 and 4** (Example tile sizes shown in docs)
- [page](https://create.roblox.com/docs/parts/textures-decals) Tween example timing: **8s and 7s, looping (-1 repeat count)** (Animated fog script example durations)

## Tools
Roblox Studio, TweenService, Show Orientation Indicator

## He points to
- Roblox Creator Docs: Textures and decals
- Community Rules and Terms of Use

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
