---
tags: [manager-kb, topic]
updated: 2026-11-01
---
# Claude Code features as a manager toolkit: best practice and unused features

Scope: subagent design, skills authoring, hooks, CLAUDE.md/memory hygiene, output styles, scheduled tasks and `/goal`, headless/SDK, permission modes, mods, plugin evals, introspection commands. Mechanics of subagents vs teams vs bg sessions, plugin loading, GitHub MCP, session naming, SSH patterns are in manager-setup.md and not repeated. Synthesised by the lead from the src- notes on disk (the assigned worker was stopped by the usage limit). Docs are Claude Code 2.1.312 (changelog head 2026-10-27).

Current setup facts (read from disk 2026-10-29): `~/.claude/settings.json` has no `hooks`, no `statusLine`, no `outputStyle`, no `permissions.deny`; `permissions.defaultMode: auto` but the master is launched with `--dangerously-skip-permissions`; only two agent presets (`sonnet-worker`, `opus-builder`) without `tools`, `maxTurns`, `omitClaudeMd` or `memory`; CLAUDE.md ~143 lines / ~29 KB (limit advice: <200 lines); master resumes the same conversation (id 78968f1c) on every boot.

## TL;DR
- Prose in CLAUDE.md is advisory; hooks and deny rules are enforced, and a hook "deny" or a `permissions.deny` rule holds even under bypassPermissions. Our "Always confirm first" list is prose only on a box that runs bypass with admin rights and a Telegram inbox. This is the single biggest gap this toolkit can close. [[src-ccdocs-hooks]], [[src-ccdocs-permission-modes-auto-mode]], [[src-ccdocs-memory]]
- CLAUDE.md should be short (<200 lines), hold only what the agent cannot discover, and be edited ruthlessly; ours is a log of history, device notes and past decisions, and it is also loaded into every subagent. [[src-ccdocs-memory]], [[src-humanlayer-claude-md-posts]], [[src-gh-anthropics-claude-code-repo]]
- Verification is the lever Anthropic's own people emphasise: give the worker a runnable check; add a Stop/SubagentStop hook where it must be deterministic. [[src-boris-cherny-tips]], [[src-ccdocs-hooks]]
- Subagents are for context control and fresh-eyes review, not "backend engineer" role play. [[src-humanlayer-skill-issue-harness]], [[src-ccdocs-sub-agents]]
- Under-used features that fit this box: `SubagentStop`/`Stop` hooks for report gating, `PreToolUse` guards, `omitClaudeMd` and `maxTurns` on presets, SessionStart hook with `prompt_cache_likely_expired`, `/goal` with a bound, `CLAUDE_CODE_RETRY_WATCHDOG` for `-p` workers, `claude plugin eval`/skill evals, custom concise output style for the phone. [[src-ccdocs-tools-commands-sandbox]], [[src-ccdocs-headless-cli]], [[src-ccdocs-plugin-evals]]
- The Windows host has no sandbox ("On native Windows, Claude Code runs commands unsandboxed"); the Linux box can. [[src-ccdocs-tools-commands-sandbox]]

## Rules
### Subagents and presets
1. **Write the description as a trigger specification: "Use this agent when ... Typical triggers include ..." and keep it under ~60 words.** Combined subagent descriptions over 15,000 tokens trigger a warning; descriptions are always in context. Add "use proactively" only for agents that should auto-dispatch. Evidence: [[src-gh-claude-plugins-official]], [[src-ccdocs-sub-agents]]. Confidence: high.
2. **Restrict tools by role for review/verification agents; do not micro-optimise tools for implementers.** Anthropic: reviewer with `tools: Read, Grep, Glob` cannot edit (enforced). HumanLayer: tool-thrash from per-agent tool tuning gave worse results. Resolve: read-only for verifier/scout, full tools for workers. Evidence: [[src-ccdocs-sub-agents]], [[src-humanlayer-skill-issue-harness]], [[src-gh-disler-hooks-mastery]] (validator `disallowedTools: Write, Edit`). Confidence: med-high.
3. **Set `maxTurns` and `omitClaudeMd` on presets.** `maxTurns` returns partial, resumable output (runaway guard); `omitClaudeMd: true` skips the big CLAUDE.md for narrow workers; `autoCompactWindow` per agent (100k-1M). Note: `disallowedTools: Bash(git push *)` removes the whole Bash tool; block specific commands with `permissions.deny`. Evidence: [[src-ccdocs-sub-agents]]. Confidence: high.
4. **Use subagents for context control and independent review.** "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help." Role-persona subagents ("frontend engineer") did not work for HumanLayer; subagents as a "context firewall" did. Evidence: [[src-humanlayer-skill-issue-harness]], [[src-ccdocs-best-practices]]. Confidence: med-high.
5. **Subagent output is scanned and (in auto mode) classifier-reviewed, but still untrusted input.** Control-tag lookalikes in a report get a backslash inserted; SendMessage content is classifier-reviewed. Evidence: [[src-ccdocs-subagent-nesting-siblings-teams]], [[src-ccdocs-permission-modes-auto-mode]]. Confidence: high.
6. **A subagent can deliver its report through `SubagentHandback` (2.1.271+) and `SubagentStop` can block with a reason.** This is a deterministic report-format gate: a hook can refuse to let a worker finish until `RESULT:`, `VERIFIED:` and `ARTIFACTS:` appear. Evidence: [[src-ccdocs-sub-agents]], [[src-ccdocs-hooks]]. Confidence: high (docs); untested here.

