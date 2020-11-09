from posterboard.loaders.loggers import get_app_logger
from posterboard.loaders.loggers import get_app_loggers
from posterboard.loaders.commands import get_app_commands
from posterboard.loaders.commands import get_app_command
from posterboard.loaders.settings import get_app_settings
from posterboard.core.commands import BaseCommand


__version__ = '.'.join(['0', '0', '0'])

__all__ = (
    'get_app_logger', 'get_app_loggers', 'get_app_command',
    'get_app_commands', 'BaseCommand', 'get_version', 'get_app_settings'
)

__doc__ = '''
A command line interface framework center focused on a rigid, but
open ended structure
'''


def get_version():
    return __version__
