---
tags: [manager-kb, source]
url: https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/fileexporter
type: repo
author: OpenTelemetry Collector contrib
published: undated
accessed: 2026-10-29
reliability: high (official README; stability alpha for traces/metrics/logs)
---
# OTel Collector file exporter
## Key claims
- "Writes telemetry data to files on disk": default newline-delimited OTLP JSON, one batch per line. Rotation only when `rotation:` key present: `max_megabytes` (default 100), `max_days`, `max_backups` (default 100), `localtime`. Traces/metrics/logs alpha stability.
- This is the no-backend way to capture Claude Code's OTel metrics and events into rotating local files: a single `otelcol-contrib` binary (OTLP receiver 4317/4318 -> file exporter) as a Windows service/scheduled task. Cost: one more always-on process; benefit: exact per-request cost/token rows without parsing transcripts.

## Used by
[[topic-long-running-always-on-agents]], [[topic-observability]]
