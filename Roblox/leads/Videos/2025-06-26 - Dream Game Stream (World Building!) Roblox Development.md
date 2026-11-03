---
title: "Dream Game Stream (World Building!) | Roblox Development"
url: https://youtu.be/krMTcTvaj_8
creator: RoBuilder
official: false
advice_density: medium
date: 2025-06-26
views: 4681
transcript: auto-captions
confidence: medium
tags: [roblox, leads, youtube-learn]
---

# Dream Game Stream (World Building!) | Roblox Development

[Watch](https://youtu.be/krMTcTvaj_8) | leads | 4,681 views | 2025-06-26

## Summary
Livestream building a motorcycle stunt game (Chicago-based, "My Bike Life"-style) in Roblox Studio. Covers terrain mountain work, rebuilding the map at larger scale, designing a stunt park with podiums, gazebo modeling in Blender, grass/sidewalk/color choices, and the developer's hiring needs (bike system scripter, terrain artist, vector art).

## Tips
- [0:53](https://youtu.be/krMTcTvaj_8?t=53) **[[building-art-and-assets]]** Use reference images when building; the streamer calls them the key tip for newer builders.
- [2:57](https://youtu.be/krMTcTvaj_8?t=177) **[[building-and-level-design]]** Delete temporary blocking-out walls once the real city shape is established, so they don't clutter the map.
- [5:54](https://youtu.be/krMTcTvaj_8?t=354) **[[building-and-level-design]]** Round off terrain edges by rendering the Archimedes shape multiple times to fold it back and avoid hard cutoffs; add variation in sizes.
- [12:57](https://youtu.be/krMTcTvaj_8?t=777) **[[building-and-level-design]]** Size parts only as big as needed; oversized parts can fail to convert to Terrain, so check part size before converting.
- [16:29](https://youtu.be/krMTcTvaj_8?t=989) **[[community-and-discord]]** Make devlogs but keep them unlisted until release, then publish a batch linking the game, so comments aren't filled with 'where is the game' impatience.
- [21:23](https://youtu.be/krMTcTvaj_8?t=1283) **[[building-and-level-design]]** Break up flat walls with structure and depth (gazebos, pavilions, uneven shapes), not just graffiti or gradients.
- [35:15](https://youtu.be/krMTcTvaj_8?t=2115) **[[building-and-level-design]]** Make parking lots flush with the road and add steps up to buildings, since real layouts don't put lots on hills.
- [38:55](https://youtu.be/krMTcTvaj_8?t=2335) **[[optimization-and-streaming]]** Enable StreamingEnabled and occlusion culling so buildings and terrain behind walls aren't rendered, especially on large maps.
- [39:37](https://youtu.be/krMTcTvaj_8?t=2377) **[[ai-and-tools]]** Use Studio folders rather than groups for organising instances.
- [43:11](https://youtu.be/krMTcTvaj_8?t=2591) **[[building-art-and-assets]]** Model props in Blender and build layouts in Studio; import props into Studio from Blender rather than round-tripping back.
- [1:08:35](https://youtu.be/krMTcTvaj_8?t=4115) **[[building-and-level-design]]** Avoid perfect symmetry in layouts; add slight variation so the environment looks natural.
- [1:20:59](https://youtu.be/krMTcTvaj_8?t=4859) **[[optimization-and-streaming]]** Double-sided meshes do not measurably hurt performance in the streamer's tests; don't prioritise removing them.
- [1:54:29](https://youtu.be/krMTcTvaj_8?t=6869) **[[optimization-and-streaming]]** Importing Studio models into Blender and back is not more optimised; it triangulates geometry and duplicates items.
- [1:58:00](https://youtu.be/krMTcTvaj_8?t=7080) **[[building-and-level-design]]** Smooth terrain under and around roads too, because roads need terrain underneath them.
- [2:00:47](https://youtu.be/krMTcTvaj_8?t=7247) **[[building-art-and-assets]]** For repeating parking-line markings, use a stretchable texture with one line on the canvas edge instead of a plugin.
- [2:00:47](https://youtu.be/krMTcTvaj_8?t=7247) **[[building-art-and-assets]]** Use unions for flat floor pieces to hide Z-fighting; collision issues are unlikely on floor-level geometry.
- [1:37:36](https://youtu.be/krMTcTvaj_8?t=5856) **[[building-and-level-design]]** Set snap-to-grid and move increments deliberately; inconsistent stud steps from snapping cause uneven stairs.
- [1:58:41](https://youtu.be/krMTcTvaj_8?t=7121) **[[team-and-budget]]** Identify the bottleneck roles early (bike system scripter, terrain artist, custom vector art) and hire for them rather than waiting on one person.
- [1:43:15](https://youtu.be/krMTcTvaj_8?t=6195) **[[analytics-metrics]]** Set a realistic CCU target for niche games; the streamer targets roughly 300-500 players for a niche motorcycle game.

## Numbers
- [1:23:51](https://youtu.be/krMTcTvaj_8?t=5031) Map size comparison: **Old map ~12 base plates (2x6); new map ~24 base plates; podium area 3x4 old vs 5x5 new** (Streamer's own estimate of the map size change)
- [1:43:15](https://youtu.be/krMTcTvaj_8?t=6195) Target player count: **300-500 players** (Streamer's stated goal for a niche motorcycle stunt game)
- [1:51:43](https://youtu.be/krMTcTvaj_8?t=6703) Comparable game daily players: **40-60 daily players** (Streamer's estimate for a similar motorcycle game with no real mechanics (Funding Dream Game testing place))

## Games
- **Funding Dream Game testing place** [1:51:43](https://youtu.be/krMTcTvaj_8?t=6703): Mentioned as a motorcycle game averaging about 40-60 daily players despite having few mechanics, as a benchmark.
- **Stunt Showdown (in-stream reference)** [29:18](https://youtu.be/krMTcTvaj_8?t=1758): Timed stunt-score event with first, second and third podium placings used as a central hub feature.

## Tools
Roblox Studio, Blender, Photoshop, OBS, concentration lines plugin, grass fixer plugin, cast shadow optimizer (mentioned)

## He points to
- Concentration lines plugin (zoom effect)
- Free optimisation plugin (streamer says it will be free soon, video planned)

## Quotes
- [16:29](https://youtu.be/krMTcTvaj_8?t=989) "I think you should make devlogs, but don't publish any of them until the game comes out."
- [1:08:35](https://youtu.be/krMTcTvaj_8?t=4115) "Symmetry kills games... nothing in the real world is symmetrical."
- [1:20:59](https://youtu.be/krMTcTvaj_8?t=4859) "Doublesided does not actually affect a game's performance."

## Topics
[[ai-and-tools]] [[analytics-metrics]] [[building-and-level-design]] [[building-art-and-assets]] [[community-and-discord]] [[optimization-and-streaming]] [[team-and-budget]]

Back to [[leads - How to make successful Roblox games]]
