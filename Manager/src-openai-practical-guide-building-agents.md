---
tags: [manager-kb, source]
url: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
type: official-doc
author: OpenAI
published: undated (PDF; 2025)
accessed: 2026-10-29
reliability: high (vendor guide, pdftotext of the full PDF, 34 pages)
---
# A practical guide to building agents (OpenAI)
## Key claims
- Orchestration section: "Our general recommendation is to maximize a single agent's capabilities first. More agents can provide intuitive separation of concepts, but can introduce additional complexity and overhead, so often a single agent with tools is sufficient."
- Manage complexity before splitting by using prompt templates (one base prompt with policy variables) instead of many prompts.
- When to split: (1) complex logic - prompts with many if-then-else branches that no longer scale; (2) tool overload - "The issue isn't solely the number of tools, but their similarity or overlap. Some implementations successfully manage more than 15 well-defined, distinct tools while others struggle with fewer than 10 overlapping tools." Improve tool names/descriptions first; split only if that fails.
- Two multi-agent categories: Manager (agents as tools; one agent keeps control and talks to the user) and Decentralized (agents hand off to peers; the receiving agent takes over the conversation). Modeled as graphs: edges are tool calls (manager) or handoffs (decentralized).
- Manager pattern "ideal for workflows where you only want one agent to control workflow execution and have access to the user". Decentralized "optimal when you don't need a single agent maintaining central control or synthesis".
- Code-first (Agents SDK) over declarative graphs: declarative graphs get "cumbersome" as workflows grow dynamic.
- Model selection: build evals with the most capable model first for a baseline, then try smaller models per step. Layered guardrails; human-in-the-loop for high-risk actions.
## Quotable
> Our general recommendation is to maximize a single agent's capabilities first.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
