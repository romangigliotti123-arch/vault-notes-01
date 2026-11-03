---
type: research-source
id: yt-yvTTxxUKA6c
title: "From Vertex to T. Rex: 3D Printing My Own Hall of Dinosaurs — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=yvTTxxUKA6c"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0043
relevance: 1
density: low
tags: ["research-source", "youtube", "blender-roblox-export-import", "other"]
---
# yt-yvTTxxUKA6c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Talk by a paleo-art professor on 3D printing life-size dinosaur skeletons (T-Rex, Utah raptor, Triceratops) from Blender models. Off-topic for Roblox and Claude/MCP workflows. Only usable material: Blender scale-vs-print units, sculpt/3D-print-toolbox tips, and printing parameters. No blender-mcp, bpy, Roblox import, or Open Cloud content.

## Claims
- c1: [15:16] Speaker says one meter in Blender equals one millimeter on most 3D printers, so models must be built at large scale. Experience-based; no Roblox relevance stated. *(experience, medium; blender-roblox-export-import)*
- c2: [14:31] For 3D printing, the speaker says models must be manifold with normals pointing outward; inside-out normals print badly. Topology matters far less than for animation. *(opinion, medium; other)*
- c3: [14:31] Dyntopo checkbox in sculpt mode lets you start low-poly and sculpt into higher poly; speaker says topology is poor but acceptable for printing. *(experience, medium; other)*
- c4: [14:31] Speaker says the 3D Print Toolbox add-on helped with model problems, but in the closing ask he could not get it to make magnetic-mated bone surfaces close. *(experience, medium; other)*
- c5: [13:22] Adjust the viewport clipping distance in Blender to see very large models. *(experience, low; other)*
- c6: [1:28] Sectioned a digital T-Rex skull by limiting camera clip distance and rendering successive slices, then sent slices to a CNC foam cutter. Lost detail; hand-resculpted afterward. *(experience, medium; other)*
- c7: [15:16] Prints in ABS rather than PLA, needs an enclosed heated chamber and ventilation. Supports are dissolved in acetone to paint-able consistency, letting seams be solvent-welded. *(experience, medium; other)*
- c8: [8:55] Planned the Utah raptor by building holes into T-Rex bone models for quarter-inch armature wire; bolts and welds used where steel rigidity was needed. *(experience, low; other)*
- c9: [10:02] Triceratops base model was a CC0 3D scan from the Smithsonian website, scaled in Blender; a dovetail split was designed for doorway transport. *(experience, medium; other)*

## Numbers
- n1: **Blender unit to print scale**: 1 m in Blender = 1 mm printed 
- n2: **T-Rex print filament**: ~110 kg 
- n3: **Utah raptor print filament**: ~10 kg 
- n4: **T-Rex printer hours**: 5,480 h 
- n5: **Utah raptor printer hours**: ~1,776 h 
- n6: **Triceratops filament**: ~60 kg, 1,776 printer hours 
- n7: **Printer build volume (GDX Max 3)**: 310 x 315 mm 
- n8: **Skull infill**: ~10% 
- n9: **Long bone infill (femur/tibia)**: 5% 
- n10: **Filament roll size and price**: 5 kg rolls, ~$100 each 

## Techniques
- t1: **Blender clip-distance slicing**: Limit camera clip distance, render successive slices of the model, deliver slices to a CNC cutter. Speaker calls this 'probably a better way'.
- t2: **Dyntopo sculpt-to-print**: Start from low-poly, enable Dyntopo in sculpt mode, sculpt detail in. Ensure manifold mesh with outward normals before printing.
- t3: **Solvent-weld ABS assembly**: Dissolve support material in acetone to roughly glue consistency, join parts, paint over seams to hide them.

## Quotes (brief, for attribution)
> one meter in Blender is equal to one millimeter on most 3D printers. So, you got to make things huge.  (at 15:16, Blender)

## Points to
- Blender Conference (speaker presented T-Rex work)
- Smithsonian 3D scan (CC0, Triceratops)
- Andrew Price newsletter
- 3D Print Toolbox (Blender add-on)
