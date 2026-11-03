---
title: "Docs: art / modeling / reimport"
url: https://create.roblox.com/docs/art/modeling/reimport.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / reimport

[Open](https://create.roblox.com/docs/art/modeling/reimport.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Reimport: updating existing custom models and textures from an external 3D file non-destructively via right-click or Alt+Shift+R, with saved file path and import preset. Covers mesh name matching, SurfaceAppearance suffix detection, pivot-relative reimport, and the Configure dialog.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-art-and-assets]]** Use Reimport (Alt+Shift+R) to update models from Blender instead of re-importing; it keeps existing properties and saves re-entering import settings.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-art-and-assets]]** Keep mesh path/names unique in your external 3D tool; reimport matches meshes by path/name, so renames create new MeshParts instead of updating.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-art-and-assets]]** Maintain the naming and tree structure of MeshParts inside the Studio model so reimport updates them correctly.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-art-and-assets]]** Name PBR texture files with recognized suffixes (e.g. _Color, _Normal, _Rough, _Metal, _Emissive) so reimport maps them to SurfaceAppearance automatically.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-art-and-assets]]** Reimport only updates mesh content and transform; CollisionFidelity and RenderFidelity are preserved, and a mesh with no texture keeps the existing texture.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[building-and-level-design]]** For models with custom pivots, use 'Reimport relative to this' on an unmoved MeshPart as the anchor so the model pivot stays correct.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[common-mistakes]]** Renaming a mesh in Blender (e.g. Mesh1 to Mesh2) creates a new MeshPart and leaves the original unchanged; plan renames carefully.
- [page](https://create.roblox.com/docs/art/modeling/reimport) **[[development-process-and-speed]]** Reimport memory is local to each device; models imported on another device open the Configure dialog, so set the file path there once per machine.

## Tools
Roblox Studio Reimport, Alt+Shift+R hotkey, Configure Reimport Settings dialog

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[common-mistakes]] [[development-process-and-speed]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
