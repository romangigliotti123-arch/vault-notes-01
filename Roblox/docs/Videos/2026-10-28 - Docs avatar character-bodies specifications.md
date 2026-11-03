---
title: "Docs: avatar / character-bodies / specifications"
url: https://create.roblox.com/docs/avatar/character-bodies/specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / character-bodies / specifications

[Open](https://create.roblox.com/docs/avatar/character-bodies/specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs specifying requirements for character body models: 15 mesh objects, body scale standards (Normal/Slender/Classic) with bounding box limits, triangle budgets per asset, naming, attachments, R15/advanced R15 rigging, skinning limits, textures, outer cages, and Marketplace requirements.

## Tips
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Freeze all transforms and set pivots to 0,0,0; characters must face positive Z and stand upright in positive Y before export.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Make all geometry watertight with no exposed holes or backfaces; use quads over N-gons where possible.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Estimate tris by doubling the quad count; each body asset must stay under its tri budget.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Name all 15 body mesh objects exactly per convention (e.g. LeftUpperArm_Geo) and cap limbs so they form watertight meshes.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Use I-Pose, A-Pose, or T-Pose before export for best Studio compatibility.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Limit skin influences to 4 bones per vertex and do not apply influences to the Root bone.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Set LowerTorso and Root bone positions to 0,0,0 in standard R15 rigs.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** For advanced R15, name optional bones exactly per hierarchy, skin their meshes, and insert HumanoidRigDescription/DigitsRigDescription objects before selling.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Keep body parts fully opaque and make each part fill at least 50% of its bounding box in front, side and back views; head at least 50%.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Keep total body dimensions within min/max bounds (width 1-8, length 4-10, depth 0.5-4 studs); overlapping parts don't add up.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** For custom skin tones, set exposed skin areas transparent so no default color is baked in; keep eyes and brows at 100% opacity.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Keep textures at or below 2048x2048 for Marketplace assets.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[building-art-and-assets]]** Use Roblox's cage templates for outer cages named <Part>_OuterCage; do not delete vertices or alter UVs on cages.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[ugc-and-avatar-economy]]** Before uploading to the Marketplace, set MeshPart Material to Plastic, Transparency 0, VertexColor 1,1,1, and strip extraneous Scripts/Parts from the Model.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Place attachments overlapping halfway into the mesh; head accessory attachments must sit on the visible head surface or they violate Marketplace policy.
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[3d-modeling-rigging-and-animation]]** Orient grip attachments perpendicular to the lower arm bone (e.g. 90,0,0 in I-Pose).
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) **[[ugc-and-avatar-economy]]** Eyebrows and eyelashes cannot be uploaded standalone; bundle them with a character body or makeup asset.

## Numbers
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Max tris per body asset: **DynamicHead 4000; Torso 1750; each limb 1248; total 10,742** (Body split into 6 Marketplace assets)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Mesh objects per body: **15** (Required for standard and higher-fidelity bodies)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Max bone influences per vertex: **4** (Skinning requirement)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Min bounding box per part (W x L x D, studs): **Head/Arm/Leg 0.05x0.5x0.05; Torso 0.05x0.65x0.05** (Validator rotates limbs to standard orientation)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Max bounding box per part (W x L x D, studs): **Head 4x2x4; Arm/Leg 4x4.5x4; Torso 4x4x4** (Same limits for Normal, Slender, Classic)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Total body bounding box min / max (studs): **min 1.0x4.0x0.5; max 8.0x10.0x4.0** (Total dimension matters most for avatar size)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Mesh fill of bounding box: **At least 50% for body parts and head** (Front, side and back views)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Max texture resolution: **2048x2048** (Marketplace assets)
- [page](https://create.roblox.com/docs/avatar/character-bodies/specifications) Optional advanced R15 bones: **up to 37** (Articulated hands, shoulders, spine)

## Tools
Blender, Maya, Roblox Studio Importer, Roblox Avatar Setup / body cage templates

## He points to
- Dynamic head specifications
- Layered accessory specifications
- General mesh specifications
- Rigging and Skinning
- Publish bodies with eyelashes and eyebrows

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
