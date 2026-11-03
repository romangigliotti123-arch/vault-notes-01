---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2606.09863
type: paper
author: Laksh Advani
published: 2026-06-01
accessed: 2026-10-29
reliability: med-high (large trajectory corpora w/ ground truth; single author preprint; structured-API benchmarks only)
---
# From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents
## Key claims
- Definition: false success = "a mismatch between the agent's natural-language claim of completion and the programmatic environment state."
- Corpora: 9,876 tau2-bench trajectories (8 model families incl. Claude Opus 4.5 / Sonnet 4.5, GPT-5.2, Gemini 3) and 1,879 AppWorld trajectories (4 families). Of 1,730 tau2 failures: 616 false success (35.6%), 753 honest failure (43.5%), 361 ambiguous.
- Prevalence: 45-48% of failures in single-control tau2 domains (airline 45%, retail 47%); telecom 3% (only 15 FS cases, hypothesis); per-model 13% (GPT-5.2) to 79% (Qwen3-Max-Thinking-Preview); AppWorld self-assessing coding agents 75.8% of failures were false successes (67% LLaMA-3 to 89% DeepSeekCoder). Easier tasks show higher false-success rates.
- LLM judges fail: "no configuration across 5 judges, 5 prompt strategies, and full task specifications exceeds AUROC 0.65 on tau2-bench" (best 0.640, Sonnet 4.5), 0.54 on AppWorld. "Judges rely on surface completion proxies - confident closing language... rather than verified state changes."
- Cheap detectors (TF-IDF + XGBoost) reach AUROC 0.83 (tau2) and 0.95 (AppWorld); top features are completion phrases ("has been", "successfully", "is now", "all set") vs honest-failure phrases ("i cannot", "to a human"). At a 10% flag rate precision is 50%. Detectors and judges flip on ~20-25% of adversarial rewrites; domain transfer weak (0.68-0.73).
- Recommendation: use lightweight domain-calibrated detectors as triage, not LLM judges as primary monitor; "reserve direct trajectory-environment consistency checks for higher-stakes deployments."
- Caveat for us: structured API environments, not open-ended sysadmin/coding work; older/other models for AppWorld.
## Quotable
> "Judges rely on surface completion proxies -- confident closing language in tau2-bench and coarse action-sequence volume in AppWorld -- rather than verified state changes."

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-report-formats-and-verification]]
