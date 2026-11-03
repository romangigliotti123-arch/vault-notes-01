---
type: research-source
id: web-92feb49cd5
title: "Roblox docs: art/accessories/creating/exporting"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/exporting.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 3
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-export-settings"]
---
# web-92feb49cd5

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on exporting clothing/accessory meshes from Blender as FBX for Studio compatibility. Lists export steps: select all, Path Mode Copy, Embed Textures, Selected Objects, Apply Scalings = FBX Unit Scale, disable Add Leaf Bones and Bake Animation. Says remove lights/cameras/mannequins and apply modifiers first. No Claude, blender-mcp or bpy content.

## Claims
- c1: Blender FBX export for Studio: Apply Scalings set to FBX Unit Scale; Path Mode Copy with Embed Textures enabled. *(doc, high; roblox-export-settings)*
- c2: Disable Add Leaf Bones and Bake Animation in the FBX armature/animation export options for clothing assets. *(doc, high; roblox-export-settings)*
- c3: Remove extra objects (lights, cameras, mannequins) and apply or remove active modifiers before exporting. *(doc, high; common-mistakes-fixes)*
- c4: If scaling issues occur on FBX import, the docs point to an alternative approach in the Blender scaling section. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **Apply Scalings**: FBX Unit Scale 
- n2: **Path Mode**: Copy 

## Techniques
- t1: **Blender FBX export for clothing**: Unhide all, select all, File > Export > FBX. Path Mode Copy, Embed Textures on, Selected Objects only, Apply Scalings FBX Unit Scale, Add Leaf Bones off, Bake Animation off, Export FBX.

## Quotes (brief, for attribution)
> It's important to follow the Blender export settings to ensure a Studio-compatible .fbx file.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender (Blender FBX scaling section)
- Long_Sleeve_Export.fbx reference sample
