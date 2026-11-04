---
tags: [moc]
---
# PICKS

Best 1-3 items per common manager job. Format: job | id(s) | why. Own items (no slash) come first, then imports (`source/name`). Agents are marked `[a]`, everything else is a skill. Find the file with `powershell -File tools\find.ps1 <id words>`; read that one file only. For anything not listed: `find.ps1 <keywords>`.

## Work with the vault (start here)
work alongside an adviser that knows every creator in both vaults and suggests tools as I go | [[S--own--rbx-mentor|rbx-mentor]], [[S--own--rbx-mentor|rbx-mentor]] | /rbx-mentor reads CAPABILITIES.md and Mentor/Combined-Brain.md, then suggests the skill, agent, note or creator method for each step

## Build and fix code
code review | code-reviewer [a] (in AI Library Vault), code-review-checklist (in AI Library Vault), anthropic-knowledge-work/code-review (in AI Library Vault) | own agent does it end to end; checklist for a quick pass; AKW skill for security/perf/correctness structure
PR review, deeper | anthropic-plugins-official/pr-test-analyzer [a] (in AI Library Vault), anthropic-plugins-official/silent-failure-hunter [a] (in AI Library Vault) | test-coverage gaps and swallowed errors that normal review misses
security review of code | security-auditor [a] (in AI Library Vault), trailofbits/differential-review (in AI Library Vault), trailofbits/variant-analysis (in AI Library Vault) | OWASP/secrets/authz sweep; Trail of Bits method for diffs and finding sibling bugs
bug hunt / debugging | bug-hunter [a] (in AI Library Vault), superpowers/systematic-debugging (in AI Library Vault), anthropic-knowledge-work/debug (in AI Library Vault) | hypothesis-driven root cause plus regression test
bug triage / reproduce | bug-triage (in AI Library Vault), trailofbits/reproduce-bug (in AI Library Vault) | rank a bug list; build a minimal repro
refactor | refactorer [a] (in AI Library Vault), awesome-copilot/refactor-plan (in AI Library Vault), anthropic-plugins-official/code-simplifier/code-simplifier [a] (in AI Library Vault) | behavior-preserving, tests first; plan multi-file moves; simplify recent code
write tests | test-writer [a] (in AI Library Vault), anthropic-knowledge-work/testing-strategy (in AI Library Vault) | matches the project's framework; strategy for what to cover
test-driven development | superpowers/test-driven-development (in AI Library Vault), mattpocock/tdd (in AI Library Vault) | strict red-green-refactor discipline
test plan | test-plan-template (in AI Library Vault), anthropic-knowledge-work/testing-strategy (in AI Library Vault) | risk-based plan with entry/exit criteria
mutation / property tests | trailofbits/mutation-testing (in AI Library Vault), trailofbits/property-based-testing (in AI Library Vault) | tests that prove the tests catch bugs
web app / E2E testing | anthropic-skills/webapp-testing (in AI Library Vault), wshobson/e2e-testing-patterns (in AI Library Vault) | Playwright toolkit; patterns for stable E2E
performance profiling | performance-profiler [a] (in AI Library Vault), alirezarezvani/performance-profiler (in AI Library Vault) | measure first, find the real bottleneck
tech debt audit | anthropic-knowledge-work/tech-debt (in AI Library Vault), anthropic-plugins-official/code-architect [a] (in AI Library Vault) | prioritised debt list; architecture-aware changes
legacy modernisation / migration | wshobson/code-refactoring-legacy-modernizer [a] (in AI Library Vault), alirezarezvani/migration-architect (in AI Library Vault), wshobson/dependency-upgrade (in AI Library Vault) | zero-downtime plans and rollback
backend / API build | api-engineer [a] (in AI Library Vault), api-design-checklist (in AI Library Vault), alirezarezvani/api-design-reviewer (in AI Library Vault) | design and implement; checklist and linting-based review
API design | api-design-checklist (in AI Library Vault), jeffallan/api-designer (in AI Library Vault), wshobson/openapi-spec-generation (in AI Library Vault) | resources, errors, pagination, versioning; OpenAPI output
database schema / SQL | wshobson/postgresql-table-design (in AI Library Vault), alirezarezvani/database-designer (in AI Library Vault), wshobson/sql-optimization-patterns (in AI Library Vault) | design, indexing, query tuning
React / TypeScript UI | wshobson/react-state-management (in AI Library Vault), awesome-copilot/Expert React Frontend Engineer [a] (in AI Library Vault), wshobson/typescript-advanced-types (in AI Library Vault) | modern React and typing patterns
Python code | wshobson/python-testing-patterns (in AI Library Vault), wshobson/python-error-handling (in AI Library Vault), 0xfurai-subagents/python-expert [a] (in AI Library Vault) | idiomatic tests, errors, style
mobile (iOS / Android) | 0xfurai-subagents/ios-expert [a] (in AI Library Vault), 0xfurai-subagents/android-expert [a] (in AI Library Vault), gstack/ios-qa (in AI Library Vault) | build and live-device QA
game dev (Unity / Godot) | [[S--jeffallan--game-developer|jeffallan/game-developer]], [[A--agency-agents--Godot-Gameplay-Scripter|agency-agents/Godot Gameplay Scripter]] [a] | systems and performance
Roblox build | [[A--own--rbx-engineer|rbx-engineer]] [a], [[A--agency-agents--Roblox-Systems-Scripter|agency-agents/Roblox Systems Scripter]] [a] | secure client/server Luau
Roblox test | [[A--own--rbx-tester|rbx-tester]] [a], [[S--own--rbx-playtest-list|rbx-playtest-list]] | playtest first 30 s through multiplayer and exploits
Roblox design / monetisation | [[A--agency-agents--Roblox-Experience-Designer|agency-agents/Roblox Experience Designer]] [a] | engagement loop, DataStore progression, monetisation
Roblox (any request) | [[A--own--rbx-lead|rbx-lead]] [a] | router: picks specialists, runs them, merges one sourced plan (KB: ~/claude-host/youtube-learn/out/roblox-kb/_tools/HOW-TO-USE.md)
Roblox quick fact / "what do creators say" | [[S--own--rbx-kb|rbx-kb]] | 2-4 cheap cited KB queries, no agents
Roblox game idea / GDD | [[A--own--rbx-designer|rbx-designer]] [a], [[S--own--rbx-gdd|rbx-gdd]], [[S--own--rbx-ideas|rbx-ideas]] | scored concepts, build-ready GDD, evidence table
Roblox pricing / passes / products | [[A--own--rbx-money|rbx-money]] [a], [[S--own--rbx-monetize-audit|rbx-monetize-audit]] | offer catalogue with Robux prices and trigger moments; audit scorecard
Roblox ads / thumbnails / launch | [[A--own--rbx-marketer|rbx-marketer]] [a], [[S--own--rbx-ad-plan|rbx-ad-plan]], [[S--own--rbx-thumb-brief|rbx-thumb-brief]] | budget and schedule with calculator, packaging brief, Discord plan
Roblox game underperforming (metrics) | [[A--own--rbx-doctor|rbx-doctor]] [a], [[S--own--rbx-metrics|rbx-metrics]] | KB benchmark comparison, prioritised fix list, 14-day test plan
Roblox updates / events calendar | [[A--own--rbx-liveops|rbx-liveops]] [a] | cadence by team size, 12-week calendar, rollback rules
Roblox Luau system (secure, performant) | [[A--own--rbx-engineer|rbx-engineer]] [a], [[S--own--rbx-remote-sec|rbx-remote-sec]], [[S--own--rbx-datastore|rbx-datastore]] | server-authoritative code with doc-verified APIs
Roblox launch readiness | [[S--own--rbx-launch-check|rbx-launch-check]] | interactive tailored checklist from the merged KB checklists
Roblox Studio control (read/edit places) | docs: mcp/roblox-studio-mcp.md | built-in Studio MCP server, project-scoped config only

