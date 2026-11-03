---
title: "How to Create PVP and PVE Environments in Roblox Studio"
url: https://youtu.be/i2_7zT36Jeg
creator: SimTek Game Development
official: false
advice_density: medium
date: 2024-10-12
views: 36539
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Create PVP and PVE Environments in Roblox Studio

[Watch](https://youtu.be/i2_7zT36Jeg) | SimTekGameDevelopment | 36,539 views | 2024-10-12

## Summary
Tutorial building a PVP/PVE toggle in Roblox Studio: a client button with cooldown, a RemoteEvent to the server, CollectionService tags for player state, a billboard indicator, and weapon damage gating by tag. Tested with two players in Test Server.

## Tips
- [10:46](https://youtu.be/i2_7zT36Jeg?t=646) **[[combat-and-gameplay-systems]]** Gate damage on the server by checking tags on both shooter and target; only apply damage when both are PVP-tagged, and always damage non-player targets like zombies.
- [6:01](https://youtu.be/i2_7zT36Jeg?t=361) **[[common-mistakes]]** Use a debounce on mode switching during testing (5s), but use a long cooldown in production (~300s, as in WoW) so players can't rapidly toggle to take shots.
- [14:06](https://youtu.be/i2_7zT36Jeg?t=846) **[[client-server-and-remotes]]** Let the client only request a mode change via RemoteEvent; the server should set the state and tags, so clients can't fake their PVP status.
- [15:28](https://youtu.be/i2_7zT36Jeg?t=928) **[[code-architecture-and-frameworks]]** On CharacterAdded, remove all existing mode tags and re-add the default PVE tag so respawns always start in a known state.
- [19:06](https://youtu.be/i2_7zT36Jeg?t=1146) **[[ui-ux-design]]** Show a billboard GUI above PVP-tagged characters so other players can see who is flagged; clone it server-side on tag change and remove it on switch back.
- [27:16](https://youtu.be/i2_7zT36Jeg?t=1636) **[[ui-ux-design]]** Set the toggle button's AnchorPoint so it stays anchored to its corner when the UI is resized across screen sizes.
- [10:46](https://youtu.be/i2_7zT36Jeg?t=646) **[[ui-ux-design]]** Use Activated rather than Activate on UI buttons so the toggle works on mobile as well as PC.

## Numbers
- [6:01](https://youtu.be/i2_7zT36Jeg?t=361) cooldown: **300 seconds** (Suggested production debounce, matching World of Warcraft standard; 5s used only for testing)

## Tools
Roblox Studio, Luau, RemoteEvent, CollectionService, BillboardGui, Creator Store toolbox

## He points to
- Simple pistol weapon (linked in video description)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[ui-ux-design]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
