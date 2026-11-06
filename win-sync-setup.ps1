# win-sync-setup.ps1 - keeps the Obsidian vault "claudes-vault" fresh on this Windows PC: clone, kit install, asset sync, and a task that updates at every logon
# (NO 15-minute polling). On demand: vault-update.ps1 in the vault folder, or /rbx-update in Claude.
# User-level only: no admin needed, no window shown. Safe to run again. Pull-only: never commits or pushes.
# Usage:  powershell -NoProfile -ExecutionPolicy Bypass -File win-sync-setup.ps1 [-Dest <folder>] [-Uninstall] [-SkipKit] [-SkipAssets]
# Assets (about 2.7 GB the first time) are synced into <vault>\Assets from the host PC's Tailscale share, never from GitHub.
# Exit codes: 0 ok, 1 git/gh missing or clone failed, 2 not logged in to GitHub (run: gh auth login), 3 task setup failed.
param(
  [string]$Dest = (Join-Path $env:USERPROFILE 'Obsidian\claudes-vault'),
  [string]$TaskName = 'ClaudesVaultPull',
  [string]$StateDir = (Join-Path $env:LOCALAPPDATA 'claudes-vault-sync'),
  [int]$Minutes = 0,   # ignored (kept so old command lines still work); there is no interval any more
  [switch]$Uninstall,
  [switch]$SkipKit,
  [switch]$SkipAssets,
  [switch]$SkipAiVault   # skip the companion AI Library Vault clone (ai-library-vault next to the vault)
)
$ErrorActionPreference = 'Stop'
$Repo = 'romangigliotti123-arch/claudes-vault'

if ($Uninstall) {
  Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force $StateDir -ErrorAction SilentlyContinue
  Write-Output "Removed task $TaskName. The vault folder $Dest is untouched."
  exit 0
}

