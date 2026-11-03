---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/headless.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (CC 2.1.3xx era)
accessed: 2026-10-29
reliability: high (official)
---
# Claude Code headless (`claude -p`) - report-format facts
## Key claims
- `--output-format json` returns result, session ID and metadata incl. `total_cost_usd` and per-model cost; `text` default; `stream-json --verbose --include-partial-messages` streams events, last line is a `result` message.
- Structured reports: "use `--output-format json` with `--json-schema` and a JSON Schema definition. The response includes metadata about the request (session ID, usage, etc.) with the structured output in the `structured_output` field." Invalid schema -> error before run. `format` keyword accepted but only annotation.
- "If a run ends without valid structured output, for example because Claude declined the request, the response has no `structured_output` field. Before your script uses `structured_output`, check that the field is present."
- Exit code 0 on success, non-zero on failure; auth failures print as the result on stdout; SIGTERM -> 143 and "records no result" for the interrupted turn; SIGINT ends the turn properly.
- Run stays open for background subagents/workflows (their result is part of the output); 10-minute idle-wait ceiling (`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`) drops partial result; `--max-budget-usd` cap stops remaining background work.
- `--resume`/`--continue` report the conversation's whole cumulative spend.

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