## Design, UX, docs
frontend design | frontend-designer [a] (in AI Library Vault), anthropic-skills/frontend-design (in AI Library Vault), design-system-starter (in AI Library Vault) | distinctive, responsive UI; tokens to start from
UI critique | ui-critic [a] (in AI Library Vault), anthropic-knowledge-work/design-critique (in AI Library Vault), gstack/design-review (in AI Library Vault) | hierarchy/usability findings, ranked
accessibility audit | accessibility-reviewer [a] (in AI Library Vault), anthropic-knowledge-work/accessibility-review (in AI Library Vault), wshobson/wcag-audit-patterns (in AI Library Vault) | WCAG 2.2 AA with code-level fixes
UX heuristic evaluation | ux-heuristic-evaluation (in AI Library Vault) | Nielsen 10 plus mobile checks
UX copy / microcopy | anthropic-knowledge-work/ux-copy (in AI Library Vault) | buttons, errors, empty states
design system / brand | anthropic-knowledge-work/design-system (in AI Library Vault), anthropic-skills/brand-guidelines (in AI Library Vault), wshobson/design-system-patterns (in AI Library Vault) | audit and extend tokens and components
design handoff | anthropic-knowledge-work/design-handoff (in AI Library Vault) | spec sheet for engineering
documentation / README | docs-writer [a] (in AI Library Vault), readme-template (in AI Library Vault), anthropic-knowledge-work/documentation (in AI Library Vault) | verified against real commands
architecture decision (ADR) | anthropic-knowledge-work/architecture (in AI Library Vault), wshobson/architecture-decision-records (in AI Library Vault) | trade-offs and consequences
system design | anthropic-knowledge-work/system-design (in AI Library Vault), jeffallan/architecture-designer (in AI Library Vault) | service boundaries, data model, APIs
diagrams | trailofbits/diagramming-code (in AI Library Vault), gstack/diagram (in AI Library Vault) | code and architecture diagrams

