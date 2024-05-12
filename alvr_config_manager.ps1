# path to the directory of ALVR. ALVR Dashboard.exe should be there.
# https://github.com/alvr-org/ALVR
$ALVR_DIR = "D:\Games\ALVR\" 

# path to the .exe
# https://github.com/alvr-org/ADBForwarder
$ADBFORWARDER_PATH = ".\adbforwarder\ADBForwarder.exe"

# path to the directory. you need to provide session-wired.json and session-wireless.json there. 
# you can find the current config in the same directory as ALVR Dashboard.exe, it's called session.json
$CONFIGS_DIR = ".\" 

$choice = Read-Host "Wired or wireless?
1 - Wired, higher quality, lower latency; via adbforwarder.
2 - Wireless, lower quality, higher latency."

if ($choice -eq 1){ # wired
    $source_path = Join-Path -Path $CONFIGS_DIR -ChildPath "session-wired.json"
    $dest_path = Join-Path -Path $ALVR_DIR -ChildPath "session.json"

    Write-Output "Copying from $source_path to $dest_path"
    Copy-Item -Path "$source_path" -Destination "$dest_path" -Force

    Start-Process $ADBFORWARDER_PATH
}
elseif($choice -eq 2){ # wireless
    $source_path = Join-Path -Path $CONFIGS_DIR -ChildPath "session-wireless.json"
    $dest_path = Join-Path -Path $ALVR_DIR -ChildPath "session.json"

    Write-Output "Copying from $source_path to $dest_path"
    Copy-Item -Path "$source_path" -Destination "$dest_path" -Force
}else{
    Write-Output "No choice provided. Exiting"
    break
}

Write-Output "Starting ALVR"
Start-Process "$ALVR_DIR\ALVR Dashboard.exe"

Write-Host "You need to launch SteamVR from the ALVR Dashboard." -ForegroundColor Black -BackgroundColor White

Start-Sleep -s 3

do {
    Write-Output "When you're done, you should close SteamVR gracefully (with the x button on it), otherwise it might disable addons and launch in 'safe mode' next time."
    $kill = Read-Host "'x' to kill all"
    if ($kill -eq "x") {
        if($choice -eq 1){
            Get-Process "ADBForwarder" | Stop-Process -Force
        }
        Get-Process "ALVR Dashboard" | Stop-Process -Force
        Get-Process "vrmonitor" | Stop-Process -Force
        Get-Process "vrcompositor" | Stop-Process -Force
    }
} while ($kill -ne "x")
