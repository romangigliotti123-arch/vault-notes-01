---
title: "[Full Release] New UI Capabilities: Shadows & Individual Corners!"
url: https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-05-14
views: 1961
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Full Release] New UI Capabilities: Shadows & Individual Corners!

[Open](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) | Roblox DevForum | 1,961 views | 2026-05-14

## Summary
Roblox DevForum release post announcing full release of UIShadow (native 2D drop shadows) and per-corner UICorner rounding. Covers properties, Explorer/Styling/script usage, known issues, and performance guidance (max ~100 UIShadows on-screen).

## Tips
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Use per-corner UICorner radii (TopLeftRadius etc.) for speech bubbles, tab headers and one-sided callouts instead of image assets or 9-slice workarounds.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[optimization-and-streaming]]** Keep under about 100 UIShadows on-screen at once for best performance; UIShadow is consistently faster than 9-sliced ImageLabels.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Use UIShadow for depth on buttons and glows; it does not affect layout or trigger recalculations, and multiple UIShadows can be stacked on one element.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** For TextLabel/TextBox/TextButton, UIShadow applies to the background rectangle, not the text; native text shadows are not available.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Avoid setting both CornerRadius and individual corner radii when styling a UICorner; it produces unexpected behaviour. Pick one approach.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Setting CornerRadius overwrites all per-corner properties; set CornerRadius first, then override individual corners in Properties.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Shadows may look jagged on elements with large corner radius; a known issue under investigation.
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) **[[ui-ux-design]]** Use low BlurRadius for hard edges and high values (up to 1000) for soft diffuse glows; scale values are a percentage of the parent's shortest dimension.

## Numbers
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) UIShadow on-screen limit: **~100 recommended max** (Recommended max UIShadows drawn on-screen at once for best performance)
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) BlurRadius max: **1000** (Upper bound for UIShadow blur; higher gives diffuse soft glow)
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) Transparency range: **0 (opaque) to 1 (invisible)** (UIShadow Transparency property range)
- [page](https://devforum.roblox.com/t/full-release-new-ui-capabilities-shadows-individual-corners/4636263) ZIndex: **negative only** (UIShadow ZIndex must be negative since shadows render below parent)

## Tools
Roblox Studio, Style Editor, Explorer/Properties

## He points to
- IndividualRoundedCorner_Demo.rbxl sample place
- UIShadow_Demo.rbxl sample place

## Topics
[[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
