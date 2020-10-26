import sys
import os

from importlib import import_module
from typing import Any, Dict, Iterable

from snippy.tools import get_project_name
from snippy.validators.settings import default_available_settings
from snippy.validators.settings import SettingsValidator


loaded_settings = dict()


def get_app_settings(settings: Iterable or str=None) -> dict:
    '''
    Return the requested settings if specified in an iterable,
    otherwise return all loaded settings
    '''
    global loaded_settings
    if not settings == None:
        return {s:loaded_settings[s] for s in loaded_settings if s in settings}
    return loaded_settings


class SettingsLoader(SettingsValidator):
    '''
    Reads and loads the settings defined in the application settings
    '''

    def __new__(cls, module):
        settings_obj = super(SettingsLoader, cls).__new__(cls)
        settings_obj.preload_extensions(module)
        settings_obj.load_settings(module)
        return settings_obj

    @classmethod
    def load_settings(cls, module):
        '''
        Load settings from the settings file
        '''
        settings = cls._read_settings_module(module)
        for s in settings:
            cls._verify_setting_type(settings, s)
        cls._update_settings(settings)

    @classmethod
    def preload_extensions(cls, module):
        '''
        Looks for any instances in EXTENSIONS to add to default
        settings prior to loading and verifying settings
        '''
        settings = cls._read_settings_module(module)
        if 'EXTENTIONS' in settings:
            for e in settings['EXTENTIONS']:
                ext_obj = import_module(e)
                cls.include_settings(ext_obj)

    @classmethod
    def include_settings(cls, module):
        '''
        Include a group of available settings in the 
        application default settings from a separate package
        '''
        global default_available_settings
        settings = module.extention_available_settings
        default_available_settings.update(settings)

    @classmethod
    def _update_settings(cls, settings: Dict[str, Any]):
        global loaded_settings
        settings['PROJECT'] = get_project_name()
        loaded_settings.update(settings)

    @classmethod
    def _read_settings_module(cls, module):
        global default_available_settings
        directory = [s for s in dir(module) if s in default_available_settings]
        module_dict = module.__dict__
        return {s:module_dict[s] for s in module_dict if s in directory}
