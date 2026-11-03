---
title: "Docs: marketplace / validation-system"
url: https://create.roblox.com/docs/marketplace/validation-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: marketplace / validation-system

[Open](https://create.roblox.com/docs/marketplace/validation-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on the UGC validation system, which checks avatar bodies, cosmetics and accessories against platform specs before Marketplace upload or in-experience avatar asset creation. Lists validation categories (schema, mesh, texture, rigging, cages, attachments, dynamic head, security) and the error messages with fixes.

## Tips
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[ugc-and-avatar-economy]]** Validation is required only for assets intended for the Marketplace or player purchase; in-game-only assets skip it, though it still helps debug custom bodies and accessories.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Set every MeshPart Transparency to exactly 0; any other value fails validation.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Give all MeshParts in one upload the same AvatarPartScaleType StringValue (Classic, ProportionsNormal or ProportionsSlender); mismatches fail.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Remove all custom Attributes from every instance in the asset hierarchy before upload, otherwise validation fails.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Rig attachments must have rotation (0,0,0) and sit near the joint boundary where their body part meets its neighbour.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Bodies and layered accessories need skinning data; rigid accessories must have none. Skin only to official advanced R15 joints.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Keep the outer cage closely conforming to the render mesh and fully enclosing it; large gaps make layered clothing float or bloat.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Reset Bone.Transform to identity CFrame before upload; Bones must sit near the MeshPart boundary and not be coincident with their parent.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Remove floating vertices, thin spikes and disconnected micro-geometry, which inflate bounding boxes and break collision, thumbnails and layered fitting.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Use the official body cage template for cage UVs without adding, removing or merging UV vertices.
- [page](https://create.roblox.com/docs/marketplace/validation-system) **[[3d-modeling-rigging-and-animation]]** Use the built-in visualization tools in Studio to see asset-specific fix guides when validation fails.

## Numbers
- [page](https://create.roblox.com/docs/marketplace/validation-system) Dynamic head FACS poses: **At least 17** (Minimum required poses for dynamic head validation)
- [page](https://create.roblox.com/docs/marketplace/validation-system) Animation Weight value: **Greater than 0 (typically 1.0)** (Weight NumberValue in idle animation hierarchy)
- [page](https://create.roblox.com/docs/marketplace/validation-system) Opacity views checked: **6 orthographic views** (Front, back, left, right, top, bottom; each has a minimum opacity threshold)
- [page](https://create.roblox.com/docs/marketplace/validation-system) AvatarPartScaleType accepted values: **3** (Classic, ProportionsSlender, ProportionsNormal)

## Tools
Roblox Studio, AvatarCreationService

## He points to
- Create and publish animation packs
- Body specifications
- Dynamic head specifications
- Makeup specifications
- Rigid accessory specifications
- Layered accessory specifications

## Topics
[[3d-modeling-rigging-and-animation]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
