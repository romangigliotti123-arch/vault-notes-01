---
name: core-fantasy-definer
description: "Write the role and feeling the player buys into (one sentence, three sensory beats, one anti-fantasy) and run every planned feature through it so the game answers why do I care, what is the setting and what am I grinding at. Use before the core loop is finalised or when features feel unrelated."
category: design
tags: fantasy, core fantasy, theme, role, feeling, identity, why do I care, coherence
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/case-studies-fisch.md, Roblox/roblox-kb/case-studies-bloxburg.md
related: idea-validator, one-sentence-pitch, core-loop-designer, world-theme-picker, scope-cutter, game-feel-polisher
---

# core-fantasy-definer

Vault (`core-loops-and-game-design`): offer a clear fantasy; the player should be able to answer why do I care, what is the setting and what am I grinding at. This skill turns that into a short document and a feature filter.

## When to use
After `idea-validator`, before or alongside `core-loop-designer`; again when a new feature does not fit. Not for: picking art style and setting (`world-theme-picker`) or the loop mechanics.

## Inputs (max 2)
1. The premise (default: `docs/idea.md`). 2. Player age band (default: 9-14).

## Procedure
1. Write the role: "You are a <role> who <does verb> in <place>". One role only. Stop if you need "and" twice.
2. Write the feeling: the emotion a good minute produces (power, calm collecting, risk-and-escape, ownership, discovery, status). Choose one primary feeling.
3. Write three sensory beats that prove it in play: a sound, a visual and a number or text moment (feeds `game-feel-polisher`). Example shape: "the thump of a hatch, the egg cracking open, a rarity banner".
4. Write the anti-fantasy: the one thing that would break the feeling (grind with no reward, unfair death, tutorial walls, pay-to-win). Add it to the pitfall list of the game.
5. Feature check: for every candidate feature write "serves the fantasy by ...". No answer = defer or cut (`scope-cutter`). Include monetisation items: a purchase that contradicts the fantasy (a pay-to-skip in a mastery fantasy) fails.
6. Say the fantasy out loud in the first-minute script: what the player sees in 5 seconds shows the role. Hand to `first-minute-designer`.
7. Save `design/fantasy.md`; run the doc check.

## Studio MCP path
Design only.

## Fallback
Pure document.

## Evidence
`core-loops-and-game-design` (clear fantasy; RPGs need an objective from the start; engagement before monetisation; prioritise long-engagement systems over cosmetics, single-mention from Deconstructor of Fun 2026-10), `player-psychology-and-game-feel` (feedback as reward), `game-ideas-and-genres` (simple culturally neutral concepts for ages 9-14), `case-studies-fisch` and `case-studies-bloxburg` (one clear role per game: pattern reading only).

## Output
`design/fantasy.md`: Fantasy (role sentence), Feeling, Sensory beats, Anti-fantasy, Feature check table (feature, serves how, keep/defer/cut).

## Acceptance checks
- [ ] One role sentence, one primary feeling, three beats (sound, visual, number).
- [ ] Anti-fantasy is specific and testable.
- [ ] Every planned feature and every monetisation item has a verdict.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/fantasy.md --kind fantasy` prints PASS.

## Pitfalls
A fantasy that is a genre label ("tycoon"). Two fantasies pulling opposite ways (horror plus cosy). Treating the fantasy as lore text instead of what the player does. Features added because a top game has them.

## Related
`one-sentence-pitch`, `core-loop-designer`, `world-theme-picker`, `scope-cutter`, `game-feel-polisher`.
