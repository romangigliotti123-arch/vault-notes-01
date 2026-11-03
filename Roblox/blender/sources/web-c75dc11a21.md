---
type: research-source
id: web-c75dc11a21
title: "Roblox docs: avatar/dynamic-heads/facs-poses-reference"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/facs-poses-reference.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0685
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories"]
---
# web-c75dc11a21

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox reference for 50 FACS facial poses on dynamic heads, authored in Blender/Maya and mapped in Studio. Marketplace validation requires 17 specific base poses. Explains pose combinations (ChinRaiser+ChinRaiserUpperLip, JawDrop+LipsTogether, MouthLeft vs JawLeft, Tongue poses) to avoid collisions. No Claude/blender-mcp or export settings content.

## Claims
- c1: Marketplace validation rejects avatar heads lacking the 17 required facial base poses. *(doc, high; avatar-ugc-accessories)*
- c2: The 17 required poses: LeftEyeClosed, RightEyeClosed, EyesLookDown, JawDrop, Pucker, Left/RightLipCornerPuller, ChinRaiser, ChinRaiserUpperLip, Left/RightCheekRaiser, Left/RightInnerBrowRaiser, Left/RightLipCornerDown, Left/RightLowerLipDepressor (these are flagged in the doc; the list as flagged totals 21 entries). *(doc, medium; avatar-ugc-accessories)*
- c3: Poses are authored and stored in the head model in Blender or Maya; after import into Studio they can be animated. Only the first neutral pose must be first; order of the rest doesn't matter because mapping is set as a custom property. *(doc, high; avatar-ugc-accessories)*
- c4: ChinRaiser with a closed mouth makes the lower lip collide with the upper lip; use ChinRaiserUpperLip together with ChinRaiser, set to the same value, to avoid it. *(doc, high; avatar-ugc-accessories)*
- c5: LipsTogether at 100% with JawDrop at 100% keeps lips together as the jaw drops; easing LipsTogether in and out opens and closes the lips. *(doc, high; avatar-ugc-accessories)*
- c6: MouthLeft/MouthRight move only the mouth; JawLeft/JawRight also move jaw, teeth, tongue and lower lip. *(doc, high; avatar-ugc-accessories)*
- c7: TongueUp and TongueDown are only visible when combined with TongueOut; otherwise the tongue bends inside the mouth. *(doc, high; avatar-ugc-accessories)*
- c8: Some FACS pose combinations collide unless a corrective pose is added for the combination (see 'combination poses' in create-basic-heads). *(doc, medium; avatar-ugc-accessories)*

## Numbers
- n1: **FACS base poses listed**: 50 
- n2: **Required Marketplace base poses**: 17 Marketplace validation rejects heads missing them

## Techniques
- t1: **Keep lips closed while raising chin**: Set ChinRaiser and ChinRaiserUpperLip to the same value so both lips rise equally and don't collide.
- t2: **Open/close mouth with JawDrop+LipsTogether**: Hold JawDrop at 100%, ease LipsTogether in/out of 100% to open and close lips; both at 100% keeps lips together while jaw drops.

## Points to
- https://en.wikipedia.org/wiki/Facial_Action_Coding_System
- art/characters/facial-animation/create-basic-heads.md
- avatar/dynamic-heads/specifications.md#facs-poses
- art/characters/facial-animation/animate-heads.md
