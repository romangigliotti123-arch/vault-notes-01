---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-view.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; first 100k of 148k chars read)
---
# Agent view: supervision, failure recovery, state reference
## Key claims
- Background sessions run under a **supervisor** service; each session is its own process. Exited unexpectedly while supervisor runs => supervisor restarts it; a session you killed yourself is marked stopped. Idle/finished sessions unattached ~1 h are stopped to free resources (conversation stays on disk; replying resumes; pin with Ctrl+T to keep alive).
- Sleep: sessions preserved. "Shutting down or restarting your machine stops running background sessions." Within 48 h they show **failed** (attach/reply restarts from saved conversation); after 48 h **stopped** ("ended while the background service was off").
- `claude respawn <id>|--all` restarts sessions (e.g. to pick up a new binary). Permission mode, model, effort persist across supervisor restarts.
- `claude agents --json [--all] [--cwd]` fields: cwd, kind (interactive|background), startedAt, id, state (working|blocked|done|failed|stopped), pid, status (busy|waiting|idle), waitingFor (permission prompt|input needed|sandbox request|worker request|dialog open), sessionId, name. Docs: files under `~/.claude/jobs/<id>/` "are not a stable interface" - use the command.
- `claude daemon status|logs|stop --any [--keep-workers]`; supervisor log `~/.claude/daemon.log` (no rotation policy stated). `claude rm <id>` deletes a row; transcripts kept per `cleanupPeriodDays`.
- The master here is an INTERACTIVE session (kind: interactive) started by Task Scheduler, so the supervisor does NOT restart it; only bg sessions get that.

## Used by
[[topic-long-running-always-on-agents]], [[topic-observability]]
