---
title: "Will emissive maps finally put an end to lighting hacks? — Beyond The Blox"
url: https://youtu.be/KNHngRRMPVI
creator: Last Level Studios
official: false
advice_density: low
date: 2025-11-05
views: 13105
transcript: manual-subs
confidence: high
tags: [roblox, lastlevelstudios, youtube-learn]
creator_trust: MIXED
creator_score: 5.5
---

> [!note] Trust: MIXED (credibility audit score 5.5): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Will emissive maps finally put an end to lighting hacks? — Beyond The Blox

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/KNHngRRMPVI) | LastLevelStudios | 13,105 views | 2025-11-05

## Summary
Beyond The Blox news episode (Nov 2025) covering Studio Beta emissive maps (glow textures with strength and tint, all quality levels and distances), SLIM auto-generated LOD model variants, EuroJam 2025 game jam, a new safety analytics dashboard in developer analytics, and age-estimation chat gating. Mostly news, little actionable advice.

## Tips
- [4:42](https://youtu.be/KNHngRRMPVI?t=282) **[[roblox-platform-changes]]** Emissive maps appear at all graphics quality levels and distances, so hidden-in-grass or quality-dependent visuals are no longer a risk; test lighting at low graphics settings too.
- [6:46](https://youtu.be/KNHngRRMPVI?t=406) **[[vfx-and-particles]]** Use emissive mask texture for glow areas, emissive strength (0 to ~40 suggested) for intensity, and emissive tint for colour; replaces old export-twice neon hacks.
- [11:16](https://youtu.be/KNHngRRMPVI?t=676) **[[optimization-and-streaming]]** Use SLIM (Studio Beta) for large worlds: Roblox auto-generates lower-fidelity variants by distance; verify with a Highlight in Workspace to see which geometry is SLIM.
- [12:42](https://youtu.be/KNHngRRMPVI?t=762) **[[optimization-and-streaming]]** SLIM has known issues (Z-fighting, corroded metal material, UV map problems); test these on your assets before relying on it in production.

## Numbers
- [4:42](https://youtu.be/KNHngRRMPVI?t=282) Emissive strength range: **0 to 40 suggested** (Emissive map strength property per Roblox example)
- [16:32](https://youtu.be/KNHngRRMPVI?t=992) EuroJam 2025 duration: **10 days, Oct 31 to Nov 9, teams up to 5** (European Roblox game jam, rebranded UNITE Developer Challenge)
- [23:08](https://youtu.be/KNHngRRMPVI?t=1388) Abuse report benchmark: **90th percentile comparison** (Safety dashboard compares game report levels to other games)
- [8:27](https://youtu.be/KNHngRRMPVI?t=507) Place file size limit: **100 MB** (Place file size limit cited as issue SLIM may help with)

## Games
- **99 Nights in the Forest** [15:49](https://youtu.be/KNHngRRMPVI?t=949): Stable ~1-2M concurrent players across the week, suggesting steady retention rather than just high peaks.
- **Grow a Garden** [15:49](https://youtu.be/KNHngRRMPVI?t=949): Very high peak players; cited as a top-visited Roblox game candidate.
- **Steal a Brainrot** [15:49](https://youtu.be/KNHngRRMPVI?t=949): Very high peak players, cited alongside Grow a Garden.

## Tools
Roblox Studio, Roblox Highlight (in Workspace), Persona (age verification partner)

## Topics
[[analytics-metrics]] [[events-and-seasonal-content]] [[optimization-and-streaming]] [[roblox-platform-changes]] [[vfx-and-particles]]

Back to [[LastLevelStudios - How to make successful Roblox games]]
