# Python Command Terminal - Enhanced Version

A fully functional command-line terminal built with Python that replicates basic terminal operations with advanced features including AI-powered natural language processing, command history, and auto-completion.

## Features

### Core Commands
- `ls` - List directory contents with file sizes and modification dates
- `cd` - Change directory with error handling
- `pwd` - Show current working directory
- `mkdir` - Create directories
- `rm` - Remove files/directories (with -r flag for directories)
- `sysinfo` - Display system information (CPU, memory usage)
- `exit` / `quit` - Exit the terminal
- `help` - Show available commands
- `history` - Show command history

### Advanced Features
- **AI-Powered Commands**: Use natural language instead of traditional commands
  - "create folder test" instead of "mkdir test"
  - "show me files" instead of "ls"
  - "go to Documents" instead of "cd Documents"
- **Command History**: Persistent command history with file storage
- **Auto-completion**: Tab completion for commands
- **Human-readable file sizes**: B, KB, MB, GB, TB format
- **Comprehensive error handling**: User-friendly error messages
- **System monitoring**: CPU and memory usage tracking

## Installation

1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the terminal:
   ```bash
   python terminal_enhanced.py
   ```

## Usage Examples

### Traditional Commands
```
Python Command Terminal - Enhanced Version
Features: AI commands, command history, auto-completion
Type 'help' for available commands, 'exit' to quit.
------------------------------------------------------------
[C:\Users\Lenovo\Desktop]> ls
Contents of C:\Users\Lenovo\Desktop:
  d    1.2 KB Sep 20 10:44 python_terminal_project
  -    2.1 KB Sep 20 10:30 command_terminal_fixed.py

[C:\Users\Lenovo\Desktop]> cd python_terminal_project
[C:\Users\Lenovo\Desktop\python_terminal_project]> pwd
C:\Users\Lenovo\Desktop\python_terminal_project

[C:\Users\Lenovo\Desktop\python_terminal_project]> mkdir test_folder
Created directory: test_folder

[C:\Users\Lenovo\Desktop\python_terminal_project]> sysinfo
System Information:
  Platform: Windows 11
  Machine: AMD64
  CPU Usage: 15.2%
  Memory: 4.2 GB / 15.8 GB
  Memory Usage: 26.6%

[C:\Users\Lenovo\Desktop\python_terminal_project]> history
Command History:
  1  ls
  2  cd python_terminal_project
  3  pwd
  4  mkdir test_folder
  5  sysinfo
  6  history
```

### AI-Powered Natural Language Commands
```
[C:\Users\Lenovo\Desktop\python_terminal_project]> ai create folder ai_test
Interpreted as: mkdir ai_test
Created directory: ai_test

[C:\Users\Lenovo\Desktop\python_terminal_project]> ai show me files
Interpreted as: ls
Contents of C:\Users\Lenovo\Desktop\python_terminal_project:
  d    1.2 KB Sep 20 10:44 ai_test
  d    1.2 KB Sep 20 10:44 test_folder
  -    2.1 KB Sep 20 10:30 commands.py
  -    2.1 KB Sep 20 10:30 terminal.py

[C:\Users\Lenovo\Desktop\python_terminal_project]> ai go to ai_test
Interpreted as: cd ai_test
```

## Project Structure

```
python_terminal_project/
├── terminal_enhanced.py    # Main enhanced terminal application
├── commands_updated.py     # Command handlers with AI integration
├── ai_commands.py          # AI natural language processing
├── history_fixed.py        # Command history and auto-completion
├── requirements.txt        # Python dependencies
├── README_ENHANCED.md      # Enhanced documentation
└── .terminal_history       # Command history file (created automatically)
```

## Architecture

### Modular Design
- **terminal_enhanced.py**: Main application loop and user interface
- **commands_updated.py**: All command implementations and handlers
- **ai_commands.py**: Natural language command interpretation
- **history_fixed.py**: Command history management and auto-completion

### Key Components

#### AI Command Processing
The AI system uses pattern matching to interpret natural language commands:
- Regular expressions to identify command patterns
- Context-aware interpretation
- Fallback to traditional commands when AI fails

#### Command History
- Persistent storage in `.terminal_history` file
- Maximum 1000 commands stored
- Auto-completion using readline library
- History navigation support

#### Error Handling
- Comprehensive error catching for all operations
- User-friendly error messages
- Graceful degradation when features aren't available

## Requirements

- Python 3.7+
- psutil library for system monitoring
- readline library for auto-completion (usually included with Python)

## Error Handling

The terminal includes comprehensive error handling for:
- Invalid commands (with AI fallback)
- File not found errors
- Permission errors
- Directory access issues
- System information retrieval failures
- History file I/O errors

## Future Enhancements

Potential additions for extended functionality:
- Web-based interface option
- Network utilities (ping, curl equivalents)
- Process management commands (ps, kill equivalents)
- Advanced file operations (cp, mv, find)
- Plugin system for custom commands
- Cloud storage integration
- Multi-user support

## License

This project is open source and available under the MIT License.

## Development Notes

This enhanced version demonstrates the use of:
- Modular Python architecture
- Object-oriented design patterns
- Regular expression processing
- File I/O operations
- System resource monitoring
- User interface design principles
