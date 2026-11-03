---
title: "Docs: avatar-setup / auto-setup-requirements"
url: https://create.roblox.com/docs/avatar-setup/auto-setup-requirements.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar-setup / auto-setup-requirements

[Open](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs spec for Avatar Setup: auto-converting custom 3D models into Roblox character bodies, rigid accessories and layered accessories. Covers supported rig/face inputs, mesh requirements (triangle budgets, head components, A/T-pose, watertight), and bundling assets in a Folder.

## Tips
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[ugc-and-avatar-economy]]** Use the Roblox-provided reference character body models built for Avatar Setup; many downloadable bodies fail validation and need modification.
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Keep character body within 10,742 triangles total (head 4000, arms 1248 each, legs 1248 each, torso 1750); Avatar Setup adds caps and segments that increase count.
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Make heads with 2 connected eyebags with half-sphere eyes and a connected mouthbag with upper teeth, lower teeth and tongue, none sharing vertices with the head.
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Use an upright A-pose or T-pose, facing negative Z, with no limbs overlapping from the front view; I-pose yields lower quality results.
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Make the model symmetrical, watertight (except eyes and mouth), with a distinct neck, no accessories, and texture maps (albedo, normal, metalness, roughness).
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Fit rigid and layered accessories onto a base body first, and bundle them with that body in one Folder; accessories without a body need a base body for correct fitting.
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) **[[3d-modeling-rigging-and-animation]]** Facial rigs must have RootFaceJoint (usually DynamicHead) parented to the Head joint, with at least 17 facial poses and neutral on frame 0.

## Numbers
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Max total character body triangles: **10,742** (Avatar Setup body limit; quads max 5495)
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Head max triangles / quads: **4000 / 2000** (Per body part grouping)
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Arms max triangles per arm / quads: **1248 / 624** (Per arm)
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Legs max triangles per leg / quads: **1248 / 624** (Per leg)
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Torso max triangles / quads: **1750 / 875** (Torso body part grouping)
- [page](https://create.roblox.com/docs/avatar-setup/auto-setup-requirements) Minimum facial animation poses: **17** (Required for custom facial rig with FACS data)

## Tools
Avatar Setup (Roblox Studio tool)

## He points to
- Roblox Creator Docs: Avatar Setup specifications

## Topics
[[3d-modeling-rigging-and-animation]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
