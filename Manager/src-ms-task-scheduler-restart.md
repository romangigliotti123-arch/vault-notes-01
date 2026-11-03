---
tags: [manager-kb, source]
url: https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-restartonfailure-settingstype-element
type: official-doc
author: Microsoft
published: 2018-05-31 (page ms.date)
accessed: 2026-10-29
reliability: high (official schema doc) + local probe of ClaudeHost task XML
---
# Task Scheduler RestartOnFailure + local ClaudeHost settings
## Key claims
- RestartOnFailure: "the Task Scheduler will attempt to restart the task if the task fails for any reason"; children Count and Interval; both must be set.
- LOCAL PROBE (Export-ScheduledTask ClaudeHost, 2026-10-29): trigger = LogonTrigger only; action = `powershell.exe -NoExit -NoProfile -ExecutionPolicy Bypass -File boot-claude.ps1`; RestartOnFailure Count 5 Interval PT1M; ExecutionTimeLimit PT0S (unlimited); MultipleInstancesPolicy IgnoreNew.
- Consequence: because of `-NoExit`, the task's process (powershell) stays alive after claude.exe exits, so the task never "fails" and RestartOnFailure never fires; with the 5-minute watchdog disabled (2026-10-28) nothing restarts a dead master. See [[topic-long-running-always-on-agents]] candidate changes.

## Used by
[[topic-long-running-always-on-agents]]
