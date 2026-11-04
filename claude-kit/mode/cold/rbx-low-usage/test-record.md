<!-- cold: rbx-low-usage/test-record.md | read when: read only to see what was tested when the mode was built. -->

## From skills/rbx-low-usage/references/how-it-works.md :: Test record (2026-11-01, temp config, haiku, headless)

On via skill; 3 further prompts in the same session, each reply began `low usage mode enabled.`; `/compact` then another prompt, still prefixed (transcript: compact_boundary, then SessionStart and UserPromptSubmit attachments); a fresh session without the skill, prefixed by hooks alone; off, then two prompts without the prefix; PowerShell fallback output identical to Python's; hook merge/remove round-trip restores the original settings.json.
