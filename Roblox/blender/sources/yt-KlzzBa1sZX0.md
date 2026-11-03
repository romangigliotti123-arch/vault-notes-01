---
type: research-source
id: yt-KlzzBa1sZX0
title: "New AI Turns One Image Into an Editable 3D Scene - Rodin WorldGen"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=KlzzBa1sZX0"
published: "2026-09-06"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "youtube", "blender-roblox-export-import", "claude-blender-ai", "other"]
---
# yt-KlzzBa1sZX0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demo of Hyper3D's Rodin WorldGen (web tool): one image is auto- or pin-segmented into editable 3D objects, a 3DGS background is generated, and the result is exported to Blender (via a bundled script that displays splats), Unreal (NanoJS plugin), or USDZ (SimReady). Not about Roblox, Claude, or bpy workflows; relevance to the topic is low.

## Claims
- c1: [6:00] Rodin WorldGen exports 3DGS in two formats (SPZ noted as more optimized) and 3D objects with options such as PBR and shading; no Roblox export path shown. *(demo, high; blender-roblox-export-import)*
- c2: [6:00] Blender cannot natively display Gaussian splats; Rodin supplies a script inside Blender that creates a proxy object to show splats. Presenter did not inspect the script. *(demo, medium; claude-blender-ai)*
- c3: [2:45] SimReady adds physical properties automatically; it can only be exported as USDZ, aimed at robotics simulation. *(doc, medium; other)*
- c4: [3:36] Pose correction is not 100% accurate; in the presenter's test it mostly just placed objects on the ground. *(experience, medium; other)*
- c5: [3:36] 3DGS generation takes up to 10 minutes at highest quality per the tool; presenter observed 15-20 minutes in several tests. FastGen is quicker but lower quality. *(experience, medium; other)*
- c6: [7:26] Scene objects were moved into Unreal Engine using the NanoJS plugin; presenter says it took only a few minutes and splats were optimized. *(experience, low; other)*
- c7: [1:25] Manual mode: user adds an object with pins marking the area to include and exclude; objects can be regenerated, boundaries refined, and extracted images edited. *(demo, high; other)*
- c8: [6:40] Refine option during generation gives better topology for objects. *(demo, low; other)*
- c9: [5:30] Presenter opinion: Rodin is among the top three 3D generators; AI Render is the most complete scene tool he has seen, and it does not charge per click. *(opinion, low; other)*

## Numbers
- n1: **3DGS generation time (highest quality)**: up to 10 min stated; 15-20 min observed 
- n2: **Free trial**: two weeks for newly registered users (per video) 
- n3: **Release date of WorldGen**: August 31 (video dated 2026-09-06) 

## Techniques
- t1: **Splat preview in Blender via bundled script**: Export 3DGS from Rodin WorldGen, run the Blender-side script that Rodin provides, which creates a proxy object that displays the splats; enable shading to view.
- t2: **Pin-based object extraction**: Choose Add New Object, mark area with include pins and exclude pins, generate; repeat per object.

## Quotes (brief, for attribution)
> they do actually have a script inside Blender. It's safe to run.  (at 6:00, Stefan 3D AI)

## Points to
- Rodin / Hyper3D WorldGen (web)
- NanoJS plugin for Unreal Engine
- Unity
- Unreal Engine
- Blender
