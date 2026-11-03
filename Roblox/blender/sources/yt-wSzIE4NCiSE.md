---
type: research-source
id: yt-wSzIE4NCiSE
title: "How To Make a Fisch Style Map In Roblox Studio"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=wSzIE4NCiSE"
published: "2026-05-14"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1259
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# yt-wSzIE4NCiSE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial on building a Forge/Fisch-style low-poly map in Roblox Studio. Blender is used manually (no Claude/MCP/bpy) to model octagon ground pieces, bisected rocks, fences and lamp posts, exported as FBX and imported via Studio's importer with specific options. Most map work is in Studio with part scaling, Build V4 and ResizeAlign. Notes: separate meshes need separate objects, union meshes break after rejoining.

## Claims
- c1: [1:34] Base ground pieces: add cylinder with 8 vertices, delete top/bottom faces leaving one octagon face, duplicate and distort ~8 shapes by moving vertices (G), then extrude downward so they are 3D. Size is irrelevant since it can be rescaled in Studio. *(demo, high; blender-roblox-export-import)*
- c2: [2:55] Before export, enable backface culling to check normals; if faces look inside-out, select all in edit mode and use Alt+N > Recalculate Outside. *(demo, high; blender-roblox-export-import)*
- c3: [4:08] Low-poly rocks: take a UV sphere, scale it elongated, then use Knife > Bisect with Clear Inner/Outer and Fill to chop flat cuts repeatedly; check for missed curved spots before export. Six rocks were reused (scaled flatter) as pebbles. *(demo, high; mesh-texture-limits)*
- c4: [6:09] Exported as OBJ or FBX; the presenter prefers FBX since it always works for him and carries textures. An OBJ export merged everything into one mesh on import because objects were one group. *(experience, medium; blender-roblox-export-import)*
- c5: [6:41] In Studio's 3D importer, turn off 'Import as model' to get individually scalable meshes, and turn off upload to Roblox for local testing. Imported scale is huge, so scale the group down, then ungroup. *(demo, medium; blender-roblox-export-import)*
- c6: [8:02] All parts must be anchored or the map falls apart. Turn off cast shadow if undesired. Uncheck 'Use 2022 materials' style option in MaterialService to get original textures matching Fisch/Forge look. *(demo, medium; automation-and-creator-workflows)*
- c7: [8:26] Recoloring and Studio Material (Slate for rocks, Grass, Pebble for path) on plain untextured meshes gives the look; no UVs/textures needed from Blender. Only 2-3 shade variants per set. *(demo, medium; mesh-texture-limits)*
- c8: [12:13] Holding Alt while scaling in Studio scales from center. Setting move/scale increment to 0.5 studs avoids gaps. Build V4 (Creator Store) or F3X resizes each selected part individually, enabling grass top layers by duplicating, shrinking 0.5 and raising 0.5 studs. *(demo, medium; automation-and-creator-workflows)*
- c9: [21:45] Unioning the imported meshes into a path looked fine in Studio but broke in play test and after rejoining (turned into a clump); fix was to not union and instead resize overlapping parts at different heights. *(experience, medium; mesh-texture-limits)*
- c10: [24:30] Turn CanCollide off on bush parts so players walk through; place bushes away from walking routes. *(opinion, medium; automation-and-creator-workflows)*
- c11: [35:02] Ramp trails: angle a part 20-25 degrees (30 is steeper), duplicate and move with Ctrl+L, rotate on only one axis per segment, then align with ResizeAlign plugin (Outer Touch) which fails when multiple axes were rotated. *(demo, medium; automation-and-creator-workflows)*
- c12: [38:00] Fences: cylinder with 6 vertices (hexagon) rather than 8 for less detail; model one segment at a time and tile in Studio; use loop cuts (Ctrl+R) and offsets for variation; keep each fence as own object. *(demo, medium; blender-roblox-export-import)*
- c13: [41:24] Lamp post bevel: select edges manually (not all faces) and Ctrl+B; inset (I) and Alt+E extrude along normals for lantern detail. *(demo, medium; mesh-texture-limits)*
- c14: [46:11] To assign different Studio materials per piece, split a single Blender mesh by material role with P > Selection (wood, rope, lantern body, neon glass), then apply materials/Neon per part in Studio after import. *(demo, high; blender-roblox-export-import)*
- c15: [46:52] Lantern glow is faked with Neon material (orange); a true glow effect needs scripting/special textures per presenter. *(opinion, low; mesh-texture-limits)*
- c16: [3:00] No Claude, blender-mcp, or bpy usage appears; all Blender work is manual. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **ground piece vertices**: 8 (octagon) 
- n2: **fence post vertices**: 6 (hexagon) 
- n3: **Studio increment used**: 0.5 studs 
- n4: **trail slope angle**: 20-25 degrees (30 steeper) 
- n5: **assets imported in batch**: 14 meshes 

## Techniques
- t1: **Bisect rock**: UV sphere, scale elongated, edit mode, Knife > Bisect drag a cut line, Clear Outer (or Inner), Fill; repeat from different views until faceted.
- t2: **Fix inside-out faces**: Enable backface culling overlay, edit mode, select all, Alt+N > Recalculate Outside.
- t3: **Import separate meshes**: Export FBX with separate objects, Studio Import 3D, uncheck 'Import as model' and upload, import, scale down, ungroup, rename, anchor.
- t4: **Split mesh by material**: Edit mode, L-select linked piece, P > Selection; repeat per material role; import and assign Studio materials per part.
- t5: **Grass tops via duplicate**: Duplicate rock parts with Ctrl+D, use Build V4 resize to shrink 0.5 studs each, raise 0.5, recolor and set Grass material.
- t6: **Aligned slope trail**: Angled part, duplicate, rotate one axis only, then ResizeAlign Outer Touch to join faces.

## Contradictions flagged
- Union of imported meshes looks fine in Studio but collapses into a clump after rejoining/testing. (vs Common assumption that unions persist as seen in Studio)

## Points to
- Building Tools by F3X
- Build V4 by Bobby Blox
- ResizeAlign plugin
- GapFill plugin
- Low character (avatar) scale reference plugin
- Roblox Creator Store
