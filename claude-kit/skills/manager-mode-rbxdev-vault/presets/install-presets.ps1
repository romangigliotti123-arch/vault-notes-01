# Installs the manager-mode-rbxdev-vault presets into ~/.claude/agents. Never overwrites a differing file: writes <name>.new instead.
$ErrorActionPreference = 'Stop'
$src = $PSScriptRoot
$dst = Join-Path $env:USERPROFILE '.claude\agents'
New-Item -ItemType Directory -Force $dst | Out-Null
foreach ($f in 'sonnet-worker', 'haiku-scout', 'opus-builder') {
  $s = Join-Path $src "$f.md"; $t = Join-Path $dst "$f.md"
  if (-not (Test-Path -LiteralPath $t)) { Copy-Item -LiteralPath $s -Destination $t; "installed $t" }
  elseif ((Get-FileHash $s).Hash -eq (Get-FileHash $t).Hash) { "unchanged $t" }
  else { Copy-Item -LiteralPath $s -Destination "$t.new" -Force; "kept your $t; wrote $t.new" }
}
'Start a new session or run /agents to load the presets.'
