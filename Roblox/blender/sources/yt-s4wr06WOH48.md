---
type: research-source
id: yt-s4wr06WOH48
title: "HOW TO RIG ROBLOX WRISTS (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=s4wr06WOH48"
published: "2025-02-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-s4wr06WOH48

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender tutorial on rigging a blocky Roblox wrist: move the lower-arm bone tail up to the wrist, extrude a wrist bone, and reassign vertex weights (wrist.L group) so the hand rotates smoothly. Covers a foot variant. No Claude, bpy/MCP, or Roblox export/import content.

## Claims
- c1: [0:00] Creator says wrist rigging on blocky Roblox rigs is harder than arm rigging; video is a short simple tutorial after a 6-month upload gap. *(demo, high; rigging-animation)*
- c2: [0:32] Wrist method: in edit mode, move lower-arm tail up to wrist position, extrude a new bone down, name it hand/wrist. Needs three loop cuts on the arm mesh. *(demo, high; rigging-animation)*
- c3: [1:17] Weight fix: remove lower-arm weights from the wrist faces, then assign those faces/edges to the wrist vertex group (wrist.L) so the wrist bends with the hand. *(demo, high; rigging-animation)*
- c4: [1:59] Creator says bone origin placement matters: placing the bone tail low (old method) causes the wrist to deform badly; moving the bone up gives smooth gradient weights. *(demo, medium; rigging-animation)*
- c5: [2:58] For feet, creator suggests moving the bone down for a nicer look; inherit rotation toggle was used to keep foot flat. Opinion: the wrist method looks better than the alternative. *(opinion, low; rigging-animation)*

## Numbers
- n1: **loop cuts on arm**: 3 Creator says make sure there are three loop cuts before rigging
- n2: **upload gap**: 6 months Creator's stated time since last upload before this video

## Techniques
- t1: **Wrist bone extrusion with weight reassignment**: Move lower-arm bone tail up to wrist; extrude wrist bone down; remove lower-arm weights on wrist faces; assign wrist faces/edges to wrist.L vertex group; test rotation for smooth gradient.
