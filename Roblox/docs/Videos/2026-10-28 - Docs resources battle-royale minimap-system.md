---
title: "Docs: resources / battle-royale / minimap-system"
url: https://create.roblox.com/docs/resources/battle-royale/minimap-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / minimap-system

[Open](https://create.roblox.com/docs/resources/battle-royale/minimap-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the battle-royale template's minimap system: how the minimap is built (ImageLabel plus CollectionService tags), how to add new tagged indicators, and the MainConfiguration values for sizing, zoom and map dimensions.

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/minimap-system) **[[building-and-level-design]]** Assume a square map; the minimap expects map center at Vector3.new(map_size, 0, map_size), so set map_size to match your map's edge length in studs.
- [page](https://create.roblox.com/docs/resources/battle-royale/minimap-system) **[[updates-live-ops]]** To show a new object on the minimap, tag the workspace object via Tags properties, add a uniquely named ImageLabel under GuiObjects/minimap/mapframe, then register the tag in MinimapGui.start().
- [page](https://create.roblox.com/docs/resources/battle-royale/minimap-system) **[[ui-ux-design]]** Provide a toggle between minimap and world map: M key on keyboard, Up on gamepad DPad, and tapping the minimap on touchscreens, so all input types can reach the full map.
- [page](https://create.roblox.com/docs/resources/battle-royale/minimap-system) **[[ui-ux-design]]** Tune minimap_width/height and minimap_zoom separately from worldmap_width/height/zoom so the small corner map and full map each fit the screen.

## Tools
Roblox Studio, CollectionService, ImageLabel, MainConfiguration

## He points to
- Roblox battle-royale template docs: minimap-system

## Topics
[[building-and-level-design]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
