---
id: "agent-platform-map"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/agent-platform-map/SKILL.md"
description: "Designs or audits an agent platform: maps each process step, marks decision points and variability, scores deterministic versus non-deterministic to decide workflow or agent, then charts which agent can use which skill with circle size as token cost to show shared skills and costly outliers; outputs a verdict and an HTML or Excalidraw diagram. Use when the user asks should this be a workflow or an agent, visualise my agents and skills, which skills cost the most tokens, audit my agent setup, or map my automation."
orig_name: "agent-platform-map"
orig_argument_hint: "<process description or skills folder>"
tags: [lib/skill, cat/orchestration, src/own]
---

# agent-platform-map

> Designs or audits an agent platform: maps each process step, marks decision points and variability, scores deterministic versus non-deterministic to decide workflow or agent, then charts which agent can use which skill with circle size as token cost to show shared skills and costly outliers; outputs a verdict and an HTML or Excalidraw diagram. Use when the user asks should this be a workflow or an agent, visualise my agents and skills, which skills cost the most tokens, audit my agent setup, or map my automation.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/agent-platform-map/SKILL.md` (extra files, if any, sit beside it in the repo)

Creator videos (notes are in the AI Library Vault, Creators/videos): 2025-03-27-ai-agents-what-99-of-beginners-get-wrong, 2026-03-17-every-openclaw-concept-explained-for-normal-people, 2025-04-10-n8n-s-native-mcp-integration-without-the-hype, 2026-03-24-claude-code-just-became-unstoppable-claudeclaw, 2026-03-28-claude-code-paperclip-just-destroyed-openclaw, 2026-03-27-everything-new-in-claude-code-explained-march-2026-edition, 2026-08-12-grok-bot-is-for-real-what-you-need-to-know

---
# agent-platform-map

Two modes: **decide** (workflow vs agent for a process) and **map** (agents x skills with token cost).

## Mode 1: decide
1. List every step of the process: actor (person, API, model), input, output, how often it varies.
2. Mark decision points (where the next step depends on content) and variability (inputs that differ per run).
3. Score each step: deterministic (same input -> same output, rule-based) or non-deterministic (needs reading, judgment, free text). Count both.
4. Verdict: all or nearly all deterministic -> plain script or workflow; a few judgment steps -> workflow with AI nodes at those steps only; judgment dominates and the path itself varies -> agent. Name the cheapest option that works (see automation-design-framework for hosting).
5. Output a table and a wireframe of the flow (Mermaid or Excalidraw JSON).

## Mode 2: map
1. Inventory agents (`agents/*.md`, subagent definitions) and skills (`SKILL.md` files). For each skill record the description length and body size; estimate tokens as chars/4 (state it is an estimate). If skills have an `effort` frontmatter field, include it.
2. For each agent read its `skills:` / tools list or instructions to find which skills it can use.
3. Build the bipartite map: agents on one side, skills on the other, an edge for access. Circle size = token estimate. Highlight skills shared by 3+ agents (candidates to keep tight) and the top-5 largest (candidates to split or trim).
4. Render as a single self-contained HTML (inline SVG, no external requests) and also list the findings in text.

## Output
Verdict or map plus 3 recommendations. Never claim token numbers are exact.

## Failure modes
- Treating every process as an agent: most are workflows.
- Missing implicit skills (global skills available to every agent): list them as a shared column.

## Related
skills-ecosystem-audit, automation-design-framework, skill-prompt-audit.

## Sources
Idea from AI-creator research (catalogue ideas idea-0066). Credit and where it appears:
- Nate Herk, "AI Agents: What 99% of Beginners Get Wrong" (2025-03-27) @ 12:40, https://www.youtube.com/watch?v=HuTyZiUDz2k&t=760s. Seen there as: Agent-vs-workflow decision check
- RoboNuggets (Jay E), "Every OpenClaw Concept Explained for Normal People" (2026-03-17) @ 20:45, https://www.youtube.com/watch?v=tFCgmeOWlA8&t=1245s. Seen there as: Skill tree visualizer
- Nate Herk, "n8n's Native MCP Integration (without the hype)" (2025-04-10) @ 11:13, https://www.youtube.com/watch?v=VTEg8uJ4yxo&t=673s. Seen there as: Claude Desktop n8n MCP client
- RoboNuggets (Jay E), "Claude Code Just Became UNSTOPPABLE (ClaudeClaw)" (2026-03-24) @ 8:07, https://www.youtube.com/watch?v=W9igiY2JdHA&t=487s. Seen there as: Skill tree view
- Nate Herk, "Claude Code + Paperclip Just Destroyed OpenClaw" (2026-03-28) @ 9:23, https://www.youtube.com/watch?v=HJ-dwefABss&t=563s. Seen there as: Paperclip skills (native)
- RoboNuggets (Jay E), "Everything NEW in Claude Code Explained (March 2026 Edition)" (2026-03-27) @ 13:39, https://www.youtube.com/watch?v=3vrn03I5Tss&t=819s. Seen there as: Effort-level skill setting
- Nate Herk, "Grok Bot is For Real. What You Need to Know." (2026-08-12) @ 11:51, 18:03, https://www.youtube.com/watch?v=PQBYZQqan2g&t=711s. Seen there as: Slash-invoked shared skills
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
