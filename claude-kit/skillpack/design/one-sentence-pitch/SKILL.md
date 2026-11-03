---
name: one-sentence-pitch
description: "Compress a game idea into the single sentence a stranger can repeat, then derive the title, thumbnail subject and first-5-seconds promise from it, and test it on three cold readers. Use after idea-validator says GO or FIX on clarity, before art, title or thumbnail work."
category: design
tags: pitch, one sentence, elevator, title, thumbnail, clarity, hook, concept, packaging
kb: Roblox/roblox-kb/game-ideas-and-genres.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/case-studies-slap-battles.md
related: idea-validator, genre-twist-finder, core-fantasy-definer, core-loop-designer, thumbnail-maker, title-generator, gdd-one-pager
---

# one-sentence-pitch

The vault's clarity test: if a stranger or a 12-year-old cannot repeat the game after one sentence (about 10-15 seconds, understood from the thumbnail), simplify. This skill writes that sentence and checks it; it never invents features.

## When to use
After `idea-validator`, or whenever the team describes the game in a paragraph. Not for: store description copy (`title-generator`), the thumbnail image itself (`thumbnail-maker`), or the loop (`core-loop-designer`).

## Inputs (max 2)
1. The premise in any length (default: `docs/idea.md`). 2. Target player (default: ages 9-14, mobile-first).

## Procedure
1. Extract three things from the premise: the player verb ("hatch", "dodge", "steal"), the object or world it acts on, and the twist. Stop if there is no single verb: send back to `core-loop-designer`.
2. Write the sentence in the form "You <verb> <object> to <reward>, but <twist>." Max 20 words, no genre jargon a 10-year-old would not use, no adjectives like "epic" or "unique". Write three variants.
3. Cold-read test: show each variant to three people (or three fresh AI contexts with no other info) and ask "what do you do in this game?". Record their answers verbatim. Pass = at least 2 of 3 restate the verb correctly. Stop and rewrite if fewer; do not defend the sentence.
4. Derive packaging from the winning sentence: title (the verb or fantasy in plain words, under about 30 characters), the thumbnail subject (one character or object doing the verb, readable at 100 px), and the first-5-seconds promise (what the player sees and does on spawn that proves the sentence; hand to `first-minute-designer`).
5. Mismatch check: the thumbnail promise must be what the first 30-90 seconds deliver. Clickbait raises first-play bounce and hurts ranking (`discovery-algorithm`).
6. Write `design/pitch.md` and run the doc check below.

## Studio MCP path
Design only; none needed. When a build exists, `screen_capture` the spawn view and compare it with the thumbnail subject.

## Fallback
Pure document. Cold readers can be people; mark AI cold reads `simulated`.

## Evidence
`game-ideas-and-genres` (pass the one-sentence test; AlvinBlox: players leave after 10 seconds; rasdev: 30 seconds to explain will not win), `thumbnails-icons` and `discovery-algorithm` (packaging gates every other signal; honest, readable thumbnails), `case-studies-slap-battles` (spawns you into slapping: the sentence is the first 5 seconds). The creator numbers are self-reported; check `creator-credibility.md` labels before quoting.

## Output
`design/pitch.md` with headings Sentence (winner plus two losers), Cold reads (answers, pass/fail), Title, Thumbnail, First-5-seconds promise.

## Acceptance checks
- [ ] Sentence is 20 words or fewer and contains exactly one verb the player performs.
- [ ] Cold-read result recorded with at least 3 verbatim answers and a pass/fail.
- [ ] Title and thumbnail subject both derive from the sentence, not from a new idea.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/pitch.md --kind pitch` prints PASS.

## Pitfalls
Writing a tagline instead of a description. Pitching the meta ("collect 500 pets") instead of the verb. Letting the twist outweigh the formula so nobody recognises the genre. Testing on teammates who already know the game.

## Related
`idea-validator`, `genre-twist-finder`, `core-fantasy-definer`, `first-minute-designer`, `gdd-one-pager`.
