import unittest

from posterboard.tools import dictionary
from posterboard.core.commands import CommandObject, AbstractCommand, BaseCommand


class TestCommandObj(BaseCommand):
    name = 'testcommand'
    description = 'A testable command for unit testing'
    parameters = {
        ('text'): {
            'help': 'string of chars to echo back',
            'type': str,
            'nargs': '+',
            'default': ''
        }
    }

    def execute(self, argv):
        print(*argv.text)


class CommandsTestCase(unittest.TestCase):

    def test_command_obj_attrs(self):
        errors = 0
        attrs = ('name', 'description', 'parameters', 'is_cached')
