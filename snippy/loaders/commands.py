from typing import Dict, Tuple, List
from importlib import import_module

from snippy.core.commands import BaseCommand, CommandObject


loaded_commands = dict()


def get_app_command(command: str) -> CommandObject:
    '''
    Returns a command if it exists in project package
    '''
    if command not in loaded_commands:
        raise NameError(f"command '{command}' not found")
    return loaded_commands[command]


def get_app_commands() -> Dict[str, CommandObject]:
    '''
    Returns the application loaded commands
    '''
    return loaded_commands


class CommandLoader(object):
    '''
    Searches for commands from application settings.py source file
    within commands directory
    '''

    def __init__(self, settings: Tuple[str] or List[str]):
        self.load_commands_from_settings(settings)

    def load_commands_from_settings(self, settings):
        comm = settings.get('COMMANDS')
        root = settings.get('PROJECT')

        if isinstance(comm, str):
            self.load_from_one_module(root, comm)
        if isinstance(comm, tuple):
            self.load_multiple_modules(root, comm)

    def load_multiple_modules(self, root: str, commands: tuple):
        for command in commands:
            self.load_from_one_module(root, command)

    def load_from_one_module(self, root: str, command: str):
        command_mod = self._import_command_module(command)
        for c in self._get_commands(command_mod):
            loaded_commands.update({c._name(): c})

    def _get_commands(self, module) -> CommandObject:
        module_dict = module.__dict__
        commands = list()
        for i in module_dict:
            if not isinstance(module_dict[i], type):
                continue
            if not issubclass(module_dict[i], CommandObject):
                continue
            if module_dict[i] is BaseCommand:
                continue
            if issubclass(module_dict[i], BaseCommand):
                commands.append(module_dict[i])
        return commands

    def _import_command_module(self, command: str):
        return import_module(command)
