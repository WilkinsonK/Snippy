from abc import ABCMeta, abstractmethod
from typing import Dict, Tuple
from argparse import ArgumentParser

from snippy.util import objname, dictionary
from snippy.validators.commands import CommandValidator


class CommandObject(object, metaclass=ABCMeta):
    parameters: Dict[Tuple[str] or str, Dict[str, str]] # Defines the arguments
    help: str                                           # Defines the help text
    name: str                                           # Define a custom name
    is_cached: bool                                     # Cache the command obj
    with_debug: bool                                    # Push debug messsages

    def execute(self):
        raise NotImplementedError

    def add_parameters(self, parser):
        raise NotImplementedError


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
        return dictionary(self).get('name', objname(self).lower())

    @classmethod
    def _name(cls):
        return dictionary(cls).get('name', objname(cls).lower())


class BaseCommand(AbstractCommand, CommandValidator):
    '''
    Abstract base class all Command Objects are derived from.
    '''

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    def _add_parameters(self, parser: ArgumentParser):
        for param in self.parameters:
            parser.add_argument(*param, **self.parameters[param])
