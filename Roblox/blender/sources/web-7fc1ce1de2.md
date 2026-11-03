---
type: research-source
id: web-7fc1ce1de2
title: "DevForum thread 633111"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/633111"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-mesh-limits"]
---
# web-7fc1ce1de2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
2020 DevForum Q&A on whether Roblox counts faces or triangles for performance. Replies agree triangles are the metric, since faces are triangulated on import. Also covers MeshPart LoD (RenderFidelity Automatic), instancing breakers, and a Blender cleanup tip (Merge by Distance, Decimate). No Blender MCP, bpy, or Claude content.

## Claims
- c1: Roblox performance cost is driven by triangle count; face count matters only indirectly because faces are made of triangles. *(opinion, medium; roblox-mesh-limits)*
- c2: Non-triangulated faces are converted to triangles by default, so counting quads is considered pointless. *(opinion, low; roblox-mesh-limits)*
- c3: MeshPart LoD only applies when MeshPart.RenderFidelity is set to Automatic. *(doc, medium; roblox-mesh-limits)*
- c4: Changing MeshId, TextureId, Material or Transparency prevents a MeshPart from instancing with others of the same kind. *(doc, medium; roblox-mesh-limits)*
- c5: No fixed triangle ceiling exists; lag depends on player hardware, optimisation, and texture resolution. *(opinion, medium; roblox-mesh-limits)*
- c6: Reusing meshes, parts or unions is presented as a general optimisation habit for slower machines. *(opinion, low; creator-workflows)*
- c7: In Blender, select all, then Mesh > Clean Up > Merge by Distance (Alt+M) to delete duplicate or unnecessary vertices before reducing polycount. *(experience, medium; common-mistakes-fixes)*
- c8: Blender's Decimate modifier can be used for polygon reduction on imported Studio-made models. *(experience, medium; procedural-generation)*

## Techniques
- t1: **Merge by Distance cleanup**: Enter edit mode, press A to select all, then Alt+M and choose By Distance to remove redundant verts before exporting back to Roblox.
- t2: **Decimate poly reduction**: Apply a Decimate modifier in Blender to reduce polygon count of an imported model.

## Quotes (brief, for attribution)
> Use the triangle count, as it gives a more accurate measurement. Faces can have a range of triangle counts.  (devforum.roblox.com)

## Points to
- https://devforum.roblox.com/t/part-instancing-pre-release-announcement/130333
- https://devforum.roblox.com/t/levels-of-detail-for-mesh-parts/280769
