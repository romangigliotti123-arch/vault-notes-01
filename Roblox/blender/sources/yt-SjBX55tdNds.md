---
type: research-source
id: yt-SjBX55tdNds
title: "A ROBLOX BILLIONAIRE APPROVED MY GAME IDEA"
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=SjBX55tdNds"
published: "2026-09-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.2186
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "claude-blender-ai"]
---
# yt-SjBX55tdNds

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Long, mostly off-topic livestream by SmartyRBX (Roblox dev) about his game "Lift and Flex for Baddies", built largely by prompting AI coding agents. Blender appears only briefly: AI-generated Blender baddie models looked wrong against Roblox R15 proportions. Also describes MCP-board multi-agent sync, port-conflict and plugin-disconnect failures, and UGC-permission worries. Mostly opinion and noise; little verifiable pipeline detail.

## Claims
- c1: [5:00:27] AI agent produced Blender baddie character models that did not resemble Roblox avatars; speaker said they looked like a knockoff and were not usable as-is. *(experience, medium; claude-blender-ai)*
- c2: [5:05:17] Speaker said the AI model was only good at Blender at the moment, and prompting it for Blender work was the source of errors. *(opinion, low; claude-blender-ai)*
- c3: [4:56:21] Speaker prompted the agent to generate Blender rigs with varied R15 body shapes and sizes for the game's characters. *(experience, low; claude-blender-ai)*
- c4: [11:48:53] Speaker believed using another creator's marketplace UGC model in his game risks DMCA; he switched to a Roblox package model instead. *(opinion, low; avatar-ugc-accessories)*
- c5: [11:49:33] Speaker claimed Roblox announced around 2022 that other people's UGC cannot be used without permission; he did not cite a source. *(opinion, low; avatar-ugc-accessories)*
- c6: [8:33:00] Speaker described his custom MCP board sync tool as more automatic than Rojo for syncing code into Studio. *(opinion, low; automation-and-creator-workflows)*
- c7: [11:30:23] Agents failed to launch code to Studio due to port mismatch: runtime port 58849 vs canonical reservation 58805, blocking every session. *(experience, medium; automation-and-creator-workflows)*
- c8: [10:52:18] Sync lanes in the MCP board went stale after playtests, apparently because the Studio plugin lost its connection. *(experience, low; automation-and-creator-workflows)*
- c9: [11:29:41] Roblox Studio repeatedly crashed; speaker suspected the MCP board plugin. *(experience, low; automation-and-creator-workflows)*
- c10: [8:41:48] With several agents writing at once, uncommitted changes overlapped and conflicted, so the workspace state no longer matched across agents. *(experience, medium; automation-and-creator-workflows)*
- c11: [6:50:35] Speaker said Devex cash-out takes one to two weeks even after a game succeeds. *(opinion, low; automation-and-creator-workflows)*

## Numbers
- n1: **Port**: runtime 58849 vs canonical reservation 58805 
- n2: **Blender-related agent failures**: qualitative only; no counts 

## Techniques
- t1: **Repo rules file for agents**: Save each fix or constraint to the repo's agents MD so later agents follow it. Speaker used this to record launch and port rules after failures.
- t2: **Goal-scoped agent runs**: Set a concrete goal (for example, match a reference game's UX and keep no added bloat) rather than a vague one, to reduce wasted tokens.
- t3: **Open-source/package substitution**: Use a public Roblox package for UI or models when a custom version is hard to get right, and check for existing assets before generating new ones.

## Quotes (brief, for attribution)
> Your baddies don't even look like Roblox characters, idiot.  (at 5:00:27, SmartyRBX)
> Port runtime reservation mismatch. Live studios on port 58 something or other.  (at 11:30:23, SmartyRBX)

## Contradictions flagged
- Speaker says the AI is 'the best' coding slave yet it is 'stupid' and fails to launch code. (vs Speaker's own claim that the AI workflow reliably ships the game)

## Points to
- Roblox Studio
- blender-mcp / MCP board (speaker's own tool)
- Rojo
- Codex
- Devex
