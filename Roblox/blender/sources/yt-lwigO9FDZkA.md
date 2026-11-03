---
type: research-source
id: yt-lwigO9FDZkA
title: "How To Animate Guns in Roblox - Moon Animator (2026)"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=lwigO9FDZkA"
published: "2025-10-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "youtube", "rigging-animation"]
---
# yt-lwigO9FDZkA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Studio tutorial (Moon Animator, Easy Weld plugin) on animating a Glock 17 rig: welding handle and mesh parts, animating slide and a beam "muzzle flash" via width keyframes, and detaching the beam from the gun. Does not use Blender, Claude, bpy, or the Blender-to-Roblox export pipeline. Only tangentially relevant.

## Claims
- c1: [0:21] Pre-made Glock model has meshes already connected and named; a transparent handle part is added and welded to parts via Easy Weld plugin (join in place). *(demo, medium; rigging-animation)*
- c2: [2:07] Moon Animator only animates parts with 'animatable' checked; beam width animated by keyframing Width 0 and Width 1 values. *(demo, medium; rigging-animation)*
- c3: [2:48] Looping shots requires pausing the beam animation with an extra keyframe and setting ease to None, otherwise the animation keeps playing after the shot. *(demo, low; rigging-animation)*
- c4: [5:17] Deleting the beam from the handle stops it following the barrel, but then it no longer follows arm movement and must be moved manually by keyframes. *(demo, medium; rigging-animation)*

## Numbers
- n1: **beam width keyframe values**: 0 and 1 (shot), 2 and 5 (second shot) Width Zero/Width One properties used for muzzle beam flash
- n2: **video length**: 5:59 claimed build time under 10 minutes

## Techniques
- t1: **Keyframed slide recoil in Moon Animator**: Keyframe slide, move it back a few frames later, copy the start keyframe and paste it at the end to return the slide.
- t2: **Detach beam from weapon**: Delete beam from handle so it stays in place after shot; keyframe its position manually when arm moves.

## Points to
- Moon Animator
- Easy Weld plugin
