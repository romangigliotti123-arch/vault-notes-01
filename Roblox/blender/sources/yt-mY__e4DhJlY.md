---
type: research-source
id: yt-mY__e4DhJlY
title: "[Patreon Monthly Asset] Blender Add-on : Particle Pro"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=mY__e4DhJlY"
published: "2021-08-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 0
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "other", "procedural-generation"]
---
# yt-mY__e4DhJlY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Darkfall Patreon monthly-asset video (2021) demos "Particle Pro", a Blender add-on that generates particle streams that follow a Bezier path. Covers install via Preferences > Add-ons, operator settings (count, lifetime, gravity, movement speed, particle flow). Nothing on Roblox, Claude, MCP, or bpy export pipeline.

## Claims
- c1: Source is a Blender particle add-on demo; does not cover Roblox, Claude, blender-mcp, or Roblox export pipeline. *(doc, high; other)*
- c2: [0:30] Blender add-on installed via Edit > Preferences > Add-ons > Install, then enabled; one-time step. *(demo, high; bpy-scripting-headless)*
- c3: [1:07] Particle Pro operator exposes particle count, lifetime (example 250 frames), lifetime random, gravity toggle, movement speed (example -33), and particle flow (0 = ignore path, 10 = stick to path). *(demo, medium; procedural-generation)*

## Numbers
- n1: **Lifetime example**: 250 frames Particle lifetime set in Particle Pro operator
- n2: **Movement speed example**: -33 Negative speed means faster; closer to zero is slower
- n3: **Particle flow path-following**: 0 vs 10 0 ignores path; 10 sticks to path

## Techniques
- t1: **Path-edited particle curve**: Edit mode on path curve, move control points in top view, extrude endpoint with E to shape curve, then play from frame 1 so particles follow it.

## Points to
- Darkfall Patreon
