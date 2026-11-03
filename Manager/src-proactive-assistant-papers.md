---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2410.04596 ; https://arxiv.org/abs/2410.12361
type: paper
author: Chen et al. (CMU/Microsoft) "Need Help? Designing Proactive AI Assistants for Programming" CHI 2025; Lu et al. (Tsinghua) "Proactive Agent / ProactiveBench"
published: 2024-10 (v2 2025-02 and v3 2024-12)
accessed: 2026-10-29
reliability: med-high (controlled study for first; benchmark with small F1 for second)
---
# Proactive assistant studies
## Key claims
- Chen et al.: randomized study of proactive chat assistant in an editor. Persistent, too-frequent suggestions were "distracting" and "annoying" ("the non-proactive chat assistant was best because it didn't interrupt what I was doing"); timing tied to the user's recent activity/flow is a design consideration; suggestions accepted were the "actionable" ones (brainstorming functionality, debugging latent errors: 18 accepts each) while "explain code"/"doc pointers" were accepted once each (69 accepts vs 6 rejects among 75 explicit decisions); the same assistant with better timing was described as "a second set of eyes". Design consideration: user accept/reject should feed back into future proactive decisions.
- Lu et al.: ProactiveBench of 6,790 events; humans labelled proactive task predictions accepted/rejected to train a reward model; best fine-tuned model F1 66.47% at deciding when to proactively offer help => even tuned models misjudge about a third of "should I speak up" decisions.
## Quotable
> untimely and irrelevant proactive messages may compromise the success of the interaction (Chen et al., related work)

## Used by
[[topic-personal-assistant-agents]], [[topic-remote-mobile-ux]]
