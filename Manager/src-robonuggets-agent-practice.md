---
tags: [manager-kb, source]
url: https://www.youtube.com/results?search_query=RoboNuggets (video links per claim below)
type: video
author: RoboNuggets
published: 2022-2026 (dates per video note)
accessed: 2026-11-01
reliability: low-medium (practitioner/creator claims from auto-caption notes; [demonstrated] = shown working in the video, [opinion] = advice or claim; not benchmarked)
---
# RoboNuggets: how to run and organise AI agents (from 20 videos)

Source: video notes in the AI Library Vault `Creators/videos/robonuggets/` (synthesised in `research/ai-creators/catalogue/MANAGER-TAKEAWAYS.md`, numbers T1-T46 below match it). Hub: `Creators/hubs/robonuggets.md`. Video ids are in each link.

## Key claims

- **T3. Assign one agent per specific job.** Avoid mega-agents. Why: broad agents get confused. Separate agents also let you give each its own memory, skills and files. [opinion]
  Cites: `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 8:07 (https://www.youtube.com/watch?v=W9igiY2JdHA&t=487s); `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 7:36 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=456s)
- **T4. Send bulky, throwaway work to a sub-agent.** Use one when the task would dump output or files you won't reread, for repeated jobs, or when you want an unbiased fresh look. Why: only a short summary returns to the main session. [demonstrated]
  Cites: `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 8:17 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=497s)
- **T9. Inspect what fills the window.** Run /context and /cost regularly, including on a fresh session. Why: startup overhead (system prompt, tools, skills, memory) can already be tens of thousands of tokens. [demonstrated]
  Cites: `2026-03-27-everything-new-in-claude-code-explained-march-2026-edition` @ 5:03 (https://www.youtube.com/watch?v=3vrn03I5Tss&t=303s)
- **T10. Keep CLAUDE.md thin.** Why: files like this are reinjected at the start of every session or message, so size becomes recurring cost. [demonstrated]
  Cites: `2026-08-03-claude-code-just-changed-forever-6-new-rules-by-anthropic-en` @ 13:37 (https://www.youtube.com/watch?v=gQeRjkb_Hlc&t=817s); `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 17:58 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=1078s)
