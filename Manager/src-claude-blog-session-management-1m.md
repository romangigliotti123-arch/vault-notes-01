---
tags: [manager-kb, source]
url: https://claude.com/blog/using-claude-code-session-management-and-1m-context
type: eng-blog
author: Anthropic (Using Claude Code series)
published: 2026-04-15
accessed: 2026-10-29
reliability: high (primary vendor; guidance, no measurements; read via WebFetch summary)
---
# Using Claude Code: session management and 1M context
## Key claims
- "Context rot is the observation that model performance degrades as context grows" (attention spread over more tokens, stale content distracts). No token threshold is given in the article (third-party summaries claim 300-400k; unverified).
- Decision table: **Continue** (everything still load-bearing, "don't pay to rebuild it"); **Rewind** (double-Esc: "Keep the useful file reads, drop the failed attempt, re-prompt with what you learned"); **/compact <hint>** (mid-task when bloated with stale debugging; "Low effort; Claude decides what mattered. Steer it with instructions"); **/clear** ("Zero rot; you control exactly what carries forward"); **Subagent** (next step produces lots of output and you only need the conclusion; test: "will I need this tool output again, or just the conclusion?").
- Why autocompact goes wrong: bad compacts happen "when the model can't predict the direction your work is going"; "the model is at its least intelligent point when compacting". With 1M context "you have more time to /compact proactively with a description of what you want to do."
## Quotable
> "Context rot is the observation that model performance degrades as context grows"
> "the model is at its least intelligent point when compacting"

## Used by
[[topic-context-window-management]]
