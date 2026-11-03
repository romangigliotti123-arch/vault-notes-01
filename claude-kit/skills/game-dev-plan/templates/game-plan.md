# game-plan: <Title> (<YYYY-MM-DD>)
FRESHNESS: <line from freshness.py>
Pitch: <one sentence> · Rating: <x.xx>/10.00 (docs/rating.md) · Project folder: <path>

## 0. Assumptions (nothing was asked; change any of these and re-run /game-dev-plan)
- Solo developer + Claude · all ages · mobile-first · first playable in <n> days · no pay-to-win / paid randomness · files-first (Rojo), Studio MCP: <present|absent at planning time>
- <every guess made while planning>

## 1. Core loop and first session (from docs/elaboration.md)
<3 lines: loop with cycle times; 0-10 s, 10-30 s, 30-120 s>

## 2. Systems
| system | build or library | option / source | owner job |
|---|---|---|---|

## 3. Milestones and acceptance tests
| # | milestone | est. days | acceptance test (pass/fail, observable) | jobs |
|---|---|---|---|---|

## 4. Assets and libraries
| need | pack / library | license | path | note |
|---|---|---|---|---|
(ids for Roblox assets, passes and products stay `0`: SET IN CREATOR HUB)

## 5. Library search result (what was chosen and why)
| job type | candidates found (Library path) | chosen | installed? |
|---|---|---|---|

## 6. Final routing table
Subagent cap: <N> alive at once · Total worker runs: <M> · Retries: 1 per job · Nesting: depth 0 · Models allowed: haiku, sonnet
| # | job | skill / agent | model | effort | parallel or serial | owns (files) | budget (runs, turns) |
|---|---|---|---|---|---|---|---|
Stop rule: budget reached -> stop dispatching, verify what exists, report PARTIAL with the remaining jobs.

## 7. Studio MCP vs files
Files/Rojo for all code and config. Studio MCP (only if present): <jobs marked MCP: map instances, insert/sync, playtest read of Output>. Never launch Studio.

## 8. Needs the owner (not done by Claude)
Publish the place, final Robux prices, real asset/pass/product ids, thumbnail upload, ad spend.

## 9. Risks and kill rules
<top 3 risks, each with the early check and the number that would end or pivot the project, with source/flag>
