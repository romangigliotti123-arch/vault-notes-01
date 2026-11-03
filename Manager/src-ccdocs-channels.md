---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/channels.md (+ channels-reference.md)
type: official-doc
author: Anthropic
published: undated (research preview, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc, raw markdown)
---
# Claude Code docs: Channels and Channels reference
## Key claims
- A channel is an MCP server that pushes events into a running session; two-way ones expose a reply tool. Telegram, Discord, iMessage plugins (Bun scripts) are in research preview; `--channels` accepts only Anthropic-allowlisted plugins; the flag is not shown in `claude --help`.
- "When Claude replies through a channel, you see the inbound message in your terminal but not the reply text" (terminal shows tool call + "sent").
- Events only arrive while the session is open: "for an always-on setup you run Claude in a background process or persistent terminal."
- Permission relay: a channel declaring the `claude/channel/permission` capability receives `notifications/claude/channel/permission_request` (request_id = 5 letters a-z without `l`, tool_name, description, input_preview). Verdict `notifications/claude/channel/permission` with request_id + behavior allow|deny; the first answer (terminal or remote) wins and closes the other. Covers Bash/Write/Edit only; project trust and MCP consent dialogs are NOT relayed. A verdict affects one call only.
- "Anyone who can reply through the channel can approve or deny tool use in your session, so only allowlist senders you trust with that authority."
- `-p` mode disables multiple-choice questions and plan approval so the session never stalls.
- description/input_preview are sanitised (v2.1.211+): direction-override and invisible chars neutralised.
- In bypassPermissions there are no prompts to relay, so relay is moot for the master (it only applies to actions "no mode auto-approves").
## Quotable
> The local terminal dialog stays open through all of this. If someone at the terminal answers before the remote verdict arrives, that answer is applied instead.

## Used by
[[topic-agent-security]], [[topic-remote-mobile-ux]]
