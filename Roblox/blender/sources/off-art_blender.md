---
type: research-source
id: off-art_blender
title: "Roblox Creator Docs: art_blender"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/blender"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0046
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# off-art_blender

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on Blender for Studio. Covers unit setup (Scene > Units: None, Degrees), import/export axis settings (Z forward, Y up in Blender; World Up Top/Front in Studio), Scale Unit Stud, FBX scale fixes (FBX Unit Scale, Scale .01, Unit Scale .01), and workspaces/modes/modeling tools. No MCP, bpy, or plugin content in the visible text.

## Claims
- c1: Blender Scene Units must be set to Unit System None and Rotation Degrees to match Studio studs. *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX export should set Apply Scalings to FBX Unit Scale; docs call this the recommended way to keep scale in Studio, with other scale values left at 1.0. *(doc, high; blender-roblox-export-import)*
- c3: Alternative FBX fixes: export Scale .01, or set Scene Units Unit Scale .01; both noted to cause import-back issues in Blender. *(doc, medium; blender-roblox-export-import)*
- c4: Roblox Studio supports glTF which does not require the FBX scaling workarounds. *(doc, high; blender-roblox-export-import)*
- c5: Blender export: Forward Z Forward, Up Y Up; Limit to Selected Objects enabled. *(doc, high; blender-roblox-export-import)*
- c6: Studio import from Blender: World Forward Front, World Up Top, Scale Unit Stud, Insert Using Scene Position enabled. *(doc, high; blender-roblox-export-import)*
- c7: Blender import of Studio files: Scale 1, Forward Z, Up Y. *(doc, high; blender-roblox-export-import)*
- c8: Avatar items and specialized components require separate export settings; docs link rigid accessories, layered accessories, and avatar character pages. *(doc, high; avatar-ugc-accessories)*
- c9: UV islands shared across objects (trim sheets) add visual detail without extra textures, saving memory. *(doc, medium; mesh-texture-limits)*
- c10: Page does not mention blender-mcp, MCP, bpy, or Claude integration. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Blender FBX Scale export value (alternative)**: .01 
- n2: **Studio import Scale Unit**: Stud 
- n3: **Default scale value for matching Studio**: 1 

## Techniques
- t1: **Set units for studs**: Properties > Scene > Units: Unit System None, Rotation Degrees. Then export/import with matching axes and scale.
- t2: **FBX Unit Scale export**: Export FBX with Transform > Apply Scalings = FBX Unit Scale, all other scale values at 1.0, Forward Z, Up Y.
- t3: **Trim sheet UV reuse**: Unwrap many objects onto one shared trim-sheet texture in UV Editing workspace to reduce texture memory.

## Quotes (brief, for attribution)
> Models exported with this setting import into Studio or back into Blender at the same scale.  (create.roblox.com)
> Roblox Studio also supports GLTF formats which do not require these additional scaling configurations.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://www.blender.org/download/
- https://create.roblox.com/docs/physics/units