## Research, product, marketing
deep research | [[A--own--deep-researcher|deep-researcher]] [a], [[S--own--research-method|research-method]], alirezarezvani/deep-research (in AI Library Vault) | cited, dated, confidence-rated
deep topic research across GitHub/YouTube/Reddit/blogs | [[S--own--rbx-research|rbx-research]], [[S--own--research-method|research-method]] | asks usage/time/worker caps first, ranks best creators, reads their whole back-catalogue, resumable, writes a cited vault; shareable zip, own YouTube transcript tool
quick lookup | [[A--own--quick-researcher|quick-researcher]] [a], mattpocock/research (in AI Library Vault) | one or two sources, fast
competitive analysis | competitive-analyst [a] (in AI Library Vault), anthropic-knowledge-work/product-management/competitive-brief (in AI Library Vault), pm-skills/competitor-analysis (in AI Library Vault) | positioning gaps, battlecards
SEO audit | seo-analyst [a] (in AI Library Vault), anthropic-knowledge-work/seo-audit (in AI Library Vault), marketing-skills/seo-audit (in AI Library Vault) | prioritised quick wins
copywriting | copywriter [a] (in AI Library Vault), marketing-skills/copywriting (in AI Library Vault), marketing-copy-checklist (in AI Library Vault) | headline variants; checklist before shipping
landing page / CRO | awesome-copilot/landing-page-conversion-audit (in AI Library Vault), voltagent-subagents/landing-page-copywriter [a] (in AI Library Vault) | conversion-leak fix list; hero and CTA copy
email sequence / cold outreach | anthropic-knowledge-work/email-sequence (in AI Library Vault), marketing-skills/cold-email (in AI Library Vault) | full drip with timing; B2B outbound
content / blog / social | anthropic-knowledge-work/content-creation (in AI Library Vault), marketing-skills/social (in AI Library Vault), alirezarezvani/content-production (in AI Library Vault) | channel-specific drafts
campaign plan | anthropic-knowledge-work/campaign-plan (in AI Library Vault) | objectives, channels, calendar, metrics
PRD / spec | spec-writer [a] (in AI Library Vault), prd-outline (in AI Library Vault), anthropic-knowledge-work/write-spec (in AI Library Vault) | goals, non-goals, acceptance criteria
roadmap / prioritisation | anthropic-knowledge-work/roadmap-update (in AI Library Vault), pm-skills/prioritization-frameworks (in AI Library Vault) | Now/Next/Later; RICE-style scoring
product strategy | pm-skills/product-strategy (in AI Library Vault), pm-skills/product-vision (in AI Library Vault), pm-skills/strategy-red-team (in AI Library Vault) | canvas, vision, then attack the plan
brainstorming | superpowers/brainstorming (in AI Library Vault), anthropic-knowledge-work/product-brainstorming (in AI Library Vault), mattpocock/grilling (in AI Library Vault) | turn ideas into designs; stress-test them
user research synthesis | anthropic-knowledge-work/research-synthesis (in AI Library Vault), anthropic-knowledge-work/user-research (in AI Library Vault) | themes, personas, next steps
metrics / experiments | anthropic-knowledge-work/metrics-review (in AI Library Vault), pm-skills/ab-test-analysis (in AI Library Vault), pm-skills/north-star-metric (in AI Library Vault) | scorecards and test readouts
sprint planning / status | anthropic-knowledge-work/sprint-planning (in AI Library Vault), anthropic-knowledge-work/stakeholder-update (in AI Library Vault), pm-skills/sprint-plan (in AI Library Vault) | capacity-based plan; audience-tailored update
customer support | anthropic-knowledge-work/ticket-triage (in AI Library Vault), anthropic-knowledge-work/kb-article (in AI Library Vault) | triage and knowledge-base answers
sales outreach | anthropic-knowledge-work/draft-outreach (in AI Library Vault), agency-agents/Sales Outreach [a] (in AI Library Vault) | personalised sequences
hiring | anthropic-knowledge-work/hiring-screener (in AI Library Vault), anthropic-knowledge-work/interview-prep (in AI Library Vault) | rubric-based shortlist; interview prep

