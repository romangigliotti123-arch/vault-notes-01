---
tags: [manager-kb, source]
url: https://www.youtube.com/results?search_query=Nate+Herk (video links per claim below)
type: video
author: Nate Herk
published: 2022-2026 (dates per video note)
accessed: 2026-11-01
reliability: low-medium (practitioner/creator claims from auto-caption notes; [demonstrated] = shown working in the video, [opinion] = advice or claim; not benchmarked)
---
# Nate Herk: how to run and organise AI agents (from 38 videos)

Source: video notes in the AI Library Vault `Creators/videos/nate-herk/` (synthesised in `research/ai-creators/catalogue/MANAGER-TAKEAWAYS.md`, numbers T1-T46 below match it). Hub: `Creators/hubs/nate-herk.md`. Video ids are in each link.

## Key claims

- **T1. Make the orchestrator only delegate.** Tell it explicitly not to write emails, summaries or code itself. Why: orchestrators that do the work themselves skip the specialists and burn expensive context and limits. [demonstrated]
  Cites: `2025-06-10-multi-agent-systems-have-never-been-easier-to-build-n8n-no-c` @ 11:00 (https://www.youtube.com/watch?v=0iUNOmeU7O4&t=660s); `2025-08-15-i-built-the-ultimate-army-of-media-agents-in-n8n-free-templa` @ 11:35 (https://www.youtube.com/watch?v=jBanaNBY-sM&t=695s); `2026-07-24-i-tested-opus-5-vs-fable-5-what-you-need-to-know` @ 29:20 (https://www.youtube.com/watch?v=2J3uX8iRNng&t=1760s)
- **T2. Brief the lead agent as a project manager.** Say: don't execute, delegate to cheaper sub-agents, parallelize independent work, log progress to a build plan or per-agent folder, and flag open issues. Why: it keeps the expensive model cheap and leaves a written trail. [demonstrated]
  Cites: `2026-08-10-build-sell-ai-saas-products-2-hour-course` @ 31:44 (https://www.youtube.com/watch?v=IVx8OSMbTss&t=1904s); `2026-08-10-build-sell-ai-saas-products-2-hour-course` @ 33:47 (https://www.youtube.com/watch?v=IVx8OSMbTss&t=2027s)
- **T3. Assign one agent per specific job.** Avoid mega-agents. Why: broad agents get confused. Separate agents also let you give each its own memory, skills and files. [opinion]
  Cites: `2026-08-12-grok-bot-is-for-real-what-you-need-to-know` @ 8:29 (https://www.youtube.com/watch?v=PQBYZQqan2g&t=509s)
- **T4. Send bulky, throwaway work to a sub-agent.** Use one when the task would dump output or files you won't reread, for repeated jobs, or when you want an unbiased fresh look. Why: only a short summary returns to the main session. [demonstrated]
  Cites: `2026-06-09-how-to-build-claude-subagents-better-than-99-of-people` @ 22:12 (https://www.youtube.com/watch?v=e18sdZLwP7o&t=1332s); `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 2:19:48 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=8388s)
- **T5. Choose skill or sub-agent by the context you need.** Skills usually run in the main session. Sub-agents get a clean window, can run in parallel, and can use another model. Why: it avoids polluting the main session. [opinion]
  Cites: `2026-06-09-how-to-build-claude-subagents-better-than-99-of-people` @ 8:40 (https://www.youtube.com/watch?v=e18sdZLwP7o&t=520s); `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 2:30:37 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=9037s); `2026-03-05-turn-claude-code-into-your-executive-assistant-in-27-mins` @ 21:35 (https://www.youtube.com/watch?v=mi4hcipESKQ&t=1295s)
- **T6. Use specialist sub-agents for expert roles.** Examples are a code reviewer, builder, debugger, test runner, security auditor or researcher, with a main session acting as project lead. Why: a general assistant with skills is a jack of all trades. [opinion]
  Cites: `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 6:52:55 (https://www.youtube.com/watch?v=mpALXah_PBg&t=24775s); `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 2:39:52 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=9592s)
- **T7. Hardcode stable lookups and delegate searches.** Put known IDs into the skill and hand the searching to a sub-agent. Why: the agent otherwise re-fetches them each run, costing time and tokens. [demonstrated]
  Cites: `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 6:22:25 (https://www.youtube.com/watch?v=mpALXah_PBg&t=22945s); `2026-02-27-master-95-of-claude-code-skills-in-28-minutes` @ 14:38 (https://www.youtube.com/watch?v=zKBPwDpBfhs&t=878s)
- **T8. Treat context as a precious resource and reset between topics.** Start a new chat or run /clear when switching tasks. Why: long context costs more, distracts the model and lowers accuracy. [opinion]
  Cites: `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:31:20 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=19880s); `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 52:16 (https://www.youtube.com/watch?v=mpALXah_PBg&t=3136s)
- **T9. Inspect what fills the window.** Run /context and /cost regularly, including on a fresh session. Why: startup overhead (system prompt, tools, skills, memory) can already be tens of thousands of tokens. [demonstrated]
  Cites: `2026-04-02-18-claude-code-token-hacks-in-18-minutes` @ 5:07 (https://www.youtube.com/watch?v=49V-5Ock8LU&t=307s); `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 3:11:56 (https://www.youtube.com/watch?v=mpALXah_PBg&t=11516s)
- **T10. Keep CLAUDE.md thin.** Why: files like this are reinjected at the start of every session or message, so size becomes recurring cost. [demonstrated]
  Cites: `2026-04-20-how-to-never-hit-your-claude-session-limit-again` @ 0:27 (https://www.youtube.com/watch?v=_qZvORxGqI0&t=27s)
- **T11. Move anything you repeat into CLAUDE.md or a skill.** Why: it stops you re-explaining and gives the agent a durable onboarding file. [opinion]
  Cites: `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 2:11:46 (https://www.youtube.com/watch?v=mpALXah_PBg&t=7906s); `2026-01-21-master-95-of-claude-code-in-36-mins-as-a-beginner` @ 21:37 (https://www.youtube.com/watch?v=saggDHHnmtQ&t=1297s)
- **T12. Write operating rules into the instruction file.** Include: check existing tools first, on error read it, fix the script, retest, then update the workflow. Why: the agent learns from failures instead of repeating them. [demonstrated]
  Cites: `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 1:08:21 (https://www.youtube.com/watch?v=mpALXah_PBg&t=4101s); `2026-02-23-from-zero-to-your-first-agentic-ai-workflow-in-26-minutes-cl` @ 8:53 (https://www.youtube.com/watch?v=tDGiWn0flK8&t=533s)
- **T14. Hand off state explicitly between sessions.** Use a handoff skill, a cross-session memory tool, or /compact with stated priorities. Why: each session starts from scratch, and re-explaining costs minutes and tokens. [demonstrated]
  Cites: `2026-04-20-how-to-never-hit-your-claude-session-limit-again` @ 9:51 (https://www.youtube.com/watch?v=_qZvORxGqI0&t=591s); `2026-05-03-i-tried-100-claude-code-skills-these-6-are-the-best` @ 9:44 (https://www.youtube.com/watch?v=eRS3CmvrOvA&t=584s)
- **T15. Use fresh context per task to fight context rot.** Spawn new sub-agents for each task rather than running one long session. Why: quality degrades as tokens build. [demonstrated]
  Cites: `2026-05-03-i-tried-100-claude-code-skills-these-6-are-the-best` @ 4:37 (https://www.youtube.com/watch?v=eRS3CmvrOvA&t=277s); `2026-08-10-build-sell-ai-saas-products-2-hour-course` @ 33:47 (https://www.youtube.com/watch?v=IVx8OSMbTss&t=2027s); `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 52:16 (https://www.youtube.com/watch?v=mpALXah_PBg&t=3136s)
- **T16. Filter what memory retrieval returns.** Fetch only the relevant items, and summarise where useful. Why: native memory pulled in irrelevant context and wasted tokens. [demonstrated]
  Cites: `2025-07-29-i-built-204-ai-automations-here-s-what-actually-matters` @ 16:09 (https://www.youtube.com/watch?v=wq001sxDTWw&t=969s); `2025-07-29-i-built-204-ai-automations-here-s-what-actually-matters` @ 15:28 (https://www.youtube.com/watch?v=wq001sxDTWw&t=928s)
- **T17. Disconnect unused MCP servers and prefer a CLI plus a skill.** Why: one server can add thousands of tokens per message. [opinion]
  Cites: `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:31:20 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=19880s); `2026-06-18-how-to-use-claude-code-better-than-98-of-people` @ 59:54 (https://www.youtube.com/watch?v=RzLV8sfFdMM&t=3594s)
- **T19. Keep one source of truth across tools.** Make agents.md a pointer to CLAUDE.md, and change both together. Why: switching costs stay low and the tools don't drift apart. [demonstrated]
  Cites: `2026-05-18-how-to-use-your-claude-code-projects-in-codex-in-5-mins` @ 5:53 (https://www.youtube.com/watch?v=kB9iMD0EjT8&t=353s)
- **T20. Use plan mode before agents change things.** Review the proposal, then approve. Why: you catch wrong approaches before they cost anything. [demonstrated]
  Cites: `2026-01-16-build-anything-with-claude-code-n8n-beginner-s-guide` @ 17:01 (https://www.youtube.com/watch?v=OCO3aq3G0mk&t=1021s); `2026-03-05-turn-claude-code-into-your-executive-assistant-in-27-mins` @ 17:31 (https://www.youtube.com/watch?v=mi4hcipESKQ&t=1051s); `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 6:03:33 (https://www.youtube.com/watch?v=mpALXah_PBg&t=21813s)
- **T21. Split planner, implementer and validator into separate sessions linked by handoff documents.** Why: it keeps each session out of the "dumb zone" of a bloated context. [opinion]
  Cites: `2026-06-18-how-to-use-claude-code-better-than-98-of-people` @ 33:40 (https://www.youtube.com/watch?v=RzLV8sfFdMM&t=2020s)
- **T22. Be specific in the plan about what happens when.** Plan the beats and the required outputs. Capable models can handle vague prompts if you add delegation and verification instructions. [opinion]
  Cites: `2026-09-25-opus-5-5-just-changed-video-editing-forever-free-skills` @ 16:12 (https://www.youtube.com/watch?v=7jHXoPGnA4c&t=972s); `2026-07-09-gpt-5-6-sol-made-this-entire-video` @ 4:24 (https://www.youtube.com/watch?v=J_jswzXhYJA&t=264s)
- **T23. Give loops a measurable done criterion.** Use "iterate until metric X equals Y", not "until you're satisfied". Why: subjective stop conditions never stop reliably. [demonstrated]
  Cites: `2026-06-19-finally-agent-loops-clearly-explained` @ 6:55 (https://www.youtube.com/watch?v=EuzYhzB0vbI&t=415s); `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22 (https://www.youtube.com/watch?v=FBVNS1l5Vb8&t=442s); `2026-01-25-agentic-workflows-just-changed-ai-automation-forever-claude` @ 16:15 (https://www.youtube.com/watch?v=AO5aW01DKHo&t=975s)
- **T24. Separate the critic from the worker.** Use a scorer or critic sub-agent per worker, and a final check that parts meet spec. For subjective output, define "good" for an LLM judge and test it. [demonstrated]
  Cites: `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22 (https://www.youtube.com/watch?v=FBVNS1l5Vb8&t=442s)
- **T25. Verify by running the thing.** Have agents build, view, click-test and use integrations until proven working. Why: self-reported success is not evidence. [demonstrated]
  Cites: `2026-08-10-build-sell-ai-saas-products-2-hour-course` @ 36:32 (https://www.youtube.com/watch?v=IVx8OSMbTss&t=2192s); `2025-04-17-n8n-just-leveled-up-ai-agents-anthropic-s-think-method` @ 17:20 (https://www.youtube.com/watch?v=WqyLxyALTt0&t=1040s)
- **T26. Review with parallel specialist reviewers who must reproduce each finding.** Cover logic, security, performance and edge cases. Why: it cuts false positives. [demonstrated]
  Cites: `2026-05-03-i-tried-100-claude-code-skills-these-6-are-the-best` @ 6:17 (https://www.youtube.com/watch?v=eRS3CmvrOvA&t=377s)
- **T27. Ask for several independent drafts and have the agent grade them against the goal.** Do not accept the first draft. Why: it gets closer to a final version, at extra usage. [opinion]
  Cites: `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22 (https://www.youtube.com/watch?v=FBVNS1l5Vb8&t=442s)
- **T29. Run independent work in parallel.** Examples are chapters, design variants, audits and test loops. Why: wall-clock time drops and context stays isolated. [demonstrated]
  Cites: `2026-06-09-how-to-build-claude-subagents-better-than-99-of-people` @ 22:12 (https://www.youtube.com/watch?v=e18sdZLwP7o&t=1332s); `2026-08-28-i-cloned-calendly-and-now-it-s-free-forever` @ 11:11 (https://www.youtube.com/watch?v=PYjbeY8sGLs&t=671s)
- **T30. Match the term to the setup.** Parallel agents are separate terminals. Sub-agents are delegated by a parent. Agent teams share a task list and message each other. Why: each pattern needs different coordination. [opinion]
  Cites: `2026-02-25-i-can-actually-watch-my-ai-agents-work-now` @ 8:44 (https://www.youtube.com/watch?v=62Rfe1w9NBc&t=524s)
- **T34. Sandbox each agent to specific tools, memory and repo.**  [opinion]
  Cites: `2026-03-06-cursor-automations-clearly-explained-worth-learning` @ 7:20 (https://www.youtube.com/watch?v=NDnv16PY2XQ&t=440s)
- **T35. Harden every webhook.** Use HTTPS, verify signing secrets, keep credentials in the credential store, and use production URLs only once secured. Why: webhooks are public entry points. [opinion]
  Cites: `2025-12-27-how-to-actually-deliver-ai-projects-apis-hosting-handover-ex` @ 4:44 (https://www.youtube.com/watch?v=xxARTGo_Oqg&t=284s); `2025-12-27-how-to-actually-deliver-ai-projects-apis-hosting-handover-ex` @ 4:03 (https://www.youtube.com/watch?v=xxARTGo_Oqg&t=243s)
- **T36. Keep human checkpoints where outputs are probabilistic or hard to reverse.** Review dialogue and prompts, and approve email drafts. Why: some outputs will be off. [demonstrated]
  Cites: `2025-11-25-master-n8n-fast-with-these-17-essential-nodes-real-examples` @ 6:11 (https://www.youtube.com/watch?v=D9MIGseFB3g&t=371s)
- **T37. Match model to job.** Use cheaper models for sub-agents and simple tasks, and the strongest for deep reasoning. Why: model tiers differ widely in cost. [demonstrated]
  Cites: `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:40:59 (https://www.youtube.com/watch?v=jdbOVepEtUE&t=20459s); `2026-06-19-glm-5-2-in-claude-code-is-blowing-my-mind` @ 6:42 (https://www.youtube.com/watch?v=2OD14-0cot4&t=402s)
- **T38. Use deterministic workflows where no AI is needed.** Let the harness route events and call the LLM only when needed. Why: AI calls are token-billed. [opinion]
  Cites: `2026-05-25-the-playbook-for-a-100m-ai-agency` @ 1:22:51 (https://www.youtube.com/watch?v=8ktcSaSTvxk&t=4971s); `2025-05-23-build-sell-n8n-ai-agents-8-hour-course-no-code` @ 5:13 (https://www.youtube.com/watch?v=Ey18PDiaAYI&t=313s); `2026-05-15-how-to-deploy-your-claude-automations-3-methods` @ 15:03 (https://www.youtube.com/watch?v=xJ5oz63mIec&t=903s)
- **T40. Build skills with a fixed framework.** Cover name and trigger, a one-sentence goal and output, steps, reference files, failure-mode rules, and a self-improvement loop. [demonstrated]
  Cites: `2026-02-27-master-95-of-claude-code-skills-in-28-minutes` @ 17:13 (https://www.youtube.com/watch?v=zKBPwDpBfhs&t=1033s); `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 6:25:10 (https://www.youtube.com/watch?v=mpALXah_PBg&t=23110s)
- **T42. Iterate fast and in small steps.** Each iteration is data that improves skills, agents, prompts and context. [opinion]
  Cites: `2026-06-15-learn-these-6-ai-skills-now-before-everyone-else-does` @ 10:13 (https://www.youtube.com/watch?v=3XIGcM7VICc&t=613s); `2026-02-19-building-beautiful-websites-with-claude-code-is-too-easy` @ 27:18 (https://www.youtube.com/watch?v=86HM0RUWhCk&t=1638s)
- **T43. Plan for failure, not only the happy path.** Test bad, missing and duplicate data. Add timeouts, error alerts and failure logs. [opinion]
  Cites: `2025-12-27-how-to-actually-deliver-ai-projects-apis-hosting-handover-ex` @ 10:21 (https://www.youtube.com/watch?v=xxARTGo_Oqg&t=621s); `2025-03-05-6-months-of-building-ai-agents-in-43-minutes-without-the-hyp` @ 32:13 (https://www.youtube.com/watch?v=QhujcQk8pyU&t=1933s); `2025-05-23-build-sell-n8n-ai-agents-8-hour-course-no-code` @ 8:17:00 (https://www.youtube.com/watch?v=Ey18PDiaAYI&t=29820s)
- **T44. Test scheduled tasks manually after creating them.** Why: each run is a fresh stateless session, so missing keys or permission prompts only show up in testing. [demonstrated]
  Cites: `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 2:52:05 (https://www.youtube.com/watch?v=mpALXah_PBg&t=10325s); `2026-05-15-how-to-deploy-your-claude-automations-3-methods` @ 17:14 (https://www.youtube.com/watch?v=xJ5oz63mIec&t=1034s)
- **T45. Invest in orchestration, not just the model.** Agents, verification checks, skills, harness and context matter more than which model you pick. [opinion]
  Cites: `2026-06-19-glm-5-2-in-claude-code-is-blowing-my-mind` @ 6:42 (https://www.youtube.com/watch?v=2OD14-0cot4&t=402s); `2026-04-01-claude-code-source-code-just-leaked-8-things-you-must-do` @ 10:22 (https://www.youtube.com/watch?v=tXtCK66fPj8&t=622s)
- **T46. Raise autonomy in steps.** Move from manual prompt-review-reprompt, to a critic loop, to a fleet of sub-agents each with a critic. Add max-iteration guardrails and keep a human available mid-run. [opinion]
  Cites: `2026-01-25-agentic-workflows-just-changed-ai-automation-forever-claude` @ 16:15 (https://www.youtube.com/watch?v=AO5aW01DKHo&t=975s)

## Quotable

No verbatim quotes kept: the source notes are summaries of auto-captions. Use the timestamp links above to hear the exact wording.

## Used by

[[topic-agent-security]], [[topic-claude-code-features]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-orchestration-patterns]], [[topic-skill-library-retrieval]]
