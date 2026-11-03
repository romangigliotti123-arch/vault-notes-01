---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/telegram
type: repo
author: Anthropic (claude-plugins-official)
published: undated
accessed: 2026-10-29
reliability: high (README, ACCESS.md and server.ts read raw)
---
# Official Telegram channel plugin (README, ACCESS.md, server.ts)
## Key claims
- Tools: `reply` (chat_id, text, reply_to, files; images sent as photos, others as documents; max 50MB; auto-chunks text), `react` (fixed Telegram emoji whitelist only), `edit_message` (edit the bot's own message; "Useful for 'working...' -> result progress updates").
- Server instructions (server.ts ~line 411): "Edits don't trigger push notifications - when a long task completes, send a new reply so the user's device pings."
- Inbound messages trigger the "typing..." indicator automatically.
- Config keys (ACCESS.md): `ackReaction` (react on receipt, whitelist only), `replyToMode` first|all|off, `textChunkLimit` (<=4096, Telegram hard cap), `chunkMode` length|newline.
- server.ts already implements INLINE-BUTTON permission relay: callback data `perm:allow|deny|more:<id>`, a "See more" button expands tool details, buttons are replaced by the outcome text so a request cannot be answered twice; sender must be in allowFrom.
- `reply`/`edit_message` accept `format: "markdownv2"` (caller must escape) else plain text. The model-facing `reply` tool has NO buttons parameter: inline keyboards exist only for the built-in permission relay, so "approve/deny/choose" buttons for ordinary questions are not available without modifying or wrapping the plugin.
- The bot registers its own slash commands `/start`, `/help`, `/status` (status = "Check your pairing status", answered by the plugin, not by Claude), so there is no built-in "what are you doing" command; Telegram's own docs say commands appear in a menu button and inline keyboards "don't send messages to the chat" (core.telegram.org/bots/features).
- No history/search in the Bot API; photos are downloaded eagerly on arrival.
- Pairing, then set policy to allowlist.
## Quotable
> Edits don't trigger push notifications - when a long task completes, send a new reply so the user's device pings.

## Used by
[[topic-agent-security]], [[topic-remote-mobile-ux]]