## Data, AI, finance, documents
data analysis | data-analyst [a] (in AI Library Vault), data-analysis-checklist (in AI Library Vault), anthropic-knowledge-work/statistical-analysis (in AI Library Vault) | checked numbers and caveats
SQL queries | anthropic-knowledge-work/sql-queries (in AI Library Vault), anthropic-knowledge-work/write-query (in AI Library Vault) | dialect-aware query writing
data visualisation | anthropic-knowledge-work/data-visualization (in AI Library Vault), agency-agents/Data Visualization Engineer [a] (in AI Library Vault) | chart choice and honest encoding
ML pipeline / MLOps | wshobson/ml-pipeline-workflow (in AI Library Vault), jeffallan/ml-pipeline (in AI Library Vault), davila7/mlops-engineer [a] (in AI Library Vault) | training to serving
LLM evals / RAG | wshobson/llm-evaluation (in AI Library Vault), alirezarezvani/agent-regression-evals (in AI Library Vault), wshobson/rag-implementation (in AI Library Vault) | prove changes did not make it worse
prompt engineering | prompt-engineer [a] (in AI Library Vault), prompt-review (in AI Library Vault), wshobson/prompt-engineering-patterns (in AI Library Vault) | evals on real cases; brief review
agent / multi-agent design | alirezarezvani/agent-workflow-designer (in AI Library Vault), anthropic-plugins-official/agent-development (in AI Library Vault), anthropic-skills/claude-api (in AI Library Vault) | patterns, SDK, Claude API facts
MCP server | anthropic-skills/mcp-builder (in AI Library Vault), anthropic-plugins-official/build-mcp-server (in AI Library Vault) | official guides
skill / plugin authoring | anthropic-skills/skill-creator (in AI Library Vault), superpowers/writing-skills (in AI Library Vault), [[S--own--add-to-library|add-to-library]] | write and test skills
finance model (DCF / 3-statement) | anthropic-financial/dcf-model (in AI Library Vault), anthropic-financial/3-statement-model (in AI Library Vault), anthropic-financial/model-builder [a] (in AI Library Vault) | live Excel models
LBO / M&A | anthropic-financial/lbo-model (in AI Library Vault), anthropic-financial/merger-model (in AI Library Vault) | accretion/dilution, returns
comps / valuation review | anthropic-financial/comps-analysis (in AI Library Vault), anthropic-financial/valuation-reviewer [a] (in AI Library Vault) | multiples and sanity checks
earnings / equity research | anthropic-financial/earnings-analysis (in AI Library Vault), anthropic-financial/equity-research (in AI Library Vault), anthropic-financial/earnings-preview (in AI Library Vault) | reports and previews
accounting close / variance | anthropic-financial/gl-recon (in AI Library Vault), anthropic-knowledge-work/variance-analysis (in AI Library Vault) | reconciliations, commentary
Excel / spreadsheets | anthropic-financial/xlsx-author (in AI Library Vault), davila7/spreadsheet (in AI Library Vault) | headless xlsx creation and edits
PDF | davila7/pdf (in AI Library Vault), awesome-copilot/convert-pdf-to-md (in AI Library Vault) | extract, create, convert
slides / PPTX | anthropic-financial/pptx-author (in AI Library Vault), wshobson/pptx-deck-creation-builder [a] (in AI Library Vault) | headless deck production
legal-ish review (not legal advice) | anthropic-knowledge-work/contract-review (in AI Library Vault), anthropic-knowledge-work/legal-risk-assessment (in AI Library Vault), agency-agents/Legal Document Review [a] (in AI Library Vault) | NDA/MSA flags, risk grading
compliance | agency-agents/Compliance Auditor [a] (in AI Library Vault), anthropic-knowledge-work/compliance-check (in AI Library Vault) | SOC 2 / ISO / HIPAA gaps
scientific literature / peer review | scientific-skills/literature-review (in AI Library Vault), scientific-skills/peer-review (in AI Library Vault) | systematic search; structured assessment
statistics | anthropic-knowledge-work/statistical-analysis (in AI Library Vault), agency-agents/Statistician [a] (in AI Library Vault) | method choice and interpretation
web scraping | alirezarezvani/universal-scraping-architect (in AI Library Vault), gstack/scrape (in AI Library Vault) | validation-heavy extraction

