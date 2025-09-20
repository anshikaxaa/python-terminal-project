#!/usr/bin/env python3
"""
Python Command Terminal - Final Enhanced Version
A fully functional command-line terminal with AI capabilities, command history,
and comprehensive file system operations (Windows-compatible).
"""

import os
import sys
from commands_final import COMMAND_HANDLERS
from history_windows import add_to_history


def main():
    """
    Main function that runs the enhanced command terminal loop.
    """
    print("Python Command Terminal - Enhanced Version")
    print("Features: AI commands, command history, auto-completion")
    print("Type 'help' for available commands, 'exit' to quit.")
    print("-" * 60)

    # Main command loop
    while True:
        try:
            # Get current working directory for prompt
            current_dir = os.getcwd()
            prompt = f"[{current_dir}]> "

            # Get user input
            user_input = input(prompt).strip()

            if not user_input:
                continue

            # Add command to history
            add_to_history(user_input)

            # Parse command and arguments
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            # Handle the command
            if command in COMMAND_HANDLERS:
                handler = COMMAND_HANDLERS[command]

                # Special handling for commands that return boolean values
                if command in ['cd', 'mkdir', 'rm', 'exit']:
                    result = handler(args)
                    if command == 'exit' and result:
                        break
                    elif command in ['cd', 'mkdir', 'rm'] and not result:
                        continue
                else:
                    # Other commands don't return values
                    handler(args)
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands.")
                print("Or try natural language: 'create folder test'")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the terminal.")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
