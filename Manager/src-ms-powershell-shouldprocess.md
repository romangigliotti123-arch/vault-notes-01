---
tags: [manager-kb, source]
url: https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-shouldprocess
type: official-doc
author: Microsoft Learn (original: Kevin Marquette)
published: 2024-09-24 (updated 2026-05-27)
accessed: 2026-10-29
reliability: high (official PowerShell docs)
---
# Everything you wanted to know about ShouldProcess (-WhatIf / -Confirm)
## Key claims
- `[CmdletBinding(SupportsShouldProcess)]` auto-creates `-WhatIf` and `-Confirm`; call `$PSCmdlet.ShouldProcess('TARGET','OPERATION')` as close to the change as possible (inside the foreach for collections) so setup/validation still runs under -WhatIf.
- `-WhatIf` prints "What if: Performing the operation X on target Y" and returns false; `ConfirmImpact='High'` prompts by default (bad for agents unless `-Confirm:$false`/`-Force` handled).
- `-Force` must be implemented by the author: `if ($Force -and -not $PSBoundParameters.ContainsKey('Confirm')) { $ConfirmPreference = 'None' }`; -WhatIf must still win over -Force.
- Pitfall: `-WhatIf` does not propagate reliably between script modules; "never trust it to work for script modules" so pass `-WhatIf:$WhatIfPreference` explicitly.
- `$PSCmdlet.ShouldContinue` always prompts (interactive-only) so avoid it in agent-facing scripts.
## Quotable
> The option to run it with -WhatIf can make a big difference.

## Used by
[[topic-tool-and-mcp-design]]
