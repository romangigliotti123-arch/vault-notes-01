---
title: "(OLD) Roblox Basic Loadout/Class Selection System (Preset/Custom for each player) - Tutorial #23"
url: https://youtu.be/LjETISdUBp8
creator: Emancyphur
official: false
advice_density: medium
date: 2020-08-19
views: 35221
transcript: auto-captions
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# (OLD) Roblox Basic Loadout/Class Selection System (Preset/Custom for each player) - Tutorial #23

[Watch](https://youtu.be/LjETISdUBp8) | Emancyphur | 35,221 views | 2020-08-19

## Summary
Tutorial building a Roblox loadout/class selection GUI with preset loadouts (level-gated) and customizable primary/secondary slots. Covers scale-based GUI layout, LocalScript button handling with RemoteFunction, server-side validation, cloning tools into backpack on respawn, and storing choices in player StringValues.

## Tips
- [0:39](https://youtu.be/LjETISdUBp8?t=39) **[[ui-ux-design]]** Set frame Size offset to 0 and use only Scale so the GUI scales across phone, tablet and monitor sizes.
- [0:39](https://youtu.be/LjETISdUBp8?t=39) **[[ui-ux-design]]** Enable TextScaled on text labels and buttons so text resizes with the button across devices.
- [12:12](https://youtu.be/LjETISdUBp8?t=732) **[[cross-platform-and-console]]** Use MouseButton1Click-style 'Activated' events instead of mouse-only events so mobile, touch and controller players can click buttons.
- [21:22](https://youtu.be/LjETISdUBp8?t=1282) **[[client-server-and-remotes]]** Use a RemoteFunction (not RemoteEvent) when the server must return a value to the client, e.g. confirming the chosen loadout.
- [29:32](https://youtu.be/LjETISdUBp8?t=1772) **[[client-server-and-remotes]]** Name the RemoteFunction variable differently from the handler function; OnServerInvoke must bind to a separately named function.
- [14:14](https://youtu.be/LjETISdUBp8?t=854) **[[client-server-and-remotes]]** Keep loadout selection on the server so the game knows which items to give when the player spawns.
- [24:06](https://youtu.be/LjETISdUBp8?t=1446) **[[data-persistence]]** Store per-player loadout choices in StringValues inside a player folder for easy inspection; note that this does not persist across sessions without DataStores.
- [37:44](https://youtu.be/LjETISdUBp8?t=2264) **[[combat-and-gameplay-systems]]** Clone tools from ServerStorage into the backpack on respawn, and check the item is not already in the character or backpack to avoid duplicates.
- [44:32](https://youtu.be/LjETISdUBp8?t=2672) **[[combat-and-gameplay-systems]]** Only tools with a child named Handle can be equipped; test items by placing them in StarterPack first to isolate problems.
- [46:35](https://youtu.be/LjETISdUBp8?t=2795) **[[combat-and-gameplay-systems]]** Use greater-than-or-equal checks on level requirements so players at higher levels can still pick lower-tier loadouts.
- [47:17](https://youtu.be/LjETISdUBp8?t=2837) **[[ui-ux-design]]** Disable ResetOnSpawn on the ScreenGui so the selected loadout label does not reset to default on respawn.
- [50:50](https://youtu.be/LjETISdUBp8?t=3050) **[[combat-and-gameplay-systems]]** Gate loadouts by player level via leaderstats; a dictionary mapping item name to required level makes adding tiers easy.
- [52:28](https://youtu.be/LjETISdUBp8?t=3148) **[[ui-ux-design]]** Build category tabs as separate frames and toggle Visible so only one category list shows at a time.
- [1:04:19](https://youtu.be/LjETISdUBp8?t=3859) **[[scripting-and-performance]]** Route the frame's parent name to the server to decide which slot (primary/secondary) an item fills, rather than sending the item alone.
- [1:09:05](https://youtu.be/LjETISdUBp8?t=4145) **[[data-persistence]]** Use DataStores before building saved custom loadouts that persist across sessions and rejoins.
- [14:56](https://youtu.be/LjETISdUBp8?t=896) **[[luau-language-and-types]]** Use GetDescendants with a loop and IsA/is-a-TextButton check to bind one handler to all buttons instead of wiring each one.

## Numbers
- [0:39](https://youtu.be/LjETISdUBp8?t=39) Background border size: **10 px gray border on loadout frame** (Visual styling choice in example GUI)
- [5:29](https://youtu.be/LjETISdUBp8?t=329) Button size scale: **Position 0.1,0 used for button placement** (Scale-based positioning example)
- [1:01:36](https://youtu.be/LjETISdUBp8?t=3696) Example level requirements: **Swordsman level 1, Brick Battler level 5** (Preset loadout level gates in tutorial)

## Games
- **Phantom Forces** [1:08:24](https://youtu.be/LjETISdUBp8?t=4104): Referenced as an example of multi-loadout customization; saved loadouts would need DataStores.

## Tools
Roblox Studio, Explorer, Properties, LocalScript, Script, RemoteFunction

## He points to
- Creator's own tutorial playlist (not named)
- Linked model in video description (not named)

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[cross-platform-and-console]] [[data-persistence]] [[luau-language-and-types]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Emancyphur - How to make successful Roblox games]]
