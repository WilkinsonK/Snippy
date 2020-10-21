from importlib import import_module

from snippy.loaders.settings import get_app_settings

from snippy.loaders.loggers import LoggerLoader
from snippy.loaders.commands import CommandLoader
from snippy.loaders.settings import SettingsLoader


def __load_commands():
    CommandLoader(get_app_settings(('COMMANDS', 'PROJECT')))


def __load_loggers():
    LoggerLoader(get_app_settings('LOGGING'))


def __load_extentions():
    extentions_settings = get_app_settings('EXTENTIONS')
    print(extentions_settings)


def load_app_settings(module):
    SettingsLoader(import_module(module))


def load_application():
    __load_extentions()
    __load_loggers()
    __load_commands()
