---
tags: [manager-kb, source]
url: https://rogs.me/2026/02/claude-code-from-the-beach-my-remote-coding-setup-with-mosh-tmux-and-ntfy/
type: practitioner-blog
author: rogs
published: 2026-02
accessed: 2026-10-29
reliability: med (single practitioner, working setup, no measurements)
---
# Claude Code from the beach: mosh + tmux + ntfy
## Key claims
- Architecture: phone (Termux) -mosh/WireGuard-> home jump box -ssh-> work PC running Claude Code in tmux; self-hosted ntfy for push.
- Two kinds of resilience: mosh for the flaky mobile leg (roaming, dead zones, phone sleep), tmux for session persistence.
- Notification policy via Claude Code hooks, three events only: AskUserQuestion (Claude needs input) = HIGH priority; Stop (task finished) = default priority; Error = HIGH. The script checks `SSH_CONNECTION` so notifications fire only when NOT actively attached (avoid pinging someone already looking).
- ntfy hygiene: per-topic access token with expiry (`ntfy token add --expires=30d`), topic denied to everyone else (`ntfy access everyone claude-code deny`).
- Loop described: give a task, pocket the phone, phone buzzes on question/finish, respond, pocket again.
## Quotable
> mosh handles the flaky mobile connection... while tmux handles session persistence

## Used by
[[topic-cross-device-agent-control]], [[topic-remote-mobile-ux]]
