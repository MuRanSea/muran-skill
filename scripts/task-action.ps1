function Test-MuranTaskAction {
    param($Task, [string]$Executable, [string]$Prefix, [string]$Suffix)
    if (-not $Task -or @($Task.Actions).Count -ne 1) { return $false }
    $action = $Task.Actions[0]
    if ($action.Execute -ne $Executable) { return $false }
    # Match the fixed runner, repository and state paths. Only the runtime path
    # may differ, allowing a legacy task or a relocated uv binary to be updated.
    $pattern = '^' + [regex]::Escape($Prefix) + ' -(Uv|Python) ("[^"]+"|[^\s"]+) ' + [regex]::Escape($Suffix) + '$'
    if ($action.Arguments -notmatch $pattern) { return $false }
    $runtime = $Matches[2].Trim('"')
    $leaf = if ($Matches[1] -eq 'Uv') { 'uv.exe' } else { 'python.exe' }
    return [IO.Path]::IsPathRooted($runtime) -and [IO.Path]::GetFileName($runtime) -eq $leaf
}
