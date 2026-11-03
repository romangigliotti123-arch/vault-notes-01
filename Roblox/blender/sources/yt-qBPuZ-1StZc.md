---
type: research-source
id: yt-qBPuZ-1StZc
title: "Imposter Syndrome — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=qBPuZ-1StZc"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "creator-workflows", "other"]
---
# yt-qBPuZ-1StZc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Talk by Thomas Murphy on "imposter cards," a Blender add-on that replaces high-poly meshes with shader-driven billboard planes using texture atlases, with camera-facing planes and a triplanar mode. Exports to Godot (glTF) and Unity (script). Does not cover Roblox, blender-mcp, or Claude-driven Blender. Includes a brief anecdote about AI-written shader code failing.

## Claims
- c1: [18:47] Speaker asked an AI to write an always-face-camera shader script; the output looked fine but did not work and was not performant. Speaker concludes AI currently does not work well for this kind of task. *(experience, medium; bpy-scripting-headless)*
- c2: [19:28] A second AI attempt, with a request for simpler code, still failed; the speaker's corrected version needed a dot-product scale term so the plane scales with the mesh. *(experience, medium; bpy-scripting-headless)*
- c3: [14:12] Add-on exports imposters to Godot via glTF (easy) and to Unity via a custom script that populates materials and textures (harder). Unreal is dropped because Unreal removed Blueprints mid-development. *(experience, medium; other)*
- c4: [20:50] Imposter add-on works only through Blender: models must be imported into Blender and published from there. It uses up to eight UV levels and stores no mesh properties incompatible with game engines. *(doc, medium; other)*
- c5: [3:38] A single texture atlas card can hold about 10-11 trees via a flipbook X-axis atlas; the earlier approach fails when viewed from top or bottom. *(experience, low; creator-workflows)*
- c6: [13:18] Joining ~200,000 impostors into a single object cut viewport benchmark time to 21 seconds; ray-traced render dropped from 5 minutes to 1 minute 18 seconds on a test scene. *(demo, low; other)*

## Numbers
- n1: **viewport benchmark for joined impostors**: 21 seconds Joined impostor object benchmark for ~200,000 objects
- n2: **ray-traced render time**: 5 min -> 1 min 18 s joined Single-sample render with impostors versus joined impostors

## Points to
- Instant Imposters add-on
- Polyhaven assets
- Godot glTF export
- Unity
