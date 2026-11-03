---
title: leads - Studio & Scripting
creator: leads
tags: [roblox, leads, theme]
---

# leads: Studio & Scripting

All leads tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2025-05-23 [2:39](https://youtu.be/Gw2FwndwnOg?t=159) Test physical item interactions early; Dev 2's dropped pickaxe was lost, so validate that tools and placed objects persist and can be recovered. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])

## [[building-art-and-assets]]
- 2025-05-23 [11:32](https://youtu.be/Gw2FwndwnOg?t=692) Generate reference images in an AI image tool, then image-to-3D, then remesh to a low poly count before importing to Roblox; drop the texture and retexture in Studio. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])
- 2025-05-23 [7:02](https://youtu.be/Gw2FwndwnOg?t=422) Check map generic-ness early; Dev 4 noted the map looked generic and changed the setting to fit the theme. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])
- 2025-06-26 [0:53](https://youtu.be/krMTcTvaj_8?t=53) Use reference images when building; the streamer calls them the key tip for newer builders. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [43:11](https://youtu.be/krMTcTvaj_8?t=2591) Model props in Blender and build layouts in Studio; import props into Studio from Blender rather than round-tripping back. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [2:00:47](https://youtu.be/krMTcTvaj_8?t=7247) For repeating parking-line markings, use a stretchable texture with one line on the canvas edge instead of a plugin. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [2:00:47](https://youtu.be/krMTcTvaj_8?t=7247) Use unions for flat floor pieces to hide Z-fighting; collision issues are unlikely on floor-level geometry. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2026-03-18 [0:29](https://youtu.be/k3id70yCMRY?t=29) Mix exponential-in and exponential-out easing: move object halfway with exponential in, then copy the frame and finish with exponential out for smoother motion. ([[2026-03-18 - My Movie Tutorial For Beginners Roblox|My Movie Tutorial For Beginners | Roblox]])
- 2026-03-18 [4:53](https://youtu.be/k3id70yCMRY?t=293) Custom decals must be 800x800 px with transparent background; upload via Creations > Development Items > Decals, then paste the asset ID into My Movie's search. ([[2026-03-18 - My Movie Tutorial For Beginners Roblox|My Movie Tutorial For Beginners | Roblox]])

## [[ai-and-tools]]
- 2025-06-26 [39:37](https://youtu.be/krMTcTvaj_8?t=2377) Use Studio folders rather than groups for organising instances. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2026-10-17 [2:24](https://youtu.be/ltbZzXRrDF8?t=144) Write a detailed master prompt covering map, systems, persistence, offline earnings, and mobile controls; the more detail, the better the AI build. ([[2026-10-17 - How To Make An ENTIRE Roblox Game With AI - Full Guide|How To Make An ENTIRE Roblox Game With AI - Full G]])
- 2026-10-17 [2:24](https://youtu.be/ltbZzXRrDF8?t=144) Back up the place before letting the AI edit an existing project, since it modifies the game directly. ([[2026-10-17 - How To Make An ENTIRE Roblox Game With AI - Full Guide|How To Make An ENTIRE Roblox Game With AI - Full G]])
- 2026-10-17 [3:45](https://youtu.be/ltbZzXRrDF8?t=225) Use a higher effort level (extra high) for complex whole-game generation; keep medium for simple queries. ([[2026-10-17 - How To Make An ENTIRE Roblox Game With AI - Full Guide|How To Make An ENTIRE Roblox Game With AI - Full G]])
- 2026-10-17 [1:11](https://youtu.be/ltbZzXRrDF8?t=71) Enable Studio as MCP server and ChatGPT Codex under Quick Connect in the Assistant settings; verify by asking it to identify the open project. ([[2026-10-17 - How To Make An ENTIRE Roblox Game With AI - Full Guide|How To Make An ENTIRE Roblox Game With AI - Full G]])
- 2026-10-23 [1:35](https://youtu.be/OfObWnrucRY?t=95) Give the AI reference images with prompts so it has visuals to match; the speaker said this made the output far closer to the intended look. ([[2026-10-23 - Building a Viral Roblox Game with AI FULL PROCESS|Building a Viral Roblox Game with AI [FULL PROCESS]])

## [[code-architecture-and-frameworks]]
- 2023-04-02 [0:28](https://youtu.be/H6LsbS_SA2w?t=28) Put the leaderstats-creating script in ServerScriptService so it runs on the server and sets up currency for every joining player. ([[2023-04-02 - HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Studio Tutorial|HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Stu]])

## [[combat-and-gameplay-systems]]
- 2018-05-27 [2:43](https://youtu.be/8X4fx-YncqA?t=163) Split every attack into anticipation, contact and recovery frames; anticipation mostly sets attack speed, and it is when the player is most vulnerable. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [3:28](https://youtu.be/8X4fx-YncqA?t=208) Decide whether attacks can be cancelled mid-animation; cancelling makes play free-flowing but enemies become more aggressive, while no cancelling makes play deliberate. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [5:30](https://youtu.be/8X4fx-YncqA?t=330) Give each move a distinct niche with minimal overlap, and give every attack a disadvantage such as slowness, vulnerability, resource cost or cooldown. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [6:19](https://youtu.be/8X4fx-YncqA?t=379) Get many moves from one attack button using hold for charge and directional input, rather than putting attacks on every button. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [7:02](https://youtu.be/8X4fx-YncqA?t=422) For casual players, reward pressing attack right as the previous hit lands instead of requiring memorised combo sequences. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [8:20](https://youtu.be/8X4fx-YncqA?t=500) Make parries risky by setting a narrow parry window and punishing mistimed parries or dodges with long vulnerable recovery. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [9:46](https://youtu.be/8X4fx-YncqA?t=586) Don't let parries be instant kills; use a stun or slow-mo reward so the player still needs the full combat system to finish enemies. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [10:11](https://youtu.be/8X4fx-YncqA?t=611) Prevent stun-locking with poise or super armour that resists stagger until enough damage is dealt, stamina limits, multiple attackers, or uninterruptible attacks. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [11:27](https://youtu.be/8X4fx-YncqA?t=687) Design enemies with distinct silhouettes and colours, exaggerated wind-up animations and clear telegraphs (sound or visual glints) so players can read incoming attacks. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [12:08](https://youtu.be/8X4fx-YncqA?t=728) Avoid enemies that only die to one specific move; that collapses the move set into one dominant strategy. Use resistant enemies to force varied moves instead. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2018-05-27 [13:34](https://youtu.be/8X4fx-YncqA?t=814) Consider enemies that adapt to repeated player moves so the player must vary tactics. ([[2018-05-27 - What Makes a Good Combat System|What Makes a Good Combat System?]])
- 2023-03-31 [4:34](https://youtu.be/bYyD6tyz6Dg?t=274) Give each status effect a clear gameplay logic tied to its theme, e.g. shock causes missed attacks, chill reduces armor, making effects easy to understand. ([[2023-03-31 - Stat System Design - Creating Rpg Game|Stat System Design - Creating Rpg Game]])
- 2023-04-02 [1:44](https://youtu.be/H6LsbS_SA2w?t=104) Anchor the coin part and add a Script inside it; the script handles the touch pickup, currency award, and respawn timer. ([[2023-04-02 - HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Studio Tutorial|HOW TO MAKE A PART GIVE YOU CURRENCY 🛠️ Roblox Stu]])
- 2025-05-23 [10:51](https://youtu.be/Gw2FwndwnOg?t=651) Prevent soft-locks: a player who can lose all money must still be able to play; add a recovery path. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])
- 2025-05-23 [10:51](https://youtu.be/Gw2FwndwnOg?t=651) Give shops stock limits; infinite stock feels idle and removes scarcity. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])

## [[building-and-level-design]]
- 2025-06-26 [2:57](https://youtu.be/krMTcTvaj_8?t=177) Delete temporary blocking-out walls once the real city shape is established, so they don't clutter the map. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [5:54](https://youtu.be/krMTcTvaj_8?t=354) Round off terrain edges by rendering the Archimedes shape multiple times to fold it back and avoid hard cutoffs; add variation in sizes. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [12:57](https://youtu.be/krMTcTvaj_8?t=777) Size parts only as big as needed; oversized parts can fail to convert to Terrain, so check part size before converting. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [21:23](https://youtu.be/krMTcTvaj_8?t=1283) Break up flat walls with structure and depth (gazebos, pavilions, uneven shapes), not just graffiti or gradients. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [35:15](https://youtu.be/krMTcTvaj_8?t=2115) Make parking lots flush with the road and add steps up to buildings, since real layouts don't put lots on hills. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [1:08:35](https://youtu.be/krMTcTvaj_8?t=4115) Avoid perfect symmetry in layouts; add slight variation so the environment looks natural. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [1:58:00](https://youtu.be/krMTcTvaj_8?t=7080) Smooth terrain under and around roads too, because roads need terrain underneath them. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [1:37:36](https://youtu.be/krMTcTvaj_8?t=5856) Set snap-to-grid and move increments deliberately; inconsistent stud steps from snapping cause uneven stairs. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])

## [[3d-modeling-rigging-and-animation]]
- 2026-03-18 [1:20](https://youtu.be/k3id70yCMRY?t=80) Move the far-side arm back on the lowest layer to make a character look like it's turning to punch; perspective sells the motion. ([[2026-03-18 - My Movie Tutorial For Beginners Roblox|My Movie Tutorial For Beginners | Roblox]])

## [[vfx-and-particles]]
- 2026-03-18 [2:04](https://youtu.be/k3id70yCMRY?t=124) Add a short (~0.5s) effect like a wind layer under the punching limb, fading out with exponential-out easing, to add polish. ([[2026-03-18 - My Movie Tutorial For Beginners Roblox|My Movie Tutorial For Beginners | Roblox]])
- 2026-03-18 [2:45](https://youtu.be/k3id70yCMRY?t=165) Build impact frames: add a white circle at the hit point, animated wavy lines crossing the frame, and a full-screen white square that fades out (exponential or smooth out). ([[2026-03-18 - My Movie Tutorial For Beginners Roblox|My Movie Tutorial For Beginners | Roblox]])

## [[ui-ux-design]]
- 2022-06-11 [26:01](https://youtu.be/Mep4_w8qxeE?t=1561) Test controls and layout on paper first. Around 66-67% of Roblox players are on mobile, and control design makes or breaks success. ([[2022-06-11 - (ENGLISH) Core Loops and Prototyping by Roblox Level Up Connect 2022|(ENGLISH) Core Loops and Prototyping by Roblox Lev]])
- 2025-05-23 [3:20](https://youtu.be/Gw2FwndwnOg?t=200) Add polish cheaply: fading text on currency change and hover/press feedback on buttons make UI feel responsive. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])
- 2025-05-23 [5:16](https://youtu.be/Gw2FwndwnOg?t=316) Rebuild a bad UI rather than patching it; Dev 3 found the existing UI poor and restyled it for consistency. ([[2025-05-23 - Can 6 DEVS Make GROW A GARDEN Without Communicating|Can 6 DEVS Make GROW A GARDEN Without Communicatin]])

## [[optimization-and-streaming]]
- 2025-06-26 [38:55](https://youtu.be/krMTcTvaj_8?t=2335) Enable StreamingEnabled and occlusion culling so buildings and terrain behind walls aren't rendered, especially on large maps. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [1:20:59](https://youtu.be/krMTcTvaj_8?t=4859) Double-sided meshes do not measurably hurt performance in the streamer's tests; don't prioritise removing them. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])
- 2025-06-26 [1:54:29](https://youtu.be/krMTcTvaj_8?t=6869) Importing Studio models into Blender and back is not more optimised; it triangulates geometry and duplicates items. ([[2025-06-26 - Dream Game Stream (World Building!) Roblox Development|Dream Game Stream (World Building!) | Roblox Devel]])

## [[cross-platform-and-console]]
- 2026-10-17 [7:38](https://youtu.be/ltbZzXRrDF8?t=458) Test on mobile: check buttons are easy to tap, UI is readable, and performance is smooth, since many players use phones. ([[2026-10-17 - How To Make An ENTIRE Roblox Game With AI - Full Guide|How To Make An ENTIRE Roblox Game With AI - Full G]])

Up: [[leads - How to make successful Roblox games]]
