---
name: rbx-mockup
description: "Toggle manual Nano Banana 2.1 UI mockups: on, off or status."
argument-hint: "[on | off | status]"
disable-model-invocation: true
---

# rbx-mockup

Result of the switch, run just now before you read this:

!`sh ".rbx/claude-kit/tools/pyrun" -I ".rbx/claude-kit/tools/ui_pref.py" toggle "$ARGUMENTS" || echo "UIPREF action=error (run python ui_pref.py status by hand)"`

The preference only says whether Claude gives the user a MANUAL Nano Banana 2.1 package (on). Off (the default, also when never answered) = Claude designs every UI button and screen layout itself before building (`rbx-ui-mockup`).

- Printed `UI mockups: ... (changed|already set)`: reply with that one line. Nothing else.
- `UIPREF action=status` (no argument, or `status`): check your tool list (ToolSearch "figma" when tools are deferred) for any tool whose name contains `figma`, then run `sh ".rbx/claude-kit/tools/pyrun" -I ".rbx/claude-kit/tools/ui_pref.py" status --tools "<those names, or none>"` and show its output as it is: the mode name (automatic design-first or manual Nano Banana 2.1), Figma connected or the one-line notice, and the preference file path.
- `action=error`: say so in one line and stop.
- Never ask for or store Figma tokens or accounts, never install anything, no keys, no billing talk.
