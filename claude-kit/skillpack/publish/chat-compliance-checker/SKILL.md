---
name: chat-compliance-checker
description: "Check every place players can send or see text (chat, signs, names, bulletin boards, DMs) for the safety rules: TextChatService instead of legacy chat, server-side text filtering before display, rate limits on shared text, chat permission checks, console behaviour. Use when adding any text feature and before publish."
category: publish
tags: chat, text filter, TextChatService, safety, rate limit, signs, names, moderation, compliance, console
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/cross-platform-and-console.md
related: tos-compliance-checker, ugc-moderation-checker, age-rating-prep, remote-guard-builder, device-support-setter, publish-readiness-gate
---

# chat-compliance-checker

One job: prove every text path is filtered, reportable and rate-limited. `tos-compliance-checker/scripts/compliance_gap.py --focus chat` finds legacy chat APIs, text inputs with no filter call anywhere, and shared text with no cooldown signal. It is a lead finder; the pass/fail rules come from the live Creator Docs chat pages, which are opened first because they change. It never changes code.

## When to use
Adding or changing chat commands, custom chat UI, signs, nicknames, pet names, bulletin boards, cross-server chat or direct messages; before publish. Not for: images or builds players create (`ugc-moderation-checker`), the maturity answers (`age-rating-prep`), remote validation in general (`remote-guard-builder`).

## Inputs (max 2)
1. Project folder (default: current). 2. List of text surfaces you know about (default: scan finds them).

## Procedure
1. Open the live chat guidelines page (Evidence) and copy the current rule list into the notes with the date. If it differs from the rules below, use the page.
2. Run `python -I ~/.claude/claude-kit/skillpack/publish/tos-compliance-checker/scripts/compliance_gap.py <project> --focus chat`. Read each `file:line`.
3. Legacy chat: any `[FAIL] legacy chat API` row means migrate to TextChatService (`TextChannel`, `SendAsync`); the vault note says the legacy system must be migrated. Stop the release on it.
4. Filtering: for each text input, trace the string from the remote handler to every place another player can see it; it must pass the server-side filter first (`GetNonChatStringForBroadcastAsync` for non-chat text, `TextChannel:SendAsync` for chat) inside `pcall`. A filtered result is shown, never the raw string.
5. Rate limits: shared editable text (signs, boards) gets a server-side cooldown keyed by UserId; the Creator Docs example uses one post per minute per player. Never trust a client timer.
6. Chat permissions: custom direct-message flows check `TextChatService:CanUserChatAsync` / `CanUsersChatAsync` / `CanUsersDirectChatAsync`, and direct channels set the requester with `TextChannel:SetDirectChatRequester`.
7. Console: confirm the chat window handling per the console guidelines page (live-check; the vault note says to disable it on console).
8. Write `release/chat-compliance.md`: text surface table (surface, file:line, filtered?, rate limited?, evidence), pages checked with date, open items. Run the script again after fixes and paste the clean output.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` for `TextBox`, `Chatted`, `FilterStringAsync` -> `start_stop_play` with two clients if available -> `execute_luau` (Client) to send a test string -> `get_console_output`. A play test with two accounts is the only proof the filter and the permission checks work; without it mark those rows `untested`.

## Fallback
Run the script on the Rojo folder and read the flagged lines by hand. Everything needing live accounts (filter results, teen/under-13 chat permissions, console UI) stays `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs chat guidelines.md` (TextChatService required, filter all user text, SendAsync handles privacy and parental settings, rate-limit editable shared text), `... Docs chat examples rate-limit-public-text-inputs.md` (server cooldown per UserId, 60 s example, clear tables on PlayerRemoving), `... Docs production publishing console-guidelines.md`. Pack: `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`, `Roblox/roblox-kb/cross-platform-and-console.md`.

## Output
`release/chat-compliance.md` and the script output before and after.

## Acceptance checks
- [ ] The script ran with `--focus chat` and exited 0 after fixes (quote the last line).
- [ ] Every text surface has a filtered? and rate limited? answer with a file:line.
- [ ] No legacy chat API remains.
- [ ] The live page date is recorded.
- [ ] Two-account test is done or marked `untested`.

## Pitfalls
Filtering on the client. Filtering once at write time and displaying a raw copy later. Forgetting names and attributes players set. Rate limits stored in a table that is never cleared (leak). Assuming a status message or admin announcement needs no filter when it echoes player text.

## Related
`tos-compliance-checker`, `ugc-moderation-checker`, `age-rating-prep`, `remote-guard-builder`, `device-support-setter`.
