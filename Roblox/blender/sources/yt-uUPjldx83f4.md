---
type: research-source
id: yt-uUPjldx83f4
title: "The Hidden Tokyo Point Cloud Download"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=uUPjldx83f4"
published: "2025-01-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-uUPjldx83f4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox. Shows importing Tokyo LAS point-cloud tiles into Blender via bpy: convert LAS to PLY with Python libs (trimesh, laspy, not bundled with Blender), batch-import PLY, apply scale, merge by distance to cut vertex count, add geometry nodes. No Roblox export, MeshPart, or Claude/MCP content.

## Claims
- c1: [6:08] Blender's bundled Python ships numpy but not the LAS reader; extra packages (laspy-type dependency) must be installed separately to read .las files. *(demo, medium; claude-blender-ai)*
- c2: [6:50] One downloaded Tokyo point-cloud tile had about 6 million vertices; merge by distance at 0.002 reduced it to about 2.5 million. *(demo, medium; mesh-texture-limits)*
- c3: [7:30] Raw point-cloud coordinates sit far from origin; scale applied (Ctrl+A) and origin set to geometry to recenter the mesh. *(demo, medium; mesh-texture-limits)*
- c4: [10:49] Batch script skips LAS files that already have a matching PLY, converts the rest, imports each PLY with the PLY importer at set global scale, joins them, and applies transforms. *(demo, medium; automation-and-creator-workflows)*
- c5: [12:10] Joined point cloud merged with distance 0.02 in the script to keep vertex count manageable; final result about 15 million verts passed to a geometry-nodes setup (mesh to points). *(demo, low; mesh-texture-limits)*
- c6: [8:54] Merge-by-distance and geometry nodes (mesh to points) were used to make the point-cloud tiles usable; the author notes the Python script does the same steps manually. *(demo, low; other)*

## Numbers
- n1: **vertices before merge**: ~6 million 
- n2: **vertices after merge by distance 0.002**: ~2.5 million 
- n3: **import scale used**: 0.1 
- n4: **final vertex count in script output**: ~15 million 

## Techniques
- t1: **Skip-if-converted batch import**: Scan folder for .las; if matching .ply exists skip conversion; else convert via trimesh; import each PLY; collect objects; join; apply transforms; set origin; merge by distance; add geometry nodes.
- t2: **Merge by distance to cut point count**: Edit mode, select all, Merge by Distance at 0.002 (manual) or 0.02 (script); exit edit mode; add Mesh to Points geometry nodes.

### Code: Vertex reduction step used in the manual workflow (Blender edit mode)
```text
Edit mode > select all > Mesh > Clean Up > Merge by Distance, threshold 0.002
```

### Code: Scale/origin fix described in transcript
```text
Ctrl+A apply scale, then Set Origin to Geometry
```

## Quotes (brief, for attribution)
> I had to update this script so I updated the code to look like this, instead of the open3d module I decided to use the trimesh package.  (at 6:08, CG Python)

## Points to
- Medium post by Shakar (LAS to PLY conversion code)
- Reddit post with Tokyo point cloud download clue
- Tokyo city government point cloud map site (Japanese, auto-translate)
- CG Python community (author's paid/free community)
