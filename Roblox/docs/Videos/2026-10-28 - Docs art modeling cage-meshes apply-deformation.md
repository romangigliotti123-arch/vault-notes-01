---
title: "Docs: art / modeling / cage-meshes / apply-deformation"
url: https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / cage-meshes / apply-deformation

[Open](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on applying mesh deformations with caged meshes. Covers parenting target and layered MeshParts in a Model, welding them, setting WrapLayer.Order, stacking multiple layers onto one target, and how layered accessories relate to the standard avatar body cage.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** Confirm the target MeshPart has a WrapTarget and the deforming MeshPart has a WrapLayer before applying a deformation.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** Duplicate the layered mesh before testing so you keep an original copy for later deformations.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** Parent target and layered MeshParts in one Model, then add a WeldConstraint with Part0 as the layered mesh and Part1 as the target.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** Change WrapLayer.Order to trigger deformation; adjust it anytime to fix stacking order between layers such as a T-shirt over a sweater.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** After deformation computes it is retained, so you can delete the duplicate layer and weld to leave one deformed mesh and simplify the workspace.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** Every layered mesh added to a target must share the same UV layout as the target, because Roblox pairs layers to the target by UV.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[building-art-and-assets]]** When stacking layers, weld each new layer to the previous layered mesh (Part0 = previous layer, Part1 = new layer) and set WrapLayer.Order so the later layer renders on top.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[3d-modeling-rigging-and-animation]]** For avatar accessories, cage to Roblox's standard body cage UV layout so the accessory fits every avatar body; non-standard cages are incompatible.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[3d-modeling-rigging-and-animation]]** Use WrapLayer.AutoSkin to transfer skinning data for layered accessories; use the Accessory Fitting Tool for the avatar workflow.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) **[[cross-platform-and-console]]** Custom non-Marketplace characters using a unique cage or UV solution need the separate non-R15 layered accessories guidance.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) Standard avatar body cage objects: **15 body parts** (Cage objects must exist for each of the 15 body parts)
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes/apply-deformation) Example WrapLayer.Order values: **2 or 5** (Suggested non-default order values in docs)

## Tools
Roblox Studio, Blender, WeldConstraint, WrapTarget, WrapLayer, Accessory Fitting Tool

## He points to
- Cage-Mesh-Examples.blend
- Layered accessories on non-R15 (docs)
- Layered accessories (docs)
- Automatic Skinning Transfer (docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[cross-platform-and-console]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
