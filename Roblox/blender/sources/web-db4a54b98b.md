---
type: research-source
id: web-db4a54b98b
title: "DevForum thread 2245171"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2245171"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "web", "creator-workflows", "open-cloud-automation", "roblox-import-pipeline"]
---
# web-db4a54b98b

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum announcement and Q&A for Open Cloud Assets API v1 (2023). Covers the API key and HTTP upload model, three supported asset types (Audio, Decal, Model from FBX), FBX-to-Model as an alternative to the Studio Mesh Importer, and the default FBX import hierarchy. Mostly off-topic for Blender-side work; no Blender MCP or bpy content.

## Claims
- c1: Open Cloud Assets API v1 lets an API key with set permissions create and update assets via HTTP requests. Announced 2023-04-07 as available to everyone. *(doc, high; open-cloud-automation)*
- c2: Initial API supports only three asset types: Audio (mp3, ogg), Decal (bmp, jpeg, png, tga), and Model (fbx). rbxm/rbxmx uploads were not supported at launch. *(doc, high; open-cloud-automation)*
- c3: Roblox staff said rbxm/rbxmx model upload support was coming, but gave no date. Rojo-built rbxm(x) files could be uploaded if supported. *(doc, medium; open-cloud-automation)*
- c4: FBX-to-Model via API is meant as an alternative to the Studio Mesh Importer. It is not a workflow for converting existing Models to FBX. *(doc, high; roblox-import-pipeline)*
- c5: Default FBX upload: scene becomes one Model/package named after the file. Hierarchy mirrors scene; each mesh becomes a unique MeshPart. Returned asset ID is the package; child MeshParts are not uploaded to inventory. *(doc, high; roblox-import-pipeline)*
- c6: Upload is asynchronous: the response returns an operations/<id> path, which is polled via GET /v1/operations/{operationId} to get the asset ID. *(experience, medium; open-cloud-automation)*
- c7: Asset update endpoint PATCH /v1/assets/{assetId} only updates model data at launch. Name and description updates were promised as future work, and moderation status was promised for a later metadata endpoint. *(doc, medium; open-cloud-automation)*
- c8: Per-user reports: a Node-fetch-based JS/TS client got 401 errors while Python worked. A Node.js client using Axios worked. *(experience, low; open-cloud-automation)*
- c9: Groups can upload assets when the API key is created under the group, per a commenter who had not tested it. *(opinion, low; open-cloud-automation)*
- c10: Users wanted this for CI/continuous deployment of Studio models, Tarmac-style asset sync, and automated Blender-to-Roblox pipelines. Repeated re-uploads on every build were flagged as impractical without change detection. *(opinion, medium; creator-workflows)*
- c11: No asset delete endpoint existed at launch; archived assets still show in inventory. Plugin asset type was said to be planned. *(doc, medium; open-cloud-automation)*

## Numbers
- n1: **Supported upload types at launch**: 3 (Audio, Decal, Model/FBX) 
- n2: **Launch date**: 2023-04-07 (initial private beta earlier) 
- n3: **FBX meshes per upload**: each mesh becomes a MeshPart in one Model package 

## Techniques
- t1: **Async upload polling**: Send upload request, receive operations/<id> path, poll the operations endpoint until the asset ID is returned, then use it for further calls.
- t2: **FBX as Mesh Importer substitute**: Export the mesh as FBX and POST to the Assets API as Model; result is a package whose child MeshParts follow the FBX hierarchy.

## Quotes (brief, for attribution)
> The FBX to Model functionality should be interpreted as an Open-Cloud API alternative to the Studio Mesh Importer, which can upload as and update packages.  (devforum.roblox.com)

## Contradictions flagged
- A commenter said groups API already supports asset upload via a group-owned API key. (vs Unverified; commenter stated they had not tried it.)

## Points to
- https://create.roblox.com/docs/reference/cloud/assets-usage-guide
- https://create.roblox.com/docs/reference/cloud/assets/v1
- https://github.com/Sleitnick/rbxcloud
- https://devforum.roblox.com/t/opencloud-assets-api/2298007
