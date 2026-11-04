# vault-published.ps1 - last line of /rbx-update (Windows, no python needed): "Your vault is up to date as of Thursday 5 November 2026, 8:40 am (local time)".
# Time = newest commit date (git log -1 --format=%cI) of the vault clone and of the kit folder's repo (when that is a different repo), in the machine's local time zone.
# No git or no date: prints "Your vault is up to date." Never fails (exit 0). Usage: vault-published.ps1 [-Vault DIR] [-Kit DIR] [-UtcOffset +HH:MM]  (env VAULT_PUBLISHED_UTC_OFFSET = test hook that fixes the zone)
param([string]$Vault = '', [string]$Kit = '', [string]$UtcOffset = '')
$ErrorActionPreference = 'SilentlyContinue'
$plain = 'Your vault is up to date.'
try {
  $inv = [Globalization.CultureInfo]::InvariantCulture
  if (-not $UtcOffset) { $UtcOffset = $env:VAULT_PUBLISHED_UTC_OFFSET }
  if (-not $Vault) { $Vault = if ($env:CLAUDES_VAULT) { $env:CLAUDES_VAULT } else { Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)) } }
  if (-not $Kit) { $Kit = Join-Path $Vault 'claude-kit' }
  $git = (Get-Command git.exe -ErrorAction SilentlyContinue | Select-Object -First 1).Source
  if (-not $git -and (Test-Path 'C:\Program Files\Git\cmd\git.exe')) { $git = 'C:\Program Files\Git\cmd\git.exe' }
  $best = $null; $seen = @{}
  if ($git) {
    $env:GIT_TERMINAL_PROMPT = '0'
    foreach ($d in @($Vault, $Kit)) {
      if (-not $d -or -not (Test-Path -LiteralPath $d -PathType Container)) { continue }
      $top = ((& $git -C $d rev-parse --show-toplevel 2>$null) | Out-String).Trim()
      if (-not $top) { $top = $d }
      $key = $top.Replace('/', '\').ToLowerInvariant()
      if ($seen.ContainsKey($key)) { continue }
      $seen[$key] = 1
      $s = ((& $git -C $d log -1 --format=%cI 2>$null) | Out-String).Trim()
      $dt = [DateTimeOffset]::MinValue
      if ($s -and [DateTimeOffset]::TryParse($s, $inv, [Globalization.DateTimeStyles]::None, [ref]$dt)) { if ($null -eq $best -or $dt -gt $best) { $best = $dt } }
    }
  }
  if ($null -eq $best) { Write-Output $plain; exit 0 }
  if ($UtcOffset) { $sign = if ($UtcOffset.StartsWith('-')) { -1 } else { 1 }; $p = $UtcOffset.TrimStart('+', '-').Split(':'); $m = if ($p.Count -gt 1) { [int]$p[1] } else { 0 }; $loc = $best.ToOffset([TimeSpan]::FromMinutes($sign * ([int]$p[0] * 60 + $m))) }
  else { $loc = $best.ToLocalTime() }
  $ampm = if ($loc.Hour -lt 12) { 'am' } else { 'pm' }
  Write-Output ('Your vault is up to date as of ' + $loc.ToString('dddd d MMMM yyyy, h:mm', $inv) + ' ' + $ampm + ' (local time)')
} catch { Write-Output $plain }
exit 0
