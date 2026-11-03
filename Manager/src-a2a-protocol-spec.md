---
tags: [manager-kb, source]
url: https://a2a-protocol.org/latest/specification/
type: spec
author: A2A project (originated at Google, now Linux Foundation project)
published: undated (latest spec, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (normative spec, full page read)
---
# Agent2Agent (A2A) Protocol specification
## Key claims
- Core objects: Agent Card (JSON identity/capabilities/skills/endpoint/auth), Message (role user|agent, Parts), Task (stateful unit of work with unique ID), Artifact (output as Parts), Context (groups related tasks), Extension.
- Task states: SUBMITTED, WORKING, COMPLETED, FAILED, CANCELED, REJECTED, plus the two interrupted states INPUT_REQUIRED and AUTH_REQUIRED. Terminal = COMPLETED/FAILED/CANCELED/REJECTED; "Messages sent to Tasks that are in a terminal state... cannot accept further messages" (follow-up = new task in same contextId).
- Three delivery modes for long work: blocking send (waits for terminal or interrupted state), streaming (SSE with status/artifact updates; stream MUST close at terminal state), and push notifications (server POSTs to a client webhook on state change); polling `GetTask` always works. Non-blocking mode: `return_immediately: true` returns a task in WORKING/SUBMITTED.
- Idempotency: Get ops idempotent; Send may use `messageId` to detect duplicates; Cancel idempotent; delete of push config idempotent.
- AUTH_REQUIRED: agent asks client for credentials out-of-band; "Agents MUST NOT treat the TASK_STATE_AUTH_REQUIRED state transition, by itself, as authorization"; a credential obtained there must not be assumed to authorise later messages.
- Takeaway for us: a ready-made small state vocabulary (submitted/working/input-required/auth-required/completed/failed/canceled/rejected) that maps onto our RESULT/NEEDS report fields, and the rule that an interrupted task is resumable by messaging the same task ID.
## Quotable
> Agents MUST NOT treat the TASK_STATE_AUTH_REQUIRED state transition, by itself, as authorization for any particular operation.

## Used by
[[topic-cross-device-agent-control]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
