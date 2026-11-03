---
type: research-source
id: off-studio_importer
title: "Roblox Creator Docs: studio_importer"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/studio/importer"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "other", "rigging-animation"]
---
# off-studio_importer

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio Importer doc: supported formats (.fbx/.gltf/.obj), import queue, presets, and per-file/object settings (Scale Unit default Studs, axes Front/Top, Rig Type R15/Custom/No Rig, Merge Meshes, Make Double Sided). Covers glTF vs FBX hierarchy differences and warning handling. No Blender-Claude, blender-mcp or bpy content.

## Claims
- c1: Studio Importer (File > Import) accepts .fbx, .gltf and .obj meshes; .fbx and .gltf support multiple meshes/hierarchies, PBR textures, cage meshes, rigs, avatar components, animation and vertex colors. *(doc, high; blender-roblox-export-import)*
- c2: Importer defaults: Scale Unit = Studs, World Forward = Front, World Up = Top; Import Only As Model enabled; Upload to Roblox enabled; Set Pivot to Scene Origin enabled. *(doc, high; blender-roblox-export-import)*
- c3: glTF imports nest each mesh primitive in an extra Model, whereas FBX places MeshPart directly under top-level Model; glTF cage nodes add extra Models you can delete. *(doc, high; blender-roblox-export-import)*
- c4: If a glTF node and its mesh share a name, the Importer appends _Node suffix to one of them (e.g. Cover_Node). *(doc, high; blender-roblox-export-import)*
- c5: Merge Meshes option (off by default) combines all MeshParts into one MeshPart instead of a Model; Invert Negative Faces (off) fixes inverted orientation. *(doc, high; blender-roblox-export-import)*
- c6: Rig Type options are R15, Custom, No Rig; default auto-detects from rig/skin data. Rig Scale (R15 only) offers Default, Rthro, Rthro Narrow. *(doc, high; rigging-animation)*
- c7: Keep Zero Influence Bones is off by default, so zero-weight bones are removed on import unless enabled. *(doc, high; rigging-animation)*
- c8: Validate UGC Body option opens imported avatar assets in Avatar Setup tool for testing and Marketplace upload. *(doc, high; avatar-ugc-accessories)*
- c9: Make Double Sided (off by default) renders faces on both sides but is more performance intensive; Ignore Vertex Colors is off by default. *(doc, high; mesh-texture-limits)*
- c10: Import queue supports bulk import with per-item presets (Studio Default, Last Imported), Apply settings to all, and Delete from queue; Upload to Roblox off enables testing without inventory copies. *(doc, high; automation-and-creator-workflows)*
- c11: Import as Package stores asset as a package (auto-updating, reusable); off by default. Open Cloud HTTP asset import is referenced as an alternative route. *(doc, high; automation-and-creator-workflows)*
- c12: Anchored is disabled by default and is forced off for rigged/avatar meshes; Set Pivot to Scene Origin is on by default. *(doc, medium; blender-roblox-export-import)*
- c13: Source does not mention Blender, blender-mcp, bpy, or Claude; it covers only Studio Importer settings, so it is thin for the Blender+Claude topic. *(doc, high; other)*

## Numbers
- n1: **Default Scale Unit**: Studs Importer file geometry setting, sizes model on import
- n2: **Default World Forward / World Up**: Front / Top Importer file transform defaults
- n3: **Rig Scale options**: Default, Rthro, Rthro Narrow Only when Rig Type is R15

## Techniques
- t1: **Preview and fix in Importer before import**: Open File > Import, pick .fbx/.gltf/.obj, check warnings in hierarchy/settings panel, adjust Scale Unit, axes, Merge Meshes, then Import.
- t2: **Batch import via queue with shared preset**: Add files to queue, set one item's settings, right-click Apply settings to all, save as preset, click Import.

## Quotes (brief, for attribution)
> Before importing a 3D object, ensure that the .fbx, .gltf or .obj meets Studio's mesh requirements to reduce errors or unexpected behavior.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/cloud/guides/usage-assets
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/art/blender
