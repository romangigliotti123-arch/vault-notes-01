---
type: research-source
id: web-95ffff35bb
title: "WPF ItemsSource not updating when items added to ObservableCollection?"
source_type: "web"
creator: "hydroxide.dev"
url: "https://hydroxide.dev/articles/wpf-itemssource-not-updating-when-items-added-to-observablecollection/"
published: "2018-09-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0006
relevance: 0
density: low
tags: ["research-source", "web"]
---
# web-95ffff35bb

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
WPF blog post (2018) on why an ItemsControl Visibility binding does not refresh when items are added to an ObservableCollection. Visibility binds to PropertyChanged, but ObservableCollection raises CollectionChanged. Fix: handle CollectionChanged and raise PropertyChanged. Nothing on Blender, Roblox, bpy, MCP, or asset pipelines.

