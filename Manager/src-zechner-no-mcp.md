---
tags: [manager-kb, source]
url: https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/
type: practitioner-blog
author: Mario Zechner
published: 2025-11-02
accessed: 2026-10-29
reliability: med-high (practitioner with measured token counts; opinionated)
---
# What if you don't need MCP at all?
## Key claims
- Thesis: for narrow tasks, agents with Bash + code can call small CLI scripts instead of broad MCP servers; popular MCP servers expose many tools with long descriptions that burn context and confuse the agent.
- Numbers: Playwright MCP ~13.7k tokens for 21 tools (6.8% of context); Chrome DevTools MCP ~18.0k tokens for 26 tools (9.0%); his equivalent CLI README ~225 tokens, read only when needed.
- Composability: outputs saved to files, chained in one Bash command, formatted as the author wants; adding a tool takes minutes; prefix script names to avoid collisions.
- No new benchmark in this post; refers to an earlier "very light" one concluding both approaches can be efficient if used carefully.
- Note: Claude Code's tool search (deferred loading) since reduced the fixed cost he measures, see [[src-ccdocs-mcp]].
## Quotable
> This efficiency comes from the fact that models know how to write code and use Bash.

## Used by
[[topic-tool-and-mcp-design]]
