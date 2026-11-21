@echo off
setlocal enabledelayedexpansion

title Decision Graph - Enterprise Node-Spreadsheet & Analytics Engine

echo ===============================================================================
echo                DECISION GRAPH DESKTOP ANALYTICS ENGINE
echo          Native Python Spreadsheet fused with Visual Node Pipeline
echo ===============================================================================
echo.

:: Detect Python environment
set "PYTHON_CMD="
if exist "E:\Python312\python.exe" (
    set "PYTHON_CMD=E:\Python312\python.exe"
) else (
    where python >nul 2>nul
    if %errorlevel% equ 0 (
        set "PYTHON_CMD=python"
    ) else (
        where py >nul 2>nul
        if %errorlevel% equ 0 (
            set "PYTHON_CMD=py"
        )
    )
)

if "%PYTHON_CMD%"=="" (
    echo [ERROR] Python 3.10+ was not found on your system.
    echo Please install Python and ensure PySide6 is installed.
    echo.
    pause
    exit /b 1
)

echo [OK] Using Python: %PYTHON_CMD%
echo [OK] Launching Decision Graph Desktop Application...
echo.

"%PYTHON_CMD%" run.py

if %errorlevel% neq 0 (
    echo.
    echo [NOTICE] Application closed with code %errorlevel%.
    pause
)
