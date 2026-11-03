---
title: "Docs: avatar / dynamic-heads / specifications"
url: https://create.roblox.com/docs/avatar/dynamic-heads/specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads / specifications

[Open](https://create.roblox.com/docs/avatar/dynamic-heads/specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs spec for dynamic-head character bodies: required outer cage with three facial landmarks, minimum 17 FACS poses for avatar chat, five validation action-unit tests, and Marketplace material/transparency/vertex color and component rules.

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Include an outer cage on dynamic heads; it is needed for layered accessories and sets facial landmarks used in validation.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Place mouth landmark vertices on the second loop of vertices from the mouth opening to avoid landmark validation failures.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Ensure left eye, right eye and mouth landmarks exist even for non-humanoid faces so they can project onto the base mesh.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Provide at least the 17 required FACS poses for avatar chat; include as many additional facial poses as possible for expressiveness.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Make sure the head deforms at cage landmarks for all five validation actions (both eye blinks, jaw drop, happy, sad) or validation fails.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Use Avatar Setup to auto-generate head cage and facial animation components, then edit the output; export as .gltf to adjust FACS or cage data externally.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Set MeshPart Material to Plastic, Transparency to 0, and VertexColor to 1,1,1 for Marketplace sale.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[3d-modeling-rigging-and-animation]]** Add separate eyelash and eyebrow assets as Accessory objects in the character model, not as loose parts.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) **[[common-mistakes]]** Remove extraneous Scripts and additional Parts from the Model; they violate Marketplace body requirements.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) Required FACS poses for avatar chat: **17 minimum**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) Dynamic head validation facial action tests: **5 must pass**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) Facial landmarks required in outer cage: **3 (left eye, right eye, mouth)**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) Sad expression CheekRaiser value (Left/Right): **0.85**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/specifications) Transparency required for Marketplace MeshPart: **0**

## Tools
Avatar Setup, Roblox Studio

## He points to
- Dynamic head validation
- Dynamic head caging best practices
- Publish bodies with eyelashes and eyebrows
- Roblox custom mesh specifications
- Roblox character body specifications

## Topics
[[3d-modeling-rigging-and-animation]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