## Security
threat model | threat-model-quick (in AI Library Vault), wshobson/stride-analysis-patterns (in AI Library Vault) | ranked threats and mitigations
dependency / supply chain | dependency-auditor [a] (in AI Library Vault), trailofbits/supply-chain-risk-auditor (in AI Library Vault) | advisories, abandonment, licences
static analysis | trailofbits/semgrep (in AI Library Vault), trailofbits/codeql (in AI Library Vault), trailofbits/sarif-parsing (in AI Library Vault) | scan and triage results
fuzzing | trailofbits/harness-writing (in AI Library Vault), trailofbits/libfuzzer (in AI Library Vault), trailofbits/aflpp (in AI Library Vault) | harnesses and obstacles
smart contract audit | agency-agents/Blockchain Security Auditor [a] (in AI Library Vault), trailofbits/solana-vulnerability-scanner (in AI Library Vault) | EVM and chain-specific scanners
web pentest (authorised only) | cybersecurity-skills/performing-web-application-penetration-test (in AI Library Vault) | WSTG-based method
malware / reverse engineering | cybersecurity-skills/performing-static-malware-analysis-with-pe-studio (in AI Library Vault), wshobson/binary-analysis-patterns (in AI Library Vault) | static triage first
forensics / IR | agency-agents/Incident Responder [a] (in AI Library Vault), cybersecurity-skills/performing-endpoint-forensics-investigation (in AI Library Vault) | evidence handling and containment
secrets / hardening | wshobson/secrets-management (in AI Library Vault), cybersecurity-skills/hardening-docker-containers-for-production (in AI Library Vault) | vault patterns; CIS Docker

