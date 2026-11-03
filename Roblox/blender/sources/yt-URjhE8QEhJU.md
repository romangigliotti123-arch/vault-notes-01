---
type: research-source
id: yt-URjhE8QEhJU
title: "Create Anything with 3D AI - Animals, Monsters, Creatures Tutorial"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=URjhE8QEhJU"
published: "2026-09-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0061
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-URjhE8QEhJU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Stefan 3D AI tutorial on making a creature character from AI images: split into parts, generate low/high-poly pieces with Tripo in Lychee Studio, assemble and retopo in Blender, UV and bake normal/AO in Blender or Marmoset, texture in MoonDiff, rig via Animate Anything, Mixamo skeleton with auto weights, or AccuRIG. Mentions Claude Code for procedural animation in Unity/Unreal. Nothing about Roblox export or blender-mcp.

## Claims
- c1: Source has no Roblox export/import, scale, or FBX/glTF settings; it covers AI generation to Blender to rig to animation for a non-Roblox game. *(doc, high; other)*
- c2: Does not use blender-mcp or bpy scripting; Claude Code is used to build procedural animation in Unity and Unreal, with Blender only as a source of assets. *(demo, medium; claude-blender-ai)*
- c3: [23:20] Mixamo auto-rig failed on the creature body; the workaround was exporting the Mixamo T-pose skeleton, placing bones manually, then parenting with automatic weights, which worked. *(experience, medium; rigging-animation)*
- c4: [24:42] Hair and accessories were assigned to follow only the head bone; belly transition weights needed manual fixing after joining the two skeletons. *(experience, medium; rigging-animation)*
- c5: [23:20] Animate Anything produced a rig and idle, walk, and attack animations from a spider template; Mesh to Motion was named as an alternative that can fall short. *(experience, medium; rigging-animation)*
- c6: [25:22] Author says joining two skeletons and fixing weights still requires weight-painting and 3D skill; he calls this the hardest step (opinion). *(opinion, medium; rigging-animation)*
- c7: [11:52] Tripo retopology is run per part with a polygon budget chosen by part size; a head at 5000 faces was rejected in favour of 3000 faces. *(experience, medium; mesh-texture-limits)*
- c8: [12:33] Retopology needed up to three retries per part; he judges Tripo retopology better than Hunyuan retopology (opinion), though Hunyuan keeps model orientation. *(experience, medium; mesh-texture-limits)*
- c9: [6:36] Tripo P2 low-poly output is very sensitive to polygon count; one to three generations at different counts were needed to get a good result. *(experience, medium; mesh-texture-limits)*
- c10: [17:24] Normal map is baked from high poly onto retopo low poly in Blender or Marmoset; ambient occlusion is baked the same way. Blender is called the easiest option (opinion). *(experience, medium; mesh-texture-limits)*
- c11: [15:21] Auto UV tools were judged unreliable; seams were placed by hand, UV Stretch checked for red areas, then packed with UV Packer add-on. *(experience, medium; mesh-texture-limits)*
- c12: [18:45] AI texturing tools can mismatch a supplied normal map; MoonDiff is used for large parts because it respects the normal map, with paid tier unlocking 4K textures only. *(doc, medium; mesh-texture-limits)*
- c13: [9:50] Mirror modifier is used for symmetric parts, so only one side is sculpted and retopologized before mirroring. *(experience, medium; other)*
- c14: [8:43] In Blender sculpt mode, Elastic Wrap, Snake Hook, and Smooth were the main brushes for aligning generated parts; Proportional Editing is an alternative. *(experience, medium; other)*
- c15: [5:15] Generated parts must be separated first; the author says generating the whole creature at once fails, and sometimes regenerates parts up to four or five times. *(experience, medium; other)*
- c16: [29:18] Claude Code, Blender, Unity and Unreal were used over a few hours to build a playable procedural-animation character; he says it was not one-shot and needed several iterations. *(experience, low; claude-blender-ai)*

## Numbers
- n1: **generation iterations**: ~20-25 generations per character concept (author) 
- n2: **variations per image**: regenerated up to 5 times 
- n3: **retopo face budget**: 5000 too high for head; 3000 chosen 
- n4: **retopo retries**: up to 3 per part 
- n5: **shoulder armor regeneration**: 4 attempts 
- n6: **time to playable procedural character**: a few hours of vibe coding 

## Techniques
- t1: **Mixamo skeleton + automatic weights**: Export Mixamo T-pose skeleton, delete mesh, fit bones to the model, select mesh then skeleton, Parent with Automatic Weights, then fix weights at transitions.
- t2: **Hybrid rig join**: Rig human half and spider half separately (AccuRIG, Animate Anything), remove unused legs bones in edit mode, join skeletons, then repair weights.
- t3: **Per-part retopology budget**: Export high-poly parts as OBJ, retopo each in Tripo with face count scaled to part size, disable bake texture, retry if poor.
- t4: **Normal and AO bake**: Select low poly, add high poly as source, create new map, bake normal and ambient occlusion in Blender or Marmoset.
- t5: **Seam and UV check**: Mark seams by hand, unwrap, enable UV Stretch preview in UV editor, reduce red islands, pack with UV Packer.
- t6: **Retopo Flow for fixes**: Use Retopo Flow add-on in Blender with high poly as source to redraw broken low-poly areas.

## Quotes (brief, for attribution)
> Generating such things falls short immediately.  (at 0:00, Stefan 3D AI)
> i tried another approach i actually exported like Mixamo skeleton  (at 24:42, Stefan 3D AI)

## Contradictions flagged
- Mixamo auto-rig failed on the creature body, but the Mixamo skeleton with automatic weights worked well. (vs Author's own earlier step (Mixamo failed))

## Points to
- Lychee Studio
- Tripo P2 / Tripo retopology
- Hunyuan 3D
- Animate Anything
- Mesh to Motion
- Mixamo
- AccuRIG
- Retopo Flow (Blender add-on)
- UV Packer (Blender add-on)
- Marmoset Toolbag
