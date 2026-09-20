[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('install', 'sync', 'update', 'doctor', 'auto-update', 'uninstall', 'docs')]
    [string]$Command = 'doctor',
    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$python = $env:MURAN_PYTHON
if (-not $python) {
    $localPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
    if (Test-Path -LiteralPath $localPython) { $python = $localPython }
    else { $python = (Get-Command python -ErrorAction Stop).Source }
}
& $python -B -X utf8 (Join-Path $PSScriptRoot 'scripts\muran.py') $Command @Rest
exit $LASTEXITCODE
