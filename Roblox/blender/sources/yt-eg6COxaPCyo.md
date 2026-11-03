---
type: research-source
id: yt-eg6COxaPCyo
title: "Roblox Animation in Blender: Full Beginner Guide [2026]"
source_type: "youtube"
creator: "Nisky"
url: "https://www.youtube.com/watch?v=eg6COxaPCyo"
published: "2025-11-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 3
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# yt-eg6COxaPCyo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial for hand-animating an R6 IK rig in Blender and getting it into Roblox Studio. Covers installing the Lazy Viewport and RBX animation importer add-ons, pose/tweak basics, dope sheet and graph editor smoothing (Automatic easing, in-betweens, cycles/noise), Save As habit, then exporting and uploading via the Blender Animations Ultimate Edition plugin and Moon Animator. No blender-mcp, bpy scripting, or Claude content.

## Claims
- c1: [0:14] Blender add-ons installed via Edit > Preferences > Add-ons > Install from disk: 'Lazy Viewport' (viewport rotate/move helper) and 'RBX animation importer' (exports animations to Roblox Studio). *(demo, high; blender-roblox-export-import)*
- c2: [0:51] Workflow uses the R6 IK rig in Blender pose mode; Tweak tool moves bones, the torso drags the whole rig, and dope sheet shows keyframes. *(demo, high; rigging-animation)*
- c3: [1:32] Timeline defaults to 40 frames; author sets End to 120 for a 2-second animation (author says 'pretty sure'). *(demo, medium; rigging-animation)*
- c4: [2:36] In Graph Editor, axes with no movement show flat curves; author ignores flat curves and keeps only curves with motion. *(opinion, medium; rigging-animation)*
- c5: [3:19] Smoothing method: select keyframes, press V > Automatic to apply easing, then add in-between poses to smooth motion. *(demo, high; rigging-animation)*
- c6: [4:41] Sway technique: bring curve back past the key so the limb overshoots and returns, applied per keyframe; author says no single right way. *(opinion, medium; rigging-animation)*
- c7: [5:22] Graph Editor sidebar (N > Modifiers) offers Cycles to loop motion and Noise to randomize; author says rarely needed. *(demo, high; rigging-animation)*
- c8: [5:51] Use File > Save As rather than Save to avoid overwriting the base tutorial file when making new animations. *(opinion, medium; automation-and-creator-workflows)*
- c9: [6:18] Export animation via the RBX addon's Roblox animation export option, then import into Roblox Studio via the 'Blender Animations Ultimate Edition' plugin from Toolbox. *(demo, medium; blender-roblox-export-import)*
- c10: [6:18] Loading a character in Studio: a character inserter plugin (author uses Moon Animator's character inserter); alternative 'load character' plugin mentioned. *(demo, medium; avatar-ugc-accessories)*
- c11: [7:00] Animation is pasted from clipboard into Studio, uploaded to Roblox via Upload Animation to Roblox with title and optional description; trimming in Blender recommended (author's test was 101 frames). *(demo, medium; rigging-animation)*
- c12: [7:00] With Moon Animator: New rig animation > File > Import Roblox, select the uploaded animation to edit it in Moon Animator. *(demo, medium; automation-and-creator-workflows)*

## Numbers
- n1: **timeline length**: 40 default, 120 frames (2s) 
- n2: **test animation length**: 101 frames before trimming 

## Techniques
- t1: **Automatic easing + in-betweens**: Select all keys, press V, choose Automatic. Add intermediate poses on other bones to smooth motion, then reapply Automatic.
- t2: **Overshoot sway**: In Graph Editor, move curve handle so the limb overshoots past the key and settles back, per keyframe.
- t3: **Cycles/Noise modifiers**: Graph Editor, N panel, Modifiers tab: add Cycles to loop or Noise to randomize motion.
- t4: **Save As versioning**: Use File > Save As with a new name for each animation so the base file stays intact.

## Quotes (brief, for attribution)
> the animation importer is to import your animations from Blender into Roblox Studio and the lazy viewport is kind of a quality of life thing.  (at 0:14, Nisky)

## Points to
- Moon Animator
- Blender Animations Ultimate Edition (Roblox plugin)
- Lazy Viewport add-on
- RBX animation importer add-on
- Nisky Discord
