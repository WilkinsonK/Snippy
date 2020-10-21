import unittest

from logging import NullHandler, StreamHandler

from snippy.logger.loggers import AppLogger


class LoggerTests(unittest.TestCase):
    test_settings = ({
        'NAME': 'test_logger0A',
        'HANDLERS': ({
            'TYPE': StreamHandler,
            'FORMAT': "%(asctime)s - %(message)s",
            'LEVEL': 'debug'
        },)
    },
    {
        'NAME': 'test_logger0B',
        'HANDLERS': ({
            'TYPE': StreamHandler,
            'FORMAT': "§ %(message)s",
            'LEVEL': 'debug'
        },
        {
            'TYPE': NullHandler,
            'FORMAT': "# %(message)s",
            'LEVEL': 'info'
        })
    })

    def test_creating_one_logger(self):
        exception = None
        try:
            AppLogger(self.test_settings[0])
        except Exception as error:
            exception = error
            print(exception)
        self.assertIsNone(exception)

    def test_creating_multiple_loggers(self):
        exception = None
        try:
            for l in self.test_settings:
                AppLogger(l)
        except Exception as error:
            exception = error
            print(exception)
        self.assertIsNone(exception)
