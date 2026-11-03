---
type: research-source
id: yt-Sw7BLJHYYAU
title: "Winter of Quality - Blender Today LIVE #253"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=Sw7BLJHYYAU"
published: "2025-02-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0055
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-Sw7BLJHYYAU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today #253 (Feb 4, 2025) covers Blender 4.4 pre-release changes from the Winter of Quality stability push. It does not discuss Claude, blender-mcp, bpy automation for Roblox, or Roblox export. Only tangential items: glTF exporter pre/post Python hooks, a Python API file path map, and a blend-to-JSON debugging tool.

## Claims
- c1: Blender 4.4 glTF exporter gained pre- and post-export Python hooks, so user Python can run before and after glTF export. *(doc, high; automation-and-creator-workflows)*
- c2: glTF collection exporter now maps collection custom properties to glTF scene extras, since the scene contains only that collection's objects. *(doc, high; automation-and-creator-workflows)*
- c3: glTF exporter now falls back to linear interpolation when no interpolation option is selected; output directory is created if missing. *(doc, medium; automation-and-creator-workflows)*
- c4: Python API gained a file path map similar to bpy.data user map. *(doc, medium; automation-and-creator-workflows)*
- c5: Blend-to-JSON tool exists as a developer aid giving a non-one-to-one JSON view of .blend files; not for production use. *(opinion, medium; other)*
- c6: Winter of Quality report: normal-severity reports dropped (modeling -45, notes/physics -153, VFX/video -183, UI -173 versus earlier counts); about 20s high-priority bugs open. *(data, medium; other)*
- c7: Blender 4.4 beta was scheduled for Feb 5, 2025 and 4.5 alpha the same day; 4.4 is a stability-focused release. *(doc, high; other)*

## Numbers
- n1: **glTF exporter hooks**: pre + post export Python hooks 
- n2: **Normal-severity report reduction (UI)**: 173 fewer 
- n3: **Normal-severity report reduction (notes/physics)**: 153 fewer 
- n4: **Commits since prior episode**: 564 

## Points to
- blender.org developer chat
- Blender Studio
- Translate blender.org
