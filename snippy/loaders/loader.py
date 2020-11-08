from importlib import import_module

from snippy.loaders.settings import get_app_settings

from snippy.loaders.loggers import LoggerLoader
from snippy.loaders.commands import CommandLoader
from snippy.loaders.settings import SettingsLoader


class AppLoader(object):
    '''
    Central loading class. Utilizes the subsequent loaders
    (LoggerLoader, CommandLoader, SettingsLoader, etc.) to fully
    load objects from a project
    '''

    @staticmethod
    def load_settings(module):
        '''Loads the config file, 'settings.py' by default'''
        SettingsLoader(import_module(module))

    @staticmethod
    def load_application():
        '''
        After settings are loaded, loads the application and its
        components
        '''
        get_app_settings('EXTENSIONS')
        LoggerLoader(get_app_settings('LOGGING'))
        CommandLoader(get_app_settings(('COMMANDS', 'PROJECT')))
