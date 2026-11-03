---
type: research-source
id: yt-yISqRvt7F_I
title: "I Tested How Realistic GPT-6 Astra Could Generate Scenes In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=yISqRvt7F_I"
published: "2026-09-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation"]
---
# yt-yISqRvt7F_I

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demo of prompting GPT-6 "Astra" (via Codex app/terminal) to recreate a reference house image as a Blender scene via Python scripting in Blender 5.2, using a creator's "Blender OS" setup pack. Shows no Roblox export or Roblox pipeline; relevance to Roblox is indirect (general Claude/AI-driven bpy workflow only).

## Claims
- c1: [9:57] Codex writes Python scripts pasted into Blender's Scripting tab to build the scene; creator says it builds 3D from code, taking ~10-15 minutes for the house. *(demo, medium; bpy-scripting-headless)*
- c2: [6:34] Setup: run a 'Blender OS setup' zip (free creator pack) via Codex terminal with full access, which configures Codex-to-Blender connection; no MCP server named. *(demo, medium; claude-blender-mcp)*
- c3: [8:59] Text/image-to-scene one-shot: a Google reference image plus a prompt asking for high realism and matched lighting produced the scene; no manual modelling. *(demo, medium; procedural-generation)*
- c4: [1:15] Creator says one-shot AI Blender output can be messy; topology is not clean and basic Blender knowledge (camera, transforms, geometry nodes) is still needed. *(opinion, medium; common-mistakes-fixes)*
- c5: [0:41] Generated scene contained over 130,000 grass blades and over 150,000 leaves; viewport lag made material preview slow. *(demo, medium; procedural-generation)*
- c6: [5:26] Creator ran on an M4 Pro MacBook with about 68 GB RAM; older or weaker hardware would take longer. *(demo, low; other)*
- c7: [3:04] Access to GPT-6 Astra requires a paid ChatGPT plan: Plus $20/mo, Pro $100/mo, higher $200/mo tier with more usage. *(doc, low; other)*
- c8: [6:08] Creator states Blender 5.2 is the most recent version, and GPT-6 has access to its tools. *(opinion, low; other)*
- c9: [4:46] Creator suggests the generated Blender model can be reused: add characters, export into a website parallax scroll, or a walkthrough, rather than an HTML-only output. *(opinion, low; creator-workflows)*

## Numbers
- n1: **grass blades**: over 130,000 
- n2: **leaves**: over 150,000 
- n3: **RAM**: about 68 GB (M4 Pro) 
- n4: **build time**: 10-15 minutes 
- n5: **ChatGPT plan prices**: $20, $100, $200 per month 

## Techniques
- t1: **Agent-written bpy via Scripting tab**: Agent (Codex) generates Python, user pastes or runs in Blender Scripting tab; viewport shows result. Creator says visible code appears in Scripting tab while agent works.
- t2: **Reference-image recreation prompt**: Find reference image (e.g., Google 'Blender house'), paste into Codex, prompt to recreate in open Blender viewport with high realism, contrast, matched lighting.

## Quotes (brief, for attribution)
> Go into Codeex, open a new Blender folder... download this Blender OS setup zip file.  (at 6:34, Aidan Stanik)
> With one single prompt, I was able to get this insanely realistic home rendered out inside of Blender.  (at 0:00, Aidan Stanik)

## Contradictions flagged
- Creator says AI one-shot output has clean topology and lighting but notes topology is not clean and the model does not understand it yet. (vs Creator's own claim that outputs are 'super clean' and 'amazing' in 3D)

## Points to
- Blender OS setup zip / free Blender AI starter pack (creator's free school community)
- Blender 5.2
- Codex app / ChatGPT app
