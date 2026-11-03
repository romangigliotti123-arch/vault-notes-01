---
type: research-source
id: yt-deojKsMWMNo
title: "Making the new rig ;)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=deojKsMWMNo"
published: "2022-08-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt-deojKsMWMNo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic livestream of manual rigging in Blender: building bone custom control shapes (planes, cubes, circles), parenting hip/torso/arm bones, limit rotation, copying weights. Mentions a "boxy rig" reference and Blender 3.9. No Roblox export, Claude/MCP, bpy, or pipeline content.

## Claims
- c1: [0:53] Creator says bone control shapes are made by adding simple mesh shapes (plane, cube, circle) and scaling them. *(demo, medium; rigging-animation)*
- c2: [2:15] Shortcut noted: Ctrl+A to apply scale on control shape objects before reuse. *(demo, low; rigging-animation)*
- c3: [4:57] Parenting done by hand: lower torso parented to hip bone, following a prior tutorial. *(demo, low; rigging-animation)*
- c4: [8:22] Control plane given a Subdivision Surface modifier so it does not produce odd geometry. *(demo, low; rigging-animation)*
- c5: [11:49] Bone rotation of 90 degrees on X axis needed so the rig can be posed/animated; positioning values adjusted by hand. *(experience, low; rigging-animation)*
- c6: [17:57] Arm bones named upper_arm.L, lower_arm.L, wrist.L; face bones skipped when selecting arm group. *(demo, medium; rigging-animation)*
- c7: [20:00] Bone Limit Rotation constraint set to 90 degrees in Local space on wrist, then copied to selected bones via weights/constraint copy. *(demo, medium; rigging-animation)*
- c8: [14:32] Head bone placement was often forgotten; creator repeatedly adjusted a 0.55/0.625 position value to get head placed correctly. *(experience, low; rigging-animation)*
- c9: [2:15] Creator advises turning off anti-aliasing to see whether lines are straight in the viewport. *(opinion, low; other)*
- c10: [0:53] Creator opinion: making control shapes is the most boring part of rigging. *(opinion, low; other)*

## Numbers
- n1: **Blender version mentioned**: 3.9 
- n2: **Rotation on X axis**: 90 degrees 
- n3: **Limit rotation**: 90 degrees, local space 
- n4: **Position value adjusted to place head**: 0.55 to 0.625 

## Techniques
- t1: **Custom bone control shapes**: Create a plane/cube/circle mesh, scale and rotate it (90 deg X), then assign as bone custom shape in Pose mode.
- t2: **Copy weights to selected**: Set up weights on one arm bone, then copy the setup to matching bones on the other side.

## Quotes (brief, for attribution)
> this is probably the most boring part of rigging in my opinion  (at 0:53, Comix Productions)

## Points to
- Boxy rig reference (named in transcript, not linked)
