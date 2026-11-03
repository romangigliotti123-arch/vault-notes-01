---
type: research-source
id: web-88dcbb0fa3
title: "DevForum thread 1566375"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1566375"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 3
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-export-settings", "roblox-import-pipeline"]
---
# web-88dcbb0fa3

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum Q&A (2021): a creator exports a glTF model, converts to FBX with baked animation via Blender, and imports via the Avatar Importer "Custom Rig" option; mesh pinches at points, while the Asset Manager import looks correct. Reply advises setting Armature and Mesh transforms to location 0, rotation 0, scale 1.0 before export. Thin, single-tip thread.

## Claims
- c1: Importing an FBX via Avatar Importer 'Custom Rig' broke the mesh (pinched points) while the same model imported via Asset Manager looked correct. *(experience, medium; roblox-import-pipeline)*
- c2: Fix suggested: set Armature and Mesh object transforms in Blender to Location 0,0,0, Rotation 0,0,0, Scale 1.000,1.000,1.000 before export; otherwise import problems are likely. *(opinion, medium; common-mistakes-fixes)*
- c3: Reporter pipeline: glTF export from source, import to Blender, re-export as FBX with baked animations, then import as Custom Rig. *(experience, low; roblox-export-settings)*

## Numbers
- n1: **Target transform values**: Location 0,0,0; Rotation 0,0,0; Scale 1.000,1.000,1.000 

## Techniques
- t1: **Reset transforms before export**: In Blender, check Object Properties on both the Armature and the Mesh; set location to 0, rotation to 0, scale to 1 before exporting FBX to avoid warped or pinched meshes on import.

## Quotes (brief, for attribution)
> Try making sure that the transform values in blender on both the Armature and the Mesh are set to stock values  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/raw/1566375
