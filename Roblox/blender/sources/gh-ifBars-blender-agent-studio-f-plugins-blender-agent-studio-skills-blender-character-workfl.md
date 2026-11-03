---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-character-workfl
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-character-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-character-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: medium
tags: ["research-source", "github", "avatar-ugc-accessories", "common-mistakes-fixes", "other", "rigging-animation"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-character-workfl

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill instructions for building, rigging, skinning, animating and exporting Blender characters with deformation and fresh-import validation. Generic to Blender, with VRChat hair-fit and Unity/VRChat/GLB notes. Nothing Roblox-specific: no Roblox scale, limits, import or upload steps.

## Claims
- c1: A mesh plus an armature is not a finished rig; a rigged deliverable also needs deformation evidence at neutral and contract poses. *(doc, high; rigging-animation)*
- c2: Add IK/FK, constraints, corrective shapes or drivers only when they solve a named deformation need. *(doc, high; rigging-animation)*
- c3: Limit vertex influences and normalize weights according to target runtime requirements. *(doc, high; rigging-animation)*
- c4: Validation checks include volume preservation, joint collapse, candy-wrapper twist, clipping, foot/hand contact and unwanted scale/shear. *(doc, high; rigging-animation)*
- c5: Export, then fresh-import into a clean Blender process and compare armature hierarchy, weights, materials, actions, frame ranges, scale and orientation. *(doc, high; common-mistakes-fixes)*
- c6: Apply or deliberately preserve transforms before skinning and document the choice. *(doc, medium; common-mistakes-fixes)*
- c7: Fit VRChat hair: use median clearance 1-8 mm, p95 at most 15 mm, under 2% gaps over 20 mm, hair-to-cranium width ratio 1.02-1.10. *(doc, medium; avatar-ugc-accessories)*
- c8: A successful GLB import is not proof of runtime avatar compatibility; target-specific validation must be reported. *(doc, medium; avatar-ugc-accessories)*
- c9: Do not align full hairstyle minimum Z to head top, since hanging strands and ponytails make that measurement invalid. *(doc, medium; other)*
- c10: Retrieve species/pose-matched anatomy references (front, profile, three-quarter, close-ups) before building a character. *(doc, medium; other)*
- c11: Static character briefs need form and surface evidence only; do not invent a rig requirement. *(doc, medium; other)*

## Numbers
- n1: **hair fit median clearance**: 1-8 mm 
- n2: **hair fit p95 clearance**: <=15 mm 
- n3: **large gaps**: <2% over 20 mm 
- n4: **hair-to-cranium width ratio**: 1.02-1.10 

## Techniques
- t1: **Contract-based acceptance poses**: Define neutral plus extreme bend per major joint, reach, twist, locomotion/contact and required facial expressions; render each from front, profile, back and close-up; recheck after geometry/material edits.
- t2: **Fresh-export round trip**: Export requested format, import in clean Blender process, compare hierarchy, weights, materials, actions, frame range, scale, orientation.
- t3: **Uniform hair fit script**: scripts/fit_vrchat_hair.py fits largest semantic hair mesh to upper cranium in evaluated world space with one uniform transform for the full hair rig; confirm intersections visually.

## Quotes (brief, for attribution)
> A mesh plus an armature is not a finished rig.  (ifBars)
> Do not align the full hairstyle minimum Z to the head top; hanging strands and ponytails make that measurement invalid.  (ifBars)

## Points to
- references/astra-workflow.md
- references/character-form-review.md
- scripts/fit_vrchat_hair.py
- $blender-agent-studio:blender-animation-workflow
- $blender-agent-studio:blender-asset-validation
