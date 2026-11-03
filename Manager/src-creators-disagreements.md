---
tags: [manager-kb, source]
url: (synthesis of video notes; see per-claim video ids in the three creator notes)
type: video
author: Nate Herk, RoboNuggets, Andrej Karpathy
published: 2025-2026
accessed: 2026-11-01
reliability: low-medium (practitioner opinion; positions paraphrased from auto-caption notes)
---
# Where the AI creators disagree on running agents

## Key claims

- **Long-running context.** Karpathy says to reset context on topic change. Nate notes loops keep continuous context as a pro, but context grows each firing and rots. `2025-02-27-how-i-use-llms` @ 16:38 vs `2026-03-07-this-new-claude-code-feature-is-a-game-changer` @ 1:43
- **Human review versus automated review.** Nate pitches an evaluator-optimizer loop as automating human review. RoboNuggets calls human-in-the-loop essential for probabilistic output. `2025-05-23-build-sell-n8n-ai-agents-8-hour-course-no-code` @ 5:07 vs `2025-12-09-ai-brand-ads-so-cinematic-you-ll-think-they-cost-30-000-it-c` @ 19:06
- **Permissions.** Nate's course setup refers to enabling "allow dangerously skip permissions" (text truncated). RoboNuggets stresses guardrails and warns against tools that lack them. `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 3:44:38 vs `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 14:49
- **Always-on agents.** RoboNuggets pitches a 24/7 multi-agent system. Nate says agents are not literally always on; they wake in loops. `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 0:00 vs `2026-03-06-cursor-automations-clearly-explained-worth-learning` @ 7:20
- **Verification versus cost.** Nate wants near-final, verified output. RoboNuggets notes verification loops made Fable about 3x costlier and slower than a cheaper model. `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22 vs `2026-07-23-i-made-fable-5-and-kimi-k3-build-the-same-app-raw-results` @ 23:07
- **Model switching.** Nate recommends mixing models (cheap sub-agents, a delegating orchestrator). RoboNuggets warns that switching models inside one chat forfeits cache discounts. `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:40:59 vs `2026-10-12-claude-5-5-model-mistakes-you-may-still-be-making-23-tips-an` @ 2:10

## Quotable

None kept verbatim; positions are paraphrased. Video notes (AI Library Vault, `Creators/videos/`) hold the timestamps.

## Used by

[[topic-orchestration-patterns]], [[topic-context-window-management]], [[topic-agent-security]], [[topic-model-effort-routing-cost]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]]
