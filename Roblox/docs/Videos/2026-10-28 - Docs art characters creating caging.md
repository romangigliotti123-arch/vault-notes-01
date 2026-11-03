---
title: "Docs: art / characters / creating / caging"
url: https://create.roblox.com/docs/art/characters/creating/caging.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / caging

[Open](https://create.roblox.com/docs/art/characters/creating/caging.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation page on caging a custom avatar head: updating the Head_OuterCage mesh in Blender so layered clothing fits over a sculpted head. Covers symmetry settings, vertex rules, and fit verification.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[ugc-and-avatar-economy]]** Never delete any cage vertices or faces; destructive edits cause import issues and prevent equipping clothing and cosmetics.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[3d-modeling-rigging-and-animation]]** Enable X-Axis symmetry and Topology Mirror in Blender Edit mode so cage edits stay symmetrical.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[3d-modeling-rigging-and-animation]]** Set Head_OuterCage Display As to Wire while editing, then back to Solid to spot-check intersections.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[3d-modeling-rigging-and-animation]]** Align the Head cage base with the top of the UpperTorso cage when editing the base of the head cage.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[3d-modeling-rigging-and-animation]]** Fit the cage tightly: move cage vertices until it just covers Head_Geo with no Head_Geo geometry poking through solid sections.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[building-art-and-assets]]** For full-body sculpt changes across many parts, use the Blender Cage Template with its std_cage_deformable helper mesh instead of editing each _OuterCage manually.
- [page](https://create.roblox.com/docs/art/characters/creating/caging) **[[3d-modeling-rigging-and-animation]]** Adjust every _OuterCage object matching any geometry changes you make to other body parts, not just the head.

## Tools
Blender, Blender Cage Template (.blend project file)

## He points to
- Blender Cage Template
- Tutorial project with caging completed (download)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
