from argparse import ArgumentParser
from typing import List

from snippy import get_app_logger
from snippy.core.commands import CommandObject
from snippy.loaders.commands import get_app_command
from snippy.tools import get_project_name
from snippy.tools.names import get_project_name


class AppParser:
    '''
    Take a list of arguments and parse them out to pass them into
    a CommandObject or multiple CommandObjects
    '''


    def __init__(self, argv: List[str]):
        self.commands = self.get_commands(argv[1:])
        self.logger = get_app_logger(get_project_name())

    def execute_commands(self):
        for c in self.commands:
            self.execute_one_command(c[0], c[1])

    def execute_one_command(self, command: CommandObject, args: list):
        command_obj = command()

        parser = self._create_parser_obj(command_obj)
        args_ = parser.parse_args(args)

        result = command_obj.execute(args_)

    def get_commands(self, argv):
        command_vars = self._find_multiple_commands(argv)
        commands = [get_app_command(c[0]) for c in command_vars]
        arguments = [a[1:] for a in command_vars]
        return [(commands[i], arguments[i]) for i in range(len(commands))]

    @classmethod
    def _create_parser_obj(cls, command: CommandObject) -> ArgumentParser:
        parser = cls._add_parameters(command)
        return parser

    @classmethod
    def _add_parameters(cls, command: CommandObject):
        parser = ArgumentParser(prog=command.name)

        for param in command.parameters:
            if isinstance(param, str):
                parser.add_argument(param, **command.parameters[param])
            if isinstance(param, tuple):
                parser.add_argument(*param, **command.parameters[param])
        return parser

    @classmethod
    def _find_multiple_commands(cls, argv) -> List[list] or list:
        stringed = ' '.join(argv)
        return cls._parse_commands(stringed)

    @classmethod
    def _parse_commands(cls, commands: str):
        commands = commands.split('/')
        for c in range(len(commands)):
            commands[c] = cls._cleanup_strings(commands[c])
            commands[c] = commands[c].split(' ')
        return commands

    @classmethod
    def _cleanup_strings(cls, command: str):
        command = command.rstrip(' ')
        command = command.lstrip(' ')
        return command
