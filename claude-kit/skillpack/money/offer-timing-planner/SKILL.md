---
name: offer-timing-planner
description: "Choose the moments in a session where an offer may appear (blocked, out of currency, inventory full, after a milestone, shop open), write the server-side gate that enforces cooldowns, no stacking and no sales on join, and test it. Use when offers feel spammy or never convert; finding data-driven moments is upsell-moment-finder."
category: money
tags: offer timing, moment of need, popup, cooldown, session cap, shop prompt, conversion, dark pattern, upsell
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/common-mistakes.md
related: upsell-moment-finder, starter-pack-designer, limited-offer-designer, shop-conversion-optimizer, pay-to-win-checker, devproduct-handler, first-minute-designer
---

# offer-timing-planner

One job: decide when offers may show and enforce it in code. The vault's rule is "right item, right time": offer a solution when a player is blocked, dying or waiting; do not show sales on join, do not stack modals, show loading-screen offers only after the first session, and skip in-play prompts if gameplay cannot pause. `scripts/OfferGate.luau` makes those rules testable.

## When to use
Offers feel intrusive, appear in the first minutes, stack, or the shop gets no attention. Not for: finding which moments convert from event data (`upsell-moment-finder`), the offer contents (`starter-pack-designer`, `devproduct-handler`), event timers (`limited-offer-designer`).

## Inputs (max 2)
1. The game's recurring friction points: running out of currency, full inventory, death, waiting for a timer, gated area (default: ask the owner to name three). 2. Where gameplay can pause (default: lobby, results, respawn).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` and note the pop-up and moment-of-need rule. Stop when you can list the vault's four "do not" items.
2. Build a table of moments: moment, what the player needs, the offer that solves it, where gameplay can pause, trigger name (`need`, `milestone`, `shopOpen`). Drop any moment where the offer does not solve a real need.
3. Configure `OfferGate` (`scripts/OfferGate.luau`): allowed triggers, first-session triggers (default player-initiated only), global cooldown (default 300 s), per-offer cooldown (default 1800 s), session cap (default 4). These defaults are starting points for an A/B test, not platform rules.
4. Server flow: a gameplay system reports a trigger by name; the server calls `OfferGate.canShow(cfg, state, offerId, trigger, os.time())`; if ok it calls `OfferGate.record` and tells that client to show the offer. The client never decides, and a player-opened shop is never blocked.
5. Keep `state` per player in memory (cooldowns reset each session by design) and read `sessionsPlayed` from saved data.
6. Run `pay-to-win-checker` on offers shown at "need" moments: an offer sold exactly when a player is stuck must sell convenience, never the only way forward.
7. Test: `lune run ../skillpack/money/offer-timing-planner/scripts/tests/OfferGate.test.luau` from `~/.claude/claude-kit/systems`.
8. Plan the measurement: compare shop opens and purchases before and after (`shop-conversion-optimizer`; `ab-testing-and-experiments.md`). Do not call it better until it is measured.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `OfferGate.luau` and the trigger calls -> `start_stop_play` -> `execute_luau` (Server) to fire a `need` trigger twice in a row (second must refuse) -> `get_console_output`. How the offer looks and feels needs a person in a play session: `untested`.

## Fallback
Files plus the Lune test (headless). UI feel stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Don't push purchases with pop-ups; trigger offers at moments of need": pop-ups read as pay-to-win, no sales on join, loading-screen offers only after the first session, a Jailbreak garage-UI buy flow reported at about 40% of purchases), `Roblox/roblox-kb/first-session-onboarding.md` (first-session priorities), `Roblox/roblox-kb/ui-ux-design.md` (modals), `Roblox/roblox-kb/common-mistakes.md`. The cooldown numbers are this skill's defaults.

## Output
`design/offer-timing.md`: the moment table, gate config with reasons, measurement plan; code `OfferGate.luau` and the trigger hooks.

## Acceptance checks
- [ ] Every moment names the need it solves and where gameplay can pause.
- [ ] `canShow` refuses `join`, unknown triggers, stacked modals, mid-action prompts, cooldown hits and the session cap (Lune tests).
- [ ] `lune run` OfferGate tests pass (quote "7 passed, 0 failed") and luau-check is clean.
- [ ] A measurement plan with a before/after metric exists.
- [ ] Offers at need moments pass `pay-to-win-checker` (0 blocks).

## Pitfalls
Timer-based pop-ups. Deciding on the client. Showing three offers back to back because each module has its own gate (use one gate). Prompting during a fight. Counting a player opening the shop as a spam event.

## Related
`upsell-moment-finder`, `starter-pack-designer`, `limited-offer-designer`, `shop-conversion-optimizer`, `pay-to-win-checker`.
