---
type: research-source
id: yt-cM3NJuY_xLc
title: "Fall of Reach - Guide to Epic Sci-Fi for Small Studios — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=cM3NJuY_xLc"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0043
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-cM3NJuY_xLc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Film-production talk on a Halo fan animation (Fall of Reach) made in Blender. Covers pre-production, script/storyboard/animatic workflow, folder structure, and Blender geometry-node tools for missiles, shields and cloth destruction. Does not cover Claude, blender-mcp, bpy scripting, Roblox export, or the Roblox pipeline.

## Claims
- c1: Team uses Blender for storyboard/animatic work; viewport playblast exported as quick MP4 then assembled in timeline for animatic. *(experience, high; other)*
- c2: Folder structure: studio asset library plus per-project folders; shots organized as series > episode > sequence > shot, with layout/render/edit split. *(experience, medium; automation-and-creator-workflows)*
- c3: Production stack: Synology Drive NAS for files, Blender for shots, DaVinci Resolve for editing, remote render workstation accessed via Parsec. *(experience, medium; automation-and-creator-workflows)*
- c4: Missile tool was a Blender geometry-nodes system (not Houdini, deemed too expensive) built by one contractor in a couple of weeks. *(experience, medium; other)*
- c5: Ship destruction done by cutting a mesh section, re-pinning it to the model, and using cloth simulation shot with projectiles to tear it. *(experience, medium; other)*
- c6: Ship light flicker driven by a noise (ink blot) texture plugged into a color ramp controlling emission. *(experience, medium; other)*
- c7: Speaker's opinion: iterate script/storyboard/animatic before Blender layout to avoid redoing work downstream. *(opinion, medium; other)*

## Numbers
- n1: **Episode length**: 20-25 min, about 5 episodes 
- n2: **Team size**: 5 grew to 10, now about 10-15 part-time 
- n3: **Shot numbering**: count by 10 in Excel shot tracker 
- n4: **Time to set up studio**: about 8 months 

## Techniques
- t1: **Playblast animatic**: Export viewport playblast at low res to MP4, pull into editor timeline with audio and notes, iterate animatic version by version.
- t2: **Sphere-within-sphere starfield**: Nested star spheres at different distances give parallax blur when camera whips, selling ship speed.

## Points to
- blender-mcp not mentioned
- Synology Drive
- DaVinci Resolve
- Parsec
- Miro
- Shot Deck
- voices.com
- VFX Process podcast
