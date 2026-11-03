---
tags: [manager-kb, source]
url: https://docs.temporal.io/encyclopedia/detecting-activity-failures
type: official-doc
author: Temporal Technologies
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (mature durable-execution system docs; transferable pattern, not agent specific)
---
# Temporal: detecting activity failures (timeouts and heartbeats)
## Key claims
- The service "doesn't detect failures when a Worker loses communication with the Server or crashes", so it relies on a Start-To-Close timeout to force retries; "We strongly recommend setting a Start-To-Close Timeout"; it must exceed the max possible runtime.
- Schedule-To-Start timeout = how long a task may wait for any worker (default infinity; non-retryable by design because a retry would re-enter the same queue); recommended to monitor schedule-to-start latency and have a plan to reroute to a different task queue.
- Heartbeat = periodic ping from the executing worker proving progress; use with a Heartbeat Timeout; for long tasks "use a relatively short Heartbeat Timeout and a frequent Heartbeat" so failures are handled in a timely manner.
- Heartbeats can carry a progress payload: if the attempt times out on a missed heartbeat, the next attempt reads the last payload and continues (resume instead of restart).
- Cancellation is delivered to activities on their next heartbeat; activities that don't heartbeat cannot receive a cancel.
- Heartbeats are throttled by the worker (default 30 s, max 60 s), so cancel delivery can lag.
## Quotable
> The Temporal Server doesn't detect failures when a Worker loses communication with the Server or crashes.

## Used by
[[topic-cross-device-agent-control]]
