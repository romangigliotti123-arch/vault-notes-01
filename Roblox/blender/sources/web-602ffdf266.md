---
type: research-source
id: web-602ffdf266
title: "Roblox docs: avatar/dynamic-heads/validate"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/validate.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "rigging-animation"]
---
# web-602ffdf266

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on dynamic head validation for Marketplace. Covers cage-based landmark projection, FACS pose tests (17 minimum poses for 5 actions), common failure causes (cage overshoot, mesh gaps, intersection, separate eye/mouth meshes), and Avatar Setup auto-generation. Not about Blender, bpy, or Claude workflows directly.

## Claims
- c1: Roblox validates dynamic heads for Marketplace compatibility: outer cage for wearing clothing/accessories and FACS facial animation poses (blink, smile, etc.). *(doc, high; avatar-ugc-accessories)*
- c2: Validation projects facial landmarks from cage vertices onto head mesh, then tests eyes closed, mouth open, and basic happy/sad poses via relative landmark displacement. *(doc, high; avatar-ugc-accessories)*
- c3: Heads require 17 specific FACS poses testing 5 basic actions; validation fails immediately if fewer than 17 are detected, regardless of landmarks. *(doc, high; rigging-animation)*
- c4: Unable-to-project-landmarks failures are usually caused by cage extending beyond head mesh or holes/gaps in head mesh; fix by adjusting the cage. *(doc, high; avatar-ugc-accessories)*
- c5: Cage must not intersect the head mesh; landmark projection expects the cage to sit over the head mesh. *(doc, high; avatar-ugc-accessories)*
- c6: If eyeballs or mouthbags are separate meshes, landmarks may land on them instead of head mesh; widen the cage projection area to fix. *(doc, medium; avatar-ugc-accessories)*
- c7: Avatar Setup auto-generates head cage and FACS animation for character models; output can be downloaded as .gltf and FACS/cage edited in third-party tools. *(doc, high; automation-and-creator-workflows)*
- c8: Non-humanoid heads with blocky or missing eyes/mouths are still projected and validated; FACS animations must displace landmarks in the projected regions. *(doc, medium; avatar-ugc-accessories)*

## Numbers
- n1: **FACS poses required**: 17 minimum poses to test 5 basic actions; fewer fails validation
- n2: **Landmarks in failure example**: 3 example failures where 3 landmarks could not be applied to eye area

## Techniques
- t1: **Cage landmark check**: Place cage vertices over eyes and mouth; keep cage over head mesh without intersecting; close gaps so projection succeeds; ensure FACS poses move landmarks.
- t2: **Avatar Setup then edit**: Submit character without avatar components to Avatar Setup, review generated cage/FACS, download .gltf, edit in modeling tool, resubmit.

## Points to
- https://create.roblox.com/docs/avatar/dynamic-heads/specifications
- https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads
- https://create.roblox.com/docs/avatar-setup/index
- https://devforum.roblox.com/c/bug-reports/10
