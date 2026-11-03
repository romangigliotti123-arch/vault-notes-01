---
type: creator-credibility
topic: "Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline"
generated: 2026-11-01
seed: 20260101
---

# Creator credibility: Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline

Sample audit of 6 creators/publishers. Per creator: the piece most cited in the topic notes plus one random piece (fixed seed 20260101), up to 6 checkable claims each, checked against official sources read during the run and against the other sources, plus non-claim signals (hype, income promises, sponsor pitching, outdated advice, original depth). Official sources are not audited.

Counts: TRUSTED 4, MIXED 1, WEAK 0, INSUFFICIENT 1.

## How the synthesis uses this

- TRUSTED (7.5+): may be a primary source; numbers and limits are still checked against official sources.
- MIXED (5.0-7.4): needs a second source before a recommendation is trusted.
- WEAK (below 5.0): never the sole source of a recommendation, and does not count as corroboration.
- INSUFFICIENT (fewer than 4 verified claims): credibility unknown, treated as unverified, not as bad.
- Score = 50% claim accuracy (WRONG counted 3x, OUTDATED half credit) + 20% evidence + 15% depth + 15% honesty. Computed in code from the claim verdicts.
- A verdict describes the sampled pieces and how their claims checked out. It is not a judgement of the person, and claims are AI-extracted summaries, so an apparent error can be an extraction slip.

## Table

| creator | verdict | score | right / wrong / outdated / unverifiable | pieces | note |
|---|---|---|---|---|---|
| Nisky | TRUSTED | 8.4 | 7 / 0 / 0 / 2 | [yt-EM9u4gIHoRg](https://www.youtube.com/watch?v=EM9u4gIHoRg) (top), [yt-KawVMkCLL44](https://www.youtube.com/watch?v=KawVMkCLL44) (rand) | Core workflow claims (bone parenting, clipboard export, anchoring HumanoidRootPart, duplicate collection) agree with DevForum and other sources. No wrong claims found; the content is off-topic for Claude/blender-mcp and many tips are unverifiable. Signals: Hands-on screen tutorials with real workflow; no Claude/MCP content despite topic; mild hype ("secret sauce"); provides downloadable rig, Discord and subscribe pitch; no income promises. |
| Zander | TRUSTED | 8.1 | 8 / 0 / 1 / 2 | [yt-gkD7zE3iTt0](https://www.youtube.com/watch?v=gkD7zE3iTt0) (top), [yt-VWdcKJCJ5Fk](https://www.youtube.com/watch?v=VWdcKJCJ5Fk) (rand) | Technical claims check out: the PBR map size caps, the Alt+N normals fix, OBJ/FBX export and the Node Wrangler shortcut. The Premium requirement from the July 2025 video is outdated, since official Aug 2026 enforcement changes it. Signals: No hype or income promises. Light self-promotion (Discord/Twitter). Fully manual Blender workflow with no Claude, MCP or bpy content. The 2025 beginner guide has rules that are now outdated. |
| Kingkade 3D | TRUSTED | 8.0 | 4 / 0 / 0 / 2 | [yt-IeblIBmiPWI](https://www.youtube.com/watch?v=IeblIBmiPWI) (top), [yt-1B46XsUvi2E](https://www.youtube.com/watch?v=1B46XsUvi2E) (rand) | The import, scale and collision workarounds (CanCollide off plus an invisible part, splitting meshes) match official docs and forum reports. The triangle limit is a hedged guess (~10-15k against ~20k in sources). The second video has no Blender content. Signals: Beginner screen-share tutorial with real demonstrated workarounds. Discloses "not sponsored". No hype or income promises. The second video is off-topic (UI scaling). Nothing on Claude, blender-mcp or bpy. (LOW CONFIDENCE: small sample or little shown evidence) |
| MrWonderHow | TRUSTED | 7.7 | 5 / 0 / 0 / 0 | [yt-Bp65_WElbJc](https://www.youtube.com/watch?v=Bp65_WElbJc) (top), [yt-d6D_XlNBSW4](https://www.youtube.com/watch?v=d6D_XlNBSW4) (rand) | The physics claims (custom density overrides material, wood floats) are consistent with Roblox behavior. Neither video covers the Blender-to-Roblox topic, so relevance is very low. Signals: Both videos are Roblox Studio scripting tutorials with no Blender, Claude or bpy content. No hype or income promises. Mild asset links in the description. Real working builds are shown. (LOW CONFIDENCE: small sample or little shown evidence) |
| Rool-Studio | MIXED | 7.2 | 5 / 0 / 0 / 2 | [yt-VoG-LF8Ff1g](https://www.youtube.com/watch?v=VoG-LF8Ff1g) (top), [yt-WGwQFK_HCP8](https://www.youtube.com/watch?v=WGwQFK_HCP8) (rand) | Standard steps are right: Export Selection, Split by Group, and Install from Disk. The core fix (the PBR Solution add-on) can't be checked against any source. The sample doesn't match the topic (no Claude, MCP or bpy), and the cutscene video is unrelated to Blender. Signals: Short basic tutorials. No hype or sponsor hits. The first video relies on a third-party add-on from a Discord and gives no version info. The second has no Blender content. Neither covers Claude, MCP or bpy. The year-tagged title '2026/2027' is mild SEO. |
| Roblox Creators | INSUFFICIENT | n/a | 3 / 0 / 0 / 5 | [yt-uElRpN1ZQ-4](https://www.youtube.com/watch?v=uElRpN1ZQ-4) (top), [yt-gu1iPJmyMgA](https://www.youtube.com/watch?v=gu1iPJmyMgA) (rand) | Re-import workflow and Alt+Shift+R hotkey match official DevForum docs. Procedural model claims are first-party previews with no checkable external grounding. Signals: Official first-party channel; no sponsor or income claims; live demos; second video is an unreleased-feature preview and barely touches Blender; no Claude/MCP content. |

## Method and limits

- Pieces come from the run's cache (no re-download). Pick 1 = most cited by the synthesised topic notes; pick 2 = random with seed 20260101 per creator (only 1 piece if the creator has one extracted item).
- Each judge call sees the extracted claims, the best-matching official facts, matching claims from other creators, and regex counts for hype/sponsor wording in the cached text.
- The judge model is listed per creator in `.cache/cred/rows.json`. Judge output is not hand-audited claim by claim; small samples can mislead.
- Model cost of this stage: about $0.24 (see costs.csv, stages cred / cred-subagent).
