---
type: research-source
id: web-0d34f892df
title: "DevForum thread 1971895"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1971895"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 3
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-0d34f892df

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum thread (2022-2025) on getting high-poly Blender models under Roblox Studio's triangle import limit. OP shows Blender Mesh > Clean Up > Decimate Geometry with ratio below 1 (190k to 19k tris). Replies cover decimate modifier, Smart mesh importer, split-and-merge FBX import, and opinion on the limit. Mostly anecdotal and opinion; little on Claude, bpy, or MCP.

## Claims
- c1: OP says models above roughly 21,000 triangles fail Roblox Studio import and need reduction; a 190k-tri tower was decimated to 19k with little visible quality loss. *(experience, low; roblox-mesh-limits)*
- c2: Decimate Geometry in edit mode needs all vertices selected; if the count does not drop, OP says to recheck steps. *(experience, low; common-mistakes-fixes)*
- c3: Commenter says the triangle import limit has been 20k since 2021 and the 10k figure is outdated; mesh importer accepts up to 20k. *(opinion, low; roblox-mesh-limits)*
- c4: Commenter says the old avatar evolution beta build gave a 50k triangle limit in Studio. *(experience, low; roblox-mesh-limits)*
- c5: Smart mesh importer is suggested as a way around the triangle limit. *(opinion, low; roblox-mesh-limits)*
- c6: Reported: setting a Decimate Geometry ratio keeps the same count for some users; a Decimate modifier added in Blender is suggested instead. *(experience, low; common-mistakes-fixes)*
- c7: Modifiers are preferred for decimation because they are non-destructive, can use vertex groups, and export with Apply Modifiers ticked. *(opinion, medium; creator-workflows)*
- c8: Split a model in Blender so each object is under 10k triangles (check via Overlays > Statistics), then import the FBX and use Merge meshes under File Geometry, yielding one undecimated MeshPart. *(experience, medium; roblox-import-pipeline)*
- c9: Merged single-mesh import needs one texture atlas; the commenter states Roblox enforces a 1k texture limit, so detail quality drops. *(opinion, low; texturing-baking-uv)*
- c10: Merging meshes improves draw call performance versus forced decimation, according to the same commenter. *(opinion, low; roblox-mesh-limits)*
- c11: Commenters argue 10k tris is low for detailed or AAA-style models; one cites Call of Duty weapons near 30k and AAA characters 10k to 60k; another argues 10k is ample with normal maps. *(opinion, low; creator-workflows)*
- c12: A commenter says that for characters, retopology should keep models under 10k tris. *(opinion, low; avatar-ugc-accessories)*

## Numbers
- n1: **Import triangle threshold (OP)**: 21,000+ triangles need reduction 
- n2: **Decimation example**: 190,000 to 19,000 triangles 
- n3: **Limit cited by commenters**: 10k (old); 20k since 2021 (claim); 50k in old avatar beta (claim) 
- n4: **Texture limit cited**: 1k per texture (claim) 
- n5: **Per-object split target before merge**: under 10k triangles each 

## Techniques
- t1: **Blender Decimate Geometry**: Edit mode, select all vertices, Mesh > Clean Up > Decimate Geometry, set ratio below 1 in the bottom-left panel; repeat if count does not drop.
- t2: **Non-destructive Decimate modifier**: Add Decimate modifier instead of destructive decimate; use vertex groups; tick Apply Modifiers on export.
- t3: **Split then merge on import**: Split model into objects under 10k tris each; verify with Statistics overlay; export FBX; in Roblox import apply Merge meshes in File Geometry settings.

## Quotes (brief, for attribution)
> Navigate to edit mode and on the top left click mesh->clean up->Decimate Geometry  (devforum.roblox.com)
> Triangle limit is actually 20k since 2021, not 10k. You can upload meshes with up to 20k triangles using the mesh importer.  (devforum.roblox.com)

## Contradictions flagged
- Triangle import limit is 20k since 2021, not 10k (vs OP and other commenters cite 10k and 21k+ thresholds inconsistently)
- Models above 10k tris are unoptimized and will lag (vs Commenter claiming AAA characters reach 60k and Call of Duty weapons about 30k)

## Points to
- devforum.roblox.com thread 1971895
- Blender Mesh > Clean Up > Decimate Geometry
- Smart mesh importer (Roblox)
- Old avatar evolution beta build
