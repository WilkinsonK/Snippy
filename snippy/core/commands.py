from abc import ABCMeta, abstractmethod
from typing import Dict, Tuple
from argparse import ArgumentParser

from snippy.tools import objname, classname, dictionary


class CommandObject(object, metaclass=ABCMeta):
    '''
    Defines the default attributes a command class object
    has available to access/modify

    This class is not meant to be directly instantiated
    '''

    parameters: Dict[Tuple[str] or str, Dict[str, str]] # Defines the arguments
    name: str                                           # Define a custom name
    description: str                                    # Define a description
    is_cached: bool                                     # Cache the command obj

    def execute(self, argv):
        raise NotImplementedError


class AbstractCommand(CommandObject):
    '''
    Abstract class which BaseClass is derived from.
    Handles the attributes of Command Objects
    '''

    @property
    def description(self):
        return dictionary(self).get('description', '')

    @property
    def parameters(self):
        return dictionary(self).get('parameters', dict())

    @property
    def is_cached(self):
        return dictionary(self).get('is_cached', False)

    @property
    def name(self):
        return dictionary(self).get('name', classname(self).lower())

    @classmethod
    def _name(cls):
        return dictionary(cls).get('name', objname(cls).lower())


class BaseCommand(AbstractCommand):
    '''
    Abstract base class all Command Objects are derived from.
    '''

    @abstractmethod
    def execute(self, argv):
        raise NotImplementedError
