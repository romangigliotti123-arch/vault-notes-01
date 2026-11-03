---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-plugins-official (plugins/plugin-dev/skills/agent-development, plugins/feature-dev/agents/code-reviewer.md, plugins/hookify, claude-md-management, receipts, claude-code-setup READMEs)
type: repo
author: Anthropic
published: undated (main branch read 2026-10-29)
accessed: 2026-10-29
reliability: high (first-party plugins; READMEs and two source files read in full)
---
# anthropics/claude-plugins-official: agent-writing guidance and maintenance plugins
## Key claims
- `plugin-dev/skills/agent-development` (v0.1.0) teaches: description is "the most critical field - it is loaded into context whenever the agent is registered, so the harness can decide when to dispatch". Required content: "Use this agent when [conditions]. Typical triggers include [scenario 1 in prose], [scenario 2...]" plus a pointer to a "When to invoke" section IN THE BODY with 2-4 worked scenarios (earlier community practice put `<example>` blocks in the description; Anthropic's current template moved the examples into the body, which keeps the always-loaded text short). Cover proactive and reactive triggering, different phrasings, and "Be specific about when NOT to use the agent". Name: lowercase-hyphen 3-50 chars; avoid generic `helper`. `tools`: least privilege, e.g. read-only `["Read","Grep","Glob"]`. `model: inherit` recommended unless a specific capability is needed. System prompt in second person; sections: core responsibilities, analysis process, quality standards, output format, edge cases; keep under 10,000 characters.
- `feature-dev/agents/code-reviewer.md` is a model reviewer subagent: `model: sonnet`, read-only tool list, "confidence-based filtering": every finding scored 0-100 with defined anchors (0 false positive, 25 might be real, 50 real but nitpick, 75 highly confident, 100 certain) and "Only report issues with confidence >= 80 ... quality over quantity"; output grouped by severity with file:line and concrete fix; "If no high-confidence issues exist, confirm the code meets standards with a brief summary." (A report format designed to suppress the always-finds-something failure mode.)
- `hookify`: turn a sentence into a hook rule file ("/hookify Warn me when I use rm -rf commands" creates `.claude/hookify.warn-rm.local.md`; regex patterns + message; "No restart needed! Rules take effect on the very next tool use"). Low-friction way to author guard hooks, but it is a plugin that itself installs hooks (review before use).
- `claude-md-management`: skill `claude-md-improver` (audit CLAUDE.md files against the current codebase, with quality scores) + command `/revise-claude-md` (capture learnings at end of session): periodic maintenance vs session-end capture.
- `receipts`: `/receipts [week|quarter|N|for repo]` builds a markdown + HTML usage report from your own session transcripts (sessions, active days, share by project, files/lines/commits/PRs); nothing published. `claude-code-setup`: read-only skill that recommends the top 1-2 hooks/skills/MCP/subagents/commands for a codebase. Other plugins listed: `ralph-loop`, `security-guidance`, `pr-review-toolkit`, `code-simplifier`, `skill-creator`, `session-report` (README 404), `explanatory-output-style`, `learning-output-style`.
## Quotable
> "This is the most critical field - it is loaded into context whenever the agent is registered, so the harness can decide when to dispatch."
> "Only report issues with confidence ≥ 80. Focus on issues that truly matter - quality over quantity."

## Used by
[[topic-claude-code-features]]
