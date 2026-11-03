---
tags: [manager-kb, source]
url: https://claude.com/blog/context-management
type: eng-blog
author: Anthropic (no byline)
published: 2025-09-29
accessed: 2026-10-29
reliability: med-high (announcement; internal evals only)
---
# Managing context on the Claude Developer Platform (context editing + memory tool launch)
## Key claims
- Context editing automatically clears stale tool calls/results as context nears the limit; conversation stays intact. Memory tool = client-side file directory outside the context window.
- Internal agentic-search eval: memory tool + context editing +39% over baseline; context editing alone +29%. 100-turn web-search test: token consumption -84% and workflows that previously failed from context exhaustion completed.
- Use cases: coding (trim old file contents/test output, keep debugging lessons), research (save findings, drop old search results), data processing (keep interim outputs, drop raw inputs).
## Quotable
> "combining the memory tool with context editing improved performance by 39% over baseline."

## Used by
[[topic-context-engineering]]
