---
title: "Docs: studio / importer"
url: https://create.roblox.com/docs/studio/importer.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / importer

[Open](https://create.roblox.com/docs/studio/importer.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Studio docs for the Importer: how to import 3D meshes (.fbx, .gltf, .obj), images, audio and video; import queue, presets, and the per-model import settings (rig, transform, geometry, cage meshes) plus warnings/errors.

## Tips
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Check the .fbx/.gltf/.obj against Studio's mesh requirements before importing to reduce errors or unexpected behavior.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Set Scale Unit to match the modelling software's units so the mesh imports at the correct size.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Disable Upload to Roblox while iterating on a model's design to avoid creating multiple copies in Toolbox and Asset Manager.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Use Import as Package for assets reused or redistributed; packages auto-update and can be shared.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Enable Merge Meshes to combine all MeshParts into one MeshPart, reducing instance count, instead of a Model of many parts.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Enable Make Double Sided only when needed; double-sided rendering is more performance intensive.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Leave Keep Zero Influence Bones disabled unless needed; the importer removes them by default.
- [page](https://create.roblox.com/docs/studio/importer) **[[ugc-and-avatar-economy]]** For avatar items, use the Validate UGC Body option to open the mesh in Avatar Setup and test before uploading to the Marketplace.
- [page](https://create.roblox.com/docs/studio/importer) **[[building-art-and-assets]]** Use presets (Studio Default, Last Imported, or custom saved presets) and Apply settings to all to speed up bulk imports from the queue.
- [page](https://create.roblox.com/docs/studio/importer) **[[common-mistakes]]** Resolve warning and error icons in the hierarchy before importing; warnings flag issues that cause errors or unexpected behavior.
- [page](https://create.roblox.com/docs/studio/importer) **[[scripting-and-performance]]** Note that Add to Workspace, when importing from a published game, grants that game permission to use the restricted asset.

## Numbers
- [page](https://create.roblox.com/docs/studio/importer) Default Scale Unit: **Studs** (File geometry setting; default unit used when importing meshes)
- [page](https://create.roblox.com/docs/studio/importer) Default Import Only As Model: **Enabled** (Imports multi-child model as single asset by default)
- [page](https://create.roblox.com/docs/studio/importer) Default Upload to Roblox: **Enabled** (Adds model to Toolbox and Asset Manager by default)
- [page](https://create.roblox.com/docs/studio/importer) Default Set Pivot to Scene Origin: **Enabled** (Sets whole model pivot to scene origin by default)
- [page](https://create.roblox.com/docs/studio/importer) Default Anchored (mesh): **Disabled** (Anchored is disabled by default; disabled for rig/avatar meshes)
- [page](https://create.roblox.com/docs/studio/importer) Default Make Double Sided: **Disabled** (Object geometry; one-sided by default)

## Tools
Roblox Studio Importer, Avatar Setup tool, Asset Manager, Toolbox, Open Cloud

## He points to
- Open Cloud usage guide for assets
- Audio Assets docs
- Presets docs
- Import settings docs

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[scripting-and-performance]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
