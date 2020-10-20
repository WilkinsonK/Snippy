from importlib import import_module

from snippy.loaders.settings import get_app_settings

from snippy.loaders.loggers import LoggerLoader
from snippy.loaders.commands import CommandLoader
from snippy.loaders.settings import SettingsLoader


def __load_commands():
    command_settings = get_app_settings(('COMMANDS', 'PROGRAM', 'PROJECT'))
    CommandLoader(command_settings)


def __load_loggers():
    logger_settings = get_app_settings('LOGGING')
    LoggerLoader(logger_settings)


def __load_extentions():
    extentions_settings = get_app_settings('EXTENTIONS')
    print(extentions_settings)


def load_app_settings(module):
    settings_module = import_module(module)
    SettingsLoader(settings_module)


def load_application():
    __load_extentions()
    __load_loggers()
    __load_commands()
