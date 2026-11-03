---
type: research-source
id: web-327c70ca7e
title: "Roblox docs: avatar/dynamic-heads/specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/specifications.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "mesh-texture-limits"]
---
# web-327c70ca7e

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on dynamic head specs for avatar character bodies. Covers the outer cage with three facial landmarks (left eye, right eye, mouth), 17 required FACS poses for avatar chat, five validation facial actions, and Marketplace material/transparency/vertex-color rules. Does not mention Blender, bpy, or FBX/glTF export settings.

## Claims
- c1: Dynamic head bodies require an outer cage for layered accessories; the cage also sets facial landmarks used in validation. *(doc, high; avatar-ugc-accessories)*
- c2: Three facial landmarks are required in the cage: left eye, right eye, and mouth. Non-humanoid faces still need them. *(doc, high; avatar-ugc-accessories)*
- c3: Mouth landmark vertices must sit on the second loop of vertices from the mouth opening to avoid landmark validation issues. *(doc, high; avatar-ugc-accessories)*
- c4: Avatar character bodies require at least 17 FACS poses for avatar chat, including LeftEyeClosed, RightEyeClosed, EyesLookDown, JawDrop, and Pucker. *(doc, high; avatar-ugc-accessories)*
- c5: Validation requires five facial actions to deform at cage landmarks: left blink, right blink, mouth open, happy, and sad. Failure fails the asset. *(doc, high; avatar-ugc-accessories)*
- c6: Sad-expression test uses LeftCheekRaiser and RightCheekRaiser = 0.85; other sad-test poses are set to 1. *(doc, high; avatar-ugc-accessories)*
- c7: Marketplace dynamic head MeshParts must have Material set to Plastic, Transparency 0, and VertexColor at default 1,1,1. *(doc, high; avatar-ugc-accessories)*
- c8: Separate eyelash and eyebrow assets must be added to the body model as Accessory objects; the Model must not contain extra Scripts or Parts. *(doc, high; avatar-ugc-accessories)*
- c9: Avatar Setup can auto-generate head cage and facial animation components; output can be downloaded as .gltf and FACS/cage data adjusted in a third-party modeling tool. *(doc, high; automation-and-creator-workflows)*
- c10: Validation uses a specialized process that may require adjusting an existing dynamic head asset. *(doc, medium; mesh-texture-limits)*

## Numbers
- n1: **required FACS poses**: 17 minimum for avatar chat support
- n2: **validation facial actions**: 5 must deform at cage landmarks or validation fails
- n3: **facial landmarks**: 3 left eye, right eye, mouth
- n4: **CheekRaiser value in sad test**: 0.85 LeftCheekRaiser and RightCheekRaiser

## Techniques
- t1: **Cage landmark placement**: Place eye and mouth landmark vertices on outer cage; mouth landmark on second vertex loop from mouth opening; verify they project onto base mesh during validation.
- t2: **Avatar Setup then edit**: Submit body without avatar components to Avatar Setup, download output as .gltf, then fix FACS or cage data in third-party modeler.

## Quotes (brief, for attribution)
> The mouth landmark vertices are on the second loop of vertices from the mouth opening.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/validate.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/caging-best-practices.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/facs-poses-reference.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/specifications.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/publish-eyebrows-eyelashes.md
