---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Oct/16/claude-skills/ ; https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
type: practitioner-blog
author: Simon Willison
published: 2025-10-16 and 2025-09-30
accessed: 2026-10-29
reliability: med-high (careful practitioner; both posts fetched in full; pre-date Claude 5-era features)
---
# Simon Willison: "Claude Skills are awesome, maybe a bigger deal than MCP"; "Designing agentic loops"
## Key claims
- Skills: "a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts". Token efficiency: the harness scans skill frontmatter at session start; "each skill only takes up a few dozen extra tokens, with the full details only loaded in should the user request a task that the skill can help solve." Skills include validation scripts the model runs on its own output (e.g. a GIF skill with a size checker so the model can retry if too large) = built-in verification.
- Skills "depend on a coding environment" (filesystem + execute commands); that dependency is the difference from MCP/ChatGPT plugins and "yet another argument in favor of making safe coding environments available to LLMs". His thesis for "bigger deal than MCP": simplicity of the format and the fact that shell + docs + scripts are cheaper in tokens than MCP tool definitions.
- Agentic loops: pick problems with clear success criteria and tedious trial-and-error (debug failing tests, perf tuning, dependency upgrades, container-size shrinking); amplified by "a good, cleanly passing test suite".
- YOLO mode risks (unattended auto-approve): (1) bad shell commands deleting things, (2) exfiltration of files/env secrets, (3) machine used as proxy for attacks. Options: sandbox with limited files/secrets/network; run on someone else's computer (Codespaces); or take the risk ("Most people choose option 3"). Quotes Anthropic's guidance: use `--dangerously-skip-permissions` "in a container without internet access", with outbound limited to trusted hosts.
- Credentials for loops: prefer test/staging; "If a credential can spend money, set a tight budget limit" (example: dedicated Fly.io org with $5 budget and an org-scoped key).
- Prefer shell commands + an AGENTS.md line of example usage over MCP for tools the model already knows; "Good LLMs already know how to use a bewildering array of existing tools" (matches HumanLayer's CLI-over-MCP advice).
## Quotable
> "An AI agent is an LLM wrecking its environment in a loop." (Solomon Hykes, quoted)
> "If a credential can spend money, set a tight budget limit."

## Used by
[[topic-claude-code-features]]
