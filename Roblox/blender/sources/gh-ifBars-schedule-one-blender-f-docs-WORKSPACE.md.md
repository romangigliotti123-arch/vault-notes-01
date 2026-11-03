---
type: research-source
id: gh-ifBars-schedule-one-blender-f-docs-WORKSPACE.md
title: "ifBars/schedule-one-blender/docs/WORKSPACE.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/docs/WORKSPACE.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "github", "mesh-texture-limits", "other"]
---
# gh-ifBars-schedule-one-blender-f-docs-WORKSPACE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Local workspace guide for a Schedule I (Unity game) Blender map reference: .blend variants, 512px packed textures, 1 Blender unit = 1 m, Unity (x,y,z) to Blender (x,z,y) axis swap, 0.5m near clip. Does not cover Roblox, blender-mcp, Claude, bpy scripting, or Roblox export. Off-topic for the target subject.

## Claims
- c1: Source is about Unity game Schedule I map reference files, not Roblox Studio; no Roblox export, MCP, or Claude content. *(doc, high; other)*
- c2: Blender unit equals one metre; Unity (x,y,z) maps to Blender (x,z,y) for coordinate conversion. *(doc, high; other)*
- c3: Axis swap reverses handedness; importer adjusts winding and normals, so do not apply a second conversion if exporter already does it. *(doc, medium; other)*
- c4: Reference workspace uses 512px packed textures in the everyday file; full-detail file keeps original texture sizes. *(doc, medium; mesh-texture-limits)*
- c5: Terrain blend maps hold four independent weights and must use Non-Color + Channel Packed; never resize as transparency. *(doc, medium; mesh-texture-limits)*

## Numbers
- n1: **Blender unit scale**: 1 unit = 1 m 
- n2: **Near clip distance**: 0.5 m 
- n3: **Packed texture size (everyday file)**: 512 px 
- n4: **Recommended RAM for opening both .blend files**: 32 GB machine, avoid opening both at once 

## Techniques
- t1: **Unity to Blender axis conversion**: Map Unity (x,y,z) to Blender (x,z,y). Apply inverse once when exporting game coordinates. Skip if exporter already converts.

## Quotes (brief, for attribution)
> One Blender unit is one metre. Unity (x,y,z) maps to Blender (x,z,y); apply the inverse once when exporting game coordinates.  (ifBars)

## Points to
- docs/EXPANSIONS.md
