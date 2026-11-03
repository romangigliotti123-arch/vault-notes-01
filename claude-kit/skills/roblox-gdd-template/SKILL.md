---
name: roblox-gdd-template
description: Fills in a one-to-three page game design document (GDD) for a Roblox experience from a concept, using the Roblox knowledge base for core-loop, onboarding, economy, retention and scope rules, with an evidence table. Use when the user wants a GDD, game design doc, design one-pager, concept document, or to turn a chosen idea into a build-ready design.
---

# Roblox GDD template

Output: a filled `GDD-<game>.md` built from `TEMPLATE.md` in this folder. For the full idea-to-GDD job with candidate scoring, use the `roblox-game-designer` agent; this skill is the template plus the fill-in rules.

## Procedure

1. Read `TEMPLATE.md` (same folder). Copy it to `GDD-<game>.md` in the project (or the path given).
2. Gather KB support (about 5 kbq calls):
   ```
   K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
   $K section core-loops-and-game-design instructions
   $K section first-session-onboarding instructions
   $K find "<genre> core loop progression economy sinks" -n 8
   $K case "<genre>" -n 2
   $K find "mistakes scope first game" -t common-mistakes -n 5
   $K num "D1 retention benchmark"
   ```
3. Fill every section with short sentences. Numbers you invent for the economy are marked ESTIMATE. Every external claim goes in the Evidence table with source link, flag (official / indie / mixed) and date.
4. Apply the checks: one-sentence pitch and named audience; three-layer loop; fun action within about 30 seconds; mid-term goals; a co-play or social hook; nothing core gated behind payment; MVP fits team and time; each milestone has a pass/fail acceptance test.
5. Return the path and a 5-line summary: the pitch, the loop, the first milestone, the biggest risk, the validation metric.

## Rules

- Patterns, not content: never copy another game's art, names, maps, code or story.
- All-ages: no paid randomness presented as a purchase without disclosure, no pay-to-win, no stranger contact without safeguards.
- Do not promise success; every risk has an early check that could prove it wrong.
