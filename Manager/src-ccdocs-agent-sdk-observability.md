---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-sdk/observability.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; full page read)
---
# Agent SDK / claude -p: Observability with OpenTelemetry
## Key claims
- The CLI itself has OTel built in (spans per model request and tool execution, token/cost metrics, structured log events); the SDK adds none of its own. Three independent signals: metrics (`OTEL_METRICS_EXPORTER`), log events (`OTEL_LOGS_EXPORTER`), traces beta (`OTEL_TRACES_EXPORTER` + `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`). Telemetry is off until `CLAUDE_CODE_ENABLE_TELEMETRY=1`.
- "The CLI fails silently on export errors by default"; `CLAUDE_CODE_OTEL_DIAG_STDERR=1` surfaces them (v2.1.179+). Do not use the `console` exporter through the SDK (stdout is the message channel). Defaults: metrics export every 60 s, traces/logs every 5 s; short tasks need shorter `OTEL_*_EXPORT_INTERVAL` or data is lost on kill.
- Subagent `llm_request` and `tool` spans nest under the parent's `claude_code.tool` span: "the full delegation chain appears as one trace". Interactive CLI sessions ignore inbound `TRACEPARENT`; `-p`/SDK honour it.
- Audit events usable as a per-user audit trail: `tool_decision`, `tool_result`, `safety_event` (which check refused or prompted; v2.1.307+), `mcp_server_connection`, `permission_mode_changed`; exported as log records with a `claude_code.` prefix.
- Content is OFF by default; opt-in flags: `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS` (also gives real agent/skill/plugin names on cost metrics), `OTEL_LOG_TOOL_CONTENT` (needs tracing; 60 KB cap), `OTEL_LOG_RAW_API_BODIES` ("implies consent to everything the three variables above would reveal"). "Leave these unset unless your observability pipeline is approved to store the data your agent handles."

## Used by
[[topic-observability]]
