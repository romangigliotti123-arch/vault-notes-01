---
type: research-source
id: yt-4T4fcPUmTDk
title: "How To Make A Roblox Rig: EP3, Adding Constraints (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=4T4fcPUmTDk"
published: "2023-08-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-4T4fcPUmTDk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender tutorial (3:39, Comix Productions, Aug 2023), episode 3 of a Roblox rig series. Shows adding Limit Rotation bone constraints in pose mode (owner set to Local Space), tuning min/max per axis for left arm and leg, and using Copy to Selected to mirror to right limbs. No Claude, blender-mcp, bpy scripting, or Roblox export/import content.

## Claims
- c1: [0:25] Bone constraints are added in Pose Mode via the Bone Constraint properties tab; Limit Rotation is used to restrict joint rotation. *(demo, high; rigging-animation)*
- c2: [1:06] Limit Rotation owner set to Local Space so limits use Armature measurements; if rotation goes the wrong way, set max 0 and min -90 on the axis. *(demo, medium; rigging-animation)*
- c3: [1:38] Copy to Selected on the constraint mirrors left-arm limits to the right arm; may need manual fixing depending on how the arms were symmetrized. *(demo, medium; rigging-animation)*
- c4: [2:47] Copy to Selected for leg constraint did not work directly; right leg needed max 0 and min -90 set manually. *(demo, medium; rigging-animation)*

## Numbers
- n1: **Left arm limit rotation X**: min -90, max 0 
- n2: **Left leg limit rotation min (Z axis, first try)**: -19 then max 90 forward 
- n3: **Right leg limit rotation**: max 0, min -90 

## Techniques
- t1: **Copy constraint to selected bones**: Shift-select target bones, make the source bone active, open Bone Constraint dropdown, choose Copy to Selected; verify direction and fix values per side.
- t2: **Limit Rotation axis tuning**: Set Owner to Local Space, test each axis by rotating the bone, flip sign ranges (min/max) on wrong axes until motion matches intent.

## Quotes (brief, for attribution)
> change maximum to zero and change minimum to minus 90  (at 1:06, Comix Productions)

## Visual notes
Contact sheet shows Blender 4.x-style Pose Mode with a wireframe cage around a stick-figure armature (bones named LeftArm, RightArm, LeftLeg, etc.) and Bone Constraint panels with Limit Rotation X/Y/Z fields and Owner/Space dropdowns.
