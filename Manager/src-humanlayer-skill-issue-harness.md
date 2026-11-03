---
tags: [manager-kb, source]
url: https://www.hlyr.dev/blog/skill-issue-harness-engineering-for-coding-agents ; https://www.hlyr.dev/blog/long-context-isnt-the-answer
type: practitioner-blog
author: Kyle (HumanLayer), 2026-03-12 and 2026-03-23
published: 2026-03-12 / 2026-03-23
accessed: 2026-10-29
reliability: med (practitioner experience; cites ETH Zurich AGENTS.md study and Chroma context rot)
---
# HumanLayer: "Skill Issue: Harness Engineering for Coding Agents" (+ "Long-Context Isn't the Answer")
## Key claims
- Thesis: failures are "a configuration problem", not a model problem; harness engineering (Mitchell Hashimoto, via Viv) = "anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again." Levers: CLAUDE.md, MCP, skills, sub-agents, hooks, back-pressure (verification).
- Sub-agents: "We tried the 'frontend engineer' sub-agent and 'backend engineer' sub-agent and 'data analyst' sub-agent thing. It doesn't work. What does work is using sub-agents for context control": a "context firewall" so intermediate tool calls never enter the parent, which stays coherent longer. Sub-agent returns should be "highly condensed" with citations in `filepath:line` or URL form so the parent can drill down if needed. Also cost control: expensive model (Opus) in the parent, Sonnet/Haiku in sub-agents. Sub-agent system prompts must specify role AND what NOT to do, what to return and how, what tools. 
- "Trying to micro-optimize which sub-agents could access which tools. This led to a lot of tool thrash which gave us worse results, not better ones." (contrast with official docs' advice to restrict `tools`).
- Hooks: notifications (sounds when done), approvals (auto-deny Bash calls that run migrations with an instruction to ask the user), integrations (Slack message, PR creation), verification via a Stop hook running formatter + typecheck: silent on success, `exit 2` with only errors on stderr on failure. Biome quirk: run twice with `||`.
- Back-pressure: "your likelihood of successfully solving a problem with a coding agent is strongly correlated with the agent's ability to verify its own work"; verification must be context-efficient ("success is silent, and only failures produce verbose output"; 4,000 lines of passing tests flooded the context).
- MCP: tool descriptions land in the system prompt (injection vector, instruction-budget cost); prefer well-known CLIs (gh, docker) over MCP; wrapped a Linear MCP into a small CLI + 6 example usages in CLAUDE.md to save thousands of tokens. Skills: registries have distributed malicious skills ("Treat skills like you'd treat npm install random-package").
- ETH Zurich AGENTS.md study (as summarised here, 138 agentfiles): LLM-generated agentfiles hurt performance and cost 20%+ more; human-written ones helped ~4%; codebase overviews/directory listings didn't help; agents spent 14-22% more reasoning tokens on context-file instructions.
- What did not work: designing the ideal harness up front; dozens of skills/MCP servers "just in case"; running 5+ min test suite at the end of every session. What worked: start simple, add config only when the agent fails, throw away hooks that did not help ("I have thrown away many more hooks than we actually use today").
- "Long-Context Isn't the Answer" (2026-03-23): after trying Opus 4.6 1M they switched back to Opus 4.5: instruction adherence degraded even well within 200K; "the instruction budget remains the same" when context grows; fix = more aggressive context isolation with sub-agents, not a bigger window. (Single-team anecdote; official docs now say 1M windows make context exhaustion rare.)
## Quotable
> "We tried the 'frontend engineer' sub-agent and 'backend engineer' sub-agent and 'data analyst' sub-agent thing. It doesn't work."
> "success is silent, and only failures produce verbose output"

## Used by
[[topic-claude-code-features]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]], [[topic-tool-and-mcp-design]]
