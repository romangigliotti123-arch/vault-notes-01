---
tags: [moc, manager-kb]
updated: 2026-11-01
---
# manager-kb: research for improving the master agent

What this is: sourced research on running Roman's always-on manager (a Claude Code session that delegates to subagents, controlled from a phone). 21 topic files, 451 source notes (URL, date, reliability, key claims). Written 2026-10-29. Reader = the manager AI and a reviewing human. Start with [[PROPOSALS]] (ranked, with exact text), then read the topic file for the area you are changing.

Conventions: [[kb-conventions]] (templates, method). Earlier mechanics research (subagents vs teams vs bg sessions, GitHub MCP, session naming, SSH patterns): `~\claude-library-research\manager-setup.md` (not mirrored).

Status notes
- 10 topic files were written by research workers; 10 were synthesised by the lead from the workers' source notes after the 5-hour usage limit stopped those workers (marked in each file's intro). Source notes were opened by the workers; the lead re-checked that 361 of 363 single-URL source links resolve (Helicone 404 and OpenAI 403 bot-block flagged) and re-verified key figures (Google scaling study 17.2x/4.4x/45%/260 configs; Anthropic auto mode FNR 17%).
- The YouTube talks digest was skipped (usage limit; instructions to skip). A partial pipeline copy exists at `~\claude-host\youtube-learn-agents\` (not Roblox data; spend about $0.03).
- Prototype scripts (tested): `prototypes\` (jobs.py, hook_log.py, digest.py, otlp_sink.py); also installed as library skills `job-ledger`.

## Topics
### Orchestration and failure
- [[topic-orchestration-patterns]]: supervisor, hierarchical, swarm, blackboard, plan-and-execute; when single agent wins; ledger; 22 rules.
- [[topic-multi-agent-frameworks]]: LangGraph, OpenAI SDK, AutoGen/MAF, CrewAI, ruflo/claude-flow, Gas Town, worktree managers, A2A/MCP; table of what to steal vs ignore.
- [[topic-multi-agent-failure-modes]]: MAST taxonomy and real incidents; symptoms, detection, mitigation.
- [[topic-llm-judge-and-adversarial-verification]]: judge biases, self-correction limits, verification ladder, verifier preset.
- [[topic-report-formats-and-verification]]: report format v2, how the manager reads reports, false-success data.

### Anthropic guidance, context, prompting
- [[topic-anthropic-agent-guidance]]: what Anthropic says an orchestrator should do (31 rules).
- [[topic-context-engineering]]: finite context, compaction, JIT retrieval, sub-agent isolation applied to a 24/7 manager.
- [[topic-context-window-management]]: measured master usage, compaction/rotation policy L0-L4, compact instructions.
- [[topic-brief-prompt-engineering]]: the brief template and pre-send checklist; model-specific prompting.
- [[topic-claude-code-features]]: subagent/skill/hook/CLAUDE.md/memory/output-style practice; features not yet used, ranked.

### Cost, long-running, observability
- [[topic-model-effort-routing-cost]]: where the usage goes (workers 95%), routing table, effort pins, limits.
- [[topic-long-running-always-on-agents]]: job ledger, idempotency, supervisor/watchdog, usage-limit pauses, boot reconciliation.
- [[topic-observability]]: hooks event log, digest, cost per job, failure review; what not to build.

### Safety, tools, interface
- [[topic-agent-security]]: threat model of a bypass-mode admin agent with Telegram/RC inputs; mechanical confirm-first; local audit findings.
- [[topic-tool-and-mcp-design]]: tool/MCP/script design; JSON/exit-code/idempotency contract for tools\*.ps1.
- [[topic-remote-mobile-ux]]: phone reporting, questions, notifications, approvals.
- [[topic-personal-assistant-agents]]: OpenClaw/Hermes/Devin/Manus/Cowork lessons; file ownership, memory write path, idle cost.
- [[topic-cross-device-agent-control]]: remote `claude -p` robustness, credentials, scoped SSH keys, Windows OpenSSH, wake.

### Knowledge and library
- [[topic-knowledge-management-rag]]: kb layout, lessons/decisions, supersession, retrieval choices, no memory framework.
- [[topic-skill-library-retrieval]]: retrieval over 5,600 skills, eval set, forced lookup, curation.

### Game dev
- [[topic-managing-ai-agents-for-roblox-game-dev]]: the manager method applied to /game-dev-workflow (head manager, workers, model table, Luau verification ladder, playtest loop). Added 2026-11-01.

### 2026 update (2026-11-01)
Topics orchestration-patterns, model-effort-routing-cost, llm-judge-and-adversarial-verification, context-engineering, claude-code-features and multi-agent-failure-modes each gained a section 'What changed in 2026' (14 new src notes: LangChain harness/evals/context posts, Bockeler/Fowler harness engineering, OpenAI harness engineering and Symphony, Anthropic AI-resistant evals, Claude Code docs on agent teams, workflows, costs, cross-session messaging, Google ADK patterns).

### AI creators (2026-11-01)
Four src notes from the research on Nate Herk, RoboNuggets and Andrej Karpathy (549 videos): [[src-nate-herk-agent-practice]], [[src-robonuggets-agent-practice]], [[src-karpathy-llm-practice]], [[src-creators-disagreements]]. Topics orchestration-patterns, context-window-management, claude-code-features, llm-judge-and-adversarial-verification, agent-security, model-effort-routing-cost, skill-library-retrieval, multi-agent-failure-modes and long-running-always-on-agents gained a section 'From Nate Herk / RoboNuggets / Karpathy'. Full video notes, hubs and the idea catalogue: AI Library Vault, `Creators/` (source: `research/ai-creators`).

## How to use
1. Changing the manager's behaviour: read [[PROPOSALS]], pick items, apply deliberately (nothing here is applied).
2. Before changing an area: read its topic file's "Applies to us" and "Candidate changes" (C-numbers are referenced from PROPOSALS).
3. Source notes are named `src-<slug>`; every claim in a topic file links to one. Disagreements are in each topic's "Where sources disagree".
4. Reusable presets/skills written from this research are in `~\claude-library\` under `agents\orchestration` and `skills\orchestration`: adversarial-verifier, haiku-scout, brief-preflight-checklist, report-reading-protocol, worker-report-format-v2, job-ledger, confirm-first-guard, master-session-hygiene.
