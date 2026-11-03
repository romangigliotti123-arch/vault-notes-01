---
id: "job-ledger"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/job-ledger/SKILL.md"
description: "File-based job ledger, side-effect idempotency keys, hook event log and daily digest for a 24/7 manager (state on disk, survives restart/compaction); includes tested scripts jobs.py, hook_log.py, digest.py."
orig_name: "job-ledger"
tags: [lib/skill, cat/orchestration, src/own]
---

# job-ledger

> File-based job ledger, side-effect idempotency keys, hook event log and daily digest for a 24/7 manager (state on disk, survives restart/compaction); includes tested scripts jobs.py, hook_log.py, digest.py.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/job-ledger/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--sonnet-worker]], [[S--own--report-reading-protocol]]

---
# Job ledger, event log, digest (no LLM, no network, ~0 tokens)

Why: job state otherwise lives only in one long conversation and in subagent transcripts; after a restart, compaction or limit stop nobody knows what was in flight, what was retried, or what a night of workers cost. Evidence base: manager-kb `topic-long-running-always-on-agents`, `topic-observability`.

Scripts live beside this file in `scripts/` (copy to `~\claude-host\tools\`; run with `python -I`). Prototypes were run against this host's real transcripts; `jobs.py` and `digest.py` were re-tested 2026-10-29.

## jobs.py (append-only JSONL ledger at `~\claude-host\jobs\ledger.jsonl`, override with env JOBS_DIR)
```
python -I tools\jobs.py new "<title>" --worker sonnet-worker [--deadline-min 45]   -> prints job id (J261029-001)
python -I tools\jobs.py set <id> running|needs_roman|done|failed|lost|cancelled "<note>"
python -I tools\jobs.py list [--stale|--all]            (default: open jobs; STALE = open and past deadline)
python -I tools\jobs.py effect <id> <step-key>          -> NEW (exit 0) | INTENT-ONLY (exit 2: verify outside first) | DONE (exit 1)
python -I tools\jobs.py effect-done <id> <step-key>
```
Manager routine: `new` before spawning; put the id in the brief; `set running` at spawn; on the report, verify (see `report-reading-protocol`) then `set done|failed`; `done` is set only by the manager, never by the worker. Before any outward side effect (message to Roman or others, git push, PR, publish) run `effect`; NEW = proceed then `effect-done`; DONE = skip; INTENT-ONLY = a previous attempt may have succeeded: check real state (`git ls-remote`, the chat) before repeating. After a restart or compaction: `list` and `list --stale`, reconcile each open job against its worker transcript (final report found => verify and close; none => mark `lost`, re-brief at most once, attempts < 2), then reply in one line.

## hook_log.py (async hook; JSON line per event to `claude-host\events\events.jsonl` + `run\<session>.hb` heartbeat)
Register for SessionStart, SubagentStop, StopFailure, Stop and PreToolUse with matcher `Agent` (records the delegation decision: worker, model, effort, label, brief length). Never blocks, never raises, redacts token-shaped strings, no network. Confirm hook field names on the installed Claude Code with one test run before relying on `StopFailure`/`SubagentStop` fields.

## digest.py [YYYY-MM-DD] (answers "what happened overnight / what did it cost")
Reads `~/.claude/projects/*/*/subagents/agent-*.jsonl` + `.meta.json`: per job start, description, agent, model, effort, minutes, messages, output tokens, cache-read tokens, finished yes/NO; plus main-transcript totals and compaction counts. Token counts are de-duplicated by `message.id` (a message is written once per content block; naive sums over-count about 2x). Pull model: run on demand, do not schedule reports.

Install is a config change (hooks live in `~/.claude/settings.json`): propose to Roman first; the scripts alone can be copied and used without hooks.
