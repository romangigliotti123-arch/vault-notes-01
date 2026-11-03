---
tags: [manager-kb, source]
url: https://aquinas-protocol.github.io/second-brain/ (and others from one search)
type: practitioner-blog
author: various community authors (snippets only)
published: 2026-04 to 2026-05
accessed: 2026-10-29
reliability: low: search snippets only, pages not opened
---
# Obsidian + Claude Code second-brain write-ups (Karpathy LLM-wiki pattern)
## Key claims
- Common implementation: CLAUDE.md at vault root as schema; index.md = catalogue of pages with one-line summaries; log.md = append-only record of ingests/queries/lints; raw/ folder for sources.
- Lint pass typically read-only and asks before fixing: missing frontmatter, broken wiki-links, orphan pages, stale pages (frontmatter last-updated), contradictions, index mismatches; one setup runs it from a git post-commit hook.
- Frontmatter fields such as related and last-updated are used to query connected pages and flag stale ones. An MIT-licensed Claude Code plugin "claude-obsidian" implements the pattern (not inspected).
- Treat as examples, not a standard; no benchmarks.
## Quotable
> (none; snippet only)

## Used by
[[topic-knowledge-management-rag]]
