---
tags: [manager-kb, source]
url: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
type: spec
author: OpenTelemetry GenAI SIG
published: undated (repo main, conventions v1.44-era; Status: Development)
accessed: 2026-10-29
reliability: high (spec text read raw via curl; status Development = may change)
---
# OpenTelemetry GenAI semantic conventions: agent and framework spans
## Key claims
- Moved from open-telemetry/semantic-conventions to open-telemetry/semantic-conventions-genai (old page is a "moved" stub). Document **Status: Development** (not stable).
- Span types and names: `create_agent {gen_ai.agent.name}`, `invoke_agent {gen_ai.agent.name}` (client and internal variants), `invoke_workflow {gen_ai.workflow.name}`, `plan {...}`, `execute_tool {gen_ai.tool.name}`; also load-skill, read-skill-resource, command-execution spans. `gen_ai.operation.name` = create_agent | invoke_agent | execute_tool ...
- Attributes seen: `gen_ai.agent.id|name|description|version`, `gen_ai.conversation.id`, `gen_ai.tool.name|type|call.id|call.arguments|call.result|description|definitions`, `gen_ai.usage.input_tokens|output_tokens|cache_read.input_tokens|cache_write.input_tokens`. A companion `anthropic.md` sets `gen_ai.provider.name = "anthropic"`.
- Tool arguments/results and definitions are opt-in content (privacy).
- Takeaway for a one-box host: borrow the vocabulary (agent, conversation id, tool call id, usage fields) for the local job ledger/digest columns so that a later move to any OTLP backend is a mapping, not a redesign.

## Used by
[[topic-observability]]
