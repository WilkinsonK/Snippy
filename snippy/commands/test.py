from snippy.core.commands import BaseCommand


class TestCommand(BaseCommand):
    name = 'test'
    description = 'run tests'
    parameters = {
        ('module'): {
            'help': 'test.py file to run tests from',
            'nargs': '+',
        },
        ('test'): {
            'help': 'specify tests to be run',
            'nargs': '*',
            'default': 'all'
        }
    }

    def execute(self, argv):
        pass
