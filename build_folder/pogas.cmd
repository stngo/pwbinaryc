@echo off

:: Checking Arguments
:check_args
set ARG1=%1

if "%ARG1%"=="build" goto build_program
if "%ARG1%"=="updater" goto build_updater

:noargs
cls
echo No args used! Use arguments! e.g. "pogas.cmd build"
echo.
pause
exit /b

:build_program
cls
echo Building .py
echo.
pyinstaller --noconfirm --onefile --console --icon "SYSTEM_SOURCE/REG_BINARY_VALUE.ico" --name "pwBinaryC" --add-data "../Updater.py;."  "../MAIN.py"
echo.
echo.
echo Finished
echo.
pause
exit /b

:build_updater
cls
pyinstaller --noconfirm --onefile --console --name "Updater" "../Updater.py"
echo.
pause
exit /b