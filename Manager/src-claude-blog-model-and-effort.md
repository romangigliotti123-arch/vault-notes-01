---
tags: [manager-kb, source]
url: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
type: eng-blog
author: Anthropic
published: undated (mentions Opus 4.8/4.7, Fable)
accessed: 2026-10-29
reliability: high (vendor guidance; curves illustrative only)
---
# Choosing a Claude model and effort level in Claude Code
## Key claims
- "Choose smaller models for more routine tasks and larger models for more complex or ambiguous tasks." Pick larger "when the smaller model is confidently wrong no matter how much context you give it."
- "for most tasks you should use the model's default effort level." Effort is "a general preference rather than a task-by-task decision" ("Think of effort as a manual override").
- Raise effort if Claude "got it wrong by skipping a file, not running the tests... or not double-checking".
- Illustrative: high-effort path "generates roughly 7x more tokens to reach a higher confidence answer"; curves "do not represent real benchmark data".
- "effort shapes token consumption but doesn't limit it" ; use task budgets or "ask Claude to keep it brief" as softer controls. Anthropic trains against "overthinking".
## Quotable
> "for most tasks you should use the model's default effort level."
> "effort shapes token consumption but doesn't limit it."

## Used by
[[topic-model-effort-routing-cost]]
