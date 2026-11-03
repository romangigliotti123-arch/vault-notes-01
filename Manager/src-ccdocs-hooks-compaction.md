---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/hooks.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.296-2.1.312)
accessed: 2026-10-29
reliability: high (raw .md; only compaction-related sections read)
---
# Hooks reference: PreCompact, PostCompact, SessionStart `compact`
## Key claims
- `PreCompact` ("Before context compaction") can BLOCK compaction (exit 2 / decision block); input has `trigger` (`manual`|`auto`) and `custom_instructions` (what the user passed to `/compact`, null otherwise). `systemMessage`/`continue` fields are discarded.
- `PostCompact` input has `trigger` and `compact_summary` (the generated summary); no decision control; use to log the summary or update external state.
- `SessionStart` input `source` is `startup|resume|clear|compact|fork`; SessionStart hooks matching `compact` run after compaction and their output is added to the compacted context (re-inject critical state).
- `InstructionsLoaded` hook logs which CLAUDE.md/rules loaded and why (`load_reason` includes `compact`).
- Reading for us: a PostCompact hook can append the summary to a disk journal (audit of what the manager believes after each compaction); a SessionStart(compact/resume) hook can print the job ledger so the manager re-reads live state instead of trusting the summary.

## Used by
[[topic-context-window-management]]
