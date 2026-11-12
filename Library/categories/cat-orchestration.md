---
tags: [moc]
---
# Category: orchestration

37 items. Back: [[_Home]]

- [a] [[A--own--adversarial-verifier|adversarial-verifier]] - Read-only falsifier: tries to prove a worker's claims false against real state (files, services, tasks, git, r
- [a] [[A--own--digest-scout|digest-scout]] - Context-isolated read-heavy subagent: gets a narrow brief and a set of files, docs or articles, reads them in 
- [a] [[A--own--haiku-scout|haiku-scout]] - Cheap read-only lookups: find a file/setting, triage a log, check a status, summarise long text. Never edits, 
- [a] [[A--own--incident-triager|incident-triager]] - Diagnoses a failed or stuck automation job from logs and state, finds the root cause and proposes the smallest
- [a] [[A--own--library-curator|library-curator]] - Imports, vets, categorizes and de-duplicates third-party skills/agents into the library with licenses recorded
- [a] [[A--own--opus-builder|opus-builder]] - Use ONLY for the toughest builds or architecture (complete game/app from scratch, large multi-file builds, har
- [a] [[A--own--parallel-audit-fanout|parallel-audit-fanout]] - Orchestrator for open-ended audits of a codebase before release: splits the code into areas, runs one capped p
- [a] [[A--own--parallel-job-splitter|parallel-job-splitter]] - Splits a large request into independent jobs for parallel workers, assigning model and effort to each and list
- [a] [[A--own--phased-build-orchestrator|phased-build-orchestrator]] - Orchestrator for a large build or a long bug/vulnerability list: plans phases, gives each worker one narrow ta
- [a] [[A--own--rbx-coach|rbx-coach]] - The vault mentor: works alongside the user on any job (designing, scripting, monetising, advertising, running 
- [a] [[A--own--remote-device-runner|remote-device-runner]] - Runs a headless Claude (or plain commands) on another machine over SSH, supervises it, and returns its report;
- [a] [[A--own--report-auditor|report-auditor]] - Checks a worker's final report against the original brief and the real artifacts, and returns accept, re-brief
- [a] [[A--own--sonnet-worker|sonnet-worker]] - Default worker for any real job. Use for multi-step work, installs and setup, SSH/Wake-on-LAN/Linux machine ta
- [a] [[A--own--task-decomposer|task-decomposer]] - Splits a large goal into independent worker jobs with self-contained briefs, model/effort picks and an integra
- [a] [[A--own--verifier|verifier]] - Independently verifies another worker's claimed result by re-running checks and looking for gaps; use before r
- [s] [[S--own--add-to-library|add-to-library]] - Step-by-step for adding or updating an agent preset or skill in claude-library, rebuilding the index and commi
- [s] [[S--own--agent-platform-map|agent-platform-map]] - Designs or audits an agent platform: maps each process step, marks decision points and variability, scores det
- [s] [[S--own--artifact-handoff|artifact-handoff]] - Deliver long or visual results to Roman by publishing a private Artifact page or a file and sending only a sho
- [s] [[S--own--brief-preflight-checklist|brief-preflight-checklist]] - Use before every Agent/worker spawn or remote claude -p run: the 6-block brief template (context, task, scope,
- [s] [[S--own--confidence-escalation-router|confidence-escalation-router]] - Pattern and code template for routing AI answers inside an automation: auto-accept when confidence is at or ab
- [s] [[S--own--confirm-first-guard|confirm-first-guard]] - PreToolUse guard hook that makes the 'Always confirm first' list mechanical (publish, send-as-user, security/f
- [s] [[S--own--job-ledger|job-ledger]] - File-based job ledger, side-effect idempotency keys, hook event log and daily digest for a 24/7 manager (state
- [s] [[S--own--library-search|library-search]] - How to browse the claude-library cheaply (names, then descriptions, then the file) and use a found agent or sk
- [s] [[S--own--master-session-hygiene|master-session-hygiene]] - Runbook for keeping a 24/7 master session healthy: compaction thresholds, compact-instructions block, ledger r
- [s] [[S--own--model-routing|model-routing]] - Decision rules for choosing haiku, sonnet or opus and the effort level for a delegated job.
- [s] [[S--own--plan-then-build|plan-then-build]] - Gate and procedure for big builds: use plan mode for setup and large work (skip it for simple fixes), ask clar
- [s] [[S--own--publish-now|publish-now]] - Last step of any task that adds or changes a skill, agent, library item, vault note or setup doc: run publish-
- [s] [[S--own--rbx-low-usage|rbx-low-usage]] - Keep Claude in low usage mode for this session and every later one until turned off: cheapest model that fits,
- [s] [[S--own--rbx-manager|rbx-manager]] - Turns this session into a manager that delegates: sizes the job, picks model and effort (haiku/sonnet/opus), b
- [s] [[S--own--rbx-mentor|rbx-mentor]] - Start the vault mentor: a co-pilot with the combined knowledge of every creator in both vaults; works alongsid
- [s] [[S--own--remote-claude-run|remote-claude-run]] - Run a headless Claude Code agent on another machine (Roman's Linux PC) over SSH, detached with a log, and coll
- [s] [[S--own--report-reading-protocol|report-reading-protocol]] - Use when a worker or remote agent reports back: read order, claim extraction, one-command spot checks by claim
- [s] [[S--own--sequential-agent-pipeline|sequential-agent-pipeline]] - Runs a multi-stage task as separate small agents or sessions in order (for example research, then draft, then 
- [s] [[S--own--vault-skill-builder|vault-skill-builder]] - Maintainer recipe (host only, never shipped) for adding ONE new skill to the Roblox Dev Mastery Vault kit: ove
- [s] [[S--own--worker-brief-template|worker-brief-template]] - Template and rules for writing a self-contained AI-to-AI brief for a worker agent; use before delegating any j
- [s] [[S--own--worker-report-format|worker-report-format]] - The standard final-report format every worker returns (RESULT/DONE/VERIFIED/PROBLEMS/NEEDS/NEXT/ARTIFACTS) and
- [s] [[S--own--worker-report-format-v2|worker-report-format-v2]] - Evidence-bound worker report format (RESULT/HEADLINE/CRITERIA/CHANGES/NOT_CHECKED/PROBLEMS/NEEDS_ROMAN/SUGGEST
