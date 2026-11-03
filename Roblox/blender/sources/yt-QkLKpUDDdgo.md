---
type: research-source
id: yt-QkLKpUDDdgo
title: "I Tested The New Higgsfield Blender Plugin"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=QkLKpUDDdgo"
published: "2026-08-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation", "rigging-animation"]
---
# yt-QkLKpUDDdgo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator demo of Higgsfield's Blender extension (v1.5.35): connects a Higgsfield account inside Blender, scene builder from text, Meshy-6 text-to-3D with rig, AI walk animation, Blender render to MP4 then Seedance 2.5 restyle. No Roblox content; relevant only to the Claude/Blender AI-tooling side.

## Claims
- c1: [0:00] Higgsfield now ships a Blender extension that brings its generation tools (scene builder, 3D, animation, image UV texturing, video) into the Blender viewport, as an alternative to running Claude with blender-mcp. *(demo, high; claude-blender-mcp)*
- c2: [6:26] Author says Claude + Blender MCP was used earlier to build high-detail scenes (subway environment with geometry nodes, dark lighting), which he considers slower to build via the Higgsfield extension. *(experience, medium; claude-blender-mcp)*
- c3: [2:26] Install: download Higgsfield-to-Blender 1.5.35 zip from Higgsfield plugins page, drag into Blender to install from disk, click 'Connect to Higgsfield', authorize with a Higgsfield account. *(demo, high; other)*
- c4: [3:07] Connection status is checked via Edit > Preferences > Add-ons, searching 'Higgsfield'. *(demo, high; other)*
- c5: [4:12] Scene builder takes a natural-language prompt (e.g. low poly forest with trees, mountains, lake) and assembles objects, camera and lights into an organised collection in one pass; ~first-pass quality, low poly. *(demo, medium; procedural-generation)*
- c6: [5:32] Higgsfield free mode was used for scene builds; paid subscription required for flagship models listed (Opus 5, Kimi 3, Soul, Grok, etc.). *(demo, medium; creator-workflows)*
- c7: [6:26] Text-to-3D uses Meshy-6 (standard, full rigging option); options include target poly count and symmetry mode; generation took a few minutes and the result imports as armature plus mesh. *(demo, medium; procedural-generation)*
- c8: [8:30] Generated Meshy character arrived with an armature (rig) imported into the scene; imported via the assets panel. *(demo, medium; rigging-animation)*
- c9: [9:05] Text prompt 'animate the rig walking in the forest' produced a walk in ~20 seconds; author observed floating feet and bad hands, needing manual fixes. *(demo, high; rigging-animation)*
- c10: [11:24] Image-to-3D of a car reference produced geometry with no UVs and no materials; scene builder mis-placed a track segment and needed a text correction prompt to fix it, and did not catch the error later. *(demo, high; procedural-generation)*
- c11: [13:27] Scene builder did not detect the track-placement problem when checked; AI output 'is never going to be super perfect' per author. *(demo, medium; common-mistakes-fixes)*
- c12: [13:27] Render workflow: set output folder, frames 1-60, 1920x1080, Workbench engine for fast low-poly preview renders as PNG sequence. *(demo, medium; bpy-scripting-headless)*
- c13: [14:09] Combine PNG sequence via Video Editing sequencer (Shift+A, Image Sequence) and re-output as MP4 before uploading as a video reference. *(demo, high; creator-workflows)*
- c14: [14:49] Seedance 2.5 (spelled C-Dance 2.5 in transcript) video model restyles low-poly render using the uploaded MP4 as motion/camera reference; prompt includes positive and negative fields. *(demo, medium; creator-workflows)*
- c15: [15:30] Author uses a Claude skill ('Blender to Seedance') to generate long reference-matching prompts from the Blender render; the skill is distributed via a free resource link, not verified. *(opinion, low; creator-workflows)*
- c16: [16:12] Seedance output kept the same car and track and even a floating prop from the reference; author judged the clip realistic but says fixes belong in Blender before re-rendering. *(opinion, medium; creator-workflows)*
- c17: [0:40] Higgsfield also offers plugins for After Effects, Premiere, Photoshop, DaVinci, and Figma. *(doc, high; other)*

## Numbers
- n1: **Extension version**: 1.5.35 
- n2: **Render resolution / frames**: 1920x1080, frames 1-60 
- n3: **AI walk animation generation time**: ~20 seconds 

## Techniques
- t1: **Render-to-reference pipeline**: Render Blender scene as PNG sequence (Workbench, 1080p, frames 1-60), assemble to MP4 in Video Editing sequencer, upload as video reference to a video model for restyling.

## Points to
- Higgsfield Blender plugin page (Higgsfield plugins section)
- Meshy (Meshy-6 text-to-3D)
- Blender MCP
- Seedance 2.5
- BlenderKit
