---
type: research-source
id: yt-rEhllWKhrfc
title: "REVIEWING YOUR ANIMATIONS 🥀🥀🥀"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=rEhllWKhrfc"
published: "2026-07-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0063
relevance: 1
density: low
tags: ["research-source", "youtube", "other", "rigging-animation"]
---
# yt-rEhllWKhrfc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Live stream reviewing viewers' Roblox animations (Moon Animator, Blender, 2D). Mostly generic animation critique: spacing, offset arms, weight transfer, feet sliding, exaggeration. Little on Blender-MCP, bpy, or the Blender-to-Roblox export pipeline. Mentions Blender version advice and that Roblox's default animation editor is weak.

## Claims
- c1: [7:48] Offsetting arm keyframes by a few frames from body/leg keys makes motion look better, especially in idles and walks. *(opinion, medium; rigging-animation)*
- c2: [8:30] Feet sliding is a common problem with FK rigs during walks; main fix is foot locking. *(opinion, medium; rigging-animation)*
- c3: [9:12] Animating at 6 FPS was called far too low; 12 FPS is unusual; 24 suggested for clips, 60 for game animation. *(opinion, medium; rigging-animation)*
- c4: [36:42] Roblox Studio default animation editor is described as bad; the speaker says software is rarely the real problem. *(opinion, low; rigging-animation)*
- c5: [37:23] Blender default easing is said to look smoother than Moon Animator without manual easing or many in-betweens. *(opinion, low; rigging-animation)*
- c6: [44:20] Blender 4.4.3 is fine to use, but 5.1.3 is recommended. *(opinion, low; other)*
- c7: [29:09] Weight transfer in walk cycles needs the contact pose and passing pose heights varied, so the body rises and falls. *(opinion, medium; rigging-animation)*
- c8: [17:23] Animations look floaty when keyframes are evenly spaced; vary keyframe spacing per pose. *(opinion, medium; rigging-animation)*
- c9: [22:53] Roblox characters have only six body parts (blocky), so they need more exaggeration than references. *(opinion, medium; rigging-animation)*
- c10: [40:48] Viewer animation at 60 FPS can look too smooth; uneven keyframe spacing reduces floatiness. *(opinion, low; rigging-animation)*
- c11: [1:28:57] Do not copy reference one-to-one; Roblox poses should be more exaggerated than the reference. *(opinion, medium; rigging-animation)*
- c12: [1:24:05] A rig with R15 controls on an R6 body is wrong; too many bones/controls is a problem. *(opinion, medium; rigging-animation)*
- c13: [49:13] Advice: learn animation from non-Roblox sources (12 principles of animation, Alan Becker video) rather than copying Roblox tutorial poses. *(opinion, low; other)*

## Numbers
- n1: **animation FPS**: 6 FPS (called too low), 12 mentioned, 24 suggested, 60 for games Frame rate advice for Roblox animation review
- n2: **Roblox body parts**: 6 Speaker's statement about blocky Roblox rigs
- n3: **Blender version**: 4.4.3 ok; 5.1.3 recommended Answer to viewer question on version

## Techniques
- t1: **Offset keyframes between body parts**: Shift arm and head keys a few frames off from torso/legs so motion is not stiff or robotic.
- t2: **Walk cycle weight transfer**: Use five poses incl. contact and passing; make passing pose higher than contact so body bobs up and down.
- t3: **Vary keyframe spacing**: Avoid equal spacing between keys; vary spacing per pose to reduce floaty look.
- t4: **Follow-through on fast motion**: Let limbs overshoot and settle after fast moves instead of stopping abruptly.

## Quotes (brief, for attribution)
> unless you're using the freaking Roblox Studio default animation dab cuz that thing sucks.  (at 36:42, Nisky)
> you've got only six body parts. It's blocky. It just needs a lot of exaggeration.  (at 19:26, Nisky)

## Contradictions flagged
- Speaker says 60 FPS is fine for games and 24 for clips, but also calls 60 FPS too smooth for viewer work. (vs Own earlier statement that game animation should be at 60 FPS most of the time)

## Points to
- 12 principles of animation (Alan Becker YouTube video)
- Noble Frugal Studio timing and spacing video
- Eclipse Animator plugin (upcoming, speaker's alternative)
- Moon Animator
