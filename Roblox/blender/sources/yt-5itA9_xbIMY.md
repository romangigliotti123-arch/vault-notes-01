---
type: research-source
id: yt-5itA9_xbIMY
title: "VC With Paribes (LIVE)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=5itA9_xbIMY"
published: "2021-12-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0036
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-5itA9_xbIMY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic livestream (Dec 2021) about hand-rigging a Roblox avatar in Blender. No blender-mcp, bpy, Claude, or Roblox export/import content. Covers IK setup (pole target at 180 degrees), merge by distance and subdivision modifiers, deleting unused materials via Outliner Blender File mode, and remarks that Blender 2.79 made a rig and the Blender Game engine was removed. Mostly chat and tangents.

## Claims
- c1: [14:46] Speaker placed IK pole target at the side of the leg rather than the front; later set pole angle to 180 degrees to fix a broken IK. *(demo, low; rigging-animation)*
- c2: [30:13] Unused materials can be deleted by switching Outliner display mode to Blender File, opening Materials, and right-clicking Delete; no shortcut exists for this. *(demo, medium; other)*
- c3: [35:03] Speaker uses Alt+P (clear parent) when unparenting bones before re-parenting. *(demo, low; rigging-animation)*
- c4: [31:35] Speaker says the Blender rig used was made in Blender 2.79, not 2.8 as commonly assumed. *(opinion, low; other)*
- c5: [45:58] Speaker says Blender Game engine was removed in the 2.8 era; a fork (UPBGE) continues it and is on Steam. *(opinion, low; other)*
- c6: [25:27] Speaker says switching texture interpolation from Closest to Smart (or Linear) reduced pixelation for low-res textures; Smart looked blurry to them. *(opinion, low; mesh-texture-limits)*
- c7: [8:33] Speaker added Subdivision Surface modifier after merge by distance and dissolve; says it does not hurt performance as far as they know. *(opinion, low; mesh-texture-limits)*

## Numbers
- n1: **Pole angle**: 180 degrees Set to fix IK in custom avatar rig; speaker's own attempt
- n2: **GFX render resolution**: 8K Christmas GFX renders, not relevant to pipeline

## Techniques
- t1: **Cleanup before modifiers**: Select edges, dissolve, then Merge by Distance to remove duplicate vertices; then add Subdivision Surface and normals modifiers.
- t2: **Purge materials via Blender File view**: Outliner display mode set to Blender File; expand Materials; right-click unused material and Delete.
- t3: **IK pole target placement**: Place pole target to the side of the leg; if IK flips, set pole angle to 180 degrees.

## Quotes (brief, for attribution)
> you can delete them by just right click delete there's no shortcut for some reason  (at 30:13, Comix Productions)

## Points to
- blender.org
- upbge (Blender game engine fork, Steam)
