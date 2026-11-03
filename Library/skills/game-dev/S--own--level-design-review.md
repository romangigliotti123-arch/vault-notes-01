---
id: "level-design-review"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/level-design-review/SKILL.md"
description: "Review a game level or map for flow, readability, difficulty curve, teaching, pacing and replay value, with concrete fixes. Use when evaluating or planning levels, obbies, arenas or worlds."
orig_name: "level-design-review"
tags: [lib/skill, cat/game-dev, src/own]
---

# level-design-review

> Review a game level or map for flow, readability, difficulty curve, teaching, pacing and replay value, with concrete fixes. Use when evaluating or planning levels, obbies, arenas or worlds.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/level-design-review/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Level design review

Input: the level (playthrough notes, map screenshots, layout file) and the target audience. Output: ranked issues with a fix each.

1. Intent: one sentence for what the player learns or feels here. If it cannot be stated, the level lacks purpose.
2. Flow: a clear path from start to goal at a glance; landmarks (distinct shapes/colours/light) so players orient; no dead ends without a reward; loops back to hubs.
3. Teaching: introduce a mechanic safely, let the player use it, then test it with a twist, then combine it with others. Check that no new mechanic first appears under pressure.
4. Difficulty curve: sawtooth, tension then rest; first 60 seconds easy; checkpoints before hard sections; fail-forward (retry takes seconds).
5. Readability: safe vs dangerous things are distinguishable by colour/shape; no unfair hidden hazards; enough contrast on mobile screens.
6. Pacing and length: target play time stated; vary activities (traverse, puzzle, fight, rest); avoid repeating the same obstacle more than 3 times without change.
7. Rewards and secrets: optional paths with clear payoff; no required secrets.
8. Multiplayer: spawn spacing, choke points, griefing spots, late-join experience, camping spots.
9. Technical: part/draw budget, streaming, collision exploits (skipping geometry), out-of-bounds recovery.
10. Playtest evidence: where players died, hesitated or quit; list top 3 friction points from at least 3 observed runs or logs.

Report table: area | issue | evidence | severity | fix | cost.
