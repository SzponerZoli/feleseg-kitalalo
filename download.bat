@echo off
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with admin privileges.
    curl -o "C:\Program Files\Szponer\kitalalo\feleseg.exe" https://raw.githubusercontent.com/SzponerZoli/feleseg-kitalalo/main/feleseg.exe
) else (
    echo Requesting admin privileges...
    powershell start-process download.bat -verb runas
)