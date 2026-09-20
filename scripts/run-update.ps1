param([string]$Python, [string]$Repo, [string]$StateDir)
$ErrorActionPreference = 'Stop'
$env:MURAN_PYTHON = $Python
& (Join-Path $Repo 'muran.ps1') update --quiet --state-dir $StateDir
exit $LASTEXITCODE
