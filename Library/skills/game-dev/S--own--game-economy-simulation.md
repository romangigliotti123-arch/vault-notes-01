---
id: "game-economy-simulation"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/game-economy-simulation/SKILL.md"
description: "Model a game's currencies, income and prices in a quick Python simulation to find inflation, stalls and dominant strategies before shipping. Use when designing or rebalancing progression, shops or idle/tycoon economies."
orig_name: "game-economy-simulation"
tags: [lib/skill, cat/game-dev, src/own]
---

# game-economy-simulation

> Model a game's currencies, income and prices in a quick Python simulation to find inflation, stalls and dominant strategies before shipping. Use when designing or rebalancing progression, shops or idle/tycoon economies.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/game-economy-simulation/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Game economy simulation

1. Write the model as data: currencies, sources (rate, caps), sinks (price curves), upgrades with their effects, player archetypes (casual 10 min/day, regular 1 h/day, grinder 4 h/day), and time step.
2. Prices: geometric cost growth `cost(n) = base * growth^n` with growth typically in a 1.07-1.3 range; check that benefit growth is slightly below cost growth so progress slows but never stops, and prestige/rebirth resets give a visible multiple.
3. Simulate with a fixed seed over the real horizon (days or weeks). Output time-to-milestone per archetype, currency stock over time, share of income by source, and which upgrades are never bought or always bought first.
4. Detect problems: inflation (stock grows faster than sinks), stalls (more than a session with no purchase), runaway (one upgrade multiplies all), paid-item dominance (paid players 10x faster). Fix by changing curves, adding sinks, or capping.
5. Sensitivity: vary each parameter by +/-20 percent; report the ones that move time-to-milestone most (those are the tuning knobs).
6. Export a CSV and a one-page summary; keep the model file in the repo so tuning is repeatable. State the assumptions and what the model cannot capture (fun, social effects).
