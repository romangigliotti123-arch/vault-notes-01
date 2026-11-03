---
type: research-source
id: web-7df4b0ea0d
title: "Roblox docs: avatar/makeup/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/makeup/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0692
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits"]
---
# web-7df4b0ea0d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on authoring face makeup (Decal-based texture layers) with Blender/Maya templates, plus eyebrow/eyelash MeshParts. Gives Blender FBX/glTF export settings for makeup (Custom Properties, Only Deform Bones), template workflow, and Marketplace decal limit. No Claude/MCP/bpy content.

## Claims
- c1: Makeup is baked into Decal objects, one texture layer per region (eyes, lips, face); regions overlap for seamless looks. *(doc, high; avatar-ugc-accessories)*
- c2: Marketplace makeup assets can include up to 6 total Decal objects, in any combination of regions. *(doc, high; avatar-ugc-accessories)*
- c3: Eyebrows and eyelashes are Models containing MeshParts with skinning and cage data so they animate with facial expressions. *(doc, high; avatar-ugc-accessories)*
- c4: Blender export for makeup: enable Include > Custom Properties (for makeup UV data transfer) and Armature > Only Deform Bones (keeps eyebrow/eyelash skinning). Standard modeling export requirements still apply. *(doc, high; blender-roblox-export-import)*
- c5: Maya export for makeup: enable Deformed Models > Skins so eyebrow/eyelash skinning data is exported. *(doc, high; blender-roblox-export-import)*
- c6: On import, Studio auto-detects mesh names and associated textures and generates Decal objects under the imported model. *(doc, high; blender-roblox-export-import)*
- c7: Template textures are named TransferTexture_Eyes, TransferTexture_Face, TransferTexture_Lips; PBR maps are Color, Metallic, Roughness, and must be reassigned in Blender/Maya templates before export. *(doc, medium; mesh-texture-limits)*
- c8: Mesh template is recommended over cage template (more intuitive, higher-fidelity mesh/UVs). Cage template has one transfer before projection vs two, possibly fewer artifacts. You cannot transfer makeup between templates. *(doc, high; avatar-ugc-accessories)*
- c9: Makeup can only be tested currently in the downloadable MakeupBeta.zip place file from the Roblox/avatar GitHub repo; drag decals/accessories into a character's Makeup or Accessories folder, then Play. *(doc, high; automation-and-creator-workflows)*
- c10: Templates are provided for Blender, Maya, and FBX/glTF, in realistic and blocky heads; texture packs for Photoshop/GIMP, Substance Painter, Procreate. Ucupaint is suggested as a Blender PBR plugin. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Max Decal objects per Marketplace makeup asset**: 6 any combination of regions
- n2: **Face regions**: 3 eyes, lips, face

## Techniques
- t1: **Makeup creation pipeline**: Download mesh template head; edit TransferTexture_Eyes/Face/Lips in 2D/PBR tool; reassign textures in Blender/Maya; adjust face cages; export FBX/glTF with makeup settings; import to Studio; drag decals into Makeup folder; Play.
- t2: **Blender makeup export settings**: In the FBX/glTF export dialog enable Include > Custom Properties and Armature > Only Deform Bones.
- t3: **Procreate texture export**: Hide all but one component layer, Share Textures - PNG, keep only Color/Metallic/Roughness, replace Color with transparent export via clipboard with background disabled, rename (Lips-Color etc.).

## Points to
- https://github.com/Roblox/avatar/blob/main/Makeup/MakeupBeta.zip
- Ucupaint Blender add-on
- Substance Painter
- Materialize
- avatar/dynamic-heads/caging-best-practices
- art/modeling/export-requirements
- avatar/makeup/reassign-textures
- avatar/makeup/import
