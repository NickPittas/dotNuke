@echo off
setlocal enabledelayedexpansion

:: Set the path to the Program Files directory
set "programFilesPath=C:\Program Files"

:: Initialize variable to store the latest Nuke path
set "latestNukePath="

:: Search for Nuke installations and find the latest version
for /d /r "%programFilesPath%" %%a in (Nuke*) do (
    if exist "%%a\python.exe" (
        if "!latestNukePath!"=="" (
            set "latestNukePath=%%a"
        ) else (
            if "%%a" gtr "!latestNukePath!" (
                set "latestNukePath=%%a"
            )
        )
    )
)

:: Check if Nuke was found
if not defined latestNukePath (
    echo Nuke installation not found.
    exit /b
)

:: Display the path of the latest Nuke version
echo Latest Nuke Version: !latestNukePath!

:: Install OpenCV and MediaPipe using Nuke's Python
echo Installing OpenCV...
"!latestNukePath!\python.exe" -m pip install opencv-python
echo Installing MediaPipe...
"!latestNukePath!\python.exe" -m pip install mediapipe

echo Installation complete.
pause
