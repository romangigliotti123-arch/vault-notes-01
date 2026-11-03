---
type: research-source
id: web-d9159bc56c
title: "DevForum thread 245052"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/245052"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "procedural-generation", "roblox-export-settings", "roblox-import-pipeline"]
---
# web-d9159bc56c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
2019 DevForum thread (#245052) about Roblox Studio mesh imports that sometimes show only a standard MeshPart with no mesh. Replies are anecdotal: retry the upload, export FBX from Blender, apply Solidify, and use the multi-mesh splitting feature. Mostly duplicates an older thread. Nothing on Claude, blender-mcp, or bpy scripting.

## Claims
- c1: Intermittent failure: after importing a mesh into Studio, only a standard MeshPart appears and the mesh is missing. Reported as sometimes happening, sometimes not. *(experience, medium; roblox-import-pipeline)*
- c2: Reply suggests retrying the import because some meshes fail to load on the first attempt; one user reports the upload only works after clicking 'no' on a prompt. *(experience, low; common-mistakes-fixes)*
- c3: Reply suggests exporting from Blender as FBX (File > Export, not Import) and saving the file before uploading. *(opinion, low; roblox-export-settings)*
- c4: Reply recommends applying a Solidify modifier in Blender to meshes before export, presented as a helpful habit with no measured effect. *(opinion, low; procedural-generation)*
- c5: Roblox staff added mesh splitting for multi-mesh file uploads around Feb 2019, cited as the way to import multiple meshes from one file. *(doc, medium; roblox-import-pipeline)*
- c6: Thread was closed as a duplicate of an earlier 'have to upload twice for mesh to show' thread (devforum 230108). *(doc, high; common-mistakes-fixes)*

## Numbers
- n1: **Date of mesh splitting feature**: about 2 weeks before 2019-02-25 (~2019-02-11) Stated by a reply as a recent staff addition

## Techniques
- t1: **Retry mesh upload**: If the mesh does not appear after import, import again; some meshes only load on a second attempt. Reported by users, not verified.
- t2: **Blender FBX export before upload**: Export the model from Blender as FBX and save the file first, then import into Studio. Forum suggestion.
- t3: **Solidify before export**: Apply Solidify modifier to thin meshes in Blender, then export. Forum suggestion, no evidence given.

## Quotes (brief, for attribution)
> the mesh that should have been imported is nowhere to be seen; all that's visible is just the standard mesh part.  (devforum.roblox.com)
> if mesh won't load for the first time, you should try it again, because some meshes won't load immediately.  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/t/have-to-upload-twice-for-mesh-to-show/230108
- https://devforum.roblox.com/t/importing-multiple-meshes-into-studio-from-blender-the-beginners-guide/189214
- https://devforum.roblox.com/t/mesh-splitting-enabled-for-uploading-multi-mesh-files/233783
- https://devforum.roblox.com/t/please-read-before-posting-steps-to-report-a-bug/24388
