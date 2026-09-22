[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('list', 'install', 'sync', 'update', 'daily-update', 'doctor', 'auto-update', 'uninstall', 'docs')]
    [string]$Command = 'doctor',
    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)
$ErrorActionPreference = 'Stop'
$uvCommand = if ($env:MURAN_UV) { $env:MURAN_UV } else { 'uv' }
$uv = Get-Command $uvCommand -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $uv) {
    throw 'uv is required. Install it with: winget install --id astral-sh.uv -e ; then reopen PowerShell.'
}
$previousUv = $env:MURAN_UV
$previousUtf8 = $env:PYTHONUTF8
$previousBytecode = $env:PYTHONDONTWRITEBYTECODE
try {
    $env:MURAN_UV = $uv.Source
    $env:PYTHONUTF8 = '1'
    $env:PYTHONDONTWRITEBYTECODE = '1'
    & $uv.Source run --locked --project $PSScriptRoot (Join-Path $PSScriptRoot 'scripts\muran.py') $Command @Rest
    $code = $LASTEXITCODE
} finally {
    $env:MURAN_UV = $previousUv
    $env:PYTHONUTF8 = $previousUtf8
    $env:PYTHONDONTWRITEBYTECODE = $previousBytecode
}
exit $code
