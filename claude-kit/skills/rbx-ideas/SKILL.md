---
name: rbx-ideas
description: "Generates, scores and plans Roblox game concepts for a solo or small team ('what should I build next'): patterns from rbx-trends, 8 candidates on a fixed rubric, top three, the chosen one expanded into a build plan (systems, milestones with acceptance tests, first three tasks)."
---

# Roblox game ideas

Two phases: **A. Ideas** (score, pick the top three) and **B. Plan** (when the user picks one, or gives a single concrete seed and asks for a plan). No idea is guaranteed to succeed: say what is likely, why, and what result would show otherwise.

## Hard rules
- Patterns, not content: never suggest copying a specific game's art, names, maps, code or unique story.
- All ages, within Roblox community standards. No real-money gambling, no paid random rewards (Robux into loot boxes, eggs or spins), no countdown or fear-of-missing-out pressure, no pay-to-win, no stranger contact without safeguards (friends-only parties, opt-in trading, only Roblox's built-in filtered chat).
- Do not invent numbers, dates, URLs or repository names. Evidence only from the KB output ([K#]) or the trend report ([S#]); anything else is marked UNVERIFIED. Full GDD after the pick: hand off to the rbx-designer agent or skill rbx-gdd; pricing: rbx-money.
- Libraries and tools are named as options, never installed. Do not run install, download, clone or execute commands.

## Defaults (assume, state in one line, do not block on questions)
Solo developer comfortable with Luau and basic building, Mac with Studio (Rojo optional) · first playable in 2 to 4 weeks · free CC0 assets only · all ages · game passes and cosmetics only. Ask only if the seed breaks a hard rule or is too vague to produce 8 distinct candidates.

## Phase A: Ideas
1. **Seed.** Keep the user's idea as the seed; do not ask them to restate it. No seed: vary the genres.
2. **Evidence, KB first, web second.** Run ONE single-line Bash command (hooks may block multi-line blocks):
   `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/kbq.py" pack ideas "<seed or genre>"`
   It prints a `[K#]` pack. If its first line is not `KB OK` (or it fails), your reply starts with `KB unavailable: <reason>. Fix: <its Fix line>`; never fall back silently.
   Tag KB evidence `[K#]` with link, flag and date (official Creator Docs/staff override indie advice; indie CCU/revenue figures are never evidence of demand, only of what creators claim). Then reuse a saved report (`research/roblox-trends-*.md`) if it is 14 days old or less and covers the seed's genre and has a Leaders table; otherwise run rbx-trends (Focused or Broad) now; ideas rest on its chart leaders. If KB and web both fail, continue, write `Trend data: unavailable (<reason>)`, and mark Discoverability and Originality as low confidence.
3. **Candidates.** 8 one-liners: "<who> does <what> to <goal>, with <twist>", each tagged with its chart anchor: 1 to 2 Leaders-table games it is formula-derived from (rank, CCU, date, [S#]/[K#]), the P# it keeps, and its twist; no such game: `no chart anchor`. Formula only, never content. With a seed: 8 variations (different loops, twists or scopes). At least 2 a solo developer could finish in half the agreed time.
4. **Score** each candidate with the rubric below. Decide every score against the anchors, with a reason of 3 to 6 words. Keep reasons out of the reply except for scores of 1 or 2; show all if asked. **Drop rule:** drop any candidate scoring 1 on Scope, First 30 seconds or Monetisation fit, or breaking a hard rule. Ties go to the higher Scope score, then First 30 seconds.
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
   Risk: <main risk>. Test: <cheap early test> (KB benchmark target, flagged)
   Weakest: <criterion> <n>, <criterion> <n>
   Anchor: <game #rank, CCU, date [S#]> keeps P# | twist <new> (or: no chart anchor)
2. ...
3. ...

Scores: | # | Idea | F30 | Loop | Ret | Share | Scope | Money | Disc | Orig | Total |
Dropped: <idea>: <rule triggered>
Reply with 1, 2 or 3 for the full plan.
```

## Phase B: Plan
A seed that went straight to a plan: score it alone first; if it triggers the drop rule, say which criterion failed and suggest the closest passing candidate before writing the plan. Keep sections short; mark items `DECIDE:` (user must choose) or `UNVERIFIED:` (no source).

**Approved-options list.** Name a library only if listed here, and only as an option. If nothing fits, the decision is "Build (bespoke module)". Never recommend Knit, Matter, Roact, TestEZ or Remodel (archived).

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

No maintained library was found for combat, inventory or state machines: build those as bespoke modules. None of these tools is approved for install yet.

### Phase B template
Sections in order: This week (exactly 3 tasks, each under 1 day with `Done when:`), Core loop and session, First session (exact flow), Systems, MVP content, Retention, Monetisation, Milestones (M1 Greybox loop ... last Private test build), Test plan (private publish; day-1 retention and session length; targets from `kbq.py num "D1 retention benchmark"` or skill rbx-metrics, else beat the previous build; a "this would prove us wrong" line each), Risks and cuts. [cold:rbx-ideas/plan-template.md] read before writing a Phase B plan, to copy the exact section layout and placeholder lines.

Milestones: 4 to 6, sized to the stated time. Every acceptance test must be observable or measurable in Studio or a playtest; "works well" is not a test.

## Worked examples (shape only, no real metrics)
[cold:rbx-ideas/worked-examples.md] read only to see the expected shape of a reply for a seedless request, a seeded request and a 'Plan #2' follow-up.

## Self-check before replying
- [ ] The first phone screen shows the pick (Phase A) or This week (Phase B).
- [ ] Every candidate has 8 scores checked against the anchors; the drop rule is applied and dropped ideas are listed with the rule they triggered.
- [ ] Every idea has an Anchor line or `no chart anchor`; each evidence claim points to a P#, [S#] or [K#] from the trend report, or is marked UNVERIFIED; no invented numbers or benchmarks.
- [ ] Hard rules hold: nothing copies a specific game's art, names, maps, code or story; no paid randomness, pressure, pay-to-win or unsafeguarded stranger contact; every library named is on the approved-options list as an option, not an install, and none is archived.
- [ ] Every milestone has a pass/fail acceptance test; the plan has exactly 3 tasks for this week.
- [ ] No promise of success; each risk has a check that could prove it wrong.
