---
title: "Docs: avatar / dynamic-heads / validate"
url: https://create.roblox.com/docs/avatar/dynamic-heads/validate.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads / validate

[Open](https://create.roblox.com/docs/avatar/dynamic-heads/validate.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on dynamic head validation for Marketplace heads. Validation uses the outer head cage to project facial landmarks onto the head mesh, then tests FACS poses (eyes closed, mouth open, happy/sad) for landmark displacement. Covers common failure causes and fixes, including 17-pose minimum and non-humanoid heads.

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[ai-and-tools]]** Use Avatar Setup to auto-generate head cage and FACS facial animation; then edit the output, or download as .gltf to adjust FACS/cage in a modeling tool.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** Position cage landmark vertices directly over the corresponding eye and mouth areas of the face.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** Keep the cage over the head mesh, not intersecting it; landmark projection expects the cage to sit on the mesh surface.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** Remove gaps, holes, and difficult surfaces on the face so landmarks can project; hollow gaps cause projection failure.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** If eyeballs or mouthbags are separate meshes, widen the cage projection area so landmarks land on the head mesh, not those parts.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** Ensure FACS animations visibly displace landmarks in eye and mouth regions; validation checks relative landmark movement from neutral.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** Provide at least 17 FACS poses covering the 5 basic actions; validation fails immediately below 17 detected poses.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) **[[3d-modeling-rigging-and-animation]]** For blocky non-humanoid heads, place cage landmarks where FACS animation can actually move them, even if eyes or mouth are missing.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) Minimum FACS poses for dynamic head validation: **17** (Validation fails immediately if fewer than 17 poses detected)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) Basic actions tested: **5** (Eyes closed (L/R), mouth open, happy and sad expressions)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate) Landmarks required to denote eye area: **3** (Error example: validation cannot apply 3 landmarks due to gap or cage overshoot)

## Tools
Avatar Setup, Roblox Studio, FACS pose mapping, glTF export

## He points to
- Dynamic head specifications - FACS poses
- Create basic dynamic heads
- Avatar Setup bug report

## Topics
[[3d-modeling-rigging-and-animation]] [[ai-and-tools]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
