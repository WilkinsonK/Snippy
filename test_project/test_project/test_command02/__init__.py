from snippy import BaseCommand


class TestCommand02(BaseCommand):
    parameters = {
        ('integer1'): {'action': 'store', 'help': 'first integer argument'},
        ('integer2'): {'action': 'store', 'help': 'second integer argument'}
    }

    def execute(self, args):
        pass
