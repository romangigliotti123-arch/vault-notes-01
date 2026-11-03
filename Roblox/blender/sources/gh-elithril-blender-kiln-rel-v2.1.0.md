---
type: research-source
id: gh-elithril-blender-kiln-rel-v2.1.0
title: "elithril/blender-kiln v2.1.0: blender-kiln 2.1 — animation, routed by subject"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v2.1.0"
published: "2026-10-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation"]
---
# gh-elithril-blender-kiln-rel-v2.1.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release note for blender-kiln v2.1.0, a Claude/Blender tool that adds animation for rigged subjects, routed by subject type. Covers scripted quadruped idle/walk, UniMate text-to-motion for bipeds and winged creatures, loop-making, and a weld that preserves shading before rigging. Only tangentially about the Roblox pipeline; no Roblox import or export specifics.

## Claims
- c1: Animation route is chosen by subject: keep shipped clips; scripted quadruped idle/walk; hand keys or own clips for other quadruped moves; UniMate text-to-motion for biped or winged; rigid-part keying for articulated objects. *(doc, high; rigging-animation)*
- c2: tools/quadruped.py generates idle and walk cycles for any quadruped on the animation-ready skeleton and reports root speed before export. *(doc, medium; rigging-animation)*
- c3: Scripted quadruped trot, jump, sit and attack were rejected on review and are not shipped. *(doc, medium; rigging-animation)*
- c4: UniMate's quadruped walking was unusable on four test rigs; unimate.py refuses quadrupeds unless --force is passed. *(data, medium; rigging-animation)*
- c5: motion_loop.py makes generated clips seamless: loop seams went from 2.1-9.7x the local frame step raw to 0.5-1.2x after looping. *(data, medium; rigging-animation)*
- c6: A plain merge re-smoothed a faceted low-poly mesh, raising corners bent over 5 degrees from 26.7% to 94.5%; the kiln weld keeps shading. *(data, medium; common-mistakes-fixes)*
- c7: Rigs must be weighted on the welded mesh; on the split mesh the rig tore 12.5 cm at the first pose. *(data, medium; rigging-animation)*
- c8: UniMate runs on Apple Silicon and Blender 5 via a 73-line patch; upstream supports NVIDIA only; optional install is about 3.2 GB. *(doc, medium; procedural-generation)*
- c9: UniMate checkpoints are CC BY-NC 4.0, so non-commercial use only; this matters for selling or UGC use. *(doc, high; creator-workflows)*
- c10: Scripted animation rules include keeping legs at or below 95% of leg length, solving IK pole angles, and driving bones in their own rest frame. *(doc, medium; rigging-animation)*
- c11: Tool is a Claude Code plugin updated via the /plugin menu, not an MCP server or live Blender bridge. *(doc, low; claude-blender-mcp)*

## Numbers
- n1: **loop seam ratio**: 2.1-9.7x raw, 0.5-1.2x looped seam size vs local frame step, motion_loop.py
- n2: **corners bent >5°**: 26.7% -> 94.5% plain merge re-smoothing faceted low-poly mesh
- n3: **rig tear at first pose**: 12.5 cm rig weighted on split mesh instead of welded mesh
- n4: **UniMate install size**: 3.2 GB optional install, only when requested
- n5: **UniMate Blender 5 patch**: 73 lines enables Apple Silicon and Blender 5; upstream NVIDIA only
- n6: **max leg length**: 95% scripted animation rule for leg extension

## Techniques
- t1: **Subject-routed animation**: Classify subject (shipped clips, quadruped, biped/winged, articulated object) and pick the method per class. Scripted cycles are reviewed and measured before export.
- t2: **Seamless loop by blending seam**: Run motion_loop.py on generated clip; measure seam jump vs local frame step; target seam near 1x the frame step.
- t3: **Weld before rigging to keep shading**: Weld mesh with a weld that preserves shading instead of plain merge; weight the rig on the welded mesh to avoid tearing at poses.

## Quotes (brief, for attribution)
> kiln now animates what it rigs — routed by subject, because no single method held up across all of them.  (elithril)
> Its checkpoints are CC BY-NC 4.0 — non-commercial use only.  (elithril)

## Points to
- https://github.com/elithril/blender-kiln
- https://github.com/Friedrich-M/UniMate
- https://github.com/elithril/blender-kiln/compare/v2.0.2...v2.1.0
