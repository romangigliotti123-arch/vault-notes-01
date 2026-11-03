---
title: "Docs: avatar / dynamic-heads / test"
url: https://create.roblox.com/docs/avatar/dynamic-heads/test.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads / test

[Open](https://create.roblox.com/docs/avatar/dynamic-heads/test.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on testing dynamic heads in Studio: importing dynamic head models, using the generated FaceControls instance to pose/animate faces, reference files, converting face accessory MeshParts to Accessories with the Accessory Fitting Tool and AutoSkin, and a troubleshooting table of import errors and warnings.

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Use Avatar Setup presets to quickly preview a character's head animations and head accessories before building your own dynamic head.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[building-art-and-assets]]** Face accessories import as MeshParts; convert them with the Accessory Fitting Tool so they're compatible with the dynamic head.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Enable WrapLayer.AutoSkin (EnabledPreserve keeps existing skinning; EnabledOverride replaces it) so face accessories follow expressions without manual skinning weights.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Ensure every imported joint has a unique name; duplicate joint names cause the import to fail.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Limit correctives to at most 3 control names; deeper correctives are unsupported and fail import.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Name corrective poses using FACS base poses only, and define every base pose a corrective uses (e.g. Funneler and JawDrop for Funneler_JawDrop).
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Set exactly one animation frame to Neutral and map each FACS pose or corrective to a single frame using Extra Attributes named Frame0, Frame1, etc.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Define a full set of base poses; fewer than the full base set may leave the character unable to express itself.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[3d-modeling-rigging-and-animation]]** Animate heads in the Animation Editor using individual tracks or the Face Animation Editor, driving FaceControls properties.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) **[[testing-debugging-and-qa]]** Check the Output window after import; it reports head errors and warnings during configuration.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) Max corrective control names: **3** (Correctives with more than 3 corrective poses are unsupported in dynamic head import)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/test) Default AutoSkin value: **Disabled** (WrapLayer.AutoSkin default; options are Disabled, EnabledOverride, EnabledPreserve)

## Games
- **Head Animation In-Game Editor**: Reference game previewing Goblin and Blocky heads with various accessories in an editor.
- **Head Schema Reference**: Reference game with a Blocky head model containing FaceControls, showing how dynamic heads interact with Studio's interface.

## Tools
Roblox Studio Importer, Accessory Fitting Tool (AFT), Animation Editor, Face Animation Editor, Avatar Setup

## He points to
- Customize characters with humanoid description
- Animate heads

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
