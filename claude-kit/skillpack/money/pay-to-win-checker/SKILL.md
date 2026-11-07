---
name: pay-to-win-checker
description: "Check every paid offer against the vault's pay-to-win and paid-random-item rules (core-progress gating, pvp power, odds disclosure, restricted-user path, pop-ups, timers, stock caps) and return BLOCK/WARN findings with sources. Use before shipping or changing any pass, product, crate or bundle; designing the offers is gamepass-maker and devproduct-handler."
category: money
tags: pay to win, paid random items, loot box, odds, policy, fairness, offers, audit, gating, restrictions
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/common-mistakes.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: gamepass-maker, devproduct-handler, starter-pack-designer, vip-pass-designer, limited-offer-designer, publish-readiness-gate, rbx-monetize-audit
---

# pay-to-win-checker

One job: a pass/fail review of paid offers against the vault's rules. The linter (`scripts/OfferLint.luau`) takes yes/no facts per offer and returns findings with the source note. It judges the description you give it, so the skill's value is in asking the facts honestly and reading the code to verify them. Roblox policy changes: every BLOCK that cites a platform rule must be live-checked (paid random items and restricted-user handling especially) before you tell an owner an offer is fine or not.

## When to use
Before launch, before adding any pass, product, crate, spin, egg or bundle, and in a review of an existing shop. Not for: designing the offers (`gamepass-maker`, `devproduct-handler`), a whole-game audit (`rbx-monetize-audit`), age-rating prep (`age-rating-prep`).

## Inputs (max 2)
1. The list of paid offers with what each grants (default: read the shop catalogue and the code that grants). 2. Modes: which are competitive pvp (default: assume combat modes are pvp).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000` (the pay-to-win rule and the paid-random-items rule) and `section monetisation-gamepasses rules`. Live-check the platform's current paid-random-items page for the restricted-user API names and the odds-disclosure format.
2. For each offer fill the facts honestly by READING the grant code, not the product description: `pvp`, `grantsCombatPower`, `gatesCoreProgress`, `requiresHardCurrency`, `randomized`, `oddsShown`, `restrictionPathHandled`, `popupOnJoin`, `timerSkipOrAppointment`, `limitedStock`.
3. Run `OfferLint.check(offers)` (in a Lune script or the command bar). It returns `findings, blocked`. BLOCK: gating core progress, combat power in pvp, random items without shown odds, random items without the restriction path. WARN: hard-currency-only tasks, appointment or buyable timers, sales on join, limited stock.
4. Fix BLOCKs by redesign, not by rewording: move power to cosmetics or progression speed, show every outcome with numeric odds before spend (including keys, re-rolls and luck boosts), gate random items per player and give restricted players a free, fixed or direct path.
5. Treat WARNs as questions for the owner; record the decision and the reason. The vault carries one dissent on limited stock (a creator reports it sells), so a WARN there is a test, not a ban.
6. Random items checklist: server-side generation only (`anti-exploit-and-security`), odds in the UI equal the odds in code (read both), pity or direct-purchase alternative considered, regional and age rules checked (`age-rating-prep`).
7. Report: findings table, what was verified in code, what stays unverified. Test: `lune run ../skillpack/money/pay-to-win-checker/scripts/tests/OfferLint.test.luau` from `.rbx/claude-kit/systems`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) to read the catalogue module and print offers -> `get_console_output`. For random items, `start_stop_play` and call the roll function 1000 times on the server to compare observed odds to the displayed odds. Live restriction behaviour needs a test account in a restricted region or age: `untested`.

## Fallback
Read the files, fill the facts, run the Lune lint (headless). Policy behaviour stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (never pay-to-win; paid random items: disclose odds, gate via the policy service, treat as optional and risky; loot boxes about 1% of one game's revenue; one creator says chests work almost anywhere, flagged as a minority view), `Roblox/roblox-kb/monetisation-gamepasses.md` (free players reach all core content), `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`, `Roblox/roblox-kb/common-mistakes.md`. The lint encodes these rules; it is not Roblox's own validator.

## Output
`reports/pay-to-win.md`: table (offer, finding, severity, rule, fix), verified-in-code list, unverified list, live-check dates. Short: one row per finding.

## Acceptance checks
- [ ] Every offer in the catalogue has a row, with facts taken from the grant code.
- [ ] `OfferLint.check` was run and `blocked` is false, or each BLOCK has a fix or an owner decision.
- [ ] Displayed odds equal the odds in code for every random offer (both quoted).
- [ ] `lune run` OfferLint tests pass (quote "7 passed, 0 failed") and luau-check is clean.
- [ ] The platform's paid-random-items page was live-checked (date) or marked unverified.

## Pitfalls
Filling the facts from the shop description instead of the code. Trusting that "odds are in the UI" without comparing to the roll code. Treating the lint as legal advice. Forgetting indirect random purchases (keys, luck boosts). Ignoring a mode that is competitive.

## Related
`gamepass-maker`, `devproduct-handler`, `starter-pack-designer`, `vip-pass-designer`, `limited-offer-designer`, `rbx-monetize-audit`.
