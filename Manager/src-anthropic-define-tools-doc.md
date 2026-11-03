---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
type: official-doc
author: Anthropic (platform docs)
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc)
---
# Anthropic docs: Define tools (best practices for tool definitions)
## Key claims
- "Provide extremely detailed descriptions. This is by far the most important factor in tool performance": what it does, when to use it AND when not to, what each parameter means, caveats/limits, what it does NOT return. "Aim for at least 3-4 sentences for each tool description, more if the tool is complex."
- Consolidate related operations into fewer tools with an `action` parameter (rather than create_pr / review_pr / merge_pr); namespace names by service (`github_list_prs`) especially with tool search.
- Return only high-signal information: semantic stable identifiers, only fields needed for the next step; bloated responses waste context.
- `input_examples` (schema-validated) for complex/format-sensitive inputs; costs ~20-50 tokens simple, ~100-200 nested.
- Ask for an explanation, not "reasoning", in parameters (a reasoning-extraction parameter can trigger a refusal).
- Forced tool use (`tool_choice any/tool`) is not supported on Opus 5.5 / Sonnet 5.5 / Fable 5.1 (400 error); use `auto` + strict tool use. (Relevant to scripted API use, not to Claude Code.)
## Quotable
> Provide extremely detailed descriptions. This is by far the most important factor in tool performance.

## Used by
[[topic-tool-and-mcp-design]]
