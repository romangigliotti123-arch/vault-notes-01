---
name: paid-random-compliance
description: "Check eggs, crates, spins and any random reward bought with Robux (or currency bought with Robux): odds table arithmetic, disclosure before purchase including indirect currencies and odds boosters, per-player PolicyService gating, and the restricted-player alternative with its expected-value price. Use when designing or before publishing any random paid item."
category: publish
tags: paid random items, odds, loot box, eggs, gacha, PolicyService, disclosure, compliance, trading, expected value
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: loot-drop-builder, age-rating-prep, tos-compliance-checker, pay-to-win-checker, devproduct-handler, regional-availability-checker
---

# paid-random-compliance

One job: make a random paid mechanic pass the published rules, with arithmetic instead of opinion. Two executable checks: `scripts/odds_check.py` validates the odds table and prints the expected-value price of each outcome; `tos-compliance-checker/scripts/compliance_gap.py --focus paid_random` finds random-item + purchase code that lacks the per-player PolicyService check. The rules, property names and thresholds come from the live paid-random-items page, opened first (`live-check`: policies change). Building the mechanic is `loot-drop-builder`.

## When to use
Designing an egg/crate/spin, adding a luck boost or re-roll, enabling trading of random outcomes, and before publish. Not for: simulated gambling (banned outright; remove it), normal fixed-price shops (`gamepass-maker`, `devproduct-handler`), the maturity answers (`age-rating-prep`).

## Inputs (max 2)
1. The outcome list with odds and the price (or "read from the project"). 2. Whether outcomes can be traded (default: unknown, the scan will look).

## Procedure
1. Open the live paid-random-items page (Evidence); copy its definition of a paid random item and the disclosure rules into the notes with the date.
2. Write the table as JSON (`cost`, `currency`, `outcomes[{name, odds, one_time}]`, `modifiers[]`, `indirect[]`, `displayed_percent_note`) and run `python -I ~/.claude/claude-kit/skillpack/publish/paid-random-compliance/scripts/odds_check.py odds.json`. Fix every FAIL: odds not summing to 100, an undisclosed luck booster, an indirect currency (key, ticket, re-roll) whose odds are not shown before it is spent.
3. Check the UI against the page: all outcomes and numeric odds visible before purchase; a "Details" button with text (a bare icon is not enough) when the list is long; boosters explained numerically and updated while active; one-time outcomes re-normalise the remaining odds per user.
4. Run `python -I .../tos-compliance-checker/scripts/compliance_gap.py <project> --focus paid_random`. A FAIL means no `ArePaidRandomItemsRestricted` (or trading) check was found.
5. Design the restricted-player path from the page's options: free earnable route, fixed-order outcomes, or a direct purchase priced from the `expected-value price` line the script printed (example in the docs: 10 Robux at 5% implies 200 Robux). Never invent a price: use the script output.
6. Trading: if outcomes are tradable, block trading for players whose policy disallows it (`IsPaidItemTradingAllowed`), on the server.
7. Write `release/paid-random.md`: odds table, script output, UI evidence (screenshots by the owner), restricted-path design, date of the page. Mark the Studio parts `untested` until a restricted-policy test run happens.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`ArePaidRandomItemsRestricted`, `GetPolicyInfoForPlayerAsync`) -> `start_stop_play` -> `execute_luau` (Server) to read the policy table for a test player and print which branch the shop took -> `get_console_output`. Policy values for real accounts differ by country and age; you cannot fake them in Studio.

## Fallback
The two scripts run with no Studio. Server behaviour for restricted accounts is `untested` until the owner tests with such an account.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production monetization paid-random-items.md` (all outcomes with numeric odds before purchase; indirect purchases and boosters; percentages sum to 100; PolicyService per user; alternatives for restricted users; expected-value pricing example), `... Docs production promotion content-maturity.md` (PolicyService for paid random items and paid item trading). Pack: `Roblox/roblox-kb/monetisation-other.md`, `Roblox/roblox-kb/_tools/CHECKLIST-monetization.md`.

## Output
`release/paid-random.md` and `odds.json` with the script output.

## Acceptance checks
- [ ] `odds_check.py odds.json` exits 0 (quote the OK line and the expected-value lines).
- [ ] `compliance_gap.py --focus paid_random` shows no FAIL.
- [ ] Every indirect currency and booster is disclosed before spend.
- [ ] A restricted-player path exists and its direct price comes from the script.
- [ ] `odds_check.py --selftest` prints `selftest ok`.

## Pitfalls
Rounding odds so they total 99.9 without the disclaimer. Disclosing odds only on the final spin screen, after the key was already spent. Calling the policy once at join and caching it for a purchase that happens later in another context. Treating "free spin" paths as exempt when a Robux-bought currency also feeds the spin.

## Related
`loot-drop-builder`, `age-rating-prep`, `tos-compliance-checker`, `pay-to-win-checker`, `regional-availability-checker`.
