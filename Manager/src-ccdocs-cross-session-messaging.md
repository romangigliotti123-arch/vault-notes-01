---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/cross-session-messaging
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (v2.1.224+; native Windows v2.1.234+)
accessed: 2026-11-01
reliability: high (official; full page read)
---
# Cross-session messaging
## Key claims
- Claude can list (`ListAgents`, `/list-agents`) and `SendMessage` to your other sessions on this machine, other machines and cloud sessions (the last two via Remote Control, through Anthropic servers). Plain text only; same-machine messages use a per-session socket or named pipe, never Anthropic servers.
- A message from another session is labelled as not from the user: it cannot approve permission prompts, change configuration or CLAUDE.md, or run slash commands; the receiver's permission rules still apply.
- `crossSessionInbound` accept|hold|refuse. Unset default: a receiving session that BYPASSES permissions HOLDS each message for human approval unless the sender also bypasses; the dialog expires after `dialogExpiry` (5 min) and drops the message; `claude -p` cannot show the dialog (needs `accept` in its --settings to take messages unattended). At most 100 held, 50 queued; loops are throttled.
- `SendMessage` `notify_when_idle` gives a one-time notice when another local session next goes idle or exits (12 h limit, no tokens spent in the watched session). Only the main conversation can subscribe.
- A delivered message costs like a typed prompt (full context re-sent when the receiver is idle); `crossSessionInbound: hold` stops idle spend.
- `isolatePeerMachines: true` requires approval before any message leaves the machine, even in bypass mode. Deny `SendMessage` and `ListAgents` to disable.
## Used by
[[topic-cross-device-agent-control]], [[topic-claude-code-features]], [[topic-agent-security]]