## Ops, infra, hosts
CI / build fixes | ci-fixer [a] (in AI Library Vault), wshobson/github-actions-templates (in AI Library Vault), wshobson/deployment-pipeline-design (in AI Library Vault) | from logs to fix
Docker / Kubernetes | 0xfurai-subagents/docker-expert [a] (in AI Library Vault), awesome-copilot/multi-stage-dockerfile (in AI Library Vault), wshobson/k8s-manifest-generator (in AI Library Vault) | images, manifests, rollouts
Terraform / IaC | wshobson/terraform-module-library (in AI Library Vault), cybersecurity-skills/auditing-terraform-infrastructure-for-security (in AI Library Vault) | modules; security scan
cloud architecture | alirezarezvani/azure-cloud-architect (in AI Library Vault), alirezarezvani/aws-solution-architect (in AI Library Vault), google-skills/google-cloud-waf-operational-excellence (in AI Library Vault) | Azure/AWS/GCP design
release | release-manager [a] (in AI Library Vault), release-checklist (in AI Library Vault), anthropic-knowledge-work/deploy-checklist (in AI Library Vault) | go/no-go and rollback
incident response (ops) | anthropic-knowledge-work/incident-response (in AI Library Vault), wshobson/postmortem-writing (in AI Library Vault), agency-agents/Incident Response Commander [a] (in AI Library Vault) | triage, comms, blameless postmortem
observability / SLOs | alirezarezvani/observability-designer (in AI Library Vault), wshobson/slo-implementation (in AI Library Vault) | metrics, logs, traces, SLIs
Windows admin | windows-sysadmin [a] (in AI Library Vault), davila7/powershell-windows (in AI Library Vault), desktop-layout-restore (in AI Library Vault) | PowerShell pitfalls; undo GUI automation
Linux admin | linux-sysadmin [a] (in AI Library Vault), linux-ssh-script-pattern (in AI Library Vault) | systemd/pacman/ssh, verifiable scripts
remote machine runs | [[A--own--remote-device-runner|remote-device-runner]] [a], [[S--own--remote-claude-run|remote-claude-run]] | headless Claude over SSH, detached with log
browser automation | browser-operator [a] (in AI Library Vault), chrome-task-pattern (in AI Library Vault), gstack/browse (in AI Library Vault) | Claude in Chrome safe steps
GitHub ops | github-operator [a] (in AI Library Vault), github-private-repo (in AI Library Vault), trailofbits/gh-cli (in AI Library Vault) | private-by-default; gh CLI patterns
git workflow | superpowers/using-git-worktrees (in AI Library Vault), superpowers/finishing-a-development-branch (in AI Library Vault) | isolation and clean merge

## Orchestration (manager habits)
split a big goal | [[A--own--task-decomposer|task-decomposer]] [a], task-planner [a] (in AI Library Vault), superpowers/writing-plans (in AI Library Vault) | independent jobs with briefs
parallel workers | superpowers/dispatching-parallel-agents (in AI Library Vault), superpowers/subagent-driven-development (in AI Library Vault), superpowers/executing-plans (in AI Library Vault) | fan-out and review loops
act as a manager (any session) | [[S--own--rbx-manager|rbx-manager]] | one skill: size the job, pick model/effort, brief, check reports, usage cap, ledger, verifier; /rbx-manager install-presets adds sonnet-worker/haiku-scout/opus-builder
keep Claude cheap / low usage for the whole session | rbx-low-usage | /rbx-low-usage on|off|status; marker + UserPromptSubmit/SessionStart hooks keep it on after compaction; every reply starts 'low usage mode enabled.'
brief a worker | [[S--own--worker-brief-template|worker-brief-template]], [[S--own--worker-report-format|worker-report-format]], [[S--own--model-routing|model-routing]] | self-contained AI-to-AI briefs; pick model/effort
verify a claim | [[A--own--verifier|verifier]] [a], superpowers/verification-before-completion (in AI Library Vault) | re-run checks before reporting success
hand off long results | [[S--own--artifact-handoff|artifact-handoff]], phone-friendly-reporting (in AI Library Vault), mattpocock/handoff (in AI Library Vault) | link plus short summary

