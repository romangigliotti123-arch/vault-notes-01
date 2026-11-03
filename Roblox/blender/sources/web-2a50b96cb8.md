---
type: research-source
id: web-2a50b96cb8
title: "Roblox docs: avatar/character-bodies/specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/specifications.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0770
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-2a50b96cb8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox spec for R15/R15+ character bodies prepared in Blender/Maya: 15 mesh objects with _Geo naming, triangle budgets per asset (10,742 total), bounding box limits, _Att attachments, rig hierarchy, skinning limits, outer cages, textures and Marketplace requirements. No Claude/MCP/bpy content.

## Claims
- c1: Character body = 15 separate mesh objects; must be watertight, no N-gons, frozen transforms with pivots at 0,0,0, facing +Z, up +Y, exported in I/A/T-pose. *(doc, high; avatar-ugc-accessories)*
- c2: Engine converts quads to tris; estimate tri count by doubling quad count. *(doc, high; mesh-texture-limits)*
- c3: On upload the body is split into 6 assets: DynamicHead, Torso, LeftArm, RightArm, LeftLeg, RightLeg. *(doc, high; avatar-ugc-accessories)*
- c4: Body parts must be named *_Geo (e.g. UpperTorso_Geo, LeftHand_Geo, Head_Geo) and limbs capped so each is watertight when separated. *(doc, high; avatar-ugc-accessories)*
- c5: Body parts must be fully opaque and fill at least 50% of their bounding box in front, side and back views. *(doc, high; avatar-ugc-accessories)*
- c6: Importer Rig Type sets body scale: Rthro = Normal, Rthro Narrow = Slender, Default = Classic. *(doc, high; blender-roblox-export-import)*
- c7: Importer converts objects with _Att suffix into Attachments only when importing meshes with caging data such as bodies. *(doc, high; blender-roblox-export-import)*
- c8: Grip attachments must be perpendicular to lower arm bone; for I-Pose set to 90,0,0. Root_Att must be at 0,0,0. Head attachments must sit on the visible head surface or violate Marketplace policy. *(doc, high; avatar-ugc-accessories)*
- c9: Standard R15 hierarchy: Root > HumanoidRootNode > LowerTorso > UpperTorso (Head, arms) and legs. Root and LowerTorso positions must be 0,0,0. *(doc, high; rigging-animation)*
- c10: Advanced R15 allows up to 37 optional bones (Spine, Chest, clavicles, HeadBase, finger joints 1-3, ToeBase). Optional bones must follow naming and the matching meshes must be skinned. *(doc, high; rigging-animation)*
- c11: After importing an advanced R15 rig, HumanoidRigDescription and/or DigitsRigDescription (one per articulated hand) must be inserted to sell on Marketplace and for animations to work; they detect bones by name. *(doc, high; rigging-animation)*
- c12: Skinning: max 4 bone influences per vertex, no influence on Root bone, keep symmetry. *(doc, high; rigging-animation)*
- c13: Marketplace textures can't exceed 2048x2048; higher-res are auto-downscaled. Custom skin tone uses transparent alpha on exposed skin areas. *(doc, high; mesh-texture-limits)*
- c14: Outer cages named <Part>_OuterCage (e.g. LeftUpperArm_OuterCage); do not delete vertices or alter UVs; use Roblox cage templates or Avatar Setup. Bodies need only an outer cage. *(doc, high; avatar-ugc-accessories)*
- c15: Marketplace: Material Plastic, Transparency 0, VertexColor 1,1,1; eyelashes/eyebrows as Accessory objects; no extraneous Scripts or Parts in the Model. *(doc, high; avatar-ugc-accessories)*

## Numbers
- n1: **DynamicHead max triangles**: 4000 
- n2: **Torso max triangles**: 1750 UpperTorso + LowerTorso
- n3: **Each arm/leg max triangles**: 1248 four limb assets
- n4: **Total body triangles**: 10,742 
- n5: **Total body bounding box min (W/L/D studs)**: 1.0/4.0/0.5 
- n6: **Total body bounding box max (W/L/D studs)**: 8.0/10.0/4.0 
- n7: **Head bbox min / max (W/L/D)**: 0.05/0.5/0.05 / 4/2/4 
- n8: **Arm and leg bbox max length**: 4.5 studs 
- n9: **Torso bbox min length / max**: 0.65 / 4.0 studs 
- n10: **Max bone influences per vertex**: 4 
- n11: **Max Marketplace texture**: 2048x2048 

## Techniques
- t1: **Pre-export body checklist**: Name 15 meshes *_Geo, cap limbs, freeze transforms, pivots 0,0,0, face +Z, I/A/T-pose, check tri budgets (quads x2), then follow export settings page for Blender/Maya.

## Points to
- export.md (Blender/Maya export settings)
- studio/importer.md Rig Scale options
- Roblox downloadable reference models (avatar/resources.md)
- Avatar Setup tool / body cage templates
- art/modeling/texture-specifications.md
- art/modeling/rigging.md
