import os

from logging import Logger, Formatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging import Handler, StreamHandler, FileHandler, NullHandler

from typing import Any, List, Dict

from posterboard.validators.loggers import LoggerValidator


logger_levels = {
    'debug': DEBUG,
    'info': INFO,
    'warning': WARNING,
    'error': ERROR,
    'critical': CRITICAL,
}


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

        for handler_config in logger_settings['HANDLERS']:
            self._setup_handler(handler_config)

    def _setup_handler(self, config: Dict[str, Any]):
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

        if handler in ('file', 'file_handler'):
            handler = FileHandler(path, mode=mode, encoding=encoding)
        elif handler in ('stream', 'stream_handler'):
            handler = StreamHandler(stream=stream)
        elif handler in ('null', 'null_handler'):
            handler = NullHandler()

        formatter = Formatter(
            fmt=format_, datefmt=datefmt, style=style, validate=validate
        )

        handler.setLevel(level=logger_levels[level])
        handler.setFormatter(fmt=formatter)

        self.handlers.append(handler)
        self.addHandler(handler)
