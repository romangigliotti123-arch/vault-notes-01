---
title: Emancyphur - Studio & Scripting
creator: Emancyphur
tags: [roblox, emancyphur, theme]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Emancyphur: Studio & Scripting

All Emancyphur tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2020-08-02 [0:58](https://youtu.be/ScdTM3ju-yk?t=58) Set Lighting Technology to Future in Properties; players need 5+ graphics bars (or Studio quality level 10+) to see it, others fall back to ShadowMap/Voxel. ([[2020-08-02 - Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & N|Future Is Bright Phase 3 Lighting Guide - Massive ]])
- 2020-08-19 [1:04:19](https://youtu.be/LjETISdUBp8?t=3859) Route the frame's parent name to the server to decide which slot (primary/secondary) an item fills, rather than sending the item alone. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2021-04-23 [18:24](https://youtu.be/DmsbnwtaVi0?t=1104) Use Humanoid:AddAccessory rather than parenting accessories to the character; it ensures the accessory works correctly. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [20:15](https://youtu.be/DmsbnwtaVi0?t=1215) Clone a 'real' accessory from ServerStorage per player so one hat can be granted to many players; check the character doesn't already have it. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [22:22](https://youtu.be/DmsbnwtaVi0?t=1342) Use CollectionService tags to loop over accessories anywhere in the game, so new hats need only be tagged, not moved into a folder. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2022-07-25 [9:28](https://youtu.be/UYnn9JF8qCc?t=568) Bind zones to a group 'EnterOnlyOneZoneAtATime' to stop overlapping zones from fighting over Atmosphere changes. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])
- 2022-07-25 [10:52](https://youtu.be/UYnn9JF8qCc?t=652) Clean up zone connections on removal and disconnect/nil them so removed zones stop listening. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])
- 2022-07-25 [3:30](https://youtu.be/UYnn9JF8qCc?t=210) Run Atmosphere zone changes in a LocalScript for per-player visuals; server changes affect everyone. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])
- 2023-03-08 [0:56](https://youtu.be/lZrfA9Ogv2M?t=56) Read the error's Script path and line number first; the error names the missing child and the parent it was searched in. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])
- 2023-03-08 [2:18](https://youtu.be/lZrfA9Ogv2M?t=138) Check exact spelling and capitalization against Explorer or Properties; Roblox names and properties are case-sensitive (BrickColor, not Brickcolor). ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])
- 2023-03-08 [3:43](https://youtu.be/lZrfA9Ogv2M?t=223) Use the full path through nested folders (e.g. Workspace.Furniture.Table); a search result showing an object elsewhere does not make a dot-path find it. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])
- 2023-03-08 [6:08](https://youtu.be/lZrfA9Ogv2M?t=368) Use :FindFirstChild() with a conditional when an object may not exist yet, so the script does not error immediately. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])
- 2023-03-08 [6:49](https://youtu.be/lZrfA9Ogv2M?t=409) Use :WaitForChild(name, seconds) when you are sure an object will appear; it yields the code below it, so put it in a separate script or reorder if needed. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])

## [[building-art-and-assets]]
- 2014-12-27 [2:21](https://youtu.be/AFY6Yfm-oaw?t=141) Select a model part in Explorer, then use the Rotate tool (blue, yellow, red rings) to pose it; use Move to reposition. ([[2014-12-27 - ROBLOX Studio Tutorial - Modeling Characters & How to find High Qualit|ROBLOX Studio Tutorial - Modeling Characters & How]])
- 2014-12-27 [5:07](https://youtu.be/AFY6Yfm-oaw?t=307) In Toolbox > Models, look for the high-quality badge (circle, triangle, square icon); Roblox hand-picks these as reliable assets. ([[2014-12-27 - ROBLOX Studio Tutorial - Modeling Characters & How to find High Qualit|ROBLOX Studio Tutorial - Modeling Characters & How]])
- 2014-12-27 [5:47](https://youtu.be/AFY6Yfm-oaw?t=347) Test high-quality models in play mode before saving; anchor parts first or they may fall over. ([[2014-12-27 - ROBLOX Studio Tutorial - Modeling Characters & How to find High Qualit|ROBLOX Studio Tutorial - Modeling Characters & How]])
- 2020-08-02 [3:06](https://youtu.be/ScdTM3ju-yk?t=186) Don't rely on SurfaceLight shadows under Future; they are not supported yet, so use SpotLights if shadows matter. ([[2020-08-02 - Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & N|Future Is Bright Phase 3 Lighting Guide - Massive ]])
- 2020-08-02 [4:59](https://youtu.be/ScdTM3ju-yk?t=299) Re-tune lighting for every time of day, especially interiors that relied on few light sources, since Future lighting changes how areas look. ([[2020-08-02 - Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & N|Future Is Bright Phase 3 Lighting Guide - Massive ]])
- 2021-04-23 [0:20](https://youtu.be/DmsbnwtaVi0?t=20) Name the central part of an accessory exactly 'Handle' (capital H); other names won't equip properly on characters. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [2:24](https://youtu.be/DmsbnwtaVi0?t=144) Recreate meshes as MeshPart with copied MeshId and TextureId from SpecialMesh before the 2021 accessory/head change to stay compatible. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [3:46](https://youtu.be/DmsbnwtaVi0?t=226) Pick the most central part of a multi-part model as the Handle so the accessory sits centred on the character's head. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [6:52](https://youtu.be/DmsbnwtaVi0?t=412) Name positioning attachments 'HatAttachment' so the accessory positions identically on both R6 and R15 characters. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [7:34](https://youtu.be/DmsbnwtaVi0?t=454) Weld all accessory parts together; unwelded parts are dropped when the accessory is added to a character, only the Handle transfers. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2021-04-23 [8:15](https://youtu.be/DmsbnwtaVi0?t=495) Weld-button auto-welding only joins intersecting parts; manually add WeldConstraints for the rest or use a welding script. ([[2021-04-23 - Roblox How to make HatsAccessories (from models, parts, & meshes) - Tu|Roblox How to make Hats/Accessories (from models, ]])
- 2022-07-25 [0:00](https://youtu.be/UYnn9JF8qCc?t=0) Add a Skybox to Lighting before adding Atmosphere, otherwise Atmosphere won't work. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])

## [[luau-language-and-types]]
- 2020-08-19 [14:56](https://youtu.be/LjETISdUBp8?t=896) Use GetDescendants with a loop and IsA/is-a-TextButton check to bind one handler to all buttons instead of wiring each one. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])

## [[client-server-and-remotes]]
- 2020-07-10 [2:35](https://youtu.be/7aqTd3PzWWM?t=155) Use a server Script that fires a RemoteEvent to each client on CharacterAdded, since PlayerGui is reset on respawn and must be cleaned again. ([[2020-07-10 - How to FreecamSpectate in your Roblox game (Cinematic Camera) - NEW TU|How to Freecam/Spectate in your Roblox game (Cinem]])
- 2020-07-10 [5:31](https://youtu.be/7aqTd3PzWWM?t=331) Pair the server RemoteEvent with a LocalScript in StarterPlayerScripts that listens via OnClientEvent and removes the Freecam GUI. ([[2020-07-10 - How to FreecamSpectate in your Roblox game (Cinematic Camera) - NEW TU|How to Freecam/Spectate in your Roblox game (Cinem]])
- 2020-08-19 [21:22](https://youtu.be/LjETISdUBp8?t=1282) Use a RemoteFunction (not RemoteEvent) when the server must return a value to the client, e.g. confirming the chosen loadout. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [29:32](https://youtu.be/LjETISdUBp8?t=1772) Name the RemoteFunction variable differently from the handler function; OnServerInvoke must bind to a separately named function. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [14:14](https://youtu.be/LjETISdUBp8?t=854) Keep loadout selection on the server so the game knows which items to give when the player spawns. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2023-03-08 [7:49](https://youtu.be/lZrfA9Ogv2M?t=469) LocalScripts cannot see ServerStorage or ServerScriptService; move shared objects to ReplicatedStorage or Workspace, or move the logic to a server Script. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])
- 2023-03-08 [9:14](https://youtu.be/lZrfA9Ogv2M?t=554) Objects created by one player's LocalScript are visible only to that player; do not update them from server scripts or other clients. ([[2023-03-08 - Fixing X is not a valid member of Y Error - Roblox Scripting Solutions|Fixing "X is not a valid member of Y" Error - Robl]])

## [[anti-exploit-and-security]]
- 2020-07-10 [1:12](https://youtu.be/7aqTd3PzWWM?t=72) Freecam is only usable by game owners/editors, but disable it for all players by destroying the Freecam GUI from PlayerGui on every respawn. ([[2020-07-10 - How to FreecamSpectate in your Roblox game (Cinematic Camera) - NEW TU|How to Freecam/Spectate in your Roblox game (Cinem]])

## [[data-persistence]]
- 2020-08-19 [24:06](https://youtu.be/LjETISdUBp8?t=1446) Store per-player loadout choices in StringValues inside a player folder for easy inspection; note that this does not persist across sessions without DataStores. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [1:09:05](https://youtu.be/LjETISdUBp8?t=4145) Use DataStores before building saved custom loadouts that persist across sessions and rejoins. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])

## [[combat-and-gameplay-systems]]
- 2020-08-19 [37:44](https://youtu.be/LjETISdUBp8?t=2264) Clone tools from ServerStorage into the backpack on respawn, and check the item is not already in the character or backpack to avoid duplicates. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [44:32](https://youtu.be/LjETISdUBp8?t=2672) Only tools with a child named Handle can be equipped; test items by placing them in StarterPack first to isolate problems. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [46:35](https://youtu.be/LjETISdUBp8?t=2795) Use greater-than-or-equal checks on level requirements so players at higher levels can still pick lower-tier loadouts. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [50:50](https://youtu.be/LjETISdUBp8?t=3050) Gate loadouts by player level via leaderstats; a dictionary mapping item name to required level makes adding tiers easy. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])

## [[building-and-level-design]]
- 2020-09-17 [12:39](https://youtu.be/C0ybJ5ghSHk?t=759) Add a sandbox or build mode so players can create their own maps without scripting, extending the game's lifespan. ([[2020-09-17 - The TRUTH of ROBLOX Piggy’s Success & MiniToon’s Rise to Fame|The TRUTH of ROBLOX Piggy’s Success & MiniToon’s R]])
- 2022-07-25 [5:13](https://youtu.be/UYnn9JF8qCc?t=313) For zone parts: Transparency 1, CanCollide off, Anchored on so players walk through invisibly and parts don't fall into the void. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])
- 2022-07-25 [5:54](https://youtu.be/UYnn9JF8qCc?t=354) Store Atmosphere values as Attributes on zone containers, named exactly like Atmosphere properties, so a LocalScript can read them. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])
- 2022-07-25 [6:37](https://youtu.be/UYnn9JF8qCc?t=397) Tune Atmosphere values in Lighting first, then copy the combination into zone Attributes once it looks right. ([[2022-07-25 - Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Dev|Roblox How to use Atmosphere (Create Custom Lighti]])

## [[ui-ux-design]]
- 2014-12-27 [0:59](https://youtu.be/AFY6Yfm-oaw?t=59) Enable Explorer, Properties, Toolbox, Game, Advanced and Command panels via right-click on empty space in Studio's top bar. ([[2014-12-27 - ROBLOX Studio Tutorial - Modeling Characters & How to find High Qualit|ROBLOX Studio Tutorial - Modeling Characters & How]])
- 2020-08-19 [0:39](https://youtu.be/LjETISdUBp8?t=39) Set frame Size offset to 0 and use only Scale so the GUI scales across phone, tablet and monitor sizes. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [0:39](https://youtu.be/LjETISdUBp8?t=39) Enable TextScaled on text labels and buttons so text resizes with the button across devices. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [47:17](https://youtu.be/LjETISdUBp8?t=2837) Disable ResetOnSpawn on the ScreenGui so the selected loadout label does not reset to default on respawn. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-08-19 [52:28](https://youtu.be/LjETISdUBp8?t=3148) Build category tabs as separate frames and toggle Visible so only one category list shows at a time. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])
- 2020-09-17 [4:16](https://youtu.be/C0ybJ5ghSHk?t=256) Add accessibility options such as colorblind mode for puzzle games where players must distinguish similar colored items. ([[2020-09-17 - The TRUTH of ROBLOX Piggy’s Success & MiniToon’s Rise to Fame|The TRUTH of ROBLOX Piggy’s Success & MiniToon’s R]])

## [[optimization-and-streaming]]
- 2020-08-02 [4:15](https://youtu.be/ScdTM3ju-yk?t=255) Expect Future lighting to cost performance; one developer saw menu FPS drop from about 200 to 100. Test on low-end PCs and mobile. ([[2020-08-02 - Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & N|Future Is Bright Phase 3 Lighting Guide - Massive ]])
- 2020-08-02 [4:15](https://youtu.be/ScdTM3ju-yk?t=255) Prefer shadowed SpotLights over shadowed PointLights; the staff note says shadowed PointLights cost more performance. ([[2020-08-02 - Future Is Bright Phase 3 Lighting Guide - Massive Lighting Changes & N|Future Is Bright Phase 3 Lighting Guide - Massive ]])

## [[cross-platform-and-console]]
- 2020-08-19 [12:12](https://youtu.be/LjETISdUBp8?t=732) Use MouseButton1Click-style 'Activated' events instead of mouse-only events so mobile, touch and controller players can click buttons. ([[2020-08-19 - (OLD) Roblox Basic LoadoutClass Selection System (PresetCustom for eac|(OLD) Roblox Basic Loadout/Class Selection System ]])

Up: [[Emancyphur - How to make successful Roblox games]]
