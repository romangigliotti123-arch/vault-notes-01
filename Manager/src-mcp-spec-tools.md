---
tags: [manager-kb, source]
url: https://modelcontextprotocol.io/specification/draft/server/tools
type: spec
author: Model Context Protocol project
published: undated (draft spec, fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (normative spec text, draft version)
---
# MCP spec: Tools (draft)
## Key claims
- Tool fields: name, title, description, inputSchema (MUST be a valid object schema; no-param tools use `{"type":"object","additionalProperties":false}`), optional outputSchema, annotations. Annotations "MUST" be treated as untrusted unless from trusted servers.
- Names: SHOULD be 1-128 chars, case-sensitive, only A-Za-z0-9 _ - . ; unique within a server; aggregators SHOULD prefix with a server id because server names are not guaranteed unique.
- Servers SHOULD return tools in deterministic order (enables client caching and prompt-cache hits); tool list MUST NOT vary per connection except by authorization.
- Structured results: `structuredContent` conforming to `outputSchema`; for backward compat also return serialized JSON in a text block. Resource links allowed.
- Two error channels: JSON-RPC protocol errors (unknown tool, malformed request) vs tool-execution errors `isError:true` carrying "actionable feedback that language models can use to self-correct" (example: "Invalid departure date: must be in the future. Current date is 08/08/2025."). Clients SHOULD pass execution errors to the model.
- Stateful tools (non-normative): return an explicit handle from a creation tool; state retention/expiry in the creation tool's description; expired handle returns a tool error so the model can recover.
- Security: servers MUST validate inputs, enforce access control, rate limit, sanitize outputs; clients SHOULD confirm sensitive operations, show tool inputs before the call, validate results, time out, log. "there SHOULD always be a human in the loop with the ability to deny tool invocations".
## Quotable
> Tool Execution Errors contain actionable feedback that language models can use to self-correct and retry with adjusted parameters

## Used by
[[topic-tool-and-mcp-design]]
