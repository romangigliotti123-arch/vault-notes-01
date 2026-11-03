---
type: research-source
id: yt-W1cZXEs8EIo
title: "Art with a Blender Python Script"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=W1cZXEs8EIo"
published: "2025-01-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "other", "procedural-generation"]
---
# yt-W1cZXEs8EIo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video walkthrough of a Blender Python (bpy) script that renders abstract hair-strand art: sets world background black, Cycles with GPU and 300 samples, square resolution, camera and area light, a curve-circle emitter converted to mesh, a hair particle system with a turbulence force field, and an emission material built from nodes via Python. Not about Claude, blender-mcp, or Roblox export.

## Claims
- c1: [1:11] Blender world background colour is set via bpy by getting the world's node tree and changing the Background shader node colour to pure black. *(demo, high; bpy-scripting-headless)*
- c2: [10:13] Re-running a bpy script that creates particle systems accumulates duplicate data blocks (e.g. ParticleSettings.001); the author fixes it by purging orphan data at the top of the script after deleting objects. *(demo, high; bpy-scripting-headless)*
- c3: [10:54] Deleting objects in Blender does not free their data blocks until reload; purge orphans with recursive option is used to clear leftover data before re-running. *(demo, medium; bpy-scripting-headless)*
- c4: [3:22] bpy rotation values must be in radians, so degrees are converted with math.radians (e.g. 90 degrees on X) when creating camera objects. *(demo, high; bpy-scripting-headless)*
- c5: [12:58] Materials can be built by script: create material, set use_nodes off/on, clear node tree, add nodes with set locations, then link sockets explicitly via node tree links. *(demo, high; bpy-scripting-headless)*
- c6: [8:05] Hair particle system in bpy: type set to HAIR, count 10,000, hair length 2, 6 steps; turbulence force field (strength 25) makes strands spread out; author notes the turbulence force is the key effect. *(demo, medium; procedural-generation)*
- c7: [6:24] A curve circle with bevel depth and extrude is converted to mesh (convert to mesh) to serve as particle emitter, with render visibility disabled so only hair renders. *(demo, medium; procedural-generation)*
- c8: [2:19] Cycles set with GPU device and 300 samples via bpy; the author says Eevee is an alternative, choice is preference. *(demo, medium; bpy-scripting-headless)*
- c9: [20:33] Video is an art-generation tutorial; it does not cover Claude, blender-mcp, Roblox Studio export, or any Roblox import settings. *(doc, high; other)*

## Numbers
- n1: **Cycles render samples**: 300 
- n2: **hair particle count**: 10,000 
- n3: **hair length / steps**: 2 / 6 
- n4: **turbulence force strength**: 25 
- n5: **backdrop plane size**: 20 
- n6: **area light power**: 100 
- n7: **square render resolution**: 1080 x 1080 (from 1920x1080 default) 

## Techniques
- t1: **Orphan data purge at script start**: After deleting scene objects, call bpy.ops.outliner.orphans_purge recursively at top of script so stale ParticleSettings and materials are not reused on rerun.
- t2: **Node-tree material via bpy**: Create material, enable nodes, remove default nodes, add Hair Info, Value to RGB (constant interp), Math multiply, Principled BSDF, Output with set locations, then link sockets and append material to emitter's material slots.

## Points to
- CG Python community (extended video promised, not in source)
- Mitch Siv tutorial (original technique source)
