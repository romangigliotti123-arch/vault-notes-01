---
name: Analytics
type: system
what: Validated wrapper over AnalyticsService for economy, onboarding/funnel, progression and custom events, with the documented caps and a rate limit enforced locally.
tags: analytics, funnel, economy events, custom events, onboarding, progression, metrics, telemetry
tested: unit-tested headless (Lune) + analyzed + linted; NOT tested in live Studio
---
# Analytics

**What:** one place for all event logging so the numbers in the Creator Dashboard (and the Open Cloud Analytics API, see `game-dev-weekly`) are clean enough to judge the game by.
**Not tested in live Studio**: the enum names in `AnalyticsGlue.luau` (`Enum.AnalyticsEconomyFlowType`, `AnalyticsProgressionType`, `AnalyticsCustomFieldKeys`) type-check against the Roblox definitions bundled in the kit, but events have not been seen in a dashboard.

## Files
`src/Analytics.luau` (pure), `src/AnalyticsGlue.luau` (builds it from `AnalyticsService` + enums), `tests/Analytics.test.luau`.

## Setup
```lua
local Analytics = require(script.Parent.Systems.Analytics.AnalyticsGlue).Create()
Analytics:Onboarding(player, 1, "Spawned")               -- first-session funnel: steps 1-100, sent once per player
Analytics:Onboarding(player, 2, "FirstCoin")
Analytics:Economy(player, "Source", "Coins", 50, newBalance, "Gameplay", "quest_wolves")
Analytics:Economy(player, "Sink", "Coins", 300, newBalance, "Shop", "sword_basic")
Analytics:Funnel(player, "FirstPurchase", HttpService:GenerateGUID(false), 1, "OpenedShop")
Analytics:Progression(player, "World1", "Complete", 3, "Level 3")
Analytics:Custom(player, "BossKilled", 1, { [Enum.AnalyticsCustomFieldKeys.CustomField01] = "Dragon" })
```
All methods return `true` when the event was sent, `false` when dropped (invalid, capped, duplicate, rate limited, service error); they never throw.

## Rules it enforces (from the current AnalyticsService docs; each has a test)
- Economy: flow `Source`/`Sink`; `amount` positive; `endingBalance` >= 0; at most 5 currency types, 20 transaction types, 100 SKUs per experience (counted per server; a dynamic name that would blow the cap is dropped and logged instead of silently eating the cap).
- Onboarding/funnel steps are integers 1-100; each step is sent once per player (per session id for funnels); at most 10 funnels.
- Progression path name: no comma, quotes, newline. (The docs say progression events do not yet appear in Roblox-provided charts.)
- Custom field keys limited to the allowed enum items; values strings up to 100 chars (docs: 8,000 unique combinations across the 3 fields per experience, so use low-cardinality values like "Dragon", not user ids).
- Rate limit: 30 per minute per player per event name (config `maxPerMinute`).

## What to log (minimal set that answers the weekly questions)
Onboarding steps for the first 2-3 minutes (where do new players drop?), economy events for every currency source and sink (is the economy inflating?), a funnel for the first purchase, one custom event per core-loop completion. See `game-dev-weekly` for how these map to benchmark checks.

## Pitfalls
- Call from the server (the glue and these rules assume it); data logged from the client can be faked.
- Never put names, user ids or free text in event names, SKUs or custom fields.
- Do not log per-frame or per-hit; log per completed action.
- Events take up to a day to appear in dashboards; test with a small number of calls and look the next day.

## Tests (2026-11-01)
```
cd <claude-kit>/systems && python check.py Analytics
  stylua ok | selene ok | analyze ok (0 errors, 0 warnings) | lune Analytics.test.luau: 9 passed, 0 failed
```

## Sources
create.roblox.com/docs/reference/engine/classes/AnalyticsService (LogEconomyEvent, LogCustomEvent, LogFunnelStepEvent, LogOnboardingFunnelStepEvent, LogProgressionEvent; caps as stated there, read 2026-11-01); /docs/production/analytics (custom events, funnels). Re-check the caps when Roblox changes the docs.
