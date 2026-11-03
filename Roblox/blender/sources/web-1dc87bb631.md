---
type: research-source
id: web-1dc87bb631
title: "Nelder Mead Optimization with F# + Fable"
source_type: "web"
creator: "hydroxide.dev"
url: "https://hydroxide.dev/articles/nelder-mead-optimization-with-fsharp-and-fable/"
published: "2019-07-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 0
density: low
tags: ["research-source", "web", "other"]
---
# web-1dc87bb631

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic: a 2019 hydroxide.dev post on the Nelder-Mead optimization method implemented in F# and run in the browser via Fable with Plotly.js bindings made by ts2fable. It has no content on Blender, Claude, blender-mcp, bpy, or the Roblox asset pipeline.

## Claims
- c1: Source is about Nelder-Mead derivative-free optimization in F# with Fable, not Blender, Claude, bpy, or Roblox. *(doc, high; other)*

### Code: Nelder-Mead simplex step in F# (source's own code; not Blender/bpy related)
```fsharp
type Simplex(points:Point[], objective:Point -> float) =
  let scored = points
              |> Array.map( fun x -> x, objective x)
              |> Array.sortBy (fun (x,y) -> y)
```

## Points to
- https://hydroxide.dev/articles/nelder-mead-optimization-with-fsharp-and-fable/
- Fable
- ts2fable
- Plotly.js