# pick up PATH changes made by winget in this session
$env:Path = $env:Path + ';' + [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
$git = (Get-Command git.exe -ErrorAction SilentlyContinue).Source
if (-not $git) { Write-Output 'Missing: git. Install: winget install --id Git.Git -e --silent'; exit 1 }
$gh = (Get-Command gh.exe -ErrorAction SilentlyContinue).Source

#region vault-heal (same block in vault-update.ps1 and win-sync-setup.ps1)
# Self-healing update of the READ-ONLY vault clone. Never throws, never runs git clean. Returns lines to print (or $null when nothing special happened).
# Sets core.autocrlf/safecrlf false (no false "modified" from CRLF), fetches, fast-forwards; if local changes or divergence block that, it first saves
# the real changes as <StateDir>\local-changes-<timestamp>.patch (+ a list of untracked files; newest 5 kept), then resets to origin/main.
# PROTECTED USER DATA: <vault>\My Research\ and every folder that contains PROTECTED-RESEARCH.md are added to .git\info\exclude on every run (so git never
# treats them as removable), are never part of a patch, and are never touched by reset. Untracked files are never removed by a normal update; the update
# Before a reset, untracked files that upstream now tracks (they would be overwritten) are copied to <StateDir>\collision-backup-<timestamp>.
# Full view (marker file <vault>\.full-view): after every update .obsidian\app.json gets userIgnoreFilters = ["Assets/", "Games/", "Models/"] only; that rewrite is never saved as a "local change".
function Write-JsonNoBom([string]$path, $obj) {
  $txt = ($obj | ConvertTo-Json -Depth 20)
  [IO.File]::WriteAllText($path, $txt + "`n", (New-Object Text.UTF8Encoding $false))
}
function Get-JsonWithoutIgnore([string]$text) {
  $o = $text | ConvertFrom-Json
  [void]$o.PSObject.Properties.Remove('userIgnoreFilters')
  return ($o | ConvertTo-Json -Depth 20 -Compress)
}
function Set-FullViewConfig([string]$vault) {
  $f = Join-Path $vault '.obsidian\app.json'
  $text = '{}'; if (Test-Path -LiteralPath $f) { $text = [IO.File]::ReadAllText($f) }
  if (-not $text.Trim()) { $text = '{}' }
  $o = $text | ConvertFrom-Json
  if ($o.PSObject.Properties['userIgnoreFilters']) { $o.userIgnoreFilters = @('Assets/', 'Games/', 'Models/') }
  else { Add-Member -InputObject $o -NotePropertyName userIgnoreFilters -NotePropertyValue @('Assets/', 'Games/', 'Models/') }
  New-Item -ItemType Directory -Force (Split-Path $f -Parent) | Out-Null
  Write-JsonNoBom $f $o
}
function Add-GitExclude([string]$vault, [string]$line) {
  $ex = Join-Path $vault '.git\info\exclude'
  New-Item -ItemType Directory -Force (Split-Path $ex -Parent) | Out-Null
  $have = @(); if (Test-Path -LiteralPath $ex) { $have = @(Get-Content -LiteralPath $ex) }
  if ($have -notcontains $line) { Add-Content -LiteralPath $ex -Value $line -Encoding ASCII }
}
# Protected folders, relative with forward slashes, no trailing slash: 'My Research' + every folder holding PROTECTED-RESEARCH.md (remembered in .git\info\protected-folders.txt).
function Get-ProtectedDirs([string]$git, [string]$vault) {
  $set = New-Object System.Collections.Generic.List[string]
  $set.Add('My Research')
  $set.Add('Games'); $set.Add('Models')   # per-game communities + Games/_Reusable: always protected
  $reg = Join-Path $vault '.git\info\protected-folders.txt'
  $cand = @(); if (Test-Path -LiteralPath $reg) { $cand += @(Get-Content -LiteralPath $reg) }
  foreach ($f in @(& $git -C $vault -c core.quotepath=false ls-files -o --exclude-standard -- '*PROTECTED-RESEARCH.md' 2>$null)) {
    if ($f -match '^(.+)/PROTECTED-RESEARCH\.md$') { $cand += $Matches[1] }
  }
  foreach ($d in $cand) {
    $d = "$d".Trim()
    if ($d -and $d -ne 'My Research' -and $d -ne 'Games' -and $d -ne 'Models' -and -not $d.StartsWith('Games/') -and -not $d.StartsWith('Models/') -and -not $d.StartsWith('My Research/') -and -not $set.Contains($d) -and (Test-Path -LiteralPath (Join-Path $vault ($d + '/PROTECTED-RESEARCH.md')))) { $set.Add($d) }
  }
  try { if ($set.Count -gt 3) { Set-Content -LiteralPath $reg -Value @($set | Select-Object -Skip 3) -Encoding UTF8 } elseif (Test-Path -LiteralPath $reg) { Remove-Item -LiteralPath $reg -Force } } catch { }
  return @($set)
}
function Protect-Vault([string]$git, [string]$vault) {
  $dirs = @(Get-ProtectedDirs $git $vault)
  foreach ($d in $dirs) { Add-GitExclude $vault ('/' + $d + '/') }
  return $dirs
}
function Get-OwnFileCount([string]$git, [string]$vault, $dirs) {
  $n = @(& $git -C $vault ls-files -o --exclude-standard 2>$null).Count
  foreach ($d in $dirs) { $p = Join-Path $vault $d; if (Test-Path -LiteralPath $p -PathType Container) { $n += @(Get-ChildItem -LiteralPath $p -Recurse -File -Force -ErrorAction SilentlyContinue).Count } }
  return $n
}
$script:PublicNotesGit = 'https://github.com/romangigliotti123-arch/vault-notes-01.git'   # set in the public copy by the site build: the GitHub repo that replaces the old website vault.git remote
function Heal-Vault {
  param([string]$git, [string]$vault, [string]$state)
  $ErrorActionPreference = 'Continue'
  $marker = Join-Path $vault '.full-view'
  $msg = $null; $prot = @('My Research', 'Games', 'Models')
  try {
    & $git -C $vault config core.autocrlf false 2>$null | Out-Null
    & $git -C $vault config core.safecrlf false 2>$null | Out-Null
    if ($script:PublicNotesGit) { $ou = (& $git -C $vault remote get-url origin 2>$null); if ("$ou" -match '\.netlify\.app/vault\.git') { & $git -C $vault remote set-url origin $script:PublicNotesGit 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $script:originMoved = "rbx-update: origin moved to $($script:PublicNotesGit)" } } }
    & $git -C $vault config core.longpaths true 2>$null | Out-Null
    $prot = @(Protect-Vault $git $vault)
    & $git -C $vault fetch -q origin 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) { $msg = 'rbx-update: fetch failed (offline?), vault left as it is' }
    else {
      $t = 'origin/main'
      & $git -C $vault rev-parse -q --verify $t 2>$null | Out-Null
      if ($LASTEXITCODE -ne 0) { $t = '@{u}'; & $git -C $vault rev-parse -q --verify $t 2>$null | Out-Null; if ($LASTEXITCODE -ne 0) { $t = $null } }
      if (-not $t) { $msg = 'rbx-update: no upstream branch, vault left as it is' }
      else {
        # full view: if app.json differs from the repo's only by the userIgnoreFilters rewrite, put the repo version back first so it is not a "local change"
        if (Test-Path -LiteralPath $marker) {
          try {
            $cur = [IO.File]::ReadAllText((Join-Path $vault '.obsidian\app.json'))
            $head = (& $git -C $vault show 'HEAD:.obsidian/app.json' 2>$null | Out-String)
            if ((Get-JsonWithoutIgnore $cur) -eq (Get-JsonWithoutIgnore $head)) { & $git -C $vault checkout -q -- .obsidian/app.json 2>$null | Out-Null }
          } catch { }
        }
        & $git -C $vault update-index -q --refresh 2>$null | Out-Null
        & $git -C $vault diff HEAD --quiet 2>$null | Out-Null
        $ok = $false
        if ($LASTEXITCODE -eq 0) { & $git -C $vault merge --ff-only -q $t 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $ok = $true } }
        if (-not $ok) {
          # blocked by local changes or divergence: save first, then reset (reset never touches untracked/excluded files unless upstream now tracks the same path)
          $base = (& $git -C $vault merge-base HEAD $t 2>$null | Out-String).Trim()
          if (-not $base) { $base = 'HEAD' }
          New-Item -ItemType Directory -Force $state | Out-Null
          $ts = Get-Date -Format 'yyyyMMdd-HHmmss'
          $patch = Join-Path $state "local-changes-$ts.patch"
          $saved = $false
          $real = (& $git -C $vault diff $base --ignore-cr-at-eol --stat 2>$null | Out-String).Trim()
          if ($real) { & $git -C $vault diff $base --binary "--output=$patch" 2>$null | Out-Null; $saved = (Test-Path -LiteralPath $patch) }
          $un = @(& $git -C $vault -c core.quotepath=false ls-files --others --exclude-standard 2>$null)
          if ($un.Count -gt 0) { Set-Content -LiteralPath (Join-Path $state "local-changes-$ts.untracked.txt") -Value $un -Encoding UTF8 }
          # untracked files that upstream now tracks would be overwritten by the reset: copy them aside first
          if ($un.Count -gt 0) {
            try {
              $tree = New-Object 'System.Collections.Generic.HashSet[string]'
              foreach ($x in @(& $git -C $vault -c core.quotepath=false ls-tree -r --name-only $t 2>$null)) { [void]$tree.Add($x) }
              foreach ($u in $un) { if ($tree.Contains($u)) {
                $dstf = Join-Path (Join-Path $state "collision-backup-$ts") $u
                New-Item -ItemType Directory -Force (Split-Path $dstf -Parent) | Out-Null
                Copy-Item -LiteralPath (Join-Path $vault $u) -Destination $dstf -Force -ErrorAction SilentlyContinue
              } }
            } catch { }
          }
          foreach ($pat in 'local-changes-*.patch', 'local-changes-*.untracked.txt', 'collision-backup-*') {
            Get-ChildItem -LiteralPath $state -Filter $pat -ErrorAction SilentlyContinue | Sort-Object Name -Descending | Select-Object -Skip 5 | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
          }
          & $git -C $vault reset --hard -q $t 2>$null | Out-Null
          if ($LASTEXITCODE -ne 0) { $msg = 'rbx-update: could not reset the vault to the latest (left as it is)' }
          elseif ($saved) { $msg = "rbx-update: local changes saved to $patch; vault reset to the latest" }
        }
      }
    }
  } catch { $msg = ('rbx-update: heal failed (' + $_.Exception.Message + '), continuing') }
  try { if (Test-Path -LiteralPath $marker) { Set-FullViewConfig $vault } } catch { }
  return @(@($script:originMoved, $msg) | Where-Object { $_ })
}
#endregion


