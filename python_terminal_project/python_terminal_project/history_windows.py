"""
Command history functionality for Windows (without readline dependency).
"""

import os
from typing import List, Optional


class CommandHistory:
    """
    Manages command history for the terminal (Windows-compatible version).
    """

    def __init__(self, history_file: str = ".terminal_history"):
        self.history_file = os.path.expanduser(history_file)
        self.history: List[str] = []
        self.max_history_size = 1000
        self.load_history()

    def load_history(self) -> None:
        """Load command history from file."""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    self.history = [line.strip() for line in f.readlines() if line.strip()]
        except Exception:
            self.history = []

    def save_history(self) -> None:
        """Save command history to file."""
        try:
            # Keep only the last max_history_size commands
            recent_history = self.history[-self.max_history_size:]

            with open(self.history_file, 'w') as f:
                for command in recent_history:
                    f.write(command + '\n')
        except Exception:
            pass  # Silently fail if we can't save history

    def add_command(self, command: str) -> None:
        """Add a command to history."""
        command = command.strip()
        if command and (not self.history or self.history[-1] != command):
            self.history.append(command)
            if len(self.history) > self.max_history_size:
                self.history.pop(0)

    def get_history(self) -> List[str]:
        """Get the command history."""
        return self.history.copy()

    def show_history(self) -> None:
        """Display command history."""
        if not self.history:
            print("No command history available.")
            return

        print("Command History:")
        for i, command in enumerate(self.history[-20:], 1):  # Show last 20 commands
            print(f"{i:3d}  {command}")


# Global history instance
command_history = CommandHistory()


def add_to_history(command: str) -> None:
    """Add a command to the global history."""
    command_history.add_command(command)


def get_history() -> List[str]:
    """Get the command history."""
    return command_history.get_history()


def show_history() -> None:
    """Show the command history."""
    command_history.show_history()
