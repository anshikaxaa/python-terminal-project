"""
Command handlers for the Python Command Terminal.
This module contains all the command implementations.
"""

import os
import datetime
import platform
import psutil
from typing import List, Callable, Dict, Any
from history import show_history, add_to_history
from ai_commands import interpret_natural_command


def get_human_readable_size(size_bytes: int) -> str:
    """
    Convert bytes to human-readable format (B, KB, MB, GB, etc.)

    Args:
        size_bytes: Size in bytes

    Returns:
        Human-readable size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def list_directory_contents(path: str = ".") -> List[str]:
    """
    List contents of a directory with file details.

    Args:
        path: Directory path to list (default: current directory)

    Returns:
        List of formatted file/directory entries
    """
    try:
        entries = []
        with os.scandir(path) as items:
            for item in items:
                # Get file stats
                stat = item.stat()

                # Format file size
                size = get_human_readable_size(stat.st_size)

                # Format modification time
                mod_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                mod_time_str = mod_time.strftime("%b %d %H:%M")

                # Determine if it's a directory
                item_type = "d" if item.is_dir() else "-"

                # Format: permissions type size mod_time name
                entry = f"{item_type} {size:>8} {mod_time_str} {item.name}"
                entries.append(entry)

        return sorted(entries)
    except PermissionError:
        return ["Error: Permission denied"]
    except FileNotFoundError:
        return ["Error: Directory not found"]


def handle_ls(args: List[str]) -> None:
    """
    Handle the 'ls' command.

    Args:
        args: Command arguments
    """
    # Default to current directory
    target_path = "."

    # Check if a path was provided
    if args and len(args) > 0:
        target_path = args[0]

    # Get directory contents
    contents = list_directory_contents(target_path)

    # Display results
    if contents:
        print(f"Contents of {os.path.abspath(target_path)}:")
        for item in contents:
            print(f"  {item}")
    else:
        print("Directory is empty")


def handle_cd(args: List[str]) -> bool:
    """
    Handle the 'cd' command.

    Args:
        args: Command arguments

    Returns:
        True if directory change was successful, False otherwise
    """
    if not args:
        print("cd: missing argument")
        return False

    target_dir = args[0]

    try:
        os.chdir(target_dir)
        return True
    except FileNotFoundError:
        print(f"cd: {target_dir}: No such file or directory")
        return False
    except PermissionError:
        print(f"cd: {target_dir}: Permission denied")
        return False
    except NotADirectoryError:
        print(f"cd: {target_dir}: Not a directory")
        return False


def handle_pwd(args: List[str]) -> None:
    """
    Handle the 'pwd' command to show current working directory.

    Args:
        args: Command arguments (ignored)
    """
    print(os.getcwd())


def handle_sysinfo(args: List[str]) -> None:
    """
    Handle the 'sysinfo' command to display system information.

    Args:
        args: Command arguments (ignored)
    """
    print("System Information:")
    print(f"  Platform: {platform.system()} {platform.release()}")
    print(f"  Machine: {platform.machine()}")

    # CPU information
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"  CPU Usage: {cpu_percent}%")
    except Exception as e:
        print(f"  CPU Usage: Unable to get CPU info ({e})")

    # Memory information
    try:
        memory = psutil.virtual_memory()
        print(f"  Memory: {get_human_readable_size(memory.used)} / {get_human_readable_size(memory.total)}")
        print(f"  Memory Usage: {memory.percent}%")
    except Exception as e:
        print(f"  Memory: Unable to get memory info ({e})")


def handle_mkdir(args: List[str]) -> bool:
    """
    Handle the 'mkdir' command to create directories.

    Args:
        args: Command arguments

    Returns:
        True if directory creation was successful, False otherwise
    """
    if not args:
        print("mkdir: missing argument")
        return False

    for dir_name in args:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"Created directory: {dir_name}")
        except PermissionError:
            print(f"mkdir: {dir_name}: Permission denied")
            return False
        except Exception as e:
            print(f"mkdir: {dir_name}: {e}")
            return False

    return True


def handle_rm(args: List[str]) -> bool:
    """
    Handle the 'rm' command to remove files/directories.

    Args:
        args: Command arguments

    Returns:
        True if removal was successful, False otherwise
    """
    if not args:
        print("rm: missing argument")
        return False

    recursive = '-r' in args
    targets = [arg for arg in args if arg != '-r']

    for target in targets:
        try:
            if os.path.isdir(target):
                if recursive:
                    import shutil
                    shutil.rmtree(target)
                    print(f"Removed directory: {target}")
                else:
                    print(f"rm: {target}: is a directory (use -r to remove directories)")
                    return False
            else:
                os.remove(target)
                print(f"Removed file: {target}")
        except FileNotFoundError:
            print(f"rm: {target}: No such file or directory")
            return False
        except PermissionError:
            print(f"rm: {target}: Permission denied")
            return False
        except Exception as e:
            print(f"rm: {target}: {e}")
            return False

    return True


def handle_exit(args: List[str]) -> bool:
    """
    Handle the 'exit' command to quit the terminal.

    Args:
        args: Command arguments (ignored)

    Returns:
        True to indicate the program should exit
    """
    print("Goodbye!")
    return True


def handle_help(args: List[str]) -> None:
    """
    Handle the 'help' command to show available commands.

    Args:
        args: Command arguments (ignored)
    """
    print("Available commands:")
    print("  ls       - List directory contents")
    print("  cd       - Change directory")
    print("  pwd      - Show current working directory")
    print("  mkdir    - Create directory")
    print("  rm       - Remove files/directories (use -r for directories)")
    print("  sysinfo  - Show system information")
    print("  history  - Show command history")
    print("  help     - Show this help message")
    print("  exit     - Exit the terminal")
    print("  quit     - Exit the terminal")
    print("\nYou can also use natural language commands:")
    print("  'create folder test' instead of 'mkdir test'")
    print("  'show me files' instead of 'ls'")
    print("  'go to Documents' instead of 'cd Documents'")


def handle_history(args: List[str]) -> None:
    """
    Handle the 'history' command to show command history.

    Args:
        args: Command arguments (ignored)
    """
    show_history()


def handle_ai_command(args: List[str]) -> None:
    """
    Handle natural language commands.

    Args:
        args: Command arguments (the natural language input)
    """
    if not args:
        print("Please provide a natural language command.")
        return

    natural_input = " ".join(args)
    command, cmd_args = interpret_natural_command(natural_input)

    if command:
        print(f"Interpreted as: {command} {' '.join(cmd_args)}")
        # Execute the interpreted command
        if command in COMMAND_HANDLERS:
            handler = COMMAND_HANDLERS[command]
            if command in ['cd', 'mkdir', 'rm', 'exit']:
                result = handler(cmd_args)
                if command == 'exit' and result:
                    return
                elif command in ['cd', 'mkdir', 'rm'] and not result:
                    return
            else:
                handler(cmd_args)
        else:
            print(f"Unknown command: {command}")
    else:
        print("Sorry, I couldn't understand that command.")
        print("Try: 'create folder test', 'show me files', 'go to Documents'")


# Command registry
COMMAND_HANDLERS: Dict[str, Callable] = {
    'ls': handle_ls,
    'cd': handle_cd,
    'pwd': handle_pwd,
    'mkdir': handle_mkdir,
    'rm': handle_rm,
    'sysinfo': handle_sysinfo,
    'exit': handle_exit,
    'quit': handle_exit,
    'help': handle_help,
    'history': handle_history,
    'ai': handle_ai_command
}
