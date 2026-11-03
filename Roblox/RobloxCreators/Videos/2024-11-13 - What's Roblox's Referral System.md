---
title: "What's Roblox's Referral System?"
url: https://youtu.be/qfWKYgO63OI
creator: Roblox Creators
official: true
advice_density: medium
date: 2024-11-13
views: 82980
transcript: manual-subs
confidence: high
tags: [roblox, robloxcreators, youtube-learn]
---

# What's Roblox's Referral System?

[Watch](https://youtu.be/qfWKYgO63OI) | RobloxCreators | 82,980 views | 2024-11-13

## Summary
Explains Roblox's referral system: players get unique referral links, and inviter, invitee, or both receive in-experience rewards when referral criteria are met. Covers RemoteEvent setup, checking ReferredByPlayerID in PlayerAdded, and anti-exploit measures.

## Tips
- [1:00](https://youtu.be/qfWKYgO63OI?t=60) **[[scripting-and-performance]]** Set up a RemoteEvent in ReplicatedStorage so the server can notify the client when a player joins via a referral link.
- [1:00](https://youtu.be/qfWKYgO63OI?t=60) **[[social-features-and-virality]]** Check ReferredByPlayerID in the PlayerAdded handler to detect referred joins and read the inviter's userID.
- [0:26](https://youtu.be/qfWKYgO63OI?t=26) **[[social-features-and-virality]]** Reward both inviter and invitee; mutual rewards build community and encourage players to share the game organically.
- [0:26](https://youtu.be/qfWKYgO63OI?t=26) **[[retention-d1-d7]]** Use referral rewards to bring existing players back and bring in new players, boosting retention and engagement.
- [2:02](https://youtu.be/qfWKYgO63OI?t=122) **[[common-mistakes]]** Prevent exploits: let each invitee reward a referrer only once, and track who has already been invited.
- [2:02](https://youtu.be/qfWKYgO63OI?t=122) **[[common-mistakes]]** Add a cooldown before the same player can submit another referral to block repeated invite-link abuse.
- [2:02](https://youtu.be/qfWKYgO63OI?t=122) **[[common-mistakes]]** Monitor for groups of players repeatedly inviting each other; ban abusers or nullify their rewards.

## Tools
RemoteEvent, ReplicatedStorage, PlayerAdded, ReferredByPlayerID

## He points to
- Uncopylocked sample experience (rewards diamond currency with DataStore), linked in video description
- Roblox documentation on preventing multiple uses of the same referral

## Topics
[[common-mistakes]] [[retention-d1-d7]] [[scripting-and-performance]] [[social-features-and-virality]]

Back to [[RobloxCreators - How to make successful Roblox games]]
