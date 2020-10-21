from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Tuple


from snippy.util import classname, dictionary
from snippy.validators.commands import CommandValidator


class CommandObject(object, metaclass=ABCMeta):
    parameters: Dict[Tuple[str] or str, Dict[str, str]] # Defines the arguments
    help: str                                           # Defines the help text
    name: str                                           # Define a custom name
    is_cached: bool                                     # Cache the command obj
    with_debug: bool                                    # Push debug messsages


class AbstractCommand(CommandObject):
    '''
    Abstract class which BaseClass is derived from.
    Handles the attributes of Command Objects
    '''

    @property
    def help(self):
        return dictionary(self).get('help', '')

    @property
    def parameters(self):
        return dictionary(self).get('parameters', dict())

    @property
    def name(self):
        return dictionary(self).get('name', self.__name__.lower())

    @classmethod
    def _name(cls):
        return dictionary(cls).get('name', cls.__qualname__.lower())


class BaseCommand(AbstractCommand, CommandValidator):
    '''
    Abstract base class all Command Objects are derived from.
    '''

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def parse_arguments(self, argv: List[Any]):
        raise NotImplementedError

    @abstractmethod
    def add_parameters(self, parser):
        raise NotImplementedError
