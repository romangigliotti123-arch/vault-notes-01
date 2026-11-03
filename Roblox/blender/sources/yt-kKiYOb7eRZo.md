---
type: research-source
id: yt-kKiYOb7eRZo
title: "HOW TO RIG A ROBLOX TORSO WITH BENDY BONES (BLENDER)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=kKiYOb7eRZo"
published: "2022-04-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0045
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "rigging-animation"]
---
# yt-kKiYOb7eRZo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short 2022 Blender tutorial (Comix Productions, about 6 min) on rigging a Roblox-style torso with bendy bones in Blender's native armature system. No Claude, MCP, bpy scripting or Roblox export steps. Covers bone setup, bendy-bone segments, Stretch To constraint, vertex-group weighting, and Limit Scale constraints to stop scale growth on rotation.

## Claims
- c1: [2:42] Bendy bone segments set to about 10 in Bone Properties > Bendy Bones; author says 10 is good enough. *(demo, medium; rigging-animation)*
- c2: [3:23] Bendy torso bone uses a Stretch To constraint targeting the end handle, with start/end handles set to absolute. *(demo, medium; rigging-animation)*
- c3: [3:23] Torso mesh parented to armature with empty groups, then only the bendy-torso vertex group kept and assigned at weight 1 in edit mode. *(demo, medium; rigging-animation)*
- c4: [4:06] Torso mesh grows when rotated too far; fixed with Limit Scale constraint (min 0, max 1 on all axes, owner local space). *(demo, medium; common-mistakes-fixes)*
- c5: [4:46] Hip bone added as parent of the unused end handle so lower torso moves correctly when rotated. *(demo, low; rigging-animation)*
- c6: [0:00] Author says the video was delayed by repeated dependency cycles in rig setup. *(opinion, low; common-mistakes-fixes)*

## Numbers
- n1: **Bendy bone segments**: 10 Recommended segment count for bendy torso bone
- n2: **Limit Scale min/max**: 0 / 1 Limit Scale constraint values on all axes

## Techniques
- t1: **Bendy-bone torso rig**: Add armature, create lower torso, upper torso and hip bones, extrude bendy bone with segments about 10, parent end handle to upper torso, Stretch To constraint to end handle, parent mesh with empty groups, assign weight 1 to bendy group.
- t2: **Limit Scale fix**: Add Limit Scale constraint to bendy bone with min 0 and max 1 on all axes, owner set to Local Space, to stop scale growth on rotation.

## Quotes (brief, for attribution)
> the torso actually gets bigger when you rotate too much. So we will be fixing this.  (at 4:06, Comix Productions)
