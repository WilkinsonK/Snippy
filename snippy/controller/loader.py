from importlib import import_module

from consoleapp.controller.settings import load_settings
from consoleapp.controller.settings import preload_extentions
from consoleapp.controller.settings import get_settings

from consoleapp.controller.loggers import LoggerLoader
from consoleapp.controller.commands import CommandLoader


def __load_commands():
    command_settings = get_settings('COMMANDS')
    CommandLoader(command_settings)


def __load_loggers():
    logger_settings = get_settings('LOGGING')
    LoggerLoader(logger_settings)


def __load_extentions():
    extentions_settings = get_settings('EXTENTIONS')
    print(extentions_settings)


def load_app_settings(settings):
    settings_module = import_module(settings)
    preload_extentions(settings_module)
    load_settings(settings_module)


def load_application():
    __load_extentions()
    __load_loggers()
    __load_commands()
