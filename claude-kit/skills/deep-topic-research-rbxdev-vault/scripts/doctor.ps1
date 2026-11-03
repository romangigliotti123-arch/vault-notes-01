# Convenience wrapper for Windows: powershell -NoProfile -File doctor.ps1 [--net]
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
foreach ($name in @("python", "py", "python3")) {
  $cmd = Get-Command $name -ErrorAction SilentlyContinue
  if (-not $cmd) { continue }
  & $cmd.Source -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" 2>$null
  if ($LASTEXITCODE -eq 0) {
    & $cmd.Source "$dir\doctor.py" @args
    exit $LASTEXITCODE
  }
}
Write-Host "[MISSING] python 3.8+  install: winget install Python.Python.3.12"
exit 1
