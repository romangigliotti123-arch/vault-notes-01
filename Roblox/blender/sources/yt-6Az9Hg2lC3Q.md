---
type: research-source
id: yt-6Az9Hg2lC3Q
title: "Blender Materials with Python Code: Adding detail with noise"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=6Az9Hg2lC3Q"
published: "2023-03-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 1
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-6Az9Hg2lC3Q

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner bpy tutorial: builds a Blender Principled BSDF roughness mask in Python. Creates ShaderNodeValToRGB, noise, mapping and texture coordinate nodes, positions them with a location step, and links them with node_tree.links. Refactors into a create_noise_mask function. Exercises set noise scale and mapping rotation randomly. No Roblox, MCP or Claude content.

## Claims
- c1: [1:38] Script creates material with use_nodes enabled, gets the Principled BSDF node, and sets base color, metallic and roughness via bpy. *(demo, high; claude-blender-ai)*
- c2: [1:38] Roughness is randomized each run using Python random.uniform, generating values between 0.1 and 1. *(demo, high; claude-blender-ai)*
- c3: [3:30] Color Ramp is created via node_tree.nodes.new with the internal type name ShaderNodeValToRGB; the name was taken from Blender Python docs. *(demo, high; claude-blender-ai)*
- c4: [4:14] Nodes created by script appear at the origin; setting node.location.x to -300 moves them left of the BSDF to avoid overlap. *(demo, high; claude-blender-ai)*
- c5: [5:40] Connections are made with node_tree.links.new(output_socket, input_socket), e.g. ColorRamp Color output to Principled BSDF Roughness input. *(demo, high; claude-blender-ai)*
- c6: [7:00] Node x-position is tracked with a step variable (-300) and current-x variable so each added node is offset automatically instead of hand-typed. *(demo, high; claude-blender-ai)*
- c7: [9:09] Mapping and Noise Texture are linked via Vector sockets; Texture Coordinate Generated or Vector output feeds the Mapping node. *(demo, medium; claude-blender-ai)*
- c8: [10:03] Color ramp stop positions are edited via color_ramp.elements[0].position and elements[1].position to create roughness islands. *(demo, high; claude-blender-ai)*
- c9: [13:55] Node inputs can be set by socket name via node.inputs['Scale'].default_value rather than index; the scale of Noise Texture is set this way. *(demo, high; claude-blender-ai)*
- c10: [14:37] Discovery aids: hovering a field with Python tooltips enabled shows the bpy path; Info editor logs the Python equivalent of UI changes. *(demo, high; claude-blender-ai)*
- c11: [16:35] Noise scale randomized from 1 to 20 each run using random.uniform. *(demo, high; claude-blender-ai)*
- c12: [17:15] Mapping node rotation X/Y/Z set to random values 0–360 degrees, converted with math.radians because bpy rotation uses radians. *(demo, high; claude-blender-ai)*
- c13: [17:15] Script needs an explicit import math at the top to use math.radians. *(demo, high; claude-blender-ai)*
- c14: [11:05] Refactored node-building code into a create_noise_mask() function that returns the ColorRamp node, then linked it to the BSDF in the caller. *(demo, high; automation-and-creator-workflows)*
- c15: [0:00] Clean-scene step at script start deletes all objects before creating the material and the icosphere, so reruns stay clean. *(demo, medium; other)*

## Numbers
- n1: **random roughness range**: 0.1 to 1 
- n2: **node x location offset**: -300 
- n3: **noise scale random range**: 1 to 20 
- n4: **mapping rotation random range**: 0 to 360 degrees (converted with math.radians) 
- n5: **video length**: 18:46 

## Techniques
- t1: **Node positioning via location.x**: After nodes.new(), set node.location.x (e.g. -300) so nodes do not overlap the Principled BSDF. Track x with step variable to offset successive nodes.
- t2: **Scripted socket linking**: Get node_tree from material, then node_tree.links.new(source_node.outputs['Color'], target_node.inputs['Roughness']). Use socket names rather than indices.
- t3: **Discover bpy paths from UI**: Enable Python Tooltips in preferences and hover a field to see its data path; or change a value and read the Info editor log for the equivalent Python line.
- t4: **Function-per-subgraph refactor**: Move node-building into a function (create_noise_mask) returning the key node; wire it to the BSDF in the caller so the graph is easier to reuse.
- t5: **Randomized parameters per run**: Use random.uniform for noise scale (1-20), roughness, and mapping rotation (0-360 deg, converted with math.radians) so each execution produces a different material.

## Quotes (brief, for attribution)
> I got this name from the Blend Python documentation.  (at 3:30, CG Python)
> remember that blender requires us to provide value rotation values in radiance.  (at 17:15, CG Python)

## Points to
- Blender Python API documentation (cited in video, not linked in transcript)
- Initial code gist linked in video description (not in transcript)
- Previous video in series on Python materials (linked on screen)
