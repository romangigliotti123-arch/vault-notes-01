# Job ledger: <game title>

Counters: runs 0/<budget> · retries 0 · alive 0/<cap> · nesting depth <0>
Environment: python <yes|no> · luau tools <rojo selene stylua luau-lsp: found|missing> · Studio MCP <present|absent>
Plan: ./game-plan.md (routing table = source of these rows)

| id | job | agent / skill | model | effort | depends | mode | owns (write set) | status | attempts | verify (check + output excerpt) | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| J01 | Scaffold Rojo project + Config | roblox-game-builder | sonnet | high | - | serial | default.project.json, src/shared/Config.luau | TODO | 0 | | |
| J02 | ... | | | | J01 | parallel | | TODO | 0 | | |

Status: TODO -> RUNNING -> DONE | FAILED (retry once) -> BLOCKED | SKIPPED. A row is DONE only when the verify cell holds a real check and its output.

## Milestones
| milestone | acceptance test (from the plan) | jobs | status | evidence |
|---|---|---|---|---|

## Progress notes
- <time> <one line per milestone or incident>
