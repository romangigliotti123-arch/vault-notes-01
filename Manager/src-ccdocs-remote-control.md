---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/remote-control.md
type: official-doc
author: Anthropic
published: undated (docs, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc, raw markdown fetched with curl)
---
# Claude Code docs: Remote Control
## Key claims
- Push to phone: "Claude decides when to push. It typically sends one when a long-running task finishes or when it needs a decision from you to continue. You can also request a push in your prompt, for example `notify me when the tests finish`. Beyond the two on/off toggles below, there is no per-event configuration."
- Two toggles in `/config`: "Push when Claude decides" (proactive) and "Push when actions required" (permission prompts + questions).
- Push is skipped while the user types in / focuses the connected terminal. `CLAUDE_CLIENT_PRESENCE_FILE` = marker file path: pushes skipped while the file exists (a screen-lock listener can create/delete it).
- iOS Focus modes / notification summaries and Android battery optimisation can delay or suppress pushes. "No mobile registered" in /config means open the Claude app so it refreshes its push token.
- Permission prompts and `AskUserQuestion` stay open until answered (no timeout). Other forwarded dialogs (e.g. model-choice after a safety refusal) wait 5 min then take the no-action default; `dialogExpiry` setting adjusts (v2.1.224+).
- One remote session per interactive process; the local process must keep running; an interactive session retries network outage indefinitely; server mode (`claude remote-control`) gives up after ~10 min of outage and exits; presence-heartbeat failure (~30 min) needs `/remote-control`; HTTP 403 retries up to 3 min.
- Commands that work from phone/web as text: /compact /clear /context /usage /exit /recap /reload-plugins; with an argument: /model /effort /fast /color /rename /config key=value /autocompact /advisor /output-style (built-in styles only) /focus /mcp (text summary). Local-only: /plugin, /resume.
- Connector re-auth cannot be done from the phone; a line starting with `!` from phone goes to Claude as a message, not to a shell.
- Transcript (messages, responses, tool activity) is stored on Anthropic servers while connected.
## Quotable
> Claude decides when to push. It typically sends one when a long-running task finishes or when it needs a decision from you to continue.
> Claude Code keeps permission prompts and `AskUserQuestion` questions open until you answer them.

## Used by
[[topic-context-window-management]], [[topic-cross-device-agent-control]], [[topic-model-effort-routing-cost]], [[topic-personal-assistant-agents]], [[topic-remote-mobile-ux]]
