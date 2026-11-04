---
tags: [moc, creator-hub]
---
# AI creators: agents, skills and manager research

Research on 4 AI creators (Nate Herk, RoboNuggets, Andrej Karpathy, Theo (t3.gg)) covering 565 videos, 667 agent/skill ideas and 39 built library items. The full notes (every video, the hubs, the idea catalogue) live in the **AI Library Vault**, folder `Creators/` (start at its `Creators/_Creators-Home.md` and `CAPABILITIES.md`). Links to that vault are plain text here.

## Their methods in one place

The combined brain ([[Combined-Brain]], `Mentor/Combined-Brain.md`) merges what these three and the Roblox creators teach, by job, with trust labels and the points where they disagree. Start there, or run `/rbx-mentor` (claude-kit) to work with it.

- **Nate Herk** (366 videos): start with the simplest layer that works, wireframe before building, add one sentence to the prompt per observed error, context engineering as the main lever, verification loops with checkable goals, human approval on risky actions, sell outcomes not agents.
- **RoboNuggets**: you are the CEO of an agency of agents; A.G.E.N.T. prompt framework (Ask, Guidelines/Goal, Examples, Notation/Negations, Tools); direct model access through aggregators; thin CLAUDE.md router with progressive disclosure; reuse proven formats. Income claims in his videos are marketing, not evidence.
- **Andrej Karpathy** (the educational series and the LLM talks only): build from first principles, verify numerically, sanity-check initial values, reset context when the topic changes. His agents and vibe-coding talks are not in the vault.

Full hubs, one note per video and the idea catalogue are in the AI Library Vault (`Creators/hubs/`, `Creators/videos/`, `Creators/catalogue/`).

## Built items that live in this vault (7)

- [[A--own--digest-scout|digest-scout]] (agent) - Context-isolated read-heavy subagent: gets a narrow brief and a set of files, docs or articles, reads them in its own clean context, and ret
- [[A--own--parallel-audit-fanout|parallel-audit-fanout]] (agent) - Orchestrator for open-ended audits of a codebase before release: splits the code into areas, runs one capped parallel auditor per area, spaw
- [[A--own--phased-build-orchestrator|phased-build-orchestrator]] (agent) - Orchestrator for a large build or a long bug/vulnerability list: plans phases, gives each worker one narrow task with exclusive file ownersh
- [[S--own--sequential-agent-pipeline|sequential-agent-pipeline]] (skill) - Runs a multi-stage task as separate small agents or sessions in order (for example research, then draft, then polish, then send), passing on
- [[S--own--agent-platform-map|agent-platform-map]] (skill) - Designs or audits an agent platform: maps each process step, marks decision points and variability, scores deterministic versus non-determin
- [[S--own--confidence-escalation-router|confidence-escalation-router]] (skill) - Pattern and code template for routing AI answers inside an automation: auto-accept when confidence is at or above a threshold (for example 8
- [[S--own--plan-then-build|plan-then-build]] (skill) - Gate and procedure for big builds: use plan mode for setup and large work (skip it for simple fixes), ask clarifying questions, write a spec

## Manager research from the creators

Rules for delegating, verifying, context, cost and permissions are in the Manager knowledge base: [[src-nate-herk-agent-practice]], [[src-robonuggets-agent-practice]], [[src-karpathy-llm-practice]], [[src-creators-disagreements]], summarised in the 'From Nate Herk / RoboNuggets / Karpathy' sections of the `Manager/topic-*.md` files (start at [[Manager-README]]).

## Other built items

The other 32 built items (general AI, writing, devops, testing, frontend) are in the AI Library Vault: see its `Creators/BUILT.md`.