### Hooks and enforcement
7. **Anything that "must always/never happen" belongs in a hook or deny rule, not CLAUDE.md.** Hook exit 2 blocks; JSON `permissionDecision: deny` blocks even in bypass; `onFailure: "block"` makes a crashed hook fail closed (2.1.295+). Use the permission system (`Bash(git push *)` deny/ask) for simple command patterns; hook `if` filters are "best-effort". Evidence: [[src-ccdocs-hooks]], [[src-ccdocs-permission-modes-auto-mode]]. Confidence: high.
8. **Copy the exit-code convention exactly: exit 2 blocks and shows stderr to Claude; exit 1 shows the user only and the action proceeds.** Popular samples (disler) document exit 1 for failure, which does not block. Windows: PowerShell hooks need `shell: powershell`; JSON must be the only stdout. Evidence: [[src-gh-anthropics-claude-code-repo]], [[src-gh-disler-hooks-mastery]], [[src-ccdocs-hooks]]. Confidence: high.
9. **Stop hooks as back-pressure: silent on success, only errors on failure.** HumanLayer verification hook ran formatter+typecheck; 4,000 lines of passing test output flooded context. Guard against loops: check `stop_hook_active`; cap of 8 consecutive blocks. Evidence: [[src-humanlayer-skill-issue-harness]], [[src-ccdocs-hooks]]. Confidence: high.
10. **Inject context as facts, not imperatives.** `additionalContext` framed as out-of-band commands can trigger injection defences; 10,000 char cap. SessionStart receives `seconds_since_last_response`, `context_tokens`, `prompt_cache_likely_expired`, `estimated_cache_write_usd` on resume: usable to warn the manager that a resume costs a cache write. Evidence: [[src-ccdocs-hooks]]. Confidence: high.
11. **Hooks are the logging bus.** `SubagentStop` input has `last_assistant_message` and `agent_transcript_path`; events carry `agent_id`/`agent_type`. One-line job log per subagent costs nothing in tokens. Evidence: [[src-ccdocs-hooks]], [[src-gh-disler-hooks-mastery]] (JSON event logs). Confidence: high. See [[topic-observability]].
12. **Prefer a no-code permission rule over code for fixed patterns; mods only for state-dependent decisions.** Mods (2.1.287+) run in-process with account permissions, work under Remote Control, draw only on the host terminal. Third-party mod bundles are unreviewed code. Evidence: [[src-ccdocs-mods]]. Confidence: high.
13. **Guard-hook ecosystem exists but is unvetted.** Safety Net, Dippy (AST-based auto-approve), Gryph, hookify (sentence to rule file). Treat as ideas; each is third-party code with hook power. Evidence: [[src-gh-awesome-claude-code]], [[src-gh-claude-plugins-official]]. Confidence: low-med.

