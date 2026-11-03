---
type: research-source
id: web-3e931d23cf
title: "Blender manual: files/import_export/fbx"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/files/import_export/fbx.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "rigging-animation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# web-3e931d23cf

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page for the FBX importer. Lists import options: Scale, Custom Properties, Vertex Colors (None/sRGB/Linear), Material Name Collision, Animation Offset, Ignore Leaf Bones. Each FBX take becomes a separate Action. Export is delegated to the FBX add-on. Generic reference; no Roblox-specific guidance.

## Claims
- c1: Blender FBX importer has a Scale option that scales imported objects relative to world origin; no Roblox-specific value is given. *(doc, high; roblox-import-pipeline)*
- c2: Ignore Leaf Bones drops the last bone in each chain, which the page says is only used to mark the length of the previous bone. *(doc, high; rigging-animation)*
- c3: Each FBX take is imported as a separate Action, with each animated object assigned to its own Action Slot. *(doc, high; rigging-animation)*
- c4: Vertex Colors import has three modes: None, sRGB, or Linear, depending on the colour space stored in the file. *(doc, high; texturing-baking-uv)*
- c5: Material Name Collision can either make each imported material unique or reference an existing same-named material instead of importing. *(doc, high; common-mistakes-fixes)*
- c6: FBX export is handled by a separate FBX Add-on, referenced from the manual but not described on this page. *(doc, medium; roblox-export-settings)*

## Points to
- https://docs.blender.org/manual/en/latest/files/custom_properties.html
- https://docs.blender.org/manual/en/latest/animation/actions.html
