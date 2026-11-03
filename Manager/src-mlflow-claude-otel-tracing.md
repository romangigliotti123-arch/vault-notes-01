---
tags: [manager-kb, source]
url: https://mlflow.org/blog/claude-otel-tracing
type: practitioner-blog
author: MLflow project
published: 2026-10-14 (per fetched page)
accessed: 2026-10-29
reliability: med (vendor blog, recent; no local-file backend discussed)
---
# MLflow: tracing Claude Code through OpenTelemetry
## Key claims
- Claude Code exports OTLP/HTTP traces to MLflow's `/v1/traces` (example `http://127.0.0.1:5000/v1/traces`, header `x-mlflow-experiment-id`); configuration is "entirely through environment variables"; each submitted prompt becomes its own trace within seconds; the Traces tab shows token and cost totals per row, each model/tool call as a step.
- Prompt/tool content stays redacted unless the `OTEL_LOG_*` flags are set; detailed tracing mode adds replies and context snapshots.
- Shows that any OTLP-HTTP backend can consume Claude Code traces without a vendor plugin: a Stop-hook plugin (Langfuse, LangSmith, Braintrust) is not required. Still needs a server process (MLflow); the 40-line JSON sink in [[topic-observability]] is the minimal alternative.

## Used by
[[topic-observability]]
