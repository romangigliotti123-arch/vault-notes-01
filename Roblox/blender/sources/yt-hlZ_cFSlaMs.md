---
type: research-source
id: yt-hlZ_cFSlaMs
title: "Blender Python Tutorial: How to Use Geometry Nodes to Split and Animate Mesh Faces"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=hlZ_cFSlaMs"
published: "2023-04-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-hlZ_cFSlaMs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial (part 2) on building Geometry Nodes with bpy: a script adds Separate Geometry, Random Value (Boolean output) and Join Geometry nodes, refactors into functions, and keyframes scale with a Cycles F-curve modifier. Not about Roblox, Claude, blender-mcp, or the Roblox export pipeline.

## Claims
- c1: [1:54] Script sets the Geometry Nodes modifier active at the end so it shows without manual selection; done by setting modifier.is_active = True after the Solidify modifier is added. *(demo, high; claude-blender-ai)*
- c2: [8:47] Random Value node has one visible output in UI but four under the hood; the Boolean is output index 3, and sockets sharing names across data types need index or lookup by type. *(demo, high; claude-blender-ai)*
- c3: [5:53] Pattern: copy the last operator-generated command from the Info panel to get the bpy call, then reuse the node reference to shorten code. *(demo, medium; claude-blender-ai)*
- c4: [33:23] Keyframe loop helper sets value then inserts keyframes at start, mid (start + loop_length/2) and end frames; each node group uses a random start frame between 0 and 150 with loop length 90. *(demo, high; claude-blender-ai)*
- c5: [34:47] Seamless looping is added by applying a Cycles modifier to every F-curve in the node tree's animation data via the Graph Editor modifiers. *(demo, high; claude-blender-ai)*
- c6: [10:08] Windows-only: the Blender system console (Window > Toggle System Console) is needed to see print output; the author says Mac and Linux need other setups. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **Random Value output index**: 3 (Boolean) Random Value node exposes four outputs; index 3 is Boolean
- n2: **Random start frame range / loop length**: 0-150 / 90 frames Per-node keyframe loop start offset and cycle length
- n3: **Node Y offsets**: 200 / -200 Top and bottom Scale Elements nodes placed in one column

## Techniques
- t1: **Activate modifier from script**: Get the object, find modifier by type GEOMETRY_NODES, set is_active=True after adding the last modifier, so it is visible on each run.
- t2: **Socket lookup by type**: Iterate node.outputs, build dict of socket.type to socket, pick the Boolean socket by type rather than by name or index.
- t3: **Keyframe loop helper**: Set property to start value, keyframe at start frame; set mid value, keyframe at start+length/2; set end value, keyframe at start+length; then add Cycles F-curve modifier.

## Quotes (brief, for attribution)
> for each one of these data types this socket this value socket is going to have the same name this is very unfortunate  (at 8:47, CG Python)

## Points to
- CG Python channel (Victor Stepanoff)
- Blender Python API documentation
