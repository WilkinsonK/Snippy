import os

from logging import Logger
from logging import Formatter
from logging import Handler
from logging import FileHandler
from logging import StreamHandler
from logging import NullHandler

from typing import Any
from typing import Dict

from snippy.logger.levels import logger_levels


class AppLogger(Logger):

    handlers = [Handler]

    def __init__(self, logger_settings: Dict[str, Any]):
        self.__verify_logger_name(logger_settings)
        self.__verify_logger_handlers(logger_settings)
        super().__init__(self.name)
        self.__setup_logger(logger_settings)

    def __setup_logger(self, settings: Dict[str, Any]):
        for handler_config in settings['HANDLERS']:
            self.__setup_handler(handler_config)

    def __setup_handler(self, config: Dict[str, Any]):
        handler: Handler    = config.get('TYPE')
        format_: str        = config.get('FORMAT')
        level: str          = config.get('LEVEL')
        path: str           = config.get('PATH')
        mode: str           = config.get('MODE', 'w')
        encoding: str       = config.get('ENCODING', 'utf-8')
        stream: str         = config.get('STREAM', None)
        datefmt: str        = config.get('DATEFMT', None)
        style: str          = config.get('STYLE', '%')
        validate: bool      = config.get('VALIDATE', True)

        if issubclass(handler, FileHandler):
            handler = handler(path, mode=mode, encoding=encoding)
        elif issubclass(handler, StreamHandler):
            handler = handler(stream=stream)
        elif issubclass(handler, NullHandler):
            handler = handler()

        formatter = Formatter(
            fmt=format_, datefmt=datefmt, style=style, validate=validate
        )

        handler.setLevel(level=logger_levels[level].value)
        handler.setFormatter(fmt=formatter)

        self.handlers.append(handler)
        self.addHandler(handler)

    def __verify_logger_name(self, settings: Dict[str, Any]):
        if 'NAME' not in settings:
            raise AttributeError(
                "NAME missing from logger settings"
            )
        if not isinstance(settings['NAME'], str):
            raise ValueError(
                "NAME in logger settings must be a string or bytes like object"
            )
        self.name = settings['NAME']

    def __verify_logger_handlers(self, settings: Dict[str, Any]):
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

            self.__verify_type_config(h, handler_config)
            self.__verify_format_config(h, handler_config)
            self.__verify_level_config(h, handler_config)

    def __verify_type_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'TYPE' not in config:
            raise AttributeError(
                f"TYPE missing in {logname} HANDLERS[{hand}] config"
            )
        if issubclass(config['TYPE'], FileHandler):
            self.__verify_path_config(hand, config)
            self.__verify_mode_config(hand, config)
            self.__verify_encoding_config(hand, config)

    def __verify_encoding_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'ENCODING' in config and not isinstance(config['ENCODING'], str):
            raise ValueError(
                f"ENCODING in {logname} HANDLERS[{hand}] must be a string"
            )

    def __verify_mode_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if not isinstance(config['MODE'], str):
            raise ValueError(
                f"MODE in {logname} HANDLERS[{hand}] must be a string object"
            )

    def __verify_path_config(self, hand: str, config: Dict[str, Any]):
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

    def __verify_format_config(self, hand: str, config: Dict[str, Any]):
        logname = self.name
        if 'FORMAT' not in config:
            raise AttributeError(
                f"FORMAT missing in {logname} HANDLERS[{hand}] config"
            )
        if not isinstance(config['FORMAT'], str):
            raise ValueError(
                f"FORMAT in {logname} HANDLERS[{hand}] must be a string object"
            )

    def __verify_level_config(self, hand: str, config: Dict[str, Any]):
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
