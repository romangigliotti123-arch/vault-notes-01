---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/monitoring-usage.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; first 100k of 172k chars read)
---
# Claude Code OpenTelemetry (monitoring usage)
## Key claims
- Enable: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_METRICS_EXPORTER` (otlp|prometheus|console|none), `OTEL_LOGS_EXPORTER` (otlp|console|none), `OTEL_TRACES_EXPORTER` (beta; also needs `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`). Console exporter works with no collector.
- Metrics: `claude_code.session.count` (start_type fresh/resume/continue/agents_view), `cost.usage` (USD per API request; attrs model, query_source, speed, effort), `token.usage` (input/output/cacheRead/cacheCreation), `lines_of_code.count`, `commit.count`, `pull_request.count`, `code_edit_tool.decision`, `active_time.total`.
- Events (log records): `claude_code.user_prompt`, `assistant_response`, `tool_result`, `tool_decision`, `api_request`, `api_error`, `api_refusal`, `api_request_body`/`api_response_body` (need `OTEL_LOG_RAW_API_BODIES`); `subagent_completed` is mentioned (name not fully shown).
- Attributes: `session.id`, `prompt.id` (UUID linking all events from one user prompt; hook payloads carry the same `prompt_id`), `tool_use_id` joins tool_result/tool_decision/hook payloads, `agent_id`, `parent_agent_id`, `agent.name`, `query_source` main|subagent|auxiliary, `workflow.run_id`.
- Privacy flags all OFF by default: `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_RAW_API_BODIES`.
- Trace spans (beta): `claude_code.interaction` > `llm_request`, `hook`, `tool` (> `blocked_on_user`, `execution`, subagent spans). Bash/PowerShell subprocesses inherit `TRACEPARENT`; `-p`/SDK read inbound `TRACEPARENT`.
- Claude Code does not pass `OTEL_*` vars to subprocesses/hooks; project `.claude/settings.json` OTEL vars are ignored (set in user env or managed settings).

## Used by
[[topic-long-running-always-on-agents]], [[topic-observability]]
