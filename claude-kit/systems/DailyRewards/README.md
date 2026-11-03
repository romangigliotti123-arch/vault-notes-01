---
name: DailyRewards
type: system
what: Daily login reward with streaks, grace days, custom day boundary and clock-tamper handling; pure functions on a state table stored in the player's data.
tags: daily reward, streak, login bonus, retention, daily, calendar
tested: unit-tested headless (Lune) + analyzed + linted; NOT tested in live Studio
---
# DailyRewards

**What:** claim once per day (UTC day by default), streak grows on consecutive days, resets after a gap (optionally forgiving `graceDays`), reward cycles over `rewardCount` days.
**Not tested in live Studio** (the pure logic is; the RemoteFunction glue is only type-checked).

## Files
`src/DailyRewards.luau` (pure), `src/DailyRewardsService.luau` (RemoteFunction `DailyReward` in ReplicatedStorage: `"status"` / `"claim"`), `tests/DailyRewards.test.luau`.

## Setup
Add `Daily = { streak = 0, total = 0 }` to your data template, then:
```lua
DailyRewardsService.Start({
	config = { rewardCount = 7, graceDays = 0 },
	getData = PlayerDataService.Get,
	apply = function(player, data, cycleDay, streak) data.coins += 100 * cycleDay end,
	saveNow = PlayerDataService.SaveNow,
})
```
Client shows the calendar from `InvokeServer("status")` (`canClaim`, `streak`, `cycleDay`, `nextClaimAt` unix time -> countdown) and calls `InvokeServer("claim")`.

## Config
`rewardCount` (cycle length), `graceDays` (default 0), `dayLength` (86400), `dayOffset` (seconds; `-5*3600` makes the day roll over at UTC-5 midnight), `capStreak`.

## Behaviour (each has a test)
First claim = streak 1. Same day again: `already`, nothing changes. Next day: +1. Gap larger than grace: back to 1 and `brokeStreak = true` so the UI can say so. Server clock moves backwards: refused (`clock`), streak untouched. `sanitize` repairs old/edited state.

## Pitfalls
- Time must come from the server (`os.time()` is UTC and correct on servers); never accept a time or "day" from the client.
- Apply the reward in the same synchronous step as `Claim` (the glue does); a yield in between allows a double pay on a second request.
- Streak-loss is a retention/fairness lever, not just a number: players hate losing a 30-day streak to a timezone; consider `graceDays = 1` and a streak-freeze item (see vault retention notes).
- Do not pay premium-sized rewards on a streak that can be reached by waiting alone; keep the cycle reward modest and the top day special.

## Tests (2026-11-01)
```
cd <claude-kit>/systems && python check.py DailyRewards
  stylua ok | selene ok | analyze ok (0 errors, 0 warnings) | lune DailyRewards.test.luau: 10 passed, 0 failed
```

## Sources
Roblox docs: `os.time` (UTC), RemoteFunction security (never trust client arguments); KB retention notes (daily rewards and streak design in the vault Roblox KB).
