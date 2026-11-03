---
title: "ViewportFrame Masking"
url: https://devforum.roblox.com/t/viewportframe-masking/2964839
creator: Roblox DevForum
official: false
advice_density: low
date: 2024-05-10
views: 1043
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# ViewportFrame Masking

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/viewportframe-masking/2964839) | Roblox DevForum | 1,043 views | 2024-05-10

## Summary
Tutorial by 6mikael6 on ViewportFrame masking. Erased-vertex-alpha meshes (made in Blender via Vertex Paint "Erase Alpha" or provided script) render nothing behind them, acting as subtractive masks. Glass parts reveal 0-alpha meshes behind them, allowing additive effects. SurfaceAppearance (AlphaMode Transparency) inherits masking; Decals, Textures, and part transparency do not. Includes example place file.

## Tips
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) **[[building-art-and-assets]]** Erase vertex alpha in Blender Vertex Paint using the Erase Alpha blend mode, or run the provided script to set all vertex alpha to 0.
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) **[[common-mistakes]]** Decals, Textures, mesh textures and part transparency do not inherit 0-alpha mesh masking; use SurfaceAppearance instead if you need masking behaviour.
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) **[[ui-ux-design]]** For image masks on a 0-alpha mesh, set SurfaceAppearance AlphaMode to Transparency; it supports only 2 or 5 transparency levels, which causes banding.
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) **[[optimization-and-streaming]]** Planar reflections built from ViewportFrame masks are performance heavy because moving objects and masks must be updated manually.

## Numbers
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) SurfaceAppearance transparency levels: **2 or 5** (Levels of transparency supported by SurfaceAppearance masks; causes banding)
- [page](https://devforum.roblox.com/t/viewportframe-masking/2964839) Glass transparency in Character1 example: **0.99** (Glass character mask revealing two 0-alpha planes behind the player)

## Tools
Blender, Roblox Studio ViewportFrame, EditableImage, EditableMesh

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
