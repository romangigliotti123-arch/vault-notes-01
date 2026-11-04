# rbx-low-usage PowerShell fallback (used by the `lum` launcher only when no Python 3 works). Handles: hook, run/on/off/status.
# install-hooks / uninstall-hooks need Python (JSON merge of settings.json). The rules text is a copy of RULES in lum.py; keep in step.
param([Parameter(Position = 0)][string]$Cmd = 'run', [Parameter(Position = 1)][string]$Arg = '')
$ErrorActionPreference = 'Stop'
$c = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE '.claude' }
$m = Join-Path $c 'state\rbx-low-usage.on'
$prefix = 'low usage mode enabled.'
$rules = "LOW USAGE MODE IS ON (the user turned it on with /rbx-low-usage; '/rbx-low-usage off' ends it). Begin EVERY reply with exactly: $prefix (all lowercase, then continue). Rules: use the cheapest model that fits (sonnet by default, haiku for lookups, simple edits and any subagent, opus only if the user asks). At most 1 subagent at a time; no agent teams, workflows or fan-out. Keep replies short: answer first, no preamble or recap. Keep tool output small: targeted reads (offset/limit), grep, head/tail, never dump whole files or repos. No screenshots or images unless essential. Batch independent tool calls in one message. Ask before anything expensive (long runs, big reads, many agents). If the conversation is large, say once that /compact or /clear would save usage."
function Hooks { try { $s = Get-Content -LiteralPath (Join-Path $c 'settings.json') -Raw -ErrorAction Stop; if ($s -match 'rbx-low-usage/scripts/lum') { 'installed' } else { 'MISSING' } } catch { 'MISSING' } }
function Line([string]$a) { 'LUM action={0} mode={1} hooks={2} config={3}' -f $a, $(if (Test-Path -LiteralPath $m) { 'on' } else { 'off' }), (Hooks), $c }
try {
  if ($Cmd -eq 'hook') {
    if (-not (Test-Path -LiteralPath $m)) { exit 0 }
    $ev = if ($Arg) { $Arg } else { 'UserPromptSubmit' }
    $ctx = if ($ev -eq 'SessionStart') { '(Restored at session start/resume/compaction.) ' + $rules } else { $rules }
    $o = @{ hookSpecificOutput = @{ hookEventName = $ev; additionalContext = $ctx } }
    [Console]::Out.WriteLine(($o | ConvertTo-Json -Compress -Depth 5)); exit 0
  }
  $act = if ($Cmd -eq 'run') { if ($Arg) { $Arg.ToLower() } else { 'on' } } else { $Cmd.ToLower() }
  switch ($act) {
    'on' { New-Item -ItemType Directory -Force (Split-Path -Parent $m) | Out-Null; '{"since":"' + (Get-Date -Format s) + '"}' | Set-Content -LiteralPath $m -Encoding ascii; Line 'on' }
    'off' { Remove-Item -LiteralPath $m -Force -ErrorAction SilentlyContinue; Line 'off' }
    'status' { Line 'status' }
    default { Write-Output ('lum.ps1: ' + $act + ' needs Python 3 (install it, then run again).'); exit 2 }
  }
} catch { if ($Cmd -eq 'hook') { exit 0 } else { Write-Output ('lum.ps1 error: ' + $_.Exception.Message); exit 1 } }
