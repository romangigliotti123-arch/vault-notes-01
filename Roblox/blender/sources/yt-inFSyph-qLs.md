---
type: research-source
id: yt-inFSyph-qLs
title: "Integrated Design Workflows for Architectures — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=inFSyph-qLs"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-inFSyph-qLs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Architect's talk on Blender for architecture: geometry nodes for a paving pattern, a self-made add-on that re-imports updated FBX files while keeping materials, a photo-to-RAL color sampling add-on, and a work-in-progress photometric false-color tool. No Roblox, blender-mcp, bpy-to-Roblox export, or Claude content. Off-topic for this research.

## Claims
- c1: [4:26] Speaker wrote an add-on to import updated FBX files into an existing Blender scene, keeping materials and modifiers while geometry changes; saves re-import and material reassignment time. *(experience, medium; automation-and-creator-workflows)*
- c2: [14:31] Speaker built an add-on that samples colors from a photo and outputs RAL codes for real-world paint matching; work in progress. *(experience, low; other)*
- c3: [16:25] Work-in-progress photometric false-color tool; outputs a txt file of light levels, with Radiance as the referenced engine used by DIALux-type software. *(experience, low; other)*
- c4: [6:59] Paving pattern on a parallelogram base was solved with geometry nodes (row instances, surface definition, booleans, raycast material); the speaker says it is not ideal for animation meshes. *(experience, low; other)*
- c5: [3:46] Speaker's opinion: architecture suffers from too many handoffs between software (Revit, SketchUp, Rhino, ArchiCAD), causing knowledge loss; IFC is not fully integrated. *(opinion, low; other)*

## Numbers
- n1: **Years as architect**: since 1997 (speaker's statement) 
- n2: **Re-import add-on scope**: FBX in, materials modifier kept; no version numbers given 

## Techniques
- t1: **FBX re-import keeping materials**: Import updated FBX over existing scene objects so geometry updates while material assignments and modifiers persist, avoiding manual reassignment for each revision.

## Points to
- Dialux (named as a lighting-simulation tool, with Radiance engine)
- ArchiCAD
- Revit
- SketchUp
- Rhino/Grasshopper
- IFC
