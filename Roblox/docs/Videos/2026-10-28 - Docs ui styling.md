---
title: "Docs: ui / styling"
url: https://create.roblox.com/docs/ui/styling.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / styling

[Open](https://create.roblox.com/docs/ui/styling.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on UI styling: a CSS-like stylesheet system with style rules, tokens (attribute variables), themes (token sets swapped via StyleDerive), StyleLink to apply sheets to a ScreenGui, selectors (class, tag, name, modifier, state, query), and Studio's modified-property indicators.

## Tips
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Define colors, sizes and fonts as tokens in one StyleSheet, then reference them from theme and rule sheets so changes propagate everywhere.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Keep themes with identical token sets; related themes must define the same tokens to swap correctly.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Only one StyleSheet can apply to a given GUI tree; link the design sheet to the ScreenGui with a StyleLink.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Use tag selectors (.ClassName) with CollectionService to style groups of unrelated buttons consistently.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Use state selectors such as Enum.GuiState.Hover for interaction feedback instead of scripting hover visuals.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Use query selectors (@ prefix) with StyleQuery to adapt layouts to screen size, input type, or accessibility settings.
- [page](https://create.roblox.com/docs/ui/styling) **[[ui-ux-design]]** Use Reset to Default on bold (overridden) properties in Properties window to restore styled values.

## Tools
Roblox Studio Style Editor, CollectionService, StyleSheet, StyleRule, StyleDerive, StyleLink

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