$Bases = @('https://vault-hhmi60uo.netlify.app')
if (-not (Test-Path (Join-Path $Dest '.git'))) {
  New-Item -ItemType Directory -Force (Split-Path $Dest -Parent) | Out-Null
  $cloned = $false
  # 1) Tailscale share (no GitHub login needed)
  foreach ($b in $Bases) {
    & curl.exe -fsS -m 8 -o NUL "$b/vault.git/HEAD" 2>$null
    if ($LASTEXITCODE -ne 0) { continue }
    Write-Output "Cloning from $b/vault.git (first time can take several minutes)..."
    for ($try = 1; $try -le 2 -and -not $cloned; $try++) {
      if ((Test-Path (Join-Path $Dest 'My Research')) -or (Test-Path (Join-Path $Dest 'Games')) -or ($try -eq 1 -and (Test-Path -LiteralPath $Dest) -and (Get-ChildItem -LiteralPath $Dest -Force -ErrorAction SilentlyContinue | Select-Object -First 1))) { Write-Output "Refusing to clear ${Dest}: it is not a clone and it is not empty (your own files could be in it). Move it away and run again."; exit 1 }
      if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest -ErrorAction SilentlyContinue }
      & $git -c core.longpaths=true -c core.autocrlf=false -c core.safecrlf=false clone "$b/vault.git" $Dest
      if ($LASTEXITCODE -eq 0) { $cloned = $true }
    }
    if ($cloned) { break }
  }
  # 2) GitHub via gh
  if (-not $cloned) {
    if (-not $gh) { Write-Output 'Share unreachable (sign in to Tailscale) and gh is missing. Install: winget install --id GitHub.cli -e --silent, or sign in to Tailscale.'; exit 1 }
    & $gh auth status *> $null
    if ($LASTEXITCODE -ne 0) { Write-Output 'NEEDS_LOGIN: share unreachable and not logged in to GitHub. Sign in to Tailscale (preferred) or run: gh auth login (GitHub.com, HTTPS, web browser), then run this script again.'; exit 2 }
    Write-Output "Cloning $Repo from GitHub (first time can take several minutes)..."
    & $gh repo clone $Repo $Dest -- -c core.longpaths=true -c core.autocrlf=false -c core.safecrlf=false
    if ($LASTEXITCODE -ne 0) { Write-Output 'Clone failed.'; exit 1 }
  }
} else {
  Write-Output "Vault already cloned at $Dest"
}
# Self-heal the (read-only) clone: autocrlf/safecrlf off, fetch, fast-forward; local changes are saved to $StateDir\local-changes-<timestamp>.patch, then reset to origin/main
$healMsg = Heal-Vault $git $Dest $StateDir
if ($healMsg) { Write-Output $healMsg }

