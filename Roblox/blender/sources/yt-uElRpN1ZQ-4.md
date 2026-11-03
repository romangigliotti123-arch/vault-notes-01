---
type: research-source
id: yt-uElRpN1ZQ-4
title: "How to not hate editing your 3D models on Roblox"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=uElRpN1ZQ-4"
published: "2026-06-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 3
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "rigging-animation"]
---
# yt-uElRpN1ZQ-4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators video (Frank, Studio import engineer) demoing Studio's new re-import feature for 3D models: import a door mesh, set up scale/colors/welds/anchor/hinge, then edit in Blender and re-import in place so constraints and colors persist. Covers right-click > Re-import > Configure, file path update, and hotkey Alt+Shift+R. Nothing on blender-mcp, bpy, or Claude.

## Claims
- c1: [1:47] Re-import updates an already-imported Studio model in place from an edited external file, keeping colors and constraints (welds, hinge) on unchanged parts. *(demo, high; blender-roblox-export-import)*
- c2: [2:23] Re-import workflow: right-click model, Re-import submenu, Configure, update file path to new export, then Save and Re-import. *(demo, high; blender-roblox-export-import)*
- c3: [3:44] Re-import configuration is set automatically on every 3D model import and persists with the model across Studio sessions. *(doc, medium; blender-roblox-export-import)*
- c4: [3:44] Default re-import hotkey is Alt+Shift+R. *(demo, high; automation-and-creator-workflows)*
- c5: [3:04] New mesh parts added in Blender (window panes) need manual setup after re-import: set material to glass and weld to the door. *(demo, medium; blender-roblox-export-import)*
- c6: [0:33] Physical setup for a door in Studio required welding handle to door, anchoring wall, and adding a hinge constraint between door and wall so it swings. *(demo, medium; rigging-animation)*
- c7: [1:47] Without re-import, an updated Blender export must be imported as a new model and all Studio setup (scale, colors, constraints) redone. *(opinion, medium; blender-roblox-export-import)*

## Numbers
- n1: **Re-import hotkey**: Alt+Shift+R (default) Re-imports the model without using the menu
- n2: **Window holes in door**: 4 Four windows punched into top half of door in Blender

## Techniques
- t1: **In-place re-import**: Edit mesh in Blender, export, then in Studio right-click model > Re-import > Configure, set file path to new export, Save and Re-import. Constraints and colors on existing parts survive.
- t2: **Hotkey re-import**: After first configuration, press Alt+Shift+R to re-import the model from the saved path after each Blender export.

## Quotes (brief, for attribution)
> Notice how re-import updated only the parts of the model that needed to be updated.  (at 2:23, Roblox Creators)
> those changes are saved with the model and will persist across Studio sessions.  (at 3:44, Roblox Creators)
