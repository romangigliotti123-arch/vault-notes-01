---
title: "Docs: ui / text-input"
url: https://create.roblox.com/docs/ui/text-input.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / text-input

[Open](https://create.roblox.com/docs/ui/text-input.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs page on TextBox text inputs: creating TextBoxes on ScreenGuis and SurfaceGuis (adorned to parts), scripting FocusLost and numeric-only input via GetPropertyChangedSignal, and the requirement to apply text filtering to user-entered text.

## Tips
- [page](https://create.roblox.com/docs/ui/text-input) **[[ui-ux-design]]** Use PlaceholderText on a TextBox to tell players what input is expected.
- [page](https://create.roblox.com/docs/ui/text-input) **[[ui-ux-design]]** If a SurfaceGui TextBox is not visible, try a different face in the SurfaceGui's Face property.
- [page](https://create.roblox.com/docs/ui/text-input) **[[client-server-and-remotes]]** Use TextBox.FocusLost with enterPressed to act only when the player submits, not when they merely click away.
- [page](https://create.roblox.com/docs/ui/text-input) **[[anti-exploit-and-security]]** Validate and sanitize TextBox input on the server; client-side filtering like gsub is not enough on its own.
- [page](https://create.roblox.com/docs/ui/text-input) **[[age-ratings-moderation-and-tos]]** Apply text filtering to any user-entered text you display; Roblox is not responsible for it and will remove games that don't filter.
- [page](https://create.roblox.com/docs/ui/text-input) **[[ui-ux-design]]** Restrict input format with GetPropertyChangedSignal('Text') and string.gsub, e.g. gsub(text, '%D', '') to allow only digits.

## Tools
TextBox, ScreenGui, SurfaceGui, Roblox Studio Explorer/Properties

## He points to
- Roblox docs: TextBox, GuiObject, string.gsub

## Topics
[[age-ratings-moderation-and-tos]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
