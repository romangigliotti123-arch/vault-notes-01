---
title: NotCumin - Studio & Scripting
creator: NotCumin
tags: [roblox, notcumin, theme]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# NotCumin: Studio & Scripting

All NotCumin tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2025-12-23 [20:45](https://youtu.be/hQpC_UHxJDU?t=1245) Ensure enemy attack hitboxes end when the animation ends. Lingering hitboxes causing damage after attacks stop feel amateur and unfair. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])

## [[client-server-and-remotes]]
- 2025-12-23 [21:27](https://youtu.be/hQpC_UHxJDU?t=1287) Account for server-side timing windows for parries and dodges so valid inputs register. Otherwise players see parries fail with no reason. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])

## [[matchmaking-and-teleport]]
- 2025-06-08 [3:15](https://youtu.be/Z1tj1OPOEZg?t=195) Keep server population healthy; with only two servers per region, high ping and empty lobbies drive players away. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-07-31 [13:59](https://youtu.be/jXogdTgtlXE?t=839) Use per-mission queues or lobbies for group PvE content instead of drop-in servers, so players don't abandon a run when others leave. ([[2025-07-31 - No, Get Good doesn't excuse bad Roblox games|No, "Get Good" doesn't excuse bad Roblox games.]])
- 2025-12-23 [22:08](https://youtu.be/hQpC_UHxJDU?t=1328) Let players create a dungeon room with a chosen dungeon and difficulty that others can join. Requiring invites makes multiplayer hard to start. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2026-09-13 [4:47](https://youtu.be/kjLtxvB_iyk?t=287) Add level-bracketed lobbies (e.g. level 1+, 30+, 60+) so players find teammates of similar skill instead of one mixed server pool. ([[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]])
- 2026-09-13 [5:28](https://youtu.be/kjLtxvB_iyk?t=328) Offer a quick-queue: send players to a bare queue server and teleport the group to the dungeon once enough players are gathered. ([[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]])
- 2026-09-13 [5:28](https://youtu.be/kjLtxvB_iyk?t=328) For robust matchmaking, let servers message each other across servers (e.g. via MessagingService or a library like Muster) to search for groups; this is significant work. ([[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]])

## [[combat-and-gameplay-systems]]
- 2025-05-11 [5:47](https://youtu.be/2auVezIcNAE?t=347) Give enemies varied behaviour beyond walk-in-a-straight-line-and-attack; the speaker criticises bare-bones enemy AI in bandit-beater RPGs. ([[2025-05-11 - The Sad State of Modern Roblox RPGs|The Sad State of Modern Roblox RPGs...]])
- 2025-05-11 [10:20](https://youtu.be/2auVezIcNAE?t=620) Make boss fights last longer than a minute or two and make boss attacks match their fiction, as the speaker says BlockTales bosses were too short. ([[2025-05-11 - The Sad State of Modern Roblox RPGs|The Sad State of Modern Roblox RPGs...]])
- 2025-05-11 [14:09](https://youtu.be/2auVezIcNAE?t=849) Make gear progression meaningful; the speaker says random gear perks were ignored and higher-number gear simply outclassed previous tiers. ([[2025-05-11 - The Sad State of Modern Roblox RPGs|The Sad State of Modern Roblox RPGs...]])
- 2025-12-23 [12:38](https://youtu.be/hQpC_UHxJDU?t=758) Add input buffering so a block or action held during an attack executes once the animation ends. Without it, precise timing feels awful. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [20:05](https://youtu.be/hQpC_UHxJDU?t=1205) Give dodge dashes i-frames tied to stamina. Pixel Blade's dash was praised as more useful than parries. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [4:36](https://youtu.be/hQpC_UHxJDU?t=276) Design enemies that give players a sense of power. Bosses that kill quickly while the player deals tickle damage kill engagement. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2026-02-07 [11:30](https://youtu.be/ROo_Xpms4ok?t=690) Tune resource systems so they matter. Near-infinite stamina regen and rare ammo make dash, push and ranged combat feel pointless. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])
- 2026-02-07 [12:52](https://youtu.be/ROo_Xpms4ok?t=772) Don't make optional objectives consume slots needed for core survival items. Carrying them blocked healing and made the secondary objective impossible solo. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])

## [[building-and-level-design]]
- 2025-06-08 [4:21](https://youtu.be/Z1tj1OPOEZg?t=261) Don't pad levels with long empty travel between objectives; a straight walk with nothing to do kills engagement. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-06-08 [7:50](https://youtu.be/Z1tj1OPOEZg?t=470) Make doors match collision; ghost doors you phase through confuse players and break immersion in modern high-fidelity games. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-12-23 [14:01](https://youtu.be/hQpC_UHxJDU?t=841) Place fast-travel points before every major boss and across large maps. Making players walk back after death is a major frustration. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [14:43](https://youtu.be/hQpC_UHxJDU?t=883) Avoid excessive fog that hides the map. Players lose their sense of direction, especially without objective markers. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [13:20](https://youtu.be/hQpC_UHxJDU?t=800) Make the world denser rather than sprawling. Large empty spaces with few NPCs or useful content feel like wasted time. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [26:29](https://youtu.be/hQpC_UHxJDU?t=1589) Guide players toward key progression items rather than hiding them in random chests. Leaving them undiscoverable makes progression feel arbitrary. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2026-02-07 [10:09](https://youtu.be/ROo_Xpms4ok?t=609) Mark objective locations clearly on screen, such as a marker for the keep. Players should know where to go. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])
- 2026-02-07 [8:06](https://youtu.be/ROo_Xpms4ok?t=486) Don't fill the hub with decorative props that do nothing. Empty big hubs and non-functional training dummies feel unfinished. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])

## [[ui-ux-design]]
- 2025-06-08 [9:22](https://youtu.be/Z1tj1OPOEZg?t=562) Make it clear where vehicles/mounts are kept and add a visible pickup prompt; hidden horses cost players minutes. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-06-08 [13:15](https://youtu.be/Z1tj1OPOEZg?t=795) Auto-reload or single-button reload for consumable weapons; manual multi-step loading is frustrating and easy to forget. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-06-08 [13:56](https://youtu.be/Z1tj1OPOEZg?t=836) Show clear HUD warnings for durability or ammo running out, with sound cues, so players aren't surprised mid-fight. ([[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]])
- 2025-12-23 [28:30](https://youtu.be/hQpC_UHxJDU?t=1710) Show a Coming Soon sign for unfinished features instead of an NPC error. Players who skip patch notes otherwise get confused. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2025-12-23 [27:10](https://youtu.be/hQpC_UHxJDU?t=1630) Have NPCs and quest-givers do useful things. Filler NPCs with no reason to exist make the world feel empty. ([[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]])
- 2026-02-07 [8:06](https://youtu.be/ROo_Xpms4ok?t=486) Use consistent, discoverable access for menus. Mixing glowing circles, keybinds and randomly placed stands with no signage hides the upgrade menu. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])
- 2026-02-07 [8:47](https://youtu.be/ROo_Xpms4ok?t=527) Show crafting materials in the inventory. Players expect to check their resources there and will be confused without them. ([[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]])
- 2026-09-13 [7:30](https://youtu.be/kjLtxvB_iyk?t=450) Show full ability stats in descriptions: hit count, cooldown, and exact scaling ratio, not vague phrases like 'scales with spell power'. ([[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]])
- 2026-09-13 [8:11](https://youtu.be/kjLtxvB_iyk?t=491) Let players upgrade equipped gear without unequipping it first; forced unequips feel lazy and add friction. ([[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]])

Up: [[NotCumin - How to make successful Roblox games]]
