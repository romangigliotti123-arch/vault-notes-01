---
title: "Roblox UI Tutorial: Clean GUI Menu in Luau"
url: https://youtu.be/BJea3LJJWww
creator: Generalist Programmer
official: false
advice_density: medium
date: 2026-07-07
views: 403
transcript: auto-captions
confidence: high
tags: [roblox, generalistprogrammer3233, youtube-learn]
creator_trust: MIXED
creator_score: 7.1
---

> [!note] Trust: MIXED (credibility audit score 7.1): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Roblox UI Tutorial: Clean GUI Menu in Luau

[Watch](https://youtu.be/BJea3LJJWww) | generalistprogrammer3233 | 403 views | 2026-07-07

## Summary
Tutorial building a clean, centered Roblox GUI from scratch in Luau: ScreenGui (ResetOnSpawn false), centered Frame using UDim2 with AnchorPoint 0.5/0.5, UICorner rounding, title TextLabel (Gotham Bold, TextScaled), TextButton wired to MouseButton1Click, and UIListLayout plus UIPadding for layout. Includes a promo for a $19 UI kit.

## Tips
- [0:59](https://youtu.be/BJea3LJJWww?t=59) **[[ui-ux-design]]** Set ScreenGui ResetOnSpawn to false so the menu is not destroyed and rebuilt on every respawn, which would reset held state.
- [2:05](https://youtu.be/BJea3LJJWww?t=125) **[[ui-ux-design]]** Use UDim2 with scale for size/position so layouts adapt to phones, tablets and monitors; offset adds fixed pixels on top.
- [2:47](https://youtu.be/BJea3LJJWww?t=167) **[[ui-ux-design]]** Set AnchorPoint to 0.5,0.5 when centering a frame with position 0.5,0,0.5,0; otherwise the top-left corner lands at center.
- [3:40](https://youtu.be/BJea3LJJWww?t=220) **[[ui-ux-design]]** Add a UICorner child to frames and buttons (scale 0, offset ~12) to replace dated sharp 90-degree corners with one instance per element.
- [4:37](https://youtu.be/BJea3LJJWww?t=277) **[[ui-ux-design]]** Enable TextScaled on text labels and buttons so text resizes to its box instead of clipping on small screens.
- [5:31](https://youtu.be/BJea3LJJWww?t=331) **[[ui-ux-design]]** Connect TextButton.MouseButton1Click for clicks; it fires on both mouse click and phone tap with no extra code.
- [6:37](https://youtu.be/BJea3LJJWww?t=397) **[[ui-ux-design]]** Use UIListLayout (padding ~8px, horizontal center) instead of hand-placing elements so the column reflows when items are added or removed.
- [7:20](https://youtu.be/BJea3LJJWww?t=440) **[[ui-ux-design]]** Add UIPadding to keep content off the frame border; roughly 10px top padding gives breathing room.

## Numbers
- [0:26](https://youtu.be/BJea3LJJWww?t=26) UI kit price: **$19 (promotional, Roblox Pro UI Kit)** (Creator's own paid UI kit, promoted in video)
- [2:05](https://youtu.be/BJea3LJJWww?t=125) Corner radius example: **0 scale + 12 offset** (UICorner soft radius suggested for panels)
- [6:37](https://youtu.be/BJea3LJJWww?t=397) UIListLayout padding: **8 px** (Spacing between stacked elements in the menu)
- [7:20](https://youtu.be/BJea3LJJWww?t=440) UIPadding top: **10 px** (Breathing room from frame top edge)
- [4:37](https://youtu.be/BJea3LJJWww?t=277) Title label height: **44 px tall, full width** (Fixed-height heading label for the shop panel)

## Tools
Roblox Studio, Luau, ScreenGui, UICorner, UIListLayout, UIPadding, TextButton, TextLabel

## He points to
- Written guide linked in video description (unnamed)
- Roblox Pro UI Kit ($19, creator's own product)

## Quotes
- [2:47](https://youtu.be/BJea3LJJWww?t=167) "Scale is a fraction of the parent, from zero to one. Offset is a flat number of pixels added on top."
- [0:59](https://youtu.be/BJea3LJJWww?t=59) "Anything you put in StarterGui gets copied into each player's PlayerGui when they join."

## Topics
[[ui-ux-design]]

Back to [[generalistprogrammer3233 - How to make successful Roblox games]]
