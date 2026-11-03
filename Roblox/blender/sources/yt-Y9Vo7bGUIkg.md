---
type: research-source
id: yt-Y9Vo7bGUIkg
title: "I Tested GPT-5.6 Sol Inside Blender. Claude Should Be Worried."
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=Y9Vo7bGUIkg"
published: "2026-07-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "other"]
---
# yt-Y9Vo7bGUIkg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator demo of driving Blender from the Codex desktop app via an MCP server, comparing it to earlier Claude (Opus 4.8, "Fable 5") runs. Covers MCP setup in Codex settings, a one-sentence image-to-scene prompt, a one-shot camera prompt that failed, and a detailed multi-step prompt that worked better. Not about Roblox export or the Roblox pipeline; comparisons are anecdotal.

## Claims
- c1: [2:12] Codex desktop app connects to Blender via Settings > Plugins > MCPs: add a server with a name and the launch command path to the local Blender MCP folder. *(demo, medium; claude-blender-mcp)*
- c2: [3:41] Author's habit: point the MCP at a dedicated Blender project folder so agent-saved .blend files stay organised; verify connection by asking the agent if it is connected to Blender. *(experience, medium; claude-blender-mcp)*
- c3: [4:17] A single pasted reference image plus one sentence ('recreate this in Blender for me') produced a first cathedral scene in about 3 minutes with curved ceilings, columns and checkered floor. *(demo, medium; claude-blender-mcp)*
- c4: [6:07] Author's opinion: Codex output looks more professional than his earlier Opus 4.8 and Fable 5 Blender outputs for similar cathedral references; comparison is across different scenes, not controlled. *(opinion, low; claude-blender-mcp)*
- c5: [6:40] One-shot prompt 'create a cinematic camera moving through the ruins' gave poor results: underwater scene, blocky low-poly geometry, judged not close to finished. *(demo, medium; claude-blender-mcp)*
- c6: [8:27] A long, step-by-step prompt after image analysis (architecture to fine details, Cycles reference render) produced a detailed marble hallway with spiral columns; author judged it much better than the one-shot prompt. *(demo, medium; claude-blender-mcp)*
- c7: [9:08] Author recommends using agent-driven Blender for small nitpicky tasks rather than taking over the whole workflow. *(opinion, medium; creator-workflows)*
- c8: [0:41] Title/thumbnail claim that GPT-5.6 outperforms Claude in Blender is not supported by any measured benchmark in the video; only a vendor benchmark slide was shown without method detail. *(opinion, low; other)*

## Numbers
- n1: **build time for cathedral scene from one image prompt**: ~3 min 
- n2: **MCP server setup fields**: server name + launch command path 

## Techniques
- t1: **Image plus one-sentence prompt**: Paste reference image into agent chat, ask to recreate in Blender; agent rebuilds scene via Python in the live viewport.
- t2: **Analyse-then-workflow prompt**: Have the agent break the reference image into architecture and detail sections, write a step-by-step Blender workflow, and render a Cycles reference image.

## Contradictions flagged
- Codex outperforms Claude/Opus 4.8 at Blender scene building (vs Video's own evidence is a few anecdotal single runs on different reference images; no controlled comparison)

## Points to
- Codex desktop app
- Blender MCP server (official, linked in video description; source URL garbled in transcript)
- Creative AI Network community (promotional, skipped)
