import os

from logging import Logger
from logging import Formatter
from logging import Handler
from logging import FileHandler
from logging import StreamHandler
from logging import NullHandler

from typing import Any, List
from typing import Dict

from snippy.logger.levels import logger_levels
from snippy.validators.loggers import LoggerValidator



class AppLogger(Logger, LoggerValidator):
    '''
    Creates a logger object from builtin logging module with
    modifications to automatically create a logger with handlers
    and a format
    '''

    handlers: List[Handler]

    def __init__(self, logger_settings: Dict[str, Any]):
        self._verify_logger_name(logger_settings)
        self._verify_logger_handlers(logger_settings)
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
