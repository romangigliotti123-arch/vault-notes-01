---
type: research-source
id: off-avatar_dynamic-heads_specifications
title: "Roblox Creator Docs: avatar_dynamic-heads_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/dynamic-heads/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "other", "rigging-animation"]
---
# off-avatar_dynamic-heads_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs on dynamic head body specs: outer cage with left eye, right eye, and mouth landmarks (mouth on second loop); at least 17 FACS poses; 5 facial action validation tests; Marketplace requirements (Plastic material, transparency 0, default vertex color, eyelash/eyebrow as Accessory, no scripts or extra parts). Does not cover Blender, blender-mcp, bpy, or FBX export.

## Claims
- c1: Dynamic head character bodies need an outer cage; the cage also sets facial landmarks (left eye, right eye, mouth) used in validation. *(doc, high; avatar-ugc-accessories)*
- c2: Mouth landmark vertices must be on the second loop of vertices from the mouth opening to avoid landmark validation issues. *(doc, high; avatar-ugc-accessories)*
- c3: Avatar character bodies require at least 17 FACS poses for avatar chat, including LeftEyeClosed, RightEyeClosed, EyesLookDown, JawDrop, Pucker, and lip/cheek/brow controls. *(doc, high; rigging-animation)*
- c4: Validation requires passing 5 facial action tests: left blink, right blink, mouth open, happy, sad; the head must deform at cage landmarks for each or validation fails. *(doc, high; rigging-animation)*
- c5: Marketplace requirements: MeshPart Material Plastic, Transparency 0, VertexColor 1,1,1, eyelash/eyebrow assets added as Accessory objects, and no extraneous Script or Part objects in the Model. *(doc, high; avatar-ugc-accessories)*
- c6: Avatar Setup auto-generates head cage and facial animation; users can submit models without avatar components, then download as .gltf to adjust FACS or cage data in a third-party tool. *(doc, medium; automation-and-creator-workflows)*
- c7: Source is Roblox official docs on dynamic head specs; it does not mention Blender, blender-mcp, bpy, or Claude workflows, so it is only tangentially relevant to the topic. *(doc, high; other)*

## Numbers
- n1: **Required FACS poses**: 17 
- n2: **Facial action validation tests**: 5 
- n3: **Sad expression LeftCheekRaiser/RightCheekRaiser**: 0.85 
- n4: **Facial landmarks required**: 3 

## Points to
- https://create.roblox.com/docs/avatar/dynamic-heads/validate
- https://create.roblox.com/docs/avatar/dynamic-heads/caging-best-practices
- https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/art/modeling/specifications
- https://create.roblox.com/docs/art/accessories/publish-eyebrows-eyelashes
