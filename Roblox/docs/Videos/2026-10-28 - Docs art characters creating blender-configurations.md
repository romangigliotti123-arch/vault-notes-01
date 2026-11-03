---
title: "Docs: art / characters / creating / blender-configurations"
url: https://create.roblox.com/docs/art/characters/creating/blender-configurations.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / blender-configurations

[Open](https://create.roblox.com/docs/art/characters/creating/blender-configurations.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Blender template configuration for avatar/character creation: explains template hierarchy (Cage, Joints with bones/_Geo/_Att/animation data, lighting objects), disabled viewport objects, a shader-based custom skin tone preview (Blender 3.4+), export workarounds for textures, FBX scale settings, and the 0–330 animation range for facial animation.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[3d-modeling-rigging-and-animation]]** Use Blender 3.4+ so the helper shader configurations in the template .blend files render correctly; older versions may show textures incorrectly.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[3d-modeling-rigging-and-animation]]** Switch to Viewport Shading mode for textures to render as expected in the skin tone preview.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[3d-modeling-rigging-and-animation]]** After swapping textures, check the normal map colorspace; it reverts to SRGB and should be set back to NonColor to render correctly.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[building-art-and-assets]]** Before exporting, either replace the Mix node with the ColorMap node or export textures manually as separate image files, since the skin tone preview blocks automatic texture packaging into the .fbx.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[3d-modeling-rigging-and-animation]]** When exporting FBX, set Transform > Apply Scalings to FBX Unit Scale so the model scales correctly in Roblox.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[3d-modeling-rigging-and-animation]]** For custom characters with facial animation, set the Blender timeline range Start to 0 and End to 330.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[building-art-and-assets]]** Use textures with full or partial transparency so underlying Class.Part.Color shows through, enabling customizable skin tones; use full opacity for areas that should always be a fixed color.
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) **[[building-art-and-assets]]** Save custom project settings as startup defaults via File > Defaults > Save Startup File to reuse them in future Blender projects.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) Cage meshes per character: **15** (Outer body cage meshes in the template Cage object)
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) Minimum Blender version: **3.4** (Required for helper shader configurations to render correctly)
- [page](https://create.roblox.com/docs/art/characters/creating/blender-configurations) Animation timeline range: **0 to 330** (Start and End frames for custom characters with facial animation)

## Tools
Blender, Roblox Studio

## He points to
- Export textures (Roblox docs)
- Blender FBX scaling (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
