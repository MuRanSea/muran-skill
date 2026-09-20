$ErrorActionPreference = 'Stop'
$action = $env:MURAN_TASK_ACTION
$name = $env:MURAN_TASK_NAME
$taskArguments = $env:MURAN_TASK_ARGUMENTS
$executable = $env:MURAN_TASK_EXECUTABLE
$prefix = $env:MURAN_TASK_PREFIX
$suffix = $env:MURAN_TASK_SUFFIX
if (-not $name -or -not $executable -or -not $taskArguments -or -not $prefix -or -not $suffix) { throw 'Missing task parameters' }
. (Join-Path $PSScriptRoot 'task-action.ps1')
$existing = Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue
$owned = Test-MuranTaskAction $existing $executable $prefix $suffix
if ($action -eq 'enable') {
    if ($existing -and -not $owned) { throw 'Task name is occupied by a different action; no task changed' }
    $time = $env:MURAN_TASK_TIME
    if ($time -notin @('09:00', '09:30')) { throw 'Unsupported schedule time' }
    $minutes = [int]$env:MURAN_TASK_TIMEOUT
    if ($minutes -notin @(10, 120)) { throw 'Unsupported execution limit' }
    $trigger = New-ScheduledTaskTrigger -Daily -At $time
    $beijing = [TimeZoneInfo]::ConvertTimeBySystemTimeZoneId([DateTimeOffset]::Now, 'China Standard Time')
    $trigger.StartBoundary = $beijing.ToString('yyyy-MM-dd') + 'T' + $time + ':00+08:00'
    $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes $minutes) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    $principal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
    $taskAction = New-ScheduledTaskAction -Execute $executable -Argument $taskArguments
    Register-ScheduledTask -TaskName $name -Action $taskAction -Trigger $trigger -Settings $settings -Principal $principal -Description "muran-skill daily update at $time Asia/Shanghai; managed by the linked repository." -Force | Out-Null
    $existing = Get-ScheduledTask -TaskName $name
    $owned = $true
} elseif ($action -eq 'disable') {
    if ($existing -and -not $owned) { throw 'Task action differs from this checkout; no task removed' }
    if ($existing) { Unregister-ScheduledTask -TaskName $name -Confirm:$false }
    @{ok=$true; task=$name; status='disabled'} | ConvertTo-Json -Compress
    exit 0
} elseif ($action -ne 'status') { throw 'Unsupported task action' }
if (-not $existing) {
    @{ok=$true; task=$name; status='absent'} | ConvertTo-Json -Compress
} else {
    $info = Get-ScheduledTaskInfo -TaskName $name
    @{ok=[bool]$owned; task=$name; status=[string]$existing.State; owned=[bool]$owned; runtime_current=[bool]($owned -and $existing.Actions[0].Arguments -eq $taskArguments); start_boundary=$existing.Triggers[0].StartBoundary; start_when_available=[bool]$existing.Settings.StartWhenAvailable; last_result=$info.LastTaskResult; last_run=$info.LastRunTime.ToString('o'); next_run=$info.NextRunTime.ToString('o')} | ConvertTo-Json -Compress
}
