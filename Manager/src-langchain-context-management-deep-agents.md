---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/context-management-for-deepagents
type: eng-blog
author: Chester Curme, Mason Daugherty (LangChain)
published: 2026-01-28
accessed: 2026-11-01
reliability: med (vendor; thresholds are config, not findings)
---
# Context management for Deep Agents
## Key claims
- Three escalating compressions: (1) tool results over 20,000 tokens offloaded to a file, replaced by path plus 10-line preview; (2) at 85% of the window, older write/edit tool inputs replaced by file pointers; (3) LLM structured summary, full originals kept on disk for search.
- For testing they trigger compression at 10-20% of the window to get more events; this showed that dedicated prompt slots for goal and next actions improved post-summary performance.
- Targeted evals: does the agent keep its objective after summarisation; can it recover a needle fact from the filesystem.
## Used by
[[topic-context-engineering]], [[topic-context-window-management]]
