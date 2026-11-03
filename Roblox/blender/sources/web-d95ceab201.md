---
type: research-source
id: web-d95ceab201
title: "Blender Python API doc: info_gotchas_threading"
source_type: "web"
creator: "docs.blender.org"
url: "https://raw.githubusercontent.com/blender/blender/main/doc/python_api/rst/info_gotchas_threading.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: medium
tags: ["research-source", "web", "bpy-scripting-headless", "other"]
---
# web-d95ceab201

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python API gotcha page: threads are unsupported and can crash Blender (Cycles rendering, drivers, timers). Threads are only safe if joined before the script ends; no bpy calls while threads run. Use multiprocessing for independent work. Source is generic and does not cover Roblox, MCP, or Claude.

## Claims
- c1: Python threads in Blender can crash in hard-to-diagnose ways (e.g., during Cycles rendering, with Python drivers, or background downloads); Blender's Python integration is not thread safe. *(doc, high; bpy-scripting-headless)*
- c2: Threading is only safe when all threads are joined before the script finishes; no bpy or Blender API calls may run while threads are active. *(doc, high; bpy-scripting-headless)*
- c3: Recommended alternative for running Python independently of Blender is the multiprocessing module, not threads. *(doc, high; bpy-scripting-headless)*
- c4: Self-rescheduling threading.Timer loops that outlive the script cause random crashes or errors in Blender's drawing code. *(doc, high; bpy-scripting-headless)*
- c5: Standard library modules such as multiprocessing.Queue may internally use threads, so they can also be unsafe in Blender. *(doc, medium; other)*

## Techniques
- t1: **Join-before-bpy threading**: Start threads doing only non-bpy work (e.g. requests downloads), join all, then resume bpy calls in main thread.

### Code: Safe pattern: parallel downloads with threads joined before bpy is used again
```python
threads = [
   threading.Thread(
      name="thread-{}".format(index),
      target=download,
      args=(url,),
   )
   for index, url in enumerate(urls)
]
for t in threads:
   t.start()
for t in threads:
   t.join()
```

### Code: Unsupported pattern: daemon Timer rescheduling itself after script ends
```python
def my_timer():
      t = Timer(0.1, my_timer)
      t.daemon = True
      t.start()
      print("Running...")
my_timer()
```

## Quotes (brief, for attribution)
> Python threads cause Blender to crash in hard to diagnose ways.  (docs.blender.org)
> For running Python code independently of Blender, it is recommended to use the multiprocessing module.  (docs.blender.org)

## Points to
- https://docs.python.org/3/library/multiprocessing.html
- https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
