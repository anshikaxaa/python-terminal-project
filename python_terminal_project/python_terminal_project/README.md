# Python Command Terminal

A fully functional command-line terminal built with Python that replicates basic terminal operations with AI capabilities.

## Features

- **Core Commands**: `ls`, `cd`, `pwd`, `mkdir`, `rm`, `sysinfo`
- **AI-Powered Commands**: Natural language command interpretation
- **Command History**: Persistent history with auto-completion
- **System Monitoring**: CPU and memory usage tracking
- **Cross-Platform**: Works on Windows, Linux, and Mac

## Quick Start

### Option 1: One-Click Deployment
```bash
# Windows
deploy.bat

# Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

### Option 2: Manual Installation
```bash
pip install -r requirements.txt
python terminal_final.py
```

## Usage Examples

### Traditional Commands
```bash
> ls
Contents of current directory:
  d    1.2 KB Sep 20 10:44 folder
  -    2.1 KB Sep 20 10:30 file.txt

> cd folder
> pwd
C:\path\to\folder

> sysinfo
System Information:
  Platform: Windows 11
  CPU Usage: 15.2%
  Memory: 4.2 GB / 15.8 GB
```

### AI Commands
```bash
> ai create folder test
Interpreted as: mkdir test

> ai show me files
Interpreted as: ls

> ai go to Documents
Interpreted as: cd Documents
```

## Project Structure

```
python_terminal_project/
├── terminal_final.py    # Main application
├── commands_final.py    # Command handlers
├── ai_commands.py       # AI processing
├── history_windows.py   # History management
├── requirements.txt     # Dependencies
├── setup.py            # Package config
├── deploy.sh           # Linux/Mac installer
├── deploy.bat          # Windows installer
├── Dockerfile          # Container config
└── README.md           # This file
```

## Deployment Options

1. **Local Scripts**: Run `deploy.bat` (Windows) or `deploy.sh` (Linux/Mac)
2. **PyPI Package**: `pip install python-command-terminal`
3. **Docker**: `docker build -t python-terminal .`
4. **GitHub Releases**: Download pre-built executables

## Requirements

- Python 3.7+
- psutil (for system monitoring)

## License

MIT License - Open source and free to use.

---

**Quick Test**: Run `python terminal_final.py` and try `help` command.
