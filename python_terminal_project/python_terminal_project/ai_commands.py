"""
AI-powered command processing for the Python Command Terminal.
This module handles natural language command interpretation.
"""

import os
import re
from typing import List, Dict, Optional, Tuple


class AICommandProcessor:
    """
    Processes natural language commands and converts them to terminal commands.
    """

    def __init__(self):
        self.command_patterns = {
            'create_folder': {
                'patterns': [
                    r'create (?:a |an )?folder (.+)',
                    r'make (?:a |an )?folder (.+)',
                    r'mkdir (.+)',
                    r'create (?:a |an )?directory (.+)'
                ],
                'handler': self._handle_create_folder
            },
            'move_file': {
                'patterns': [
                    r'move (.+) to (.+)',
                    r'mv (.+) (.+)',
                    r'move (.+) into (.+)'
                ],
                'handler': self._handle_move_file
            },
            'list_files': {
                'patterns': [
                    r'show (?:me |)files',
                    r'list files',
                    r'what files are (?:in |at )(.+)',
                    r'show (?:me |)what\'s in (.+)'
                ],
                'handler': self._handle_list_files
            },
            'change_directory': {
                'patterns': [
                    r'go to (.+)',
                    r'cd (.+)',
                    r'change to (.+)',
                    r'navigate to (.+)'
                ],
                'handler': self._handle_change_directory
            }
        }

    def process_command(self, natural_command: str) -> Tuple[Optional[str], List[str]]:
        """
        Process a natural language command and return the corresponding terminal command.

        Args:
            natural_command: The natural language command from the user

        Returns:
            Tuple of (command_name, arguments) if recognized, (None, []) otherwise
        """
        for command_name, config in self.command_patterns.items():
            for pattern in config['patterns']:
                match = re.match(pattern, natural_command.lower().strip())
                if match:
                    return config['handler'](match.groups())

        return None, []

    def _handle_create_folder(self, groups: tuple) -> Tuple[str, List[str]]:
        """Handle folder creation commands."""
        folder_name = groups[0].strip()
        return 'mkdir', [folder_name]

    def _handle_move_file(self, groups: tuple) -> Tuple[str, List[str]]:
        """Handle file moving commands."""
        source, destination = groups[0].strip(), groups[1].strip()
        return 'mv', [source, destination]

    def _handle_list_files(self, groups: tuple) -> Tuple[str, List[str]]:
        """Handle file listing commands."""
        if len(groups) > 0 and groups[0]:
            path = groups[0].strip()
            return 'ls', [path]
        return 'ls', []

    def _handle_change_directory(self, groups: tuple) -> Tuple[str, List[str]]:
        """Handle directory changing commands."""
        directory = groups[0].strip()
        return 'cd', [directory]


def interpret_natural_command(command: str) -> Tuple[Optional[str], List[str]]:
    """
    Interpret a natural language command and return terminal command equivalent.

    Args:
        command: Natural language command

    Returns:
        Tuple of (command_name, arguments) or (None, []) if not recognized
    """
    processor = AICommandProcessor()
    return processor.process_command(command)
