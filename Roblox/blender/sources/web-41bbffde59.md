---
type: research-source
id: web-41bbffde59
title: "Roblox docs: art/modeling/gltf-export"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/gltf-export.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-41bbffde59

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs for beta glTF export from Studio to external tools such as Blender or Maya. Covers supported components (meshes, textures, rigging/skinning, vertex colors, cages, FACS), limitations (no animation, inconsistent layered accessories), and permission rules. Export runs from Explorer or File menu. It covers Studio-to-Blender, not Blender-to-Roblox import.

## Claims
- c1: Roblox Studio glTF export is in beta and must be enabled in settings; the doc says specs may change during beta. *(doc, high; blender-roblox-export-import)*
- c2: glTF export does not support animation data. *(doc, high; blender-roblox-export-import)*
- c3: glTF export supports rigging and skinning data. *(doc, high; rigging-animation)*
- c4: Layered clothing accessories may not position correctly in glTF export and won't deform to avatar bodies outside Roblox. *(doc, high; avatar-ugc-accessories)*
- c5: glTF export supports cages, and Avatar auto setup output can be exported, finalized in a third-party tool, then reused. *(doc, medium; avatar-ugc-accessories)*
- c6: glTF export carries meshes, textures, and vertex colors; no explicit triangle, texture size, or UV limits are stated. *(doc, medium; mesh-texture-limits)*
- c7: Exportable assets: those uploaded directly to the user's or group's account, and meshes/images explicitly shared with them. *(doc, high; automation-and-creator-workflows)*
- c8: Not exportable: Avatar Marketplace assets, acquired Creator Store assets, collaborator-shared assets whose meshes/images are not explicitly shared, and public Open Use assets not shared with user or group. *(doc, high; automation-and-creator-workflows)*
- c9: Explorer export path: select items, right-click, Save / Export > Export as glTF, adjust components, Export, then Studio runs a permission check. Whole-place export is File > Export as glTF. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Supported components**: 6 types: meshes, textures, rigging/skinning, vertex colors, cages, dynamic head FACS data 

## Techniques
- t1: **Explorer glTF export**: Select items in Explorer, right-click, Save / Export > Export as glTF, tune components, click Export, resolve any permission prompt, choose save location.
- t2: **Whole-place glTF export**: File > Export as glTF, tune components, Export, resolve permission prompt, save .glTF file for external renders or editing.

## Quotes (brief, for attribution)
> This open standard format allows for efficient transfer of 3D assets and associated data between Studio and other software, such as Blender or Maya.  (create.roblox.com)
> Does not support animation data.  (create.roblox.com)

## Points to
- https://en.wikipedia.org/wiki/GlTF
- ../../avatar-setup/index.md#auto-setup
