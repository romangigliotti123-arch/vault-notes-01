---
type: research-source
id: yt-lj-xPo7ueGA
title: "Free and Local Real-Time AI Animation - NVIDIA MotionBricks.cpp"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=lj-xPo7ueGA"
published: "2026-09-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other", "rigging-animation"]
---
# yt-lj-xPo7ueGA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on MotionBricks CPP, a CPU/low-VRAM port of NVIDIA's real-time motion system, tested in Unreal Engine. Mentions Kimodo (text-to-motion) and Skin Tokens CPP (auto-rigging). Blender/Roblox content is minimal: an AI agent (GPT-6) reportedly rigged and animated a character via Blender MCP tools. No Roblox export, mesh, or pipeline details.

## Claims
- c1: [2:25] Presenter says an AI agent rigged a character and made a set of animations, but only with the right MCP tools and skills. No workflow steps shown. *(experience, low; claude-blender-ai)*
- c2: [2:30] Hicksfield Blender plugin is described as exposing many tools for agents to work with Blender. Presenter is sponsored by Hicksfield, so treat as promotional. *(opinion, low; claude-blender-ai)*
- c3: [3:21] Kimodo-generated animations can be exported and mapped to Unreal Engine or other engines. Presented without export settings or retargeting steps. *(opinion, low; rigging-animation)*
- c4: [4:01] Skin Tokens CPP takes a mesh and predicts skeleton and skin weights. Presenter calls it still a work in progress. *(demo, low; rigging-animation)*
- c5: [4:50] MotionBricks CPP ran on a local machine and connected to Unreal Engine through a bridge; port built in under an hour per presenter. *(experience, low; other)*
- c6: [5:00] Presenter estimates 8 GB VRAM yields about 30 fps motion output; Unreal can scale it to 60 fps. CPU runs are possible but expected to have delay. *(opinion, low; other)*
- c7: [1:45] Presenter installed the CPP port by giving an AI model the git repo and asking it to install, instead of following the README manually. *(experience, medium; automation-and-creator-workflows)*

## Numbers
- n1: **output frame rate**: up to 30 fps (MotionBricks), scalable to 60 in Unreal 
- n2: **VRAM**: ~8 GB estimated for 30 fps output 
- n3: **port time**: under an hour (presenter's estimate) 

## Techniques
- t1: **AI-agent install from repo**: Create empty folder, give the git repo URL to an AI chat model, ask it to install the project. Presenter did not read the install doc.
- t2: **Agent with Blender MCP tools**: Connect a Blender MCP plugin so an agent can drive Blender tools; presenter reports agent-driven rigging and animation this way.

## Quotes (brief, for attribution)
> GPT-6 rigged my character and did a set of animations  (at 2:25, Stefan 3D AI)

## Points to
- MotionBricks CPP port (github, linked in description)
- Kimodo CPP
- Skin Tokens CPP
- Hicksfield Blender plugin (sponsor)
- Unreal Engine MCP server
- NVIDIA MotionBricks (official open source)
