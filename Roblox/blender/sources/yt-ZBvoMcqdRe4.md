---
type: research-source
id: yt-ZBvoMcqdRe4
title: "Blender Python: How to manipulate the Sky Texture from a script"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=ZBvoMcqdRe4"
published: "2023-05-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-ZBvoMcqdRe4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short bpy tutorial on scripting Blender's World shader. It clears the world node tree, creates Sky Texture, Background and World Output nodes, positions and links them, and sets inputs by name. Sun rotation uses math.radians. A config dict is applied with setattr, and random rotation is added. Nothing on Roblox, MCP, or export.

## Claims
- c1: [0:00] Video is a generic bpy scripting tutorial for World shader sky texture; no Claude, blender-mcp, or Roblox content. *(doc, high; claude-blender-ai)*
- c2: [2:12] Clearing world nodes via the world node_tree nodes clear removes all world shader nodes before rebuilding. *(demo, medium; claude-blender-ai)*
- c3: [3:00] Three nodes are created in the world node tree: Sky Texture, Background, World Output. *(demo, high; claude-blender-ai)*
- c4: [5:41] Sky Texture Color links to Background Color; Background output links to World Output Surface, producing lighting. *(demo, high; claude-blender-ai)*
- c5: [7:10] Input sockets can be addressed by name (e.g. 'Strength') rather than index; index 0 is Color, index 1 is Strength. *(demo, high; claude-blender-ai)*
- c6: [8:51] Sun rotation is stored in radians, so degrees are converted with math.radians (33 degrees example). *(demo, high; claude-blender-ai)*
- c7: [10:42] Config dict pattern: loop over dict items and setattr on the sky node if hasattr is true; otherwise warn about missing attribute. *(demo, medium; claude-blender-ai)*
- c8: [13:31] Random sun rotation generated per run via random value 0-360 degrees converted to radians into the config dict. *(demo, medium; claude-blender-ai)*
- c9: [14:20] Presenter notes the viewport was in Eevee and switched to Cycles to see the sky lighting. *(experience, low; claude-blender-ai)*

## Numbers
- n1: **video length**: 14:59 
- n2: **random sun rotation range**: 0-360 degrees 
- n3: **example sun rotation**: 33 degrees 

## Techniques
- t1: **Build world nodes via bpy**: Get scene.world.node_tree, clear nodes, nodes.new Sky Texture/Background/World Output, set node.location, links.new to connect outputs to inputs.
- t2: **Dict-driven node settings**: Pass a dict of attribute names to a function; for each key that hasattr on the sky node, setattr the value; warn on unknown keys.

## Points to
- Blender Python API documentation (node reference), linked in video description
