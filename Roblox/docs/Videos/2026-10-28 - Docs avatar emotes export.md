---
title: "Docs: avatar / emotes / export"
url: https://create.roblox.com/docs/avatar/emotes/export.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / emotes / export

[Open](https://create.roblox.com/docs/avatar/emotes/export.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on exporting avatar animation data (emotes) as .fbx or .gltf. Covers prerequisites (timeline Start/End covering all keyframes) and step-by-step Blender and Maya FBX export settings so imports into Studio succeed at correct scale.

## Tips
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** Set the animation timeline Start and End to cover the full range of all keyframes before exporting, or full-body and FACS animation data may be cut off.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Blender FBX export, set Apply Scalings to FBX Unit Scale and review Blender FBX scaling docs if scale is wrong on import.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Blender FBX export, uncheck Add Leaf Bones in the Armature section to keep the rig matching Roblox's emote specs.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Blender Animation export options, uncheck NLA Strips, All Actions and Force Start/End Keyframes, and set Simplify to 0.0 to preserve keyframe data.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Blender, set Path Mode to Copy and enable Embed Textures; enable Custom Properties in the Include section.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Maya FBX export, enable Bake Animation and Animation, since avatar characters with dynamic heads require animation data.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[3d-modeling-rigging-and-animation]]** In Maya FBX export, enable Smooth Mesh and Referenced Asset Content under Geometry, and set Units to Automatic and Up Axis to Y.
- [page](https://create.roblox.com/docs/avatar/emotes/export) **[[building-art-and-assets]]** Enable Embed Media in Maya export only if you need textures imported as .png.

## Numbers
- [page](https://create.roblox.com/docs/avatar/emotes/export) Blender Animation Simplify setting: **0.0** (Set in Blender FBX export animation section to avoid simplifying keyframes)
- [page](https://create.roblox.com/docs/avatar/emotes/export) Maya Up Axis: **Y** (Axis Conversion setting in Maya FBX export advanced options)

## Tools
Blender, Maya, Roblox Studio

## He points to
- Blender FBX scaling documentation
- Export avatar animations from Maya tutorial

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
