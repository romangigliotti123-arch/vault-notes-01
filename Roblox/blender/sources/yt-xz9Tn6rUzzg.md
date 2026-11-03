---
type: research-source
id: yt-xz9Tn6rUzzg
title: "How to apply HDRIs with a Blender Python script"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=xz9Tn6rUzzg"
published: "2024-05-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-xz9Tn6rUzzg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video (Victor Stenov, CG Python) walks through a bpy script that clears the World shader node tree, builds an Environment Texture to Background to World Output chain for an HDRI, sets node X locations, and renders one PNG per HDRI in a folder. Relevant only to the bpy scripting part of the topic; nothing on Roblox export, Claude, or MCP.

## Claims
- c1: [0:26] Source recommends polyhaven.com as HDRI source; put files in a home-folder 'hdris' directory. *(opinion, high; other)*
- c2: [1:37] Script starts with import bpy; world node tree is reached via context scene world, then node list cleared to build from scratch. *(demo, high; claude-blender-ai)*
- c3: [3:27] pathlib.Path(home) used for cross-platform paths (Mac, Linux, Windows); image loaded via bpy.data.images.load. *(demo, medium; claude-blender-ai)*
- c4: [4:01] Environment texture node created with nodes.new using its internal type name, then image assigned to its image property. *(demo, high; claude-blender-ai)*
- c5: [5:29] Nodes stack on top of each other by default; script sets node location.x, incrementing a location_x variable by 300 per node. *(demo, high; claude-blender-ai)*
- c6: [7:57] Links created with node_tree.links.new from Environment Texture Color output to Background Color input, then Background to World Output Surface. *(demo, high; claude-blender-ai)*
- c7: [9:20] Render triggered from script with bpy.ops.render.render(write_still=True) after setting scene output file path. *(demo, medium; claude-blender-ai)*
- c8: [10:43] Unique output names built from datetime timestamp (hour, minute, second) to avoid overwriting renders. *(demo, high; automation-and-creator-workflows)*
- c9: [12:15] Output format must be set to PNG in render settings to match script's output name; script renders are saved to a renders folder. *(demo, medium; claude-blender-ai)*
- c10: [12:55] Refactor into apply_hdri, render_image and main functions; apply_hdri takes a path parameter. *(demo, high; automation-and-creator-workflows)*
- c11: [15:15] Batch mode: iterate hdris folder with iterdir(), apply each HDRI and render; convert Path to str before passing to Blender image loading. *(demo, high; automation-and-creator-workflows)*
- c12: [15:56] Running the script in the Blender Text Editor (Run Script) renders one image per HDRI in the folder; no Claude or MCP involved. *(demo, medium; claude-blender-ai)*

## Numbers
- n1: **node X offset**: 300 units per node 
- n2: **renders per HDRI folder**: one PNG per HDRI file 

## Techniques
- t1: **Rebuild World node tree from scratch**: Get scene.world.node_tree, clear nodes collection, then add Environment Texture, Background, World Output nodes with nodes.new and link them.
- t2: **Incremental node X placement**: Keep location_x variable; after each nodes.new set node.location.x and add 300 to avoid overlapping nodes.
- t3: **Timestamped render filenames**: Build name from datetime hour/minute/second, set scene render output path, call render.render(write_still=True).
- t4: **Function split batch loop**: Wrap apply_hdri(path) and render_image() in functions; main loops over Path('hdris').iterdir() and renders each.

## Points to
- poly haven (polyhaven.com) HDRI source
- Blender Python API documentation (linked in video description)
