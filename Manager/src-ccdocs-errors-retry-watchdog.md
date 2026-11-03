---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/errors.md
type: official-doc
author: Anthropic (Claude Code docs); env vars at /env-vars.md
published: undated
accessed: 2026-10-29
reliability: high (official; read from cached copies of errors.md and env-vars.md)
---
# Errors / automatic retries / CLAUDE_CODE_RETRY_WATCHDOG
## Key claims
- Built-in: "Claude Code retries transient failures up to 10 times with exponential backoff before showing you an error" (`CLAUDE_CODE_MAX_RETRIES`, cap 15). 529 backoff base 500 ms to max 32 s (`CLAUDE_CODE_OVERLOADED_RETRY_*`).
- `CLAUDE_CODE_RETRY_WATCHDOG=1` is documented "for unattended sessions such as eval harnesses, CI jobs, or remote workers": retries 429/529 indefinitely; "backs off up to 5 minutes between attempts, or until the limit resets when the response carries a rate-limit reset time, so a session that hits a usage limit waits out the remaining window"; raises other transient-error retry count to 300 (~3 h of backoff). Fails at once on a 429 that reports a spend limit / exhausted credits. Needs v2.1.186+. `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` (60000-10800000) checks whether a limit lifted early (v2.1.305+).
- Not retried: TLS cert failures, etc. Tool-call parse failure: 2 retries then turn ends.
- `cleanupPeriodDays` default 30: background sweep deletes transcripts silently (setting 0 invalid; use e.g. 3650 for long retention).

## Used by
[[topic-long-running-always-on-agents]]
