---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high: official API doc
---
# Tool search tool (platform docs)
## Key claims
- Two server-side variants: regex (Python re.search patterns, max 200 chars) and bm25 (natural language, max 500 chars). Searches tool names, descriptions, argument names and argument descriptions.
- defer_loading: true keeps a tool out of context until discovered; at least one tool must be non-deferred; keep the 3-5 most used tools non-deferred. Max 10,000 deferred tools per request; 5 results by default, Claude can set limit 1-10,000.
- "Claude's ability to pick the right tool degrades once you exceed 30-50 available tools." Typical 5-server MCP setup ~55k tokens of definitions; tool search typically cuts it by over 85%.
- Use tool search when 10+ tools, definitions >10k tokens, selection accuracy dropping, 200+ MCP tools, or a growing library.
- Best practices: clear names/descriptions, consistent namespacing prefix so one search matches the group, keywords in descriptions matching how users describe tasks, a system-prompt section listing tool categories, and 'Monitor which tools Claude discovers to refine your descriptions.'
- Custom client-side search (embeddings etc.) is supported by returning tool_reference blocks from your own tool; cookbook recipe 'tool search with embeddings' exists.
- Deferred tools are appended inline so the prompt-cache prefix is untouched.
## Quotable
> "Add common keywords to tool descriptions to improve discoverability."

## Used by
[[topic-agent-security]], [[topic-skill-library-retrieval]], [[topic-tool-and-mcp-design]]
