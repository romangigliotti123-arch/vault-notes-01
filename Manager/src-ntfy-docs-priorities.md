---
tags: [manager-kb, source]
url: https://docs.ntfy.sh/publish/
type: official-doc
author: ntfy project
published: undated
accessed: 2026-10-29
reliability: high (official doc)
---
# ntfy: publishing and message priority
## Key claims
- Five priorities set by header `Priority`/`X-Priority`/`p`: 5 max/urgent (really long vibration bursts, pop-over), 4 high (long vibration, pop-over), 3 default, 2 low ("No vibration or sound. Notification will not visibly show up until notification drawer is pulled down"), 1 min (under the fold in "Other notifications"). Android can map custom sounds/vibration patterns per priority.
- Plain HTTP POST publish (curl one-liner) with title and tags; works from any script or hook, so a hook can push without an MCP channel. Relevant as an independent out-of-band alert path if the Telegram/RC session itself is dead.
- Used in practice by [[src-rogs-claude-code-mosh-tmux-ntfy]] with hook events mapped to priorities.
## Quotable
> Low priority: No vibration or sound. Notification will not visibly show up until notification drawer is pulled down.

## Used by
[[topic-remote-mobile-ux]]