# Companion AI Library Vault (private repo ai-library-vault) -> folder ai-library-vault next to the vault. Share first, then GitHub; non-fatal. Skip with -SkipAiVault.
$aiScript = Join-Path $Dest 'ai-vault-sync.ps1'
if (-not $SkipAiVault -and (Test-Path $aiScript)) {
  try { & powershell -NoProfile -ExecutionPolicy Bypass -File $aiScript -Dest (Join-Path (Split-Path $Dest -Parent) 'ai-library-vault') } catch { Write-Output ('AI Library Vault setup failed (non-fatal; run vault-update.ps1 later): ' + $_.Exception.Message) }
}

# Claude kit (Roblox agents, skills, tools) -> %USERPROFILE%\.claude. Idempotent, no questions, the vault owns its files: every update overwrites them with the new version. Skip with -SkipKit.
$kitScript = Join-Path $Dest 'claude-kit\install.ps1'
if (-not $SkipKit -and (Test-Path $kitScript)) {
  $env:CLAUDE_KIT_NOFOOTER = '1'
  try { & powershell -NoProfile -ExecutionPolicy Bypass -File $kitScript } catch { Write-Output ('Kit install failed (non-fatal): ' + $_.Exception.Message) }
}

# Assets -> <vault>\Assets from the share (first run downloads everything, about 2.7 GB; later runs only changes). No questions. Skip with -SkipAssets.
$refreshScript = Join-Path $Dest 'claude-kit\kit-refresh.ps1'
if (-not $SkipAssets -and (Test-Path $refreshScript)) {
  try { $env:CLAUDE_KIT_SKIP = '1'; & powershell -NoProfile -ExecutionPolicy Bypass -File $refreshScript } catch { Write-Output ('Asset sync failed (non-fatal; run vault-update.ps1 later): ' + $_.Exception.Message) }
  finally { Remove-Item Env:\CLAUDE_KIT_SKIP -ErrorAction SilentlyContinue }
}

