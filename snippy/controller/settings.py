from importlib import import_module
from typing import Any, Dict, Iterable

default_available_settings = {
    'PROGRAM': str,
    'DESCRIPTION': str,
    'HELP': str,
    'EXTENTIONS': tuple,
    'COMMANDS': tuple,
    'LOGGING': object
}

loaded_settings = dict()


def __verify_setting_type(settings: Dict[str, Any], id_):
    global default_available_settings
    defaults = default_available_settings
    setting = settings[id_]
    default = defaults[id_]
    if not isinstance(setting, default):
        raise ValueError(
            f"Invalid type for setting '{id_}' must be {defaults[id_]}"
        )


def __update_settings(settings: Dict[str, Any]):
    global load_settings
    loaded_settings.update(settings)


def __read_settings_module(module):
    global default_available_settings
    directory = [s for s in dir(module) if s in default_available_settings]
    module_dict = module.__dict__
    return {s:module_dict[s] for s in module_dict if s in directory}


def include_settings(module):
    '''
    Include a group of available settings in the 
    application default settings from a separate package
    '''
    global default_available_settings
    settings = module.extention_available_settings
    default_available_settings.update(settings)


def preload_extentions(module):
    settings = __read_settings_module(module)
    if 'EXTENTIONS' in settings:
        for e in settings['EXTENTIONS']:
            ext_obj = import_module(e)
            include_settings(ext_obj)


def load_settings(module):
    '''
    Load settings from the targeted module. First verifying the
    settings are valid entries from the default settings
    '''
    settings = __read_settings_module(module)
    for s in settings:
        __verify_setting_type(settings, s)
    __update_settings(settings)


def get_settings(settings: Iterable=None) -> dict:
    '''
    Return the requested settings if specified in an iterable,
    otherwise return all loaded settings
    '''
    global loaded_settings
    if not settings == None:
        return {s:loaded_settings[s] for s in loaded_settings if s in settings}
    return loaded_settings
