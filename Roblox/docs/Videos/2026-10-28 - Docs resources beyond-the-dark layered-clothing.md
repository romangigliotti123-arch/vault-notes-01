---
title: "Docs: resources / beyond-the-dark / layered-clothing"
url: https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / beyond-the-dark / layered-clothing

[Open](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on building Layered Clothing for a custom character ("The Visitor") in a space station game: base body rules (R15, cages, poly budget), skinning, cage fitting, clothing layering, surface appearance textures, helmet as hardpoint accessory, and the upcoming Accessory Tool.

## Tips
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Keep each base body part under 10,000 triangles; body geo, cage parts and skeleton must follow the standard R15 schema.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Limit clothing skinning to a maximum of 4 influences per vertex; skin only to the joints the garment affects.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Name cages [clothing name]_InnerCage and [clothing name]_OuterCage; body cages use the Roblox-supplied cage with _OuterCage suffix per part.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Keep outer cages close to the mesh but always outside it so Hidden Surface Removal can hide covered geometry.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Model base characters in a neutral pose with a slight joint bend to imply movement direction; cap mesh parts and average vertex normals at seams.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Export skeletons with unique joint names, joint scale [1,1,1], mesh transforms zeroed (scale 1), and outward-facing normals.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Paint skin weights tighter at elbows and knees and copy influences across part seams so weights match 1:1.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Unbind the rig from the mesh before texturing; do range-of-motion tests first to catch deformation issues early.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Make shirt, shorts, gloves and boots opaque for skin-tone control; use partial alpha on exposed skin to add anatomy detail.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Always supply albedo, metalness, roughness and normal maps for SurfaceAppearance; missing metalness defaults to plastic and missing roughness to smooth.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Test materials in Studio's actual lighting before finalising textures; adjust metalness after seeing it in-world.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Use attachments for particles, beams or lights on accessories, since attachments are valid in accessories while parts are not.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Reuse shared trim maps across the environment and props to minimise texture count.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[3d-modeling-rigging-and-animation]]** Gloves and boots are not supported by Layered Clothing; keep cages inside rigid hand/foot pieces so the suit deforms to them.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[ugc-and-avatar-economy]]** Design clothing as modular layers so one character can be released to the Marketplace separately from its clothing.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) **[[building-art-and-assets]]** Use hardpoint accessories (no cage deformation) for rigid items like helmets; a single mesh can be placed as a MeshPart and given a SurfaceAppearance.

## Numbers
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) Max triangles per body part: **10,000** (Layered accessory base body checklist, per part)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) Max character size: **2000×2000×2000 units** (Base body size limit)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) Max skin influences for clothing: **4** (Clothing must skin to standard R15 skeleton)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/layered-clothing) Body cage parts: **15** (One cage part per R15 body part mesh)

## Games
- **Space station game (unnamed, Roblox docs example)**: Layered clothing let the creators build a main character and release the suit as a modular Marketplace component.

## Tools
Roblox Studio, Asset Manager, Accessory Fitting Tool / Accessory Tool (upcoming), Layered clothing cage template (Roblox), DCC application (Blender-style rigging/skinning)

## He points to
- Layered accessories (guides, example projects, reference models)
- Accessory Fitting Tool docs

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
