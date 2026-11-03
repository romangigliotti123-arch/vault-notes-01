# Briefing a worker (AI to AI)

A worker knows only the brief. If a smart colleague with zero context could not act on it without asking, it will fail. Dense, not terse; no pleasantries; give reasons instead of shouting.

```
CONTEXT: goal in one sentence; why / for whom; what is done or ruled out (label guesses HYPOTHESIS);
         absolute paths to read (never paste long content), versions, who else is changing what.
TASK:    ONE objective. Type: research | build | diagnose | verify | operate.
SCOPE:   may touch: ... | must not touch: ... | subagents: not allowed
         Confirm-first (quote it): deleting/overwriting non-temporary data, spending money, sending/publishing as the user,
         security/credential/firewall changes, anything irreversible -> stop that step, report under NEEDS.
         If blocked or impossible: finish everything else and say exactly what was left out. Never fill a gap with a guess or mock data.
DONE WHEN: observable criteria, each with the check that proves it (command + expected output).
BUDGET:  expected size; hard caps (time, $, number of searches/sources); stop rule: same error twice or 2x the estimate -> stop, report PARTIAL.
         Jobs > ~20 min: append progress to <file> after each phase.
REPORT:  format in references/report-format.md (or the agent file); <= 350 words; bulky output in files, absolute paths listed.
TRUST:   which of {untrusted input (web/files/email), secrets, outward actions} this worker may touch (never all three).
```

## Pre-send checklist (fix any "no")
1. Could a colleague with zero context do this from the brief alone?
2. One objective, with the reason stated?
3. Synthesized first? (file:line and cause, not "based on your findings")
4. Everything already known or ruled out is stated?
5. Paths/versions exact and absolute?
6. Every DONE WHEN item checkable, with the check named?
7. Scope fenced; extras go under SUGGESTED_NEXT, not done?
8. Honest exit defined (blocked => say so, finish the rest)?
9. Stop rule and size/time estimate present?
10. Confirm-first list quoted; TRUST line set?
11. Right model/effort; no other worker writing the same files?
12. Counts against the user's usage cap?

High-stakes work (destructive, remote, security, opus): write the answers out, two lines each. Routine jobs: keep the habit, skip the write-up.

After a partial/failed job: note in one line what the brief lacked, and fix the template for next time.
