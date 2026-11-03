---
type: research-source
id: yt-0P3AMPijKrY
title: "How To Create INSANE Scenes In Blender + GPT-6 Astra + Higgsfield"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=0P3AMPijKrY"
published: "2026-09-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0036
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "other"]
---
# yt-0P3AMPijKrY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video by Aidan Stanik on driving Blender from GPT-6 Astra in Codex, using computer use plus Python scripting, then a previz-to-video handoff to Seedance 2.5 via the Higgsfield Blender add-on. Nothing on Roblox, Studio, or the Roblox export pipeline. Blender-to-AI-video workflow only; the Claude-specific claims are thin.

## Claims
- c1: [5:32] Creator says GPT-6 Astra computer use can click Blender UI and build scenes, and that a Blender MCP is unnecessary for this. Opinion, single demo. *(opinion, low; claude-blender-mcp)*
- c2: [6:15] Simple cabin built from one prompt in a blank Blender session via computer use; output was a basic orthographic scene the creator says he would not use himself. *(demo, medium; claude-blender-mcp)*
- c3: [7:35] Codex writes Python into Blender's Scripting tab to create objects, and uses computer use only for viewport and render output settings. *(demo, medium; bpy-scripting-headless)*
- c4: [9:40] previz-to-seedance skill runs in phases: interview, Blender build (MCP if installed, otherwise computer use), character sheets, video prompt, delivery via Higgsfield. *(demo, medium; claude-blender-mcp)*
- c5: [16:34] Higgsfield Blender add-on installed by dragging the zip into the viewport, authorizing in a browser, then enabling it under Preferences > Add-ons; panel opens with N key. *(demo, medium; other)*
- c6: [17:16] Higgsfield add-on can drive the Blender camera from a phone scanning a QR code and recording the movement. *(demo, medium; other)*
- c7: [14:38] Creator found the reference-driven video stiff and rigid, so the master prompt asks for natural character motion while keeping the camera move. Reason given: stiff output wastes credits. *(experience, medium; other)*
- c8: [20:12] Final Seedance 2.5 output kept the camera and environment, but the creator says it still looked like a Blender render rather than realistic. *(experience, medium; other)*
- c9: [4:16] Creator keeps the Blender project in a separate folder from other AI projects (with a .claude skills folder) and gives it full access. *(experience, medium; creator-workflows)*
- c10: [2:11] Creator opinion: GPT-6 Astra beats the Anthropic model he names as Fable 5.1 for creative taste, while Fable 5.1 does well at Blender modeling. No benchmark shown. *(opinion, low; claude-blender-mcp)*

## Numbers
- n1: **shot length**: 15 seconds 
- n2: **community size**: over 3.2 thousand members (creator's own community) 

## Techniques
- t1: **Computer-use scene build**: Open a blank Blender session, prompt the agent to build the scene in the open viewport, and let it control the GUI. No MCP addon required, per the creator.
- t2: **Blender previs to AI video**: Build a simple viewport scene and character block, render it as an MP4 reference, then feed that video plus environment and character-sheet images into the video model with a timed prompt.
- t3: **Higgsfield add-on generation**: Install the add-on zip, authorize, enable it in Add-ons, use the N panel, select the video model, upload reference video and images, then generate inside Blender.

## Quotes (brief, for attribution)
> you don't even need a Blender MCP anymore because the computer use is so good on ChatGPT, it can take over your full scenes and environments.  (at 5:32, Aidan Stanik)
> it still looks a little bit Blender 3D generated, doesn't have like that realism that I was going for.  (at 20:12, Aidan Stanik)

## Contradictions flagged
- A Blender MCP is not needed because computer use can take over the scene. (vs The creator's own previz skill uses the Blender MCP when installed and falls back to computer use only otherwise (9:40).)

## Points to
- Creative AI Network (creator's community, skills download)
- Higgsfield Blender add-on
- Codex app
- Seedance 2.5
- GPT image 2.5
