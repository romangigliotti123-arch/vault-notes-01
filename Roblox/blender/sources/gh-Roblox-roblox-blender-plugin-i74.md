---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i74
title: "Roblox/roblox-blender-plugin#74 Couldn't Upload Textures."
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/74"
published: "2025-01-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 3
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i74

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #74 on the Roblox Blender plugin: textures fail to upload or show in Studio, and UVs look broken when they do. OBJ via Studio works but normals break. Maintainer suspects export or cloud API processing; a commenter reports FBX and OBJ work manually, suspecting the cloud API. No fix recorded.

## Claims
- c1: Roblox Blender plugin issue #74 (Jan 15, 2025): textures don't appear in Studio; when they do, UV map is reported broken. Reporter uses Blender 4.3.1. *(experience, medium; blender-roblox-export-import)*
- c2: Reporter says OBJ export imported via Studio's regular importer works, but normals were not correct. *(experience, medium; blender-roblox-export-import)*
- c3: Maintainer (Nightriff) notes the plugin uses FBX during export and upload; asks whether FBX via Studio reproduces, to isolate export vs cloud API processing. *(doc, medium; blender-roblox-export-import)*
- c4: Another reporter found FBX and OBJ both worked when imported manually via Studio, suggesting the fault lies in the plugin's cloud API upload path rather than the export. *(experience, low; automation-and-creator-workflows)*
- c5: No confirmed fix or root cause is recorded in the thread; the issue appears unresolved in the captured comments. *(data, medium; blender-roblox-export-import)*

## Numbers
- n1: **Blender version**: 4.3.1 Reporter's version when texture upload failed

## Techniques
- t1: **Isolation test: compare plugin upload vs manual Studio import**: Export same model as FBX and OBJ, import via Studio's regular importer, and compare with plugin upload to locate fault in export or cloud processing.

## Quotes (brief, for attribution)
> if the textures does show up in roblox studio the UV Map is messed up.  (Roblox)
> The plugin uses fbx during the export and upload process.  (Roblox)

## Contradictions flagged
- Plugin upload path is the suspected fault (FBX/OBJ both fine manually) (vs Maintainer's assumption that export process itself may be at fault)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/74

## Visual notes
Two screenshots attached to the original post (not described in text).
