---
tags: [manager-kb, topic]
updated: 2026-11-01
---
# Managing AI agents for Roblox game dev

Scope: how the manager method in this KB maps onto the vault's `/game-dev-workflow` skill (head manager, workers, model choice, Luau verification, playtest loop). Written 2026-11-01 from the KB's own notes plus the 2026 additions; the skill files and Roblox KB paths were read, the Roblox notes were NOT used for factual game claims here (paths only). Skill: `~\claude-library\skills\game-dev\game-dev-workflow\` (`SKILL.md`, `references\head-manager.md`, `templates\brief.md`, `templates\jobs.md`). Side skill: `game-dev-playtest`. Roblox KB (do not edit from here): vault `Roblox\roblox-kb\` (`ai-and-tools.md`, `code-architecture-and-frameworks.md`, `anti-exploit-and-security.md`, `_tools\DECISION-RULES.md`, `_tools\CHECKLIST-launch.md`), `Roblox\docs\Videos\2026-10-28 - Docs studio testing-modes.md`, `Roblox\devforum\Videos\2026-06-26 - Automated Performance Profiling with MicroProfiler and Assistant.md`, `Roblox\crusherfiredev\Videos\2025-11-22 - 10x Your Roblox Studio Productivity - Claude Code & OpenAI Codex Integ.md` (Studio MCP setup).

## TL;DR
- The existing head-manager design already follows the KB's core rules: one manager, flat workers (depth 0), a job ledger, briefs from a template, cheap independent verification, retry once, caps. Keep it; tune three things below. [[topic-orchestration-patterns]], [[topic-brief-prompt-engineering]]
- Parallel only on disjoint write-sets; the Studio MCP session is one shared writer, so MCP jobs stay serial (already in `head-manager.md`). Read-parallel (design review, economy review, code review) is the safe fan-out. [[src-langchain-how-and-when-multi-agent-systems]], [[src-ccdocs-agent-teams]]
- Verification of Luau must be a RUN of a check, never "I re-read it": the most common agent failure is stopping after a self-review. Computational sensors first (selene, stylua, luau-lsp, grep for banned patterns), LLM reviewer second, a real playtest last. [[src-langchain-improving-deep-agents-harness]], [[src-bockeler-fowler-harness-engineering]]
- Playtest is the only check that tests functional behaviour, and it is the weakest link: AI-written tests are not trusted alone. Put a human-readable acceptance test per milestone in the plan, run it, and keep the human playtest as the final gate. [[src-bockeler-fowler-harness-engineering]], [[src-advani-false-success]]
- Model choice: sonnet-class for builders and reviewers, haiku for lookups and mechanical checks, strongest model only for plan/design and for resolving a second failure; spend extra effort on planning and verification, not on every step. [[topic-model-effort-routing-cost]], [[src-langchain-improving-deep-agents-harness]]
- Make the repo the memory: `game-plan.md`, `jobs.md`, `docs/PROGRESS.md`, briefs on disk. Workers see only the brief plus CLAUDE.md, never the manager's chat. [[src-openai-harness-engineering-infoq]], [[src-ccdocs-agent-teams]]

## Rules
1. **Manager does not write the game; it decomposes, briefs, verifies and keeps score.** Matches `head-manager.md` ("small glue and fixes" only). Decompose by context and file ownership (systems = disjoint folders: economy, combat, UI, data), not by role-play titles. Evidence: [[src-claudecom-building-multi-agent-systems]], [[src-claudecom-fold-subagents]], [[src-cognition-dont-build-multi-agents]]. Confidence: high (official/primary).
2. **Cap fan-out by the plan, default 2-3 live workers; one writer per file.** A Roblox project makes conflicts easy (a shared `Remotes` module, one `ReplicatedStorage` tree, one data module). Declare owned files in each brief; shared modules belong to one job. Evidence: [[src-ccdocs-agent-teams]] ("assign file ownership", "3 focused beat 5 scattered"), [[src-cursor-scaling-agents]], [[src-google-adk-multi-agent-patterns]] (unique output key per parallel agent). Confidence: med-high.
3. **Use subagents for the normal 5-30 job build; a dynamic workflow only for same-step-over-many-items work.** Examples that fit: audit every `RemoteEvent` handler for missing server validation across 40 scripts; lint-and-fix a whole folder until `luau-check.sh` is clean; generate N item/shop entries then verify each. Not a fit: designing the core loop or feel tuning (needs the manager's judgment, sequential). Start with workflow size `small`; try one folder first. Evidence: [[src-ccdocs-workflows-usage-and-limits]]. Confidence: med (official doc; no Roblox-specific evidence). Agent teams: leave off; they add cost (~7x in plan mode) and need an interactive session. [[src-ccdocs-costs-2026-update]]
4. **Model routing for game work (starting table, adjust with `/usage` data).**

   | Job | Model / effort | Why |
   |---|---|---|
   | Game plan, economy and progression design, architecture | strongest available, high | decomposition quality bounds everything; cheap relative to rework [[src-arxiv-think-big-search-small]] (med-low) |
   | Luau feature builds (`roblox-luau-engineer`, `roblox-builder`) | sonnet, medium-high | default worker |
   | Code review / security review (`roblox-luau-reviewer`, anti-exploit) | sonnet, high, fresh context, read-only | independent verifier rule [[topic-llm-judge-and-adversarial-verification]] |
   | Lookups, grep sweeps, "does file X exist / does check pass" | haiku, low | mechanical; [[topic-model-effort-routing-cost]] |
   | Second failure on the same job | escalate one tier or change the brief, not a third identical retry | [[topic-multi-agent-failure-modes]] |
   Thinking cannot be switched off on current-generation models, so `effort` is the lever; extra effort goes to plan and verify steps. [[src-ccdocs-costs-2026-update]], [[src-langchain-improving-deep-agents-harness]]. Confidence: med (vendor numbers, other domain).
5. **Brief = goal, inputs as paths, owned files, hard rules, DONE WHEN with a runnable check, report format, stop rule, turn budget.** The kit's `templates\brief.md` already has these; add two Roblox lines: "never invent asset/pass ids (use 0)" (already a kit rule) and "state the exact command whose output proves each DONE WHEN item". A numeric or checkable target changes agent behaviour (Opus 4.5 quit until given a target). Evidence: [[topic-brief-prompt-engineering]], [[src-anthropic-ai-resistant-evals]]. Confidence: med.
6. **Luau verification ladder.** In order, cheapest first, record command plus output excerpt in the ledger `verify` column:
   1. File exists / non-empty (`ls -l`, `wc -c`).
   2. Static: `luau-check.sh` (selene, stylua, luau-lsp) read last 10 lines; if tools missing, report "tools missing: manual review" and say so, never claim lint-clean.
   3. Pattern sensors from `head-manager.md` (`loadstring`, `wait(`, `spawn(`, fake `rbxassetid://`; server handlers for every `OnServerEvent`/`OnServerInvoke` validate arguments; `BindToClose`/`UpdateAsync`/release present for data). Make each sensor's failure message say how to fix it. [[src-bockeler-fowler-harness-engineering]]
   4. Behaviour: Studio MCP playtest reading Output when present; otherwise the `game-dev-playtest` code-walk path (weaker; label it). Studio test modes: see `Roblox\docs\Videos\2026-10-28 - Docs studio testing-modes.md` (not read for this note).
   5. Independent reviewer worker (fresh context) for anything touching data saving, purchases, remotes or the economy (exploit and monetisation risk tier). `Roblox\roblox-kb\anti-exploit-and-security.md`, `_tools\CHECKLIST-launch.md`.
   6. Human playtest for feel, onboarding and the first 30 seconds: no agent check replaces it.
   A silent sensor is not proof: seed one known-bad snippet occasionally to see the check fail. [[src-bockeler-fowler-harness-engineering]]. Confidence: med-high (design from KB rules; Luau specifics are the kit's).
7. **Make the worker run the decisive check before reporting.** Add to the brief: "before you report, run <check> and paste the last lines; if it fails, fix and re-run; two identical failed edits in a row means stop and report." This is the pre-completion plus loop-detection pair that gained +13.7 points. Evidence: [[src-langchain-improving-deep-agents-harness]]. Confidence: med (vendor, other domain); cost is two brief lines.
8. **Playtest loop.** Per milestone: build -> static checks -> acceptance test written in the plan (observable pass/fail, e.g. "player can buy item X, coins drop by price, item persists after rejoin") -> run it (MCP or code-walk) -> bug list -> at most one fix round per bug batch -> re-run only the failed tests -> next milestone. Track efficiency (jobs, retries, tokens) per milestone to see when the loop stalls; cap retries as the plan says. Evidence: [[src-langchain-how-we-build-evals-deep-agents]] (efficiency ratios), [[topic-report-formats-and-verification]]. Confidence: med.
9. **Do not let reports stand in for state.** Ledger rows move to DONE only with evidence; an unverified claim stays "reported, unchecked". [[topic-report-formats-and-verification]], [[src-advani-false-success]].
10. **Keep depth at 1 and the budget visible.** The kit agents cannot spawn agents; if the head manager is itself a subagent, run the ledger inline one job at a time (already in `SKILL.md`). Report spend and caps in `docs/PROGRESS.md`; on a usage-limit stop, the ledger plus briefs on disk let a fresh session resume. [[topic-long-running-always-on-agents]]
11. **Harness before more agents.** When the same defect recurs (e.g. unvalidated remotes), fix the harness: add a grep sensor or a rule to the project `CLAUDE.md`/template, rather than adding a reviewer role. Repo docs (GDD, architecture notes, module boundaries such as client / server / shared) are the agents' source of truth; enforce boundaries by a structural check. [[src-openai-harness-engineering-infoq]], [[src-bockeler-fowler-harness-engineering]]. Roblox KB: `Roblox\roblox-kb\code-architecture-and-frameworks.md`. Confidence: med.

## Where sources disagree
- **How many agents.** Anthropic/Cognition/LangChain: single agent or orchestrator-subagent, write-serial; Cursor/OpenAI Symphony run many parallel agents with a strong verifier (CI) and per-task isolation. For a solo game with shared modules and a weak automatic verifier (no real playtest in CI) follow the first group. [[topic-orchestration-patterns]]
- **Studio MCP vs files.** The kit makes files/Rojo the source of truth and MCP optional; the creator video favours MCP to avoid Rojo. No evidence in this KB decides it; the file-first default is the safer, auditable one.

## Applies to us
- Already in place (per `head-manager.md`): ledger, briefs on disk, cheap verification with evidence, retry once, caps, MCP-serial, no GUI launching. Keep.
- Missing or thin: (a) "run the check before reporting" and repeated-edit stop rule in `templates\brief.md`; (b) a seeded-bad-snippet test that the pattern sensors can fail; (c) per-milestone acceptance tests that are executable, not prose; (d) model table above in `game-plan.md`; (e) a decision note on when a workflow beats subagents.
- Run the build from a worker session (not the always-on manager) when possible, so the manager stays phone-short; see [[topic-model-effort-routing-cost]] on where usage goes.

## Candidate changes for us
- C1: add the two brief lines of rule 5/7 to `templates\brief.md` in the game-dev-workflow skill (edit in the claude-library; not done here).
- C2: add the model table (rule 4) to the plan template's routing section.
- C3: add a `verify` seed test: a tiny known-bad Luau file the pattern sensors must flag; run it once per project.
- C4: before the first big fan-out, run one `/usage` check and record the subagent share.

## Open questions
- Does Studio MCP expose a playtest run with readable Output in our installs (the skill says "only when present")? Not checked.
- No measured data on agent-written Luau defect rates here; the verification ladder is design, not benchmark.

## Related
[[topic-orchestration-patterns]], [[topic-brief-prompt-engineering]], [[topic-model-effort-routing-cost]], [[topic-llm-judge-and-adversarial-verification]], [[topic-report-formats-and-verification]], [[topic-multi-agent-failure-modes]], [[topic-claude-code-features]], [[topic-long-running-always-on-agents]]
