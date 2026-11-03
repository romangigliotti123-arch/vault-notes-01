---
type: research-source
id: yt-AzC8jKpT9pY
title: "How To Make A Roblox Rig: EP5, Rigging a Torso (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=AzC8jKpT9pY"
published: "2023-09-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "rigging-animation"]
---
# yt-AzC8jKpT9pY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Manual Blender rigging tutorial (episode 5 of a Roblox rig series) for a torso in a Roblox-style tool rig. Covers armature bone layers, bendy-bone segments, stretch-to-constraints, limit-scale constraint, vertex-group weighting and Armature Deform parenting. Does not cover Claude, blender-mcp, bpy scripting, or Roblox import/export settings.

## Claims
- c1: [1:09] Bone layers in Armature object data properties group bones; a main layer holds all bones and secondary layers hide extra bones. *(demo, high; rigging-animation)*
- c2: [3:58] Bendy bones are segmented bones; tutorial sets the middle torso bone to 8 segments (suggests 10 if 8 is insufficient). *(demo, high; rigging-animation)*
- c3: [4:39] Stretch To constraint on the torso end bone targets the armature's end handle so the torso bends without the whole tool rotating. *(demo, medium; rigging-animation)*
- c4: [5:20] Limit Scale constraint on torso bone: min 0 and max 1 on all axes, owner space set to Local. *(demo, medium; rigging-animation)*
- c5: [5:37] Vertex group named after the torso bone, all vertices assigned at weight 1, then Armature Deform (Ctrl+P) with the armature parents the mesh. *(demo, high; rigging-animation)*
- c6: [5:37] Without an Armature modifier, bone movement produces no mesh deformation; adding Armature Deform fixes it. *(demo, high; common-mistakes-fixes)*
- c7: [6:12] Result: torso-and-hip tool rig moves with the arms but has no bend shapes yet; author defers those to a later episode. *(demo, medium; rigging-animation)*
- c8: [3:58] End handle parent is cleared with Alt+P (keep connected off) and reparented to the upper torso; start handle should have no parent. *(demo, medium; rigging-animation)*
- c9: [0:25] Author says the torso is harder than other parts of the Roblox rig because of extra work beyond bends (opinion). *(opinion, low; rigging-animation)*

## Numbers
- n1: **bendy bone segments**: 8 (try 10 if needed) middle torso bone segments set in Bendy Bones panel
- n2: **limit scale min/max**: min 0, max 1 on all axes Limit Scale constraint on torso bone, owner space Local
- n3: **vertex weight**: 1.0 torso vertex group assigned to all vertices

## Techniques
- t1: **Bendy bone torso segments**: Create bones spanning torso, rename start/end handles, set middle bone to 8 bendy segments, set handles to Absolute, assign custom handle bones.
- t2: **Stretch To + Limit Scale constraints**: Add Stretch To on torso bone targeting end handle; Limit Scale min 0 max 1, owner Local; reparent end handle to upper torso with Alt+P (keep connected off).
- t3: **Vertex group + Armature Deform**: Create vertex group matching torso bone name, assign all verts at weight 1, shift-select armature, Ctrl+P > Armature Deform.

### Code: Parenting the Armature Deform to the mesh
```text
Select mesh, shift-select Armature, Ctrl+P > Armature Deform
```

## Quotes (brief, for attribution)
> just hold down on shift and select the Armature then press Ctrl p and just click on Armature deform now  (at 5:37, Comix Productions)

## Points to
- Comix Productions 'How To Make A Roblox Rig' series (episode 5)
