---
id: "rbx-ideas"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-ideas/SKILL.md"
description: "Generates, scores and plans Roblox game concepts for a solo or small team ('what should I build next'): patterns from rbx-trends, 8 candidates on a fixed rubric, top three, the chosen one expanded into a build plan (systems, milestones with acceptance tests, first three tasks)."
orig_name: "rbx-ideas"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-ideas

> Generates, scores and plans Roblox game concepts for a solo or small team ('what should I build next'): patterns from rbx-trends, 8 candidates on a fixed rubric, top three, the chosen one expanded into a build plan (systems, milestones with acceptance tests, first three tasks).

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-ideas/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--rbx-designer]], [[A--own--rbx-money]], [[S--own--rbx-metrics]], [[S--own--rbx-trends]]

---
# Roblox game ideas

Two phases: **A. Ideas** (score, pick the top three) and **B. Plan** (when the user picks one, or gives a single concrete seed and asks for a plan). No idea is guaranteed to succeed. Say what is likely, why, and what result would show otherwise.

## Hard rules

- Patterns, not content: never suggest copying a specific game's art, names, maps, code or unique story.
- All ages, within Roblox community standards. No real-money gambling, no paid random rewards (Robux into loot boxes, eggs or spins), no countdown or fear-of-missing-out pressure, no pay-to-win, and no stranger contact without safeguards (for example, friends-only parties, opt-in trading, and only Roblox's built-in filtered chat).
- Do not invent numbers, dates, URLs or repository names. Use evidence only from the KB output ([K#]) or the trend report ([S#]); anything else is marked UNVERIFIED. For a full GDD after the pick, hand off to the rbx-designer agent or skill rbx-gdd; for pricing, rbx-money.
- Libraries and tools are named as options, never installed. Do not run install, download, clone or execute commands.

## Defaults (assume these, state them in one line, and do not block on questions)

Solo developer, comfortable with Luau and basic building, Mac with Studio (Rojo optional) · first playable in 2 to 4 weeks · free CC0 assets only · all ages · game passes and cosmetics only. Ask a question only if the seed breaks a hard rule or is too vague to produce 8 distinct candidates.

## Phase A: Ideas

1. **Seed.** Keep the user's idea as the seed and do not ask them to restate it. With no seed, vary the genres.
2. **Evidence, KB first, web second.** First query the local Roblox knowledge base (about 5 calls; it is sourced, dated and flagged official/indie):
   ```
   K="python ~/claude-library/tools/roblox-kb/kbq.py"
   $K route "game idea <seed or genre> core loop demand"
   $K section game-ideas-and-genres instructions
   $K section trend-research-and-validation instructions
   $K find "<seed/genre> saturation demand validate" -t game-ideas-and-genres,trend-research-and-validation -n 8
   $K case "<genre>" -n 3
   $K find "mistakes <genre> scope" -t common-mistakes -n 5
   ```
   Tag KB evidence `[K#]` with its link, flag and date (official Creator Docs/staff override indie advice; indie CCU/revenue figures are never evidence of demand, only of what creators claim). Then reuse a report saved in this project (`research/roblox-trends-*.md`) if it is 14 days old or less and covers the seed's genre; run rbx-trends (Focused or Broad, which also reads the KB first) only for live facts the KB cannot hold (current charts, CCU, what rose in the last 90 days). If the KB and the web both fail, continue, write `Trend data: unavailable (<reason>)`, and mark Discoverability and Originality scores as low confidence.
3. **Candidates.** Write 8 one-liners: "<who> does <what> to <goal>, with <twist>". Tag each with the pattern IDs it uses (P#). With a seed, give 8 variations of it (different loops, twists or scopes). Include at least 2 that a solo developer could finish in half the agreed time.
4. **Score** each candidate with the rubric below. Decide every score against the anchors, with a reason of 3 to 6 words. Keep the reasons out of the reply except for scores of 1 or 2, and show all of them if the user asks. **Drop rule:** drop any candidate that scores 1 on Scope, First 30 seconds or Monetisation fit, or that breaks a hard rule. Ties go to the higher Scope score, then First 30 seconds.
5. **Self-check**, then reply with the Phase A template.

### Scoring rubric (integers; 2 and 4 sit between the anchors)

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| First 30 seconds | Needs a tutorial or reading before anything fun happens | Core action understood within a minute, with some text | Fun action within 10 s, taught by doing; no text needed |
| Core loop | No clear repeatable action-reward cycle | A loop exists, but the cycle is long (over 5 min) or the reward is weak | Action, reward and upgrade cycle under 2 min, and it still pulls on day 2 |
| Retention hook | Nothing to return for | One hook (for example, progression only) | Two or more that reinforce each other (progression and collection, or social and daily) |
| Shareability | Nothing visible or funny to show | Occasional striking moments | Moments players want to clip, plus a look that sells the thumbnail |
| Scope | Needs a team, heavy custom art or complex netcode; over 3x the agreed time | Fits the time but relies on 1 or 2 risky bespoke systems | MVP in half the time or less, using the approved options and CC0 assets |
| Monetisation fit | Only earns through pay-to-win, paid randomness or pressure | Passes or cosmetics possible but feel bolted on | Cosmetics or convenience that others see, while free players get the full game |
| Discoverability | No clear hook; hard to title or search | Clear genre but a generic title or thumbnail | One searchable hook word and an obvious thumbnail image |
| Originality | Reskin of a known formula | Known formula plus one meaningful twist | A fresh verb or combination not seen among the researched leaders, still clear in 30 s |

### Phase A template

```
Pick: <Title>. <why, one line>. Score <x>/40.
Assumed: <defaults line> · Trend data: <report date | unavailable>

1. <Title> (<x>/40): <pitch>
   Loop: <act> -> <reward> -> <upgrade>
   First 30 s: <what the player does>
   Hook: <retention> · Money: <passes/cosmetics/none>
   MVP: <in> | Cut: <out>
   Risk: <main risk>. Test: <cheap early test> (target from the KB benchmarks with flag, e.g. D1)
   Weakest: <criterion> <n>, <criterion> <n> · Patterns: P#, P#
2. ...
3. ...

Scores: | # | Idea | F30 | Loop | Ret | Share | Scope | Money | Disc | Orig | Total |
Dropped: <idea>: <rule triggered>
Reply with 1, 2 or 3 for the full plan.
```

## Phase B: Plan

If the user went straight to a plan from a seed, score the seed alone first. If it triggers the drop rule, say which criterion failed and suggest the closest candidate that passes before you write the plan. Keep each section short and mark items `DECIDE:` (the user must choose) or `UNVERIFIED:` (no source).

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
| Tooling and testing | Rojo, Rokit, luau-lsp, StyLua, Jest Lua (runs inside Roblox only, so it needs Studio), Roblox Studio MCP (needs Roman's approval) |

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

1. "Give me a Roblox game idea." No seed: defaults assumed and Broad research reused or run; 8 candidates across 5+ genres; the reply opens `Pick: <Title>`, followed by 3 cards, the score table and 1 or 2 dropped ideas (for example, "Scope 1: needs custom vehicle physics").
2. "Something about cooking with friends." The seed is kept and Focused research run on cooking and co-op; the 8 candidates are variations (a timed co-op kitchen, a cooking tycoon, a delivery obby...); social features use friends-only parties, so there is no stranger contact.
3. "Plan #2." Phase B: the This week block comes first (for example, "Greybox the kitchen with Kenney kit pieces. Done when: a player can walk from the counter to the stove in under 5 s"). The Systems table shows Player data = ProfileStore (option), Order queue = Build, and UI = DECIDE.

## Self-check before replying

- [ ] The first phone screen shows the pick (Phase A) or This week (Phase B).
- [ ] Every candidate has 8 scores checked against the rubric anchors; the drop rule has been applied, and dropped ideas are listed with the rule they triggered.
- [ ] Each evidence claim points to a P# or [S#] from the trend report, or is marked UNVERIFIED; no invented numbers or benchmarks.
- [ ] Nothing copies a specific game's art, names, maps, code or story.
- [ ] All-ages checks pass: no paid randomness, pressure, pay-to-win or unsafeguarded stranger contact.
- [ ] Every library named is on the approved-options list and described as an option, not an install; no archived libraries.
- [ ] Every milestone has a pass/fail acceptance test; the plan has exactly 3 tasks for this week.
- [ ] No promise of success; each risk has a check that could prove it wrong.


## Triggers (moved out of the description)

Use proactively, without being asked for a skill by name, whenever the user wants to make a Roblox game, asks for a Roblox game idea or concept, wants a rough idea turned into a plan, asks which idea to build, or asks what kind of game would do well on Roblox.
