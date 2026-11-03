---
name: social-hook-designer
description: "Add co-play and friend-invite hooks that make a session with a friend likelier: pick 2-3 hooks from invite prompt, shared goal, trade, party, friend teleport and spectate, keep the solo path working, and define the metric that proves they work. Use after the core loop, before social systems are built."
category: design
tags: social, co-op, invite, friends, party, trade, multiplayer, virality, referral, retention
kb: Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-meep-city.md, Roblox/roblox-kb/case-studies-island-royale.md
related: core-loop-designer, session-length-designer, friend-invite-reward-builder, teleport-hub-builder, trading-system-builder, retention-diagnoser
---

# social-hook-designer

Vault (official): a meaningful play session with a friend is the top predictor of return; about 30 percent longer sessions and 60 percent more likely to return D0-D1 with friends. Players who find friends in days 1-7 retain much better. Any genre can be social.

## When to use
Designing how players find, invite or play with friends. Not for: the API plumbing (`friend-invite-reward-builder`, `teleport-hub-builder`) or chat/moderation.

## Inputs (max 2)
1. The core loop (default: `design/core-loop.md`). 2. Typical server size (default: 8-20 players).

## Procedure
1. Name the social job: why would a friend make this loop better? Pick one: shared goal (co-op bonus), competition (leaderboard, race), exchange (trade, gift), showing off (visible progress, base), or rescue (revive). Stop if none fits the loop; add the lightest one anyway.
2. Choose 2-3 hooks from this menu and write the exact moment each fires: invite prompt at a natural high (after a rare drop, a win, a milestone); friend-find on join (see friends online, join-friend); party or team invite from the lobby; spectate for eliminated players; low-risk icebreakers (trade quest, team task with a shared bonus); reserved server slots for friends joining full servers.
3. Reward design: mutual rewards for inviter and invitee, detected with `ReferredByPlayerID` in `PlayerAdded`; Roblox (2026) prefers social-by-design (co-op) over invite-for-reward pop-ups, so make the reward small and the co-op the point.
4. Solo path: the loop must still work alone and on empty servers (AI modes, practice, tasks that count without guests). Remove social gates from the core loop (vault).
5. Safety: no forced contact between strangers, easy mute and block, no trading of items that can scam children without confirmations; hand to `tos-compliance-checker` for chat or trade.
6. Metric: define the proof before building: share of sessions with 2+ friends, D1 of friend-sessions vs solo, invite prompt acceptance rate. These need your own analytics; vault numbers (30 percent, 60 percent) are Roblox-wide, not your game's.
7. Save `design/social.md`; run the doc check.

## Studio MCP path
Design only. After building, `start_stop_play` with multiple clients is not available through MCP; test with Studio's multi-client test mode manually and mark `untested`.

## Fallback
Pure document.

## Evidence
`social-features-and-virality` (invite button is the most important tip per waveshine; about a third of the top 1,000 developers adopted invite prompts; reserved slots improved retention in 2018 data; seed interaction with low-risk icebreakers), `retention-d1-d7` (design for playing with friends), `core-loops-and-game-design` (build social play into the loop but keep solo working), `case-studies-meep-city`, `case-studies-island-royale` (friends list, teleport, team invites: pattern only).

## Output
`design/social.md`: social job, 2-3 hooks with trigger moment and reward, solo path, safety notes, metrics.

## Acceptance checks
- [ ] Each hook has a trigger moment and a reward or reason.
- [ ] A solo and empty-server path is described.
- [ ] A metric with a baseline plan exists for each hook.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/social.md --kind social` prints PASS.
- [ ] Friends are never split into isolated servers; group play earns a bonus and solo players are never penalised; inviter and invitee are both rewarded (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, social-features-and-virality).

## Pitfalls
Invite pop-ups spammed at join. Social gate on the first reward. Trading before an anti-scam design. Assuming platform averages apply to your game.

## Related
`core-loop-designer`, `session-length-designer`, `friend-invite-reward-builder`, `teleport-hub-builder`, `retention-diagnoser`.
