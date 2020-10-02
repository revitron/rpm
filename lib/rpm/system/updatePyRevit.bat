@echo off

echo %1
cd %1

:stillRunning
	TASKKILL /IM Revit.exe /F
	timeout 3 > NUL
	tasklist /FI "IMAGENAME eq Revit.exe" 2>NUL | find /I /N "Revit.exe">NUL
	if "%ERRORLEVEL%"=="0" goto :stillRunning

git pull origin

pause