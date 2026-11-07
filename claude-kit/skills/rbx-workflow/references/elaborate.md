# Stage 2: elaborate the idea from the vault

Goal: turn one sentence into a concrete, sourced design brief in about 20-25 tool calls. Output `docs/elaboration.md`. Cheap first: `_tools` sheets and kbq, then topic sections, then at most 3 creator playbooks. Budget: stop searching when each section below has at least two cited facts or is marked `KB gap`.

## Setup (each Bash call is a fresh shell, so start with these two lines)
```
K="bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/kbq.py"; eval "$($K where)"   # VAULT KB ASSETS
GENRE="<genre word(s) from the idea>"
```
No python: replace `$K ...` by `rg -n -m5 "<words>" "$KB/<topic>.md"`; topic names are listed in `$KB/README.md`.

## Searches (run the ones that apply; cite what you use)
| Section of the output | Queries |
|---|---|
| Best core loop | `$K route "<idea> core loop"`; `$K section core-loops-and-game-design instructions`; `$K case "$GENRE" -n 3`; `$K find "<genre> core loop cycle time" -t core-loops-and-game-design,genre-mechanics -n 6` |
| First 30 s / 2 min | `$K section first-session-onboarding instructions`; `$K find "first 30 seconds tutorial reward" -t first-session-onboarding -n 5` |
| Map / world | `$K find "<genre> map level design layout" -t building-and-level-design,genre-mechanics -n 6`; `ls "$VAULT/Roblox/docs/Videos" \| grep -i "$GENRE"` (official genre playbooks) |
| Features and progression | `$K find "<genre> progression upgrades rebirth collection" -t core-loops-and-game-design,player-psychology-and-game-feel,genre-mechanics -n 8` |
| Game passes and monetisation | `head -n 60 "$KB/_tools/PRICE-LADDER.md"`; `$K section monetisation-gamepasses rules`; `$K section monetisation-devproducts rules`; `$K num "pass price" -n 8`; `head -n 60 "$KB/_tools/CHECKLIST-monetization.md"` |
| Social and virality | `$K section social-features-and-virality instructions`; `$K find "co-play friends invite party" -n 6` |
| Retention and events | `$K section retention-d1-d7 numbers`; `$K section updates-live-ops instructions` |
| Risks and mistakes | `$K find "mistakes <genre> scope" -t common-mistakes -n 5`; `head -n 80 "$KB/_tools/DECISION-RULES.md"` then `rg -n -i "$GENRE" "$KB/_tools/DECISION-RULES.md" \| head -12` |
| Creator playbooks | `rg -il "$GENRE" "$VAULT/Roblox" --glob "*How to make successful Roblox games.md" \| head -5`, open the top 3 with `head -n 60` |
| How to work | `head -n 60 "$VAULT/Manager/Manager-README.md"` (conventions only) |

Rules: official-flag rows beat indie; a row older than 12 months is "possibly outdated"; indie CCU or revenue numbers are anecdotes, not targets. Patterns, never another game's art, names, maps, code or story. All ages; no paid randomness, no pressure timers aimed at children, no pay-to-win. No source found = write `KB gap`, do not invent.

## Output template for docs/elaboration.md
```
# <Title>: elaboration (<YYYY-MM-DD>)
One-sentence pitch · target player · session length · platform (mobile-first)
FRESHNESS: <paste the Stage 0 line>

## 1. Core loop (three layers)
Moment (seconds): ... -> Session (minutes): ... -> Meta (days): ...   cycle times + why it pulls on day 2. Sources: [path/kbq link, flag, date]
## 2. First 30 seconds and first 2 minutes
0-10 s ... 10-30 s ... 30-120 s ... first reward at <t>, first upgrade at <t>. Sources
## 3. Map / world ideas
3 options (one recommended), size, landmarks, how a new player finds the first goal, performance notes. Sources
## 4. Features (MVP vs later)
| Feature | MVP? | Why | Source |
## 5. Progression and retention hooks
D1 / D7 / D30 hooks; daily/streak vs replayable systems; the one co-play feature. Sources
## 6. Game passes, products, cosmetics
| Item | Kind (pass/product/cosmetic) | Robux price from PRICE-LADDER (source) | Never gates core progress |
Free-player promise; what is never sold.
## 7. Social and virality
Co-play in the core loop, invites, shareable moments, safe-by-default social features.
## 8. Risks and mistakes to avoid
Top 5 with the early check that would show each one is real.
## 9. Open assumptions
Everything you guessed.
## Sources
numbered list: path or link | flag | date
```
Show the user only a 12-line digest (loop, first 30 s, best map idea, 3 key features, pass list, biggest risk) and the path to the file.
