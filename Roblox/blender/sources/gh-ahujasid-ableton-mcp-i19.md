---
type: research-source
id: gh-ahujasid-ableton-mcp-i19
title: "ahujasid/ableton-mcp#19 Ollama Integration"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/19"
published: "2025-04-19"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-ai", "other"]
---
# gh-ahujasid-ableton-mcp-i19

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on ahujasid/ableton-mcp (Ableton, not Blender) asking how to run the MCP server with Ollama (Deepseek/Mistral) instead of Claude. Replies: Ollama is REST-based, so MCP commands must map to its endpoints; suggests a pypi ollama-mcpo-adapter, Open WebUI with mcpo, and OpenRouter. No Blender, bpy, or Roblox content.

## Claims
- c1: Source is about ableton-mcp (Ableton Live), not Blender; no blender-mcp or bpy content. *(doc, high; claude-blender-ai)*
- c2: Commenter says Ollama's API is REST-based rather than socket-based, so MCP commands must be mapped to Ollama endpoints and responses reformatted. *(opinion, medium; claude-blender-ai)*
- c3: Suggested bridge for Ollama with MCP: pypi package ollama-mcpo-adapter; Open WebUI can connect to MCP servers through mcpo while using Ollama for models. *(opinion, low; claude-blender-ai)*
- c4: Suggested OpenRouter as cheaper alternative: $5 credit gives API access to free models (claim as stated by commenter, unverified). *(opinion, low; other)*

## Numbers
- n1: **OpenRouter credit**: $5 Commenter says $5 credit unlocks free models in the API

## Points to
- https://github.com/ahujasid/ableton-mcp/issues/19
- https://pypi.org/project/ollama-mcpo-adapter/
- https://openrouter.ai
- Open WebUI
- Docker Model Runner
