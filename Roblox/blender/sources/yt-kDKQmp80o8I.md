---
type: research-source
id: yt-kDKQmp80o8I
title: "SEQUENCER gets LOVE 🫶 Blender Today LIVE #280"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=kDKQmp80o8I"
published: "2026-04-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0080
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-kDKQmp80o8I

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today #280 (Apr 2026) mostly covers Blender 5.2 dev news. Only the Blender-AI part is relevant: Blender Lab's MCP server runs as a separate app outside Blender, plus a separate add-on that Blender core does not ship. It works with local open-source LLMs such as llama.cpp. Nothing on Roblox, FBX/glTF export, mesh limits, rigging, or accessories.

## Claims
- c1: [11:55] Blender's MCP setup has three parts: an MCP server running outside Blender, an MCP add-on inside Blender, and a chat LLM client that talks to the server. *(doc, high; claude-blender-ai)*
- c2: [14:22] Presenter says Blender core got zero lines of code for the MCP work; the add-on is not on the extensions site and must be downloaded separately from lab.blender.org. *(doc, high; claude-blender-ai)*
- c3: [14:22] Presenter says setup is not easy and takes many steps (opinion, from personal attempt). *(experience, medium; claude-blender-ai)*
- c4: [23:21] Presenter tested with local open-source models; renaming data blocks and explaining node groups worked. Limits: only certain data blocks are accessible. *(experience, medium; claude-blender-ai)*
- c5: [23:21] Per the presenter, MCP tools can render the scene and run Python commands in natural language. *(doc, medium; claude-blender-ai)*
- c6: [1:03:27] The Blender Lab MCP page's setup example uses llama.cpp with an open-source client; it does not mention Claude or other proprietary services. *(doc, high; claude-blender-ai)*
- c7: [17:06] Anthropic, original author of the MCP spec, joined the Blender Development Fund as a pattern sponsor, a no-strings-attached donation to core development. *(doc, high; other)*
- c8: [1:57:16] Presenter says nothing in the upcoming Blender 5.2 build changes the MCP setup; the add-on is outside default Blender and will not ship in it. *(opinion, medium; claude-blender-ai)*
- c9: [1:50:27] Presenter says the MCP tools mostly wrap basic Python operations (e.g. rename many objects, find object with most vertices) in natural language; no generative creation. *(opinion, medium; claude-blender-ai)*
- c10: [1:52:31] Presenter says the MCP setup can run fully offline with local models, with no data sent to external servers, when a local model is used. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **Sponsorship level**: 240-250 per year (patron level) Presenter cites patron-level amount for corporate dev-fund membership
- n2: **Cycles render memory**: 3.5 GB -> 2.3 GB Ray differential widening change on one example render; texture cache reduction
- n3: **Eevee instancing FPS**: 11 -> 22 fps (OpenGL), 8 -> 16 fps (other backend) 100,000 geometry-nodes instances; instancing optimization

## Techniques
- t1: **External MCP server + Blender add-on bridge**: 1) Run MCP server as separate process on your machine. 2) Install MCP add-on in Blender from lab.blender.org. 3) Point chat LLM client at server; it sends instructions to Blender. Setup has several steps.

## Quotes (brief, for attribution)
> Blender got zero lines of codes in the source code of Blender. This is an add-on that it's not even in the Blender extensions website.  (at 14:22, Blender)
> we've been exploring building like a MCP connector MCP server component which runs outside of Blender.  (at 11:55, Blender)
> it even in the Blender page, there is no mention of cloud at all.  (at 1:03:27, Blender)

## Contradictions flagged
- Claude works directly inside Blender (viewer claim in chat) (vs Presenter: MCP server is separate from Blender; Blender itself has no Claude integration.)

## Points to
- code.blender.org/roadmap
- lab.blender.org (MCP server experiment)
- studio.blender.org
- llama.cpp (local LLM client in lab example)
- Blender Conference 2026 Amsterdam
