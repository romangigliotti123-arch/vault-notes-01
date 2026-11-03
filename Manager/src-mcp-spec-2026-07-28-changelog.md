---
tags: [manager-kb, source]
url: https://modelcontextprotocol.io/specification/2026-07-28/changelog
type: spec
author: Model Context Protocol project
published: 2026-07-28 (spec revision date)
accessed: 2026-10-29
reliability: high (official changelog page, read in part)
---
# MCP specification 2026-07-28: Key Changes (vs 2025-11-25)
## Key claims
- Stateless core: no `initialize` handshake and no `Mcp-Session-Id` on Streamable HTTP; each request carries protocol version + client capabilities in `_meta`; `server/discover` RPC advertises versions/capabilities/identity. Cross-call state uses explicit server-minted handles passed as ordinary tool arguments.
- Tasks moved out of core into official extension `io.modelcontextprotocol/tasks`: polling via `tasks/get`, new `tasks/update` for client-to-server input, `tasks/list` removed, servers may return task handles unsolicited (SEP-2663). Matches the "submit, poll, resume" shape needed for long agent jobs.
- Multi Round-Trip Requests: server returns `InputRequiredResult` (`resultType: "input_required"`) carrying `inputRequests`; client re-sends with `inputResponses`. Every result has `resultType` "complete" or "input_required". (Interactive pause = typed result, not a hidden hang.)
- "Remove SSE stream resumability and message redelivery (Last-Event-ID)... A broken response stream loses the in-flight request; clients MUST re-issue it as a new request with a new request ID." => long work must be handle/poll based, not stream based.
- OpenTelemetry trace context (`traceparent`, `tracestate`, `baggage`) propagated in `_meta`; deterministic tools/list order recommended for prompt-cache hits; `ttlMs`/`cacheScope` on list results; client credentials bound to issuing authorization server.
## Quotable
> A broken response stream loses the in-flight request; clients MUST re-issue it as a new request with a new request ID.

## Used by
[[topic-cross-device-agent-control]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-tool-and-mcp-design]]
