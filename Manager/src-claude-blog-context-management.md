---
tags: [manager-kb, source]
url: https://claude.com/blog/context-management
type: eng-blog
author: Anthropic
published: 2025-09-29
accessed: 2026-10-29
reliability: high (primary; internal benchmarks)
---
# Managing context on the Claude Developer Platform (context editing + memory tool)
## Key claims
- Context editing "automatically clears stale tool calls and results from within the context window when approaching token limits"; memory tool = file-based storage outside the window, developer-hosted, "operates entirely client-side through tool calls".
- Internal agentic-search eval: memory tool + context editing "improved performance by 39% over baseline"; context editing alone 29%. 100-turn web-search eval: context editing cut token consumption by 84% and let workflows finish that would otherwise fail from context exhaustion.
- Public beta on Claude Developer Platform, Bedrock, Vertex (tied to Sonnet 4.5 at the time). Use cases: coding (clear old file reads/test results, keep decisions in memory), research, data processing.
- Note: this is API-level; Claude Code applies similar tool-result clearing internally ("expected rebuilds: compaction or tool-result clearing" in /usage).
## Quotable
> "Context editing automatically clears stale tool calls and results from within the context window when approaching token limits."

## Used by
[[topic-context-window-management]]
