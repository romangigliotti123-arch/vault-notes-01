---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/code-execution-with-mcp
type: eng-blog
author: Adam Jones, Conor Kelly
published: 2025-11-04
accessed: 2026-10-29
reliability: high (primary; token numbers are one illustrative example)
---
# Code execution with MCP
## Key claims
- Two costs: all tool definitions loaded up front; every intermediate result passes through the model (a 2-hour transcript copied between tools ~50,000 tokens).
- Fix: expose MCP servers as code APIs in a filesystem tree (./servers/google-drive/getDocument.ts); agent reads only needed files (progressive disclosure) and filters/aggregates data in code before it reaches the model. Example 150,000 -> 2,000 tokens (98.7%). A 10,000-row sheet: agent sees 5 rows.
- Also: loops/conditionals in code, privacy (tokenised PII never enters context), persisting state and reusable functions as skills.
- Drawback: needs a sandbox, resource limits, monitoring.
## Quotable
> "Every intermediate result must pass through the model."

## Used by
[[topic-agent-security]], [[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-tool-and-mcp-design]]
