---
type: research-source
id: yt-QrDt1_Bn670
title: "Blender 4.2 Extensions VS Add-ons Explained"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=QrDt1_Bn670"
published: "2024-07-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "other"]
---
# yt-QrDt1_Bn670

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on Blender 4.2 extensions vs legacy add-ons. Covers the new Get Extensions UI, internet access gating, install methods (platform, drag-drop, zip, local repositories), and developer changes: blender_manifest.toml replaces bl_info, bundled wheels for third-party deps, relative imports, and an extension build command. Not about Roblox, blender-mcp, or Claude.

## Claims
- c1: [0:38] In Blender 4.2, add-on developers replace the bl_info dict with a blender_manifest.toml file in the extension zip; not all fields map one-to-one. *(doc, high; bpy-scripting-headless)*
- c2: [5:56] Extensions with third-party Python dependencies must bundle them, recommended as python wheels referenced by relative path in the manifest; platform-specific wheels per OS. *(doc, high; bpy-scripting-headless)*
- c3: [7:28] Migrating code to extensions requires relative imports for internal modules and replacing the add-on name string in quotes with __package__. *(doc, high; bpy-scripting-headless)*
- c4: [7:28] A new extension build command automates creating extension packages, useful for producing per-platform builds. *(doc, medium; bpy-scripting-headless)*
- c5: [2:07] Blender blocks internet access by default; command-line flags can fully disable it or auto-allow it, intended for studio or education deployments. *(doc, high; other)*
- c6: [3:42] Extensions can be installed from the Get Extensions UI, drag-and-drop from the website, install-from-disk zip, or local user/system repositories of unzipped extensions. *(doc, high; other)*
- c7: [4:34] Former bundled add-ons such as Rigify and Node Wrangler moved to a Core add-ons group on the extensions platform; Images as Planes became a built-in operator. *(doc, high; other)*

## Techniques
- t1: **Legacy add-on to extension migration**: Write blender_manifest.toml replacing bl_info; switch internal imports to relative; replace add-on name strings with __package__; bundle wheels for deps; package as zip with __init__.py and manifest; build with extension build command.

## Points to
- Blender extensions platform
- Blender 4.2 release
