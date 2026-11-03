---
name: chat-filter-tester
description: "Verify that all user-generated text (chat, pet names, signs, titles, descriptions, saved text) is filtered on the server with the text filter before other players or storage see it. Scans handlers for unfiltered text sinks, then runs a live test with a non-dev account. Use before launch and whenever a feature lets players type."
category: qa
tags: chat filter, text filter, filterstringasync, moderation, user text, pet names, sign, tos, safety, textchatservice
kb: Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md
related: input-validation-auditor, exploit-audit, remote-guard-builder, age-rating-prep, publish-readiness-gate, server-authority-checker
---

# chat-filter-tester

Any text one player can type and another player (or a later session) can read must pass Roblox's text filter on the server first. Default chat does this for you; custom text (pet names, signs, clan tags, house names, bios, in-game messages, saved notes) does not. `scripts/FilterScan.luau` finds handlers where an argument that looks like text reaches a sink (`.Text`, `.Name`, `FireAllClients`, a DataStore write, an attribute) without a filter call in the same handler. It is a heuristic that reuses `input-validation-auditor/scripts/ArgScan.luau` for handler extraction.

## When to use
Before launch, after adding any typing feature, after a moderation warning, or when reviewing `publish-readiness-gate`. Not for: argument shape validation (`input-validation-auditor`), blocking links or scams beyond the filter, or deciding age ratings (`age-rating-prep`).

## Inputs (max 2)
1. Where players can type (default: grep `TextBox`, `ChatService`, `RenameRemote`, `SetAsync` with strings). 2. Who sees the text: self only, other players, or stored for later (default: assume other players).

## Procedure
1. Inventory every text entry point: `TextBox` instances in GUIs, chat commands, remotes with string arguments, any saved free text. Stop when each has a row: source, who sees it, where stored.
2. Run `FilterScan.scanHandlers(ArgScan.extract(source))` on the server scripts: each finding is a handler where a text-named argument reaches a visible/persistent sink with no `FilterStringAsync`/`FilterTextAsync`/`GetNonChatStringForBroadcastAsync` in the handler. Read each one; a filter inside a helper function is a false positive, a missing one is HIGH.
3. `FilterScan.scanClient(path, source)` flags client scripts that show remote-supplied text. That is only safe if the SERVER filtered it for this recipient before sending.
4. The correct shape: the client sends raw text; the server validates length first, calls `TextService:FilterStringAsync(text, senderUserId)` in a pcall (it can fail: show a placeholder or reject), then uses `GetNonChatStringForBroadcastAsync()` for text shown to everyone (names, signs) or `GetChatForUserAsync(recipientId)` for private/per-recipient text. Never filter on the client, never store raw text for later display without storing the filtered form or re-filtering at display.
5. Free text also enters through `Name` of instances, billboard labels, leaderboard names, and saved descriptions: apply the same rule.
6. Live test in a TEST place with a NON-dev account (dev accounts can behave differently): type a clearly filterable test string, a long string, an empty string and unicode; check the OTHER client sees the filtered result (hashes) and that a failed filter call (simulate with a pcall error) rejects instead of falling back to raw text.
7. Record rows that depend on Roblox's behaviour as live-checked; the filter's exact rules change and are Roblox's.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `TextBox|FilterStringAsync|OnServerEvent` -> `script_read` -> `execute_luau` (Edit) running FilterScan over `Script.Source` -> `multi_edit` to add the filter -> `start_stop_play` with two clients -> `execute_luau` (Client) to fire the text remote -> `screen_capture` of the second client -> `get_console_output`.

## Fallback
Grep for the sinks above and read each handler; `lune run ../skillpack/qa/chat-filter-tester/scripts/tests/FilterScan.test.luau` from `claude-kit/systems` shows the scan on samples. The behaviour of the live filter (what it blocks) cannot be tested offline and is `untested` without a published place.

## Evidence
`Roblox/roblox-kb/anti-exploit-and-security.md`: filter all player-generated text on the server with `TextService:FilterStringAsync` before showing free text to others; Safety Callback / Reviewable Content APIs are early access (live-check). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`: moderation and TOS obligations for user content. `Roblox/roblox-kb/testing-debugging-and-qa.md`: test with non-dev accounts. Trust: official docs and DevForum, labelled.

## Output
```
CHAT FILTER <game> <date>: text entry points N, unfiltered sinks M
| entry | who sees it | sink | filtered? | fix |
Live test: <account type, strings tried, result>   Unchecked: <helper filters, dynamic remotes>
```

## Acceptance checks
- [ ] `lune run` of the FilterScan test prints "5 passed, 0 failed".
- [ ] Every text entry point has a row and every sink a verdict.
- [ ] A failed filter call rejects the text (no raw fallback); verified by reading the code or by test.
- [ ] The live test used a non-dev account and a second client, or is marked `untested`.
- [ ] Saved free text is stored filtered or re-filtered at display.

## Pitfalls
Filtering on the client. Filtering once for the sender and showing the same string to everyone. Using the filtered result for the sender but the raw text for storage. Ignoring `Name` and attribute sinks. Letting a pcall failure fall through to the raw text. Assuming an allowlist of words replaces the filter.

## Related
`input-validation-auditor`, `exploit-audit`, `remote-guard-builder`, `age-rating-prep`, `publish-readiness-gate`.
