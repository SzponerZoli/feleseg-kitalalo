@echo off
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with admin privileges.
    curl -o "C:\Program Files\Szponer\kitalalo\file_neve.exe" https://raw.githubusercontent.com/felhasznalo/repo/master/file_neve.exe
) else (
    echo Requesting admin privileges...
    powershell start-process elevated_curl_download.bat -verb runas
)