### CLAUDE.md, memory, output style
14. **CLAUDE.md: under 200 lines, concrete, only what the agent cannot discover; move procedures to skills or path-scoped rules.** Imports do not reduce cost; HTML block comments are stripped (free maintainer notes). Project-root CLAUDE.md survives `/compact`. `/doctor prompt-audit` finds stale paths and contradictions. Evidence: [[src-ccdocs-memory]], [[src-humanlayer-claude-md-posts]], [[src-gh-claude-plugins-official]] (`claude-md-improver`). Confidence: high.
15. **Delivery caveat: CLAUDE.md arrives as a user message; instruction-following degrades with count.** HumanLayer: frontier models follow ~150-200 instructions reliably; Claude Code's own prompt uses ~50. Wrap rarely-relevant sections in conditional blocks (`<important if="...">`, anecdotal). The ETH Zurich AGENTS.md study (second-hand): auto-generated files hurt (+20% cost), human-written helped ~4%. Evidence: [[src-humanlayer-claude-md-posts]], [[src-humanlayer-skill-issue-harness]]. Confidence: med.
16. **Compounding-learning habit: after every correction, add a rule; ruthlessly edit.** Boris Cherny: "Update your CLAUDE.md so you don't make that mistake again"; edit until mistake rate drops. Counterweight: HumanLayer "I have thrown away many more hooks than we actually use". Evidence: [[src-boris-cherny-tips]], [[src-humanlayer-skill-issue-harness]]. Confidence: med.
17. **Auto memory: MEMORY.md is an index; only the first 200 lines or 25 KB load.** Four memory types; subagents do not inherit auto memory (own `memory:` field). Evidence: [[src-ccdocs-memory]]. Confidence: high.
18. **Output style is the supported place for voice/length (phone brevity).** Built-in `Concise` works from Remote Control; custom styles must be selected on the host; subagents do not get the style. On 5.5-era models the shorter system prompt is default, so `keep-coding-instructions` is moot. Evidence: [[src-ccdocs-output-styles]]. Confidence: high.

### Skills
19. **Skill descriptions are the trigger; make them slightly "pushy", state when NOT to use.** Listing always shows every NAME; descriptions share a 1%-of-context budget; truncated at 1,536 chars; key use case first. Evidence: [[src-ccdocs-skills]], [[src-gh-anthropics-skills-skill-creator]]. Confidence: high.
20. **Progressive disclosure: SKILL.md < 500 lines; scripts executed not loaded; Gotchas section is the highest-signal content.** After compaction only the first 5,000 tokens of each recent skill are re-attached. Evidence: [[src-ccdocs-skills]], [[src-thariq-skills-lessons]]. Confidence: high (Thariq second-hand).
21. **Evaluate skills against a no-skill baseline in the same turn; measure tokens and time.** `skill-creator` runs with-skill and baseline subagents; `claude plugin eval` (2.1.269+) does N=3 runs with/without, six grader types, a cost ceiling and exit codes. It can test subagent delegation. Evidence: [[src-gh-anthropics-skills-skill-creator]], [[src-ccdocs-plugin-evals]]. Confidence: high.
22. **Skills are code-adjacent: treat like npm.** Skills registries have distributed malicious skills; anything in `~/.claude/skills` runs with full power. Evidence: [[src-humanlayer-skill-issue-harness]], [[src-willison-skills-and-agentic-loops]]. Confidence: med. See [[topic-agent-security]].

### Headless, scheduling, goals
23. **For scripted `claude -p` workers: set budget, turns, permission behaviour, retry watchdog.** `--max-turns`, `--max-budget-usd`, `--permission-prompts none`-style denial instead of hanging, `CLAUDE_CODE_RETRY_WATCHDOG=1` waits out 429/529 and usage-limit windows. `--bare` is API-key only and will become default for `-p` (watch for this on subscription). Exit 143 on SIGTERM leaves the turn unfinished. Evidence: [[src-ccdocs-headless-cli]]. Confidence: high.
24. **`/goal <condition>` is a small-model Stop hook that judges "done" from the transcript only.** It runs no tools, so write conditions the worker's own output can demonstrate; always include a bound ("or stop after 20 turns"). Works in `-p`. Evidence: [[src-ccdocs-scheduled-tasks-goal]]. Confidence: high.
25. **Scheduling limits matter for an always-on host.** `/loop` is session-scoped, recurring tasks expire after 7 days, fire only while Claude is idle, no catch-up for missed fires; cloud routines have 1-hour minimum and cannot touch local files. Use Windows Task Scheduler for host jobs. Evidence: [[src-ccdocs-scheduled-tasks-goal]]. Confidence: high.
26. **Agent SDK is the same engine as a library; subscription use is restricted.** Docs say third parties may not offer claude.ai login or rate limits; SDK programs are API-key oriented. Use only if we deliberately move a job to API billing. Evidence: [[src-agent-sdk-docs-and-python-readme]]. Confidence: high.

