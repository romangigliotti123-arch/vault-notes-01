---
title: "Docs: parts / meshes"
url: https://create.roblox.com/docs/parts/meshes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / meshes

[Open](https://create.roblox.com/docs/parts/meshes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Meshes: importing MeshParts from Blender/Maya via the Importer, PBR textures via SurfaceAppearance or MaterialVariant, single TextureID, level-of-detail render fidelity by camera distance, collision fidelity options, and rigging/skinning basics.

## Tips
- [page](https://create.roblox.com/docs/parts/meshes) **[[building-art-and-assets]]** Use the Importer to preview and check texture, rigging, skinning and animation data before importing; it flags issues and rejects meshes with errors.
- [page](https://create.roblox.com/docs/parts/meshes) **[[building-art-and-assets]]** Name objects ending in _Att, _OuterCage, _InnerCage or _OuterCage in the source file to have the Importer convert them to Attachments and wrap objects.
- [page](https://create.roblox.com/docs/parts/meshes) **[[building-art-and-assets]]** Use Asset Manager for bulk-importing images and audio, but not meshes with rigging, skinning, animation, accessories or facial animation; use the Importer for those.
- [page](https://create.roblox.com/docs/parts/meshes) **[[building-art-and-assets]]** Setting a TextureID cannot override a mesh's existing PBR textures; remove the PBR textures first if you want a single texture.
- [page](https://create.roblox.com/docs/parts/meshes) **[[optimization-and-streaming]]** Keep the default Automatic RenderFidelity unless needed: detail drops to Medium at 250-500 studs and Lowest beyond 500 studs from the camera.
- [page](https://create.roblox.com/docs/parts/meshes) **[[optimization-and-streaming]]** Use Box collision for small or non-interactive objects; Hull for convex shapes; Default for complex semi-detailed interaction; PreciseConvexDecomposition only when precision justifies its high cost.
- [page](https://create.roblox.com/docs/parts/meshes) **[[optimization-and-streaming]]** Use CollisionFidelity Tunable with the CollisionPrecision slider to trade collision precision against cost without switching fidelity options.
- [page](https://create.roblox.com/docs/parts/meshes) **[[building-art-and-assets]]** Add a SurfaceAppearance child to apply up to four PBR maps without changing geometry; if both SurfaceAppearance and MaterialVariant are set, only SurfaceAppearance's texture maps apply.
- [page](https://create.roblox.com/docs/parts/meshes) **[[3d-modeling-rigging-and-animation]]** Rig and skin meshes for deformable parts: skinning lets a head bend at the neck instead of rotating rigidly on one axis.

## Numbers
- [page](https://create.roblox.com/docs/parts/meshes) RenderFidelity Highest distance: **Less than 250 studs from camera**
- [page](https://create.roblox.com/docs/parts/meshes) RenderFidelity Medium distance: **250-500 studs**
- [page](https://create.roblox.com/docs/parts/meshes) RenderFidelity Lowest distance: **500 or more studs**

## Tools
Roblox Studio Importer, Asset Manager, Animation Editor, MaterialService / MaterialVariant, Visualization Options (Collision fidelity), Blender, Maya

## He points to
- Rigging and skinning docs page
- PBR Textures docs page
- Improve performance docs page
- Set physics and rendering parameters docs page
- Create an animation docs page
- Avatar docs page

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
