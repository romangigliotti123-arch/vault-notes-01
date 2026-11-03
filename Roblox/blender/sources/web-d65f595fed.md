---
type: research-source
id: web-d65f595fed
title: "DevForum thread 1619788"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1619788"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 2
density: low
tags: ["research-source", "web", "rigging-animation", "roblox-export-settings", "roblox-import-pipeline"]
---
# web-d65f595fed

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short DevForum thread (2022) where a creator's FBX/OBJ model imported from Blender into Roblox loads wrongly, with bones not visible and animations not loading. Replies suggest exporting selected objects only as a single mesh, FBX scale 0.01, and OBJ scale 1.0. The OP says a 0.01 scale would break a chest lid animation. No Claude, blender-mcp, or bpy content.

## Claims
- c1: Suggested fix: FBX export scale set to 0.01 when importing into Roblox; OBJ export uses scale 1.0. *(opinion, medium; roblox-export-settings)*
- c2: Suggested fix: export only selected objects and ensure the model is a single mesh before importing to Roblox. *(opinion, medium; roblox-import-pipeline)*
- c3: OP reports bones not showing in Roblox Animation Editor and animations not loading after import, even though bones exist in Blender. *(experience, low; rigging-animation)*
- c4: OP says a 0.01 FBX scale would break a chest lid-opening animation, a trade-off with no resolution in thread. *(experience, low; roblox-export-settings)*

## Numbers
- n1: **FBX export scale**: 0.01 Colgobs' suggestion for FBX export into Roblox
- n2: **OBJ export scale**: 1.0 Colgobs' suggestion for OBJ export

## Techniques
- t1: **Export selected objects only as single mesh**: Select only the model's objects in Blender, join into one mesh, then export. Suggested by AstroStudioz as the fix for import problems.
- t2: **FBX scale 0.01 for Roblox**: When exporting FBX from Blender for Roblox, set the scale to 0.01. For OBJ, keep scale 1.0. Suggested by Colgobs.

## Quotes (brief, for attribution)
> if you mean scale when you export objects in fbx. you have to set the scale at 0.01  (devforum.roblox.com)
> then I would not be able to load the chest animation since it is the lid opening  (devforum.roblox.com)
