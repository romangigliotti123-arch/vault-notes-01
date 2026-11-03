---
title: "Docs: art / characters / creating / remove-extra-bones"
url: https://create.roblox.com/docs/art/characters/creating/remove-extra-bones.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / remove-extra-bones

[Open](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on removing the helper bones left over from placing head geometry on a character armature. Explains that extra non-skinned bones must be deleted for validation to pass, while DynamicHead facial bones must stay. Gives step-by-step Blender Edit-mode deletion.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones) **[[3d-modeling-rigging-and-animation]]** Delete the extra helper head bones before validation; leftover bones break the standard geometry and joint hierarchy and cause validation failures.
- [page](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones) **[[3d-modeling-rigging-and-animation]]** Never delete the facial animation bones parented under DynamicHead; they carry skinning data that drives facial animation.
- [page](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones) **[[3d-modeling-rigging-and-animation]]** Combine head geometry before removing head bones, since combining is required for the head to validate correctly.
- [page](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones) **[[3d-modeling-rigging-and-animation]]** In Blender, select extra head child joints under Head in Edit mode (except DynamicHead), then right-click and choose Delete Selected Bones.

## Tools
Blender, Roblox Studio

## Topics
[[3d-modeling-rigging-and-animation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
