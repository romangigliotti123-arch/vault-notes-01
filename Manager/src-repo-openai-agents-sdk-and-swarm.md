---
tags: [manager-kb, source]
url: https://github.com/openai/openai-agents-python
type: repo
author: OpenAI
published: undated (SDK created 2025-03-11; pushed 2026-10-27)
accessed: 2026-10-29
reliability: high (README, docs page and gh api read)
---
# OpenAI Agents SDK (30,355 stars, MIT) and Swarm (22,085 stars, MIT, replaced)
## Key claims
- Swarm README banner: "Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm ... We recommend migrating to the Agents SDK for all production use cases." Swarm = "experimental, educational", last push 2026-04-15.
- Agents SDK core concepts: Agents (LLM + instructions + tools + guardrails + handoffs), sandbox agents, agents-as-tools, handoffs, guardrails, human-in-the-loop, sessions, tracing, voice/realtime. Provider-agnostic (Responses and Chat Completions APIs, "100+ other LLMs").
- Docs "Agent orchestration": two ways - LLM decides vs code decides. Two SDK patterns: **Agents as tools** ("A manager agent keeps control of the conversation and calls specialist agents through Agent.as_tool() ... You want one agent to own the final answer") and **Handoffs** ("A triage agent routes the conversation to a specialist, and that specialist becomes the active agent"). Use agents-as-tools for bounded subtasks that should not take over the user-facing conversation.
- Orchestrating via code (more deterministic in speed/cost/performance): classify with structured output then pick next agent; chain agents (research, outline, write, critique, improve); while-loop task agent + evaluator agent until pass; parallel runs via asyncio.gather. Mix and match.
- Tactics for LLM orchestration: good prompts, monitor and iterate, let the agent critique itself in a loop, specialised agents rather than one general agent, evals.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
