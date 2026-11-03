---
type: research-source
id: web-aa3c5b4431
title: "DevForum thread 1078816"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1078816"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0037
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-aa3c5b4431

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum tutorial for a basic top hat made from two cylinders in Blender (modelling, UV unwrap, painting a texture), then exported to Roblox Studio. Manual GUI workflow only: no Claude, blender-mcp, or bpy scripting. Covers OBJ export, MeshPart import, and decal upload for TextureID. Thin on pipeline specifics; no numeric UGC limits given.

## Claims
- c1: Author exports the hat as Wavefront .obj from Blender, then imports it into a MeshPart via the Properties folder button in Studio. *(demo, high; roblox-import-pipeline)*
- c2: Commenter suggests exporting FBX; author replied that .fbx automatically carries the texture over, unlike .obj, and said the tutorial would be updated. *(opinion, medium; roblox-import-pipeline)*
- c3: Texture is painted in Blender Texture Paint after Smart UV Project with island margin changed from 0 to 1, then saved via Image > Save As. *(demo, high; texturing-baking-uv)*
- c4: Texture must be uploaded as a Roblox decal and its asset ID pasted into TextureID in Studio properties. *(demo, high; texturing-baking-uv)*
- c5: Author says a two-cylinder top hat is easy to keep under UGC Program size limits; no numeric limits are given. *(opinion, low; roblox-mesh-limits)*
- c6: After import the hat may need rotating to match the dummy's facing, scaling down, and centring on the head. *(demo, high; common-mistakes-fixes)*
- c7: Test dummy comes from the preinstalled Rig Builder plugin pack; a new MeshPart is placed on its head before importing. *(demo, medium; roblox-import-pipeline)*

## Techniques
- t1: **Smart UV Project unwrap**: Select all vertices in edit mode, press U, choose Smart UV Project, set island margin to 1, then paint face regions in Texture Paint.

## Contradictions flagged
- Step 7 instructs uploading the painted texture as a decal and pasting its ID into TextureID. (vs Reply #6 says .fbx automatically carries the texture, so the separate decal step is unnecessary with FBX.)

## Points to
- https://devforum.roblox.com/raw/1077232
- https://www.blender.org/
- https://www.roblox.com/develop?View=13
