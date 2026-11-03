---
tags: [manager-kb, source]
url: https://docs.dbos.dev/architecture
type: official-doc
author: DBOS
published: undated
accessed: 2026-10-29
reliability: high (vendor doc)
---
# DBOS architecture (Postgres-backed durable execution)
## Key claims
- "DBOS checkpoints those workflows and steps to a Postgres database": inputs and step outputs stored; no separate orchestrator server. Single-node: at startup "DBOS scans for incomplete (PENDING) workflows" and resumes them from the last completed step.
- Workflow code must be deterministic (same steps, same inputs, same order on replay); nondeterministic work (DB, API, random, time) goes in steps.
- "Steps should be idempotent, meaning it should be safe to retry them multiple times." A step interrupted mid-run is retried; "once a step completes and is checkpointed, it is never re-executed."
- Direct lesson: a lightweight ledger on SQLite/Postgres (or even a JSON file) plus a scan-for-PENDING on startup is the minimal durable-execution design; no heavy platform required.

## Used by
[[topic-long-running-always-on-agents]]
