from abc import ABC
from typing import Any, Dict


default_available_settings = {
    'PROGRAM': str,
    'DESCRIPTION': str,
    'HELP': str,
    'EXTENTIONS': tuple,
    'COMMANDS': tuple,
    'LOGGING': object
}

class SettingsValidator(ABC):

    @classmethod
    def _verify_setting_type(cls, settings: Dict[str, Any], id_):
        global default_available_settings
        defaults = default_available_settings
        setting = settings[id_]
        default = defaults[id_]
        if not isinstance(setting, default):
            raise TypeError(
                f"Invalid type for setting '{id_}' must be {defaults[id_]}"
            )