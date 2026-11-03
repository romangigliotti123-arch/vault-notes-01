---
type: research-source
id: yt-_pFs7Cpuc94
title: "HOW TO MAKE PARTICLES (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=_pFs7Cpuc94"
published: "2022-08-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-_pFs7Cpuc94

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic Blender 2.9x-era tutorial on particle systems: hair particle system on a cube, emit from Volume, render as Object using an icosphere, then adjust count, scale, randomness, rotation and instance display. No Claude, blender-mcp, bpy, Roblox export, mesh/texture limits, rigging or accessory content. Off-topic for the research subject.

## Claims
- c1: [0:42] Particle system set to Hair, Emit From set to Volume, Render As set to Object so particles do not emit from the box outskirts. *(demo, high; other)*
- c2: [1:22] Tutorial sets particle count to 2500 and object scale to 0.025 with scale randomness 1. *(demo, high; other)*

## Numbers
- n1: **Icosphere subdivisions**: 1 
- n2: **Particle count**: 2500 (example; 2000 also shown) 
- n3: **Instance object scale**: 0.025 

## Techniques
- t1: **Particle instancing of an object**: Add Hair particle system to cube; Source Emit From Volume; Render As Object; pick icosphere; tune count, scale, scale randomness, rotation randomize under Advanced.
- t2: **Hide emitter in render**: Object properties > Instancing set to Face; uncheck Show Emitter on render (and viewport optionally) so only particles appear.

## Visual notes
none
