---
type: research-source
id: yt-mTEw45oqio4
title: "Can GPT-6 Astra Animate Characters In Blender?"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=mTEw45oqio4"
published: "2026-09-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 1
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "claude-blender-mcp", "creator-workflows", "other", "procedural-generation", "rigging-animation"]
---
# yt-mTEw45oqio4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demo of driving Blender character animation and scene building through OpenAI Codex (GPT-6 Astra, high effort) connected to the official Blender MCP server. Covers MCP install and connection steps, prompt-based wave, facial and backroom-scene animation, and per-step credit and dollar costs. No Roblox content: no export, import, mesh limits or Roblox workflow.

## Claims
- c1: [5:51] Official Blender MCP install: drag the blue box from blender.org lab MCP server page into the Blender viewport; first drag downloads the add-on, second drag activates the MCP connection. *(demo, medium; claude-blender-mcp)*
- c2: [6:34] Codex side setup: Settings > Plugins, search 'Blender', open MCPs, set Command to launch the Blender MCP file path from the Blender add-on folder; verify with /mcp which shows Blender as authorized. *(demo, medium; claude-blender-mcp)*
- c3: [5:34] Video recommends Blender 5.2 (most recent at recording) and Codex app with full-access mode and GPT-6 Astra high effort. *(opinion, low; claude-blender-mcp)*
- c4: [9:02] On a fully rigged Blender Studio character, a one-line prompt ('Give the character a nice wave') produced a wave plus smile and head nod, but the character stayed stuck in T-pose at the start, needing a follow-up prompt to keep hands down. *(demo, high; rigging-animation)*
- c5: [10:17] Facial expression prompts (warm smile, surprised, worried, angry, skeptical, playful wink, big laugh) were produced on the rig; the presenter says references such as uploaded faces or Pixar-style material can steer the look. *(demo, medium; rigging-animation)*
- c6: [11:06] A single detailed prompt generated a multi-shot backrooms scene with camera cuts, sound effects and music, but the presenter judged the character motion rigid and the render glitchy, not client-ready. Rendered in Eevee (believed). *(demo, high; procedural-generation)*
- c7: [14:12] Reported session cost on Codex Pro plan: MCP setup 21 cents; character isolation/T-pose ~31 credits (~$1); wave ~25 credits (~$1); wave revision 52 cents; facial showcase ~64 credits ($2); backroom ideation ~6 credits; 30s film build 304 credits (~$12); save 13 credits (54 cents); total ~464 credits, $18.57. *(data, medium; creator-workflows)*
- c8: [3:34] Presenter's own benchmark claim: GPT-6 Astra high effort about 61% resolution rate at ~$14 API cost versus Claude 'Fable 5.1' about 40% at ~$20; unverified and self-reported. *(opinion, low; other)*
- c9: [8:29] Character sources named: Blender Studio Storm rig (paid subscription about $15-17/month per video), Sketchfab free rigged models, meshy.com image-to-3D. *(opinion, medium; avatar-ugc-accessories)*
- c10: [2:00] Computer use mode lets the model view the screen and iterate on animations; screenshots and screen recordings can be uploaded as feedback. Keyframing can be used for manual fixes. *(demo, medium; claude-blender-mcp)*

## Numbers
- n1: **total session cost**: 464 credits / $18.57 
- n2: **30s backroom film build**: 304 credits, about $12 
- n3: **MCP setup cost**: 21 cents 
- n4: **self-reported benchmark resolution rate (GPT-6 Astra high vs Fable 5.1 high)**: 61% vs 40% 
- n5: **self-reported API cost per run (Astra high vs Fable 5.1 high)**: $14 vs $20 
- n6: **recommended Blender version**: 5.2 
- n7: **Blender Studio subscription price per video**: about $15-17/month 
- n8: **demo sequence length**: about 15:55 video; backroom film about 30 s 

## Techniques
- t1: **Blender MCP connection to Codex**: Install MCP add-on via blender.org link drag-drop, enable in Preferences > Add-ons, copy add-on file path, add it as launch command in Codex Settings > Plugins > MCPs, then type /mcp to confirm Blender is authorized.
- t2: **Iterative prompt correction**: Generate a first pass, then send a follow-up prompt describing the fix (e.g., keep hands down, raise one hand to wave) rather than hand-keyframing.
- t3: **Visual feedback loop**: Upload screenshots or screen recordings to the chat or enable computer use so the model inspects the Blender viewport and revises.
- t4: **Storyboard-style scene prompt**: Ask Codex for a detailed shot-by-shot prompt with timings, then paste it into the Blender session to build cameras, scenes, sound and animation in one pass.
- t5: **Project folder organisation**: Keep all Blender projects inside one dedicated folder so Codex can read context and manage .blend files.

## Quotes (brief, for attribution)
> Give the character a nice wave. Very simple prompt, but I just want to show you with this very simple prompt we can get some pretty clean outputs back.  (at 9:02, Aidan Stanik)
> So, in total, with that generation, I spent about 464 credits and $18.57.  (at 14:12, Aidan Stanik)

## Contradictions flagged
- Video says 'Claude has access to all of the rig movements' while the session runs in Codex with GPT-6 Astra. (vs The model actually driving the session is named as GPT-6 Astra in the same video)
- Presenter states GPT-6 Astra outperforms 'Fable 5.1' from Anthropic with 61% vs 40% resolution. (vs No source or methodology is shown; figures are self-reported on screen)

## Points to
- blender.org lab MCP server page (official Blender MCP)
- Blender Studio (Storm rig character)
- Sketchfab
- meshy.com
- Codex app (OpenAI)
