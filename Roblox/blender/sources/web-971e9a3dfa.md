---
type: research-source
id: web-971e9a3dfa
title: "Roblox docs: art/modeling/project-files"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/project-files.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0630
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-971e9a3dfa

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs index of downloadable modeling project files: reference models (tree, Shoebot, Creature, avatars, mannequins), Blender/.ma/.fbx templates for R15 rig, cages, and avatar heads, plus Blender add-ons (Studio upload plugin, validation tool, Calisthenics skinning checker). No Claude/MCP/bpy content.

## Claims
- c1: Body cage templates include the 15 individual body-part cages required for caging avatar bodies; clothing cage templates include a full-body inner and outer cage mesh. *(doc, high; avatar-ugc-accessories)*
- c2: A standard R15 rig template for Blender is provided (.blend, .ma, .fbx) for rigging bodies and clothing; a combined template adds body cages and attachment points. *(doc, high; rigging-animation)*
- c3: Roblox avatar template files (Round, Square, Muzzle, SemiRealistic, Anime, Caricature, Stylized) come as Blender and FBX with pre-baked avatar components. Cleanup steps (combine head geometry) are required before they validate for Marketplace. *(doc, high; avatar-ugc-accessories)*
- c4: Lola reference R15 model has no inner/outer cage data, so it cannot equip layered accessories. *(doc, high; avatar-ugc-accessories)*
- c5: The mannequin FBX files with cages hold individual outer body cages and may not import correctly into Studio without modification. *(doc, high; blender-roblox-export-import)*
- c6: For Marketplace upload, a head ornament such as the Fish person's bulb antenna must be a separate head accessory, not part of head geometry. *(doc, high; avatar-ugc-accessories)*
- c7: An open-source Blender add-on (Roblox Blender plugin) uploads assets directly from Blender to Studio. *(doc, high; automation-and-creator-workflows)*
- c8: A Blender validation add-on checks avatar technical compatibility before Studio import. *(doc, high; avatar-ugc-accessories)*
- c9: A Blender Calisthenics add-on checks skinning data on characters and clothing. *(doc, high; rigging-animation)*
- c10: The maple tree sample is a skinned model with soil, branches and leaves as separate meshes bound to one armature, with UV textures for SurfaceAppearance. *(doc, high; mesh-texture-limits)*

## Numbers
- n1: **Creature model size**: 11 meshes, 50+ bones Beyond The Dark showcase creature reference FBX
- n2: **Body part cages**: 15 individual cages required for avatar bodies

## Techniques
- t1: **Start from combined template**: Download Combined_Templates.zip (.blend/.ma/.fbx) with rig skeleton, body cages and attachment points; use it to rig and cage bodies and clothing, then validate with the Blender validation add-on before Studio import.

## Points to
- https://www.youtube.com/watch?v=QwZaA9Gc-WQ
- art/modeling/roblox-blender-plugin.md
- art/accessories/validation-tool.md
- art/modeling/skin-a-humanoid-model.md
- art/modeling/skin-a-simple-mesh.md
- art/characters/creating/combine-head-geometry.md
- avatar/character-bodies/specifications.md