# GitHub origin only: let the scheduled git pull authenticate through gh (skipped when no gh credential helper is needed)
$origin = (& $git -C $Dest remote get-url origin)
if ($gh -and $origin -match 'github\.com') {
  $helpers = (& $git config --global --get-all 'credential.https://github.com.helper') -join ' '
  if ($helpers -notmatch 'gh') { & $gh auth setup-git *> $null }
}

try {
  New-Item -ItemType Directory -Force $StateDir | Out-Null
  $log = Join-Path $StateDir 'pull.log'
  $vbs = Join-Path $StateDir 'pull-hidden.vbs'
  # cmd /c "<git>" -C "<dest>" pull --ff-only >> "<log>" 2>&1, wrapped for cmd's quote rule, then escaped for VBScript
  # after the pull, refresh the installed kit (agents, skills, tools) from the vault; quiet, the vault owns its files: every update overwrites them with the new version
  $refresh = Join-Path $Dest 'claude-kit\kit-refresh.ps1'
  # runs at logon (and by hand): vault-update.ps1 -Quiet = self-healing fetch + fast-forward (see Heal-Vault) + kit refresh + asset sync; falls back to pull + kit refresh if the script is not there yet
  $upd = Join-Path $Dest 'vault-update.ps1'
  $cmd = 'cmd /c "' + ('if exist "{4}" (powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{4}" -Quiet >> "{2}" 2>&1) else ("{0}" -C "{1}" pull --ff-only >> "{2}" 2>&1 & if exist "{3}" powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{3}" >> "{2}" 2>&1)' -f $git, $Dest, $log, $refresh, $upd) + '"'
  $vbsCmd = $cmd.Replace('"', '""')
  $vbsText = @(
    'Set sh = CreateObject("WScript.Shell")',
    'Set fso = CreateObject("Scripting.FileSystemObject")',
    ('logp = "{0}"' -f $log.Replace('"', '""')),
    'If fso.FileExists(logp) Then',
    '  If fso.GetFile(logp).Size > 200000 Then fso.DeleteFile logp',
    'End If',
    'sh.Environment("Process")("GIT_TERMINAL_PROMPT") = "0"',
    ('sh.Run "{0}", 0, True' -f $vbsCmd)
  ) -join "`r`n"
  Set-Content -Path $vbs -Value $vbsText -Encoding ASCII

  $action = New-ScheduledTaskAction -Execute (Join-Path $env:WINDIR 'System32\wscript.exe') -Argument ('//B //nologo "{0}"' -f $vbs)
  # At log on only (no repetition): starts 2 minutes after logon so it never competes with the login itself
  $trigger = New-ScheduledTaskTrigger -AtLogOn -User ([Security.Principal.WindowsIdentity]::GetCurrent().Name)
  $trigger.Delay = 'PT2M'
  $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -Hidden -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 4)
  $principal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
  Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
} catch {
  Write-Output ("Task setup failed: " + $_.Exception.Message)
  exit 3
}

