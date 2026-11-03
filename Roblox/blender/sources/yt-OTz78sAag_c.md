---
type: research-source
id: yt-OTz78sAag_c
title: "Reusable COMPOSITOR! - Blender Today LIVE #261"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=OTz78sAag_c"
published: "2025-06-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0071
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-OTz78sAag_c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #261 (June 2025) covers Blender 5.0 dev changes. Almost nothing targets Roblox, blender-mcp, Claude, or bpy pipelines. Scripting-relevant items: data-block names raised from 64 to 256 bytes, GPU API cleanup breaking Python add-ons, deprecated BGL API removed, and 5.0 .blend files open only in 4.5 (not 4.4) without a save-down step.

## Claims
- c1: [21:51] Blender 5.0 raises data-block ID name limit from 64 to 256 bytes (objects, materials, meshes); requested by script users hitting 64-char limit. *(doc, high; automation-and-creator-workflows)*
- c2: [22:32] Opening 5.0 data with long names in Blender 4.5 causes name truncation via conversion. *(doc, medium; automation-and-creator-workflows)*
- c3: [1:40] Blender 5.0 .blend files won't open in 4.4 or earlier; 4.5 acts as bridge: open in 4.5 and re-save to reach older versions. *(doc, high; claude-blender-ai)*
- c4: [33:23] GPU module API definitions changed in 5.0, breaking Python add-ons and PRs that use the GPU API. *(doc, high; claude-blender-ai)*
- c5: [47:13] Deprecated BGL API fully removed in 5.0 (about 4,500 lines), affecting older bpy/add-on drawing code. *(doc, high; claude-blender-ai)*
- c6: [6:35] New .blend format default in 5.0 allows data blocks over 2 GB, lifting the old few-hundred-million-polygon practical limit. *(doc, medium; mesh-texture-limits)*
- c7: [5:48] Armature automated tests added to Blender source, run nightly or on demand by developers. *(doc, low; automation-and-creator-workflows)*
- c8: [3:03] Blender 5.0 disruption: most add-ons and many blend files expected to break until 5.0 beta; add-on updates encouraged then. *(opinion, medium; other)*

## Numbers
- n1: **ID name length**: 64 -> 256 bytes 
- n2: **Data block size limit**: over 2 GB in new blend format 
- n3: **BGL removal**: ~4,500 lines 
- n4: **Release date**: Blender 4.5 LTS on 15 July 2025 

## Points to
- projects.blender.org
- studio.blender.org
