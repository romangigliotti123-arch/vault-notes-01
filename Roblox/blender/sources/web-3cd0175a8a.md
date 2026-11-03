---
type: research-source
id: web-3cd0175a8a
title: "Roblox docs: avatar/resources"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/resources.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0794
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-3cd0175a8a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator-docs resource index for avatar creation: downloadable reference characters, Blender/Maya/FBX rig, attachment and cage templates, mannequins, head templates, and links to the Blender Studio plugin, Validation tool and Calisthenics tool. No Claude/MCP/bpy content; useful for Blender-to-Roblox avatar asset inputs and validation caveats.

## Claims
- c1: Project files (rig, attachments, cages) are for third-party apps and are not suitable for direct import into Studio. Templates come in .blend, .ma and .fbx. *(doc, high; avatar-ugc-accessories)*
- c2: Body cage templates include the 15 individual body part cages needed to cage avatar bodies. The clothing cage template has a full-body inner and outer cage mesh. *(doc, high; avatar-ugc-accessories)*
- c3: Standard R15 reference characters (Nature Girl, Stylish Male) contain clothing and accessories that may cause validation errors unless removed. *(doc, high; avatar-ugc-accessories)*
- c4: Opening the Nature Girl and Stylish Male Blender files may show armature bones in odd orientations, because the source was exported from Maya. Roblox says this doesn't affect rig performance. *(doc, high; blender-roblox-export-import)*
- c5: When importing the Roxie higher-fidelity model, set Rig Scale to Rthro Narrow. *(doc, high; blender-roblox-export-import)*
- c6: Mannequin models (Classic, Rthro, Rthro Slender) are scale and caging references. They aren't meant for direct Studio upload and may fail import or validation. The 'With Cage' FBX holds individual outer body cages and may need modification to import. *(doc, high; avatar-ugc-accessories)*
- c7: Auto-Setup reference assets (Nature Girl, Stylish Male) fail normal validation if uploaded as-is. They aren't compatible with the traditional avatar creation workflow. *(doc, high; avatar-ugc-accessories)*
- c8: Lola, a skinned R15 model from the skinning guide, has no inner or outer cage data, so it can't equip rigid or layered accessories. *(doc, high; avatar-ugc-accessories)*
- c9: Fish Person reference: for Marketplace upload, the bulb antenna must be a separate head accessory, not part of the head geometry. *(doc, high; avatar-ugc-accessories)*
- c10: Head and body templates (Round, Square, Muzzle, SemiRealistic, Anime, Caricature, Stylized) are Blender and FBX files with pre-baked components. They require the cleanup steps (combine head geometry) to validate before Marketplace publishing. *(doc, high; avatar-ugc-accessories)*
- c11: Some template eyebrow/eyelash meshes may not be fully compatible with the template body. See the layered accessory specs for face accessories. *(doc, medium; avatar-ugc-accessories)*
- c12: Roblox lists three Blender tools: the open-source Blender Studio plugin (upload assets from Blender to Studio), the Validation Tool (checks avatar technical compatibility before Studio import), and the Calisthenics Tool (checks skinning data on characters and clothing). *(doc, high; automation-and-creator-workflows)*
- c13: Some listed add-ons are not actively supported and may be incompatible with your hardware version. *(doc, medium; automation-and-creator-workflows)*
- c14: Mannequin and Robuta higher-fidelity references ship with 2K PBR textures. HipToBeSquare has color, roughness and metal maps. *(doc, medium; mesh-texture-limits)*
- c15: Advanced R15 rigs add bones/joints for articulated hands, shoulders and spine. Standard R15 rigs have the standard bone count. *(doc, high; rigging-animation)*

## Numbers
- n1: **individual body part cages in body cage template**: 15 
- n2: **PBR texture size in Mannequin and Robuta references**: 2K 

## Techniques
- t1: **Start from combined templates**: Download Combined_Templates.zip (.blend/.ma/.fbx), which has the standard R15 rig, body cages and attachment points. Use it to rig and cage bodies and clothing in Blender.
- t2: **Pre-check in Blender**: Run the Blender Validation Tool before importing to Studio. Use the Calisthenics Tool to check skinning on characters and clothing.
- t3: **Upload from Blender via plugin**: Use the open-source Roblox Blender Studio plugin to upload assets directly from Blender to Studio.

## Points to
- https://create.roblox.com/docs/art/modeling/roblox-blender-plugin
- https://create.roblox.com/docs/art/accessories/validation-tool
- https://create.roblox.com/docs/art/modeling/calisthenics-tool
- https://www.youtube.com/watch?v=QwZaA9Gc-WQ
- Avatar Auto-Setup docs
- Create characters with templates tutorial
