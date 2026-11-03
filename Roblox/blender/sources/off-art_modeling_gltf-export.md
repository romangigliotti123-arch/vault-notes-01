---
type: research-source
id: off-art_modeling_gltf-export
title: "Roblox Creator Docs: art_modeling_gltf-export"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/gltf-export"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "other"]
---
# off-art_modeling_gltf-export

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on beta glTF export from Studio. Covers supported components (meshes, textures, rigging, vertex colors, cages, FACS), limits (no animation, weak layered accessory support), permission rules for exportable vs. non-exportable assets, and export steps from Explorer or File menu. Mentions Blender/Maya as target apps but no Blender-specific settings, scale, or axes.

## Claims
- c1: Roblox Studio glTF export is in beta and must be enabled through Studio beta features settings. *(doc, high; blender-roblox-export-import)*
- c2: Studio can export selected Explorer items (right-click Save / Export > Export as glTF) or the entire place (File > Export as glTF). *(doc, high; blender-roblox-export-import)*
- c3: glTF export supports meshes, textures, rigging and skinning data, vertex colors, cages, and dynamic head FACS data. *(doc, high; blender-roblox-export-import)*
- c4: glTF export does not support animation data. *(doc, high; blender-roblox-export-import)*
- c5: Layered accessories export inconsistently: clothing may misposition and will not deform to avatar bodies outside Roblox. *(doc, high; avatar-ugc-accessories)*
- c6: Avatar auto setup output can be exported as glTF, then meshes, cages, or rigging finalized in a third-party tool. *(doc, high; avatar-ugc-accessories)*
- c7: Export permission check runs on export; conflicts trigger a permission prompt with details before the file is saved. *(doc, high; automation-and-creator-workflows)*
- c8: Exportable assets: those uploaded to your account or group, and mesh/image assets explicitly shared with you or your group. *(doc, high; automation-and-creator-workflows)*
- c9: Not exportable: Avatar Marketplace assets, acquired Creator Store assets, collaborator assets not explicitly shared, and public Open Use assets not shared with you. *(doc, high; automation-and-creator-workflows)*
- c10: Common glTF use cases: finalizing avatar auto-setup output externally, high-fidelity scene renders of whole place in other 3D apps, and editing Studio part-based models or editable meshes externally. *(doc, medium; other)*

## Techniques
- t1: **Explorer glTF export**: Select items in Explorer, right-click > Save / Export > Export as glTF, choose components, click Export, pass permission check, pick save path.

## Points to
- https://create.roblox.com/docs/avatar-setup/index.md#auto-setup
- https://en.wikipedia.org/wiki/GlTF
