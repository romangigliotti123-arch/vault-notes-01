---
type: research-source
id: yt-qcceynPZOrg
title: "Blender SURVEY 2025! — Blender Today LIVE #268"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=qcceynPZOrg"
published: "2025-10-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0050
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-qcceynPZOrg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Weekly Blender Today livestream (Oct 28, 2025) covering the Blender 2025 survey, newsletter plans, Blender 5.0 beta/release timing, 5.1 changes (compositor radial tiling node, sequencer strip-info node, timeline return, Python 3.13 and other library upgrades) and UI/mesh fixes. Nothing on Roblox, Claude, blender-mcp, or the Roblox export pipeline.

## Claims
- c1: [15:52] Blender 5.0 release scheduled for 11 November 2025; beta switch had been delayed one week. *(doc, high; other)*
- c2: [25:26] Blender 5.1 development uses upcoming library upgrades including Python 3.13 and NumPy, plus OpenXR and ThorVG proposals. *(doc, medium; other)*
- c3: [42:38] Built-in startup.blend is now compressed, dropping from about 800 KB to roughly 100 KB; compression is on by default for saves in 5.0. *(doc, high; other)*
- c4: [6:43] Speaker proposed a script that opens Blender per version and saves screenshots via the built-in screenshot operator to regenerate website images; described as a dream, not implemented. *(opinion, low; automation-and-creator-workflows)*
- c5: [31:18] Mesh validation rewritten; 1M-vertex cube check dropped from 200 ms to 92 ms, with 1,300 lines removed and 900 added. *(data, high; other)*
- c6: [39:10] Blender updater notification for new releases proposed as a 2026 project, aimed mainly at LTS users. *(doc, low; automation-and-creator-workflows)*
- c7: [17:13] Sequencer compositor gains a Strip Info node (community contributor) enabling strip-time-driven effects like fade in/out; the compositor modifier is CPU-only for now. *(demo, medium; other)*
- c8: [1:02:31] Uuk Paint add-on, installable from the Blender extensions platform, was suggested as the closest option to Substance-style texture painting. *(opinion, low; other)*

## Numbers
- n1: **Blender 5.0 release date**: 11 Nov 2025 Two weeks after stream; beta switch delayed one week
- n2: **Mesh validation speed (1M-vertex cube)**: 200 ms -> 92 ms Rewritten validation split into individual functions
- n3: **startup.blend size**: ~800 KB -> ~100 KB After enabling compression
- n4: **AMD HIP Windows driver minimum**: Adrenalin 24.6 -> 24.9.1; ProRender Q2 -> Q4 Cycles minimum driver version change for 5.x
- n5: **Planned newsletter emails**: about 5 per year Only for major releases, survey, and year-end campaign
- n6: **First newsletter batch**: about 10,000 random Blender IDs Test email sent before full rollout

## Techniques
- t1: **Strip Info + time curve compositor for sequencer**: In sequencer compositor modifier, use Strip Info node for strip frame start, map frame range via time curve to factor 0-1 (e.g., 24 fps, 1 s fade), feed factor to Set Alpha. Keeps effect tied to strip when moved, unlike keyframed opacity.
- t2: **Checking node merge branch in GitHub PR**: Open merge commit, use three-dot menu to see which branches contain the change (main vs release branch) to tell which Blender version includes it.

## Quotes (brief, for attribution)
> the startup.blend ... wasn't compressed. It was like 800 kilobytes. Now it's compressed and it's only 100 or so kilobytes.  (at 42:38, Blender)

## Points to
- survey.blender.org
- blender.org/feed
- code.blender.org/feed
- translate.blender.org
- news.blender.org
- extensions.blender.org (Uuk Paint)
