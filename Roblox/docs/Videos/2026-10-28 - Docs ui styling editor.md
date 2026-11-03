---
title: "Docs: ui / styling / editor"
url: https://create.roblox.com/docs/ui/styling/editor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / styling / editor

[Open](https://create.roblox.com/docs/ui/styling/editor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the built-in Style Editor (UI tab): creating a design style set, tokens, design sheets, style rules (class, tag, UI modifier, state), queries (built-in and custom), transitions, and themes.

## Tips
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Do not delete or modify the generated BaseStyleSheet; build tokens and style rules on top of the design StyleSheet instead.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Keep the StyleDerive linking the StyleSheet to the BaseStyleSheet; removing it makes unstyled GuiObjects get odd defaults such as Size 0,0,0,0.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Create tokens early (colors, fonts, UDim sizes, text sizes) and link properties to them; tokens are highly recommended for updating UI styles over time.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Use tag rules (.ButtonPrimary) with CollectionService tags to style specific UI objects without affecting every instance of a class.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Use built-in ViewportDisplaySize queries (Small/Medium/Large) and test with the Device Emulator across PS5, Average Laptop, and iPhone XR presets.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Use Controller Emulator to verify PreferredInput-based style switches, such as gamepad layouts.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Use a default TweenInfo transition on TextButton plus Hover GuiState rules to get smooth hover feedback with minimal scripting.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** Create themes by duplicating a base theme and swapping only the theme tokens that differ, so both themes share a common token set.
- [page](https://create.roblox.com/docs/ui/styling/editor) **[[ui-ux-design]]** When linking theme tokens, check the hover text for '$[Token] in ThemeA' to confirm the value comes from the theme, not the global token sheet.

## Numbers
- [page](https://create.roblox.com/docs/ui/styling/editor) Default transition: **1, Quad, Out, 0 (duration 1s, no delay)** (Default transition inserted under TextButton rule)
- [page](https://create.roblox.com/docs/ui/styling/editor) Hover rotation example: **-5 degrees** (TextButton hover state in transition example)
- [page](https://create.roblox.com/docs/ui/styling/editor) Custom query MinSize: **400, 0 (width 400 px)** (Custom StyleQuery condition for TextLabel width)
- [page](https://create.roblox.com/docs/ui/styling/editor) Default Color3 in base sheet: **[163, 162, 165]** (Engine default synced by BaseStyleSheet)

## Tools
Style Editor, Device Emulator, Controller Emulator, CollectionService

## He points to
- Class.StyleQuery.IsActive
- Class.StyleSheet:SetDerives()
- Enum.GuiState
- Enum.DisplaySize

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
