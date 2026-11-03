---
title: "A Guide to User Interface Design"
url: https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526
creator: Roblox DevForum
official: false
advice_density: medium
date: 2017-08-07
views: 270
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# A Guide to User Interface Design

[Open](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) | Roblox DevForum | 270 views | 2017-08-07

## Summary
Beginner tutorial on Roblox GUI design: anchors/scale vs offset, grid-based alignment with consistent padding, header/body/footer layout, color weight and meaning, and gradients as focal-point tools. Hierarchy and motion chapters are marked as coming soon.

## Tips
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Use Offset only (no Scale) for elements that must not stretch, such as health bars, and keep a fixed Offset padding (e.g. 10) from screen edges.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Use Scale for position at center or edges (e.g. X Scale 0.5 for top center) and Offset for size, so UI doesn't stretch across different screens.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Keep UI grid-based with one universal padding value applied across all frames for consistent alignment.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Structure windows like websites: header for title/categories, body for items, footer for currency/resources; drop the footer when information is minimal.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Use concept art or reference games to decide layout, since one interface design does not fit all games.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Use color for meaning: red for danger/health, green for good/health/money, yellow for money/gold, black and white for foreground/background.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Use contrast in color weight (dark header and footer, lighter body) to create visual gravity and structure.
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) **[[ui-ux-design]]** Place gradients and bright, pure colors on the most important information to act as a focal point; use gradients on selected category icons to show current state.

## Numbers
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) Padding example: **10 Offset from edges** (Example padding for UI frames from screen borders)
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) Scale example: **0.1 = 10% of screen, 0.5 = 50%** (Scale is percentage of screen size)
- [page](https://devforum.roblox.com/t/a-guide-to-user-interface-design/47526) Edge offset scale: **~0.02** (Example Scale value for near-edge positioning mentioned by author)

## Tools
Roblox Studio, Adobe Express Color Palette Generator

## He points to
- GUI Anchoring Template (Roblox library asset 901513077)
- colour-affects.co.uk psychological properties of colours
- Printwand Basic Alignment Principles in Graphic Design

## Topics
[[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
