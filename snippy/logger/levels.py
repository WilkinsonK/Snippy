import logging


class Level:
    '''Logging level object. Holds the integer value for a log level'''
    value: int


class DEBUG(Level):
    value = logging.DEBUG


class INFO(Level):
    value = logging.INFO


class WARNING(Level):
    value = logging.WARNING


class ERROR(Level):
    value = logging.ERROR


class CRITICAL(Level):
    value = logging.CRITICAL


class FATAL(Level):
    value = logging.FATAL


logger_levels = {
    'debug': DEBUG,
    'info': INFO,
    'warning': WARNING,
    'error': ERROR,
    'critical': CRITICAL,
    'fatal': FATAL
}
