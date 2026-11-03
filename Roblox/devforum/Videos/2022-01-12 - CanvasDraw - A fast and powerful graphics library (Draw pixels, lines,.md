---
title: "CanvasDraw - A fast and powerful graphics library (Draw pixels, lines, triangles, read/modify image data, and much more!)"
url: https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-01-12
views: 1529
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# CanvasDraw - A fast and powerful graphics library (Draw pixels, lines, triangles, read/modify image data, and much more!)

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) | Roblox DevForum | 1,529 views | 2022-01-12

## Summary
CanvasDraw v4.20.2 documentation page: a Roblox pixel-canvas graphics library built on EditableImage. Covers creating canvases on Frames/MeshParts, drawing primitives (SetPixel, DrawLine, DrawCircle, DrawTriangle, DrawImage), coordinate and RGBA conventions, and EditableImage throttling and memory-budget workarounds.

## Tips
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) **[[scripting-and-performance]]** Set Canvas.AutoRender = false when using multiple canvases, then call Canvas:Render() only when needed to avoid per-frame EditableImage updates.
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) **[[optimization-and-streaming]]** If EditableImage memory budget is hit, lower the canvas resolution, or use Canvas:CreateImageContent() for static images, which does not consume the editable memory budget.
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) **[[scripting-and-performance]]** Use SetRGB(x, y, r, g, b) instead of SetPixel with Color3 for faster pixel writes.
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) **[[common-mistakes]]** CanvasDraw pixel coordinates start at (1,1) and end at (Width, Height), unlike most Roblox APIs; out-of-range access causes buffer out-of-bounds errors.

## Numbers
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) Default canvas resolution: **100x100** (CanvasDraw.new default when no resolution given)
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) Max resolution: **1024x1024 (2048x2048 in plugins)** (Variable resolution limit stated in features)
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) Custom image max size: **2048x2048** (Image instance generated from image files)
- [page](https://devforum.roblox.com/t/canvasdraw-a-fast-and-powerful-graphics-library-draw-pixels-lines-triangles-readmodify-image-data-and-much-more/1624633) Compression example: **1024x1024 image on a single DataStore key** (Image compression for data handling)

## Games
- **The Powder Box**: Falling sand/powder game built by the author with CanvasDraw; example of pixel-simulation gameplay on canvas.
- **3D Fishing Game**: Showcased as a featured project built with CanvasDraw; no specific lesson stated.

## Tools
CanvasDraw module, CanvasDraw Tools plugin, CanvasDraw Image Importer plugin, GitHub

## Topics
[[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
