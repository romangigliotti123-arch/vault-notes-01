---
type: research-source
id: yt-Is8Qu7onvzM
title: "Master the Basics of Blender Python for Geo Nodes in Just One Video"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=Is8Qu7onvzM"
published: "2023-03-27"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "procedural-generation"]
---
# yt-Is8Qu7onvzM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial for building a Geometry Nodes network with bpy in the Text Editor. Covers scene-clearing helper code, copying UI actions from the Info panel to get Python, creating nodes by type name, laying them out via location.x, linking sockets, and setting inputs. No Roblox, Claude, blender-mcp or export content.

## Claims
- c1: [0:29] Script is written and run in Blender's Text Editor; provided helper code clears the scene each run so iteration is fast. *(demo, high; bpy-scripting-headless)*
- c2: [2:07] Info panel in the Scripting workspace shows Python equivalents of the last UI actions; author copies those lines (add plane, add geometry nodes modifier) into the script. *(demo, high; bpy-scripting-headless)*
- c3: [4:17] Geometry nodes are added with node_tree.nodes.new(type=...) using a node type name taken from the Python API documentation (e.g. cube mesh, subdivide mesh, triangulate, split edges, scale elements). *(demo, high; procedural-generation)*
- c4: [6:31] Newly created nodes all spawn at the same spot; author spaces them by setting node.location.x with a 300-unit step per node, and also moves the group output node. *(demo, high; bpy-scripting-headless)*
- c5: [8:48] Nodes are connected with node_tree.links.new(from_socket, to_socket) by picking the mesh output socket and the mesh input socket. *(demo, high; bpy-scripting-headless)*
- c6: [10:56] Author refactors repeated node creation into a helper create_node(node_tree, type, x, step=0) that returns the node and next x position; a similar link_nodes helper handles mesh-socket links. *(demo, medium; bpy-scripting-headless)*
- c7: [19:41] Node inputs can be set in script by index or by socket name (e.g. Subdivide Mesh levels set to 4); the Info panel gives the exact socket names. *(demo, medium; procedural-generation)*
- c8: [20:22] Scale Elements scale input is set in script to 0.7 to make the split-and-scale result visible. *(demo, medium; procedural-generation)*
- c9: [21:05] Transcript says subdivision value is set to 3 at this point, which conflicts with the earlier value of 4; the exact final value is unclear from audio. *(demo, low; procedural-generation)*
- c10: [21:45] Solidify modifier was added manually via the UI first and then its Python line was copied into the create function after the node update. *(demo, medium; bpy-scripting-headless)*
- c11: [23:06] Next video in the series covers animating and looping the Scale Elements scale input from Python. Final code is posted in the description. *(doc, low; procedural-generation)*

## Numbers
- n1: **node x-spacing step**: 300 units 
- n2: **Subdivide Mesh levels set in script**: 4 
- n3: **Scale Elements scale set in script**: 0.7 

## Techniques
- t1: **Info-panel to Python**: Perform action in UI, copy the matching command from Scripting workspace Info panel, paste into Text Editor script, comment and rerun to verify.
- t2: **Node layout by location.x**: Track current x in a variable, add a fixed step (300) after each nodes.new call, set node.location.x, and move the group output node too.
- t3: **Helper-function refactor**: Wrap nodes.new and positioning in create_node(tree, type, x, step) returning node and next x; wrap links.new in a link helper taking from/to nodes.
- t4: **Set inputs by socket name**: Copy input socket reference from Info panel, then assign node.inputs['Level'] or similar value in script before rerunning.

## Points to
- Blender Python API documentation (node type names), linked in video description
- Initial helper code file linked in video description (raw text)
- Final script posted in video description
