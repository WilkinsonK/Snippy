from argparse import ArgumentParser
import argparse
from typing import List

from snippy.loaders.commands import get_app_command
from snippy.loaders.commands import CommandObject


class AppParser:

    def __init__(self, argv: List[str]):
        self.commands = self.get_commands(argv[1:])
        self.execute_commands()

    def execute_commands(self):
        for c in self.commands:
            print(c, self.commands[c])

    def get_commands(self, argv):
        command_vars = self._find_multiple_commands(argv)
        commands = [get_app_command(c[0]) for c in command_vars]
        arguments = [a[1:] for a in command_vars]
        return {commands[i]:arguments[i] for i in range(len(commands))}

    def _find_multiple_commands(self, argv) -> List[list] or list:
        stringed = ' '.join(argv)
        return self._parse_commands(stringed)

    def _parse_commands(self, commands: str):
        commands = commands.split('/')
        for c in range(len(commands)):
            commands[c] = self._cleanup_strings(commands[c])
            commands[c] = commands[c].split(' ')
        return commands

    def _cleanup_strings(self, command: str):
        command = command.rstrip(' ')
        command = command.lstrip(' ')
        return command
