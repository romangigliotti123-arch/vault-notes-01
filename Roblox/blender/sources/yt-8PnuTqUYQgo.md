---
type: research-source
id: yt-8PnuTqUYQgo
title: "I Gave My AI Assistant an Anime Body - Full 3D Workflow"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=8PnuTqUYQgo"
published: "2026-08-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-8PnuTqUYQgo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Anime 3D character workflow: AI-generated low-poly parts (Tripo-style), Blender merge and retopo, manual UV seams, AI texturing, Mixamo rig with added spring bones and colliders, VRM add-on export with MToon outline, Faceit blendshapes, then running the VRM in a desktop AI companion app. No Roblox content, no bpy scripting, no mcp usage. Sponsor and course promotion omitted.

## Claims
- c1: [2:16] Low-poly AI generation tool used; head generated at 5000 triangles, retopo to 6000 triangles for a sculpted high-poly version. *(demo, medium; other)*
- c2: [4:59] In Blender, Ctrl+L selects connected parts by delimiter, which speeds selection on logically split AI meshes. *(experience, medium; other)*
- c3: [4:18] Textures withheld until geometry is final because merging vertices or dissolving faces would ruin the UV map. *(experience, medium; mesh-texture-limits)*
- c4: [11:29] Mixamo rig used for VRM; its bones are auto-detected by the VRM add-on, while Auto-Rig Pro's larger skeleton is harder to match to VRM requirements. *(experience, medium; rigging-animation)*
- c5: [13:29] Extra physics bones added for braids, cape and accessories because VRM spring bones need separate bones; weights set to 100% for crown. *(experience, medium; rigging-animation)*
- c6: [16:53] Spring bones need colliders attached to bones (e.g., head, body) so braids and cape do not pass through the mesh. *(experience, medium; rigging-animation)*
- c7: [14:50] VRM add-on for Blender is installed by drag and drop; VRM version 0 vs 1 choice matters depending on the target tool. *(experience, medium; other)*
- c8: [19:31] Enabling VRM MToon shader on a material and setting outline mode from None to World Coordinates gives the anime outline. *(demo, medium; other)*
- c9: [17:30] Faceit add-on creates facial shape keys; they must also be mapped in VRM blend shape proxy to be recognized by other software. *(experience, medium; rigging-animation)*
- c10: [24:04] Author used Claude to fork the AIRI desktop app and add animation features by prompting, without 3D-specific instructions; it also loaded a GLB animated object (paint cans) into the scene. *(experience, medium; claude-blender-ai)*
- c11: [8:38] Author says manual UV unwrapping with seams is simple; AI unwrap in Hunyuan 3D Studio is random in results. *(opinion, low; other)*

## Numbers
- n1: **head low-poly triangle count**: 5000 tris 
- n2: **retopo target polycount**: 6000 polys (author: 'more than enough') 
- n3: **texturing time for whole character**: just under 1 hour 
- n4: **Faceit setup time after learning**: about 30 minutes per character (author estimate) 

## Techniques
- t1: **Ctrl+L delimiter selection**: In Blender edit mode on a low-poly AI mesh, select one area and press Ctrl+L to select all connected faces by delimiter, then clean geometry.
- t2: **Physics bone add-on setup for VRM**: Add extra bones for hair, cape, accessories; paint weights; assign them as VRM spring bones; set physics settings; add colliders on head and body.
- t3: **MToon outline setup**: Select material, enable VRM MToon shader, set outline mode from None to World Coordinates, adjust width.
- t4: **Projection then patch texturing**: Add reference image, select view, generate; use patching with a selected area and a second reference view to fix seams and artifacts.

## Quotes (brief, for attribution)
> If you're not going to add this collider, the braids basically go through the head.  (at 16:53, Stefan 3D AI)

## Points to
- VRM add-on for Blender
- Mixamo
- Faceit (Blender add-on)
- VC face
- Project AIRI
