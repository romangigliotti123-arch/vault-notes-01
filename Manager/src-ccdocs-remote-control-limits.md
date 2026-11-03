---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/remote-control.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; Limitations section read verbatim via saved fetch)
---
# Remote Control: limitations relevant to an unattended master
## Key claims
- "Local process must keep running": if the `claude` process stops the session goes offline until brought back (`--continue`/`--resume`).
- Interactive session + extended network outage: "Claude Code retries for as long as the outage lasts and reconnects on its own". Server mode (`claude remote-control`) gives up after ~10 minutes and the process EXITS.
- "Presence heartbeats failing": an interactive session can disconnect with `could not reach the Remote Control server for about 30 minutes`; fix is to run `/remote-control` (a LOCAL action - cannot be done from the phone because the phone cannot reach a disconnected session).
- HTTP 403 refusals retried up to 3 minutes then disconnect. Forwarded non-permission dialogs expire after 5 minutes (`dialogExpiry`); permission prompts and AskUserQuestion stay open until answered.
- While connected the session transcript is stored on Anthropic servers (retention per Data usage policy).
- Crashed sessions in server mode are re-served when a connected device sends a message (v2.1.238+).

## Used by
[[topic-long-running-always-on-agents]]
