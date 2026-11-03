---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-sdk/subagents
type: official-doc
author: Anthropic (Claude Code / Agent SDK docs)
published: undated (current; mentions Claude Code v2.1.302 forks, v2.1.210 output scanning)
accessed: 2026-10-29
reliability: high (official)
---
# Subagents in the SDK
## Key claims
- Four benefits: context isolation (only the subagent's final message returns; "The parent receives a concise summary, not every file the subagent read"), parallelisation, specialised instructions, tool restrictions ("A tool you leave out isn't in the subagent's session at all").
- What a non-fork subagent receives: its own system prompt + the Agent tool's prompt string + project CLAUDE.md (unless `omitClaudeMd`) + tool definitions. It does NOT get the parent's conversation, tool results, or system prompt. "The only content you pass from parent to subagent is the Agent tool's prompt string, so include any file paths, error messages, or decisions the subagent needs directly in that prompt." Forks (v2.1.302+) copy the conversation instead.
- By default spawned subagents run in the background (`status: "async_launched"`, report arrives in a later turn); Claude waits only when its next action needs the report.
- The parent may summarise the subagent report in its own response; to keep it verbatim, say so. Since v2.1.210 the final message is scanned for instruction-shaped patterns (control tags neutralised, turn markers escaped, `[harness: ...]` marker prepended) - subagent output is treated as untrusted-ish.
- Resume: completed subagents return `agentId`; resumed subagent keeps full history; Explore/Plan are one-shot (no agentId). `maxTurns` stop is marked partial and resumable.
- Caps (v2.1.219+): depth `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` default 3 (1 = no nesting), concurrency `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` default 20, spend `max_budget_usd` (refuses spawns with "Budget limit reached", stops background subagents, ends with `error_max_budget_usd`). "Claude decides on its own when to spawn a subagent and how many... one prompt can grow into a tree of agents."
- AgentDefinition fields: description, prompt, tools, disallowedTools, model, skills (max 32), memory, mcpServers, maxTurns, autoCompactWindow (100k-1M), background, omitClaudeMd, effort, permissionMode.
- Opus 5 with the `claude_code` preset: Claude Code adds a line telling Claude not to call the Agent tool unless asked; with a custom/omitted system prompt that line is absent - add your own delegation instruction.
- For dozens to hundreds of agents use the Workflow tool (script runs outside the conversation context).
## Quotable
> "The only content you pass from parent to subagent is the Agent tool's prompt string"
> "one prompt can grow into a tree of agents."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
