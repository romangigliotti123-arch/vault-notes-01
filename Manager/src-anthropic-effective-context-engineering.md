---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
type: eng-blog
author: Anthropic Engineering
published: 2025-09 (undated in fetch)
accessed: 2026-10-29
reliability: high (primary vendor; guidance not benchmark)
---
# Effective context engineering for AI agents
## Key claims
- "Context, therefore, must be treated as a finite resource with diminishing marginal returns." Goal: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
- Context rot: as token count grows, "the model's ability to accurately recall information from that context decreases."
- Compaction: preserve "architectural decisions, unresolved bugs, and implementation details", discard redundant output. Tuning: "Start by maximizing recall" then "iterate to improve precision by eliminating superfluous content."
- "One of the safest lightest touch forms of compaction is tool result clearing."
- Structured note-taking / agentic memory: agent "regularly writes notes persisted to memory outside of the context window" and pulls them back later.
- Sub-agent architectures: specialised sub-agents with clean context windows return "only a condensed, distilled summary".
- Just-in-time retrieval: keep "lightweight identifiers (file paths, stored queries, web links)" and load at runtime; progressive disclosure lets agents "incrementally discover relevant context".
## Quotable
> "Context, therefore, must be treated as a finite resource with diminishing marginal returns."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-knowledge-management-rag]], [[topic-report-formats-and-verification]], [[topic-skill-library-retrieval]]
