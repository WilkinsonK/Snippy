from snippy.loaders.loggers import get_app_logger
from snippy.loaders.loggers import get_app_loggers
from snippy.loaders.commands import get_app_commands
from snippy.loaders.commands import get_app_command
from snippy.core.commands import BaseCommand


__version__ = '.'.join(['0', '0', '0'])

__all__ = (
    'get_app_logger', 'get_app_loggers', 'get_app_command',
    'get_app_commands', 'BaseCommand', 'get_version'
)

__doc__ = '''
A command line interface framework center focused on a rigid, but
open ended structure
'''


def get_version():
    return __version__
