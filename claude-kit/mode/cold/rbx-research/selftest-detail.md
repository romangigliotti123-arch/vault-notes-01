<!-- cold: rbx-research/selftest-detail.md | read when: read only to understand what the offline self-test simulates. -->

## From skills/rbx-research/references/orchestration.md :: Try it without spending anything

`PY SKILL_DIR/scripts/selftest.py` runs mode A on a built-in fixture (cap 2): two concurrent simulated workers per wave follow real briefs through the real prep/save scripts, one worker fabricates numbers and is caught and retried, then themes, credibility and trust layer run, and a mode B pass finishes it. It uses `DTR_STUB=1`, the offline stand-in for model calls, which is for tests only.
