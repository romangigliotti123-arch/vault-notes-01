---
type: research-source
id: gh-elithril-blender-kiln-rel-v2.2.0
title: "elithril/blender-kiln v2.2.0: blender-kiln 2.2 — /kiln animate"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v2.2.0"
published: "2026-10-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "github", "other", "procedural-generation", "rigging-animation"]
---
# gh-elithril-blender-kiln-rel-v2.2.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release note for elithril/blender-kiln v2.2.0, a Claude Code plugin. Adds "/kiln animate", which runs only the animation phase on a rigged .glb asset. It inspects the rig, folds bone-parented parts into the skin, refuses rigs too coarse to bend, prefers the asset's own clips, and routes by subject. Nothing about Roblox, blender-mcp, or bpy.

## Claims
- c1: /kiln animate runs the animation phase alone on a rigged asset, without the full pipeline; takes a .glb plus clip prompts such as 'walk, idle'. *(doc, high; rigging-animation)*
- c2: Inspects the rig and folds bone-parented parts (eyes, props) into the skin; recognises quadrupeds. *(doc, high; rigging-animation)*
- c3: Stops on a rig too coarse to bend when asked to animate, and offers to rig it properly first. *(doc, high; rigging-animation)*
- c4: Offers the asset's own embedded clips first; author states hand-made clips beat every generator measured. *(doc, medium; rigging-animation)*
- c5: Routes by subject: scripted idle/walk cycles for quadrupeds; UniMate text-to-motion for bipeds and winged creatures (installed on demand, non-commercial weights); keyed parts for articulated objects. *(doc, medium; procedural-generation)*
- c6: Shows every kept clip for review before export. *(doc, high; rigging-animation)*
- c7: Plugin is updated via Claude Code's /plugin menu; routing measurements are unchanged from v2.1.0. *(doc, high; other)*

## Techniques
- t1: **Bone-to-skin folding**: Detect parts parented to bones (eyes, props) and merge them into the skinned mesh before animating.

### Code: Command usage from the release note
```text
/kiln animate SK_Cat.glb walk, idle
/kiln animate dragon.glb "flaps its wings"
```

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v2.1.0
- https://github.com/elithril/blender-kiln/compare/v2.1.0...v2.2.0
