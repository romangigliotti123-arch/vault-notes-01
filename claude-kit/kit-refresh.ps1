# kit-refresh.ps1 - run right after the vault update (self-healing fetch + fast-forward) (by vault-update.ps1, the logon task, or by hand) so installed copies of the kit
# (agents, skills such as /game-dev-workflow, tools) refresh whenever the vault updates, and then syncs <vault>\Assets from the host share.
# 1) install.ps1 (idempotent; kit wins: a file you changed is backed up to claude-kit/backup/<date>/ and replaced). Env CLAUDE_KIT_SKIP=1 skips this part.
# 2) tools\assets-sync.py --vault <this vault>: downloads only new/changed asset files (about 2.7 GB the first time), deletes removed ones.
#    Quiet unless something changed; skips with one line when the share is unreachable (Tailscale off). Env CLAUDE_ASSETS_SKIP=1 skips this part.
# Prints a line only when something changed, so the log stays quiet. Never fails the caller. Env CLAUDE_KIT_HOME is honoured by install.ps1.
$ErrorActionPreference = 'Continue'
$env:CLAUDE_KIT_NOFOOTER = '1'
$d = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($env:CLAUDE_KIT_SKIP -ne '1') {
  $inst = Join-Path $d 'install.ps1'
  if (Test-Path -LiteralPath $inst) {
    try {
      $out = (& powershell -NoProfile -ExecutionPolicy Bypass -File $inst 2>&1 | Out-String).Trim()
    } catch { $out = 'kit refresh failed: ' + $_.Exception.Message }
    if ($out -notmatch 'installed 0 new, updated 0, unchanged \d+, replaced-yours 0 ') {
      Write-Output ("{0} kit-refresh: {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), ($out -replace "\s*\r?\n\s*", ' '))
    }
  }
}
if ($env:CLAUDE_ASSETS_SKIP -ne '1') {
  $sync = Join-Path $d 'tools\assets-sync.py'
  if (Test-Path -LiteralPath $sync) {
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
        $pyArgs = @($pyPre) + @('-I', $sync, '--vault', $vault)
        $shp = Join-Path $d 'tools\vault-shards.py'
        if (Test-Path -LiteralPath $shp) { & $py @($pyPre + @('-I', $shp, '--vault', $vault)) }   # extra repo shards (vault-notes-02, ...) from repos.json; silent when there are none
        & $py @pyArgs   # streams its own progress lines (first sync); prints nothing when nothing changed
      } catch { Write-Output ("{0} assets-sync: failed (non-fatal): {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $_.Exception.Message) }
    }
  }
}
exit 0
