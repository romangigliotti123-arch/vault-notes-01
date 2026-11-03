---
type: research-source
id: gh-elithril-blender-kiln-f-site-assets-src-turntable-turntable_log.md
title: "elithril/blender-kiln/site/assets-src/turntable/turntable_log.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/site/assets-src/turntable/turntable_log.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "other", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-site-assets-src-turntable-turntable_log.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Production log for a glTF/three.js turntable prop in a web project (elithril/blender-kiln), not Roblox. Relevant only as an example of headless scripted Blender modeling without MCP, plus GLB size reduction from 4.40 MB to 73 KB via WebP, Draco and 512 px textures.

## Claims
- c1: Model was built by a script run headless via blender -b --factory-startup --python-exit-code 1 on Blender 5.2.2 LTS, not over MCP, to avoid touching a live Blender session holding another project. *(doc, high; bpy-scripting-headless)*
- c2: Author chose not to use the MCP-connected live Blender because it held an unrelated open project (diorama.blend); left untouched. *(doc, high; claude-blender-mcp)*
- c3: Review renders were produced by a separate script (review_render.py) using EEVEE from two opposite angles, replacing screenshots. *(doc, medium; bpy-scripting-headless)*
- c4: Top-face PBR came from Poly Haven rubberized_track (CC0): roughness and normal from scan, colour from grain tinted charcoal. *(doc, medium; texturing-baking-uv)*
- c5: Near-white render of a dark texture was caused by review light at 900 W, not the asset; re-lit at 110 W fixed it. *(doc, medium; common-mistakes-fixes)*
- c6: Scripted cleanup: bevels applied as geometry, merge by distance, normals recalculated, sharp edges from 35 degrees. *(doc, medium; other)*
- c7: Optimisation reduced GLB from 4.40 MB to 437 KB via WebP and Draco, then to 73 KB by resizing textures to 512 px; no geometry simplified; 1,912 triangles. *(data, high; roblox-mesh-limits)*
- c8: Draco-compressed GLB requires a decoder on the client side. *(doc, high; other)*

## Numbers
- n1: **GLB file size**: 4.40 MB -> 437 KB -> 73 KB (72,696 bytes final) WebP + Draco, then textures resized to 512 px
- n2: **Triangles**: 1,912 final turntable GLB, no geometry simplified
- n3: **Review light power**: 900 W -> 110 W dark texture read as near-white under 900 W light
- n4: **Sharp edge angle**: 35 degrees scripted cleanup before export

## Techniques
- t1: **Headless scripted build**: Run blender -b --factory-startup --python-exit-code 1 with build script; keep any live MCP-connected Blender session untouched.
- t2: **Texture downscale for small on-screen prop**: Resize textures to 512 px and re-export compressed GLB to cut size from 437 KB to 73 KB.

### Code: Headless Blender batch run used for scripted modeling (no MCP)
```bash
blender -b --factory-startup --python-exit-code 1 --python build_turntable.py
```

## Points to
- polyhaven.com/a/rubberized_track