### Introspection and permission modes
27. **Use `/context`, `/usage` (`/cost`), `/doctor`, `/insights`, `/skill-doctor` regularly; note which do not work over Remote Control** (`/skill-doctor` does not). Third-party: ccusage, context-tax, cctop. Evidence: [[src-ccdocs-tools-commands-sandbox]], [[src-ccdocs-skills]], [[src-gh-awesome-claude-code]]. Confidence: high.
28. **bypassPermissions "offers no protection against prompt injection"; docs recommend isolated containers/VMs only.** Auto mode (classifier) is the documented alternative; deny rules and ask rules still apply in bypass. Boris Cherny: do not use `--dangerously-skip-permissions`. Evidence: [[src-ccdocs-permission-modes-auto-mode]], [[src-boris-cherny-tips]]. Confidence: high. See [[topic-agent-security]].
29. **Phone UX tools exist in-session:** `PushNotification`, `SendUserFile`, `AskUserQuestion` forwarded over Remote Control and held until answered, `askUserQuestionTimeout`, "Push when actions required". Evidence: [[src-ccdocs-tools-commands-sandbox]], [[src-ccdocs-mods]], [[src-ccdocs-headless-cli]]. Confidence: high. See [[topic-remote-mobile-ux]].
30. **12-factor thinking: human contact is a tool call; agents should be pausable/resumable at the tool-selection gap.** `PreToolUse` `defer`/`ask` and permission prompts fill the gap the 12-factor post names. Evidence: [[src-humanlayer-12-factor-agents]]. Confidence: med.

## Features we do not use yet but should evaluate (ranked)
1. **Deny rules + PreToolUse guard hook for the confirm-first list** (`git push`, `gh pr/repo/release`, `Remove-Item -Recurse` outside temp, `curl|iex`, edits to `~/.claude`, `.ssh`, firewall/`netsh`, `reg add HKLM`, `schtasks /delete`). Highest value, low cost.
2. **`maxTurns` + `omitClaudeMd` (+ `tools` for read-only scouts) on presets; add `haiku-scout`.**
3. **`SubagentStop` hook: append one line per worker to the job log and block on malformed reports.**
4. **Trim CLAUDE.md below ~200 lines, move device/runbook sections to files read on demand, enable `/doctor prompt-audit`.**
5. **`SessionStart` hook printing cache-expiry/cost info on resume and a rotation reminder.**
6. **Custom output style `phone-manager`** (select on host).
7. **`CLAUDE_CODE_RETRY_WATCHDOG=1` and `--max-budget-usd` in all scripted `claude -p` runs (cachyos-run.ps1).**
8. **`claude plugin eval`/skill-creator evals for the 3-5 own skills that matter** (brief-writer, report-checker).
9. **`/goal` with bounds for "keep going until X" jobs instead of ad-hoc re-prompting.**
Not recommended: agent teams, ruflo mods/plugins, hookify (installs hooks itself), `--bare` (API key only).

## What changed in 2026 (added 2026-11-01)
Features to know that were not ranked here before (all official docs, full page read):
- **Dynamic workflows** (`/workflows`, `/deep-research`, `ultracode` keyword, `workflowSizeGuideline`, saveable to `.claude/workflows/`): [[src-ccdocs-workflows-usage-and-limits]]. Keyword works only in human-typed prompts; in `-p`/SDK the launch needs an allow rule (`Workflow`) or bypass.
- **Agent teams** (experimental, `TeammateIdle`/`TaskCreated`/`TaskCompleted` hooks, `CLAUDE_CODE_SUBAGENT_MODEL` ordering): [[src-ccdocs-agent-teams]]. Keep disabled unless a job needs peer debate.
- **Cross-session messaging** (`ListAgents`, `SendMessage`, `notify_when_idle`, `crossSessionInbound`, `isolatePeerMachines`): [[src-ccdocs-cross-session-messaging]]. `notify_when_idle` is a zero-token way to learn a long-running session finished, usable instead of polling.
- **`/usage` attribution and recommendations; prompt-cache line**: [[src-ccdocs-costs-2026-update]].
Candidate (C-new, low risk): after any Claude Code upgrade, re-read the `workflows`, `agent-teams` and `costs` pages' version notes; several defaults changed between v2.1.2xx and v2.1.30x.

## Where sources disagree
- **Restrict tools per subagent (official docs, disler validators) vs do not (HumanLayer "tool thrash").** Follow: restrict for read-only verification/scout, not for workers.
- **Always plan first (Boris Cherny) vs "start simple, add config only on failure" (HumanLayer).** Compatible for a manager: plan = the brief and definition of done; no standing plan phase for trivial jobs.
- **Big instruction files (many hooks/rules) vs minimal.** Anthropic and HumanLayer agree: minimal; ruflo-style maximalism has no evidence behind it.
- **Longer context (1M) vs context isolation.** HumanLayer found adherence worse at 1M; Anthropic offers `autoCompactWindow` up to 1M. Single-team anecdote; test locally ([[topic-context-window-management]]).

