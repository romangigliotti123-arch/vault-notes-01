---
title: "Docs: avatar / makeup / reassign-textures"
url: https://create.roblox.com/docs/avatar/makeup/reassign-textures.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / makeup / reassign-textures

[Open](https://create.roblox.com/docs/avatar/makeup/reassign-textures.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on reassigning PBR texture images on the template head for custom makeup in Blender and Maya, then exporting the head with makeup-specific export settings for Studio import.

## Tips
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[ugc-and-avatar-economy]]** Only reassign PBR textures on Roblox template heads that already have texture nodes; for scratch builds, use the 'Assign textures' guide instead.
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[3d-modeling-rigging-and-animation]]** Replace each PBR texture by removing the existing image link and browsing for the new file; delete unused texture nodes and verify the graph matches the reference.
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[3d-modeling-rigging-and-animation]]** Blender shortcut: File > External Data > Unpack Resources > Remove Pack clears all image links at once instead of unassigning each texture.
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[3d-modeling-rigging-and-animation]]** Blender export as FBX/glTF: enable Custom Properties in Include and Only Deform Bones in Armature so eyebrows and eyelashes get skinning data and makeup UV data transfers.
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[3d-modeling-rigging-and-animation]]** Maya export as FBX/glTF: enable Skins under Deformed Models so eyebrows and eyelashes include skinning data.
- [page](https://create.roblox.com/docs/avatar/makeup/reassign-textures) **[[3d-modeling-rigging-and-animation]]** Export the entire template head file (not a partial mesh) after replacing textures, applying all standard 3D export requirements.

## Tools
Blender, Maya, Roblox Studio

## He points to
- Assign textures in Blender and Maya (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
