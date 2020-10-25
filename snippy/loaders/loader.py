from importlib import import_module

from snippy.loaders.settings import get_app_settings

from snippy.loaders.loggers import LoggerLoader
from snippy.loaders.commands import CommandLoader
from snippy.loaders.settings import SettingsLoader


class AppLoader(object):

    @staticmethod
    def load_settings(module):
        SettingsLoader(import_module(module))

    @staticmethod
    def load_application():
        AppLoader._load_extensions()
        AppLoader._load_loggers()
        AppLoader._load_commands()

    @classmethod
    def _load_loggers(cls):
        LoggerLoader(get_app_settings('LOGGING'))

    @classmethod
    def _load_commands(cls):
        CommandLoader(get_app_settings(('COMMANDS', 'PROJECT')))

    @classmethod
    def _load_extensions(cls):
        get_app_settings('EXTENSIONS')
