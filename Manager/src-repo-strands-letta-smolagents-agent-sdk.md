---
tags: [manager-kb, source]
url: https://github.com/strands-agents/harness-sdk
type: repo
author: AWS (Strands), Letta, Hugging Face, Anthropic
published: undated (READMEs read 2026-10-29)
accessed: 2026-10-29
reliability: high (READMEs + gh api metadata)
---
# Four smaller frameworks (one note)
- **Strands Agents** (repo renamed strands-agents/harness-sdk; sdk-python redirects there): 8,986 stars, Apache-2.0, pushed 2026-10-28, 1,048 open issues. "A model-driven approach"; "Choose Strands when you would otherwise write your own agent loop: it runs in your process with no hosted control plane." Now a monorepo with a Python and a TypeScript SDK plus a "harness" (`create_harness()`), CLI, evals, a Claude-Code/Codex/Cursor plugin for scaffolding and LangGraph migration. Multi-agent patterns built in (README line; details not read). Anthropic's own BEA post lists Strands among frameworks.
- **Letta** (formerly MemGPT): 25,274 stars, Apache-2.0, pushed 2026-10-18. README: "Build stateful agents with memory that can learn and improve over time"; the active code moved to letta-ai/letta-code (terminal UI/harness, App Server, Slack/Telegram/Discord channels, desktop + web apps, an Agent SDK). Memory-first, not an orchestration framework; relevant to "persistent agent" ideas ([[topic-long-running-always-on-agents]], [[topic-knowledge-management-rag]]).
- **smolagents** (huggingface): 30,124 stars, Apache-2.0, pushed 2026-10-22. ~1,000 lines for agent logic, CodeAgent writes actions as code; multi-agent = manager + managed agents. See [[src-smolagents-building-good-agents]].
- **Claude Agent SDK** (anthropics/claude-agent-sdk-python): 8,376 stars, MIT, pushed 2026-10-28. Bundles the Claude Code CLI; `query()` returns an async iterator of messages. It is the same engine we run (subagents, hooks, MCP, sessions) as a library; see [[src-ccdocs-agent-sdk-subagents]].

## Used by
[[topic-multi-agent-frameworks]]
