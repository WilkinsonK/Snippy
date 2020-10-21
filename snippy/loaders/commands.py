from typing import Tuple, List
from importlib import import_module

from snippy.commands.base import BaseCommand, CommandObject


loaded_commands = dict()


def get_app_command(command_name: str) -> CommandObject:
    if (command := loaded_commands.get(command_name)) is None:
        raise NameError(f"No such command named {command_name}")
    return command


class CommandLoader(object):

    def __new__(cls, settings: Tuple[str] or List[str]):
        loader_obj = super(CommandLoader, cls).__new__(cls)
        loader_obj.load_commands_from_settings(settings)
        return loader_obj

    @classmethod
    def load_commands_from_settings(cls, settings):
        comm = settings.get('COMMANDS')
        root = settings.get('PROJECT')

        if isinstance(comm, str):
            cls.load_from_one_module(root, comm)
        if isinstance(comm, tuple):
            cls.load_multiple_modules(root, comm)

    @classmethod
    def load_multiple_modules(cls, root: str, commands: tuple):
        for command in commands:
            cls.load_from_one_module(root, command)

    @classmethod
    def load_from_one_module(cls, root: str, command: str):
        command_mod = cls.__import_command_module(root, command)
        for c in cls.__get_commands(command_mod):
            loaded_commands.update({c._name(): c})

    @classmethod
    def __get_commands(cls, module) -> CommandObject:
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

    @classmethod
    def __import_command_module(cls, root: str, command: str):
        module = '.'.join([root, command])
        return import_module(module)
