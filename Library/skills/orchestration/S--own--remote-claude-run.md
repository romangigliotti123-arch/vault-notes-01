---
id: "remote-claude-run"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/remote-claude-run/SKILL.md"
description: "Run a headless Claude Code agent on another machine (Roman's Linux PC) over SSH, detached with a log, and collect its report."
orig_name: "remote-claude-run"
tags: [lib/skill, cat/orchestration, src/own]
---

# remote-claude-run

> Run a headless Claude Code agent on another machine (Roman's Linux PC) over SSH, detached with a log, and collect its report.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/remote-claude-run/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Remote Claude run (Linux PC "cachyos")

Prefer plain SSH commands (`tools\cachyos-run.ps1`) and use this only when the job needs judgement or long autonomous work: a remote Claude costs real usage.

1. Make sure the machine is awake and reachable: `powershell -File ~\claude-host\tools\cachyos-run.ps1 -Script 'echo ready'`. If not, `linux-power.ps1 -Action wake`, then retry until SSH answers.
2. Write the brief to the remote (self-contained, ends with the report format):
   `cachyos-run.ps1 -Script 'mkdir -p ~/claude-workspace/briefs ~/claude-host/logs; cat > ~/claude-workspace/briefs/job1.md <<"EOF"` ... `EOF'`
3. Short job (under ~8 min), foreground:
   `cachyos-run.ps1 -Script 'cd ~/claude-workspace && timeout 480 ~/.local/bin/claude -p --permission-mode bypassPermissions --model sonnet "$(cat briefs/job1.md)"'`
4. Long job, detached, then poll:
   `... 'cd ~/claude-workspace && setsid nohup timeout 3600 ~/.local/bin/claude -p --permission-mode bypassPermissions --model sonnet "$(cat briefs/job1.md)" > ~/claude-host/logs/job1.log 2>&1 < /dev/null & echo started'`
   then `... 'tail -n 40 ~/claude-host/logs/job1.log; pgrep -f "claude -p" || echo finished'` every minute or two.
5. Nothing may pop up on his screen: no terminals, no windows. GUI work (Sober/Roblox) needs `~/claude-host/tools/env.sh`, `shot.sh`, ydotool; run `quiet.sh off` first and `quiet.sh on` after if it was on.
6. Never suspend/reboot/power off except via `tools\linux-power.ps1`. Obey confirm-first rules.
7. Verify the report with your own commands; clean up the brief file; keep the log.

The login shell on the remote is fish: always go through `bash -s` (cachyos-run does).
