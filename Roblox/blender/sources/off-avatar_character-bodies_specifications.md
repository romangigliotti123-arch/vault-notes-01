---
type: research-source
id: off-avatar_character-bodies_specifications
title: "Roblox Creator Docs: avatar_character-bodies_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/character-bodies/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0037
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "mesh-texture-limits", "rigging-animation"]
---
# off-avatar_character-bodies_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs spec for character body models used in Studio/Marketplace. Covers 15 named mesh parts, watertight/quads/transform rules, bounding-box min/max, per-asset triangle budgets (total 10,742), attachment naming, standard vs advanced R15 rig hierarchy, skinning max 4 influences, texture 2048 cap, outer cages. Nothing on Blender MCP, bpy, or Claude workflows.

## Claims
- c1: Character body triangle budgets: DynamicHead 4000, Torso 1750, each arm 1248, each leg 1248; total 10,742 tris. *(doc, high; mesh-texture-limits)*
- c2: Roblox converts imported quads to tris; quick tri estimate in modeling app is double the quad count. *(doc, high; mesh-texture-limits)*
- c3: Body textures for Marketplace assets cannot exceed 2048x2048. *(doc, high; mesh-texture-limits)*
- c4: Character body must have 15 mesh objects named e.g. UpperTorso_Geo, LeftHand_Geo, Head_Geo; limbs must be capped to be watertight when separated. *(doc, high; avatar-ugc-accessories)*
- c5: Body scale bounding box min total 1.0 x 4.0 x 0.5 studs; max total 8.0 x 10.0 x 4.0 studs (width/length/depth). *(doc, high; avatar-ugc-accessories)*
- c6: Importer Rig Type mapping: Rthro = Normal, Rthro Narrow = Slender, Default = Classic. *(doc, high; avatar-ugc-accessories)*
- c7: Standard R15 hierarchy: Root > HumanoidRootNode > LowerTorso > UpperTorso > Head/arms; LowerTorso and Root must be at 0,0,0. *(doc, high; rigging-animation)*
- c8: Advanced R15 supports up to 37 optional bones; HumanoidRigDescription and DigitsRigDescription objects must be inserted after import to sell on Marketplace. *(doc, high; rigging-animation)*
- c9: Skinning: max 4 bone influences per vertex; no influences on Root bone. *(doc, high; rigging-animation)*
- c10: Attachments are imported as Attachment objects only when names carry the _Att suffix (e.g. FaceCenter_Att, Hat_Att, RightGrip_Att); grip attachments perpendicular to lower arm (I-pose: 90,0,0). *(doc, high; avatar-ugc-accessories)*
- c11: Transformations must be frozen with pivots at 0,0,0; character faces +Z and stands along +Y; use I, A or T pose. *(doc, high; avatar-ugc-accessories)*
- c12: Marketplace body requirements: MeshPart Material Plastic, Transparency 0, VertexColor 1,1,1; no extraneous Script or Part objects in the Model. *(doc, high; avatar-ugc-accessories)*
- c13: Outer cage meshes named <PartName>_OuterCage; do not delete vertices or alter UVs; body needs only outer cage. *(doc, high; avatar-ugc-accessories)*
- c14: Body parts must be fully opaque and occupy at least 50% of their bounding box in front, side and back views. *(doc, medium; avatar-ugc-accessories)*

## Numbers
- n1: **Triangle budget DynamicHead**: 4000 
- n2: **Triangle budget Torso / each limb**: 1750 / 1248 
- n3: **Total body triangles**: 10,742 
- n4: **Max texture resolution**: 2048x2048 
- n5: **Max bone influences per vertex**: 4 
- n6: **Advanced R15 optional bones**: up to 37 
- n7: **Body bounding box min total (W/L/D studs)**: 1.0 / 4.0 / 0.5 
- n8: **Body bounding box max total (W/L/D studs)**: 8.0 / 10.0 / 4.0 
- n9: **Visibility fill of bounding box**: at least 50% 
- n10: **Body mesh objects**: 15 (become 6 assets) 

## Quotes (brief, for attribution)
> Character body models for avatars are made up of 15 separate mesh objects and require additional geometry requirements to import into Studio and publish successfully.  (create.roblox.com)
> Each asset of your character model must not exceed our maximum tri budget.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/export
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/art/modeling/rigging
- https://create.roblox.com/docs/avatar/resources
- https://create.roblox.com/docs/art/accessories/publish-eyebrows-eyelashes
