---
type: research-source
id: yt-lcT0ARV6dCk
title: "3D Truchet Tile with Python in Blender (Step-by-Step)"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=lcT0ARV6dCk"
published: "2023-05-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "rigging-animation"]
---
# yt-lcT0ARV6dCk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Victor Stepanoff's Blender Python tutorial builds a looping 3D Truchet tile animation with bpy: arc curve via Extra Objects, extrude/solidify/convert to mesh, duplicate and join tiles, collection instances in a grid, keyframed tile rotation, and linear camera loop. Relevant only as bpy scripting technique; no Roblox export, no MCP, no Claude content.

## Claims
- c1: [0:00] Tutorial is a Blender Python (bpy) procedural workflow: paste helper code into Scripting workspace, run, then build in create_centerpiece function. Not about blender-mcp or Claude. *(demo, high; claude-blender-ai)*
- c2: [2:05] Arc curve created via Extra Objects add-on, end angle set to 290 degrees, then converted to mesh via copying Info panel commands into script. *(demo, high; claude-blender-ai)*
- c3: [3:28] Workflow pattern: perform each action by hand, copy generated bpy commands from Info panel into script, then clean up (extrude 0.15, solidify thickness 0.1 offset 0, shade smooth, auto smooth, origin to cursor). *(demo, high; claude-blender-ai)*
- c4: [6:05] Helper functions used to duplicate objects and apply materials; tile duplicated and rotated 180 degrees about Z. *(demo, medium; claude-blender-ai)*
- c5: [11:06] Animation of tile: keyframe Euler Z rotation with pauses; rotate 90 degrees, hold, rotate back, using keyframe insertion via script. *(demo, medium; rigging-animation)*
- c6: [16:35] Grid built with nested for loops over X and Y steps; collection instances (collection instance_add) placed at computed locations; Y reset each X iteration. *(demo, medium; automation-and-creator-workflows)*
- c7: [24:06] Camera keyframed at frame 1 and last frame, moved two section steps, linear interpolation; last frame is frame count +1 so loops join without duplicated frame stutter. *(demo, high; rigging-animation)*
- c8: [27:04] Author moved helper functions into a separate Python package installable via pip or Blender add-on, reducing script to imports; not Roblox-specific. *(demo, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Arc end angle**: 290 degrees 
- n2: **Extrude / solidify**: 0.15 extrude, 0.1 thickness, 0 offset 
- n3: **Tile rotation step**: 90 degrees 
- n4: **Duplicate rotation**: 180 degrees about Z 

## Techniques
- t1: **Record-then-copy bpy workflow**: Perform action manually in Blender, copy generated commands from Info panel into script, indent into function, remove redundant lines, rerun.
- t2: **Nested-loop collection instancing**: Loop X and Y, reset Y each X iteration, create collection instance at computed location, then group instances into a collection and instance again for a macro grid.
- t3: **Seamless loop camera**: Keyframe camera at frame 1 and frame_count+1, linear interpolation, end location equals start after two steps.

## Quotes (brief, for attribution)
> you can get this python package via pip or a blender add-on  (at 27:04, CG Python)

## Points to
- Visual Studio Code for Blender Python tutorial (author's separate video)
- Extra Objects add-on (arc curve)
