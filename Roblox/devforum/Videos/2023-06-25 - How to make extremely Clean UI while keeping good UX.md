---
title: "How to make extremely Clean UI while keeping good UX"
url: https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099
creator: Roblox DevForum
official: false
advice_density: high
date: 2023-06-25
views: 107
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to make extremely Clean UI while keeping good UX

[Open](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) | Roblox DevForum | 107 views | 2023-06-25

## Summary
Tutorial on making clean, usable Roblox UI: color schemes via Adobe Color and contrast checker, primary/secondary button hierarchy, font choice (avoid over-expressive fonts, Gotham suggested), strokes, restrained gradients, flat one-color icons, blur, and three shadow techniques, plus simplicity via collapsible menus and dividers.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Keep one constant color scheme across the UI; pick palettes with a color tool such as Adobe Color rather than ad hoc choices.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Make primary actions visually distinct from secondary ones: give the primary button a background color and remove the background from Cancel, so users don't misclick.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Place key navigation (e.g. Log In / Sign Up) in consistent, predictable locations so users never have to search for them.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Avoid over-expressive display fonts for primary text; use a clean font family (author recommends Gotham and its weights) throughout.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Check text contrast with a contrast checker (e.g. Coolors contrast checker); avoid low-contrast pairs like yellow on white.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Use flat, one-color vector icons (e.g. Google Material icon set, Font Awesome) instead of large multicolor icons.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Use gradients sparingly: as subtle shading, on highlighted text, or matched to a stroke on the primary button, never on all text.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Reduce clutter by using collapsible menus and dividers; for black backgrounds use slightly lighter dividers, for white backgrounds slightly darker ones.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Add depth with shadows: UIStroke with a transparency NumberSequence from 0 to 1 linearly, thickness ~2, black; or duplicated offset frames behind with lower ZIndex; or a drop-shadow texture placed behind the frame.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Use a subtle stroke on containers, slightly darker than the fill and partly transparent, to separate elements.
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) **[[ui-ux-design]]** Use blur behind top bars or panels rather than a solid background for a cleaner look; a stronger blur often looks better.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) Black background color: **RGB(35, 35, 35)** (author's recommended dark background color)
- [page](https://devforum.roblox.com/t/how-to-make-extremely-clean-ui-while-keeping-good-ux/2438099) UIStroke transparency NumberSequence: **0 to 1 linear (0, 0.1, ... 1), thickness ~2, color RGB(0,0,0)** (technique #1 drop shadow via UIStroke)

## Games
- **Pet Sim X**: Its UI uses duplicated offset, rotated, rounded frames behind panels to create a cartoon-style shadow.

## Tools
Adobe Color, Coolors contrast checker, Google Material icons, Font Awesome, Roblox UIStroke, Roblox UICorner, Gotham font

## He points to
- @ImSnox - New ui blur [fully automatic] (DevForum)
- @rivvvur - Product: exe | Modern Admin Panel (UI reference)
- Vercel landing page (gradient reference)
- Font Awesome landing page (design reference)

## Topics
[[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
