---
tags: [manager-kb, source]
url: https://github.com/matt1398/claude-devtools
type: repo
author: matt1398
published: undated
accessed: 2026-10-29
reliability: med (OSS desktop app; README via summariser)
---
# claude-devtools
## Key claims
- Desktop app + Docker option that "reads the Claude Code logs and session transcripts already saved to ~/.claude/". Does not sit between you and Claude Code.
- Features: isolated execution trees per subagent with tool traces, token metrics, duration, cost; per-turn token attribution across 7 categories (CLAUDE.md, skills, tool I/O, thinking...); compaction visualisation; SSH remote session inspection; notification triggers; export Markdown/JSON; cross-session search.
- Windows .exe installer (may trigger SmartScreen; SmartScreen is disabled on this host); MIT licence. Docker mode serves on localhost:3456.
- It needs a GUI/browser to view: use on demand, not as a service.

## Used by
[[topic-observability]]
