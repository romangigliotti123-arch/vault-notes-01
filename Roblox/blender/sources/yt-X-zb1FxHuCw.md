---
type: research-source
id: yt-X-zb1FxHuCw
title: "The Colleagtion: Phygital, Self-Funded and Lightning Fast — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=X-zb1FxHuCw"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 0
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other", "rigging-animation"]
---
# yt-X-zb1FxHuCw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
BCON26 talk by the Colleagtion studio (director/animator Igor, producer Nijat) on merch, brand integrations, and a stop-motion-style Blender pipeline. No mention of Roblox, Claude, blender-mcp, bpy automation, or FBX/glTF export. Only tangential Blender production tips (10 fps, linked data, asset browser).

## Claims
- c1: [12:37] Studio animates at 10 fps, reducing frames to animate and render by about 2.5x, which it calls a major speed gain. *(demo, high; other)*
- c2: [19:41] Studio uses linked library data in Blender, making files about 10 times lighter, and wrote an add-on to auto-create library overrides and add lights to characters. *(experience, medium; automation-and-creator-workflows)*
- c3: [19:01] Team shares assets by connecting a cloud drive to the Blender Asset Browser so library updates reach the whole team. *(experience, medium; automation-and-creator-workflows)*
- c4: [17:34] Studio built custom Rigify samples (hand, eyes, detachable head) to simplify rigs for junior animators, since default Rigify arm twist suits organic bodies, not rigid doll characters. *(experience, medium; rigging-animation)*

## Numbers
- n1: **frame rate**: 10 fps all animations made at 10 fps to cut animation and render work
- n2: **file size reduction**: ~10x lighter claimed effect of linked data in Blender files
- n3: **scene animation time**: 3-5 days time to animate one client video's scenes after animatic

## Techniques
- t1: **Linked data plus library override add-on**: Link character data from a shared asset library, then one-click add-on creates library override and imports character. Add-on also appends light rig from external blend file and parents it to pelvis.
- t2: **Animatic-first production**: Record voice-over in CapCut, build layouts in Blender, edit into animatic, then share with client, sound and modelers; animate scenes while updating edit.

## Points to
- Charlie 3D auto lip sync add-on
- Rigify
- CapCut
- Figma
