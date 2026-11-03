---
tags: [manager-kb, source]
url: https://claude.dev/blog/lessons-from-building-claude-code-prompt-caching-is-everything/
type: eng-blog
author: Anthropic (Claude Code team)
published: undated (2026)
accessed: 2026-10-29
reliability: high (primary, from the Claude Code builders)
---
# Lessons from building Claude Code: Prompt caching is everything
## Key claims
- "we run alerts on our prompt cache hit rate and declare SEVs if they're too low"; "Monitor your cache hit rate like you monitor uptime."
- Ordering: static system prompt+tools, then CLAUDE.md, then session context, then conversation. "static content first, dynamic content last".
- Model switching: "if you're 100k tokens into a conversation with Opus and want to ask a question that is fairly easy to answer, it would actually be more expensive to switch to Haiku than to have Opus answer, because we would need to rebuild the prompt cache for Haiku." "If you need to switch models, the best way to do it is with subagents."
- Don't change tools mid-session; plan mode implemented as tools (EnterPlanMode/ExitPlanMode) so tool defs never change; deferred tools via stubs with `defer_loading: true`.
- Compaction uses the exact same system prompt, context and tools as the parent, appends the compaction prompt as a new user message ("cache-safe forking"; summary "about 20k tokens", read at "one tenth the price"). Needs a reserved "compaction buffer" in the window.
## Quotable
> "Monitor your cache hit rate like you monitor uptime."
> "If you need to switch models, the best way to do it is with subagents"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-model-effort-routing-cost]]