## Roblox and game development (added 2026-10-29)
make a game / plan a game | [[S--own--rbx-workflow|rbx-workflow]], [[S--own--rbx-plan|rbx-plan]], [[S--own--rbx-rate|rbx-rate]] | /rbx-workflow: asks only for the idea, elaborates from the vault, rates 1.00-10.00, plans (skills/agents/models/cap), asks Ready to build, then a head manager builds and playtests
rate a game idea | [[S--own--rbx-rate|rbx-rate]], [[S--own--rbx-ideas|rbx-ideas]] | 12 weighted criteria with vault-derived weights, computed score, strengths/weaknesses/fixes, what is hot now
Roblox ads plan / tutorial | [[S--own--rbx-ads|rbx-ads]], [[S--own--rbx-ad-plan|rbx-ad-plan]] | reads newest ad notes and live-checks costs and policy every run; never spends
Roblox update roadmap / patch notes | [[S--own--rbx-game-update|rbx-game-update]], [[A--own--rbx-liveops|rbx-liveops]] [a] | cadence, events calendar, retention levers, A/B ideas, patch notes; reads newest live-ops notes
Roblox icon / thumbnail images with Nano Banana | [[S--own--rbx-thumbnail|rbx-thumbnail]], [[S--own--rbx-thumb-brief|rbx-thumb-brief]] | looks up the newest image model from the user's own key, prompts + reference guidance + content-rules checklist
Roblox playtest without Studio | [[S--own--rbx-playtest|rbx-playtest]], [[A--own--rbx-tester|rbx-tester]] [a] | Studio MCP if present, else luau-check + static scan + code-walk; bug and feel report
Roblox DataStore / saving | [[S--own--rbx-datastore|rbx-datastore]], [[S--roblox-brain--roblox-server-data|roblox-brain/roblox-server-data]], [[S--luau-skills--roblox-data|luau-skills/roblox-data]] | safe UpdateAsync + session lock + test list; sourced KB; API detail
Roblox exploit review | [[S--own--rbx-remote-sec|rbx-remote-sec]], [[A--own--rbx-reviewer|rbx-reviewer]] [a], [[S--roblox-brain--roblox-security|roblox-brain/roblox-security]] | remote validation table; severity-ranked review agent
Roblox monetisation | [[S--own--rbx-monetize|rbx-monetize]], [[S--roblox-brain--roblox-monetization|roblox-brain/roblox-monetization]], [[S--roblox-skills-ashexplained--roblox-monetization-optimization|roblox-skills-ashexplained/roblox-monetization-optimization]] | ProcessReceipt done right plus ethical pricing
Roblox economy design | [[A--own--rbx-economist|rbx-economist]] [a], [[S--own--game-economy-simulation|game-economy-simulation]], [[S--roblox-skills-ashexplained--roblox-economy-balancing|roblox-skills-ashexplained/roblox-economy-balancing]] | simulate before coding
Roblox Luau style | [[S--own--rbx-luau|rbx-luau]], [[S--luau-skills--luau-core|luau-skills/luau-core]], [[S--luau-skills--luau-types|luau-skills/luau-types]] | strict typing, task library, lifecycle and leak cleanup
Roblox architecture (OOP / components / ECS / pooling) | [[S--own--rbx-arch|rbx-arch]] | evidence-based pattern choice with Luau examples
Roblox bug fix (reproduce first) | rbx-playtest (Fix loop) | red check before the edit, same check green after, RED and GREEN ledger
Roblox balance / optimise with a number | [[S--own--rbx-tune|rbx-tune]] | baseline, one change per experiment, keep or revert, ledger checked by tune_check.py
Roblox code gates (comments, stubs, security) | rbx-critic (code_gates.py) | scored never blocking; the critic must run them before GOOD
Roblox project setup (Rojo) | [[S--own--rbx-rojo|rbx-rojo]], [[S--roblox-skills-el4cteo--roblox-studio-mcp|roblox-skills-el4cteo/roblox-studio-mcp]] | file-based workflow Claude can edit
Roblox UI | [[S--own--rbx-ui|rbx-ui]], [[S--roblox-brain--roblox-gui|roblox-brain/roblox-gui]] | phone-first scaling and safe areas
Roblox performance | [[S--own--rbx-perf|rbx-perf]], [[S--roblox-brain--roblox-performance|roblox-brain/roblox-performance]] | measure first; MicroProfiler
Roblox round / minigame loop | [[S--own--rbx-rounds|rbx-rounds]], [[S--roblox-skills-el4cteo--roblox-teleport-matchmaking|roblox-skills-el4cteo/roblox-teleport-matchmaking]] | state machine and cleanup
Roblox NPC / enemy AI | [[S--own--rbx-npc|rbx-npc]], [[S--roblox-brain--roblox-npc-ai|roblox-brain/roblox-npc-ai]] | pathfinding with network ownership
Roblox leaderboards / events | [[S--own--rbx-leaderboard|rbx-leaderboard]] | OrderedDataStore, badges, daily rewards
Roblox launch | [[S--own--rbx-publish|rbx-publish]], [[S--roblox-brain--roblox-publish-checklist|roblox-brain/roblox-publish-checklist]], [[A--own--rbx-tester|rbx-tester]] [a] | go / no-go for Roman to publish
Roblox analytics | [[S--own--rbx-analytics|rbx-analytics]], [[A--own--rbx-doctor|rbx-doctor]] [a], [[S--roblox-brain--roblox-analytics|roblox-brain/roblox-analytics]] | ranked experiments with thresholds
Roblox icon / thumbnails / ads | [[S--own--rbx-thumb-brief|rbx-thumb-brief]], [[A--own--rbx-marketer|rbx-marketer]] [a] | briefs and A/B plan; never spends Robux
Game design doc | [[A--own--game-design-doc-writer|game-design-doc-writer]] [a], [[S--own--rbx-ideas|rbx-ideas]], [[S--game-studios--brainstorm|game-studios/brainstorm]] | pitch to GDD
Game feel / level design | [[S--own--game-feel-checklist|game-feel-checklist]], [[S--own--level-design-review|level-design-review]] | polish and review checklists
Playtest feedback | [[S--own--playtest-feedback-synthesis|playtest-feedback-synthesis]], [[S--game-studios--playtest-report|game-studios/playtest-report]] | themes to ranked fixes
Game balance | [[A--own--game-balance-tester|game-balance-tester]] [a], [[S--game-studios--balance-check|game-studios/balance-check]] | simulate with numbers
Godot | [[A--own--godot-developer|godot-developer]] [a], [[S--godotprompter--godot-project-setup|godotprompter/godot-project-setup]], [[S--godotprompter--gdscript-patterns|godotprompter/gdscript-patterns]] | typed GDScript, headless tests
Unity | [[A--own--unity-developer|unity-developer]] [a] | C# with tests in batch mode
Game audio / art | [[S--own--game-sound-design-brief|game-sound-design-brief]], [[S--own--pixel-art-asset-pipeline|pixel-art-asset-pipeline]] | event lists, palettes, export specs
Promote a game | [[S--own--game-trailer-short-script|game-trailer-short-script]], [[S--own--game-update-announcement|game-update-announcement]] | drafts only, Roman approves posting
Manager: audit a worker report | [[A--own--report-auditor|report-auditor]] [a] | accept / re-brief / escalate
Manager: split into parallel jobs | [[A--own--parallel-job-splitter|parallel-job-splitter]] [a] | table of jobs with briefs
Manager: failed automation | [[A--own--incident-triager|incident-triager]] [a] | evidence-first triage