# Software check (read-only table: what is installed, what is missing, install commands per OS; installs nothing). Non-fatal.
try { $chk = Join-Path $Dest 'claude-kit\tools\setup-check.py'; if (-not $SkipKit -and (Test-Path $chk)) { foreach ($n in 'python3', 'python', 'py') { $c = Get-Command $n -ErrorAction SilentlyContinue; if ($c -and $c.Source -notmatch 'WindowsApps') { Write-Output ''; & $c.Source -I $chk; break } } } } catch { }
Write-Output ''
Write-Output "Done. Task '$TaskName' updates $Dest (vault pull, kit refresh, assets) at every logon, 2 minutes after you sign in; it does NOT poll (log: $log)."
Write-Output "Update now, any time: powershell -NoProfile -ExecutionPolicy Bypass -File `"$Dest\vault-update.ps1`"   (or run /rbx-update in Claude). Assets are in $Dest\Assets."
Write-Output "Next: open Obsidian > Open folder as vault > choose $Dest"
Write-Output 'Do not edit notes here (the update saves any local changes to a patch and resets to the latest). Remove the sync: win-sync-setup.ps1 -Uninstall'
$kitHome = if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }
if (Test-Path (Join-Path $kitHome '.claude\claude-kit\vault-mode\.claude\skills\rbx-workflow\SKILL.md')) { Write-Output 'The Roblox Dev Mastery Vault kit is installed. TO USE THE VAULT: load it by starting a Claude session in ' + $Dest + ' (that folder is the loaded vault: the vault skills, agents, art-direction, placement, lighting and visual-QA rules and reference images are there automatically; no load command is needed; your other Claude sessions stay clean). Always available in every session: /rbx-update /rbx-check /rbx-uninstall. In the vault folder: /rbx-idea-quick (one fresh idea) or /rbx-workflow (idea, rating, plan, build); /rbx-make; judgement and your games (in the Games/ folder of the vault, never touched by updates): /rbx-critic /rbx-weekly /rbx-launch-kit /rbx-harvest; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; placement, lighting and looks (a game is never called done without them): /rbx-placement /rbx-lighting /rbx-art /rbx-visual; measure the vault itself: /rbx-bench; mentor: /rbx-mentor; research: /rbx-research; manager: /rbx-manager; vault: /rbx-clean /rbx-setup /rbx-light-on /rbx-light-off /rbx-list; usage: /rbx-low-usage. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)' }
elseif (Test-Path (Join-Path $kitHome '.claude\claude-kit\vault-mode\.claude\agents\rbx-builder.md')) { Write-Output ('Kit installed. Load the vault by starting a Claude session in ' + $Dest + ', then say "make me a Roblox game: <your idea>" to Claude.') }
if (-not $SkipKit -and (Test-Path (Join-Path $kitHome '.claude\claude-kit\vault-mode\.claude\skills\rbx-workflow\SKILL.md'))) { Write-Output ''; Write-Output ('>>> Load the vault by starting a Claude session in ' + $Dest + ' (then /rbx-list shows everything it contains).') }
exit 0
