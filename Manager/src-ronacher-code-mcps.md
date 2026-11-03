---
tags: [manager-kb, source]
url: https://lucumr.pocoo.org/2025/8/18/code-mcps/
type: practitioner-blog
author: Armin Ronacher
published: 2025-08-18
accessed: 2026-10-29
reliability: med (practitioner opinion, small experiments)
---
# Your MCP Doesn't Need 30 Tools: It Needs Code
## Key claims
- One tool that accepts code (e.g. `pexpect-mcp` running Python against retained state) can beat dozens of narrow tools; "the more tools you have, the more you're contributing to context rot".
- Composability: agents chain CLI commands and write scripts, whereas MCP calls typically need a model inference between steps; code loops need none. Code from a session can be saved as a standalone script (his debug session: ~7 tool calls, saved script ran in 1 call without MCP).
- MCP's real strength is session management ("We're relegating the MCP to do the thing that it does really well: session management"); CLI has its own problems (platform behaviour, encoding, lost tmux state).
- His own Playwright experiment did not yet beat Playwright MCP. Notes code-execution risk is not much worse than existing agent risk.
## Quotable
> the more tools you have, the more you’re contributing to context rot

## Used by
[[topic-tool-and-mcp-design]]
