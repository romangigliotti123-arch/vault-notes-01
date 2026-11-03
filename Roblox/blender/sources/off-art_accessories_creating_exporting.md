---
type: research-source
id: off-art_accessories_creating_exporting
title: "Roblox Creator Docs: art_accessories_creating_exporting"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/accessories/creating/exporting"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# off-art_accessories_creating_exporting

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on exporting clothing/accessory meshes from Blender to Studio-compatible FBX. Lists required FBX export settings: selected objects only, Path Mode Copy with Embed Textures, Apply Scalings set to FBX Unit Scale, Add Leaf Bones disabled, Bake Animation disabled. Says to remove lights/cameras/mannequins and apply or remove modifiers first. Does not cover blender-mcp or bpy scripting.

## Claims
- c1: Blender FBX export for Studio-compatible clothing: Include 'Selected Objects' enabled, after selecting all unhidden objects in Outliner. *(doc, high; blender-roblox-export-import)*
- c2: Set FBX export Path Mode to Copy and enable Embed Textures. *(doc, high; blender-roblox-export-import)*
- c3: Transform > Apply Scalings set to FBX Unit Scale; if scaling issues occur, use the alternative approaches in the Blender FBX scaling doc. *(doc, high; blender-roblox-export-import)*
- c4: Disable 'Add Leaf Bones' in the Armature section and disable 'Bake Animation' for accessory export. *(doc, high; rigging-animation)*
- c5: Remove extra objects (lights, cameras, mannequins) and apply or remove active modifiers before export. *(doc, high; blender-roblox-export-import)*
- c6: Accessory export is a step in a sequence: modify-cage, then exporting, then importing. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Clothing FBX export checklist**: 1. Unhide all objects and make selectable in Outliner. 2. Select all. 3. File > Export > FBX. 4. Path Mode Copy, toggle Embed Textures. 5. Include Selected Objects. 6. Apply Scalings: FBX Unit Scale. 7. Disable Add Leaf Bones. 8. Disable Bake Animation. 9. Export FBX.

## Quotes (brief, for attribution)
> It's important to follow the Blender export settings to ensure a Studio-compatible .fbx file.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender.md (Blender FBX scaling section)
- https://create.roblox.com/docs/art/accessories/creating/modify-cage
- https://create.roblox.com/docs/art/accessories/creating/importing