## Applies to us
- Hooks/deny rules: missing entirely; top priority (see [[topic-agent-security]]).
- Presets: missing `maxTurns`, `omitClaudeMd`, read-only scout; both presets still tell workers to read the 29 KB CLAUDE.md (duplicate load).
- CLAUDE.md: oversized and mixes durable rules with dated status ("STATUS 2026-10-18 ...", "REBOOT TEST PASSED"); history belongs in log.md.
- Skills: library approach is right (not loaded); own skills lack evals.
- Output style / status line / `/goal` / retry watchdog: unused.
- Cannot do over Remote Control: `/skill-doctor`; sandbox does not exist on Windows.

## Candidate changes for us
- **C1 settings.json (user) hooks, deny rules.** Add (illustrative, test in a scratch session first):
```json
"permissions": { "deny": ["Bash(git push *)", "Bash(gh repo create *)", "Bash(gh release *)", "PowerShell(Remove-Item -Recurse * ~\\.ssh*)"], "ask": ["Bash(gh pr create *)", "Bash(gh api -X POST *)"] }
```
plus a `PreToolUse` command hook `confirm-first-guard.ps1` returning `permissionDecision: "ask"` (not deny) for matches so Roman can approve from the phone. Benefit: confirm-first becomes mechanical. Risk: false prompts, hook crash (use `onFailure: "block"` only after testing). Evidence: rules 7-8, 28.
- **C2 agents/*.md frontmatter:** `sonnet-worker`: add `maxTurns: 60`, remove the line "Read ~\.claude\CLAUDE.md" and set `omitClaudeMd: true` after moving the five facts workers need into a 40-line `~\claude-host\WORKER-NOTES.md` that the brief points to; `opus-builder`: `maxTurns: 100`. New `haiku-scout`: `model: haiku`, `effort: low`, `tools: Read, Grep, Glob, Bash`, `omitClaudeMd: true`, `maxTurns: 15`. Benefit: tokens per worker, runaway guard. Risk: workers lose machine rules, hence WORKER-NOTES. Evidence: rules 1-3.
- **C3 SubagentStop log hook:** append `{time, agent_type, agent_id, first 200 chars of last_assistant_message}` to `claude-host\jobs\subagents.jsonl`. Evidence: rule 11.
- **C4 CLAUDE.md diet:** target 120 lines: keep Naming, Manager role, routing, library pointers, confirm-first, screenshots rule, link to `RUNBOOK-*.md` files for Linux power/CachyOS tools/telegram/disk cleanup. Delete the "Pending work" and "STATUS" history (log.md keeps it). Evidence: rules 14-16.
- **C5 output style `phone-manager.md`:** "Lead with the outcome in one sentence. <= 6 lines unless asked. Anything Roman must do goes last, in its own paragraph. Paths absolute, no markdown tables." Select with `/output-style phone-manager` on host. Evidence: rule 18.
- **C6 `cachyos-run.ps1` flags:** add `--max-budget-usd`, `--max-turns`, and `CLAUDE_CODE_RETRY_WATCHDOG=1` to remote `claude -p` templates. Evidence: rule 23.

## Open questions
- Does `SubagentStop` fire for background (notification-style) subagents on the host in the same way? Test with a 10-line hook before relying on it.
- Does a `PreToolUse` `ask` decision reach the phone via Remote Control while the master runs bypass? Docs say permission prompts are forwarded; hooks returning `ask` under bypass are not documented in the notes read.

## From Nate Herk / RoboNuggets / Karpathy

Added 2026-11-01 from 549 creator videos (Nate Herk, RoboNuggets, Andrej Karpathy). Practitioner evidence: [demonstrated] = shown working in a video, [opinion] = advice. Weigh below the official/benchmarked sources above; where they disagree see [[src-creators-disagreements]].

- **Use plan mode before agents change things.** Review the proposal, then approve. Why: you catch wrong approaches before they cost anything. [demonstrated] (T20; [[src-nate-herk-agent-practice]])
- **Split planner, implementer and validator into separate sessions linked by handoff documents.** Why: it keeps each session out of the "dumb zone" of a bloated context. [opinion] (T21; [[src-nate-herk-agent-practice]])
- **Be specific in the plan about what happens when.** Plan the beats and the required outputs. Capable models can handle vague prompts if you add delegation and verification instructions. [opinion] (T22; [[src-nate-herk-agent-practice]])

## Related
[[topic-agent-security]], [[topic-observability]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-remote-mobile-ux]], [[topic-brief-prompt-engineering]], [[topic-multi-agent-frameworks]], [[topic-skill-library-retrieval]]
