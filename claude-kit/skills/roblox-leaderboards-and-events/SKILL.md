---
name: roblox-leaderboards-and-events
description: "Implement Roblox global leaderboards (OrderedDataStore), badges, timed live events and daily rewards safely. Use when adding competition, badges or recurring events to a Roblox game."
---

# Leaderboards, badges, live events

## Global leaderboard
1. Use `DataStoreService:GetOrderedDataStore("Wins_v1")`. Values are integers only. Write with `SetAsync`/`UpdateAsync` from the server only, after the score is validated by the server.
2. Update on meaningful changes and at save time, not every second (shared request budgets with other DataStores).
3. Read the top N with `GetSortedAsync(false, 50)` and `GetCurrentPage()`, cache the result for 60-120 s on the server and replicate to clients; do not let every client query.
4. For weekly/monthly boards, put the period in the store name (`Wins_2026W44`) and keep the previous one for rewards. Resolve names with `Players:GetNameFromUserIdAsync` (pcall + cache) or thumbnails with `Players:GetUserThumbnailAsync`.
5. Anti-cheat: score comes only from server-observed events; cap per-minute gain; log outliers.

## Badges
`BadgeService:AwardBadge(userId, badgeId)` from the server inside pcall; check `UserHasBadgeAsync` first; create badges in Creator Hub (costs Robux per badge beyond the daily free allowance, so confirm with the user before creating many). Award for onboarding milestones, not spam.

## Timed and live events
1. Drive event windows from server time (`os.time()`/`DateTime.now()`), with the schedule in a config module or MessagingService / a remote config table so it can change without an update.
2. Use `MessagingService` to sync across servers (rate limits apply, treat messages as hints, not guarantees).
3. Daily reward: store `lastClaim` (UTC day number) and streak in the profile; claim on the server; grace window for time zones; never trust client dates.
4. Event content ships hidden and unlocks by time; test by faking time in a config flag in Studio only.
5. Ethics: rewards must be earnable by play; no countdown pressure aimed at kids or paid random rewards.

Verification: claim twice in a day (second denied), claim next day (streak +1), rejoin mid-event, two servers see the same event state.
