from abc import ABCMeta, abstractmethod
from typing import Dict, Tuple
from argparse import ArgumentParser

from snippy.tools import objname, classname, dictionary
from snippy.validators.commands import CommandValidator


class CommandObject(object, metaclass=ABCMeta):
    parameters: Dict[Tuple[str] or str, Dict[str, str]] # Defines the arguments
    help: str                                           # Defines the help text
    name: str                                           # Define a custom name
    description: str                                    # Define a description
    is_cached: bool                                     # Cache the command obj
    with_debug: bool                                    # Push debug messsages

    def execute(self, args):
        raise NotImplementedError

    def _add_parameters(self, parser: ArgumentParser):
        for param in self.parameters:
            if isinstance(param, str):
                parser.add_argument(param, **self.parameters[param])
            if isinstance(param, tuple):
                parser.add_argument(*param, **self.parameters[param])


class AbstractCommand(CommandObject):
    '''
    Abstract class which BaseClass is derived from.
    Handles the attributes of Command Objects
    '''

    @property
    def description(self):
        return dictionary(self).get('description', '')

    @property
    def help(self):
        return dictionary(self).get('help', '')

    @property
    def parameters(self):
        return dictionary(self).get('parameters', dict())

    @property
    def name(self):
        return dictionary(self).get('name', classname(self).lower())

    @classmethod
    def _name(cls):
        return dictionary(cls).get('name', objname(cls).lower())


class BaseCommand(AbstractCommand, CommandValidator):
    '''
    Abstract base class all Command Objects are derived from.
    '''

    @abstractmethod
    def execute(self, args):
        raise NotImplementedError
