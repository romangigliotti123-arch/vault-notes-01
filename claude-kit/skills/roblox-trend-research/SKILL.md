---
name: roblox-trend-research
description: "Market research on Roblox only. Finds which Roblox experiences lead right now and turns them into a dated, sourced library of transferable patterns (first 30 seconds, core loop, retention, social, monetisation, discovery), never content to copy. Reads the local knowledge base first, then the web for live data. Not for ranking ideas or writing a plan; that is roblox-game-ideas."
---

# Roblox trend research

Output: a pattern library with a date and a source on every claim. Not a list of games to clone, and not game ideas (hand those requests to roblox-game-ideas).

## Hard rules

- Patterns, not content. Describe mechanics and structure ("daily reward offered on the first screen"). Never reproduce a game's art, names, maps, code or unique story.
- Read-only, public pages only, via WebSearch and WebFetch. No login, no account, no posting, no rapid or bulk fetching. Do not install, download, clone or run anything.
- Never guess an endpoint, URL, number, date or repository name. Use only URLs found in search results or on pages already fetched.
- Correlation is not cause. "Most leaders do X" is evidence, not proof that X drives success.
- All ages. Flag, never recommend: real-money gambling, paid random rewards, countdown or fear-of-missing-out pressure aimed at children, and contact with strangers without safeguards.

## Mode and budget

Pick the mode from the request, then stay within its budget. When the budget runs out, stop and report what you have, listing the gaps.

| Mode | When | Games | Max searches | Max page fetches |
|---|---|---|---|---|
| Broad | "What's working on Roblox?" | 12 to 15 across 4+ genres | 10 | 25 |
| Focused | A genre, theme or question, or a call from roblox-game-ideas | 6 to 8 in the genre, plus 4 overall leaders for contrast | 8 | 18 |

If a report saved in the current project (`research/roblox-trends-*.md`) is 14 days old or less and covers the same scope, reuse it, say so, and only fill gaps.

## Source rules

Tier every source.

- **A (primary):** Roblox-owned pages: Creator Hub docs, the Roblox blog or newsroom, Roblox staff posts on the DevForum, Roblox's public charts/Discover pages, a game's own roblox.com page.
- **B (secondary):** trackers that show a timestamp on their data, and developer-written postmortems with figures.
- **C (leads only):** news and gaming press, YouTube, wikis, Reddit, aggregators. A claim backed only by C sources is marked UNVERIFIED.

Freshness:
- Player counts and chart positions: 30 days old or less, otherwise label them `stale (<date>)`.
- Trend claims ("rising", "saturated"): need at least one source from the last 90 days.
- Design patterns (how a loop works): older sources are fine if the game is still live, but say how old they are.
- If a page shows no date, write `undated`; never infer one.

Citations: every number and every trend claim gets a `[S#]` tag that points to the Sources table (URL, published date, accessed date, tier). A claim you could not source is written as:
`UNVERIFIED: <claim>. Tried: <S# or search terms>.`
Dynamic pages often show no numbers to WebFetch; then write `not visible to fetch` instead of estimating.

## Step 0: KB first, web second

The local Roblox knowledge base holds dated, sourced, official/indie-flagged material (516 sources, 90 case studies). Query it before any web search, about 4-6 calls:

```
K="bash $HOME/.claude/claude-kit/tools/pyrun $HOME/.claude/claude-kit/tools/kbq.py"   # run `$K where` once to see VAULT/KB/ASSETS
$K route "trends <genre or question>"
$K section trend-research-and-validation instructions
$K section game-ideas-and-genres instructions
$K case "<genre>" -n 4          # case studies with transferable patterns and numbers
$K find "<genre> growing saturated demand" -t trend-research-and-validation,game-ideas-and-genres -n 8
$K section roblox-platform-changes date
```

Treat KB items as Tier A when flagged official (Creator Docs, Roblox sessions) and as Tier C leads when indie/self-reported; cite them as `[K#]` with the timestamp link. KB patterns count toward "shared patterns" (3+ games). The KB is a snapshot dated by its sources, so use the web only for live facts it cannot hold: current CCU and chart positions, what rose in the last 90 days, and anything the KB reports as a gap. Reduce the search and fetch budget below by the number of KB case studies you used (minimum 3 searches). Add a `K#` block to the Sources table.

