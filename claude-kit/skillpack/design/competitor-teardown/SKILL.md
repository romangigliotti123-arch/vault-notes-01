---
name: competitor-teardown
description: "Break a top competitor into transferable patterns (never content): first minute, core loop, progression, retention hooks, social, monetisation and packaging, each with a source and a how-to-reuse-as-pattern line, plus a do-not-copy list. Use when picking a genre or after launch to learn from a rival. Deeper than game-reviewer, narrower than trend research."
category: design
tags: competitor, teardown, analysis, benchmark, pattern, rival, reverse engineer, reference game
kb: Roblox/roblox-kb/trend-research-and-validation.md, Roblox/roblox-kb/case-studies-big-games.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/creator-credibility.md, Roblox/roblox-kb/case-studies-grow-a-garden.md
related: game-reviewer, genre-twist-finder, idea-validator, roblox-trend-research, core-loop-designer, first-minute-designer
---

# competitor-teardown

`game-reviewer` scores a game. This skill extracts reusable design patterns from one competitor and records the evidence, so the team copies mechanisms and never art, names, code or text.

## When to use
Choosing among two or three references, or learning why a rival retains. Not for: a quick quality verdict (`game-reviewer`), trend scans across many games (`roblox-trend-research`).

## Inputs (max 2)
1. The competitor (name or URL; default: top comparable from the validator). 2. The question (default: "why do players stay?").

## Procedure
1. Gather facts in this order: the local vault case study (`Roblox/roblox-kb/case-studies-<name>.md` if it exists), then the game page and a 15-minute play session, then the web (`roblox-trend-research`). Record each fact with its source and date. Stop at 8 facts per area; stale or unsourced numbers get `unverified`.
2. Walk the seven areas and write one pattern line each: first minute (time to first action and reward), core loop (verb, cycle time), progression (what unlocks, how often), retention hooks (daily, timers, events), social (invite, trade, co-op), monetisation (what is sold, what stays free), packaging (icon, title, thumbnail subject).
3. For each pattern add "Reuse as pattern: ..." rewritten in your own game's terms, and a "Why it works" claim marked evidence or `judgment`. Never copy content: names, art, music, text, code, UI layout.
4. Separate causes from luck: CCU spikes from hype, a brand deal or an influencer are not design. The vault's examples: hype with no reason to return faded (Concrete Cleaning), Grow a Garden fell from a peak once hype ended (tracker claims). Mark such facts `context`, not `pattern`.
5. Write the Do-not-copy list (anything unique to their IP) and the Gap list (what they do badly: your opening).
6. Save `design/teardown-<name>.md`; run the doc check.

## Studio MCP path
Design only. To play a rival, join it in the Roblox client; Studio MCP cannot inspect other places.

## Fallback
If you cannot play it, use the vault case study and public videos; mark play-derived rows `not played`.

## Evidence
`trend-research-and-validation` (method), `case-studies-big-games` and the per-game `case-studies-*.md` files (patterns only), `discovery-algorithm` (what the platform rewards), `creator-credibility.md` (only TRUSTED creators are authorities; tracker blogs and self-reported CCU are labelled claims).

## Output
`design/teardown-<name>.md`: Sources (with dates), seven Pattern lines each with Reuse and Why it works, Context (not design), Do not copy, Gaps.

## Acceptance checks
- [ ] Every pattern line has a source or `judgment`; no unlabelled numbers.
- [ ] Do-not-copy list is non-empty and names the IP-specific parts.
- [ ] At least one gap is listed (what the rival does worse than you could).
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/teardown-<name>.md --kind teardown` prints PASS.

## Pitfalls
Treating peak CCU as proof of design quality. Copying their economy numbers without their loop. Analysing five games shallowly instead of one well. Quoting a self-reported creator number as official.

## Related
`game-reviewer`, `genre-twist-finder`, `idea-validator`, `core-loop-designer`, `roblox-trend-research`.
