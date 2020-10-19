from typing import Tuple, List

class CommandLoader(object):

    def __new__(cls, settings: Tuple[str] or List[str]):
        loader_obj = super(CommandLoader, cls).__new__(cls)
        loader_obj.load_commands_from_settings(settings)
        return loader_obj

    @classmethod
    def load_commands_from_settings(cls, settings):
        settings = settings.get('COMMANDS')
        print(settings)