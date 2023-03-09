# Clear recently accessed folders history
Clear-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue

# Clear run history
Clear-History -Count 1000 -ErrorAction SilentlyContinue

# Clear Google Chrome browser history
$ChromeProfileDir = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default"
if(Test-Path $ChromeProfileDir){
    $ChromeHistoryFile = Join-Path $ChromeProfileDir "History"
    if(Test-Path $ChromeHistoryFile){
        Remove-Item $ChromeHistoryFile -Force
    }
}

# Clear recent file history
Clear-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs' -Name '*' -ErrorAction SilentlyContinue
