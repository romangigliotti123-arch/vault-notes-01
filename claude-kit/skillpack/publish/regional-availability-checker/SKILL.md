---
name: regional-availability-checker
description: "Check what changes by player country, age and policy: regional content restrictions, PolicyService flags for paid random items, trading and ads, age-gated features, and whether the game degrades gracefully for restricted players. Use before publish and before expanding to new regions or younger audiences."
category: publish
tags: regional availability, PolicyService, country restrictions, age gating, paid random items, trading, ads, compliance
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/cross-platform-and-console.md
related: tos-compliance-checker, paid-random-compliance, ad-policy-checker, age-rating-prep, localization-setup, device-support-setter
---

# regional-availability-checker

One job: find every feature whose availability depends on WHO the player is, and prove the game behaves for the restricted player. The platform can make content undiscoverable and unplayable in specific countries because of local law, and per-player flags (`PolicyService:GetPolicyInfoForPlayerAsync`) change what the game may offer. You cannot choose or test real countries from Studio. `tos-compliance-checker/scripts/compliance_gap.py --focus region` shows whether policy is read at all next to restricted-feature signals. All lists of regions and flags are `live-check`: restrictions change over time.

## When to use
Before publish, when adding paid random items, trading, ads, chat or social features, and when marketing to a new country. Not for: translating the game (`localization-setup`), regional pricing (`regional-pricing-checker`), the questionnaire (`age-rating-prep`).

## Inputs (max 2)
1. Project folder (default: current). 2. Target markets (default: no specific market).

## Procedure
1. Open the live regional content availability page and the content maturity page (Evidence) and copy what they say about country restrictions and policy flags, with the date.
2. Run `python -I .rbx/claude-kit/skillpack/publish/tos-compliance-checker/scripts/compliance_gap.py <project> --focus region` and `--focus all` for context.
3. List the restricted-feature candidates in this game: paid random items, trading of paid items, ads, social features, text. For each, name the policy property that governs it (from the live page, not memory) and the file:line that reads it.
4. Design the degraded path per feature: hide, replace or block, never crash. The paid random and ads pages list concrete alternatives (free route, fixed-order outcomes, direct purchase, no ad).
5. Read the policy once per player at join AND before the gated action when long sessions are possible; cache with a short time, not forever. Never trust a client-supplied value.
6. Record that the game itself can be unavailable in some countries and that nothing in code can change that; check analytics by country after launch (`post-launch-monitor`) so a sudden drop is explained.
7. Write `release/regional.md`: feature table (feature, governing flag, reads it at file:line, restricted-player behaviour), market notes, page dates, `untested` rows.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`GetPolicyInfoForPlayerAsync`) -> `start_stop_play` -> `execute_luau` (Server) to print the policy table for the test player -> `get_console_output`. The result is for the test account only; a restricted country or age needs a real restricted account.

## Fallback
The scan and the table need no Studio. The restricted-player behaviour stays `untested` until someone plays with a restricted account.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production promotion regional-content-availability.md` (content restricted by local law becomes undiscoverable and unplayable there; can change over time), `... Docs production promotion content-maturity.md` (PolicyService for paid random items and trading), `... Docs production monetization paid-random-items.md`, `... Docs production promotion comply-with-advertising-standards.md`. Pack: `Roblox/roblox-kb/localization-and-international.md`.

## Output
`release/regional.md`.

## Acceptance checks
- [ ] The region scan ran and its lines are attached.
- [ ] Every gated feature has a governing flag, a read location and a restricted-player behaviour.
- [ ] The live page date is recorded.
- [ ] Restricted-player tests are done or marked `untested`.
- [ ] No feature relies on a value sent by the client.

## Pitfalls
Assuming a VPN in Studio tests a restriction. Hard-coding country lists. Reading the policy only at join and gating a purchase hours later. A restricted player seeing a broken, empty shop instead of the alternative path.

## Related
`tos-compliance-checker`, `paid-random-compliance`, `ad-policy-checker`, `age-rating-prep`, `localization-setup`.
