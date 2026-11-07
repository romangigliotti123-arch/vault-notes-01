---
name: rbx-ideas
description: "Claude invents ONE fresh, strange Roblox game idea ('what should I build', 'give me a game idea', 'surprise me'), single-player or open-world first: made blind from the market brief and random seeds, then tested by a separate judge, as a short dot-point card. Then 'build it', 'another' or 'plan'. Own idea: rbx-idea-creator; quick: rbx-idea-quick."
argument-hint: "[genre or theme, optional]"
---

# Roblox game ideas

ONE game, made blind, tested by someone else, shown as a short card. A maker that has never seen a rubric invents the idea from the market brief and random seeds; a separate judge (a bored 12-year-old, hidden questions) says what is good, what is bad and where a kid quits; the maker edits; only after the loop is the idea turned into the card. If the user brings their own idea or wants to be guided to one, that is `rbx-idea-creator`, which uses the Engine below. Phase A = the single card; Phase B = the plan (only on "plan"). No idea is guaranteed to succeed. Say what is likely, why, and what result would show otherwise.

## Hard rules

- Patterns, not content: never suggest copying a specific game's art, names, maps, code or unique story.
- All ages, within Roblox community standards. No real-money gambling, no paid random rewards (Robux into loot boxes, eggs or spins), no countdown or fear-of-missing-out pressure, no pay-to-win, and no stranger contact without safeguards (for example, friends-only parties, opt-in trading, and only Roblox's built-in filtered chat).
- Do not invent numbers, dates, URLs or repository names. Use evidence only from the KB output (tags `[K:...]`) or the market brief (`[S#]`, dated); anything else is marked UNVERIFIED. For a full GDD after the pick, hand off to the rbx-designer agent or skill rbx-gdd; for pricing, rbx-money.
- Libraries and tools are named as options, never installed. Do not run install, download, clone or execute commands (the kit's own `kbq.py`, `spark.py`, `idea-brief.py`, `vault-mode.py` and `games.py` calls named below are the only commands).
- Chart data shows what is already taken, not what to build: never copy the formula of a chart leader as the idea, and never start generating from it.

## Defaults (assume these, state them in one line, and do not block on questions)

Solo developer, comfortable with Luau and basic building, Mac with Studio (Rojo optional) · first playable in 2 to 4 weeks · free CC0 assets only · all ages · game passes and cosmetics only. Ask a question only if the seed breaks a hard rule.

## Engine (shared pipeline: rbx-ideas and rbx-idea-creator both run exactly this)

**QUIET RUN (hard rule, real bug).** While any step or sub-agent runs, write NO text to the user: no "running in the background", no "waiting for ...", no "judge round 2 is running", no progress narration between tool calls, no announcing that the market brief is missing or being written. The only text the user sees is the final card (or the short card) and ONE Done/You/Next footer. The maker and judge sub-agent prompts also say: "Output only your block(s). Never write a Done/You/Next footer, status line or greeting." A footer printed by a hook outside this skill is not yours to fix.

Input: a seed (the user's idea, a genre, the creator funnel's answers) or nothing. Output: ONE reply, the card for the single idea that came out of the loop (or, when no idea cleared the judge, the short card), plus the full detail saved to a file. No menu, no pick turn. The loop is BLIND: the maker never sees a rubric, a score or the card template; the judge's questions live only in the agent file `rbx-idea-judge`, which neither you nor the maker reads. The card template is at the end of this file; do not read past "Formatter" until step (e).

**LANE rule (default; the user's seed overrides it, for example "co-op party game").** An idea is either (a) single-player-first: fun alone, social is optional; or (b) a multiplayer open world or persistent shared world that is also fun solo (explore, collect, build, survive, quest, RPG or adventure style). Co-op-REQUIRED party, puzzle or team-physics ideas (a friend is needed to have fun) are banned unless the seed asks for them. The card states the lane in the Category line (for example "Single-player adventure" or "Open-world MMO-lite").

**Not-a-clone rule.** Chart data shows what is already taken. The idea may borrow a proven format (why the market rewards it) but its verb, rule or moment must be one players have not seen; if you can name the game it is "X but with a theme", it is dead.

**Banned unless the idea earns the word (state the reason in the saved file):** cozy, simulator, tycoon, "obby" plus a noun, idle or clicker, "Escape the X", "Survive X", "Find the Y", "co-op X with friends" as the whole idea, rising tide, lava or water as the pressure, a single rope, bridge, tower or sandcastle gimmick, hatching, eggs, pets plus a coin loop, brainrot, "Grow a" and "Steal a" shapes, and one-word atmospheric titles ("Echo", "Hollow", "Tide"). A colour, mood or setting is not a twist; a changed rule or verb is.

### The blind loop

**(a) Market brief.** Run ONE single-line command: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/idea-brief.py" status`. Fresh (14 days old or less): read it once yourself with `... idea-brief.py show` (you need its date, its [S#] source lines for the card and the summary below); its file path is `... idea-brief.py path`. Missing or stale: refresh it silently (say nothing in chat about the brief being missing or being written) by following [cold:rbx-ideas/brief-refresh.md] read now (the brief is missing, stale or a refresh was asked), with at most the number of searches or fetches it states, then store the result with `idea-brief.py write` (stdin). Sections: What is doing well now / What is fading / Patterns / What players ask for / Gaps. If the refresh fails, use the stale brief, or run without one, and the Notes line says `Market brief unavailable: <reason> - demand and originality claims low confidence`. The user asking for fresh research ("refresh the brief") forces a refresh. Note the brief's date (its first line) for the saved file, and write its summary for the judge: 5 lines at most (what is doing well, what is fading, the biggest gap). Paths, not pasted text, go to agents (cost rule): never paste the brief or the cold files into an agent prompt.

**(b) Idea-maker.** With the Agent tool available the maker is a SEPARATE sub-agent (`subagent_type: general-purpose`, model sonnet) so it has never seen this file. Its prompt contains ONLY:
- the brief's file path and the design-tricks path; the maker reads both itself ([cold:rbx-ideas/design-tricks.md] is read by the maker, never printed; get its path with `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/vault-mode.py" cold rbx-ideas/design-tricks.md --path`; in the installed vault layout and in a bare kit copy this command works as is; if it prints an error, tell the maker to work without the tricks). The maker may read only these two files;
- the seeds from `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/spark.py" draw --n 3 --lane <single|open|any>` (single or open from the lane rule; any when the seed asks for another shape): 3 seed sets, each a group of parts (domain, verb, feeling, constraint, optional twist);
- the user's seed if any; the lane rule; the not-a-clone rule; the banned list; the defaults line;
- this brief (call 1, sparks only): "Invent a Roblox game idea that a 12-year-old would actually play and tell a friend about. Do not try to be balanced, complete or polished. Write 3 one-line sparks; each collides parts of 2 or 3 of the seed sets into ONE playable moment (what the kid does and feels in the first minute, plus the one rule or verb nobody has seen). Kill the weak ones and replace them: a spark dies if a 12-year-old could not repeat it in one sentence, if you can name the game it copies, or if the main verb is what the top games already do (running, collecting, hatching, buying upgrades, surviving a timer, rebirthing). Seeds that push a countdown or pressure may be dropped. After each surviving spark add ` | Quit: ` and your honest one-line guess of the exact moment a kid would quit it. Answer with only a line `SPARKS:` then the 3 sparks, numbered 1 to 3, one line each. Do NOT write the idea yet. Write no file, no scores, no title page. Output only that block; never a Done/You/Next footer or status line."
- the develop message (call 2, sent only after the tournament below, to the same maker): "Develop spark <n> into ONE free-form idea of about 12 lines: the moment, what you do, why you keep playing, what is strange about it, what a solo dev builds first. Keep what is strange. Answer with only a line `IDEA:` whose next line is `<working title> - <one-line pitch>` followed by the idea. No footer or status line."
Seeds may be bent or dropped if they make the idea worse, but the idea must stay strange. With a user seed: the maker keeps the user's core (see rbx-idea-creator). Without the Agent tool: do this yourself as step (b) of the single-agent pass (see "No agents" below). **Tournament (cheap, before the deep loop).** Take the 3 sparks (spark text and quit-moment guess only, never the seeds) and make ONE short call with `subagent_type: rbx-idea-judge` in rank mode: the prompt starts `MODE: rank`, then the sparks, the 5-line brief summary and the lane rule. It returns at most 6 plain lines: `Pick: <n>` (the spark most likely to be played twice) and one `Kill <m>: <why>` line for each other spark. If its answer has no usable `Pick: n`, or fewer than 2 sparks came back, take spark 1. Only the picked spark continues: send the develop message (call 2) for it to the same maker (SendMessage to the exact agent id; fresh maker call with the same paths, the seeds and the picked spark if that fails). The killed sparks and their Kill lines go to the saved file's `## Sparks killed` and are never shown in chat and never relayed to the maker. Everything after `IDEA:` is the idea (the only thing the judge sees in the deep loop). Then run `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/spark.py" hist check "<title>" "<one-line pitch>"`: `NEW` continues; `SIMILAR: <title>` (same or near title, or same pitch) means ONE retry with a fresh `draw` (the maker is told which title to avoid); that retry is not an attempt in the restart rule below.

**(c) Judge.** Call the Agent tool with `subagent_type: rbx-idea-judge` (model haiku, set in the agent file). Its prompt contains ONLY: the idea text, the 5-line brief summary, the lane rule and the stated build time (2 to 4 weeks, solo). Never the full brief, the banned list, the sparks, an opinion of how good it is, scores or a hint about the maker. The judge may read [cold:rbx-ideas/graveyard.md] (only the judge, never the maker, reads it). Send NO message to the user while it runs, and add "Output only your lines; never a footer or status line" to its prompt. It returns at most 10 plain lines (strip a code fence if one slipped in): `Good:` `Bad:` `Quit moment:` `Generic:` (names which part is generic, core or side) `Play twice: yes|no` `Keep (strange, do not sand down):` an optional `Core broken: yes - ...` and an internal `Verdict: n/10`. `Play twice: yes` with a verdict under 7 is inconsistent: treat it as `no`. Relay the lines to the maker verbatim except the Verdict line; the number is for the loop only and is never shown as a rubric.

**(d) Revise.** Stop at once when `Play twice: yes` and the verdict is 7 or more; this is allowed after round 1 (then the card says best of 1 round). Otherwise the maker edits its own idea from the feedback. Continue the same maker with SendMessage to the exact agent id the Agent call returned (cheapest, it keeps its context); if SendMessage is missing, errors or the id is unknown, make a fresh maker call that gets only the same input paths, the previous idea and the feedback. The edit prompt: "Edit your idea from this feedback. Keep what is strange. Never replace the core verb or rule, or the part named under Keep; change only side parts (reward, setting, meta, rules around the core) unless the feedback has the line `Core broken: yes`. If Generic names the core shape, change how it feels, not what it is. Do not adopt another game's mechanic. Fix the quit moment. Remove generic side parts; never swap them for more average ones. Make EDITS, not a rewrite. Answer with `CHANGED:` (one line) then `IDEA:` and the full idea." Judge again with a fresh judge call (same prompt form). At most 3 judge rounds in total per attempt (version 1, then up to two edited versions). Keep the BEST version (highest verdict, later version on a tie).

**Restart rule (replaces polishing a dead idea).** After judge round 2 (and after round 3 if it is played), if the attempt's latest answer is `Play twice: no` with a verdict of 5 or less, or it carries `Core broken: yes`, ABANDON the idea: do not polish it, do not show it. Start a NEW attempt from the tournament: fresh `spark.py draw` seeds (fresh seeds, not the old ones), a fresh maker call (not the resumed one) whose prompt adds "Do not repeat this problem: the abandoned idea was <its one-line pitch>; a kid quit at <the judge's Quit moment line>". Register the abandoned idea with `spark.py hist add` so it cannot come back. Max 2 attempts in total (one restart); after the second attempt never restart. Keep the best-scoring version across both attempts (highest verdict, later on a tie); judge feedback never carries over except the quit moment above.

**After the last attempt.** If the best version has `Play twice: yes` with a verdict of 7 or more, go to (e) for the normal card. If not, never present a build recommendation (no `TL;DR: build ...`): print the SHORT card below instead (the Formatter step (e) is skipped, so no D1 to D7, money or risk tables are written), save the idea file with only front matter, `## Idea`, `## Judge feedback`, `## Run`, `## Sparks killed`, a `## Core loop` line from the idea and a one-line note under `## Week 1`, `## Money` and `## Risks` saying `not written: the judge would not play it twice; reply "plan" for the full version`, then `spark.py hist add`. The full card stays available on `plan`: run (e) on the saved idea, then Phase B.

**Cost guard.** A normal run is 1 maker (call 1, then the develop message resumed) + 1 rank call + up to 3 judge calls; with one restart at most twice that. The saved file's `Run:` line states the real counts (maker, rank, judge, attempts, brief refresh, KB pack, version kept). Nothing can read the weekly-usage note, so the cap of 2 attempts is the only guard.

**(e) Formatter (same turn, after the loop; the template was not read before this point).** Turn the final idea into the card and the saved file. The idea stays as the maker wrote it: do not add a feature the idea does not have or sand the strange part into something generic. Fill what the card needs from the idea; where the idea is silent, decide the smallest thing that fits it; if the idea fails a bar below, say so under Reasons not to build instead of bending the idea. Evidence: run ONE single-line Bash command `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/kbq.py" pack ideas "<the idea's genre words>"`. It prints a pack with stable tags and drops hits that do not match the idea's words. If its first line is not `KB OK` (or it fails), the Notes line says `KB unavailable: <reason>. Fix: <its Fix line>`; never fall back silently. If it says `no relevant KB evidence`, the card says so in one line and uses only the brief; never pad with off-topic hits. `pack` has no length option; if a section ends `(truncated; raise --max-chars)` and you need the rest, read it once with `kbq.py section <topic> instructions --max-chars 3000`. Use the evidence to set the benchmarks and money bands and to back the claims the card makes; it must not pull the idea back toward a chart leader's formula.
   **Citing (strict).** Cite a fact only as the tag its source line printed: `[K:<topic>#id]`, `[K:<topic>/<section>]` or `[K:<case-study>]` (these are stable: they resolve in the KB later), or `[<topic>, <flag>, <date>]` copied from a `kbq.py num` or `section` line, or the brief's own `[S#]` tags. `[S#]` tags belong to the dated brief (the card's Why-this-format line says `brief <date>`), not to the KB. Never mint a tag or number; every bracket in the card must match text in the tool output or brief you actually saw. A claim with no printed source is `UNVERIFIED`; a brief figure the brief marks low confidence stays low confidence on the card. Official Creator Docs and staff override indie advice; indie CCU/revenue figures are never evidence of demand, only of what creators claim. For retention, first-session and pricing facts also run (single-line commands, same `kbq.py`) `num "D1 retention benchmark"` and `section monetisation-gamepasses rules` when the pack lacks them. Benchmarks are indie self-reported unless flagged official; say so.
   **Why this format now:** 1 or 2 evidence bullets from the brief naming the chart games or formats (rank, players, growth, date, [source tag], `brief <date>`) and what the market proves, never a template to copy. If the brief is missing or stale, say so in one line.
   Not-a-clone line (required): `Keeps: <the nearest known formula, named> | New: <fresh verb or rule>`. Bars for the card:
   - **Hook:** one sentence a 12-year-old repeats, clear from the title and thumbnail, with a moment worth clipping. Name the clip moment.
   - **First 30 seconds:** the player acts in under 10 seconds with no reading; first reward within about 15 seconds; a guaranteed first win; teaching by doing, icons over text.
   - **Core loop:** act, reward, upgrade in about 2 minutes or less, and it still pulls on day 2.
   - **D1 return reason:** a specific unfinished thing in THIS game (a named goal in sight, a collection gap, a build to finish, a friend waiting), never "a daily reward" alone. Daily rewards only ethically: no loss framing, no penalty for missing a day, never the sole reason to return.
   - **Week 1 (D1 to D7):** one short line per day, and every line must name something that exists only in this game (a rule that changes, a place, a role, a creature, an event, a tool) and could not be pasted into another game's card. Banned as week-1 lines: "daily reward", "leaderboard", "friends board", "album" or "collection of N" without a game-specific item, "teaser for the next zone", "new area unlocked", "bigger version of the same". Something real must change by D3; D5 or D6 adds a social beat that fits the game's social shape; D7 has a long goal. State how many pieces of content or sessions week 1 needs and whether a solo dev can make that.
   - **Money:** game pass, cosmetic and convenience ideas that fit THIS game (what players would proudly show, or what saves a real chore), with prices in Robux (cosmetic or convenience in the 59 to 99 band unless the KB says otherwise) and when each first appears in week 1 (never in the first minutes; after the first win). What free players get: the full loop and every goal. No paid randomness, no pressure, nothing that blocks core progress. Do not reuse the same three items (decor pack, emote pack, extra slot) from game to game.
   - **Build ease (solo) 1 to 10, with a time estimate in weeks:** 9 to 10 = one place, no custom netcode, CC0 assets, about 2 weeks; 7 to 8 = one risky system, 2 to 4 weeks; 4 to 6 = several bespoke systems or multiplayer sync; 1 to 3 = needs a team, custom physics or heavy art. One-line reason and a one-line first build (what to build first, what to cut).
   - **Category:** the genre label the player would search for plus the lane.
   - **Reasons not to build, biggest risk, cheapest test** (measures 2 numbers; D1/D7 targets from the KB, flagged indie or official).
   Save the full detail to `research/idea-<slug>.md` (slug = kebab-case title) in the game's project folder; when there is none (for example a session in the vault folder), use `./research/` under the current folder (create it) and say so in one clause. The file must let every tag resolve later: the `## Sources` section lists each KB tag used with its printed source line (topic, flag, date, link) and each [S#] used with its brief line and link, headed `Brief date: <YYYY-MM-DD>`. Then register the idea so it never repeats: `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/spark.py" hist add "<title>" "<one-line pitch>"`. In chat show ONLY the card and the short relative path.

**"Another":** a different idea: rerun (b) to (e) with a fresh `draw` (different seeds; the earlier title and pitch named as taken; the brief reused by path; `hist check` blocks repeats). No runner-up reuse.

**No agents available** (you are a subagent, the Agent tool is missing, or low-usage mode): run the same sequence yourself in one pass, in this order and without looking at the card template until step (e): brief, 3 sparks with quit-moment guesses, a separate rank pass that picks the spark a bored 12-year-old would play twice, one idea, then a SEPARATE judge pass in which you play the bored 12-year-old and answer only: would I play it twice and why, what do I tell a friend, where do I quit, what known games is it (core or side), is the strange part fun or only weird, is it buildable, does it need a friend; write the same `Good/Bad/Quit moment/Generic/Play twice/Keep` lines (yes only if you would rate it 7 of 10 or more), edit side parts (up to 2 times, keep what is strange; a `no` with verdict 5 or less after the second pass means one restart with fresh seeds, as in the restart rule), then format, or print the short card if the answer is still `no`. The Notes line says `No independent judge - single-agent pass` and the judge field of the card reads `Judge: self-review, would play twice: yes/no`. Never present your own pass as an independent judge's.

### Saved file format (what the builder and `games.py init --from-idea` read)

```
---
title: <Title>
slug: <kebab-case-slug>
pitch: <one line>
category: <genre label and lane>
---
## Idea               (the maker's final free-form text)
## Core loop          (act -> reward -> upgrade, with cycle time)
## Hook and first 30 seconds
## Week 1             (D1 .. D7, one line each; content or sessions needed)
## Money              (passes, cosmetics, convenience, prices, when; free-player experience)
## Judge feedback     (each round: the judge's lines as returned, what the maker changed; final: Play twice yes/no, best of N rounds, version K)
## Risks              (biggest risk, cheapest test measuring 2 numbers, D1/D7 target)
## Target player
## Evidence           (Why this format now: chart games with rank, players, date, brief date)
## Sources            (Brief date: <YYYY-MM-DD>; every [S#] used with its brief line and link; every KB tag used exactly as printed with its topic, flag, date and link, so tags resolve later)
## Run                (one line: calls made, e.g. maker 2, rank 1, judge 2, attempts 1, brief refresh no, KB pack yes; version kept; est. cap: 2 attempts x (1 maker + 1 rank + 3 judge))
## Sparks killed      (the sparks the rank call killed, with its Kill lines, and any abandoned attempt with its quit moment; the seeds drawn; why each banned word used was earned)
## Funnel answers     (creator only: each round, answer or "skipped -> default applied")
```

### The card (chat output; cap 48 non-blank lines, blank lines are not counted; dot points, no tables, bullets short (about 12 words), no "a / b" joined bullets, plain words, phone-readable)

```
TL;DR: build / skip - <one short reason>            <- ALWAYS the first line
Notes: <only when needed, one line each: "No independent judge - single-agent pass" | "KB unavailable: ..." | "Market brief unavailable: ..." | creator: "Building your idea from: <answers>" ; the normal card is printed only for an idea with `Play twice: yes`, otherwise the short card>
**<Title>** - <one-line pitch>
- Category: <genre> - <lane> · Judge: would play twice: yes/no, best of <N> rounds (version <K>), <independent | self-review> - <its one-line reason>
- Why picked: <bullet> · <bullet>
- Not a clone: Keeps <x> | New <y>
- Why this format now (brief <date>): <chart game or format, rank, players, growth, date [S# tag]> · <what the market proves; second bullet optional>

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

Why it can work
- <evidence bullet with the exact tag as printed> (2 bullets), or "No relevant KB evidence for this idea; the brief only"
Reasons not to build this: <one line, the owner decides>
Biggest risk: <risk>. Cheapest test: <test measuring 2 numbers>; target D1 <x>%, D7 <y>% (<KB tag>, indie or official)

Detail: research/idea-<slug>.md
Done — <what happened, one line; the detail file lists the sources behind every tag>
You — reply "build it" (create the game folder + README), "another" (a different idea), or "plan" (full plan)
Next — <what happens on your reply>
```

Output rules (these were real bugs): the TL;DR is the very first line of the reply, nothing above it; any Notes line sits directly under it; print exactly ONE Done/You/Next footer, as the last three lines, and no other "Reply ..." closing line; no progress message or footer is printed before the final card (not while the brief is read, the maker works or the judge runs); the one reply ends with exactly one footer. There is no scores line: only `Build ease x/10` and the judge line show a rating, and the judge's number is never printed.

Spell Robux in full where first used and avoid jargon (say "first build" not MVP, "players online" not CCU, or define it in two words). Assumed defaults go in one short line under the title only if they changed something. Do not print the Engine steps, sparks, the judge's raw feedback, the idea drafts or the evidence table in chat: they live in the file.

### The short card (only when no idea cleared the judge; cap 14 non-blank lines)

```
TL;DR: No idea cleared the judge; best attempt below is weak
**<Title>** - <one-line pitch>
- <second pitch line: what you do and the one strange rule>
- Judge: would not play it twice, <N> attempts, <independent | self-review>
- Quit moment: <the judge's Quit moment, in plain words>
- Keep if you build it: <the judge's Keep part>

Detail: research/idea-<slug>.md
Done — <one line: tried N ideas, none passed the judge>
You — reply "another" (a fresh idea), "build it anyway" (create the game folder + README), or "plan" (full card and plan)
Next — <what happens on your reply>
```

Same output rules as the card: nothing above the TL;DR, exactly one footer, no scores or rubric.

### After the card

- **"build it" (or "build it anyway" after the short card):** run (single line) `bash "$HOME/.claude/claude-kit/tools/pyrun" "$HOME/.claude/claude-kit/tools/games.py" init <slug> --from-idea research/idea-<slug>.md`. It creates `Games/<slug>/` and seeds README.md (pitch, loop, hook, week-1 loop, monetisation, risks). Then give the folder path and offer `/rbx-workflow` to continue. Nothing else is built.
- **"another":** see the Engine ("Another"): one different idea, the same lane rule and the same single card.
- **"plan":** Phase B below, on the idea in the file. Phase B is unchanged.

## Phase B: Plan

If the user asks for a plan with no card yet, run the Engine on that seed first (brief, maker, judge loop, card) and plan the result; if the judge would not play it twice, say what the quit moment is and offer the closest stronger variation before you write the plan. With a card, plan that idea from `research/idea-<slug>.md`. Keep each section short and mark items `DECIDE:` (the user must choose) or `UNVERIFIED:` (no source).

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

1. "What should I build?" No seed: the market brief is read (or refreshed once if stale), three random seeds are drawn, a maker that never saw a rubric (it reads the brief and the tricks file by path) collides parts of them into three one-line sparks with quit-moment guesses, a one-line rank call picks one, and the maker writes ONE free-form idea from it, `hist check` (title and pitch) says NEW, the haiku judge returns its lines (nothing printed meanwhile), the maker edits keeping the strange part, the loop stops at `Play twice: yes` with verdict 7 or more (a dead idea is abandoned and restarted once, never polished or shown), and only then is the card written (lane in the Category line, `Why this format now:` with chart evidence, `Judge: would play twice: yes, best of 2 rounds (version 2)`) ending in one Done/You/Next footer, with the detail in `research/idea-<slug>.md`.
2. "Something about cooking with friends." The seed is kept as the core and developed through the same loop (social features friends-only, so no stranger contact). The dedicated route for a user's own idea is rbx-idea-creator.
3. "Plan" after a card: Phase B. The This week block comes first (for example, "Greybox the kitchen with Kenney kit pieces. Done when: a player can walk from the counter to the stove in under 5 s"). The Systems table shows Player data = ProfileStore (option), Order queue = Build, and UI = DECIDE.

## Self-check before replying

- [ ] Quiet run: no text was written while sub-agents ran (no "running in the background", "waiting for" or brief-writing lines); maker and judge prompts forbade a footer; the reply has exactly one footer. Tournament: 3 sparks, one rank call, only the pick was developed. Restart: at most 2 attempts, fresh seeds, no `TL;DR: build` and no full card for an idea the judge rejected (short card instead).
- [ ] The reply is the card only (no menu, no pick turn): cap 48 non-blank lines, TL;DR as the very first line (Notes lines under it), exactly one Done/You/Next footer at the end, no interim progress message was printed, dot points, no tables, no candidate list, bullets short; the detail is in `research/idea-<slug>.md` and only the short relative path is shown.
- [ ] The loop was blind: the maker (a sub-agent, or the single-agent pass labelled in the Notes line) got only the brief and tricks file paths, the drawn seed sets, the user's seed, the lane, not-a-clone and banned rules; no rubric, score or card template. The judge was an `rbx-idea-judge` Agent call (or the Notes line says `No independent judge - single-agent pass`), got only the idea, a brief summary of 5 lines at most, the lane rule and the build time, and its raw feedback and number were not printed. At most 3 judge rounds; early stop on yes with verdict 7 or more; best version kept; the card says `best of N rounds (version K)` and the real `Play twice` answer; the detail file has the `Run` line.
- [ ] Sparks collided drawn seeds into one playable moment; `spark.py hist check "<title>" "<pitch>"` was NEW (one retry on SIMILAR); `spark.py hist add` ran after the card was made; no banned trope word survived without a stated reason; ONE idea in the card, with the `Keeps | New` line naming the nearest formula.
- [ ] Lane and charts: the Category line names the lane; `Why this format now:` has 1 or 2 evidence bullets with rank, players, date and a printed tag (or the one-line brief-missing note); the idea is not a chart leader's formula.
- [ ] Present: hook, first 30 seconds, loop, tomorrow reasons, D1 to D7 lines, money with Robux prices and timing, free-player experience, build ease with weeks and first build, category, judge line, reasons not to build, risk with cheapest test and D1/D7 target. No scores line.
- [ ] Week-1 lines and money items are specific to this game (none could be pasted into another card; no daily reward, leaderboard, album or teaser filler).
- [ ] Every bracket tag in the card matches text in the kbq output or the market brief; no minted tags; the saved file's Sources section lets each tag resolve (brief date included); unsupported claims are UNVERIFIED; benchmarks are flagged indie or official; a missing or stale brief is stated.
- [ ] Nothing copies a specific game's art, names, maps, code or story; all-ages checks pass (no paid randomness, pressure, pay-to-win, unsafeguarded stranger contact; daily rewards only as an ethical extra).
- [ ] The footer's You line offers build it, another, plan, and the reply has exactly one footer. For a plan: every library is on the approved-options list as an option, no archived libraries, every milestone has a pass/fail acceptance test, exactly 3 tasks for this week, no promise of success, each risk has a check that could prove it wrong.
