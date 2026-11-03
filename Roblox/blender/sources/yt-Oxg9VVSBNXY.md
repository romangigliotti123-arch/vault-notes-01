---
type: research-source
id: yt-Oxg9VVSBNXY
title: "How To Make a Tree In Roblox Studio"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=Oxg9VVSBNXY"
published: "2026-05-19"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0621
relevance: 2
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# yt-Oxg9VVSBNXY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Manual tutorial for building three Roblox trees (parts-only stud tree, Blender low-poly tree, detailed swamp tree). No Claude/MCP/bpy content. Pipeline bits: model in Blender with cube extrusion, split parts with P selection, export FBX, import via Studio importer with options unchecked, rescale, ungroup, set Material and color, group and anchor.

## Claims
- c1: [9:22] Creator exports from Blender as FBX because they find it easiest, then imports in Studio with both import checkboxes unchecked. *(demo, medium; blender-roblox-export-import)*
- c2: [9:22] Imported FBX arrives far too large; select the whole thing and scale it down in Studio. *(demo, high; blender-roblox-export-import)*
- c3: [9:22] Import comes in as a Model; right-click and Ungroup to get a single MeshPart. Material (Wood) and color are then set in Studio. *(demo, high; blender-roblox-export-import)*
- c4: [9:22] A single combined mesh with separate sections caused invisible surfaces/wall between sections when walked on in Studio, per the creator's test. Fine for small trees; for large walkable trees use separate parts. *(demo, medium; mesh-texture-limits)*
- c5: [12:38] For a big walkable tree, keep pieces as separate meshes rather than one merged mesh because of the invisible-surface collision problem. *(experience, medium; mesh-texture-limits)*
- c6: [9:22] Splitting a combined mesh into separate objects: Edit Mode, hover and press L to select linked, then P > Selection. Needed if leaves are modeled in Blender so each can be colored individually. *(demo, high; blender-roblox-export-import)*
- c7: [8:41] Leaves are better done in Studio with colored parts because each leaf cluster has a different color; trunk and branches done in Blender. *(opinion, medium; automation-and-creator-workflows)*
- c8: [11:25] After placement, trees may float above ground; sink them slightly into the ground. Group and anchor everything. *(experience, high; automation-and-creator-workflows)*
- c9: [4:35] Trees can be built entirely from scaled Parts in Studio; Blender is used only because scaling and manipulating is easier. *(opinion, high; automation-and-creator-workflows)*
- c10: [1:03] The Resize Align plugin is recommended to align faces of angled parts and close gaps when building with parts. *(opinion, medium; automation-and-creator-workflows)*
- c11: [20:52] Vines are 1.2 x 1.2 stud grass-material parts of varied lengths, duplicated around the leaves. *(demo, high; automation-and-creator-workflows)*
- c12: [17:24] Keep root base fairly flat and shallow since the underside goes underground and is invisible; roots may curve back up if they go too deep. *(experience, medium; mesh-texture-limits)*

## Numbers
- n1: **stud tree trunk part size**: 1x1 studs scaled to ~6-7 studs; branch ~3 studs simple stud tree
- n2: **vine part size**: 1.2 x 1.2 studs swamp tree vines
- n3: **tree tilt**: 5 degrees rotation applied to swamp tree after placing

## Techniques
- t1: **Blender tree trunk by extrusion**: Add cube, Edit Mode, S Z to set height. Shift D duplicate, scale Y, move faces to form tapered pieces; Shift E duplicate faces, scale, rotate, E extrude outward to make branches. Press Z then wireframe to see through.
- t2: **Radial duplication of base**: Select pieces with L, top view, Shift D, R 180 and move to the other side; repeat with R 90 to form four-sided trunk base.
- t3: **FBX to Studio import**: Export FBX from Blender. In Studio Import, uncheck both options, import, scale down, Ungroup, then set Material and Color.
- t4: **Separate parts via P selection**: In Edit Mode hover piece, L to select linked, P > Selection to split into own object so it imports as separate part.
- t5: **Rotated leaf layering**: Spawn Parts for leaves, rotate slightly off-axis to follow branches, make middle larger, thin out toward branch tips, then recolor sets of leaves in darker/brighter greens.

## Points to
- Resize Align plugin (Roblox Studio)
- Kingkade 3D channel membership asset pack
