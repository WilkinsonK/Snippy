import sys
import os

from importlib import import_module
from typing import Any, Dict, Iterable

from snippy.tools import get_project_name
from snippy.validators.settings import default_available_settings
from snippy.validators.settings import SettingsValidator


loaded_settings = dict()


def get_app_settings(settings: Iterable or str=None) -> Any:
    '''
    Return the requested settings if specified in an iterable or string,
    otherwise return all loaded settings
    '''
    global loaded_settings
    if not settings == None and not isinstance(settings, str):
        return {s:loaded_settings[s] for s in loaded_settings if s in settings}
    if isinstance(settings, str):
        return loaded_settings.get(settings)
    return loaded_settings


class SettingsLoader(SettingsValidator):
    '''
    Reads and loads the settings defined in the application settings
    '''

    def __init__(self, module):
        self.preload_extensions(module)
        self.load_settings(module)

    def load_settings(self, module):
        '''
        Load settings from the settings file
        '''
        settings = self._read_settings_module(module)
        for s in settings:
            self._verify_setting_type(settings, s)
        self._update_settings(settings)

    def preload_extensions(self, module):
        '''
        Looks for any instances in EXTENSIONS to add to default
        settings prior to loading and verifying settings
        '''
        settings = self._read_settings_module(module)
        if 'EXTENTIONS' in settings:
            for e in settings['EXTENTIONS']:
                ext_obj = import_module(e)
                self.include_settings(ext_obj)

    def include_settings(self, module):
        '''
        Include a group of available settings in the 
        application default settings from a separate package
        '''
        global default_available_settings
        settings = module.extention_available_settings
        default_available_settings.update(settings)

    def _update_settings(self, settings: Dict[str, Any]):
        global loaded_settings
        settings['PROJECT'] = get_project_name()
        loaded_settings.update(settings)

    def _read_settings_module(self, module):
        global default_available_settings
        directory = [s for s in dir(module) if s in default_available_settings]
        module_dict = module.__dict__
        return {s:module_dict[s] for s in module_dict if s in directory}
