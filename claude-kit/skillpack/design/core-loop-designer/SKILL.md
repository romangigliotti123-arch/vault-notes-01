---
name: core-loop-designer
description: "Turn a game premise into ONE core loop split into the three layers the vault uses (minute-to-minute action, session loop, progression engine) with cycle times, feedback beats, a reward schedule, a 'does it feed the loop' filter for every feature and the list of systems to cut. Use right after the idea passes validation and before systems are planned."
category: design
tags: core loop, loop, gameplay loop, progression, feedback, juice, cycle time, retention, design
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/genre-mechanics.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/case-studies-pet-simulator-99.md
related: idea-validator, first-minute-designer, progression-curve-designer, reward-schedule-designer, game-feel-polisher, scope-cutter, feature-prioritizer, rbx-rounds
---

# core-loop-designer

Everything else hangs from this. The vault's first rule: define one core loop and make it fun before anything else; every new system must feed it or be cut.

## When to use
After `idea-validator` says GO, or when a game feels like a pile of features. Not for: round/intermission structure of a match game (`rbx-rounds` covers state flow; use this first for the player-facing loop).

## Inputs (max 3)
1. The premise (default: `docs/idea.md`). 2. Reference game(s) (default: from the validator). 3. Session target (default: 10-15 minute sessions, mobile-first).

## Procedure
1. Name the verb. The most repeated action in the fantasy ("hatch", "mine", "dodge", "build"). One verb, one sentence: "I <verb> to get <reward> so I can <upgrade> and <verb> better/faster".
2. Layer 1, minute-to-minute (seconds per cycle): the interaction, the instant feedback (sound, number pop-up, particles, camera/tween ~0.1-0.3 s), the reward unit. Target: understood in about 30 seconds with no text. Write the cycle time and the feedback beats (`game-feel-polisher` expands them).
3. Layer 2, session: what the player does over 5-15 minutes: gather -> spend -> unlock -> new area/target. Name the 2-3 decisions the player makes (what to buy, where to go, when to cash in).
4. Layer 3, progression engine: what makes the next session different (levels, zones, rebirth, collection). Use short, mid and long-term goals; early levels take about a minute; show the long-term goal early (`progression-curve-designer`).
5. Reward schedule: fixed small rewards every cycle, variable bigger ones every few cycles, milestone rewards per session; no paid randomness; free players reach all core content.
6. Feature filter: list candidate features; for each write "feeds layer N by ..."; no answer = cut or defer. Flag parallel loops ("tumors"): a second loop that competes for time splits the player base and creates update debt.
7. Co-play hook: one reason a friend makes it better (shared goals, trading, co-op bonus). Official guidance: a session with a friend is the top return predictor.
8. Prototype test in three lines: what a bot or a player does for 2 minutes, what must be on screen, and the pass condition ("a new player gets reward #1 within 20 s and reward #3 within 60 s"). Hand to `playtest-bot-writer` or build it in the MVP.
9. Write `design/core-loop.md` and append the cut list to `decisions.md`.

## Studio MCP path
Design only. When a prototype exists: `start_stop_play`, drive the loop with `character_navigation` / `user_keyboard_input` / `execute_luau` (Server), `screen_capture` at the first reward, `get_console_output`; the evidence is "cycle time measured: N s".

## Fallback
Pure document; mark the cycle times `estimated` until measured.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (one loop; three parts; instant feedback and juice; layered goals; front-load progression; avoid tumors), `Roblox/roblox-kb/player-psychology-and-game-feel.md`, `Roblox/roblox-kb/retention-d1-d7.md` (friends, return hooks), `Roblox/roblox-kb/case-studies-pet-simulator-99.md` (a collect-and-upgrade loop in practice; read for pattern only).

## Output
`design/core-loop.md`: verb sentence; three layers with cycle times; feedback beats; reward schedule table; feature filter table (feature, feeds layer, keep/cut); co-play hook; 2-minute prototype test with pass condition.

## Acceptance checks
- [ ] One loop, stated in a single sentence a stranger can repeat.
- [ ] All three layers present with a number (seconds/minutes) each.
- [ ] Every feature in the plan has a "feeds the loop" line or is cut.
- [ ] No paid-randomness or paywall on core progress in the reward schedule.
- [ ] The prototype pass condition is measurable.

## Pitfalls
Two loops at once. A loop that needs a tutorial. Rewards that are numbers in a menu instead of felt feedback. Putting the best content behind the grind wall with nothing to see until later. Designing the economy before the verb is fun.

## Related
`idea-validator`, `first-minute-designer`, `progression-curve-designer`, `reward-schedule-designer`, `scope-cutter`, `game-feel-polisher`.
