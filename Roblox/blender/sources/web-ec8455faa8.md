---
type: research-source
id: web-ec8455faa8
title: "DevForum thread 1615354"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1615354"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "roblox-import-pipeline"]
---
# web-ec8455faa8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum thread (2022) on Roblox mesh importer showing File Dimensions inf,inf,inf and transparent meshes for FBX files exported from Blender after importing SketchUp COLLADA models. Replies give a workaround: find and remove the empty or extraneous-point mesh, re-export. Also advises against SketchUp 3D Warehouse assets. Little on bpy or Claude.

## Claims
- c1: Blender-exported FBX imported via the beta mesh importer showed File Dimensions inf,inf,inf and rendered transparent, across many files from SketchUp 3D Warehouse COLLADA sources. *(experience, medium; common-mistakes-fixes)*
- c2: Reported fix: locate the object giving inf/-inf position (a mesh with no vertices), delete it in Blender, re-export FBX; original poster said it worked for them. *(experience, medium; common-mistakes-fixes)*
- c3: Asset Manager can be used to find the mesh with no vertices causing the unified mesh importer failure. *(opinion, low; roblox-import-pipeline)*
- c4: Check for extraneous points and empty geometry by re-importing the FBX into Blender before sending it to Roblox. *(opinion, medium; common-mistakes-fixes)*
- c5: Advice: avoid SketchUp 3D Warehouse assets, which are typically unoptimized and have severe topology issues. *(opinion, medium; creator-workflows)*
- c6: Another replier suggested simply reuploading the mesh; no evidence given that it resolves the inf dimensions. *(opinion, low; common-mistakes-fixes)*

## Numbers
- n1: **File Dimensions reported**: inf,inf,inf 

## Techniques
- t1: **Isolate empty mesh**: Inspect the imported object list for the one with inf position or no vertices, remove it in Blender, re-export FBX, re-import into Roblox.

## Quotes (brief, for attribution)
> find the mesh that has no vertices. This mostly bug out the whole unified mesh importing system.  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/raw/1615354
