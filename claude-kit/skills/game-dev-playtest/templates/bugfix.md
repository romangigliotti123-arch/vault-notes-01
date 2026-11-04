---
type: bugfix
game: <slug>
id: <id>
---
# Bug <id>: <symptom in one line>

Symptom: <what the player sees, steps, where>

## RED
Command: `<the one command that fails because of the bug>`
```
<output excerpt showing the failure>
```

Cause: <root cause, file:line>
Fix: <what changed, files>

## GREEN
Command: `<the same command>`
```
<output excerpt showing it passing>
```

Regression check kept at: <path>
Also re-run: static_scan.py <clean | findings>, placement verify <n/a | pass>
Premise tested (only after two failed fixes): <the assumption and how it was tested>
