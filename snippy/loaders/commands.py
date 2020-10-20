from typing import Tuple, List
from importlib import import_module

from snippy.commands.base import CommandObject


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
        command_config = settings.get('COMMANDS')

        if isinstance(command_config, str):
            cls.load_one_command(settings)
        if isinstance(command_config, tuple):
            cls.load_multiple_commands(settings)

    @classmethod
    def load_multiple_commands(cls, commands: tuple):
        for command in commands:
            cls.load_one_command(command)

    @classmethod
    def load_one_command(cls, command: str):
        pass
