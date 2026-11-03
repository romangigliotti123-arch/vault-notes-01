---
type: research-source
id: yt-KgOw8kmjKnA
title: "GPT 5.6 Sol + Blender: Full Character Animation"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=KgOw8kmjKnA"
published: "2026-07-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0037
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-KgOw8kmjKnA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator demo of driving Blender character animation and camera moves with GPT 5.6 in the Codex app via the Blender MCP server. Shows a text-only wave prompt scoring poorly (flat hand), then better results when a reference video is uploaded. Covers camera dolly, jump, and fisheye follow-cam scenes. No Roblox export, rig-limit, or asset-pipeline content.

## Claims
- c1: [0:00] Codex app with GPT 5.6 plus a character file and a reference video recreated a dolly-zoom camera scene in Blender in under one minute. *(demo, medium; claude-blender-ai)*
- c2: [4:32] Blender MCP is connected to Codex via Settings > Plugins; add a server named 'Blender' with the command/path pointing to the local Blender MCP file. *(experience, medium; claude-blender-ai)*
- c3: [5:13] Blender MCP install: drag the add-on into Blender (twice), verify under Edit > Preferences > Add-ons. *(experience, medium; claude-blender-ai)*
- c4: [6:25] Text-only prompt 'make the character wave at the camera' produced a flat palm throughout; author rated the wave 40/100 and said reference is needed. *(demo, medium; claude-blender-ai)*
- c5: [8:26] Uploading a short reference video of a wave and prompting to recreate it gave much cleaner arm motion, though it also rebuilt the scene unasked. *(demo, medium; claude-blender-ai)*
- c6: [9:49] Reference-driven wave still had a wrist rotated wrong; fix was pose mode wrist rotation and keyframing, but it snapped back until keyed. *(demo, medium; claude-blender-ai)*
- c7: [10:30] Suggested workflow: generate with Codex, then refine keyframes and the Graph Editor by hand; Codex acts as an assistant rather than a final result. *(opinion, medium; claude-blender-ai)*
- c8: [12:00] Reference-based jump scene on concrete blocks got a decent camera move with motion blur, but text came out upside down and the character blended into block tops. *(demo, medium; claude-blender-ai)*
- c9: [12:43] Fisheye skateboard follow-cam was reproduced; character passes through some objects in Eevee, less visible in Cycles. *(demo, medium; claude-blender-ai)*
- c10: [13:24] Choppy stylized look achieved by lowering the frame rate for a blocky, quick effect. *(demo, low; claude-blender-ai)*
- c11: [3:36] Author uses GPT 5.6 on high effort; claims it can analyze the Blender UI and navigate it via Python-based control. *(opinion, low; claude-blender-ai)*
- c12: [2:14] Character source used was Blender Studio's character library with pro-rigged characters (Storm rig), including non-human rigs. *(experience, medium; other)*
- c13: [3:36] Author sets Codex to full access for non-sensitive Blender project folders; recommends approval for sensitive data. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **time to recreate dolly-zoom scene**: under 1 minute 
- n2: **author score for text-only wave**: 40/100 (opinion) 
- n3: **text-only wave generation time**: about 1 minute 

## Techniques
- t1: **Reference-video-driven animation**: Download a short reference clip, upload it to Codex, prompt to recreate the exact movement in Blender; then fix wrong joints in pose mode and keyframe.
- t2: **Low frame rate stylization**: Lower the scene frame rate to get a choppy, blocky look for stylized motion.

## Quotes (brief, for attribution)
> make the character wave at the camera. Make sure his palm is facing towards the camera  (at 6:25, Aidan Stanik)
> recreate this scene from the GIF inside of Blender with the same character movement waving  (at 8:26, Aidan Stanik)

## Points to
- Codex app
- Blender MCP
- Blender Studio character library
- iCandy reference video library
