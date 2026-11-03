---
title: "Docs: art / characters / creating / export-character"
url: https://create.roblox.com/docs/art/characters/creating/export-character.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / export-character

[Open](https://create.roblox.com/docs/art/characters/creating/export-character.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page on exporting a character model from Blender as FBX with the correct export settings (Path Mode, Embed Textures, Custom Properties, Add Leaf Bones off, Bake Animation settings), then testing the import in Studio. Covers what you can do with the resulting Class.Model after import.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[building-art-and-assets]]** In Blender FBX export, set Path Mode to Copy and enable Embed Textures so the .fbx carries its textures with it.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[3d-modeling-rigging-and-animation]]** Enable Custom Properties in the FBX Include section so custom properties survive export to Studio.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[3d-modeling-rigging-and-animation]]** Disable Add Leaf Bones in the Armature section of the FBX export to avoid extra bones on the rig.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[3d-modeling-rigging-and-animation]]** When baking animation on export, disable NLA Strips, All Actions and Force Start/End Keyframes, and set Simplify to 0.0 to keep full animation fidelity.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[testing-debugging-and-qa]]** Test character assets repeatedly at every creation stage, both inside Blender and after importing into Studio.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[testing-debugging-and-qa]]** After exporting the .fbx, import it into a test place and verify the avatar and related components before publishing.
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) **[[ugc-and-avatar-economy]]** Once the Class.Model is imported, you can upload it to the Marketplace, apply a HumanoidDescription to use it in existing games, or save it to the Toolbox.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/creating/export-character) Simplify (FBX bake animation): **0.0** (Required setting when baking animation on FBX export)

## Tools
Blender, Roblox Studio

## He points to
- Test characters
- Test character bodies

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
