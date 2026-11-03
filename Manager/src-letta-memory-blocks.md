---
tags: [manager-kb, source]
url: https://docs.letta.com/guides/agents/memory-blocks
type: official-doc
author: Letta (MemGPT successor)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (vendor docs; design concept, not benchmarked here)
---
# Letta memory blocks (core memory = persona + human)
## Key claims
- Memory blocks are labelled, size-limited sections of the context window, "always visible - no retrieval needed", prepended in XML-like form. Default labels `persona` (who the agent is) and `human` (key details about the user), each with `chars_limit` (example 5000) and a description telling the agent how to use it. This is the same split as soul.md (persona) + user model.
- Properties: agent-managed (agent edits blocks via memory tools), shareable across agents (update once, visible everywhere), and `read_only: true` blocks (agent cannot change them) for policies/organisation facts "you don't want the agent to be able to make potentially destructive changes to".
- Takeaway: hard char limits plus labels force curation; read-only vs read-write is the safety switch between "operator-owned rules" and "agent-learned notes".
## Quotable
> Memory blocks are structured sections of the agent's context window that persist across all interactions. They are always visible - no retrieval needed.

## Used by
[[topic-knowledge-management-rag]], [[topic-personal-assistant-agents]]
