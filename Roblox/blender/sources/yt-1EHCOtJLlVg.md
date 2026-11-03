---
type: research-source
id: yt-1EHCOtJLlVg
title: "How To Make A Roblox Rig: EP7, Adding IK Constraints (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=1EHCOtJLlVg"
published: "2023-09-27"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-1EHCOtJLlVg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Episode 7 of a Blender rig series for Roblox (Comix Productions) covering IK constraints on legs and arms. Shows adding an Inverse Kinematics bone constraint with an Armature target and a separate pole-target bone, setting chain length to 2, adjusting pole angle, and limiting rotation via the IK bone panel. No Claude, blender-mcp, bpy, or Roblox import/export content.

## Claims
- c1: [1:51] For a two-bone limb IK, set the IK constraint Chain Length to 2 so the chain covers upper and lower bone. *(demo, medium; rigging-animation)*
- c2: [1:51] Leg IK needed pole angle 90 to face the knee the correct direction in the creator's rig. *(demo, medium; rigging-animation)*
- c3: [2:32] Limit the IK bone's Z rotation to min 0 and max 90 to stop the leg bending past its limit. *(demo, medium; rigging-animation)*
- c4: [3:20] Arm IK uses target and pole target set to the Armature, with the pole target on a separate arm pole bone. *(demo, medium; rigging-animation)*
- c5: [4:29] Arm IK limit rotation on X is set min -90 and max as per constraint (Z max noted). *(demo, low; rigging-animation)*
- c6: [4:51] Pole angle is rig-specific: creator had to change it from 0 and 90 to 180 for some limbs. *(demo, medium; rigging-animation)*
- c7: [0:13] Leg IK is crucial for animators; for GFX-only rigs IK matters little (opinion). *(opinion, medium; rigging-animation)*

## Numbers
- n1: **IK chain length**: 2 
- n2: **Leg pole angle**: 90 (some limbs 180) 
- n3: **Leg Z limit**: min 0, max 90 
- n4: **Arm X limit**: min -90 

## Techniques
- t1: **Bone IK constraint setup**: Select lower leg bone, add Inverse Kinematics in Bone Constraint properties, set Target and Pole Target to the Armature with IK and pole bones, set chain length to 2, then tune pole angle.
- t2: **IK rotation limits**: Open Bone properties > Inverse Kinematics on the IK bone and set per-axis min/max limits to prevent over-bending.
