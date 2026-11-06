# kit-refresh.ps1 - run right after the vault update (self-healing fetch + fast-forward) (by vault-update.ps1, the logon task, or by hand) so installed copies of the kit
# (agents, skills such as /rbx-workflow, tools) refresh whenever the vault updates, and then syncs <vault>\Assets from the public vault-assets repositories.
# 1) install.ps1 (idempotent; every vault file is overwritten with the incoming version, files that left the kit are removed). Env CLAUDE_KIT_SKIP=1 skips this part.
# 2) tools\assets-sync.py --vault <this vault>: downloads only new/changed asset files (about 2.7 GB the first time), deletes removed ones.
#    Quiet unless something changed; skips with one line when no asset source is reachable (offline). Env CLAUDE_ASSETS_SKIP=1 skips this part.
# 3) tools\refs-sync.py: fetches/updates the public Roblox reference screenshots (repos vault-refs-NN from repos.json, ~30 MB) into <claude config dir>\claude-kit\roblox-reference and
#    writes <claude config dir>\claude-kit\reference-path.txt (read by the visual-QA / art-direction skills). Silent when offline or up to date. Env CLAUDE_REFS_SKIP=1 skips this part.
# Prints a line only when something changed, so the log stays quiet. Never fails the caller. Env CLAUDE_KIT_HOME is honoured by install.ps1.
# Last line (only when the kit changed and the caller is not the current vault-update.ps1, which prints it itself): "Your vault is up to date as of ... (local time)" (tools\vault-published.ps1).
$ErrorActionPreference = 'Continue'
$env:CLAUDE_KIT_NOFOOTER = '1'
$env:CLAUDE_KIT_NOLOAD = '1'   # install.ps1 does not load the vault folder; step 1b below does (its output is shown, not folded into the log line)
$d = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($env:CLAUDE_KIT_SKIP -ne '1') {
  $inst = Join-Path $d 'install.ps1'
  if (Test-Path -LiteralPath $inst) {
    try {
      $out = (& powershell -NoProfile -ExecutionPolicy Bypass -File $inst 2>&1 | Out-String).Trim()
    } catch { $out = 'kit refresh failed: ' + $_.Exception.Message }
    $chk = (($out -split "`r?`n" | Where-Object { $_ -notmatch '^similar skills of yours' }) -join "`n").Trim()
    if ($chk -notmatch '^claude-kit: installed 0 new, updated 0, unchanged \d+ \(into [^\r\n]*\)$') {
      $kChanged = $true
      Write-Output ("{0} kit-refresh: {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), ($out -replace "\s*\r?\n\s*", ' '))
    }
  }
}
# 1b) tools\vault-mode.py sync --quiet: folders that have Roblox dev mode loaded (/rbx-load) get the updated skills/agents; silent when nothing changed. Env CLAUDE_MODE_SKIP=1 skips it.
$vmode = if ($env:CLAUDE_CONFIG_DIR) { Join-Path $env:CLAUDE_CONFIG_DIR 'claude-kit\tools\vault-mode.py' } elseif ($env:CLAUDE_KIT_HOME) { Join-Path $env:CLAUDE_KIT_HOME '.claude\claude-kit\tools\vault-mode.py' } else { Join-Path $env:USERPROFILE '.claude\claude-kit\tools\vault-mode.py' }
if (($env:CLAUDE_MODE_SKIP -ne '1') -and (Test-Path -LiteralPath $vmode)) {
  try {
    foreach ($c in @(@('python'), @('python3'), @('py', '-3'))) {
      $exe = (Get-Command $c[0] -ErrorAction SilentlyContinue | Select-Object -First 1)
      if (-not $exe) { continue }
      $pre = @(); if ($c.Count -gt 1) { $pre = $c[1..($c.Count - 1)] }
      & $exe.Source @pre -c "import sys" *> $null
      if ($LASTEXITCODE -eq 0) { & $exe.Source @($pre + @('-I', $vmode, 'load', '--project', (Split-Path -Parent $d), '--quiet', '--announce')); break }
    }
  } catch { }
}
$sync = Join-Path $d 'tools\assets-sync.py'
$refs = Join-Path $d 'tools\refs-sync.py'
$doAssets = ($env:CLAUDE_ASSETS_SKIP -ne '1') -and (Test-Path -LiteralPath $sync)
$doRefs = ($env:CLAUDE_REFS_SKIP -ne '1') -and (Test-Path -LiteralPath $refs)
if ($doAssets -or $doRefs) {
  $py = $null; $pyPre = @()
  foreach ($c in @(@('python'), @('python3'), @('py', '-3'))) {
    $exe = (Get-Command $c[0] -ErrorAction SilentlyContinue | Select-Object -First 1)
    if (-not $exe) { continue }
    $pre = @(); if ($c.Count -gt 1) { $pre = $c[1..($c.Count - 1)] }
    & $exe.Source @pre -c "import sys" *> $null
    if ($LASTEXITCODE -eq 0) { $py = $exe.Source; $pyPre = $pre; break }
  }
  if (-not $py) {
    Write-Output ("{0} assets-sync: skipped (no working python; install Python 3 and run vault-update.ps1)" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))
  } else {
    try {
      $vault = Split-Path -Parent $d
      if ($doAssets) {
        $shp = Join-Path $d 'tools\vault-shards.py'
        if (Test-Path -LiteralPath $shp) { & $py @($pyPre + @('-I', $shp, '--vault', $vault)) }   # extra repo shards (vault-notes-02, ...) from repos.json; silent when there are none
      }
      if ($doRefs) { & $py @($pyPre + @('-I', $refs)) }   # reference screenshots (vault-refs-NN) + reference-path.txt; silent when offline or unchanged
      if ($doAssets) { & $py @($pyPre + @('-I', $sync, '--vault', $vault)) }   # streams its own progress lines (first sync); prints nothing when nothing changed
    } catch { Write-Output ("{0} assets-sync: failed (non-fatal): {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $_.Exception.Message) }
  }
}
if ($kChanged -and -not $env:VAULT_UPDATE_LINE) {
  $pl = ''
  $pubScript = Join-Path $d 'tools\vault-published.ps1'
  if (Test-Path -LiteralPath $pubScript) { try { $pl = @((& powershell -NoProfile -ExecutionPolicy Bypass -File $pubScript -Vault (Split-Path -Parent $d) -Where | Out-String) -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -Last 2) -join "`n" } catch { } }
  if (-not $pl) { $pl = 'Your vault is up to date.' }
  Write-Output $pl
}
exit 0
