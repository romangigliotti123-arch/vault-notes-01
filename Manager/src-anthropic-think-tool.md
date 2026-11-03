---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/claude-think-tool
type: eng-blog
author: Anthropic Engineering
published: 2025-03-20 (update note 2025-12-15)
accessed: 2026-10-29
reliability: high (primary; superseded in part by its own update note)
---
# The "think" tool
## Key claims
- A no-op tool giving the model a place to stop mid-response and check it has the info to proceed. tau-bench airline: pass^1 0.570 vs 0.370 baseline (+54% relative) with an optimised prompt; smaller in retail. Best for policy-heavy, sequential, costly-mistake settings; long guidance belongs in the system prompt.
- Little benefit for single/parallel tool calls or simple instruction following.
- Dec 2025 update: "we recommend using [extended thinking] instead of a dedicated think tool in most cases."
## Quotable
> "we recommend using that feature instead of a dedicated think tool in most cases."

## Used by
[[topic-anthropic-agent-guidance]]
