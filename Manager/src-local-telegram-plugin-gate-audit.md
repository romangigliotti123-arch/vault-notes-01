---
tags: [manager-kb, source]
url: ~\.claude\plugins\cache\claude-plugins-official\telegram\0.0.7\server.ts + ~\.claude\channels\telegram\access.json (IDs not recorded here)
type: local-audit
author: F1 research worker
published: 2026-10-29
accessed: 2026-10-29
reliability: high (read the code and config on this host)
---
# Local audit: Telegram channel gate and access.json
## Key claims
- `access.json` has `dmPolicy:"allowlist"` with ONE user ID in `allowFrom` (good), plus a `groups` entry for one group chat ID with `requireMention:true` and `allowFrom:[]`.
- `gate()` in server.ts (lines ~277-292): for group/supergroup messages, `if (groupAllowFrom.length > 0 && !groupAllowFrom.includes(senderId)) drop`. With an EMPTY group `allowFrom`, the sender check is skipped; delivery then depends only on `requireMention` (@bot mention or reply). So ANYONE in that group who mentions the bot can inject text into the session. Docs say the opposite for channels: "Gate on the sender's identity, not the chat or room identity ... gating on the room would let anyone in an allowlisted group inject messages into the session" ([[src-ccdocs-channels]]).
- DM gating, pairing and `assertSendable` (refuses to send files from the channel state dir) look sound. `download_attachment` writes into `inbox/` (Telegram caps at 20 MB); attachments are untrusted content.
- Status: boot-claude.ps1 (2026-10-28) now starts the normal session WITHOUT `--channels`, so inbound Telegram is currently not injected, but CLAUDE.md still describes Telegram as live, the plugin is enabled in settings.json (reply/react tools exist in the session), and re-adding `--channels` re-arms the group hole.
- Not verified: whether the bot is actually still a member of that group, or whether BotFather "allow groups" is on.

## Used by
[[topic-agent-security]]
