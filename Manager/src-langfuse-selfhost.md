---
tags: [manager-kb, source]
url: https://langfuse.com/self-hosting
type: official-doc
author: Langfuse
published: undated
accessed: 2026-10-29
reliability: high (vendor doc; acquisition fact from search snippets of langfuse.com/blog/joining-clickhouse and clickhouse.com blog, snippet only)
---
# Langfuse self-hosting requirements
## Key claims
- Components: Langfuse Web + Worker containers, PostgreSQL (transactional), ClickHouse (observability data), Redis/Valkey (cache + queue), S3/blob (raw events, attachments). Docker Compose is for "local use and testing", "Single VM without high availability, scaling, or backups".
- Six moving parts (4 stateful) for one box; no minimum-resource numbers on the page.
- Search snippets (not opened): ClickHouse acquired Langfuse, announced 2026-01-16; posts say MIT licence and self-hosting continue.
- Verdict for us: too heavy for a low-cost dedicated Windows box whose main job is something else; no Docker is mentioned on the host (CLAUDE.md lists none for Windows).

## Used by
[[topic-observability]]
