from typing import Dict, Tuple, Any

from posterboard.core.loggers import AppLogger

loaded_loggers = dict()


def get_app_logger(logger_name: str) -> AppLogger:
    '''
    Returns one loaded logger from application settings by NAME
    attribute
    '''
    if (logger := loaded_loggers.get(logger_name)) is None:
        return loaded_loggers.get('main')
    return logger


def get_app_loggers():
    '''
    Returns all loaded loggers from applications in the form of a
    dictionary with key/value pairs of NAME/AppLogger
    '''
    return loaded_loggers


class LoggerLoader(object):
    '''
    Creates and loads AppLogger objects from application settings
    '''

    def __init__(self, settings: Tuple[Dict[str, Any]] or Dict[str, Any]):
        self.load_loggers_from_settings(settings)

    def load_loggers_from_settings(self, settings):
        '''
        Builds loggers from settings file
        '''

        if isinstance(settings, dict):
            self.load_one_logger(settings)
        if isinstance(settings, tuple):
            self.load_multiple_loggers(settings)

    def load_multiple_loggers(self, logger_config: Tuple[Dict[str, Any]]):
        for logger in logger_config:
            self.load_one_logger(logger)

    def load_one_logger(self, logger_config: Dict[str, Any]):
        logger_obj = AppLogger(logger_config)
        logger_name = logger_config['NAME']
        loaded_loggers[logger_name] = logger_obj
