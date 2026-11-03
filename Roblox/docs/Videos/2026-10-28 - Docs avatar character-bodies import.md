---
title: "Docs: avatar / character-bodies / import"
url: https://create.roblox.com/docs/avatar/character-bodies/import.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / character-bodies / import

[Open](https://create.roblox.com/docs/avatar/character-bodies/import.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on importing a rigged character body .fbx/.gltf via the 3D Importer as a Model, fixing textures manually in Asset Manager (PBR SurfaceAppearance mapping), and next steps: HumanoidRigDescription, playtesting as StarterCharacter, and Marketplace/Creator Store publishing.

## Tips
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[building-art-and-assets]]** If your single-mesh model needs splitting, use the Avatar Setup tool to partition it into the 15 required avatar body parts.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[3d-modeling-rigging-and-animation]]** For advanced R15 rigs, set Rig Type to Custom Humanoid in the Importer's Rig General section.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[3d-modeling-rigging-and-animation]]** Set Rig Scale to the character's appropriate Body Scale and Constraint Type to Joint Upgrade when importing a character body.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[building-art-and-assets]]** If textures fail to load, upload them manually via Asset Manager; save and publish the game first if Asset Manager is inaccessible.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[building-art-and-assets]]** For PBR textures, add a SurfaceAppearance to the MeshPart and map ColorMap=_ALB, MetalnessMap=_MTL, NormalMap=_NOR, RoughnessMap=_RGH.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[3d-modeling-rigging-and-animation]]** Add HumanoidRigDescription and/or DigitsRigDescription objects for Marketplace and animation requirements; use Adaptive Animation plugin to remap joints and set a t-pose reference if needed.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[testing-debugging-and-qa]]** Playtest a character by renaming the Model to StarterCharacter and moving it into StarterPlayer before testing; verify with Test character bodies docs.
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) **[[ugc-and-avatar-economy]]** Marketplace upload involves extra validation and moderation; the Importer's checks alone do not guarantee avatar-ready character bodies, so verify against character body specs before selling.

## Numbers
- [page](https://create.roblox.com/docs/avatar/character-bodies/import) Avatar body parts: **15 parts** (Required partition count for an avatar character body from a single mesh)

## Tools
Studio Importer (3D Importer), Asset Manager, Avatar Setup tool, Adaptive Animation plugin, HumanoidDescription, HumanoidRigDescription, DigitsRigDescription

## He points to
- Importer docs
- Test character bodies docs

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
