---
title: "Docs: art / characters / creating / modeling-best-practices"
url: https://create.roblox.com/docs/art/characters/creating/modeling-best-practices.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / modeling-best-practices

[Open](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on modeling/sculpting character heads in Blender. Explains non-destructive sculpting (only move existing vertices, never add/delete), edge flow rules for face regions (forehead, nasolabial, mouth, eyes, eyelids/eyebrows), and why topology collisions break rigs and facial animation.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** When editing a character template, never delete or add vertices to the body; only move existing vertices so skinning and facial animation data stay intact.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Start from a template model close to your final design; extreme geometric changes can adversely affect rigging and skinning even if no vertices are deleted.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Make consistent, proportional changes when sculpting to preserve the template's edge flow and rig compatibility.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Keep forehead wrinkle and nasolabial edge lines in their original shape and in the same relative relationship to each other.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Avoid modifying mouth/lip topology; it drives open/close and vowel shapes and is tied to tongue, jaw and facial data. Use a sculpting mask to protect it.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Avoid modifying eye topology; it affects eyeball meshes and saved facial expression data. Use a sculpting mask to protect it.
- [page](https://create.roblox.com/docs/art/characters/creating/modeling-best-practices) **[[3d-modeling-rigging-and-animation]]** Leave adequate space between eyelids and eyebrows so they don't clash during facial poses, which causes jagged collision artifacts.

## Tools
Blender

## Topics
[[3d-modeling-rigging-and-animation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
