---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-animation.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/animation.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/animation.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "other", "rigging-animation"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-animation.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Guide from the blender-mcp repo on keyframing via bpy across versions (4.4 slotted actions, 5.0 removed Action.fcurves), easing, looping with Cycles modifiers, NLA strips, action naming, cameras, and checking motion with look(mode='frames'). Animation-general; no Roblox export or import content.

## Claims
- c1: Keyframing via bpy (keyframe_insert on location/rotation_euler) works in every Blender version and needs no context. *(doc, high; bpy-scripting-headless)*
- c2: Blender 4.4 added slotted actions; Blender 5.0 removed Action.fcurves, so scripts must use anim_utils.action_get_channelbag_for_slot when action_slot exists. *(doc, high; bpy-scripting-headless)*
- c3: Pose bone keyframes use pose-space values, not world space. *(doc, high; rigging-animation)*
- c4: Safe mode may block drivers; keyframes always work. *(doc, medium; bpy-scripting-headless)*
- c5: Name actions like Character_Walk or Door_Open because game engines import them by name. *(doc, medium; rigging-animation)*
- c6: Push finished actions into NLA strips via nla_tracks.new() and strips.new() to layer or sequence clips. *(doc, high; rigging-animation)*
- c7: For seamless loops, make first and last key identical and add a CYCLES fcurve modifier, or exclude the duplicate last frame from the frame range. *(doc, high; rigging-animation)*
- c8: look(mode='frames') returns a strip of evenly spaced frames; frames=[...] selects specific frames and view='camera' renders through the camera, to check motion. *(doc, high; claude-blender-mcp)*
- c9: Author opinion: timing and spacing matter more than poses; ease in/out of holds, keep linear for constant motion like wheels. *(opinion, medium; creator-workflows)*
- c10: Source is an animation guide for the blender-mcp repo, not Roblox-specific; it does not cover Roblox export, scale, or the Roblox import pipeline. *(doc, high; other)*

## Numbers
- n1: **follow-through offset**: 2-4 frames Secondary parts like antennae or tails offset from main motion
- n2: **Blender version boundaries**: 4.4 added slotted actions; 5.0 removed Action.fcurves Fcurve access differs across these versions
- n3: **example scene timing**: frames 1-120 at 24 fps Example scene settings in keyframe snippet

## Techniques
- t1: **Cycles loop seam**: Make first and last key identical, add fc.modifiers.new('CYCLES'), or exclude duplicate last frame from frame range.
- t2: **NLA clip layering**: Create track via ad.nla_tracks.new(), then track.strips.new(name, start, action) to sequence clips such as walk then wave.
- t3: **Version-safe fcurve access**: Check hasattr(ad,'action_slot'); if true use anim_utils.action_get_channelbag_for_slot, else ad.action.fcurves.
- t4: **Frame strip motion check**: Call look(mode='frames') for evenly spaced frames; add frames=[...] or view='camera' to inspect specific shots.

### Code: Keyframe object location and rotation across frames
```python
scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, 120
scene.render.fps = 24

obj.location = (0, 0, 0); obj.keyframe_insert("location", frame=1)
obj.location = (0, 0, 2); obj.keyframe_insert("location", frame=24)
obj.rotation_euler.z = 3.1416; obj.keyframe_insert("rotation_euler", index=2, frame=48)
```

### Code: Get fcurves across Blender versions (slotted actions in 4.4+, removed Action.fcurves in 5.0)
```python
def fcurves(obj):
    ad = obj.animation_data
    if not ad or not ad.action:
        return []
    if hasattr(ad, "action_slot"):
        from bpy_extras import anim_utils
        cb = anim_utils.action_get_channelbag_for_slot(ad.action, ad.action_slot)
        return list(cb.fcurves) if cb else []
    return list(ad.action.fcurves)
```

## Quotes (brief, for attribution)
> Keyframe properties directly; it works in every version and needs no context  (ahujasid)
> A single screenshot can't show motion.  (ahujasid)

## Points to
- https://github.com/ahujasid/mcp-for-blender
