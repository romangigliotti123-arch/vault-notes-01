---
tags: [manager-kb, source]
url: https://blog.cloudflare.com/code-mode/
type: eng-blog
author: Cloudflare
published: 2025-09-26
accessed: 2026-10-29
reliability: med-high (vendor, no benchmark numbers in the post itself)
---
# Code Mode: the better way to use MCP
## Key claims
- Convert MCP tools to a typed TypeScript API; the model writes code that calls it. "LLMs are better at writing code to call MCP, than at calling MCP directly" (models have seen far more real TypeScript than tool-call examples).
- Chained calls keep intermediate results out of the model's context.
- Sandbox: fresh V8 isolate per snippet, no internet (`fetch()`/`connect()` throw); only bindings to connected MCP servers. Supervisor holds tokens and attaches them, "generated code never sees API keys".
- Caveats: Worker Loader API closed beta; post gives no benchmark figures. Secondary reports (WorkOS, not opened) claim 32% fewer tokens on simple and 81% on complex tasks; a later server-side variant exposes only `search()` and `execute()` (snippet only).
- Companion to Anthropic's [[src-anthropic-code-execution-with-mcp]].
## Quotable
> LLMs are better at writing code to call MCP, than at calling MCP directly.

## Used by
[[topic-tool-and-mcp-design]]
