---
tags: [manager-kb, source]
url: https://docs.temporal.io/activity-definition
type: official-doc
author: Temporal Technologies
published: undated
accessed: 2026-10-29
reliability: high (vendor doc, framework origin)
---
# Temporal: Activity definition (idempotency, timeouts, heartbeats)
## Key claims
- "Activities should be designed to be safely executed multiple times without causing unexpected or undesired side effects." "You should always make your business logic Activities idempotent in Temporal."
- Because Activities may be retried "these functions may be executed more than once"; Temporal guarantees completion is observed exactly once (at-least-once execution, exactly-once observed result).
- Must specify at least one timeout, typically start_to_close ("how long to wait before assuming that an Activity is inactive").
- "your operation should either complete within a few minutes or it should heartbeat." Heartbeats show a long activity is progressing.
- "You should typically not write retry logic manually within your Activity Definition": retry policy lives in the platform and survives worker crashes. Companion page (why-temporal): on worker crash another worker "replays the Event History and resumes at the line where execution stopped."

## Used by
[[topic-long-running-always-on-agents]]
