# Python Command Terminal

A fully functional command-line terminal built with Python that replicates basic terminal operations.

## Features

### Core Commands
- `ls` - List directory contents with file sizes and modification dates
- `cd` - Change directory with error handling
- `pwd` - Show current working directory
- `sysinfo` - Display system information (CPU, memory usage)
- `exit` / `quit` - Exit the terminal
- `help` - Show available commands

### Additional Features
- Human-readable file sizes (B, KB, MB, GB, TB)
- File modification timestamps
- Comprehensive error handling
- Clean, responsive CLI interface
- System resource monitoring

## Installation

1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the terminal:
   ```bash
   python terminal.py
   ```

## Usage

The terminal provides a command-line interface similar to bash/cmd:

```
Python Command Terminal
Type 'help' for available commands, 'exit' to quit.
--------------------------------------------------
[C:\Users\Lenovo\Desktop]> ls
Contents of C:\Users\Lenovo\Desktop:
  d    1.2 KB Sep 20 10:44 python_terminal_project
  -    2.1 KB Sep 20 10:30 command_terminal_fixed.py

[C:\Users\Lenovo\Desktop]> cd python_terminal_project
[C:\Users\Lenovo\Desktop\python_terminal_project]> pwd
C:\Users\Lenovo\Desktop\python_terminal_project

[C:\Users\Lenovo\Desktop\python_terminal_project]> sysinfo
System Information:
  Platform: Windows 11
  Machine: AMD64
  CPU Usage: 15.2%
  Memory: 4.2 GB / 15.8 GB
  Memory Usage: 26.6%

[C:\Users\Lenovo\Desktop\python_terminal_project]> exit
Goodbye!
```

## Project Structure

```
python_terminal_project/
├── terminal.py          # Main terminal application
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Error Handling

The terminal includes comprehensive error handling for:
- Invalid commands
- File not found errors
- Permission errors
- Directory access issues
- System information retrieval failures

## Future Enhancements

Potential additions for extended functionality:
- Command history and auto-completion
- Additional file operations (mkdir, rm, cp, mv)
- Process management commands
- Network utilities
- AI-powered natural language command processing
- Web-based interface option

## Requirements

- Python 3.7+
- psutil library for system monitoring

## License

This project is open source and available under the MIT License.
