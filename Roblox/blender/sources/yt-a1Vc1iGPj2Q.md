---
type: research-source
id: yt-a1Vc1iGPj2Q
title: "How to Use RigEdit Lite in Roblox Studio (Create & Edit Joints)"
source_type: "youtube"
creator: "MrWonderHow"
url: "https://www.youtube.com/watch?v=a1Vc1iGPj2Q"
published: "2026-10-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-a1Vc1iGPj2Q

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio tutorial on the RigEdit Lite plugin (free version, installed from Toolbox). Covers viewing rig joints, moving and resetting them, creating joints between parts (Create Joints), and welding decorative parts (Create Welds). Does not involve Blender, bpy, Claude, or FBX/glTF export, so it is only tangentially related to the topic.

## Claims
- c1: [0:14] RigEdit Lite is a free Roblox Studio plugin installable from the Toolbox; a paid Pro version exists. *(demo, high; rigging-animation)*
- c2: [2:00] RigEdit Lite's Create Joints button auto-creates a joint between two selected parts (shift-select second part), letting the new part move relative to the first when animated. *(demo, medium; rigging-animation)*
- c3: [3:18] RigEdit Lite's Create Welds button welds selected parts to a base part so they move with it instead of independently. *(demo, medium; rigging-animation)*
- c4: [1:15] Custom model animation playback requires an anchored root PrimaryPart, Motor6D joints between parts, and an AnimationController inside the model. *(demo, medium; rigging-animation)*

## Techniques
- t1: **Create joints via plugin**: Select model, open Rig Edit, select parent part, shift-select child part, click Create Joints. Plugin generates joint between them.
- t2: **Weld decorations to moving part**: Open Rig Edit, select base part first, shift-select decoration parts, click Create Welds.

## Points to
- RigEdit Lite plugin (Roblox Toolbox; Pro version linked in video description)
