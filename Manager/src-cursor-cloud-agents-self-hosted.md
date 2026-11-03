---
tags: [manager-kb, source]
url: https://cursor.com/help/ai-features/background-agents.md ; /cloud-agents.md ; /self-hosted-machines.md ; https://cursor.com/docs/cloud-agent/self-hosted/pool.md
type: official-doc
author: Cursor (Anysphere)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (vendor docs, raw markdown)
---
# Cursor Cloud/Background Agents and Self-Hosted Machines (worker pools)
## Key claims
- Background agent definition: moves a task "to the cloud, where the agent takes it from start to finish without interruption and reports back with proof that the work is done" - screenshots, videos, logs attached to the PR "so you can validate the work without checking out the branch"; user can take over the agent's remote desktop.
- Start surfaces: IDE, web/mobile at cursor.com/agents, `@Cursor` in Slack/GitHub/Linear, schedules/events via Automations. Completion = Slack notification with PR link.
- "Move to Cloud" does not snapshot uncommitted files: the cloud agent starts from clean git state, transfers conversation + context only (handoff pitfall: commit/stash first).
- Cloud agents auto-fix CI failures on PRs they create (Teams/Enterprise), ignoring checks failing on base; opt-out with a PR comment.
- Self-hosted machines: agent loop (inference + planning) stays in Cursor cloud; the worker runs tool calls on your hardware. Worker opens a long-lived OUTBOUND HTTPS connection: "No inbound ports or VPN are required." `agent worker start --name devbox` (My Machines) or `agent worker --pool start` (team pool, service-account key).
- Dispatch model: pool = named routing target; "Requests wait in the pool until an available worker claims them"; "one Cloud Agent claims the worker at a time"; routing by key-value labels (reserved `repo`, `pool`); `--idle-release-timeout` (default 3600 s) keeps a worker alive after a session for follow-ups; health endpoints `/healthz /readyz /metrics` via `--management-addr`; k8s controller with `--warm-idle` pre-warmed workers; sessionStart/sessionEnd hooks fire on claim/release; per-claim session tokens and signed identity tokens; limits 200 workers/user, 1000/team; `--computer-use` lets agents click/type/screenshot on the worker.
## Quotable
> Requests wait in the pool until an available worker claims them.
> reports back with proof that the work is done

## Used by
[[topic-cross-device-agent-control]], [[topic-personal-assistant-agents]], [[topic-remote-mobile-ux]]
