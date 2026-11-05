---
name: rbx-ideas
description: "Claude finds the single best Roblox game idea for you ('what should I build', 'give me a game idea', 'pick one for me'): evidence from trends and the knowledge base, red-teamed and rated by an independent critic, shown as a short dot-point card (hook, retention, week 1, money, build ease). Then 'build it', 'another' or 'plan'. If you already have an idea, use rbx-idea-creator."
argument-hint: "[genre or theme, optional]"
---

# Roblox game ideas

ONE game, deep, as a short card. Claude picks it from evidence ("what should I build"); if the user brings their own idea or wants to be guided to one, that is `rbx-idea-creator`, which uses the Engine below. Phase A = the card, Phase B = the plan (only on "plan"). No idea is guaranteed to succeed. Say what is likely, why, and what result would show otherwise.

## Hard rules

- Patterns, not content: never suggest copying a specific game's art, names, maps, code or unique story.
- All ages, within Roblox community standards. No real-money gambling, no paid random rewards (Robux into loot boxes, eggs or spins), no countdown or fear-of-missing-out pressure, no pay-to-win, and no stranger contact without safeguards (for example, friends-only parties, opt-in trading, and only Roblox's built-in filtered chat).
- Do not invent numbers, dates, URLs or repository names. Use evidence only from the KB output ([K#]) or the trend report ([S#]); anything else is marked UNVERIFIED. For a full GDD after the pick, hand off to the rbx-designer agent or skill rbx-gdd; for pricing, rbx-money.
- Libraries and tools are named as options, never installed. Do not run install, download, clone or execute commands.
- Chart data shows what is already taken, not what to build: never copy the formula of a chart leader as the idea.

## Defaults (assume these, state them in one line, and do not block on questions)

Solo developer, comfortable with Luau and basic building, Mac with Studio (Rojo optional) · first playable in 2 to 4 weeks · free CC0 assets only · all ages · game passes and cosmetics only. Ask a question only if the seed breaks a hard rule.

## Engine (shared pipeline: rbx-ideas and rbx-idea-creator both run exactly this)

Input: a seed (the user's idea, a genre, the creator funnel's answers) or nothing. Output: the card, plus the full detail saved to a file.

1. **Seed.** Keep the user's idea as the core and do not ask them to restate it. Funnel answers count as constraints (category, fantasy, co-op or solo, session length, audience age, art and scope, money comfort). No seed: choose the category yourself from the evidence, preferring a niche that is not at the top of the charts.
2. **Evidence, KB first, web second.** Run ONE single-line Bash command (hooks may block multi-line blocks):
   `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/kbq.py" pack ideas "<seed or genre>"`
   It prints a `[K#]` pack. If its first line is not `KB OK` (or it fails), your reply starts with `KB unavailable: <reason>. Fix: <its Fix line>`; never fall back silently.
   Tag KB evidence `[K#]` with its link, flag and date (official Creator Docs/staff override indie advice; indie CCU/revenue figures are never evidence of demand, only of what creators claim). Then reuse a report saved in this project (`research/roblox-trends-*.md`) if it is 14 days old or less, covers the seed's genre and has a Leaders table; otherwise run rbx-trends (Focused or Broad, which also reads the KB first) now. Trend patterns are EVIDENCE of what players like, never a template. If the KB and the web both fail, continue, write `Trend data: unavailable (<reason>)`, and mark originality and demand claims as low confidence.
   For retention, first-session and pricing facts also run (single-line commands, same `kbq.py`) `num "D1 retention benchmark"` and `section monetisation-gamepasses rules` when the pack lacks them. Benchmarks are indie self-reported unless flagged official; say so.
3. **Candidates (silent, do not print).** Consider 5 to 6 candidates across at least 3 categories (or variations of the seed). For each: category, the hook as ONE sentence a 12-year-old could repeat, the verb the player does in the first 10 seconds, what it keeps from a known formula and what is new. Kill a candidate when: it is a chart clone (the "new" part is only a theme or skin), it needs more than one sentence, it is five features with no single hook, it needs a team or custom netcode, the only return reason is a daily reward, it breaks a hard rule. Keep a one-line reason for each kill for the saved file.
4. **Pick and develop ONE.** Not-a-chart-clone line (required): `Keeps: <formula element> | New: <fresh verb or combination>`. Then develop with these quality bars:
   - **Hook:** a unique verb or combination, clear from the title and thumbnail in one sentence, with a moment worth clipping.
   - **First 30 seconds:** the player acts in under 10 seconds with no reading; first reward within about 15 seconds; a guaranteed first win; teaching by doing, contextual hints, icons over text.
   - **Core loop:** act, reward, upgrade in about 2 minutes or less, and it still pulls on day 2.
   - **D1 return reason:** a specific unfinished thing (a goal in sight, a collection gap, a build to finish, a friend waiting), not "a daily reward" alone. Daily rewards are allowed only ethically: no loss framing, no penalty for missing a day, and never the sole reason to return.
   - **Week 1 (D1 to D7):** one short line per day. Something must change by D3 (new area, mechanic or social unlock), D5 or D6 adds a social or collection beat, D7 has a long goal and the next-week hook.
   - **Money:** game pass, cosmetic and convenience ideas with price points (cosmetic or convenience in the 59 to 99 Robux band unless the KB says otherwise) and when each first appears in week 1 (never in the first minutes; after the first win). What free players get: the full loop and every goal. No paid randomness, no pressure, nothing that blocks core progress.
   - **Build ease (solo) 1 to 10:** 9 to 10 = one place, no custom netcode, CC0 assets, about 2 weeks; 7 to 8 = one risky system, 2 to 4 weeks; 4 to 6 = several bespoke systems or multiplayer sync; 1 to 3 = needs a team, custom physics or heavy art. One-line reason and a one-line MVP (what to build first, what to cut).
   - **Category:** the genre label the player would search for.
5. **Red-team.** Write the 3 worst weaknesses (an honest list: clone risk, thin D3, weak money fit, too much scope, nothing to clip, ...). Fix each in the design, say what changed, then re-score. A weakness that cannot be fixed cheaply stays as the Biggest risk.
6. **Independent critic.** Write the draft (pitch, category, loop, hook and first 30 s, D1, week 1, money, build ease, risks, the Keeps/New line) to `research/idea-<slug>.md` first. Then call the Agent tool with `subagent_type: rbx-judge` and a prompt that says: idea-stage review of this file; no game folder exists, so do NOT run verdict.py or write any file; judge only the written idea against `kbq.py` evidence; score 1 to 10 each: hook, D1 return, week-1 retention, monetisation, originality, build ease, and an overall; 8 or more and 3 or less need a cited fact; spread the scores, do not cluster at 7 to 8; name the weakest area and one cheapest fix; reply in at most 10 lines. Pass NO opinion of how good it is. The `rbx-critic` skill is the alternative route. Fold the critic's fix in once, adjust the file, and use the critic's scores in the card (if you changed the design, say so; never edit its numbers). If you cannot spawn agents (you are a subagent, or low-usage mode), run the same rubric yourself and print `self-critique (not independent)` next to the score. Never skip this step and never present your own score as the critic's.
7. **Scores are honest.** A mid idea is a 5 to 6. 8 or more or 3 or less needs a cited fact ([K#]/[S#]). The overall is the critic's overall, not an average of flattering numbers. An idea below 5 overall after the red-team is replaced by the next-best candidate once; if that fails too, show the best one and say plainly that it is weak.
8. **Save, then show the card.** Save the full detail to `research/idea-<slug>.md` in the project folder (create `research/`; slug = kebab-case title) in the format below. In chat show ONLY the card and the file path.

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
## Week 1             (D1 .. D7, one line each)
## Money              (passes, cosmetics, convenience, prices, when; free-player experience)
## Scores             (critic overall, six areas with one-line reasons, build ease)
## Risks              (3 red-team weaknesses, fixes, biggest risk, cheapest test, D1/D7 target)
## Target player
## Evidence           ([K#]/[S#] with link, flag, date)
## Candidates killed  (one line each with the reason)
```

### The card (chat output; about 35 lines at most, dot points, no tables, no wall of text)

```
(KB unavailable line here ONLY if the KB failed)
**<Title>** - <one-line pitch>
- Category: <genre> · Critic: <x>/10 (<independent | self-critique>) - <one-line reason>
- Why picked: <bullet> / <bullet>
- Not a clone: Keeps <x> | New <y>

Hook and first 30 seconds
- <2 to 3 bullets>
Core loop: <act> -> <reward> -> <upgrade> (about <n> min)

Why they come back
- Tomorrow (D1): <bullet> / <bullet>
- Week 1: D1 <line>
- D2 <line> ... D7 <line>   (one short bullet per day)

Money (all ages, no paid randomness or pressure)
- <pass / cosmetic / convenience> - <price> R$ - appears <when>
- Free players: <what they get>

Build ease: <x>/10 (solo) - <reason>. MVP: <one line>
Scores: hook <n> · D1 <n> · week-1 <n> · money <n> · originality <n> · build ease <n>

Why it can work
- <evidence bullet> [K#] (2 to 3)
Risk: <biggest risk>. Cheapest test: <test>; target D1 <x>%, D7 <y>% (KB benchmark, indie/official flag)

Full detail: research/idea-<slug>.md
Reply "build it" to create the game folder + README, "another" for a different idea, or "plan" for the full plan.
```

Assumed defaults go in one short line under the title only if they changed something. Do not print the Engine steps, candidate lists, red-team notes or the evidence table in chat: they live in the file.

### After the card

- **"build it":** run (single line) `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/games.py" init <slug> --from-idea research/idea-<slug>.md`. It creates `Games/<slug>/` and seeds README.md (pitch, loop, hook, week-1 loop, monetisation, scores, risks). Then give the folder path and offer `/rbx-workflow` to continue. Nothing else is built.
- **"another":** run the Engine again for ONE different idea (different category, a new slug, the previous idea named as rejected; reuse the KB pack and the trend report). Never a list.
- **"plan":** Phase B below, on the idea in the file. Phase B is unchanged.

## Phase B: Plan

If the user asks for a plan with no card yet, run the Engine on that seed first (card, critic) and plan the result; if the critic overall is below 5, say which area failed and offer the closest stronger variation before you write the plan. With a card, plan that idea from `research/idea-<slug>.md`. Keep each section short and mark items `DECIDE:` (the user must choose) or `UNVERIFIED:` (no source).

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

1. "What should I build?" No seed: defaults assumed, KB pack and trend report read, 5 to 6 candidates weighed silently, clones killed, one picked and red-teamed, rbx-judge scores it; the reply is the short card and the closing line, with the detail in `research/idea-<slug>.md`.
2. "Something about cooking with friends." The seed is kept as the core and developed into one card (social features friends-only, so no stranger contact). The dedicated route for a user's own idea is rbx-idea-creator.
3. "Plan" after a card: Phase B. The This week block comes first (for example, "Greybox the kitchen with Kenney kit pieces. Done when: a player can walk from the counter to the stove in under 5 s"). The Systems table shows Player data = ProfileStore (option), Order queue = Build, and UI = DECIDE.

## Self-check before replying

- [ ] The reply is the card only: about 35 lines at most, dot points, no tables, no candidate list; the full detail is in `research/idea-<slug>.md` and only its path is shown.
- [ ] ONE idea, with the `Keeps | New` not-a-clone line; clones and five-feature ideas were killed in the silent pass.
- [ ] Present: hook, first 30 seconds, core loop, D1 reason, D1 to D7 lines, money with prices and timing, free-player experience, build ease with MVP, category, six area scores, risk with cheapest test and D1/D7 target.
- [ ] The critic score came from an rbx-judge Agent call (or is labelled `self-critique (not independent)`); the 3-weakness red-team was done and the re-score reflects it; scores are spread, and every 8 or more or 3 or less cites a [K#]/[S#] fact.
- [ ] Each evidence claim points to a [K#] or [S#] or is marked UNVERIFIED; benchmarks are flagged indie or official; no invented numbers; the `KB unavailable` line appears if the KB failed.
- [ ] Nothing copies a specific game's art, names, maps, code or story; all-ages checks pass (no paid randomness, pressure, pay-to-win, unsafeguarded stranger contact; daily rewards only as an ethical extra).
- [ ] The closing line offers build it, another, plan. For a plan: every library is on the approved-options list as an option, no archived libraries, every milestone has a pass/fail acceptance test, exactly 3 tasks for this week, no promise of success, each risk has a check that could prove it wrong.
