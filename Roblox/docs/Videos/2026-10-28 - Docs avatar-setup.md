---
title: "Docs: avatar-setup"
url: https://create.roblox.com/docs/avatar-setup.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar-setup

[Open](https://create.roblox.com/docs/avatar-setup.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Avatar Setup: an in-Studio tool that auto-processes custom 3D models (FBX/OBJ/glTF imports or existing models) into avatar bodies, rigid accessories, and layered accessories by adding rigging, skinning, facial rigs, cages, body partitioning, and attachments. Covers import, running setup with Platform vs Development presets, testing tools, editing tools, and Marketplace publishing.

## Tips
- [page](https://create.roblox.com/docs/avatar-setup) **[[building-art-and-assets]]** Import models with the Importer tool and disable 'Upload To Roblox' in File General to avoid unwanted copies of similar assets in Toolbox.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Use Platform Avatar preset for Marketplace items; it generates a more restrictive setup needed to pass validation and moderation. Development Avatar is for NPCs or starter characters.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Set each mesh's Type correctly (Body, Layered, Rigid, Eye Layered) so it moves and animates correctly.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Run Avatar Setup with the character's body and head together when converting a face decal; running head-only causes the face-as-2D-decal setting to fail.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Verify the face is front-facing before running setup and enable Manually Align Front if auto-alignment fails.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Delete any Class.FaceControls under the Head model before running setup, otherwise the existing face setup is retained.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Replace MeshPart.TextureId textures with SurfaceAppearance objects for significant texture quality improvements when rendering.
- [page](https://create.roblox.com/docs/avatar-setup) **[[building-art-and-assets]]** Enable Improve facial caging if you plan to use makeup with the character; it improves head cage alignment with facial features.
- [page](https://create.roblox.com/docs/avatar-setup) **[[optimization-and-streaming]]** Leave Reduce triangle count enabled unless you need to skip auto-decimation; it reduces meshes above Marketplace triangle budgets.
- [page](https://create.roblox.com/docs/avatar-setup) **[[3d-modeling-rigging-and-animation]]** Use the Cage Brush for minor-to-moderate layered accessory fit fixes; major cage changes require re-exporting from your modeling tool.
- [page](https://create.roblox.com/docs/avatar-setup) **[[age-ratings-moderation-and-tos]]** Expect imported models to enter the moderation queue; appeals can take up to 10 minutes to resolve.
- [page](https://create.roblox.com/docs/avatar-setup) **[[ugc-and-avatar-economy]]** Publishing to the Marketplace requires paying an upload fee and passing moderation before items enter the catalog.
- [page](https://create.roblox.com/docs/avatar-setup) **[[testing-debugging-and-qa]]** Use the Check Body and Check Face tabs (animations, clothing, accessories) to test rigs and fits before publishing; retry auto-setup after fixing the base model.

## Numbers
- [page](https://create.roblox.com/docs/avatar-setup) Moderation appeal resolution time: **up to 10 minutes** (Appeal of moderated imported model via emailed link)
- [page](https://create.roblox.com/docs/avatar-setup) Marketplace publishing cost: **Upload fee required** (Paid upload fee plus passing moderation to add items to catalog)
- [page](https://create.roblox.com/docs/avatar-setup) Body parts from partitioning: **15** (Avatar character body split into 15 MeshParts; R15 rig)

## Tools
Avatar Setup (Roblox Studio), Importer tool, Attachment Tool, Cage Brush, Check Body / Check Face testing tools

## He points to
- Nature Girl Avatar Setup template
- Stylish Male Avatar Setup template
- Publish to the Marketplace docs
- Marketplace fees and commissions docs
- Marketplace policy docs

## Topics
[[3d-modeling-rigging-and-animation]] [[age-ratings-moderation-and-tos]] [[building-art-and-assets]] [[optimization-and-streaming]] [[testing-debugging-and-qa]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
