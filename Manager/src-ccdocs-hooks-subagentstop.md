---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/hooks.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (CC 2.1.3xx era)
accessed: 2026-10-29
reliability: high (official; sections SubagentStop, stop decision control, prompt/agent hooks read)
---
# Claude Code hooks: SubagentStop and verification hooks
## Key claims
- `SubagentStop` fires when a subagent finishes; input includes `agent_id`, `agent_type`, `agent_transcript_path` (nested `subagents/` folder), `last_assistant_message` ("the text content of the subagent's final response"), `stop_hook_active`, plus `background_tasks`.
- Decision control: "Returning `decision: "block"` with a `reason` keeps the subagent running and delivers `reason` to the subagent as its next instruction. A hook that blocks by exiting 2 delivers its stderr message the same way." Loop protections: `stop_hook_active` and an 8-consecutive-continuation cap. `hookSpecificOutput.additionalContext` gives non-error feedback and keeps it running.
- To inject context into the PARENT after a subagent returns, use a `PostToolUse` hook on the `Agent` tool.
- On v2.1.271+ a subagent using the `SubagentHandback` tool delivers its report through that tool; `last_assistant_message` is then only the closing text and the report is the call's `tool_input.message` (hookable via Pre/PostToolUse matcher `SubagentHandback`).
- Hook handler types: `command`, `http`, `mcp_tool`, `prompt` (single LLM call decides allow/block) and `agent` (spawns an agentic verifier with tool access, default timeout 60 s). Stop/SubagentStop support all five.
- Exit code 2 blocks on Stop/SubagentStop; a missing script file is treated as a non-blocking error.
- Notification types include `agent_needs_input` and `agent_completed`.

## Used by
[[topic-report-formats-and-verification]]
