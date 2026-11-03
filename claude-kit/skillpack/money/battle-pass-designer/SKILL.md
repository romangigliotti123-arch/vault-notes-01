---
name: battle-pass-designer
description: "Design a season pass with free and paid tracks, a stated end date, fair pacing and quests tied to the core loop, then implement the server-side track logic (idempotent claims, premium gate, mid-season unlock) with tests. Use when adding a seasonal progression pass; permanent perks are gamepass-maker."
category: money
tags: battle pass, season pass, free track, premium track, tiers, xp, quests, seasonal, claim, pacing
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/pricing.md
related: gamepass-maker, devproduct-handler, event-planner, limited-offer-designer, subscription-planner, economy-balancer, pay-to-win-checker
---

# battle-pass-designer

One job: a season pass that players finish and trust. The vault's rules for season or battle passes are short and consistent: free and paid tracks, limited time with a stated end date, quests tied to the core loop, previewed in the shop, mid-season buyers claim premium rewards they already earned, and premium rewards visually separate. The server logic is in `scripts/SeasonTrack.luau`; purchase and ownership go through the kit Shop system (`systems/Shop`, NOT live-tested in Studio).

## When to use
A seasonal progression with tiers is wanted. Not for: permanent one-time perks (`gamepass-maker`), monthly auto-renewing tiers (`subscription-planner`), event content without a paid track (`event-planner`).

## Inputs (max 3)
1. Season length and cadence (default: 30 days, new season on a calendar). 2. The actions that give season XP (default: the core loop's main action plus 3 daily quests). 3. Reward types you can afford to produce (default: cosmetics, currency, one permanent convenience).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` and `section events-and-seasonal-content rules`. Stop when you can name the five season-pass rules above.
2. Fix the frame: `tiers`, `xpPerTier`, `startsAt`, `endsAt` (required: a pass without an end date is rejected by `SeasonTrack.validate`).
3. Pace it: choose the XP a casual player earns per day and run `SeasonTrack.pacing(cfg, xpPerDay)`. If a casual player cannot finish, cut tiers or raise XP; players quit passes they cannot finish.
4. Fill both tracks. Free track: real rewards at regular intervals so free players have a reason to engage (reward currency, one cosmetic, one emote). Paid track: cosmetics and convenience, never required content or pvp power. Run `pay-to-win-checker` on the paid list.
5. Price the pass with `price-ladder-planner` (a core or higher rung; one price per season at first). Consider whether the pass currency can be bought as a developer product: if so, apply `receipt-flow-tester`.
6. Wire: premium is a game pass or product in the Shop catalogue; on a confirmed purchase the grant sets `state.premium = true` in the saved data. Every XP award and every claim runs on the server through `SeasonTrack.addXp` and `SeasonTrack.claim`; the client sends only `track` and `tier`. After a mid-season purchase call `SeasonTrack.claimable` to show everything already earned.
7. Store `state` (xp, premium, claimed) in the player's saved record (`datastore-schema-builder`), not in a separate table that could lose idempotency.
8. Test: `lune run ../skillpack/money/battle-pass-designer/scripts/tests/SeasonTrack.test.luau` from `~/.claude/claude-kit/systems`.
9. Plan the next season before this one ends and write the Creator Hub checklist. You never create or price the pass.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `SeasonTrack.luau` and the quest hooks -> `start_stop_play` -> `execute_luau` (Server) to add XP for a test player and claim tier 1 twice (second must refuse) -> `get_console_output`. Premium purchase needs a published place: `untested` until the owner buys with a test account.

## Fallback
Files plus the Lune test (headless). UI and the purchase stay `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (season pass rules; limited-time items and event currency; no pay-to-win; moments of need), `Roblox/roblox-kb/events-and-seasonal-content.md` (seasonal cadence), `Roblox/roblox-kb/updates-live-ops.md` (content calendar), `Roblox/roblox-kb/retention-d1-d7.md` (return reasons), `Roblox/roblox-kb/pricing.md`. Tier counts and XP numbers are not in the vault as targets: they come from your pacing check.

## Output
`design/season-N.md`: frame, pacing result, both tracks as a table (tier, free reward, paid reward, cost to produce), quests, price, next-season plan, Creator Hub checklist, test steps; code `SeasonTrack.luau` plus the grant hook.

## Acceptance checks
- [ ] `SeasonTrack.validate(cfg)` returns no problems (quote the output).
- [ ] `SeasonTrack.pacing` shows a casual player can finish, or the design says why not.
- [ ] A second claim of the same tier is refused and the premium track refuses without the pass (Lune tests).
- [ ] `lune run` SeasonTrack tests pass (quote "8 passed, 0 failed") and luau-check is clean.
- [ ] Paid track passes `pay-to-win-checker` with 0 blocks.

## Pitfalls
A pass with no end date or an unfinishable grind. Granting premium rewards from the client. Forgetting that a mid-season buyer must get earned tiers. Storing claims outside the saved record. Reusing last season's rewards without a plan for owners.

## Related
`gamepass-maker`, `devproduct-handler`, `event-planner`, `limited-offer-designer`, `subscription-planner`, `economy-balancer`.
