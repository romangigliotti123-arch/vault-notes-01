# Independent verifier

Use for irreversible, external, security, spend or config work; for negative claims ("nothing wrong", "cannot be done"); and when your own spot-check disagrees with the report. Skip it for reversible, low-stakes jobs where one spot-check is conclusive.

How
- Spawn a FRESH worker (sonnet, effort high; haiku only for pure existence checks). Give it: the DONE WHEN criteria, the artifact paths, the commands that can check them. Do NOT give it the first worker's conclusion or reasoning.
- Instruction: "Try to show each criterion is NOT met. Run the checks yourself. Change nothing. Report per criterion: holds / fails / cannot tell, with the command and an output excerpt."
- The verifier is read-only (restrict write tools if your setup allows, otherwise say so in the brief) and spawns no agents.
- A worker must never approve its own work with a subagent it spawned.
- Disagreement: trust evidence, not either party. Re-brief the original worker once with the failed criterion, or report partial to the user.
- Cost: one short extra worker, counted against the usage cap.

Order of checks: computational first (tests, linters, grep sensors, `luau-check.sh`), LLM verifier only for what they cannot see. Prove a sensor can fail by running it once on a seeded known-bad input. Verifier judgments are binary per criterion (holds / fails / cannot tell), not scores. Read the raw trace or output before trusting an eval or score. Roblox ladder: `game-dev-playtest/references/verification-ladder.md`. Source: manager knowledge base topics `topic-llm-judge-and-adversarial-verification` and `topic-managing-ai-agents-for-roblox-game-dev`.
