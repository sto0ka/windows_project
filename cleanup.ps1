# Clear recently accessed folders history
Clear-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue

# Clear run history
Clear-History -Count 1000 -ErrorAction SilentlyContinue

# Clear Google Chrome history
$ChromeHistoryPath = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
if(Test-Path $ChromeHistoryPath){
    $connectionString = "Data Source=$ChromeHistoryPath;Version=3;New=False;Compress=True;"
    $dbConnection = New-Object System.Data.SQLite.SQLiteConnection($connectionString)
    $dbConnection.Open()
    $dbCommand = $dbConnection.CreateCommand()
    $dbCommand.CommandText = "DELETE FROM urls;"
    $dbCommand.ExecuteNonQuery()
    $dbConnection.Close()
}
