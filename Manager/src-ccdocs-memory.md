---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/memory.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md, 55 KB)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# How Claude remembers your project: CLAUDE.md, rules, auto memory
## Key claims
- CLAUDE.md is "context, not enforced configuration", delivered as a user message after the system prompt; "To block an action regardless of what Claude decides, use a PreToolUse hook". Size: "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." Startup + `/status` warn on oversize files and on a combined limit; Claude Code skips a file over 4 MiB entirely.
- Imports (`@path`, max depth 4 hops) "help you organize a long file but don't reduce its context cost, because imported files load together with the CLAUDE.md". Block-level HTML comments are stripped before injection (free maintainer notes). External imports from a project file need a one-time approval dialog; user-scope files (~/.claude/CLAUDE.md, ~/.claude/rules) are trusted.
- `.claude/rules/*.md` (and `~/.claude/rules/`): unconditional rules load at launch like CLAUDE.md; rules with `paths:` frontmatter (globs) load only when Claude reads/edits/writes a matching file. User-level rules load before project rules; conflicts resolved arbitrarily. Per-file limit for on-demand files (subdir CLAUDE.md, path-scoped rules): 40,000 chars on 200K windows, 150,000 on 1M windows of newer models; Claude gets only the start plus a note to read the rest (2.1.309+).
- Hierarchy: managed policy > user (~/.claude/CLAUDE.md) > project (./CLAUDE.md or ./.claude/CLAUDE.md) > CLAUDE.local.md; ancestors load at launch, subdirectory files lazily. Project-root CLAUDE.md survives `/compact` (re-read from disk); conversation-only instructions do not.
- "When to add": Claude repeats a mistake, a review catches something, you retype the same correction, a newcomer needs the same context. Multi-step procedures or single-area rules belong in a skill or path-scoped rule.
- Write concretely: "Use 2-space indentation" not "Format code properly". Conflicts between files are resolved arbitrarily; `/doctor prompt-audit` (2.1.283+) audits CLAUDE.md, rules, skills, commands, subagents, output styles for stale paths, instructions written for older models, contradictions. `/doctor` proposes trims (cuts what Claude can derive from code).
- Auto memory: on by default locally; four types (`user`, `feedback`, `project`, `reference`) as frontmatter in topic files; `MEMORY.md` is an index (one line per memory) of which only the first 200 lines OR 25 KB load at session start; topic files load on demand; over-limit write returns an error telling Claude to rewrite the index; memory files are excluded from the `cleanupPeriodDays` sweep. Claude skips what it can derive from code or CLAUDE.md. `autoMemoryDirectory` can relocate it. Machine-local; shared across worktrees of one repo. Toggle cannot be turned ON in background sessions or sessions started by another Claude session (e.g. `claude` run through Bash).
- Subagents do not inherit the main auto memory; their own `memory:` field creates a separate directory. Forks inherit everything.
- `InstructionsLoaded` hook logs which CLAUDE.md/rules loaded and why (debugging). `/context` lists Memory files. `claudeMdExcludes` skips unwanted CLAUDE.md files.
## Quotable
> "Claude treats CLAUDE.md files as context, not enforced configuration"
> "Files over 200 lines consume more context and may reduce adherence."
> "The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first, are loaded at the start of every conversation."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-claude-code-features]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-knowledge-management-rag]], [[topic-model-effort-routing-cost]]