- **T12. Write operating rules into the instruction file.** Include: check existing tools first, on error read it, fix the script, retest, then update the workflow. Why: the agent learns from failures instead of repeating them. [demonstrated]
  Cites: `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 11:09 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=669s)
- **T13. Organise the workspace for agents, using router files.** Use a short index file, a workspace map, and per-department routers listing skills and references. Why: the agent loads only what it needs. [demonstrated]
  Cites: `2026-10-21-a-new-agentic-os-standard-for-claude-5-5-is-here-claude-mods` @ 21:47 (https://www.youtube.com/watch?v=s_1GPN-NXA0&t=1307s); `2026-08-21-the-new-agentic-os-standard-for-claude-5-models-is-here-full` @ 11:16 (https://www.youtube.com/watch?v=8NSyI-npJCU&t=676s)
- **T14. Hand off state explicitly between sessions.** Use a handoff skill, a cross-session memory tool, or /compact with stated priorities. Why: each session starts from scratch, and re-explaining costs minutes and tokens. [demonstrated]
  Cites: `2026-10-21-a-new-agentic-os-standard-for-claude-5-5-is-here-claude-mods` @ 26:34 (https://www.youtube.com/watch?v=s_1GPN-NXA0&t=1594s)
- **T18. Do not switch models mid-chat.** Why: each model has its own prompt cache, so switching rereads the whole conversation with no discount. [opinion]
  Cites: `2026-10-12-claude-5-5-model-mistakes-you-may-still-be-making-23-tips-an` @ 2:10 (https://www.youtube.com/watch?v=gvESqM6s0kM&t=130s)
- **T19. Keep one source of truth across tools.** Make agents.md a pointer to CLAUDE.md, and change both together. Why: switching costs stay low and the tools don't drift apart. [demonstrated]
  Cites: `2026-06-04-codex-sites-just-became-the-new-lovable` @ 9:29 (https://www.youtube.com/watch?v=Wio-CD84BHE&t=569s); `2026-07-11-i-made-fable-5-and-gpt-5-6-build-the-same-app-raw-results` @ 21:18 (https://www.youtube.com/watch?v=_rTPBC3RnRI&t=1278s)
- **T24. Separate the critic from the worker.** Use a scorer or critic sub-agent per worker, and a final check that parts meet spec. For subjective output, define "good" for an LLM judge and test it. [demonstrated]
  Cites: `2026-08-05-this-new-claude-prompting-technique-is-blowing-people-s-mind` @ 4:02 (https://www.youtube.com/watch?v=BNjzXcEXmg4&t=242s); `2026-08-05-this-new-claude-prompting-technique-is-blowing-people-s-mind` @ 5:45 (https://www.youtube.com/watch?v=BNjzXcEXmg4&t=345s)
- **T25. Verify by running the thing.** Have agents build, view, click-test and use integrations until proven working. Why: self-reported success is not evidence. [demonstrated]
  Cites: `2026-03-11-every-antigravity-concept-explained-for-normal-people` @ 5:09 (https://www.youtube.com/watch?v=QrqMAAOFpIQ&t=309s)
- **T26. Review with parallel specialist reviewers who must reproduce each finding.** Cover logic, security, performance and edge cases. Why: it cuts false positives. [demonstrated]
  Cites: `2026-03-27-everything-new-in-claude-code-explained-march-2026-edition` @ 4:11 (https://www.youtube.com/watch?v=3vrn03I5Tss&t=251s); `2026-05-28-claude-ultracode-will-10x-your-workflows` @ 8:10 (https://www.youtube.com/watch?v=2rhZOisVXZM&t=490s)
- **T27. Ask for several independent drafts and have the agent grade them against the goal.** Do not accept the first draft. Why: it gets closer to a final version, at extra usage. [opinion]
  Cites: `2026-10-12-claude-5-5-model-mistakes-you-may-still-be-making-23-tips-an` @ 8:17 (https://www.youtube.com/watch?v=gvESqM6s0kM&t=497s)
- **T29. Run independent work in parallel.** Examples are chapters, design variants, audits and test loops. Why: wall-clock time drops and context stays isolated. [demonstrated]
  Cites: `2026-04-29-claude-canva-design-on-autopilot-beginners-course` @ 5:27 (https://www.youtube.com/watch?v=fT3rsZ22C4A&t=327s)
- **T31. Enforce never-break rules with hooks, not skill text.** Example: no invoice above a limit without sign-off. Why: hooks run as code regardless of what the model decides. [opinion]
  Cites: `2026-10-05-anthropic-just-revealed-10-new-rules-for-claude-skills` @ 10:22 (https://www.youtube.com/watch?v=VQyYzLJ6xos&t=622s); `2026-10-05-anthropic-just-revealed-10-new-rules-for-claude-skills` @ 11:04 (https://www.youtube.com/watch?v=VQyYzLJ6xos&t=664s)
- **T32. Add caution rules and prefer guarded tools.** Ask the agent to amend CLAUDE.md to be more careful about deleting files, and avoid tools without permission and deletion guardrails. [opinion]
  Cites: `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 5:27 (https://www.youtube.com/watch?v=W9igiY2JdHA&t=327s); `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 14:49 (https://www.youtube.com/watch?v=W9igiY2JdHA&t=889s)
- **T33. Use auto mode for safe decisions and permission relay for big ones.** Why: agents no longer stall waiting at a terminal. [demonstrated]
  Cites: `2026-03-25-anthropic-just-fixed-the-worst-part-of-claude-code` @ 2:01 (https://www.youtube.com/watch?v=9BIy_h4L-MY&t=121s); `2026-03-25-anthropic-just-fixed-the-worst-part-of-claude-code` @ 4:40 (https://www.youtube.com/watch?v=9BIy_h4L-MY&t=280s); `2026-03-25-anthropic-just-fixed-the-worst-part-of-claude-code` @ 5:33 (https://www.youtube.com/watch?v=9BIy_h4L-MY&t=333s)
- **T35. Harden every webhook.** Use HTTPS, verify signing secrets, keep credentials in the credential store, and use production URLs only once secured. Why: webhooks are public entry points. [opinion]
  Cites: `2025-11-23-build-stunning-one-prompt-apps-with-gemini-3-here-s-the-secr` @ 18:02 (https://www.youtube.com/watch?v=4xic0AViHm0&t=1082s)
- **T36. Keep human checkpoints where outputs are probabilistic or hard to reverse.** Review dialogue and prompts, and approve email drafts. Why: some outputs will be off. [demonstrated]
  Cites: `2025-12-09-ai-brand-ads-so-cinematic-you-ll-think-they-cost-30-000-it-c` @ 19:06 (https://www.youtube.com/watch?v=UEeJShCrROw&t=1146s); `2025-09-21-the-ultimate-agent-for-limitless-ugcs-seedream-x-nanobanana` @ 7:11 (https://www.youtube.com/watch?v=KrdthDfS-KI&t=431s)
- **T37. Match model to job.** Use cheaper models for sub-agents and simple tasks, and the strongest for deep reasoning. Why: model tiers differ widely in cost. [demonstrated]
  Cites: `2026-07-23-i-made-fable-5-and-kimi-k3-build-the-same-app-raw-results` @ 23:07 (https://www.youtube.com/watch?v=WfnHJOYZA0E&t=1387s)
- **T39. Prune dead weight.** Run /doctor and /skill-doctor, and view a skill tree to find skills clogging context. [demonstrated]
  Cites: `2026-08-03-claude-code-just-changed-forever-6-new-rules-by-anthropic-en` @ 20:37 (https://www.youtube.com/watch?v=gQeRjkb_Hlc&t=1237s); `2026-10-28-anthropic-just-shipped-claude-2-0-master-it-in-17-minutes` @ 13:08 (https://www.youtube.com/watch?v=yMnFHFf43Qg&t=788s); `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 20:45 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=1245s)
- **T41. Close the loop at session end.** Run a calibrate or reflect step that updates skills, memory and rules with learnings. Why: the system improves with each run. [demonstrated]
  Cites: `2026-08-03-claude-code-just-changed-forever-6-new-rules-by-anthropic-en` @ 17:06 (https://www.youtube.com/watch?v=gQeRjkb_Hlc&t=1026s); `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 11:09 (https://www.youtube.com/watch?v=tFCgmeOWlA8&t=669s)
- **T46. Raise autonomy in steps.** Move from manual prompt-review-reprompt, to a critic loop, to a fleet of sub-agents each with a critic. Add max-iteration guardrails and keep a human available mid-run. [opinion]
  Cites: `2026-08-05-this-new-claude-prompting-technique-is-blowing-people-s-mind` @ 4:02 (https://www.youtube.com/watch?v=BNjzXcEXmg4&t=242s)

## Quotable

No verbatim quotes kept: the source notes are summaries of auto-captions. Use the timestamp links above to hear the exact wording.

## Used by

[[topic-agent-security]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-model-effort-routing-cost]], [[topic-orchestration-patterns]], [[topic-skill-library-retrieval]]
