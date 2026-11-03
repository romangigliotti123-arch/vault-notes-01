---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/context-windows
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (current)
accessed: 2026-10-29
reliability: high (official)
---
# Context windows
## Key claims
- "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as context rot. This makes curating what's in context just as important as how much space is available."
- 1M-token window is default for Fable/Mythos 5.x, Opus 4.6-5.5, Sonnet 4.6-5.5, Haiku 5.5 (no beta header; Haiku 5.5 prompts >100k tokens cost more). Max output 128k. Sonnet 4.5/Haiku 4.5 are 200k.
- Context awareness (injected `<budget:token_budget>` and "Token usage: x/y" warnings) exists on Sonnet 5, Sonnet 4.6, Haiku 4.5; NOT on Opus 4.7+, Sonnet 5.5, Fable/Mythos, Haiku 5.5 (use task budgets, beta, instead).
- Server-side compaction is "the primary strategy for context management" for long-running agents (beta, Claude 4.6+). Context editing offers tool-result clearing and thinking-block clearing. Cached prefixes still occupy the window (caching changes price, not size).
- Thinking blocks of earlier turns are kept by default on Opus 4.5+/Sonnet 4.6+/Haiku 5.5 and count toward the window.
- Tip: "For agents that span multiple sessions, design your state artifacts so that context recovery is fast when a new session starts" (memory tool multisession pattern; effective-harnesses post).
## Quotable
> "more context isn't automatically better."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
