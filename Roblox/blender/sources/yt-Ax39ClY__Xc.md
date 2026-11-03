---
type: research-source
id: yt-Ax39ClY__Xc
title: "How To Make A Roblox Rig: EP6, Fixing Bends (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=Ax39ClY__Xc"
published: "2023-09-19"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "rigging-animation", "texturing-baking-uv"]
---
# yt-Ax39ClY__Xc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender tutorial (Comix Productions, EP6 of a Roblox rig series) on fixing arm and leg bend deformation for a Roblox R15-style rig using shape keys driven by armature bone transforms. Covers box-selecting verts, disabling smooth wires/anti-aliasing for straight edges, and adding drivers with tan() expressions. No Claude, MCP, bpy or Roblox export/import content.

## Claims
- c1: [1:40] Bends are made with a shape key 'Bend' per mesh; the basis stays unchanged and the Bend key is edited in edit mode with modifiers' edit-mode toggles enabled. *(demo, high; rigging-animation)*
- c2: [1:40] Box-select all vertices on both models when editing shape keys, since click-select only picks front or back verts. *(demo, medium; rigging-animation)*
- c3: [2:20] Turning off viewport smooth wires and anti-aliasing makes bend edges visibly straight; the author says this helps and keeps it off. *(opinion, medium; texturing-baking-uv)*
- c4: [3:31] Author says the basic bend is a starting point; moving the outer verts too far down makes the bend look sharp, so keep edge loops in equal diagonal lines. *(opinion, low; rigging-animation)*
- c5: [5:36] Without a driver, the Bend shape key stays at full value regardless of pose, so it must be driven by the bone rotation to appear progressively. *(demo, high; rigging-animation)*
- c6: [6:18] Driver setup: right-click Bend value > Add Driver; object = Armature, bone = lower arm; variable type Transform Channel, X Rotation, Local Space, matching the bone constraint value of -90°. *(demo, high; rigging-animation)*
- c7: [7:38] Driver expression used is tan(var/2), with a leading minus added for the arm because the constraint minimum was -90°; then click Update Dependencies. *(demo, high; rigging-animation)*
- c8: [8:33] Copy the working driver and paste it to other Bend values, then edit each to point at the correct bone (right lower arm, left/right lower leg) since copied drivers don't retarget correctly. *(demo, high; rigging-animation)*
- c9: [9:14] Leg bends use Z Rotation rather than X Rotation, so the expression has no minus sign: tan(var/2). *(demo, high; rigging-animation)*
- c10: [6:18] Author notes older rigs released publicly lacked correct driver setup and that the drivers were confusing for them at first; the tutorial teaches drivers for later episodes. *(opinion, low; common-mistakes-fixes)*

## Numbers
- n1: **Bone constraint rotation value for arm bend**: -90°, local space, X axis 
- n2: **Driver expression**: tan(var/2) with minus for arm, none for leg 
- n3: **Bend key rotation limit before deformation**: arm lower bones rotated to maximum (-90° per constraint) 

## Techniques
- t1: **Shape-key bend correction**: Enable modifier edit-mode toggles, add shape key 'Bend' (keep Basis), in edit mode box-select verts on both meshes, move into straight diagonal edge loops, check no aliasing jaggies.
- t2: **Bone-driven shape key driver**: Right-click Bend value > Add Driver; Armature object + bone; add Transform Channel variable (Rotation, Local space) matching constraint axis; expression tan(var/2) with sign set by constraint; Update Dependencies.
- t3: **Copy/paste driver then retarget**: Copy working driver, paste on other Bend values, then Edit Driver to change bone and rotation axis (Z for legs) and sign.

### Code: Driver expression used for the arm and leg Bend shape keys
```text
tan(var/2)  (arm: -tan(var/2); leg: tan(var/2) with Z rotation)
```

## Quotes (brief, for attribution)
> make sure it is the tangent of your variable divid by two  (at 7:38, Comix Productions)
