---
name: private-server-planner
description: "Decide whether private servers suit a game, choose a monthly price and the features that make them worth buying, check the platform restrictions, and project 12-month income with a constant-rate model. Use when considering paid private servers; one-time perks are gamepass-maker."
category: money
tags: private server, vip server, monthly fee, subscription, social, groups, income projection, paid access
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/_tools/PRICE-LADDER.md
related: gamepass-maker, subscription-planner, price-ladder-planner, devex-planner, regional-pricing-checker
---

# private-server-planner

One job: decide if private servers are worth offering and set them up sensibly. They are a monthly Robux fee, need a public game, cannot coexist with paid access, and group-game split percentages are locked when a subscription is bought (all vault facts, Roblox Creator Docs 2026-10: live-check). They suit social, roleplay, hangout and event games where friends want their own space; they do little for solo grinders.

## When to use
Social or roleplay game with groups, events or creators who host. Not for: one-time perks (`gamepass-maker`), custom subscription tiers (`subscription-planner`).

## Inputs (max 2)
1. Game type and typical group size (default: ask; solo games usually skip). 2. Owner type: individual or group, with revenue split (default: individual).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 5000` and find the paid-access and private-server rule. Confirm the game is public and not on paid access; if paid access is on, stop: they cannot coexist.
2. Judge fit: list what a private-server owner gets that a public server does not (control over who joins, rules, events, saved builds, admin tools). If you cannot name two, report "skip".
3. Features that justify the fee: owner admin panel (kick, ban from the private server, time of day, map choice), reserved capacity, a name and message of the day, saved settings. Build them server-side with the kit `Admin` system where it fits; never trust the client for admin actions.
4. Price: start from `price-ladder-planner` and `_tools/PRICE-LADDER.md` (creator-reported price points); one monthly price per server to start.
5. For group-owned games: set the revenue split before selling anything, because split percentages are fixed at purchase (vault).
6. Projection: `python -I ~/.claude/claude-kit/skillpack/money/private-server-planner/scripts/privserver.py --price <robux> --share <creator share> --new-per-month <n> --churn <0-1>`. The share is REQUIRED because the vault gives no fixed private-server share; read it in Creator Hub the same day. Compare the total with support and moderation work.
7. Regional pricing: review with `regional-pricing-checker`; monthly fees feel different across economies.
8. Write the Creator Hub checklist for the owner. You never turn private servers on or set prices.

## Studio MCP path
Settings live in Creator Hub, not in Studio. For admin features: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` -> `start_stop_play` -> `get_console_output`. Whether a server is private is read from the platform's private-server identifiers at runtime (live-check names); real private servers need a published place and an account that rents one: `untested`.

## Fallback
Plan document plus the projection script (headless). Everything platform-side stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Paid access and private servers rules": public game required, monthly Robux fee, no coexistence with paid access, paid-access games not on Xbox), `Roblox/roblox-kb/business-and-payouts.md` (split percentages locked at purchase; payout timing), `Roblox/roblox-kb/social-features-and-virality.md` (social hooks), `Roblox/roblox-kb/_tools/PRICE-LADDER.md` (creator-reported prices). The churn and new-subscriber inputs are the owner's assumptions.

## Output
`design/private-servers.md`: fit verdict with reasons, feature list, price and rung, `privserver.py` table, split note for groups, Creator Hub checklist.

## Acceptance checks
- [ ] The game is public and not on paid access (stated, with the setting name seen by the owner).
- [ ] `python -I .../privserver.py --selftest` prints "5 checks ok".
- [ ] The projection used a share value the owner confirmed (not a guess) and printed the live-check line.
- [ ] At least two owner benefits are named, or the verdict is "skip".
- [ ] Admin features are server-side only.

## Pitfalls
Selling private servers for a game with no groups. Forgetting the split lock for group games. Planning on a made-up creator share. Leaving owners without tools, so the fee feels like a tax. Turning on paid access later without realising the conflict.

## Related
`gamepass-maker`, `subscription-planner`, `price-ladder-planner`, `devex-planner`, `regional-pricing-checker`.
