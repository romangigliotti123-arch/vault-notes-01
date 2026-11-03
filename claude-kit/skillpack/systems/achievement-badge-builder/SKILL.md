---
name: achievement-badge-builder
description: "Build achievements that unlock once, are saved in player data, and award Roblox badges idempotently through a pending queue with retries, so a failed BadgeService call never loses a badge and a retry never double-awards. Use for badges and in-game achievement lists."
category: systems
tags: badges, achievements, BadgeService, AwardBadge, idempotent, retry, unlock, pending queue
kb: Roblox/roblox-kb/genre-mechanics.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/discovery-algorithm.md
related: quest-system-builder, first-minute-designer, event-planner, discord-server-setup, roblox-launch-checklist
---

# achievement-badge-builder

One job: unlock an achievement exactly once and get the matching badge onto the player's account even when the Roblox call fails or the server shuts down. The unlock flag and a pending entry are written into the player's saved data in one step; `flush` calls the injected award function (a `pcall` around `BadgeService:AwardBadge`) and removes the entry only on success. Badge id 0 means the badge is not created yet (SET IN CREATOR HUB): the achievement still unlocks.

## When to use
Welcome badge, discovery badges, milestone badges, hidden achievements. Not for: quest objectives (`quest-system-builder`), creating or pricing badges in Creator Hub (the owner does that), pass ownership (`gamepass-maker`).

## Inputs (max 2)
1. Achievement list: id, trigger, badge id (default: 5 achievements, badge ids 0). 2. Hidden or visible in the UI (default: visible with progress).

## Procedure
1. List achievements by what they celebrate: first action, discovery, milestone, mastery. Vault: reward discovery (easter eggs) with badges and hint at them in the badges tab. Avoid achievements that require grinding a loophole.
2. Copy `Achievements.luau`; `Achievements.new({ defs = { first_win = { badgeId = 0 } }, award = function(userId, badgeId) ... end, onUnlock = notifyClient })`. The `award` function is `pcall(BadgeService.AwardBadge, BadgeService, userId, badgeId)` returning true when it succeeds (an already-owned badge counts as success).
3. Trigger from server code where the condition is proven: `ach:unlock(userId, data, "first_win")` returns true only the first time. No remote ever says 'give me achievement X'.
4. Flush: call `ach:flush(userId, data)` in its own thread right after an unlock, on join (after `resetAttempts`), and on a slow timer; it yields (network). Entries keep a try counter and park after `maxAttempts` until the next session.
5. Check the badge before awarding if you want a hard guarantee: `BadgeService:UserHasBadgeAsync` (live-check limits) can be wrapped into `award` so a double award is impossible even when the local flag was lost.
6. Save the unlock before the badge call (the flag is in `data.Achievements`); on `BindToClose` run one last flush with a short time budget.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/achievement-badge-builder/scripts/tests/Achievements.test.luau` (quote the "N passed, 0 failed" line); verify in a published place with a test account that the badge appears (`untested` until then).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Achievements.luau` and the award wrapper -> `start_stop_play` -> `execute_luau` (Server) to unlock an achievement for the test player with a fake award function that fails twice, then print `data.Achievements` -> `get_console_output` to read the result. Real badge awarding needs a published place and created badges: `untested` until the owner checks the account.

## Fallback
Files + Lune tests with a failing fake award. Everything that needs a running Studio session (BadgeService calls, notification UI) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/genre-mechanics.md` (hide easter eggs and award badges for discovery, hint in the badges tab), `Roblox/roblox-kb/retention-d1-d7.md` (early milestones support retention), `Roblox/roblox-kb/anti-exploit-and-security.md` (verify progression on the server). BadgeService limits and API behaviour: live-check the official docs.

## Output
`Achievements.luau`, the award wrapper, `Achievements.luau` defs, `design/achievements.md` (list, triggers, badge ids to create).

## Acceptance checks
- [ ] `unlock` is true once and queues one badge call (Achievements test 1).
- [ ] A failing award is retried and never doubled (test 2).
- [ ] Badge id 0 unlocks with no badge call (test 3); unknown ids unlock nothing (test 4).
- [ ] Entries park after the attempt limit and resume next session (test 5).
- [ ] Achievements Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/achievement-badge-builder/scripts/tests/Achievements.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Marking done only after the badge call succeeds (a crash repeats the unlock effects). Calling `AwardBadge` on the main thread without `pcall`. Awarding in `PlayerAdded` before data loads. Trusting a client remote as the trigger. Creating badges the design never pays out.

## Related
`quest-system-builder`, `first-minute-designer`, `event-planner`, `roblox-launch-checklist`.
