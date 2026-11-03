---
title: "Docs: resources / beyond-the-dark / custom-characters"
url: https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / beyond-the-dark / custom-characters

[Open](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on building a custom animated creature: rig with minimal joints from a neutral pose, skin with falloff, import via Importer, add neon/SpotLight glow and particles via a tagged VFX-follow module, PBR textures, and animate in the Animation Editor.

## Tips
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[building-art-and-assets]]** Model the character in a neutral pose; curled poses stretch when animated to bend the opposite way.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Use as few joints as possible; each joint must be managed when skinning and controlled when animating.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Give a dense tentacle mass one large joint chain with small tails at the tips instead of joints for every tentacle.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Make joint and mesh names unique; meshes must not share names with joints or bones.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Keep mesh transforms at 0 and scales at 1 before skinning; skeleton joints should be [1,1,1] scale.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Limit skinning to 4 influences per vertex and use generous falloff and joint overlap to avoid sharp bends.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Every joint you want imported must influence the skin; skin in the bind pose when possible.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[building-art-and-assets]]** Keep each mesh part under 10,000 triangles and the total size under 2000 units on any axis before import.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[building-art-and-assets]]** Keep SurfaceAppearance texture maps at 1024x1024 or smaller and pack maps into one sheet per type.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[vfx-and-particles]]** Use a small part near a long tentacle's tip for particle emitters; an emitter on the whole limb emits from its entire length.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[vfx-and-particles]]** Neon material does not emit real light; add separate SpotLight parts to project light and enhance glow.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[vfx-and-particles]]** Skinned mesh part positions don't update with animation; sync attached VFX/lights to bones each frame via PreSimulation and CollectionService tags.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Export animations at 30 FPS or higher with the same character rig, as a separate .fbx, and import via the Animation Editor.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[3d-modeling-rigging-and-animation]]** Add secondary (layered) motion so limbs react to body movement rather than moving in sync.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[player-psychology-and-game-feel]]** Use high-contrast focal points (glowing eyes and tentacle tips on a dark body) to direct player attention.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) **[[building-art-and-assets]]** Delete the AnimSaves folder after closing the Animation Editor; its files are only needed during editing.

## Numbers
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) Max triangles per mesh part: **10,000** (Custom character import requirement per part)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) Max mesh size per axis: **2000 units** (Total mesh size limit for import)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) Max skinning influences per vertex: **4** (Recommended maximum)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) Minimum animation frame rate: **30 FPS** (Recommended for external DCC animation)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/custom-characters) Max texture map size: **1024x1024** (SurfaceAppearance guideline)

## Tools
Roblox Studio Importer, Animation Editor, SurfaceAppearance, CollectionService, RunService.PreSimulation

## He points to
- Roblox docs: Mesh Requirements

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[player-psychology-and-game-feel]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
