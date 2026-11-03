---
type: research-source
id: yt-TXtDfATbe0M
title: "Blender JAM: A Collective Animation Experiment — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=TXtDfATbe0M"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-TXtDfATbe0M

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Conference jam talk (Friday Lab) on a collaborative 3-person-team animation experiment: modeler/rigger, animator, and compositor pass .blend files via shared team folders, with a 180-frame, 30 fps, Eevee-rendered shot. It does not cover Claude, blender-mcp, bpy scripting, Roblox export, or the Roblox pipeline.

## Claims
- c1: [2:41] Jam teams of three split roles: modeler/rigger, animator, and light compositor, sharing work by overriding files in a numbered team folder. *(demo, high; automation-and-creator-workflows)*
- c2: [4:04] Animation shot was 180 frames at 30 fps (six seconds), with camera and clip pre-set in the template file. *(demo, high; other)*
- c3: [4:45] Compositor renders final output in Eevee for speed, starting from pre-made light presets and compositing node setups. *(demo, medium; other)*
- c4: [6:37] Time budget: 5 min brainstorm, 20 min build, 8 min assemble/upload/download/render. *(demo, medium; automation-and-creator-workflows)*
- c5: [28:07] Advice: keep all added models and objects inside the designated collection so teammates' files stay consistent when overridden. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **animation length**: 180 frames, 30 fps, 6 s 
- n2: **jam time budget**: 5 min brainstorm, 20 min build, 8 min assemble 

## Techniques
- t1: **Shared-folder file handoff**: Each team uploads its .blend to its numbered folder; teammates download and override local copies to pull the latest model, rig, or clip. Keep object names and collections unchanged so links still resolve.
