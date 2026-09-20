$ErrorActionPreference = 'Stop'
$action = $env:MURAN_TASK_ACTION
$name = $env:MURAN_TASK_NAME
$taskArguments = $env:MURAN_TASK_ARGUMENTS
$executable = $env:MURAN_TASK_EXECUTABLE
if (-not $name -or -not $executable -or -not $taskArguments) { throw 'Missing task parameters' }
$existing = Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue
$owned = $existing -and $existing.Actions.Count -eq 1 -and $existing.Actions[0].Execute -eq $executable -and $existing.Actions[0].Arguments -eq $taskArguments
if ($action -eq 'enable') {
    if ($existing -and -not $owned) { throw 'Task name is occupied by a different action; no task changed' }
    $trigger = New-ScheduledTaskTrigger -Daily -At '09:00'
    $beijing = [TimeZoneInfo]::ConvertTimeBySystemTimeZoneId([DateTimeOffset]::Now, 'China Standard Time')
    $trigger.StartBoundary = $beijing.ToString('yyyy-MM-dd') + 'T09:00:00+08:00'
    $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    $principal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
    $taskAction = New-ScheduledTaskAction -Execute $executable -Argument $taskArguments
    Register-ScheduledTask -TaskName $name -Action $taskAction -Trigger $trigger -Settings $settings -Principal $principal -Description 'Update the personal muran-skill checkout daily at 09:00 Asia/Shanghai and reconcile skill junctions.' -Force | Out-Null
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
    @{ok=[bool]$owned; task=$name; status=[string]$existing.State; owned=[bool]$owned; start_boundary=$existing.Triggers[0].StartBoundary; start_when_available=[bool]$existing.Settings.StartWhenAvailable; last_result=$info.LastTaskResult; last_run=$info.LastRunTime.ToString('o'); next_run=$info.NextRunTime.ToString('o')} | ConvertTo-Json -Compress
}
