@echo off
REM Setup script for OS Info Tool
REM This script sets up the development environment

echo Setting up OS Info Tool...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or later
    pause
    exit /b 1
)

echo Python is installed

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install optional dependencies
echo Installing optional dependencies...
pip install PyYAML>=6.0
pip install pytest>=7.0.0
pip install pytest-cov>=4.0.0

REM Run tests
echo Running tests...
python -m pytest test_os_info.py -v

REM Test the tool
echo Testing the tool...
python os-info.py --minimal

echo.
echo Setup complete!
echo.
echo To use the tool:
echo   python os-info.py
echo   python os-info.py --format yaml
echo   python os-info.py --minimal
echo.
echo To run tests:
echo   python -m pytest test_os_info.py
echo.
pause
