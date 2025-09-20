@echo off
REM Python Command Terminal - Windows Deployment Script

echo 🚀 Python Command Terminal - Deployment Script
echo =============================================
echo.

REM Colors for output
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "NC=[0m"

REM Function to print colored output
goto :main

:print_status
    echo %GREEN%[INFO]%NC% %~1
    goto :eof

:print_warning
    echo %YELLOW%[WARNING]%NC% %~1
    goto :eof

:print_error
    echo %RED%[ERROR]%NC% %~1
    goto :eof

:main
    echo Starting deployment process...
    echo.

    REM Check if Python is installed
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        call :print_error "Python is not installed. Please install Python 3.8 or higher."
        goto :end
    )

    call :print_status "Python found: "
    python --version
    echo.

    REM Create virtual environment
    call :print_status "Creating virtual environment..."
    python -m venv venv
    if %errorlevel% neq 0 (
        call :print_error "Failed to create virtual environment"
        goto :end
    )
    echo.

    REM Activate virtual environment and install dependencies
    call :print_status "Installing Python dependencies..."
    call venv\Scripts\activate.bat
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install -e .
    if %errorlevel% neq 0 (
        call :print_error "Failed to install dependencies"
        goto :end
    )
    echo.

    REM Test installation
    call :print_status "Testing installation..."
    where pct >nul 2>&1
    if %errorlevel% equ 0 (
        call :print_status "✓ Command 'pct' is available"
    ) else (
        call :print_warning "Command 'pct' not found in PATH"
    )

    where python-terminal >nul 2>&1
    if %errorlevel% equ 0 (
        call :print_status "✓ Command 'python-terminal' is available"
    ) else (
        call :print_warning "Command 'python-terminal' not found in PATH"
    )
    echo.

    REM Create desktop shortcut
    call :print_status "Creating desktop shortcut..."
    set "SHORTCUT_PATH=%USERPROFILE%\Desktop\Python Terminal.lnk"
    powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT_PATH%');$s.TargetPath='cmd.exe';$s.Arguments='/k \"cd /d %~dp0 && venv\Scripts\activate.bat && python terminal_final.py\"';$s.WorkingDirectory='%~dp0';$s.IconLocation='cmd.exe,0';$s.Description='Python Command Terminal';$s.Save()"
    if %errorlevel% equ 0 (
        call :print_status "Desktop shortcut created!"
    ) else (
        call :print_warning "Could not create desktop shortcut"
    )
    echo.

    call :print_status ""
    call :print_status "🎉 Deployment completed successfully!"
    echo.
    call :print_status "Usage:"
    call :print_status "  python terminal_final.py"
    call :print_status "  # or (if installed globally):"
    call :print_status "  pct"
    call :print_status "  python-terminal"
    echo.
    call :print_status "Commands:"
    call :print_status "  help     - Show available commands"
    call :print_status "  ls       - List directory contents"
    call :print_status "  cd       - Change directory"
    call :print_status "  sysinfo  - Show system information"
    call :print_status "  ai ^<cmd^> - Use natural language commands"
    echo.

:end
    echo Press any key to exit...
    pause >nul
