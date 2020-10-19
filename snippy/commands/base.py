from abc import ABCMeta, abstractmethod
from typing import Dict


class BaseCommand(metaclass=ABCMeta):
    arguments: Dict[str, dict]
    optionals: Dict[tuple, dict]
    help: str

    def __getattr__(self, attr):
        if attr not in self.__annotations__:
            raise AttributeError(
                f"Command object has no attribute '{attr}'"
            )
        self.__get_default_attribute(attr)

    def __get_default_attribute(self, attr):
        attr_type = self.__annotations__[attr]
        default_values = {
            bytes: b'',
            str: '',
            bool: False,
            int: 0,
            float: 0.00,
            list: [],
            dict: {},
            tuple: ()
        }
        return default_values.get(attr_type, None)

    @property
    def _arguments(self):
        return self.arguments

    @property
    def _optionals(self):
        return self.optionals

    @abstractmethod
    def __init__(self, argv):
        pass

    @abstractmethod
    def execute(self):
        raise NotImplementedError
