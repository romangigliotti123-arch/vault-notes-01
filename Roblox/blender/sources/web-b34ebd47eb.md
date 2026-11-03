---
type: research-source
id: web-b34ebd47eb
title: "DevForum thread 521521"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/521521"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-export-settings", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-b34ebd47eb

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
2020 DevForum thread where a user cannot import Blender models into Roblox Studio; replies offer troubleshooting: check face orientation, decline the location-data prompt, watch mesh size and triangle limits, export FBX at scale 0.01 with selected objects, re-export or rename, and try OBJ. No blender-mcp, bpy, or Claude content. Low relevance, anecdotal.

## Claims
- c1: Import failure fix suggested: check face orientation (flipped normals) and decline the location-data prompt. *(opinion, low; common-mistakes-fixes)*
- c2: Meshes that are too large, or exceed the object/triangle limit, fail to import; the thread cites this as a common cause. *(opinion, low; roblox-mesh-limits)*
- c3: Suggested FBX export settings: File > Export > FBX, Selected Objects checked, scale 0.01. *(opinion, medium; roblox-export-settings)*
- c4: Re-exporting under a different filename, or moving the mesh and re-exporting, reportedly made a failed import appear. Anecdotal, no verified cause. *(experience, low; roblox-import-pipeline)*
- c5: Meshes with vertex paint or Blender materials import grey because the texture is not carried over. *(opinion, medium; texturing-baking-uv)*
- c6: Separate objects can cause an error when not using multiple import; trying OBJ instead of FBX was suggested. *(opinion, low; roblox-import-pipeline)*
- c7: Forgetting to scale the model before export was the original poster's suspected cause; the user then reported that correct FBX export still failed. *(experience, medium; common-mistakes-fixes)*

## Numbers
- n1: **FBX export scale**: 0.01 Suggested scale when exporting Blender mesh as FBX for Roblox

## Techniques
- t1: **FBX export with selected objects at 0.01 scale**: File > Export > FBX; set scale to 0.01; tick Selected Objects; export and retry import.
- t2: **Re-export under new name**: Export the same mesh to a different filename and import again; reported to make the import appear.

### Code: Export settings suggested in thread
```text
File > Export > FBX
Export by FBX -> Scale 0.01
Selected Objects: checked
```

## Quotes (brief, for attribution)
> Make sure it doesn't go over limit or it won't work.  (devforum.roblox.com)
> Also try to import as OBJ rather than FBX  (devforum.roblox.com)

## Contradictions flagged
- Scale 0.01 FBX export is the fix, yet the original poster reported that the correct export still failed. (vs Thread's own outcome; no resolution recorded)

## Points to
- devforum.roblox.com
