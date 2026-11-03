---
tags: [manager-kb, source]
url: https://dev.to/uenyioha/writing-cli-tools-that-ai-agents-actually-want-to-use-39no
type: practitioner-blog
author: Ugo Enyioha
published: undated (posted Feb 27, year not shown on fetched text; likely 2026)
accessed: 2026-10-29
reliability: med (practitioner opinion, consistent with other sources)
---
# Writing CLI tools that AI agents actually want to use
## Key claims
- `--json` structured output with flat objects, consistent field types, ISO 8601/seconds durations; JSON Lines for streams.
- Results to stdout, progress/warnings to stderr.
- Documented exit codes beyond 0/1 (usage error, not found, permission denied, conflict); distinguish transient (retryable) from permanent errors.
- Idempotency: declarative `ensure`/`apply` or `--if-not-exists`; else a distinct conflict exit code. "Agents retry. Networks fail. Commands get interrupted."
- `--dry-run` that returns a structured diff; `--yes`/`--force` to skip prompts; fail clearly when stdin is not a TTY.
- Self-documenting help with examples; predictable noun-verb grammar; `--quiet` bare values; batch/selector operations.
- Other community skill files (search snippets only, not opened) add: schema introspection commands, field masks (`--fields`), truncation defaults, exit 2 usage / 1 runtime / 69 transient.
## Quotable
> if your agent has shell access, a well-designed CLI often wins.

## Used by
[[topic-tool-and-mcp-design]]
