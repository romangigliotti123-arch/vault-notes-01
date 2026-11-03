---
type: research-source
id: web-c0edb6a948
title: "DevForum thread 3125992"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/3125992"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "other", "roblox-import-pipeline", "roblox-mesh-limits"]
---
# web-c0edb6a948

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum thread (Aug 2024) about FBX character rig failing Import 3D with 'Upload failed' status 400/-1 errors. Suggested triangle-limit cause disputed. Mesh resize, Studio restart, export settings did not help. Import succeeded intermittently; a network change (Ethernet, closing apps) coincided with success. No confirmed fix. Off-topic to Claude/bpy tooling.

## Claims
- c1: User reports 'Import Failed' with 'Upload failed. status code: 400' and 'status code: -1' on a custom character rig exported as FBX, with failing mesh names changing between attempts. *(experience, high; roblox-import-pipeline)*
- c2: Reply claims a ~10,000 triangle limit causes import errors; original poster says that limit applies to MeshPart, not Import 3D, which uses per-piece meshes under 20k triangles. *(opinion, low; roblox-mesh-limits)*
- c3: Resizing the mesh in Blender, restarting Studio and changing Blender export settings did not fix the 400 upload error for the poster. *(experience, medium; common-mistakes-fixes)*
- c4: Model imported after a few attempts; after deleting and re-importing the same model to change pivot point, the same upload error returned. *(experience, medium; common-mistakes-fixes)*
- c5: Poster says switching from Wi-Fi to Ethernet, then quitting Discord, Google and Spotify, made the import succeed; the poster has no confirmed cause. *(experience, low; roblox-import-pipeline)*
- c6: Thread was auto-closed 14 days after last reply and has no confirmed root-cause or official fix. *(doc, high; other)*

## Numbers
- n1: **triangle limit (claimed, MeshPart)**: ~10,000 tris 
- n2: **per-piece triangle limit (Import 3D, per poster)**: under 20k tris 

## Quotes (brief, for attribution)
> that limit is for importing using meshpart. I'm importing using "Import 3D" with seperates every lil mesh piece  (devforum.roblox.com)

## Contradictions flagged
- Triangle count (~10k) is the cause of import errors (vs Original poster: limit applies to MeshPart; Import 3D pieces are under 20k and still fail)
