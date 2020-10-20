from abc import ABCMeta, abstractmethod
from typing import Dict, Tuple


from snippy.util import classname, dictionary


class AbstractCommand(metaclass=ABCMeta):
    '''
    Abstract class which BaseClass is derived from.
    Handles the attributes of Command Objects
    '''
    parameters: Dict[Tuple[str] or str, Dict[str, str]] # Defines the arguments
    help: str                                           # Defines the help text
    name: str                                           # Define a custom name
    is_cached: bool                                     # Cache the command obj
    with_debug: bool                                    # Push debug messsages

    @property
    def help(self):
        return dictionary(self).get('help', '')

    @property
    def parameters(self):
        return dictionary(self).get('parameters', dict())

    @property
    def name(self):
        return dictionary(self).get('name', classname(self).lower())


class BaseCommand(AbstractCommand, metaclass=ABCMeta):
    '''
    Abstract base class all Command Objects are derived from.
    '''

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def parse_arguments(self, argv):
        raise NotImplementedError

    @abstractmethod
    def add_parameters(self, parser):
        raise NotImplementedError
