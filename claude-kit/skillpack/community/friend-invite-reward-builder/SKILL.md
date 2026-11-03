---
name: friend-invite-reward-builder
description: "Build a friend-invite reward for a Roblox game: an in-game invite prompt, referral detection on the server, mutual rewards, daily caps, milestone ladders and abuse limits, with InviteReward.luau (pure rules with Lune tests). Use when you want invite chains to compound without being farmed, or before adding an invite button."
category: community
tags: invite, referral, friends, social, rewards, viral, share-link, launchdata, abuse, luau
kb: Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: social-hook-designer, clan-system-planner, codes-system-builder, remote-guard-builder, datastore-schema-builder, leaderboard-hooks-planner
---

# friend-invite-reward-builder

The vault is blunt: an in-game invite button is among the most important tips, invite chains are the main organic traffic source, friends found in days 1-7 retain far better, and rewards should go to both inviter and invitee. Roblox (2026) also prefers games that are social by design over pop-ups that beg for invites. This builds the invite flow so it is useful, safe and hard to farm.

## When to use
You want invite chains, a "play with friends" push, or a referral reward. Not for: clan mechanics (`clan-system-planner`), redeem codes (`codes-system-builder`), or designing co-play itself (`social-hook-designer`).

## Inputs (max 2)
1. The reward for each side (default: invitee a small starter cosmetic, inviter soft currency; both modest). 2. Caps (default: 3 rewarded invites per inviter per day; milestone ladder at 1, 5, 10).

## Procedure
1. Make friends better first: natural invite moments (a prompt when a friend would help, a join-friend button, no isolation into separate servers, reserved server slots for friends joining a full server; live-check the reserved-server API) beat a begging pop-up. Do not interrupt gameplay.
2. Invite UI: call `SocialService:CanSendGameInviteAsync(player)` inside `pcall`, only then `SocialService:PromptGameInvite(player)`; handle failure silently. Use a Share Link for off-platform sharing (deep links are deprecated, per the vault) and put your own context in LaunchData if you need it (see step 4).
3. Detect the referral on the server only: `Player:GetJoinData()` after `PlayerAdded` gives the inviter id (the vault names `ReferredByPlayerId`; verify the field in current docs) and LaunchData for share links; join data can arrive late, so poll up to about 10 times at one-second intervals before deciding there is none (vault).
4. Decide with `scripts/InviteReward.luau`: `decide(cfg, referrerId, inviteeId, state)` returns ok or a reason (no_referrer, self_referral, already_claimed, not_new, inviter_cap); `milestonesCrossed(ladder, before, after)` pays every step crossed; `validate(cfg, ladder)` catches config mistakes at server start. Keep results in the kit PlayerData profile (`claimedInvite`, `claimsToday`, `isFirstJoin`) and grant through the kit Shop/PlayerData code.
5. Abuse limits: first join only, one claim per invitee, daily cap per inviter, rewards cosmetic or soft currency (never Robux or anything convertible), delayed grant until the invitee has played a few minutes (optional), alt-account detection by playtime requirement. Never reward off-platform contact exchange.
6. Tell the truth in the UI: say what each side gets; no countdown pressure; no wording that asks young players to message strangers; parents should not need to read fine print.
7. Measure: invites sent, accepted, retained at day 1 and day 7 vs baseline, reward cost, abuse flags.
8. Run `cd systems && lune run ../skillpack/community/friend-invite-reward-builder/scripts/tests/InviteReward.test.luau` (6 tests); lint UI copy with `python welcome-message-writer/scripts/text_lint.py invite-copy.txt`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `InviteReward.luau` and the server wiring -> `start_stop_play` -> `execute_luau` (Server) calling `decide` with junk and valid input -> `get_console_output`. Real referral join data needs a published place and two accounts: `untested`.

## Fallback
The module and tests run in Lune without Studio. Platform calls (`PromptGameInvite`, join data, Share Links) are hand wiring and stay `untested` until run live.

## Evidence
`Roblox/roblox-kb/social-features-and-virality.md` (invite button is key; reward both inviter and invitee and detect referrals on the server; users who find friends in days 1-7 retain much better; guard prompts with CanSendGameInviteAsync; Share Links over deep links; LaunchData and polling; reserve slots for friends; prefer social-by-design over invite pop-ups). `Roblox/roblox-kb/community-and-discord.md` (reward friend invites; invites compound until stable). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`.

## Output
`community/invites.md` (flow, reward table, caps, measures), `InviteReward.luau` in the game, the Lune output pasted.

## Acceptance checks
- [ ] InviteReward Lune test runs green; output quoted ("6 passed, 0 failed").
- [ ] Referral is read on the server; the client never states the inviter.
- [ ] Self-referral, repeat claims, existing players and the daily cap are refused (tests cover each).
- [ ] No reward is Robux or convertible; `text_lint.py` exits 0 on the copy.
- [ ] The invite call is wrapped in `CanSendGameInviteAsync` + `pcall`.

## Pitfalls
Trusting the client. Rewarding existing players (reward loops). Unlimited rewards. A popup that begs on every join. Rewards that tempt kids into sharing contact details. Forgetting join data can be late.

## Related
`social-hook-designer`, `clan-system-planner`, `codes-system-builder`, `remote-guard-builder`, `leaderboard-hooks-planner`.
