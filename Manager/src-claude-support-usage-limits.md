---
tags: [manager-kb, source]
url: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
type: official-doc
author: Anthropic Help Center (also articles 11145838 and 14552983, read via WebFetch summary)
published: updated ~Oct 2026
accessed: 2026-10-29
reliability: high for what it states; it states little (no numeric weights)
---
# Usage and length limits (Help Center)
## Key claims
- "Paid plans have two types of usage limits: a session limit that resets every five hours, and weekly limits that reset once every week." Usage "is affected by ... the length and complexity of your conversations, the features you use, which Claude model you're chatting with, and the effort level you've selected." All surfaces (claude.ai, Claude Code, Desktop) share one limit. Usage credits extend it.
- Max plans have "a separate weekly limit for Fable" besides the general weekly limit. A small capped "wrapping up" allowance applies when a 5-hour limit hits mid-response (counts toward weekly).
- Models/usage in Claude Code article (WebFetch summary, not raw): "Opus costs several times more per turn than Sonnet, and Sonnet more than Haiku"; "Spending Opus on routine work is the fastest way to drain a daily limit"; "Clear between tasks ... the single most effective lever for both quality and cost"; "plan with Opus, execute with Sonnet"; CLAUDE.md under roughly 200 lines.
- Anthropic publishes NO conversion from tokens to plan allowance, no prompt counts, no weighting for subagents or cache reads.
## Quotable
> "Paid plans have two types of usage limits: a session limit that resets every five hours, and weekly limits that reset once every week."

## Used by
[[topic-model-effort-routing-cost]]
