---
type: research-source
id: web-d2119bb0b6
title: "DevForum thread 197600"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/197600"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "roblox-mesh-limits"]
---
# web-d2119bb0b6

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender/Claude/bpy pipelines. A 2018 DevForum Q&A on mesh triangle counts in Roblox. Only concrete item: a quoted 2018 update setting CSG limit to 5k triangles and MeshPart limit to 10k (over-limit uploads fail). Rest is community opinion, with no Blender, export or scripting content.

## Claims
- c1: As of a 2018 update, MeshParts were limited to 10k triangles (up from 5k); meshes over the limit fail to upload. *(doc, high; roblox-mesh-limits)*
- c2: As of the same 2018 update, CSG parts were limited to 5k triangles (up from 3k); over-limit parts are auto-simplified to 5k. *(doc, high; roblox-mesh-limits)*
- c3: Poster reports MeshParts are instanced, so triangle total is not a reliable measure of data cost for unique meshes (opinion). *(opinion, medium; roblox-mesh-limits)*
- c4: Poster says low-poly meshes in a detailed game look off and usually need texture or face tricks to compensate (opinion). *(opinion, low; common-mistakes-fixes)*
- c5: Advice given: no fixed triangle target exists; test in a full server and watch the Performance window (opinion). *(opinion, medium; roblox-mesh-limits)*
- c6: One developer reports a low-poly style game with under 1000 triangles per part and about 70k total triangles showed no issues (anecdote). *(experience, low; creator-workflows)*

## Numbers
- n1: **MeshPart triangle limit (2018)**: 10k (was 5k) 
- n2: **CSG part triangle limit (2018)**: 5k (was 3k) 
- n3: **Anecdotal total scene triangles without issues**: ~70k 

## Quotes (brief, for attribution)
> Mesh parts are now limited to 10k triangles (instead of the old limit of 5k). Parts that go over this limit will fail to upload.  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/t/195604 (linked update post by zeuxcg)
