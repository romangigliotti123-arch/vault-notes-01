---
name: donation-system-builder
description: "Build a tip or donation flow the safe way: a server-validated amount, the platform's Robux transfer prompt confirmed in the receipt handler, an idempotent donation board, and no reliance on cross-game passes or products that are being disabled. Use when adding donation boards or tips; selling items is gamepass-maker."
category: money
tags: donation, tip, robux transfer, leaderboard, board, receipt, server validation, regional pricing, transfers api
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/case-studies-please-donate.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/roblox-platform-changes.md
related: devproduct-handler, receipt-flow-tester, regional-pricing-checker, pay-to-win-checker, remote-guard-builder, shop-conversion-optimizer
---

# donation-system-builder

One job: tips that cannot be forged, double counted, or built on a feature that is going away. The vault reports that cross-game pass and developer-product tipping stops when those sales are disabled (DevForum, 2026-05) and points to the Robux transfer prompt, whose result is confirmed in the receipt handler; the game sets the amount in its own UI because it is fixed once the platform's transfer UI opens; the vault also reports transfer limits (10-500 Robux, developer gets 10%) and that you validate on the server, grant after the receipt and answer NotProcessedYet if the player left. All of that is a fast-moving API: live-check it before building. A donation board may lift revenue in lobbies per one self-reported case; test against your own ARPDAU.

## When to use
Donation boards, tip jars, "support the dev" buttons. Not for: selling items (`gamepass-maker`, `devproduct-handler`), subscriptions (`subscription-planner`).

## Inputs (max 2)
1. Amount model: fixed presets, free input, or both (default: presets). 2. Where the board lives and how many names it shows (default: lobby, top 10).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000` and find the transfers rule and the lobby-board note. Live-check the transfer API page: names, limits, the receipt callback.
2. Decide the donation target: the experience's creator account or a specific player (the vault's player-to-player tipping context is Please Donate; read `case-studies-please-donate.md` for the pattern, not to copy).
3. Validate on the server before opening any prompt: `Donations.validate(cfg, fromUserId, toUserId, amount)` rejects non-whole numbers, NaN, out-of-range amounts, amounts not in the preset list and self-donation. The client sends an amount choice; the server owns the config. Put the min/max in `cfg` from the live-checked docs, not from memory.
4. Open the platform's transfer prompt from the server-validated request only (rate limit the remote with `remote-guard-builder`).
5. Confirm and count in the transfer receipt handler only: on a confirmed transfer call `Donations.add(board, receiptId, userId, name, amount)`; it returns false for a receipt it already counted (idempotent). If the player left or data is not ready, answer the retry status so the platform delivers again, exactly as for products (`receipt-flow-tester`).
6. Board: `Donations.top(board, 10)`; store totals in the saved record or an ordered store, never trust client-sent totals; escape or filter display names through the platform text filter before showing them.
7. Rewards: if donors get a cosmetic, grant it in the same confirmed step through the Shop-style grant; never promise gameplay power for donations (`pay-to-win-checker`).
8. Regional pricing does not apply to a transfer amount the same way as to passes; the vault reports donation-style passes misbehaving under regional pricing, so do not rebuild tips as passes (`regional-pricing-checker`).
9. Test: `lune run ../skillpack/money/donation-system-builder/scripts/tests/Donations.test.luau` from `.rbx/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `Donations.luau`, the remote and receipt handler -> `start_stop_play` -> `execute_luau` (Server) to call `Donations.validate` with junk and valid amounts and `Donations.add` twice with one receipt id -> `get_console_output`. The real transfer needs a published place and two accounts: `untested`.

## Fallback
Files plus the Lune test (headless). The transfer flow stays `untested`; never spend Robux in testing.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Regional pricing, gifting and Robux transfers"; "Migrate tipping and donations to the Transfers API"; "Add lobby monetisation once players arrive", PineappleDev 2025, self-reported), `Roblox/roblox-kb/case-studies-please-donate.md`, `Roblox/roblox-kb/pricing.md` (turn off regional pricing on donation-style passes, one 2025-12 report), `Roblox/roblox-kb/anti-exploit-and-security.md`, `Roblox/roblox-kb/roblox-platform-changes.md`. API names and limits: live-check.

## Output
`design/donations.md`: flow diagram in text (client request, server validate, prompt, receipt confirm, count, display), config values with their live-check date, test results; code `Donations.luau`, the remote and the receipt hook.

## Acceptance checks
- [ ] The server rejects junk amounts (Lune test "junk amounts are refused" passes).
- [ ] A receipt id is counted once (test "the board counts a receipt once").
- [ ] `lune run` Donations tests pass (quote "7 passed, 0 failed") and luau-check is clean.
- [ ] No tip path depends on cross-game passes or products.
- [ ] The transfer API names and limits were live-checked (date) or marked unverified.

## Pitfalls
Trusting a client-sent amount or total. Counting on prompt-finished events instead of the confirmed receipt. Building tips on cross-game passes. Showing unfiltered names. Skipping the retry status when the player left.

## Related
`devproduct-handler`, `receipt-flow-tester`, `regional-pricing-checker`, `pay-to-win-checker`, `remote-guard-builder`.
