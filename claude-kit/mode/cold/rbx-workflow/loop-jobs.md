<!-- cold: rbx-workflow/loop-jobs.md | read when: read only when the user asks for a long unattended grind (port, optimise, polish to a reference). -->

## From skills/rbx-workflow/references/manager.md :: 6b. Loop jobs (only when the user asks for a long unattended grind: port, optimise, polish to a reference)

Default is the normal job loop above. Source: Theo (t3.gg), `NBCM_ZoWZo8` (MIXED, one creator's method, own numbers); the held-out check is from `Manager/src-gabor-evilgenie.md`.
1. GOAL = a check the worker runs itself that prints PASS/FAIL or a number, plus the target ("`luau-check.sh` clean AND `lune run Sim.spec.luau` prints PASS AND join time under 8 s in 3 runs"). No machine check, no loop: a goal that needs a human look stalls it.
2. Ratchet: when met, raise the bar in a NEW job (2x faster, old checks still green); do not widen the goal mid-run.
3. Visual target: matched-state screenshots of our build vs the reference, scored by a fresh judge (no history, written rubric). Choose the reference deliberately (a wrong reference burns the budget polishing the wrong thing). Patterns only, never copy.
4. Caps in the brief: iterations and spend per loop (the video's skybox polish ate about $800), and one held-out check the worker has not seen, to catch gaming the visible check.
5. Unblock check-in: when throughput drops (two jobs without a new DONE, or a loop with no progress), spawn a read-only fresh haiku/sonnet: "read `jobs.md` and the logs: the single biggest blocker or slowdown, and what it needs." Fix the top item (queue, tool, access, smaller test) and ask again; it repeats, it is not one-and-done.
6. After a reboot or crash, restart with "continue" plus the handoff file (`session-handoff`), not a re-explained brief.
