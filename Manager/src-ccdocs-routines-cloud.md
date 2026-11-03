---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/routines.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (research preview)
accessed: 2026-10-29
reliability: high (official doc; read via saved fetch output and grep)
---
# Cloud scheduled tasks (formerly routines)
## Key claims
- Saved config (prompt + repos + connectors) run on Anthropic cloud on schedule, API POST (bearer token, `/fire` endpoint under beta header `experimental-cc-routine-2026-04-01`) or GitHub events. Pro/Max/Team/Enterprise; create at claude.ai/code/routines or `/schedule`.
- Research preview: "Behavior, limits, and the API surface may change."
- Runs start in auto mode (classifier) unless unavailable; repeated blocks cause a prompt that waits until someone answers. Claude pushes to `claude/`-prefixed branches. Actions appear as the user (commits, connector messages).
- Limits: scheduled runs 100/hour per account (waits for reset); Run now / API fires / one-off re-run 30/hour per task; "None of these hourly limits has overage". Runs draw on subscription usage; at limit, additional runs rejected until window reset unless usage credits on. Paused subscription => tasks on hold.
- Minimum schedule interval 1 hour. `/schedule why did my nightly review do nothing?` reads run history and logs (v2.1.227+).
- Cloud runs cannot touch the local PCs (fresh clone); suited to repo work and to a "watcher" that does not need local files.

## Used by
[[topic-long-running-always-on-agents]]
