---
id: "master-session-hygiene"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/master-session-hygiene/SKILL.md"
description: "Runbook for keeping a 24/7 master session healthy: compaction thresholds, compact-instructions block, ledger re-injection, rotation levels L0-L4, handoff file, boot-script pitfalls (hard-coded resume id, forced model), idle cache cost."
orig_name: "master-session-hygiene"
tags: [lib/skill, cat/orchestration, src/own]
---

# master-session-hygiene

> Runbook for keeping a 24/7 master session healthy: compaction thresholds, compact-instructions block, ledger re-injection, rotation levels L0-L4, handoff file, boot-script pitfalls (hard-coded resume id, forced model), idle cache cost.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/master-session-hygiene/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Master session hygiene (compaction and rotation)

Measured on this host (manager-kb `src-local-master-usage-analysis`, 2026-10-29): the master compacted once (260k -> 22k tokens, 68 s); fixed baseline ~70k tokens per boot; two idle gaps (88 and 174 min) each forced a 52-69k-token cache re-write; six model switches in 40 minutes rebuilt 49-155k tokens of cache each; workers were 95% of all tokens. `boot-claude.ps1` resumes a hard-coded session id and forces `--model haiku`. Evidence base: manager-kb `topic-context-window-management`, `topic-context-engineering`, `topic-model-effort-routing-cost`.

## Levels
| Level | Trigger | Action |
|---|---|---|
| L0 hygiene | every job | full worker report to a file, <= 250 words in context; ledger line; pipe tool output through `Select-Object -First 40` / `head`; no dumps > 50 lines; do not switch my own model mid-session (delegate instead) |
| L1 warm compaction | idle >= ~1 h with context >= 100k, or Roman sends `/compact <focus>` at a natural break | compaction with the block below; SessionStart(compact) re-injects the ACTIVE ledger |
| L2 hard compaction | context reaches the configured window (suggested 250k) | automatic; same hooks |
| L3 rotation (rare) | 4+ compactions in 7 days; manager contradicts the ledger or re-asks settled things twice a week; Roman asks; before a planned multi-day outage | wait until no workers in flight (or name them in the ledger); manager writes `claude-host\manager\handoff-<date>.md` and updates the ledger; Roman types `/clear` then `/rename <master name>` (the model cannot); SessionStart(clear) re-injects handoff + ledger; update the session id file the boot script reads; verify against `/tasks` |
| L4 restart | crash/reboot | boot resumes; reconcile the ledger against live state before acting |
Open items: whether `/clear` changes the Remote Control row on claude.ai/the phone (test on a throwaway state first); whether a scheduled `/compact` via CronCreate actually runs (test once).

## Compact-instructions block (append to CLAUDE.md)
```
# Compact instructions
When compacting keep these sections in this order and keep exact identifiers (agent IDs/names, file paths, job slugs, IPs, commit hashes):
1. Roman's open requests and any pending approval (verbatim constraints).
2. Active jobs: id, agent name, model+effort, brief file, status, report file.
3. Decisions and standing preferences stated in chat that are not yet in CLAUDE.md or memory.
4. State of devices (this PC, CachyOS awake/quiet, [host]) and anything left running.
5. What was tried and failed, with the reason.
Drop raw tool output, worker report bodies (they are in files), greetings, superseded plans.
After compaction read claude-host\jobs ledger (jobs.py list) before acting; live state (/tasks, claude agents) wins over the ledger.
```

## Settings to consider (propose to Roman; they change behaviour)
`modelSettings`: `autoCompactWindow` 250000 for the manager model; `env.CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` = 100000; `CLAUDE_CODE_RETRY_WATCHDOG=1` for unattended waits. Do not run the 1M window by default (adherence degrades far earlier; every compaction/cold cache costs real usage).

## Boot script fixes (propose; edit only with Roman's OK)
Read the session id from a file the rotation step updates instead of a literal; stop forcing `--model haiku` on a resumed session that actually runs another model (it churns the cache); use `--fallback-model`.

## Pitfalls
Keep instruction files thin and hand-written: add a line only for a mistake the agent keeps repeating, after first trying to fix the code or add a check; one line under ~15 words; never paste `/init` output or repo overviews (generated context files did not raise success and cost over 20% more in the ETH Zurich AGENTS.md study; Theo MIXED, Nate Herk's applied-learning bullets agree; manager-kb takeaways 10, 47).
CLAUDE.md edits only take effect after /clear, /compact or restart; make them at job boundaries. Instructions given only in chat are lost at compaction: write standing rules to the right file the same turn. Keep the stable prefix stable (no timestamps at the top of injected text).
