---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-animation-workfl
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-animation-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-animation-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: medium
tags: ["research-source", "github", "common-mistakes-fixes", "creator-workflows", "rigging-animation"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-animation-workfl

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill doc for authoring and reviewing Blender animation of mechanical props, articulated assemblies and humanoid motion. Covers semantic phases, pivot placement, endpoint-based connectors, validation renders, and checking exported GLB action frame ranges. Mentions a Mixamo FBX-to-.blend import tool. Does not cover Roblox import or export settings.

## Claims
- c1: Mixamo workflow uses blender_prepare_mixamo_search for browser handoff and blender_import_mixamo_animation to turn downloaded FBX into a standalone animated .blend. *(doc, high; rigging-animation)*
- c2: Applying Mixamo motion to a different rig requires a separate compatibility or retargeting workflow; live catalog access needs host browser tools. *(doc, high; rigging-animation)*
- c3: Rebuild or key dynamic connectors (cables, hoses, pistons, link rods) from their two evaluated endpoints at each critical frame; compute moving attachments from local anchors transformed by the assembly's matrix_world. *(doc, medium; rigging-animation)*
- c4: Use linear interpolation for mechanically constant motion and clamped Bezier handles for eased human-visible motion. *(opinion, medium; creator-workflows)*
- c5: An animation is not accepted solely because keyframes and actions survived export; validate by rendering critical frames from at least two cameras and the full action to video. *(opinion, medium; creator-workflows)*
- c6: Avoid never-rotate-world-point-around-origin shortcuts for hinges; pivots must sit on actual hinge or rotation axes. *(doc, medium; common-mistakes-fixes)*

## Techniques
- t1: **Endpoint-driven connector rebuild**: Compute each moving attachment from local anchor times owning assembly matrix_world; rebuild connector from two evaluated endpoints at each critical frame; assert endpoint error numerically before rendering.

## Points to
- references/astra-workflow.md
- references/mixamo.md
- references/mechanical-animation.md
- $blender-agent-studio:blender-asset-validation
