---
title: "Docs: art / modeling / export-requirements"
url: https://create.roblox.com/docs/art/modeling/export-requirements.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / export-requirements

[Open](https://create.roblox.com/docs/art/modeling/export-requirements.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on exporting 3D models as .fbx for Studio import. Covers general export requirements and step-by-step FBX export settings for Blender and Maya, including scale, armature bones, animation baking, texture embedding and axis setup.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Export models as .fbx to get all Studio 3D import features; for rigs/skinning, the .fbx carries both rig and influence data.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Check the model against Roblox modeling specifications before exporting; characters and accessories have extra specs and separate export settings.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[building-art-and-assets]]** Blender: set Path Mode to Copy and enable Embed Textures so textures travel with the .fbx.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Blender: set Transform > Apply Scalings to FBX Unit Scale to avoid import scaling issues.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Blender: disable Add Leaf Bones in the Armature section to keep the rig clean on import.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Disable Bake Animation in Blender unless exporting keyframed animation such as a walk cycle or facial animation.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Maya: enable Smooth Mesh and Referenced Asset Content in the Geometry section of FBX export.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Maya: disable Animation unless importing an animation; some avatar assets require it, and then enable Bake Animation.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[building-art-and-assets]]** Maya: enable Embed Media if textures must be imported as .png.
- [page](https://create.roblox.com/docs/art/modeling/export-requirements) **[[3d-modeling-rigging-and-animation]]** Maya: enable Automatic units and set Axis Conversion Up Axis to Y in Advanced Options.

## Tools
Blender, Maya, Roblox Studio

## He points to
- Roblox modeling specifications
- Accessory specifications and export settings
- Layered accessory specifications and layered export settings
- Avatar specifications and avatar export settings
- Blender FBX scaling guide

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
