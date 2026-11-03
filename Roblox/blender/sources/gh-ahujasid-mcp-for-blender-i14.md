---
type: research-source
id: gh-ahujasid-mcp-for-blender-i14
title: "ahujasid/mcp-for-blender#14 Using MCP with an LLM API Instead of Claude’s Website"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/14"
published: "2025-03-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "other"]
---
# gh-ahujasid-mcp-for-blender-i14

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue asking whether blender-mcp can run with an LLM API (not the Claude website). Thread has no official answer; maintainer says PRs welcome. Commenters report LangChain-based MCP clients, Ollama/DeepSeek and Doubao attempts, Windsurf/Cursor use, and a Cursor integration PR. No Roblox content.

## Claims
- c1: Maintainer ahujasid says a PR adding non-Claude LLM API support would be welcome; no official setup guide exists in the thread. *(doc, high; claude-blender-mcp)*
- c2: A commenter says connecting blender-mcp to other models is easy via LangChain (langchain_mcp_adapters + LangGraph ReAct agent) and reports gpt-4o output quality was worse than Claude. *(experience, low; claude-blender-mcp)*
- c3: A commenter reports blender-mcp works decently with several models through Windsurf Cascade. *(experience, low; claude-blender-mcp)*
- c4: A PR (blender-mcp #133) adds Cursor integration to blender-mcp. *(doc, medium; claude-blender-mcp)*
- c5: Users attempting local models (Ollama with DeepSeek, Gemma, Llama) and Doubao API via RooCode; results reported as in progress, no confirmed working setup in thread. *(experience, medium; claude-blender-mcp)*
- c6: Thread contains no Roblox export, import, or mesh-limit information. *(doc, high; other)*

## Numbers
- n1: **blender-mcp Cursor integration PR**: #133 

## Techniques
- t1: **LangChain MCP agent wrapper**: Start Blender MCP server via stdio_client/StdioServerParameters, load tools with load_mcp_tools, build agent with langgraph create_react_agent, swap in any chat model (Azure OpenAI, Azure AI) via env keys.

### Code: Commenter's LangChain + MCP client imports (snippet truncated in source)
```python
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
```

## Quotes (brief, for attribution)
> Would be open to Pull Requests for this, I think it has a lot of potential  (ahujasid)
> It's actually pretty easy to do with langchain. Tried gpt-4o, but the quality doesn't seem to be as good.  (ahujasid)

## Contradictions flagged
- Issue title names repo 'mcp-for-blender' while the linked PR and comments refer to 'blender-mcp'. (vs Naming of the project in the issue itself (repo name drift))

## Points to
- https://github.com/ahujasid/blender-mcp/pull/133
- https://www.cnblogs.com/zhangbo2008/p/18980422
