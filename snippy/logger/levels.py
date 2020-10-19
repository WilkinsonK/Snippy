import logging


class Level:
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
