---
type: research-source
id: web-df8d902e57
title: "Roblox docs: art/blender"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/blender.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0989
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# web-df8d902e57

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on Blender setup for Studio: set Blender units to None/degrees, axis settings for import/export between Blender (Z-up) and Studio (Y-up), FBX scale fixes (FBX Unit Scale recommended; glTF needs none), Studio importer options, plus Blender UI/modeling/UV tool overviews. No Claude/MCP/bpy content. Truncated before the end of texturing section.

## Claims
- c1: Set Blender Scene > Units > Unit System to None and Rotation to Degrees so measurements are consistent with studs. *(doc, high; roblox-export-settings)*
- c2: Blender uses Z-up; Studio uses Y-up. Import/export axis settings must be adjusted to preserve orientation. *(doc, high; roblox-export-settings)*
- c3: Blender export: enable Limit to Selected Objects; for FBX set Apply Scalings to FBX Unit Scale; Forward Z Forward; Up Y Up. *(doc, high; roblox-export-settings)*
- c4: Default Blender FBX export often imports unexpectedly large in Studio. glTF does not require the extra scaling configuration. *(doc, high; roblox-export-settings)*
- c5: FBX Unit Scale is the recommended FBX scale method; keep all other scale values at 1.0. Alternatives: export Scale 0.01, or Scene Unit Scale 0.01. *(doc, high; roblox-export-settings)*
- c6: Working at 0.01 scene unit scale can cause camera difficulties and modifier issues in Blender; re-importing 0.01-exported models into Blender may come in tiny. *(doc, high; common-mistakes-fixes)*
- c7: Studio importer settings: Import Only as a Model groups multiple objects into a Model; Upload to Roblox creates an asset ID; Creator Me or group; Insert Using Scene Position keeps Blender position. *(doc, high; roblox-import-pipeline)*
- c8: Studio import File Transform: World Forward = Front, World Up = Top; File Geometry: Scale Unit = Stud. *(doc, high; roblox-import-pipeline)*
- c9: Studio to Blender import (obj/fbx/gltf): Scale 1, Forward Axis Z, Up Axis Y to keep Studio orientation. *(doc, high; roblox-import-pipeline)*
- c10: Avatar items (rigid accessories, layered accessories, character bodies) require their own specs and export settings, separate from generic export settings. *(doc, high; avatar-ugc-accessories)*
- c11: Sharing one UV map/trim sheet across multiple meshes (e.g. Laser Tag doorway, ceiling, card reader) adds visual complexity without extra textures, saving memory. *(doc, medium; texturing-baking-uv)*
- c12: Mark seams with Ctrl+E > Mark Seam in the UV Editing workspace to unwrap related face groups as separate islands, e.g. leather grip vs metal barrel. *(doc, medium; texturing-baking-uv)*
- c13: Reference files, demos and tutorials may use older or inconsistent scale settings; test and validate external resources against your current export workflow. *(doc, medium; common-mistakes-fixes)*
- c14: Fill and New Faces from Edges are used to close holes so meshes are watertight; Mirror modifier for symmetrical avatars/architecture; Dissolve to optimise without holes. *(doc, medium; creator-workflows)*

## Numbers
- n1: **FBX export Scale workaround**: 0.01 Transform > Scale so FBX imports at expected size in Studio
- n2: **Scene Unit Scale workaround**: 0.01 Alternative scene-wide scaling; may cause Blender camera/modifier issues
- n3: **Blender import Scale**: 1 When importing Studio objects into Blender

## Techniques
- t1: **Blender FBX export for Studio**: File > Export > FBX; enable Limit to Selected Objects; Transform: Apply Scalings = FBX Unit Scale, Forward = Z Forward, Up = Y Up; other scales at 1.0.
- t2: **Studio import of Blender object**: File > Import; pick file; enable Insert Using Scene Position; World Forward Front, World Up Top; Scale Unit Stud; optionally Import Only as a Model and Upload to Roblox; set Creator; Import.
- t3: **Use glTF to avoid FBX scale issues**: Export .gltf/.glb from Blender; Studio supports it without additional scaling configuration.

## Contradictions flagged
- Doc says set Blender Unit System to None for stud compatibility, while FBX path needs FBX Unit Scale or 0.01 scaling because default FBX imports too large. (vs Assumption that units=None alone gives correct FBX scale in Studio)

## Points to
- https://www.blender.org/download/
- Roblox rigid accessory export docs (avatar/rigid-accessories/export)
- Roblox layered accessory export docs (avatar/layered-accessories/export)
- Roblox avatar character-bodies export docs
- Environmental art curriculum: trim sheets
- Laser Tag template
