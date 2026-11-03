---
title: "Docs: ui / styling / css-comparisons"
url: https://create.roblox.com/docs/ui/styling/css-comparisons.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / styling / css-comparisons

[Open](https://create.roblox.com/docs/ui/styling/css-comparisons.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page mapping CSS/HTML concepts to Roblox StyleSheets: StyleRule selectors (class, tag, name, child, descendant, list, state, pseudo-instance), style queries (container and built-in viewport/input/motion), attribute-based tokens with $ prefix, property transitions, and nesting/merging.

## Tips
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Use tag selectors (.ButtonPrimary via CollectionService tags) for reusable styles instead of relying on instance names, since names are not expected to be unique.
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Use built-in style queries (@ViewportDisplaySizeSmall/Medium/Large, @PreferredInputTouch, @ReducedMotionEnabledTrue) to adapt UI to screen size, input device and accessibility settings.
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Define shared design values as StyleSheet attributes and reference them with a $ prefix (e.g. $ButtonBgColor) to keep colours and sizes centralised as tokens.
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Use SetPropertyTransitions with TweenInfo on a StyleRule to animate property changes like colour or rotation on state changes, instead of hand-scripting tweens.
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Nest StyleRules as children of parent rules to merge selectors and reduce repetition, similar to SCSS nesting.
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) **[[ui-ux-design]]** Set AutoButtonColor to false when defining custom hover styles so the default button hover colour does not conflict with your rule.

## Numbers
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) Viewport size breakpoints: **Small <=600px, Medium 601-1200px, Large >=1201px** (Built-in ViewportDisplaySize style query thresholds, mapped from CSS media queries)
- [page](https://create.roblox.com/docs/ui/styling/css-comparisons) Container query example min width: **400px** (Example WideContainer MinSize Vector2(400,0) condition)

## Tools
StyleSheet, StyleRule, StyleLink, StyleQuery, CollectionService

## He points to
- Roblox Docs: CSS Comparisons

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