## Steps

1. **Leaders.** Find the current top experiences by concurrent players (and visits where shown). Record name, genre, concurrent players, date seen and S#. Prefer Tier A, then B.
2. **Break down each game.** Use one line per field, only for what the sources show (otherwise `n/a`):
   first 30 s (what the player does first and how it is taught) · core loop (action, reward, cycle length) · session (length, what ends it) · retention (daily, progression, collection, events, friends, limited-time) · social (solo, co-op, PvP, trading; how players meet) · monetisation (what is sold, where offers appear) · discovery (title and thumbnail style, update cadence).
3. **Shared patterns.** Group what appears in 3 or more games. Give each one an ID (P1, P2...) and fill in: description, used by (n of N, with names), why it likely works, a small-scope version for a solo developer, and saturation (low, medium or high, with the reason).
4. **Rising patterns.** Up to 3 patterns that are rare among the leaders but present in newer or smaller recent hits. Mark these as low confidence.
5. **Build and avoid.** Build: common, cheap for a solo developer with free assets, fits all ages. Avoid: needs a big team or art budget, relies on pressure or paid randomness, or is saturated with no obvious twist.
6. **Self-check** (below), then reply using the template. Save to `research/roblox-trends-<YYYY-MM-DD>.md` in the current project when the user asks or when roblox-game-ideas called this skill.

## Output template

```
# Roblox trends: <Broad | genre/question> (<YYYY-MM-DD>)
TL;DR
- Strongest trend: <one line> [S#]
- Best pattern to build small: P# <name>
- Main caveat: <data gaps, staleness, saturation>

## Leaders (seen <date range>)
| # | Game | Genre | CCU | Seen | Src |

## Shared patterns (most widely used first)
| ID | Pattern | Used by | Why it likely works | Small-scope version | Saturation |

## Rising patterns (low confidence)
- P# <name>: <one line> [S#]

## Build / Avoid
Build: P#, P#, P# (one reason each)
Avoid: <pattern>: <reason>

## Unverified and gaps
- UNVERIFIED: ...
- Budget used: <x>/<max> searches, <y>/<max> fetches. Not covered: ...

## Sources
| S# | Title | URL | Published | Accessed | Tier |
```

Per-game breakdowns from step 2 go in the saved file only, not in the chat reply, unless the user asks for them.

## Worked examples (shape only; numbers come from sources at run time)

1. "What's working on Roblox right now?" leads to Broad mode: about 14 leaders, about 6 shared patterns, each with an S# tag; TL;DR names one trend, one buildable pattern and one caveat ("CCU for 5 games not visible to fetch").
2. "What do top tycoon games do in the first minute?" leads to Focused mode: 6 to 8 tycoons and 4 overall leaders; the patterns table is weighted towards the first 30 seconds and onboarding; Build lists the 2 cheapest onboarding patterns.
3. "Is the obby genre saturated?" leads to Focused mode: the TL;DR opens with a saturation verdict (low, medium or high), the evidence for it ([S#] from the last 90 days) and what would show the verdict is wrong; Rising patterns lists the twists that newer obbies use.

## Self-check before replying

- [ ] The TL;DR fits on the first phone screen and answers the question.
- [ ] Every number and trend claim has an [S#] with a date; nothing estimated or guessed.
- [ ] Stale and undated data are labelled; trend claims have a source from the last 90 days or are marked UNVERIFIED.
- [ ] No URL, endpoint or repository name was typed from memory.
- [ ] Patterns only: no art, names, maps, code or story offered for reuse.
- [ ] Nothing that breaks the all-ages rules is recommended (risky patterns appear only under Avoid).
- [ ] No claim that a pattern guarantees success.
- [ ] Budget respected and the gaps listed.


## Triggers (moved out of the description)

Use proactively, without being asked for a skill by name, whenever the user asks what is popular, trending or working on Roblox, what top Roblox games do, whether a Roblox genre is saturated, or wants research before building a Roblox game.
