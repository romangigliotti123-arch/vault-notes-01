---
type: research-source
id: yt-nYiIQOun7HQ
title: "Why using print() can get you into trouble"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=nYiIQOun7HQ"
published: "2024-05-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-nYiIQOun7HQ

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox/blender-mcp pipeline. Teaches Python logging in Blender scripts: replace print with logging levels, add a StreamHandler with a formatter, guard against duplicate handlers on re-run, set logger level to filter debug output, and avoid logging.basicConfig in add-ons because it configures all of Blender.

## Claims
- c1: [10:47] logging.basicConfig in a Blender script configures logging globally for all Blender add-ons, so add-ons should not call it; configure a named logger and handlers instead. *(opinion, medium; claude-blender-ai)*
- c2: [8:23] Blender keeps the logger alive between script runs, so handlers must be added only if the logger has none, otherwise each run adds a duplicate handler. *(demo, medium; claude-blender-ai)*
- c3: [2:40] Use info for milestones only; put detailed context in debug; reserve error for issues that need immediate attention. *(opinion, low; other)*
- c4: [9:16] Setting logger level to INFO hides debug messages without commenting them out. *(demo, medium; claude-blender-ai)*
- c5: [5:53] On Windows the Blender system console shows log output; Mac/Linux need extra setup. *(demo, low; other)*

## Techniques
- t1: **Guard handler creation**: Check if logger.handlers is empty before adding a StreamHandler so re-running a Blender script does not duplicate output.
- t2: **Level-based filtering**: Set logger level (e.g. INFO) to suppress debug logs instead of commenting out print calls.

### Code: Named logger with a stream handler and formatter, added once
```python
import logging
logger = logging.getLogger("my_script")
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.debug("detail")
logger.info("milestone")
```

## Points to
- Dr. Cin blog post on logging in Blender (named in video, no URL given)
