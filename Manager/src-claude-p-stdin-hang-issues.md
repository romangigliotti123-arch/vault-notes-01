---
tags: [manager-kb, source]
url: https://claudeissues.com/issue/64202-regression-in-2-1-158-claude-p-hangs-waiting-for-stdin-eof-on-termux-arm64 ; https://dev.to/creeta/claude-p-is-all-that-stands-between-you-and-a-hanging-ci-job-2peh ; issue-list snippets (claudeissues.com #9026, #21506, #36758, #36331, #42588, #50188, #48440)
type: practitioner-blog + GitHub issues mirror
author: community reporters; Creeta (dev.to, 2026-08-01)
published: 2025-10 to 2026-08
accessed: 2026-10-29
reliability: med (issue #64202 and dev.to opened; other issues snippet-only)
---
# `claude -p` over SSH / non-TTY: hangs and silent failures
## Key claims
- #64202 (opened 2026-05-31, "Closed - not planned" 2026-07-05): in 2.1.158 `claude -p "hello"` hangs, exit 124 under `timeout`, no stdout/stderr; `fd[0]` stays an open pipe, the process "blocks on stdin" until EOF; 2.1.157 worked; interactive mode fine. A regression of this kind is version specific.
- Search-snippet pattern across several other issues: headless runs with captured stdout or no TTY hang or exit 1 silently (#9026 "Claude CLI hangs without TTY despite -p", #21506 hang with stdout redirect in 2.1.22, #36758 `--continue` hangs when stdout captured, #36331/#50188/#42588 Desktop SSH remote: remote claude spawned without TTY exits code 1 or silently drops prompts with "no data on stdin"). Diagnoses are disputed (PTY vs stdin timing), so treat `ssh -t` vs no `-t` as an experiment, not a rule.
- Practical mitigations documented/implied: give stdin explicitly (pipe the prompt, or `< /dev/null` when the prompt is an argument), always wrap with `timeout`, check exit code 124, pin/record the CLI version, use `--output-format json` + `--max-turns`; dev.to guide says `--bare` (API key only; not usable on subscription auth) and pin versions "so a patch release cannot silently change agent behavior".
## Quotable
> The process blocks waiting for stdin to close and never produces output.

## Used by
[[topic-cross-device-agent-control]]
