---
name: rbx-ideas
description: "Claude invents a fresh Roblox game idea ('what should I build', 'give me a game idea', 'surprise me'): shows the 3 best of many sparks as short pitches, you pick one, then a short dot-point card (hook, retention, week 1, money, build ease, critic rating). Then 'build it', 'another' or 'plan'. Own idea: rbx-idea-creator; quick: rbx-idea-quick."
argument-hint: "[genre or theme, optional]"
---

# Roblox game ideas

Many sparks, THREE short pitches, then ONE game, deep, as a short card. Claude invents the sparks from player moments ("what should I build"), you pick; if the user brings their own idea or wants to be guided to one, that is `rbx-idea-creator`, which uses the Engine below. Phase A = the pitches, then the card for the pick; Phase B = the plan (only on "plan"). No idea is guaranteed to succeed. Say what is likely, why, and what result would show otherwise.

## Hard rules

- Patterns, not content: never suggest copying a specific game's art, names, maps, code or unique story.
- All ages, within Roblox community standards. No real-money gambling, no paid random rewards (Robux into loot boxes, eggs or spins), no countdown or fear-of-missing-out pressure, no pay-to-win, and no stranger contact without safeguards (for example, friends-only parties, opt-in trading, and only Roblox's built-in filtered chat).
- Do not invent numbers, dates, URLs or repository names. Use evidence only from the KB output or the trend report ([S#]); anything else is marked UNVERIFIED. For a full GDD after the pick, hand off to the rbx-designer agent or skill rbx-gdd; for pricing, rbx-money.
- Libraries and tools are named as options, never installed. Do not run install, download, clone or execute commands.
- Chart data shows what is already taken, not what to build: never copy the formula of a chart leader as the idea, and never start generating from it.

## Defaults (assume these, state them in one line, and do not block on questions)

Solo developer, comfortable with Luau and basic building, Mac with Studio (Rojo optional) · first playable in 2 to 4 weeks · free CC0 assets only · all ages · game passes and cosmetics only. Ask a question only if the seed breaks a hard rule.

## Engine (shared pipeline: rbx-ideas and rbx-idea-creator both run exactly this)

Input: a seed (the user's idea, a genre, the creator funnel's answers) or nothing. Output: first the 3 short pitches (turn 1), then, after the pick, the card plus the full detail saved to a file (turn 2).

1. **Seed.** Keep the user's idea as the core and do not ask them to restate it. Funnel answers count as constraints (category, fantasy, co-op or solo, session length, audience age, art and scope, money comfort). No seed: choose freely; do not look at charts yet.
2. **Sparks (silent, BEFORE any trend or KB reading, do not print).** Start from a player MOMENT, not from a genre, a chart or a pattern: the specific thing a kid does, feels or tells a friend afterwards ("I got my whole team to hold perfectly still while the thing behind them woke up"). Give each spark ONE concrete, surprising constraint or twist that changes how that moment plays (an odd rule, an unusual tool, a role swap, a limit on what you can see, say or carry). Write about 12 sparks, one line each: `moment + constraint -> the verb the player does in the first 10 seconds`. With a seed (the user's idea or the funnel answers) every spark keeps the user's core fantasy and verb and varies the rest (a different twist, social shape, setting or constraint); without a seed spread them over at least 5 different verbs, 5 different settings and 3 social shapes (solo, duo, friend group of 3 to 6, one-vs-many, asymmetric roles, spectators).
   **Tests, every spark must pass all four:** (a) tell-a-friend: one plain sentence a 12-year-old repeats; (b) clip: a moment a kid would record and post; (c) verb: the main verb is not what players do in the top 20 games (running, collecting, hatching, buying upgrades, surviving a timer, rebirthing); (d) scope: a solo dev builds the first playable in 4 weeks or less, no custom netcode. Kill any spark that fails, then kill the generic survivors: if you can name the game it is "X but with a theme", cut it.
   **Banned unless the pitch earns the word (state the reason in the saved file):** cozy, simulator, tycoon, "obby" plus a noun, idle or clicker, "Escape the X", "Survive X", "Find the Y", "co-op X with friends" as the whole idea, rising tide, lava or water as the pressure, a single rope, bridge, tower or sandcastle gimmick, hatching, eggs, pets plus a coin loop, brainrot, "Grow a" and "Steal a" shapes, and one-word atmospheric titles ("Echo", "Hollow", "Tide"). A colour, mood or setting is not a twist; a changed rule or verb is.
3. **Sanity check with evidence, KB first, web second (top sparks only).** Take the 5 best surviving sparks. Run ONE single-line Bash command (hooks may block multi-line blocks):
   `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/kbq.py" pack ideas "<seed, or the genre words of the top sparks>"`
   It prints a `[K#]` pack. If its first line is not `KB OK` (or it fails), your reply's Notes line says `KB unavailable: <reason>. Fix: <its Fix line>` (see the card); never fall back silently. `pack` has no length option; if a pack section ends `(truncated; raise --max-chars)` and you need the rest, read that section once with `kbq.py section <topic> instructions --max-chars 3000`.
   Use the evidence ONLY to (1) drop a spark that is already taken by a chart leader or is a known saturated formula, (2) set the benchmarks and the money bands, (3) back the claims the card makes. It must not supply new ideas and must not pull a winner back toward the charts. The chart-clone rule stays: chart data shows what is already taken, never the formula to copy.
   **Citing (strict).** Cite a fact only as the tag its source line printed: `[K#]` where the pack printed one, otherwise `[<topic>, <flag>, <date>]` copied from the `kbq.py num` or `section` line (for example `[retention-d1-d7, official]`). Never mint a tag or number; every bracket in the card must match text in the tool output you actually saw. A claim with no printed source is `UNVERIFIED`. Official Creator Docs and staff override indie advice; indie CCU/revenue figures are never evidence of demand, only of what creators claim.
   For retention, first-session and pricing facts also run (single-line commands, same `kbq.py`) `num "D1 retention benchmark"` and `section monetisation-gamepasses rules` when the pack lacks them. Benchmarks are indie self-reported unless flagged official; say so.
   **Trend data.** Reuse a report saved in this project (`research/roblox-trends-*.md`) if it is 14 days old or less, covers the seed's genre and has a Leaders table; otherwise run rbx-trends (Focused) with a hard cap of 4 searches or fetches, used to check whether the top sparks are already taken. Trend data is **partial** when there is no Leaders table of 14 days or less for the genre, and **unavailable** when the KB and the web both fail. Then the Notes line carries `Trend data: partial/unavailable - demand and originality claims low confidence`, novelty is capped at 6, and no 8 or more for demand or money.
4. **Shortlist: TOP 3 as short pitches, then STOP.** Pick the 3 strongest survivors that differ from each other in verb AND setting. Print only this (no card, no scores, no sparks list) and wait for the user:
   ```
   TL;DR: 3 ideas - pick 1, 2 or 3, or say "surprise me" (an independent critic picks)
   (Notes line only if needed: KB unavailable / Trend data partial / No independent critic)
   1. **<Title>** (<category>) - <hook moment in one line: what the player does and what happens>
      Fresh because: <one line: the verb or rule nobody else has>
   2. ...
   3. ...
   Done — <what was prepared, one line>
   You — pick 1, 2 or 3, or say "surprise me"
   Next — I build the full card for your pick
   ```
   Pitches are 2 lines each, plain words, no jargon. Save the sparks and the shortlist to `research/ideas-shortlist-<slug of pitch 1>.md` (one line per spark with the kill reason; the 3 pitches) so "another" and the pick turn can reuse them. If the user already said "just do it" or "no choice, one idea", develop the strongest spark directly (step 5) and name the 2 other pitches in one line.
   **On the pick** (a number, a title, or "surprise me"): for "surprise me" call the critic (step 7) once on the three pitches asking for the pick and a NOVELTY score (1 to 10) for each, then use its pick (no agents: pick by your harshest self-review and say so); otherwise take the user's. Do not re-ask. Continue with step 5 in the same reply.
5. **Develop the pick (deep).** Not-a-clone line (required): `Keeps: <the nearest known formula, named> | New: <fresh verb or rule>`. Never develop an idea whose own risk says "saturated" or "low originality" without first trying the next pitch. Bars:
   - **Hook:** one sentence a 12-year-old repeats, clear from the title and thumbnail, with a moment worth clipping. Name the clip moment.
   - **First 30 seconds:** the player acts in under 10 seconds with no reading; first reward within about 15 seconds; a guaranteed first win; teaching by doing, icons over text.
   - **Core loop:** act, reward, upgrade in about 2 minutes or less, and it still pulls on day 2.
   - **D1 return reason:** a specific unfinished thing in THIS game (a named goal in sight, a collection gap, a build to finish, a friend waiting), never "a daily reward" alone. Daily rewards only ethically: no loss framing, no penalty for missing a day, never the sole reason to return.
   - **Week 1 (D1 to D7):** one short line per day, and every line must name something that exists only in this game (a rule that changes, a place, a role, a creature, an event, a tool) and could not be pasted into another game's card. Banned as week-1 lines: "daily reward", "leaderboard", "friends board", "album" or "collection of N" without a game-specific item, "teaser for the next zone", "new area unlocked", "bigger version of the same". Something real must change by D3; D5 or D6 adds a social beat that fits the game's social shape; D7 has a long goal. State how many pieces of content or sessions week 1 needs and whether a solo dev can make that.
   - **Money:** game pass, cosmetic and convenience ideas that fit THIS game (what players would proudly show, or what saves a real chore), with prices in Robux (cosmetic or convenience in the 59 to 99 band unless the KB says otherwise) and when each first appears in week 1 (never in the first minutes; after the first win). What free players get: the full loop and every goal. No paid randomness, no pressure, nothing that blocks core progress. Do not reuse the same three items (decor pack, emote pack, extra slot) from game to game.
   - **Build ease (solo) 1 to 10, with a time estimate in weeks:** 9 to 10 = one place, no custom netcode, CC0 assets, about 2 weeks; 7 to 8 = one risky system, 2 to 4 weeks; 4 to 6 = several bespoke systems or multiplayer sync; 1 to 3 = needs a team, custom physics or heavy art. One-line reason and a one-line first build (what to build first, what to cut).
   - **Category:** the genre label the player would search for.
6. **Red-team.** List the 3 worst weaknesses (honest: clone risk, thin D3, weak money fit, too much scope, nothing to clip, reads like a known game with a skin, ...). Fix each in the design and mark it fixed or unfixed. Re-score every area from scratch against the new design (never write "unchanged"), and subtract 1 from the related area for each unfixed weakness. The before and after scores appear only in the saved file. An unfixed weakness that matters most stays as the Biggest risk.
7. **Critic (wait for it; print nothing while it runs).** Write the draft (pitch, category, loop, hook and first 30 s, D1, week 1, money, build ease, risks, the Keeps/New line) to `research/idea-<slug>.md` ONCE, before the critic; update that file once after the critic. With the Agent tool available, call it with `subagent_type: rbx-judge` and a prompt that says: idea-stage review of this file; no game folder exists, so do NOT run verdict.py or write any file; judge only the written idea against `kbq.py` evidence; score 1 to 10 each: hook, D1 return, week-1 retention, monetisation, NOVELTY, build ease, and an overall; NOVELTY = would a 12-year-old tell a friend, and is the verb or rule one they have not seen; be harsh on generic: a "cozy / simulator / tycoon / obby / survive / escape" shape with a theme on top, filler week-1 lines and stock monetisation each cost novelty, and 6 or less means slop; 8 or more and 3 or less need a cited fact; spread the scores, do not cluster at 5 to 7; name the weakest area and one cheapest fix; reply in at most 10 lines. Pass NO opinion of how good it is. The `rbx-critic` skill is the alternative route. Send NO interim message while it runs (no "running the critic", no "waiting", no partial card, no Done/You/Next footer): your next visible text is the final card. When it returns, fold the critic's fix in once and use the critic's scores in the card (say so if you changed the design; never edit its numbers).
   **Slop gate:** critic NOVELTY below 6 (or overall below 5): discard this pick, develop the next pitch from the shortlist (or write one new spark if none is left) and run steps 5 to 7 once more, silently. If that one also scores NOVELTY below 6, show the better of the two and add the plain line "Weak on novelty: <why>".
   **No agents available** (you are a subagent, or low-usage mode): do a separate adversarial pass in which you try to reject the idea, and for EACH of the six scores (novelty included) write why it is lower than or equal to your design score; the same slop gate applies to your novelty score; the Notes line says `No independent critic - self-review only` and the critic field reads `self-review x/10`. Never present your own score as an independent critic's.
8. **Scores are honest.** A mid idea is a 5 to 6. 8 or more or 3 or less needs a cited fact. The overall is the critic's overall, not an average of flattering numbers. An idea below 5 overall after the red-team is replaced once by the next pitch; if that fails too, show the best one and say plainly that it is weak.
9. **Save, then show the card.** Save the full detail to `research/idea-<slug>.md` (slug = kebab-case title) in the game's project folder; when there is none (for example a session in the vault folder), use `./research/` under the current folder (create it) and say so in one clause. In chat show ONLY the card and the short relative path.

### Saved file format (what the builder and `games.py init --from-idea` read)

```
---
title: <Title>
slug: <kebab-case-slug>
pitch: <one line>
category: <genre label>
---
## Core loop          (act -> reward -> upgrade, with cycle time)
## Hook and first 30 seconds
## Week 1             (D1 .. D7, one line each; content or sessions needed)
## Money              (passes, cosmetics, convenience, prices, when; free-player experience)
## Scores             (critic overall, six areas incl. novelty with one-line reasons incl. what lifts D1 and week 1, build ease with weeks)
## Risks              (3 red-team weaknesses fixed/unfixed, scores before -> after, biggest risk, cheapest test measuring 2 numbers, D1/D7 target)
## Target player
## Evidence           (tags exactly as printed by the tools, with link, flag, date)
## Sparks killed     (one line each with the reason; also the 3 pitches, and why each banned word used was earned)
## Funnel answers     (creator only: each round, answer or "skipped -> default applied")
```

### The card (chat output; cap 40 lines; dot points, no tables, bullets of about 12 words at most, no "a / b" joined bullets, plain words)

```
TL;DR: build / skip - <one short reason>            <- ALWAYS the first line
Notes: <only when needed, one line each: "No independent critic - self-review only" | "KB unavailable: ..." | "Trend data: partial/unavailable - ..." | creator: "Building your idea from: <answers>" | "Weak on novelty: ...">
**<Title>** - <one-line pitch>
- Category: <genre> · Critic: <x>/10 (<independent | self-review>) - <reason> · Novelty: <n>/10
- Why picked: <bullet> · <bullet>
- Not a clone: Keeps <x> | New <y>

Hook and first 30 seconds
- <2 to 3 bullets; one of them is the clip moment>
- Loop: <act> -> <reward> -> <upgrade> (about <n> min)

Why they come back
- Tomorrow: <bullet> · <bullet>
- D1 <line>
- D2 ... D7 <line>   (one bullet per day, each naming something only this game has)

Money (all ages, no paid randomness or pressure)
- <pass / cosmetic / convenience> - <price> Robux - appears <when>
- Free players: <what they get>

Build ease: <x>/10 for a solo dev, about <n> weeks - <reason>. First build: <one line>
Scores: hook <n> · D1 <n> · week 1 <n> · money <n> · novelty <n> · build ease <n>

Why it can work
- <evidence bullet with exact tag> (2 bullets)
Reasons not to build this: <one line, the owner decides>
Biggest risk: <risk>. Cheapest test: <test measuring 2 numbers>; target D1 <x>%, D7 <y>% (<KB tag>, indie or official)

Detail: research/idea-<slug>.md
Done — <what happened, one line>
You — reply "build it" (create the game folder + README), "another" (a different idea), or "plan" (full plan)
Next — <what happens on your reply>
```

Output rules (these were real bugs): the TL;DR is the very first line of the reply, nothing above it; any Notes or "Trend data" line sits directly under it; print exactly ONE Done/You/Next footer, as the last three lines, and no other "Reply ..." closing line; no progress message or footer is printed before the final card (not while the critic runs, not after the shortlist step except the shortlist's own single footer); the shortlist reply and the card reply each end with exactly one footer.

Spell Robux in full where first used and avoid jargon (say "first build" not MVP, "players online" not CCU, or define it in two words). Assumed defaults go in one short line under the title only if they changed something. Do not print the Engine steps, sparks, candidate lists, red-team notes or the evidence table in chat: they live in the file.

### After the card

- **"build it":** run (single line) `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/games.py" init <slug> --from-idea research/idea-<slug>.md`. It creates `Games/<slug>/` and seeds README.md (pitch, loop, hook, week-1 loop, monetisation, scores, risks). Then give the folder path and offer `/rbx-workflow` to continue. Nothing else is built.
- **"another":** the 2 pitches not picked are still on the shortlist file: offer them first in one line ("or take pitch 2 / 3"); if the user wants new ones, run the Engine again from step 2 with fresh sparks (different verbs and settings, the rejected ones named; reuse the KB pack and the trend report) and show 3 new pitches.
- **"plan":** Phase B below, on the idea in the file. Phase B is unchanged.

## Phase B: Plan

If the user asks for a plan with no card yet, run the Engine on that seed first (pitches, the pick, card, critic) and plan the result; if the critic overall is below 5, say which area failed and offer the closest stronger variation before you write the plan. With a card, plan that idea from `research/idea-<slug>.md`. Keep each section short and mark items `DECIDE:` (the user must choose) or `UNVERIFIED:` (no source).

**Approved-options list.** Name a library only if it appears here, and only as an option. If nothing fits, the decision is "Build (bespoke module)". Never recommend Knit, Matter, Roact, TestEZ or Remodel (all archived).

| Area | Options |
|---|---|
| Characters and movement | Roblox Character Controller Library (official) |
| Player data | ProfileStore |
| Utilities | Sleitnick RbxUtil (Signal, Trove, Component) |
| Networking | Zap |
| Pathfinding | ParallelPath (new and little used, so review it first), fallback SimplePath |
| Zones and areas | ZonePlus |
| UI | Native Roblox UI, or `DECIDE:` React Luau, Vide or Fusion (one per project; not yet chosen) |
| Assets (CC0) | Kenney, Quaternius, Poly Haven, ambientCG |
| Tooling and testing | Rojo, Rokit, luau-lsp, StyLua, Jest Lua (runs inside Roblox only, so it needs Studio), Roblox Studio MCP (needs the user's approval) |

No maintained library was found for combat, inventory or state machines, so build those as bespoke modules. None of these tools is approved for install yet.

### Phase B template

```
# <Title>: plan (<YYYY-MM-DD>)
Promise: <one sentence a player would repeat>
Genre · Target player · Session length

## This week
1. <task, under 1 day>. Done when: <observable result>
2. ...
3. ...

## Core loop and session
<step -> step -> step, with rough timings; what ends a session>

## First session (exact flow)
0-10 s: ... · 10-30 s: ... · 1-5 min: ... · End: <reason to return>

## Systems
| System | Build or library | Option | Why |

## MVP content
| Item | Count | Source (CC0 pack or self-made) | Licence |

## Retention
Day 1: ... · Day 7: ... · Day 30: ...

## Monetisation
Sold: ... · Shown where: ... · Always free: ...

## Milestones
| # | Milestone | Est. days | Acceptance test (pass/fail) |
| M1 | Greybox loop | <n> | A new tester finishes 3 loops in 5 min without help; no errors in the output |
| ... | | | |
| M<last> | Private test build | <n> | Published privately; testers have played; analytics are recording |

## Test plan
Private publish, with friends or invited testers only. Watch 2 numbers in Creator Hub analytics: day-1 retention and average session length (check the current metric names there). Targets: from `kbq.py num "D1 retention benchmark"` / skill rbx-metrics (flagged indie vs official; compare with Creator Hub Similar Experience Benchmarks), otherwise beat the previous test build. Each number has a "this would prove us wrong" line.

## Risks and cuts
Risks: 1 ... 2 ... 3 ... (each with an early check)
Cut first: ... then ...
```

Milestones: 4 to 6, sized to the stated time. Every acceptance test must be something a person can observe or measure in Studio or in a playtest; "works well" is not a test.

## Worked examples (shape only, no real metrics)

1. "What should I build?" No seed: about 12 sparks written silently from player moments, stock-trope and generic ones killed, the KB and trends used only to check the survivors; turn 1 shows 3 two-line pitches and a footer; the user answers "2" (or "surprise me"); turn 2 develops that pick, rbx-judge scores it (novelty included) while nothing is printed, and the reply is the card ending in one Done/You/Next footer, with the detail in `research/idea-<slug>.md`.
2. "Something about cooking with friends." The seed is kept as the core and developed into one card (social features friends-only, so no stranger contact). The dedicated route for a user's own idea is rbx-idea-creator.
3. "Plan" after a card: Phase B. The This week block comes first (for example, "Greybox the kitchen with Kenney kit pieces. Done when: a player can walk from the counter to the stove in under 5 s"). The Systems table shows Player data = ProfileStore (option), Order queue = Build, and UI = DECIDE.

## Self-check before replying

- [ ] Turn 1 is the TL;DR line plus 3 two-line pitches plus ONE footer, nothing else. Turn 2 is the card only: cap 40 lines, TL;DR as the very first line (Notes lines under it), exactly one Done/You/Next footer at the end, no interim progress message was printed, dot points, no tables, no candidate list, bullets about 12 words at most; the detail is in `research/idea-<slug>.md` and only the short relative path is shown.
- [ ] Sparks came from a player moment plus one surprising constraint BEFORE any chart or KB reading; about 12 were written; every shortlisted pitch passed tell-a-friend, clip, verb-not-in-the-top-20 and solo-scope; no banned trope word survived without a stated reason; the 3 pitches differ in verb and setting. ONE idea in the card, with the `Keeps | New` line naming the nearest formula.
- [ ] Present: hook, first 30 seconds, loop, tomorrow reasons, D1 to D7 lines, money with Robux prices and timing, free-player experience, build ease with weeks and first build, category, six area scores, reasons not to build, risk with cheapest test and D1/D7 target.
- [ ] Week-1 lines and money items are specific to this game (none could be pasted into another card; no daily reward, leaderboard, album or teaser filler). Critic scored NOVELTY; novelty below 6 was sent back once. Critic: an rbx-judge Agent call, or the Notes line says `No independent critic - self-review only`; the 3-weakness red-team was done with the unfixed-minus-1 rule; scores are spread; every 8 or more or 3 or less cites a printed source.
- [ ] Every bracket tag in the card matches text in the kbq output or the trend report; no minted [K#]; unsupported claims are UNVERIFIED; benchmarks are flagged indie or official; partial trend data is stated and capped.
- [ ] Nothing copies a specific game's art, names, maps, code or story; all-ages checks pass (no paid randomness, pressure, pay-to-win, unsafeguarded stranger contact; daily rewards only as an ethical extra).
- [ ] The footer's You line offers build it, another, plan. For a plan: every library is on the approved-options list as an option, no archived libraries, every milestone has a pass/fail acceptance test, exactly 3 tasks for this week, no promise of success, each risk has a check that could prove it wrong.
