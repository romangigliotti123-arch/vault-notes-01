---
type: research-source
id: yt-L9VyjUyIfIs
title: "Hunyan Studio 1.2 - Testing & Answer Questions"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=L9VyjUyIfIs"
published: "2026-01-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0050
relevance: 1
density: low
tags: ["research-source", "youtube", "creator-workflows", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# yt-L9VyjUyIfIs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Livestream Q&A testing Hunyuan Studio 1.2 for AI image-to-3D. Almost no Blender scripting, blender-mcp, or Roblox import content. Covers AI character generation, retopo and texturing in Modiv, FaceIt facial rig in Blender, and a promised but unshown Roblox UGC video. Low relevance to the Claude/bpy/Roblox pipeline.

## Claims
- c1: Hunyuan Studio 1.2 has no subscription; access is by waitlist, with approval expected in about three days per the host. *(opinion, low; procedural-generation)*
- c2: Host's workflow: generate a reference image with Nano Banana, remove background, then image-to-3D; multi-view adds little unless back details are hidden. *(opinion, medium; creator-workflows)*
- c3: [38:23] Modiv textures meshes from a reference image; free plan caps output at 2K, 4K requires subscription. *(doc, medium; texturing-baking-uv)*
- c4: [1:49:24] Host says Modiv is best of tested texturing tools; Tripo texture lacks image attachment and Tripo removed image-generation feature. *(opinion, low; texturing-baking-uv)*
- c5: [1:50:47] Host retopologizes then reduces meshes up to about 17 million polygons, using InstaLOD for decimation. *(experience, low; texturing-baking-uv)*
- c6: [54:20] Host says Modiv texture paint can be fixed by brush-masked regional regeneration; during the stream the layer failed to upscale. *(demo, low; texturing-baking-uv)*
- c7: [55:02] FaceIt Blender add-on produces facial rig from a mask, exporting ARKit 52 blendshapes for VTuber software; host says about 15 minutes learning. *(opinion, medium; rigging-animation)*
- c8: [39:45] Hunyuan model download was about 63 MB and slow due to server latency. *(demo, low; procedural-generation)*
- c9: [1:14:47] Generated AI characters are not topology-suited for animation; host says separate parts (head, body) and retopo before rigging. *(opinion, medium; rigging-animation)*
- c10: [1:02:40] Host says the Roblox UGC creation video is planned for Monday, not shown in this stream. *(doc, low; creator-workflows)*
- c11: [1:18:57] Host says 3D printing optimisation: reduce mesh to about half a million polygons or fewer. *(opinion, low; creator-workflows)*

## Numbers
- n1: **Target poly count for printing**: about 500k or fewer 
- n2: **Pre-decimation polygon count**: up to ~17 million 
- n3: **Model download size**: 63 MB 
- n4: **Modiv texture resolution free vs paid**: 2K free, 4K paid 

## Techniques
- t1: **FaceIt facial rig**: Place mask on mesh in Blender, activate FaceIt add-on, adjust mask, press button to generate rig with ARKit 52 shapes, then export to VTuber software.
- t2: **Reference-image texturing in Modiv**: Optimise mesh, select reference image, disable texture, generate image; paint problem areas with brush and regenerate only the masked region.

## Points to
- Hunyuan Studio (Tencent)
- Modiv
- Tripo
- Meshy
- Rodin
- FaceIt Blender add-on
- Nano Banana
- Top3D AI leaderboard
