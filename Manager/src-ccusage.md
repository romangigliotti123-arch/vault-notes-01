---
tags: [manager-kb, source]
url: https://github.com/ryoppippi/ccusage
type: repo
author: ryoppippi
published: undated
accessed: 2026-10-29
reliability: med-high (popular OSS CLI; README fetched via summariser)
---
# ccusage: token/cost analysis from local agent-CLI data
## Key claims
- CLI: "Analyze coding (agent) CLI token usage and costs from local data." Supports Claude Code and other CLIs. Commands: `daily`, `monthly`, `weekly`, `session`, `blocks` (Claude Code 5-hour billing windows), `statusline` (beta), `--json`, `--since/--until`, `--instances` (group by project), `--timezone`, `--offline`.
- Run without install: `npx ccusage@latest`.
- Cost = tokens x LiteLLM pricing file (API-equivalent USD, NOT what a subscription bills); override prices in `ccusage.json`. README does not say how close to a real bill.
- Reads local data only (README does not name the files; it is understood to read ~/.claude/projects JSONL; not stated on the fetched page).
- For a subscription host the useful outputs are token counts per day/session/5-hour block, not dollars.

## Used by
[[topic-long-running-always-on-agents]], [[topic-observability]]
