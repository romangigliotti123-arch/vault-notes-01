<!-- cold: rbx-manager/usage-limit-hit.md | read when: read only after a usage-limit message appears (stop, ledger, pause/resume steps). -->

## From skills/rbx-manager/references/usage-safety.md :: On a usage-limit message

1. Stop launching. Record in the ledger which jobs were running and in what state.
2. Tell the user in one line: what stopped, what is saved (report/progress files), the reset time shown in the message.
3. Pause/resume: stop running workers cleanly with the agent/task stop tool (do not kill processes), mark rows `needs_user` with "paused: usage". After the reset time, resume each by messaging the same agent ("continue from progress file X"), or if it is gone, brief one fresh worker from the progress file. Resume only if the user is present or has agreed to a scheduled resume; otherwise leave the resume to them.
4. Never work around limits (other accounts, hiding work).
