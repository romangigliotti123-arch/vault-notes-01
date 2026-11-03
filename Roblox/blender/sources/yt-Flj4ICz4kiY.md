---
type: research-source
id: yt-Flj4ICz4kiY
title: "THE AI SLAVES ARE GETTING OUT OF CONTROL"
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=Flj4ICz4kiY"
published: "2026-09-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0204
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# yt-Flj4ICz4kiY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Streamer rant about using Claude Opus 5.5 to one-shot Roblox games. Blender is mentioned only in passing: the AI reportedly modeled assets in Blender, and the streamer asks for more detailed models built in Blender and imported via Open Cloud. No blender-mcp setup, bpy code, FBX/glTF settings, or Roblox import steps are shown. Mostly opinion and hype.

## Claims
- c1: [15:41] Streamer says the AI agent generated game models in Blender as part of a one-prompt game build; no settings, scripts, or export steps shown. *(demo, low; claude-blender-ai)*
- c2: [2:49:38] Streamer tells the agent to regenerate dog models in Blender at extreme detail, using sub-agents, because the blocky placeholder models looked bad. *(opinion, low; claude-blender-ai)*
- c3: [3:10:57] Streamer asks for an oversized boss sword to be replaced by a new one built in Blender and imported through the Open Cloud API; no import settings given. *(opinion, low; blender-roblox-export-import)*
- c4: [1:18:44] Streamer instructs the agent to import free UI packs into Studio via a board CLI and upload assets through Open Cloud; method details not shown. *(demo, low; automation-and-creator-workflows)*
- c5: [41:56] Streamer reports repeated agent-introduced bugs and regressions across edits (broken proximity prompts, unplaceable items); agent output needed manual checks. *(experience, medium; claude-blender-ai)*
- c6: [2:50:21] Streamer says prompting for 'as detailed as possible' has always worked for him on models; this is anecdotal opinion, not a tested method. *(opinion, low; claude-blender-ai)*
- c7: [4:26:47] Streamer hit Claude session limits on two $200/month plans mid-session, which stalled the agent pipeline until reset. *(experience, medium; automation-and-creator-workflows)*
- c8: [56:55] Roblox publish fee cited as 1,000 Robux; Roblox Premium at $5/month waives it; expedited review cost 50,000 Robux. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Claude plan price**: $200/month Streamer's personal Claude subscription used for agent work
- n2: **Roblox publish fee**: 1,000 Robux Streamer's stated cost to publish; Premium $5/mo waives it
- n3: **Expedited review fee**: 50,000 Robux Streamer's claim, down from 100,000 Robux
- n4: **Parallel sub-agents**: 5 Streamer's agent runs feedback tasks with five sub-agents

## Techniques
- t1: **Agent-built models via prompt**: Describe the game in one prompt; agent generates Blender models and assets; streamer reviews in Studio. No steps, versions, or settings given.
- t2: **Sub-agent detail pass**: Ask agent to rebuild low-detail models in Blender using parallel sub-agents, then re-upload. Streamer reports this as anecdotal.
- t3: **Open Cloud asset upload**: Agent uploads generated images, sounds, and models to Roblox through the Open Cloud API instead of manual Studio imports.

## Quotes (brief, for attribution)
> Generate in extreme detail in Blender with sub agents.  (at 2:49:38, SmartyRBX)
> build your own sword that's better with Blender and import it through OpenCloud API.  (at 3:10:57, SmartyRBX)

## Contradictions flagged
- Agent output is reliable enough to ship without review ('we can trust it working'). (vs Same stream repeatedly reports agent-introduced bugs and rolled-back breakage.)

## Points to
- Open Cloud API
- Claude Max plan
- Mac OS Spaces
