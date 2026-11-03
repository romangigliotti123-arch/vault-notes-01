---
id: "confidence-escalation-router"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/confidence-escalation-router/SKILL.md"
description: "Pattern and code template for routing AI answers inside an automation: auto-accept when confidence is at or above a threshold (for example 80 percent), otherwise send to a human review queue, with retries and a fallback model chain on failure, logging each decision so the cutoff can be tuned. Also covers default-fast, escalate-to-thinking-model for hard problems. Use when AI output feeds an automation that sometimes needs a human, or the user says confidence threshold, human in the loop, fall back to another model, retry then escalate, or review queue."
orig_name: "confidence-escalation-router"
orig_argument_hint: "[threshold] [model chain]"
tags: [lib/skill, cat/orchestration, src/own]
---

# confidence-escalation-router

> Pattern and code template for routing AI answers inside an automation: auto-accept when confidence is at or above a threshold (for example 80 percent), otherwise send to a human review queue, with retries and a fallback model chain on failure, logging each decision so the cutoff can be tuned. Also covers default-fast, escalate-to-thinking-model for hard problems. Use when AI output feeds an automation that sometimes needs a human, or the user says confidence threshold, human in the loop, fall back to another model, retry then escalate, or review queue.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/confidence-escalation-router/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--model-routing]]

Creator videos (notes are in the AI Library Vault, Creators/videos): 2025-08-07-why-99-of-ai-automations-fail-in-production, 2026-02-27-336-ways-to-use-openclaw-here-s-what-actually-works, 2025-02-27-how-i-use-llms, 2026-10-28-anthropic-just-shipped-claude-2-0-master-it-in-17-minutes, 2026-10-29-jev-for-images-just-changed-visual-automations-forever

---
# confidence-escalation-router

## Contract
Input: `{answer, confidence 0-1, item_id, context}`, config `{threshold, retries, model_chain}`. Output: `{route: auto|review|failed, reason, model_used, attempts}` plus a log line and, for `review`, a queue item.

## Steps
1. **Get a confidence signal**. Prefer a checkable one: the answer passes schema validation, a deterministic check, or agreement between two independent runs. Self-reported model confidence is a weak signal; if used, calibrate it (see Tune).
2. **Retry on failure** (API error, invalid JSON): up to `retries` (default 3) with backoff; same model first.
3. **Fallback chain**: after retries, move to the next model in `model_chain` (for example a cheap primary, a stronger fallback). Log each hop.
4. **Route**: `confidence >= threshold` and checks pass -> `auto`; else `review`. Never `auto` after a failed validation.
5. **Review queue item**: id, question, answer, confidence, why flagged, a link or context, status. Human decision is stored back as ground truth.
6. **Escalate for hard problems**: default to a fast non-thinking model; if the check fails or the task is known-hard (math, multi-step code), rerun on a thinking/stronger model once before routing to review.

## Code template (language-neutral)
```
for model in model_chain:
  for attempt in 1..retries:
    r = call(model, item)
    if valid(r): break
  if valid(r): break
route = auto if (valid(r) and r.confidence >= threshold) else review
log(item_id, route, model, attempts, r.confidence, reason)
```

## Tune
Collect logged cases with human outcomes. Plot confidence vs. correct rate; set the threshold where auto accuracy meets the target (say 98 percent). Review rejected-auto cases monthly.

## Failure modes
- Threshold picked once and never tuned.
- Human queue grows unbounded: add an SLA and a daily digest.
- Confidence inflated by the model: use external checks.

## Related
llm-answer-grader (scoring), automation-design-framework, model-routing (library skill for choosing models).

## Sources
Idea from AI-creator research (catalogue ideas idea-0035, idea-0231). Credit and where it appears:
- Nate Herk, "Why 99% of AI Automations Fail in Production" (2025-08-07) @ 5:00, https://www.youtube.com/watch?v=Irk4-DO5qgM&t=300s. Seen there as: Fallback agent (OpenRouter)
- RoboNuggets (Jay E), "336 Ways to Use OpenClaw (here's what actually works)" (2026-02-27) @ 3:49, https://www.youtube.com/watch?v=miJLo234L9s&t=229s. Seen there as: Model fallback chain
- Andrej Karpathy, "How I use LLMs" (2025-02-27) @ 29:46, https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1786s. Seen there as: Thinking-model escalation
- RoboNuggets (Jay E), "Anthropic Just Shipped Claude 2.0 (Master it in 17 minutes)" (2026-10-28) @ 13:48, https://www.youtube.com/watch?v=yMnFHFf43Qg&t=828s. Seen there as: Advisor
- RoboNuggets (Jay E), ""Jev for Images" Just Changed Visual Automations Forever" (2026-10-29) @ 5:35, https://www.youtube.com/watch?v=0SFKD0xkdR8&t=335s. Seen there as: Confidence-threshold router
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
