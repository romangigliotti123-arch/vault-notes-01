---
name: genre-twist-finder
description: "Pick the 10-20 percent twist on a proven genre formula: name the formula's fixed parts, list 6 candidate twists, and keep the one that changes a single layer while the genre stays instantly readable. Use when a validated genre is saturated or the idea is a pure clone."
category: design
tags: genre, twist, differentiate, clone, formula, 80/20, saturated, mash-up, originality
kb: Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/genre-mechanics.md, Roblox/roblox-kb/trend-research-and-validation.md, Roblox/roblox-kb/case-studies-steal-an-egg.md, Roblox/roblox-kb/case-studies-steal-a-brainrot.md
related: idea-validator, competitor-teardown, one-sentence-pitch, core-fantasy-definer, core-loop-designer, rbx-trends
---

# genre-twist-finder

Vault rule (`game-ideas-and-genres`): do not invent a new genre; start from a proven loop and change roughly 10-20 percent. Exact clones rarely blow up; totally original games are harder to blow up. This skill finds the twist and proves it does not break readability.

## When to use
When `idea-validator` flags "saturated" or "clone", or the team cannot say what is different. Not for: finding the genre (`rbx-ideas`, `rbx-trends`), or analysing a rival in depth (`competitor-teardown`).

## Inputs (max 2)
1. The reference game(s) or genre (default: the validator's comparables). 2. What the team can build in the time box (default: one week of art plus one new mechanic).

## Procedure
1. Write the formula in one line from the references: "<verb> -> <reward> -> <upgrade> -> <new area>". List its fixed parts (the 80-90 percent players already understand) and mark them LOCKED.
2. Generate six twists, one per layer: (a) the verb, (b) the reward object, (c) the upgrade path, (d) the setting or fantasy, (e) the social mode (co-op, steal, trade), (f) the risk (loss, chaser, timer). The vault's levers: combine 2-3 inspirations ("steal like an artist"), a non-game source, a new hook on the same loop.
3. Estimate the changed share per twist: count changed layers over total layers. Keep only twists of about 10-20 percent. Under 10 is a clone; over 40 needs a new validation (the vault's Ride a Pet example is a self-reported 40 percent change).
4. Readability test: state the genre plus twist in one sentence ("a <known genre> where <twist>"). A stranger must name the known genre from that sentence. Stop and drop any twist that fails.
5. Cost test: twist must be buildable in the time box and must feed the core loop (`core-loop-designer` filter). Drop twists that create a second loop.
6. Pick one; record the runners-up. Write `design/twist.md`; run the doc check.

## Studio MCP path
Design only.

## Fallback
Pure document. Reference facts come from the vault or from `rbx-trends`; label web facts `live-check`.

## Evidence
`game-ideas-and-genres` (change at least ~20 percent per Tizzy and AlvinBlox 80/20 rule, TRUSTED-labelled in `creator-credibility.md` but self-reported results; combine two or three inspirations; official signal that RPG, strategy, puzzle and shooter are underrepresented), `case-studies-steal-an-egg` and `case-studies-steal-a-brainrot` (a steal loop reskinned and extended: pattern only), `genre-mechanics` (modes that change the enemy, not the objective, add replayability without new content).

## Output
`design/twist.md`: Base formula (LOCKED parts), six candidate twists with changed-layer count, Twist (winner) with one-sentence readability test result, Cost, runners-up.

## Acceptance checks
- [ ] Locked parts and the winning twist are both written; changed share is stated and within about 10-40 percent.
- [ ] The readability sentence names a genre a stranger recognises (record who tested).
- [ ] The twist feeds an existing loop layer; no new parallel loop.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/twist.md --kind twist` prints PASS.

## Pitfalls
A cosmetic reskin counted as a twist. Twisting the verb, which breaks the one thing players understood. Three twists at once. Copying another game's names, art or code instead of its pattern.

## Related
`idea-validator`, `competitor-teardown`, `one-sentence-pitch`, `core-fantasy-definer`, `scope-cutter`.
