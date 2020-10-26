from typing import Dict, Tuple, Any

from snippy.logger.loggers import AppLogger

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

    def __new__(cls, settings: Tuple[Dict[str, Any]] or Dict[str, Any]):
        loader_obj = super(LoggerLoader, cls).__new__(cls)
        loader_obj.load_loggers_from_settings(settings)
        return loader_obj

    @classmethod
    def load_loggers_from_settings(cls, settings):
        '''
        Builds loggers from settings file
        '''
        settings = settings.get('LOGGING')

        if isinstance(settings, dict):
            cls.load_one_logger(settings)
        if isinstance(settings, tuple):
            cls.load_multiple_loggers(settings)

    @classmethod
    def load_multiple_loggers(cls, logger_config: Tuple[Dict[str, Any]]):
        for logger in logger_config:
            cls.load_one_logger(logger)

    @classmethod
    def load_one_logger(cls, logger_config: Dict[str, Any]):
        logger_obj = AppLogger(logger_config)
        logger_name = logger_config['NAME']
        loaded_loggers[logger_name] = logger_obj
