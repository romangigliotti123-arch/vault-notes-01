---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Aug/15/the-summer-of-johann/
type: practitioner-blog
author: Simon Willison (on Johann Rehberger's "Month of AI Bugs")
published: 2025-08-15
accessed: 2026-10-29
reliability: high (curated summary of primary research)
---
# The Summer of Johann: prompt injections as far as the eye can see
## Key claims
- Aug 2025 daily disclosures hit ChatGPT, Codex, Anthropic's filesystem MCP server, Cursor, Amp, Devin, OpenHands, Claude Code, GitHub Copilot, Google Jules.
- Attack classes: markdown-image (and Mermaid) exfiltration when the UI renders attacker URLs; shell/fetch/browser tools and DNS (`nslookup`, `dig`) as exfil; wildcard allow-listed domains (`*.azure.net`) hosting attacker logging endpoints; CONFIG SELF-MODIFICATION (Amp, Copilot tricked into editing their own settings to enable auto-approve or add MCP servers); tool abuse (Devin port exposure, OpenHands "support tool" C2); prefix-match path validation bug in Anthropic's filesystem MCP server; hidden Unicode in issues (Jules).
- Many vendors left issues unfixed after 90-120 days. Willison: "There may be systems that should not be built at all until we have a robust solution."
- "AI Kill Chain": injection makes the agent misuse its own privileges so tools run without human approval.
## Quotable
> There may be systems that should not be built at all until we have a robust solution.

## Used by
[[topic-agent-security]]
