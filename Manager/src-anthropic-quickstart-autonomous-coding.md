---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding
type: repo
author: Anthropic (claude-quickstarts)
published: undated
accessed: 2026-10-29
reliability: high (official reference implementation of the harness blog)
---
# claude-quickstarts / autonomous-coding
## Key claims
- Two-agent pattern: initializer (session 1) reads `app_spec.txt`, writes `feature_list.json` (200 test cases), inits git; coding agent (sessions 2+) implements features one by one and flips them to passing. `feature_list.json` is "Test cases (source of truth)"; `claude-progress.txt` = session notes.
- Auto-continues between sessions after a 3 s delay; `--max-iterations` default unlimited; Ctrl+C pauses, same command resumes (state in files + git).
- Defence in depth: OS sandbox, filesystem restricted to project dir, bash allowlist enforced by a security hook.

## Used by
[[topic-long-running-always-on-agents]]
