import os

from abc import ABC
from typing import Dict, Any
from logging import FileHandler

from snippy.logger.levels import logger_levels


class LoggerValidator(ABC):

    def _verify_logger_name(self, settings: Dict[str, Any]):
        if 'NAME' not in settings:
            raise AttributeError(
                "NAME missing from logger settings"
            )
        if not isinstance(settings['NAME'], str):
            raise ValueError(
                "NAME in logger settings must be a string or bytes like object"
            )
        self.name = settings['NAME']

    def _verify_logger_handlers(self, settings: Dict[str, Any]):
        logname = self.name

        if 'HANDLERS' not in settings:
            raise AttributeError(
                f"HANDLERS missing from {logname} settings"
            )
        handlers = settings['HANDLERS']
        if len(handlers) < 1:
            raise AttributeError(
                f"HANDLERS in {logname} has no configs"
            )
        if not isinstance(handlers, (list, tuple)):
            raise ValueError(
                f"HANDLERS in {logname} is must either be a tuple or list object"
            )

        for h in range(len(handlers)):
            handler_config = handlers[h]

            self._verify_type_config(h, handler_config)
            self._verify_format_config(h, handler_config)
            self._verify_level_config(h, handler_config)

    def _verify_type_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'TYPE' not in config:
            raise AttributeError(
                f"TYPE missing in {logname} HANDLERS[{hand}] config"
            )
        if issubclass(config['TYPE'], FileHandler):
            self._verify_path_config(hand, config)
            self._verify_mode_config(hand, config)
            self._verify_encoding_config(hand, config)

    def _verify_encoding_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'ENCODING' in config and not isinstance(config['ENCODING'], str):
            raise ValueError(
                f"ENCODING in {logname} HANDLERS[{hand}] must be a string"
            )

    def _verify_mode_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if not isinstance(config['MODE'], str):
            raise ValueError(
                f"MODE in {logname} HANDLERS[{hand}] must be a string object"
            )

    def _verify_path_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'PATH' not in config:
            raise AttributeError(
            f"PATH missing in {logname} HANDLERS[{hand}] config"
        )
        if not isinstance(config['PATH'], (str, bytes)):
            raise ValueError(
            f"PATH in {logname} HANDLERS[{hand}] must be a string object"
        )
        if not os.path.exists(config['PATH']):
            raise FileExistsError(
                f"PATH in {logname} HANDLERS[{hand}] does not exist"
            )

    def _verify_format_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'FORMAT' not in config:
            raise AttributeError(
                f"FORMAT missing in {logname} HANDLERS[{hand}] config"
            )
        if not isinstance(config['FORMAT'], str):
            raise ValueError(
                f"FORMAT in {logname} HANDLERS[{hand}] must be a string object"
            )

    def _verify_level_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'LEVEL' not in config:
            raise AttributeError(
                f"LEVEL missing in {logname} HANDLERS[{hand}] config"
            )
        if not isinstance(config['LEVEL'], str):
            raise ValueError(
                f"LEVEL in {logname} HANDLERS[{hand}] must be a string object"
            )
        if config['LEVEL'] not in logger_levels:
            raise KeyError(
                f"LEVEL in {logname} HANDLERS[{hand}] is not a valid level key"
        )
