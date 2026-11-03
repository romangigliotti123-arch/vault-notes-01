---
type: research-source
id: yt-eJg2dosWp3o
title: "I Tested Seedance 2.5's 3D Workflow in Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=eJg2dosWp3o"
published: "2026-08-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-eJg2dosWp3o

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator used Claude Code with Blender MCP (26 tools) to generate a low-poly castle/stair scene with a Claude-made Rigify rig and six camera setups, rendered it to MP4, and used it as a video reference in Higgsfield's Seedance 2.5. Motion artifacts and wall clipping carried over. No Roblox export, bpy script, or Roblox pipeline content is covered.

## Claims
- c1: [0:07] Creator used Claude to generate a Rigify-rigged walking character and low-poly stair scene; Blender MCP connected to Claude showing 26 tools. *(demo, medium; claude-blender-ai)*
- c2: [5:24] Single prompt asked Claude to build a 30-second low-poly castle-on-mountain scene with rigged character and at least six camera setups via Blender MCP. *(demo, medium; claude-blender-ai)*
- c3: [5:24] Generated Claude rig was not professionally rigged; creator noted weird character movement artifacts, e.g. character walking through wall. *(demo, medium; claude-blender-ai)*
- c4: [6:10] Creator added color to low-poly scene so the video model could distinguish references; gray renders may confuse it. *(opinion, medium; claude-blender-ai)*
- c5: [2:26] Blender low-poly MP4 render used as video reference; prompt 'turn the video one into a rendered output of a robot walking up the stairs' preserved rig movement and camera movement. *(demo, medium; claude-blender-ai)*
- c6: [3:49] Changing background via prompt referencing video1 kept character motion and camera; a follow-up Tesla Gigafactory edit lost the camera movement. *(demo, medium; claude-blender-ai)*
- c7: [7:11] Prompt to reference @video1 for camera, framing, timing and character motion, then restyle into knight with materials and lighting; 30s generation cost about 120 credits. *(demo, medium; claude-blender-ai)*
- c8: [8:40] Result: choppy, too-clean character motion and wall clipping carried over from the Blender render; creator said motion could be fixed in Blender. *(opinion, medium; claude-blender-ai)*
- c9: [0:07] Seedance 2.5 claims: 30s per generation (2x Seedance 2.0's 15s), native 4K with 1080p/720p options, up to 50 reference inputs (vs 12 in Gen-1), ~20% better prompt adherence. *(doc, low; other)*
- c10: [1:34] Seedance 2.5 can edit one element (e.g. background, clothing) while keeping the rest of the generated video consistent. *(opinion, low; other)*

## Numbers
- n1: **Blender MCP tools exposed to Claude**: 26 Blender connected in Claude session
- n2: **credits for 30s generation**: ~120 Higgsfield, Seedance 2.5 generation
- n3: **minimum camera setups requested**: 6 castle scene prompt
- n4: **Seedance 2.5 max duration**: 30 s double 2.0's 15 s
- n5: **reference inputs**: 50 (vs 12 in Gen-1) Seedance 2.5 claim

## Techniques
- t1: **Blender-render-as-video-reference**: Build low-poly scene and rig in Blender, render viewport to MP4, upload as video reference, prompt model to reference video1 for camera and motion while restyling.
- t2: **Iterative element swap**: Reference the generated video again and change only background or one element via prompt, keeping character motion.
- t3: **Claude-driven scene build via Blender MCP**: Prompt Claude in terminal (Claude Code) with scene spec: low-poly, rigged character, multiple cameras, duration; Claude builds in Blender, then review and render.
- t4: **Color-coding for reference**: Add distinct colors to parts of low-poly models so the video model can track which element to change.

## Quotes (brief, for attribution)
> Turn the video one into a rendered output of a robot walking up the stairs.  (at 2:26, Aidan Stanik)
> some of the character movements are a little choppy  (at 8:40, Aidan Stanik)

## Points to
- Higgsfield
- Seedance 2.5
- Rigify
- Blender MCP
- Claude Code
