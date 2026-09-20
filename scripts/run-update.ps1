# Python is accepted only so existing scheduled tasks survive the uv migration.
param([string]$Uv, [string]$Repo, [string]$StateDir, [string]$Python)
$ErrorActionPreference = 'Stop'
if ($Uv) { $env:MURAN_UV = $Uv }
& (Join-Path $Repo 'muran.ps1') daily-update --quiet --state-dir $StateDir
exit $LASTEXITCODE
