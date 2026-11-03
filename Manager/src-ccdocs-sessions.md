---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/sessions.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.2xx-2.1.311)
accessed: 2026-10-29
reliability: high (raw .md)
---
# Manage sessions (resume, /clear, naming)
## Key claims
- `claude --resume <name|id|path>` reloads the transcript; a resumed session restores permission mode, background work state, active goal (counters reset), agent. NOT restored: `--mcp-config`, `--settings`, `--plugin-dir`, `--fallback-model`, `--add-dir` (pass again). Interrupted tool calls are not rerun.
- "Resume this conversation?" dialog: the estimate is "the share of your 5-hour usage limit that the saved conversation alone would use"; appears on Pro/Max when resuming a long conversation after a long break or on a different model (cold cache). Pick **Start a new conversation** if the next task does not need the old one; Claude can still look it up.
- `/clear` saves the previous session (reopen via `/resume`), keeps a name set with `--name`/`/rename`; `/clear <name>` names the session you leave. `/compact [instructions]`, `/context`.
- Transcripts at `~/.claude/projects/<project>/<id>.jsonl`; retention `cleanupPeriodDays` (30).

## Used by
[[topic-context-window-management]]
