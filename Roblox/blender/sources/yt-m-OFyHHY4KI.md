---
type: research-source
id: yt-m-OFyHHY4KI
title: "Easily Create Driver Variables with Blender Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=m-OFyHHY4KI"
published: "2024-11-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-m-OFyHHY4KI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short bpy tutorial on creating Blender drivers from Python: add a driver to an icosphere's X location, add a variable, set its name, target an empty and its Z location path, and set expression to variable*0.5. Does not cover Roblox, Claude, blender-mcp, or export. Low relevance to the Roblox pipeline.

## Claims
- c1: [1:41] Driver on an object property can be added from bpy by calling driver_add on the icosphere's location with index 0 to target only X. *(demo, high; claude-blender-ai)*
- c2: [3:52] A driver's variables are created from Python by adding a new variable to the driver's variable list and getting a reference to it. *(demo, high; claude-blender-ai)*
- c3: [5:42] Variable targets are set by indexing the first target (index 0), assigning the empty as its ID, and setting the data path to the empty's Z location. *(demo, high; claude-blender-ai)*
- c4: [6:28] Driver expression is set as a string via the driver's expression property, here the variable multiplied by 0.5. *(demo, high; claude-blender-ai)*
- c5: [7:10] Moving the empty along Z in the viewport changes the icosphere's X location, confirming the driver works. *(demo, medium; claude-blender-ai)*
- c6: [0:00] Workflow tip: iterate by editing the script, running it, then deleting the scene to avoid duplicate objects. *(experience, medium; other)*

## Numbers
- n1: **expression multiplier**: 0.5 driver expression is variable * 0.5

## Techniques
- t1: **Python driver creation via driver_add**: Get object reference, call driver_add with property name and index (0 for X). Get driver from returned F-curve. Add variable via driver.variables.new(), set name, set targets[0].id to empty, set data_path, set driver.expression.
