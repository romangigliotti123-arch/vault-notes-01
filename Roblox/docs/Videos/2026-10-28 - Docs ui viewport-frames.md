---
title: "Docs: ui / viewport-frames"
url: https://create.roblox.com/docs/ui/viewport-frames.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / viewport-frames

[Open](https://create.roblox.com/docs/ui/viewport-frames.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on ViewportFrame: renders 3D objects into a 2D viewport. Covers three configurations (camera-linked, static via duplicated camera, self-rotating via LocalScript), skybox cubemap reflections via Sky child, and lighting/appearance properties (Ambient, LightDirection, LightColor, ImageColor3, ImageTransparency).

## Tips
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[ui-ux-design]]** Use ViewportFrame for item previews in inventory menus, equipped-item rotation, and minimaps instead of separate rendering setups.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[ui-ux-design]]** For a static preview, duplicate the top-level Camera and assign the duplicate to CurrentCamera so the game camera doesn't move the object.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[building-art-and-assets]]** To show a workspace object in a ViewportFrame, duplicate it and parent the duplicate; the original stays in Workspace for gameplay.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[ui-ux-design]]** When updating a ViewportFrame view, move the camera, not the objects inside the viewport.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[optimization-and-streaming]]** For rotation, drive the viewport camera in RunService.PostSimulation using delta time rather than a fixed wait loop.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[building-art-and-assets]]** For reflections inside a ViewportFrame, add a Sky child with all six Skybox textures set, and give parts Reflectance > 0 or Glass/Foil material.
- [page](https://create.roblox.com/docs/ui/viewport-frames) **[[building-art-and-assets]]** For MeshParts to reflect in a ViewportFrame, apply a SurfaceAppearance with a properly configured MetalnessMap.

## Numbers
- [page](https://create.roblox.com/docs/ui/viewport-frames) Default Ambient: **Color3.fromRGB(200,200,200)** (ViewportFrame.Ambient default, ghost grey)
- [page](https://create.roblox.com/docs/ui/viewport-frames) Default LightDirection: **(-1,-1,-1)** (Direction of light source from origin)
- [page](https://create.roblox.com/docs/ui/viewport-frames) Default LightColor: **Color3.fromRGB(140,140,140)** (ViewportFrame.LightColor default, silver)
- [page](https://create.roblox.com/docs/ui/viewport-frames) ImageTransparency range: **0 (opaque) to 1 (invisible)** (Default 0)
- [page](https://create.roblox.com/docs/ui/viewport-frames) Example camera distance / FOV / pitch / rotation speed: **10 / 50 / 40 / 50** (Sample rotation script parameters)

## Tools
Roblox Studio, ViewportFrame, Camera, Sky, LocalScript, RunService.PostSimulation

## He points to
- Roblox Creator Docs: ViewportFrame

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
