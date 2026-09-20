param([string]$Uv, [string]$Repo, [string]$StateDir)
$ErrorActionPreference = 'Stop'
$env:MURAN_UV = $Uv
& (Join-Path $Repo 'muran.ps1') docs update --quiet --state-dir $StateDir
exit $LASTEXITCODE
