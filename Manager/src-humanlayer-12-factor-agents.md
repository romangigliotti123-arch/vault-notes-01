---
tags: [manager-kb, source]
url: https://github.com/humanlayer/12-factor-agents (README; content/factor-06, factor-07, factor-11 read)
type: repo
author: Dex Horthy (HumanLayer)
published: 2025 (talk at AI Engineer World's Fair; repo ~27k stars, CC BY-SA content)
accessed: 2026-10-29
reliability: med (influential practitioner framework; opinion, no benchmarks; factors 6/7/11 read in full, others via README titles)
---
# 12-Factor Agents (Dex Horthy): factors relevant to human approval and triggering
## Key claims
- Thesis: "most of the products out there billing themselves as 'AI Agents' are not all that agentic ... mostly deterministic code, with LLM steps sprinkled in"; agents are "mostly just software"; builders mostly roll their own stack instead of frameworks. Factors: 1 NL to tool calls, 2 own your prompts, 3 own your context window, 4 tools are structured outputs, 5 unify execution and business state, 6 launch/pause/resume with simple APIs, 7 contact humans with tool calls, 8 own your control flow, 9 compact errors into context, 10 small focused agents, 11 trigger from anywhere, 12 stateless reducer.
- Factor 6: agents should be launchable/pausable/resumable through simple APIs; "often AI orchestrators will allow for pause and resume, but not between the moment of tool selection and tool execution" (the gap that Claude Code's `PreToolUse` `defer`/`ask` and permission prompts fill).
- Factor 7: model human contact as a tool call (`request_human_input` with `urgency`, `format: free_text|yes_no|multiple_choice`, `choices`); save state, notify, break the loop, resume on a webhook with the thread id. Maps to Claude Code `AskUserQuestion`/permission prompts surfaced over Remote Control.
- Factor 11: trigger from Slack/email/SMS and respond there; "Outer Loop Agents" triggered by crons/events may work "5, 20, 90 minutes, but when they get to a critical point, they can contact a human for help, feedback, or approval"; "High Stakes Tools: If you're able to quickly loop in a variety of humans, you can give agents access to higher stakes operations like sending external emails, updating production data" with auditability. This is exactly Roman's confirm-first list implemented as approvals rather than prohibitions.
- Factor 10 (title only here): small, focused agents; HumanLayer's later post says role-based subagents ("frontend engineer") do not work, context-control subagents do (see [[src-humanlayer-skill-issue-harness]]).
## Quotable
> "High Stakes Tools: If you're able to quickly loop in a variety of humans, you can give agents access to higher stakes operations"

## Used by
[[topic-claude-code-features]]
