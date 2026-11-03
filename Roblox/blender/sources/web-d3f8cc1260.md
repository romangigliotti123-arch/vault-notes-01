---
type: research-source
id: web-d3f8cc1260
title: "DevForum thread 2646338"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2646338"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-import-pipeline"]
---
# web-d3f8cc1260

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum Q&A (Oct 2023): a Blender mesh failed to import into Roblox after FBX, GLB and OBJ export, and the pivot reset did not help. A replier said a flat plane in the model makes the whole mesh import as infinitely small pieces. Removing the plane was suggested, and a stray faceless circle reportedly corrupted another import. Thread auto-closed after 14 days.

## Claims
- c1: A flat plane (zero-volume face) left in a mesh can make the whole model import into Roblox as infinitely small meshes. *(experience, medium; common-mistakes-fixes)*
- c2: Suggested fix: delete the plane/flat geometry before export; poster had not confirmed it worked at time of thread. *(opinion, low; common-mistakes-fixes)*
- c3: A stray circle with no faces (edge loop only) reportedly corrupted an entire Roblox import. *(experience, low; common-mistakes-fixes)*
- c4: Heuristic: if the object is not fully 3D (has no volume), it is a plane. No tool or menu check was named. *(opinion, low; common-mistakes-fixes)*
- c5: Export failed in the poster's case across FBX, GLB and OBJ, so the problem was in the geometry, not the export format. *(experience, medium; roblox-import-pipeline)*
- c6: Resetting the pivot did not resolve the broken import in this case. *(experience, medium; common-mistakes-fixes)*

## Techniques
- t1: **Remove stray flat geometry before export**: Inspect the mesh for faces with no volume or stray edge loops with no faces. Delete them, then re-export to FBX/GLB/OBJ and re-upload to Roblox.

## Quotes (brief, for attribution)
> You may have a plane in the model. That causes the entire model to show up as infinitely small meshes  (devforum.roblox.com)
> If it isnt 3d its a plane.  (devforum.roblox.com)
