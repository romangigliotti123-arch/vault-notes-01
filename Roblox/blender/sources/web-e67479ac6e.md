---
type: research-source
id: web-e67479ac6e
title: "DevForum thread 3094203"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/3094203"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "rigging-animation", "roblox-export-settings"]
---
# web-e67479ac6e

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox DevForum guide (Aug 2024) on preparing R15 character meshes in Blender: separating body parts with Data Transfer custom normals, morphing and UV-linking Roblox body cage resources, attachment placement rules, UV mapping for 2D clothing, modesty layer on UpperTorso/LowerTorso, and post-import fixes for ankle/neck rig attachments and WrapTarget CageOrigin. Blender-terminology only; no Claude/MCP or bpy content.

## Claims
- c1: Body cage resource must be morphed to the character without vertex or face deletion, then UV data linked (Ctrl+L) from morphed copy to original cage part, selecting morphed part first, to avoid UV errors on import. *(doc, medium; avatar-ugc-accessories)*
- c2: Attachments must not have translation applied after positioning; applying it breaks Studio attachments so tools and accessories will not work. *(experience, medium; avatar-ugc-accessories)*
- c3: Separating body parts causes shading issues; fix by duplicating the model, adding Data Transfer modifier (Face Corner Data > Custom Normals) per part, then applying. *(experience, medium; common-mistakes-fixes)*
- c4: 2D clothing is no longer officially supported for UGC bundles but correctly UV-mapped body parts should still work, per the author. *(opinion, low; avatar-ugc-accessories)*
- c5: Modesty layer texture must be applied to both UpperTorso and LowerTorso because Studio does not use LowerTorso texture alone. *(experience, medium; avatar-ugc-accessories)*
- c6: After import, set Left/Right AnkleRigAttachment and child OriginalPosition to 0,0.03 (check Studio's range during avatar setup if it differs). *(experience, medium; rigging-animation)*
- c7: Set all WrapTarget CageOrigin to 0,0,0 to avoid errors; find them by searching cageorigin= in Explorer search. *(experience, medium; rigging-animation)*
- c8: NeckRigAttachments on UpperTorso and Head can be copied from another model (e.g. Rig Builder plugin default) then repositioned. *(experience, low; rigging-animation)*
- c9: Attachment helper meshes suggested: UV sphere with 10 segments and 10 rings; rotate left/right grip 90 degrees on X axis. *(experience, low; roblox-export-settings)*

## Numbers
- n1: **AnkleRigAttachment OriginalPosition**: 0,0.03 
- n2: **WrapTarget CageOrigin**: 0,0,0 
- n3: **Attachment UV sphere**: 10 segments, 10 rings 
- n4: **Grip rotation**: 90 degrees on X axis 

## Techniques
- t1: **Data Transfer custom normals per body part**: Duplicate model; separate original into parts; on each part add Data Transfer modifier, source = duplicate, enable Face Corner Data > Custom Normals; apply modifiers; delete duplicate.
- t2: **Body cage morphing and UV linking**: Morph Roblox cage resource to character without deleting verts/faces; select your morphed part then original cage part; Ctrl+L link UV data.

## Quotes (brief, for attribution)
> Attachments should NOT have their translation/position transform applied after positioning. Doing so will completely freak out Roblox studios attachments and tools and accessories will NOT work.  (devforum.roblox.com)
> This is because the Roblox Studio engine kind of doesn't use the LowerTorso's texture, so the UpperTorso needs to have the modesty layer texture as well.  (devforum.roblox.com)

## Contradictions flagged
- 2D clothing support for UGC bundles is not entirely removed; correctly UV-mapped parts still work though not officially supported. (vs Common belief that 2D clothing was fully removed from UGC bundles)

## Points to
- https://create.roblox.com/docs/art/characters
- https://create.roblox.com/docs/avatar/resources
- https://devforum.roblox.com/t/uv-map-references-for-r15-r6-humanoid-body-parts-to-support-clothing/1760371
- https://www.youtube.com/watch?v=xJn7QfmXINw
- Rig Builder plugin
