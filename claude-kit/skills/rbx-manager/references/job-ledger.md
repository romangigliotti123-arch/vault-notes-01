# Job ledger (state on disk, survives compaction and limit stops)

Use for 2+ workers, any job > 20 min, or work that may outlive this session. Plain file `jobs.md` in the project (or `~/.claude/manager-jobs.md` without a project). Append rows; afterwards edit only Status and Note.

```
| id | title | worker (model/effort) | brief file | report file | started | deadline | status | note |
|----|-------|-----------------------|------------|-------------|---------|----------|--------|------|
| J1 | research X | sonnet/medium | briefs/j1.md | reports/j1.md | 14:02 | 14:45 | running | cap: 2 agents |
```
Status: queued | running | needs_user | done | failed | lost | cancelled.

1. Write the row BEFORE spawning; put the id in the brief.
2. `done`/`failed` is set by YOU after checking the report, never by the worker.
3. Before any outward side effect (message, push, publish, purchase) add a row "intent: <action>"; mark it done afterwards. After a restart an intent without done may already have happened: check real state before repeating.
4. After a restart, compaction or usage-limit stop: read the ledger and reconcile each open row with live state (agent still running? report file?). Report found => check it and close. Nothing found => mark `lost`, re-brief at most once.
5. Keep full reports in files; keep <= 250 words of each in context.
