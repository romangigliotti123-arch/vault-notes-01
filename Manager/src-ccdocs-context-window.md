---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/context-window.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.304+ mentions)
accessed: 2026-10-29
reliability: high (primary vendor docs)
---
# Claude Code docs: Explore the context window / what survives compaction
## Key claims
- Table "What survives compaction": system prompt + output style stay; project-root CLAUDE.md and unscoped rules and auto memory **re-injected from disk**; skill descriptions rebuilt (v2.1.304+); plan-mode plan re-injected from disk; **path-scoped rules and nested CLAUDE.md are summarised away** (reload on demand) - "If a rule must persist across compaction, drop the paths: frontmatter or move it to the project-root CLAUDE.md"; up to 5 recently touched files re-read (files >5,000 tokens come back as path reference only); invoked skill bodies re-injected, 5,000 tokens each / 25,000 total, oldest dropped; background commands/subagents keep running and Claude is reminded; context hooks added is summarised; **SessionStart hooks matching `compact` source run and add output** (re-inject context after compaction).
- Summarisation request inherits the session's thinking config (v2.1.198+).
- Before-it-fills levers: `/compact <focus>`, `/rewind` + "Summarize from here/up to here", `/autocompact 500k`, `/clear`, delegate large reads to subagents (only summary + small metadata trailer comes back).
- `/context` live breakdown by category with optimisation suggestions; `/memory` to edit loaded memory files.
## Quotable
> "If a rule must persist across compaction, drop the `paths:` frontmatter or move it to the project-root CLAUDE.md."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-context-window-management]]
