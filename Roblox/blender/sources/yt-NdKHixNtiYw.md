---
type: research-source
id: yt-NdKHixNtiYw
title: "NanoBanana PRO just unlocked 3D Product Videography"
source_type: "youtube"
creator: "Jay E | RoboNuggets"
url: "https://www.youtube.com/watch?v=NdKHixNtiYw"
published: "2025-12-11"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0488
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-NdKHixNtiYw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender/Roblox. It shows an n8n + Airtable automation that uses Nano Banana Pro for start/end images and Veo 3.1 (via kie.ai) for product videos. It only mentions Blender in passing, as older complex software (with KeyShot and Cinema 4D) that this approach replaces. Its only transferable material is generic automation patterns: a webhook trigger, a switch router, and polling for async generation.

## Claims
- c1: [1:42] Speaker says product videos that once required KeyShot, Cinema 4D or Blender can now be made with AI image and video models. This is a passing mention with no Blender workflow. *(opinion, low; claude-blender-ai)*
- c2: [7:08] An Airtable button field opens an n8n webhook URL with ?record_id=... appended. The workflow then fetches that row. This is a pattern for triggering automations from a table UI. *(demo, high; automation-and-creator-workflows)*
- c3: [8:32] An n8n Switch node routes a job to the prompt, image or video branch based on which output columns are already filled. This gives staged, human-in-the-loop generation. *(demo, high; automation-and-creator-workflows)*
- c4: [12:35] An n8n webhook test URL differs from the production URL by '-test'. The workflow must be published, and the Airtable button URL edited, for it to run without clicking execute. *(demo, high; automation-and-creator-workflows)*
- c5: [19:10] kie.ai has no sync mode, so n8n needs a Wait node followed by a get-result node (polling) to fetch finished videos. *(demo, medium; automation-and-creator-workflows)*
- c6: [9:52] Prompting advice: make the starting-image prompt detailed (composition, lighting, environment, action, camera, aesthetic, mood). Keep the ending-image prompt simple and pass the starting image as input so both frames stay the same scene. *(experience, medium; other)*
- c7: [10:33] Opinion: for quality, review the prompts and images between stages (human in the loop) rather than running fully automated. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Veo 3.1 Fast cost via kie.ai**: 60 credits (~$0.30) per video Compared with 4 videos on a Freepik Essentials plan.
- n2: **Cost of one full product video (2 images + 1 clip)**: as low as 60 (credits) Speaker's own summary.

## Techniques
- t1: **Airtable button to n8n webhook**: Add a button field whose action opens the n8n webhook URL plus ?record_id=<row id>. In n8n, the webhook passes the id to an Airtable Get node, which fetches the row. Publish the workflow and use the production URL.

## Points to
- n8n
- Airtable
- kie.ai
- Nano Banana Pro
- Veo 3.1
- RoboNuggets community
