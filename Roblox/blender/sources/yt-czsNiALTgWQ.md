---
type: research-source
id: yt-czsNiALTgWQ
title: "This Is How I Actually Make Games With AI - My Setup"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=czsNiALTgWQ"
published: "2026-10-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-czsNiALTgWQ

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator's personal AI game-dev workflow video: local folder-based workspace with skills, Claude Code as main agent, and subscription/cost notes. Blender coverage is minimal: mentions an official Blender MCP and a Blender plugin as useful for autonomous Blender work. No Blender-to-Roblox export, bpy, or Roblox pipeline details. Transcript is ASR-garbled (e.g., "Hicksville" likely Higgsfield).

## Claims
- c1: [12:30] Creator says they use the official Blender MCP and a Blender plugin (name garbled in transcript) and that these can work autonomously on Blender tasks. *(opinion, low; claude-blender-ai)*
- c2: [14:32] Creator states they have more tools for working in Blender than for other engines and recommends trying these Blender MCP options; claims they are best for Blender tasks. *(opinion, low; claude-blender-ai)*
- c3: [15:13] Creator says Unreal Engine 5.8 ships a native Unreal MCP; mentions Unity CLI and Unity MCP for Unity, not Roblox. *(opinion, medium; other)*
- c4: [6:30] Workflow: keep one folder per workspace with skills and context; launch agent (Claude Code CLI) in that folder so it has project context; one chat per narrow task. *(experience, medium; automation-and-creator-workflows)*
- c5: [4:14] Creator's workspace is a local install with no servers; it runs off the user's PC and can be forked from GitHub. *(experience, medium; automation-and-creator-workflows)*
- c6: [11:52] Creator estimates per-game AI asset cost at about $20-25 with APIs (about $10-12 excluding video generation) and prefers paid APIs over local generation because time is more costly. *(opinion, medium; other)*
- c7: [9:51] Creator is downgrading subscriptions: paid ChatGPT Pro (~$500 ultra-fast tier) tried and cancelled; Claude $200 plan kept; prefers Claude over GPT for long game tasks. *(experience, medium; other)*

## Numbers
- n1: **estimated AI asset cost per game**: $20-25 total; ~$10-12 without video generation 15 images, 10 3D models, plus video references, via paid APIs
- n2: **ChatGPT ultra-fast spend**: ~$500 tried then cancelled
- n3: **Claude subscription**: $200/month plan kept as main agent
- n4: **GitHub stars on workspace repo**: ~400 self-reported

## Techniques
- t1: **Per-task chats in a shared project folder**: Keep all project files, skills and history in one folder; start the agent there so context persists. Open a separate narrow chat per task (animation, VFX). Ask the agent to save successful approaches into skills for reuse.

## Quotes (brief, for attribution)
> I have three things official Blender, MCP, Hicksville, Blender plugin and mix are but actually best if you work in Blender  (at 12:30, Stefan 3D AI)

## Points to
- Blender official MCP (named, not linked)
- Higgsfield (transcribed as 'Hicksville') Blender plugin
- Tripo
- Unity CLI / Unity MCP
- Unreal Engine 5.8 native MCP
- Vibe UE
