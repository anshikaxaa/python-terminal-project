#!/bin/bash

# Python Command Terminal - Deployment Script
# This script helps with easy installation and deployment

set -e

echo "🚀 Python Command Terminal - Deployment Script"
echo "============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
check_python() {
    if command -v python3 &>/dev/null; then
        print_status "Python 3 found: $(python3 --version)"
        PYTHON_CMD="python3"
    elif command -v python &>/dev/null; then
        print_status "Python found: $(python --version)"
        PYTHON_CMD="python"
    else
        print_error "Python is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
}

# Install system dependencies (Linux)
install_system_deps() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        print_status "Installing system dependencies..."
        if command -v apt-get &>/dev/null; then
            sudo apt-get update
            sudo apt-get install -y python3-pip python3-venv
        elif command -v yum &>/dev/null; then
            sudo yum install -y python3-pip
        elif command -v dnf &>/dev/null; then
            sudo dnf install -y python3-pip
        fi
    fi
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    source venv/bin/activate
}

# Install Python dependencies
install_deps() {
    print_status "Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install -e .
}

# Test installation
test_installation() {
    print_status "Testing installation..."
    if command -v pct &>/dev/null; then
        print_status "✓ Command 'pct' is available"
    else
        print_warning "Command 'pct' not found in PATH"
    fi

    if command -v python-terminal &>/dev/null; then
        print_status "✓ Command 'python-terminal' is available"
    else
        print_warning "Command 'python-terminal' not found in PATH"
    fi

    # Test the application
    echo "Testing basic functionality..."
    echo "help" | timeout 10s python terminal_final.py | head -10
}

# Create desktop shortcut (Linux)
create_desktop_shortcut() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        print_status "Creating desktop shortcut..."
        cat > ~/.local/share/applications/python-terminal.desktop << EOF
[Desktop Entry]
Name=Python Command Terminal
Comment=A fully functional command-line terminal with AI capabilities
Exec=$PWD/venv/bin/python $PWD/terminal_final.py
Icon=terminal
Terminal=true
Type=Application
Categories=Development;Utility;
EOF
        chmod +x ~/.local/share/applications/python-terminal.desktop
        print_status "Desktop shortcut created!"
    fi
}

# Main deployment function
main() {
    print_status "Starting deployment process..."

    check_python
    install_system_deps
    create_venv
    install_deps
    test_installation

    print_status ""
    print_status "🎉 Deployment completed successfully!"
    print_status ""
    print_status "Usage:"
    print_status "  $PYTHON_CMD terminal_final.py"
    print_status "  # or (if installed globally):"
    print_status "  pct"
    print_status "  python-terminal"
    print_status ""
    print_status "Commands:"
    print_status "  help     - Show available commands"
    print_status "  ls       - List directory contents"
    print_status "  cd       - Change directory"
    print_status "  sysinfo  - Show system information"
    print_status "  ai <cmd> - Use natural language commands"
    print_status ""
}

# Run main function
main "$@"