## AI-creator ideas (added 2026-11-01)
Best 10 from the Nate Herk / RoboNuggets / Karpathy research (job | item | why).
Vague request, before building | [[S--own--rbx-clarify|rbx-clarify]] | 3-7 multiple-choice questions with defaults, then one spec with success criteria
Audit a whole repo for bugs | [[A--own--parallel-audit-fanout|parallel-audit-fanout]] [a] | parallel auditors per area, a verifier per finding, HTML report, unverified findings dropped
Roblox exploit and bug sweep | [[A--own--rbx-auditor|rbx-auditor]] [a] | area auditors using rbx-reviewer, repro per exploit, remote inventory table
Rate anything 1-10 | [[S--own--rbx-rate-any|rbx-rate-any]] | weighted criteria with anchors, evidence per score, script-computed total, ordered fixes (Roblox ideas: rbx-rate; Luau code: rbx-code-rate)
Verified multi-angle research | research-lens-panel [a] (in AI Library Vault) | five expert lenses, contradiction map, peer review, every citation checked
Fact-check findings before building | [[A--own--rbx-verifier|rbx-verifier]] [a] | labels each finding seen / inferred / unknown
Smaller diffs, no unrelated edits | rbx-karpathy (in AI Library Vault) | think first, minimum code, surgical changes, success criteria
Unattended scheduled Claude task | scheduled-claude-routine-design (in AI Library Vault) | one skill holds the steps, tiny routine prompt, idempotent status file
Keep the main context clean | [[A--own--digest-scout|digest-scout]] [a] | cheap isolated reader that returns a capped digest
Big build split among workers | [[A--own--phased-build-orchestrator|phased-build-orchestrator]] [a] | exclusive file ownership, stronger model for design/review, verified status table
