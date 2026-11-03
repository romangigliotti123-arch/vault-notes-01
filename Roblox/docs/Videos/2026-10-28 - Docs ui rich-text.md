---
title: "Docs: ui / rich-text"
url: https://create.roblox.com/docs/ui/rich-text.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / rich-text

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/ui/rich-text.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on rich text markup for TextLabel, TextButton and TextBox. Covers enabling the RichText property, supported tags (color, size, font, weight, stroke, bold, italic, underline, strikethrough, line break, uppercase, small caps, mark, comment), escape forms for special characters, and a localization warning.

## Tips
- [page](https://create.roblox.com/docs/ui/rich-text) **[[ui-ux-design]]** Set RichText = true per object (TextLabel, TextButton, TextBox); it is off by default and must be enabled individually.
- [page](https://create.roblox.com/docs/ui/rich-text) **[[ui-ux-design]]** Toggle the RichText checkbox in Studio's Properties window to preview the final render and catch broken tags while editing Text.
- [page](https://create.roblox.com/docs/ui/rich-text) **[[localization-and-international]]** Localizing a game removes rich text tags; re-apply formatting manually to each localized string so styling appears in other languages.
- [page](https://create.roblox.com/docs/ui/rich-text) **[[ui-ux-design]]** Escape special characters (&gt; &quot; &apos; &amp;) so they are not parsed as rich text tags, e.g. write 100 &gt; 10.

## Numbers
- [page](https://create.roblox.com/docs/ui/rich-text) Font weight numeric range: **100 to 900 in factors of 100** (Font weight tag accepts numeric values)

## Tools
Studio Properties window (RichText checkbox preview)

## Topics
[[localization-and-international]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
