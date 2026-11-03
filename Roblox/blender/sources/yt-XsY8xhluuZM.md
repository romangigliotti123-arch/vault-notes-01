---
type: research-source
id: yt-XsY8xhluuZM
title: "How to make a game using AI on Roblox"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=XsY8xhluuZM"
published: "2026-06-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-XsY8xhluuZM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators video (Jun 2026) on prototyping a Roblox wave-survival game with Claude connected to Roblox's MCP server. Covers stepwise planning, reprompting, and using the LLM as a tutor. No Blender, bpy, or Blender-to-Roblox export content, so it is largely off-topic for this research.

## Claims
- c1: [0:21] Roblox presenter says LLMs like Claude can cut pre-production prototyping from weeks to days; opinion/claim without data. *(opinion, low; automation-and-creator-workflows)*
- c2: [3:26] Workflow: connect the LLM to the codebase and to Roblox Studio via Roblox's MCP server, then have the AI plan the game in testable chunks. *(demo, medium; automation-and-creator-workflows)*
- c3: [4:53] Demo game: wave-survival with clone enemies, 5-shot gun, R to reload, 2 shots per kill, enemies speed up each round. Multiplayer worked without multiplayer-specific prompting. *(demo, medium; other)*
- c4: [5:34] Enemy health bars had to be explicitly requested to show at long distance so hits were visible; fixed by reprompting. *(demo, medium; other)*
- c5: [7:39] Prompting practice: ask the AI to stop at logical checkpoints for testing rather than building the whole game in one prompt. *(opinion, medium; automation-and-creator-workflows)*
- c6: [8:20] Switching first-person was described by the AI as about one line of change, showing mid-build mechanic changes are cheap if prompted incrementally. *(experience, low; other)*
- c7: [9:41] Presenter recommends asking the LLM to explain its decisions and cite references so the user learns while building. *(opinion, medium; automation-and-creator-workflows)*
- c8: [10:23] AI-generated code quality varies; generated projects will need review and restructuring, with more guardrails once a team is involved. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **pre-production time**: weeks to days claimed reduction from AI prototyping, no measurement given
- n2: **gun/combat rules**: 5 shots, 2 hits per kill demo game rules built via prompts
- n3: **build time**: about 6 hours presenter's total dev time for his demo game

## Techniques
- t1: **Plan-then-chunk prompting**: Describe design, ask AI for a plan split into testable chunks, test in Studio after each chunk, then feed back corrections and revise the plan.
- t2: **Tutor addendum**: Append an instruction asking the AI to explain its decisions simply with metaphors and to explain why, so the user can give better feedback.
- t3: **Ask for references**: After a decision, ask the LLM where the information came from and for links to read later.

## Quotes (brief, for attribution)
> it's not only just using an LLM, it's also tying it to our MCP server, which lets you actually drive Roblox itself  (at 2:46, Roblox Creators)
> If you're a one person army working with an AI you can do a lot. When you move to a team working on things you have to start putting a few more guardrails on it.  (at 10:23, Roblox Creators)

## Points to
- Roblox MCP server (drives Roblox Studio from the LLM)
- Claude
- ChatGPT
- Gemini
- Sister video with zip file setup guide (not in transcript)
